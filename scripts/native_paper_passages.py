#!/usr/bin/env python3
"""Replace PDF text/math screenshots with checked HTML and native MathML.

The snippets below transcribe the *linked PDFs*, not a newer manuscript.
No article-wide replacement is made because the available LaTeX differs from
the published website version. Pandoc is used locally, without client scripts.
Run once on the original fragments; subsequent runs are harmless.
"""
from pathlib import Path
import subprocess
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parents[1]


def latex(fragment):
    result = subprocess.run(
        ['pandoc', '-f', 'latex', '-t', 'html5', '--mathml'],
        input=fragment, capture_output=True, text=True, check=True,
    )
    if result.stderr or 'class="math inline"' in result.stdout or 'class="math display"' in result.stdout:
        raise ValueError(result.stderr or 'Unrendered math')
    return result.stdout


def equation(tex, number=None):
    soup = BeautifulSoup(latex(r'\[' + tex + r'\]'), 'html.parser')
    math = soup.find('math')
    assert math and math.get('display') == 'block'
    label = f'<span class="equation-number">({number})</span>' if number else ''
    return '<div class="paper-equation">' + str(math) + label + '</div>'


def prose(tex):
    return latex(tex)


def apply(slug, replacements, cleanup=None):
    path = ROOT / 'content' / (slug + '.html')
    soup = BeautifulSoup(path.read_text(), 'html.parser')
    if soup.select_one('.native-passages'):
        print(slug, 'already converted')
        return
    images = list(soup.find_all('img'))
    for index, replacement in replacements.items():
        image = images[index - 1]
        wrapper = image.find_parent('figure') or image.parent
        assert len(wrapper.find_all('img')) == 1
        if wrapper.name == 'figure':
            details = wrapper.find_next_sibling()
            assert details and 'text-transcription' in details.get('class', [])
            details.decompose()
        rendered = BeautifulSoup(replacement, 'html.parser')
        wrapper.replace_with(rendered)
    if cleanup:
        cleanup(soup, images)
    soup.select_one('.article-text')['class'].append('native-passages')
    path.write_text(str(soup))
    print(slug, 'replaced', len(replacements), 'crops;', len(soup.find_all('img')), 'graphics retained')


def reflexivity():
    eq = {
        1: (r'F_i(u_i;w):=\mathbb{E}_{z\sim D(w)}\big[\ell_i(u_i;z)\big].', 1),
        2: (r'B_i(w):=\mathop{\mathrm{arg\,min}}_{u_i\in\mathcal{W}_i}F_i(u_i;w).', 2),
        4: (r'w_{t+1}=B(w_t),\qquad t=0,1,2,\ldots,', 3),
        6: (r'\|\nabla_{u_i}F_i(u_i;w)-\nabla_{u_i}F_i(u_i;w\prime)\|\le\sum_{j=1}^k a_{ij}\,\|w_j-w_j\prime\|.', None),
        7: (r'\|B_i(w)-B_i(w\prime)\|\le\sum_{j=1}^k\frac{a_{ij}}{\mu_i}\,\|w_j-w_j\prime\|.', None),
        9: (r'\|B_i(w)-B_i(w\prime)\|\le\sum_{j=1}^k\Gamma_{ij}\,\|w_j-w_j\prime\|.', 4),
        10: (r'\|B(w)-B(w\prime)\|_q\le\alpha\,\|w-w\prime\|_q\qquad\text{for all }w,w\prime\in\mathcal{W},', None),
        11: (r'\|x\|_q:=\max_{1\le i\le k}\frac{\|x_i\|}{q_i}.', None),
        12: (r'\sum_{j=1}^k\Gamma_{ij}\,q_j\le\alpha\,q_i\qquad\text{for every }i.', 5),
        13: (r'\|B_i(w)-B_i(w\prime)\|\le\sum_{j=1}^k\Gamma_{ij}\,q_j\,\|w-w\prime\|_q\le\alpha\,q_i\,\|w-w\prime\|_q.', None),
        14: (r'\|w_t-w^\star\|_q\le\alpha^t\,\|w_0-w^\star\|_q\qquad\text{for every }t\ge0.', None),
        16: (r'\widetilde{\mathrm{Reg}}_T:=\sum_{t=0}^{T-1}\sum_{i=1}^k\Big(F_i(w_{i,t};w_t)-F_i(B_i(w_t);w_t)\Big).', 6),
        17: (r'\widetilde{\mathrm{Reg}}_T\le\frac{C}{1-\alpha^2}\,\|w_0-w^\star\|_q^2\qquad\text{for every }T\ge1.', None),
        19: (r'F_i(w_{i,t};w_t)-F_i(B_i(w_t);w_t)\le\frac{L_i}{2}\,\|w_{i,t}-B_i(w_t)\|^2.', 7),
        20: (r'\|w_{i,t}-B_i(w_t)\|=\|B_i(w_{t-1})-B_i(w_t)\|\le\sum_{j=1}^k\Gamma_{ij}\,\|w_{j,t-1}-w_{j,t}\|,', None),
        21: (r'\|w_{i,t}-B_i(w_t)\|\le\Big(\sum_{j=1}^k\Gamma_{ij}q_j\Big)\|w_t-w_{t-1}\|_q.', None),
        22: (r'\sum_{i=1}^k\Big(F_i(w_{i,t};w_t)-F_i(B_i(w_t);w_t)\Big)\le C\prime\,\|w_t-w_{t-1}\|_q^2,', None),
        25: (r'\begin{aligned}\|w_t-w_{t-1}\|_q&\le\|w_t-w^\star\|_q+\|w_{t-1}-w^\star\|_q\\&\le(1+\alpha)\,\alpha^{t-1}\,\|w_0-w^\star\|_q,\end{aligned}', None),
        28: (r'\Gamma_\varepsilon:=(1+\varepsilon)\,vv^\top.', 8),
        29: (r'Y_t=\nu\Delta v+\Gamma_\varepsilon w_t+\xi_t,\qquad\xi_t\sim\mathcal{N}(0,\sigma_\varepsilon^2 I_k),', 9),
        30: (r'F_i(a;w,\nu)=\frac12\Big(a-\nu\Delta v_i-(\Gamma_\varepsilon w)_i\Big)^2+\frac{\sigma_\varepsilon^2}{2}.', 10),
        32: (r'w^{\star,\nu}=(I-\Gamma_\varepsilon)^{-1}\nu\Delta v=-\frac{\nu\Delta}{\varepsilon}\,v.', 11),
        33: (r'r_t^\nu:=\sum_{i=1}^k\Big(F_i(w_{i,t};w_t,\nu)-F_i(w_i^{\star,\nu};w^{\star,\nu},\nu)\Big),', 12),
        38: (r'P_\nu(Y_t\mid\mathcal{F}_t)=\mathcal{N}(\nu\Delta v+\Gamma_\varepsilon w_t,\sigma_\varepsilon^2I_k).', None),
        39: (r'\mathrm{KL}\big(P_+(Y_t\mid\mathcal{F}_t)\,\|\,P_-(Y_t\mid\mathcal{F}_t)\big)=\frac{\|2\Delta v\|^2}{2\sigma_\varepsilon^2}=\frac{2\Delta^2}{\sigma_\varepsilon^2}=\frac{\varepsilon}{4}.', None),
        40: (r'\mathrm{KL}(P_+^t\,\|\,P_-^t)=\frac{t\varepsilon}{4}.', 13),
        41: (r'\mathrm{TV}(P_+^t,P_-^t)\le\sqrt{\frac12\mathrm{KL}(P_+^t\,\|\,P_-^t)}\le\sqrt{\frac{t\varepsilon}{8}}\le\sqrt{1/16}=\frac14.', None),
        42: (r'\widehat\nu_t:=\mathop{\mathrm{arg\,min}}_{s\in\{-1,+1\}}\|w_t-w^{\star,s}\|.', None),
        44: (r'|\langle w_t-w^{\star,\nu},v\rangle|\ge\frac{\Delta}{\varepsilon}\qquad\text{on }\{\widehat\nu_t\ne\nu\}.', 14),
        45: (r'r_t^\nu=\frac12\|w_t-\nu\Delta v-\Gamma_\varepsilon w_t\|^2=\frac12\|(I-\Gamma_\varepsilon)(w_t-w^{\star,\nu})\|^2,', 15),
        47: (r'\mathbb{E}_\nu[r_t^\nu]\ge\frac{\Delta^2}{2}\,P_\nu(\widehat\nu_t\ne\nu).', None),
        48: (r'\frac12\mathbb{E}_+[r_t^+]+\frac12\mathbb{E}_-[r_t^-]\ge\frac{\Delta^2}{2}\cdot\frac12\Big(P_+(\widehat\nu_t\ne+1)+P_-(\widehat\nu_t\ne-1)\Big).', None),
        49: (r'\frac12\mathbb{E}_+[r_t^+]+\frac12\mathbb{E}_-[r_t^-]\ge\frac{p_0\Delta^2}{2}\qquad\text{for every }t\le c_0/\varepsilon.', None),
    }
    # Prime notation is an exponent in the PDF, including on profile vectors.
    replacements = {i: equation(t.replace(r'\prime', "'"), n) for i, (t, n) in eq.items()}
    passages = {
        3: r"Assumption 1 below ensures that this minimizer exists and is unique. The joint best-response map is $B(w):=\big(B_1(w),\ldots,B_k(w)\big)$. An equilibrium of the system is a profile that is consistent with every agent's best response.",
        5: r'\textbf{Assumption 1} (Strong convexity in own action). \emph{For each agent $i$ and every fixed deployed profile $w\in\mathcal{W}$, the map $u_i\mapsto F_i(u_i;w)$ is $\mu_i$-strongly convex on $\mathcal{W}_i$, with $\mu_i>0$.}',
        8: r"\emph{Proof.} Fix an agent $i$ and let $u_i:=B_i(w)$ and $u_i':=B_i(w')$. First-order optimality gives $\nabla_{u_i}F_i(u_i;w)=0$ and $\nabla_{u_i}F_i(u_i';w')=0$. Strong convexity of $F_i(\cdot;w)$ (Assumption 1) yields $\mu_i\|u_i-u_i'\|\le\|\nabla_{u_i}F_i(u_i;w)-\nabla_{u_i}F_i(u_i';w)\|$. Substituting the first optimality condition and then the second gives $\mu_i\|u_i-u_i'\|\le\|\nabla_{u_i}F_i(u_i';w)\|=\|\nabla_{u_i}F_i(u_i';w)-\nabla_{u_i}F_i(u_i';w')\|$. The right-hand side is a gradient difference at a fixed action $u_i'$ across two deployed profiles, which Assumption 2 bounds by $\sum_j a_{ij}\,\|w_j-w_j'\|$. Dividing by $\mu_i>0$ yields the claim. $\square$",
        15: r'\textbf{Assumption 4} (Smoothness in own action). \emph{For each agent $i$ and every fixed deployed profile $w$, the map $u_i\mapsto F_i(u_i;w)$ is $L_i$-smooth.}',
        18: r'\emph{Proof.} Fix $t\ge1$ and $i$. The best response $B_i(w_t)$ minimizes $u_i\mapsto F_i(u_i;w_t)$, which is $L_i$-smooth by Assumption 4. Standard smoothness gives',
        24: r"for a constant $C'$ absorbing the $L_i$ and the row-sum factors $\big(\sum_j\Gamma_{ij}q_j\big)^2$. By Corollary 5 and the triangle inequality,",
        26: r'so the per-round excess loss decays as $\alpha^{2(t-1)}$. Summing the geometric series from $t=1$ to $T-1$ gives a contribution of order $\|w_0-w^\star\|_q^2/(1-\alpha^2)$. For $t=0$, $\|w_0-B(w_0)\|_q\le\|w_0-w^\star\|_q+\|B(w^\star)-B(w_0)\|_q\le(1+\alpha)\|w_0-w^\star\|_q$, which fits the same geometric series. Combining yields the claim. $\square$',
        27: r"\textbf{Definition 7} (Decentralized local-information learner). \emph{A decentralized local-information learner is a policy profile $A=(A_1,\ldots,A_k)$ in which agent $i$'s action $w_{i,t}$ at round $t$ is measurable with respect to the private history $\mathcal{H}_{i,t}^{\mathrm{pre}}:=\sigma\big(w_{i,0:t-1},\;Y_{i,0:t-1},\;U_{i,0:t}\big)$, where $Y_{i,s}$ is agent $i$'s private observation at round $s$ and $U_{i,s}$ is agent $i$'s internal randomization.}",
        31: r'The additive constant $\sigma_\varepsilon^2/2$ cancels in differences and is dropped below. Minimizing over $a$ gives the best-response map $B(w;\nu)=\nu\Delta v+\Gamma_\varepsilon w$. The fixed-point equation $w^{\star,\nu}=B(w^{\star,\nu};\nu)$ has the explicit solution',
        34: r'\textbf{Theorem 8} (Linear lower bound in a supercritical family). \emph{There exist absolute constants $c_0,c_1>0$ such that the following holds. For every $\varepsilon\in(0,1]$, in the supercritical family defined by (8)--(9) with $\sigma_\varepsilon^2=8\Delta^2/\varepsilon$, every decentralized local-information learner $A$ satisfies}',
        36: r"\emph{Indistinguishability.} Conditional on the realized pre-observation history $\mathcal{F}_t$, the action $w_t$ is fixed by the learner's policy. Under the two hypotheses, the next observation is Gaussian with common covariance $\sigma_\varepsilon^2I_k$ and conditional means differing by $2\Delta v$. The per-round Kullback--Leibler divergence is therefore $\|2\Delta v\|^2/(2\sigma_\varepsilon^2)=2\varepsilon/C$ by the noise scaling. Chain rule and Pinsker's inequality give $\mathrm{TV}(P_+^t,P_-^t)<1/2$ for $t\le c_0/\varepsilon$ with $c_0=C/8$, so the minimax testing error is bounded below by an absolute constant $p_0>0$.",
        37: r"""\emph{Geometric cost of misidentification.} The two equilibria (11) lie at $\pm(\Delta/\varepsilon)v$, so on the event that the midpoint decoder picks the wrong sign, $|\langle w_t-w^{\star,\nu},v\rangle|\ge\Delta/\varepsilon$. The closed form $r_t^\nu=\tfrac12\|(I-\Gamma_\varepsilon)(w_t-w^{\star,\nu})\|^2$ together with $(I-\Gamma_\varepsilon)v=-\varepsilon v$ then gives $r_t^\nu\ge\Delta^2/2$ on that event. The factor $\varepsilon$ from the contraction of $(I-\Gamma_\varepsilon)$ along $v$ cancels exactly with the factor $1/\varepsilon$ from the equilibrium separation, which is why the obstruction survives the limit $\varepsilon\to0$ and produces a horizon of order $1/\varepsilon$.

Combining the two parts: averaging over $\nu$ and using minimax testing error at least $p_0$ gives $\tfrac12\mathbb{E}_+[r_t^+]+\tfrac12\mathbb{E}_-[r_t^-]\ge p_0\Delta^2/2$ for every $t\le c_0/\varepsilon$, and summing yields the claim with $c_1=p_0/2$. $\square$""",
        43: r"On the event $\{\widehat\nu_t\ne\nu\}$, the action $w_t$ lies strictly closer to the incorrect equilibrium than to the correct one. Using (11), the two equilibria lie on opposite sides of the origin along $v$ at distance $\Delta/\varepsilon$ each. The midpoint between them is the origin, so $\widehat\nu_t\ne\nu$ implies that the projection of $w_t$ onto $v$ has the same sign as $\nu$. Consequently,",
    }
    replacements.update({i: prose(t) for i,t in passages.items()})
    replacements[35] = (
        equation(r'\frac12\mathbb{E}_+[\mathrm{Reg}_T^+(A)]+\frac12\mathbb{E}_-[\mathrm{Reg}_T^-(A)]\ge c_1\,\Delta^2\,T\qquad\text{for every }T\le c_0/\varepsilon.')
        + '<p><em>In particular,</em></p>'
        + equation(r'\sup_{\nu\in\{-1,+1\}}\mathbb{E}_\nu[\mathrm{Reg}_T^\nu(A)]\ge c_1\,\Delta^2\,T\qquad\text{for every }T\le c_0/\varepsilon.')
    )
    replacements[46] = (
        equation(r'\|(I-\Gamma_\varepsilon)(w_t-w^{\star,\nu})\|\ge|\langle(I-\Gamma_\varepsilon)(w_t-w^{\star,\nu}),v\rangle|=\varepsilon\,|\langle w_t-w^{\star,\nu},v\rangle|,')
        + '<p>and substituting (14),</p>'
        + equation(r'\|(I-\Gamma_\varepsilon)(w_t-w^{\star,\nu})\|\ge\varepsilon\cdot\frac{\Delta}{\varepsilon}=\Delta\qquad\text{on }\{\widehat\nu_t\ne\nu\}.')
        + '<p>Substituting into (15) yields</p>'
        + equation(r'r_t^\nu\ge\frac{\Delta^2}{2}\qquad\text{on }\{\widehat\nu_t\ne\nu\}.',16)
    )
    assert set(replacements) == set(range(1,50)) - {23}

    def cleanup(soup, images):
        # These lines are both inside an over-wide PDF crop and its extracted
        # text. Restore each once in the correct position, including lost math.
        for p in list(soup.find_all('p')):
            text = p.get_text(' ',strip=True)
            if text.startswith('and the cumulative excess loss over'):
                p.replace_with(BeautifulSoup(prose(r'and the cumulative excess loss over $T$ rounds is $\mathrm{Reg}_T^\nu(A):=\sum_{t=0}^{T-1}r_t^\nu$.'),'html.parser'))
            if text in ('In particular,','and substituting (14),','Substituting into (15) yields'):
                # Keep only the inserted copy, identified by no trailing space.
                if p.contents and str(p.contents[-1]).endswith(' '):
                    p.decompose()
        # The old <em>In particular,</em> has trailing whitespace after <em>.
        copies=[p for p in soup.find_all('p') if p.get_text(strip=True)=='In particular,']
        for p in copies[1:]:p.decompose()
    apply('reflexivity-threshold', replacements, cleanup)


def emojis():
    replacements = {
        1: '<p>Each emoji is assigned a unique code in the Unicode encoding system, similar to characters such as letters. For instance, the letter “A” is assigned the Unicode codepoint U+0041, whereas the emoji 🚀 is assigned U+1F680. Whereas this, in theory, allows them to be displayed consistently across different devices and platforms, in practice, their appearance may vary due to font, software, and device differences.</p>',
        2: '<div class="table-scroll" role="region" aria-label="Different ways to use emojis" tabindex="0"><table class="article-table"><thead><tr><th scope="col">Usage</th><th scope="col">Example</th></tr></thead><tbody><tr><td>emphasizing text</td><td>What a great market! 🚀</td></tr><tr><td>substituting text</td><td>What a 🚀 market!</td></tr><tr><td>contradicting text</td><td>What a great market! 💩 🩸 📉</td></tr></tbody></table></div>',
        5: '<div class="table-scroll" role="region" aria-label="Stocks and cryptocurrencies in the data set" tabindex="0"><table class="article-table"><thead><tr><th scope="col">Symbol</th><th scope="col">S&amp;P 500</th><th scope="col">Bitcoin</th><th scope="col">Dogecoin</th><th scope="col">Apple</th><th scope="col">GameStop</th><th scope="col">Shiba Inu</th><th scope="col">Others</th></tr></thead><tbody><tr><th scope="row">Number of Posts</th><td>6,067,248</td><td>2,803,824</td><td>2,236,581</td><td>1,897,368</td><td>1,386,519</td><td>1,220,177</td><td>2,945,419</td></tr><tr><th scope="row">Percentage</th><td>33%</td><td>15%</td><td>12%</td><td>10%</td><td>7%</td><td>7%</td><td>16%</td></tr></tbody></table></div>',
        9: '<p>The green “emoji cloud” diagram in Fig. 3 shows the emojis present in the posts labeled bullish by the poster, with the emoji size reflecting the frequency of the emoji. The larger the emoji, the higher the number of Tweets in which it is mentioned. Many of the larger emojis in the diagram clearly show a bullish sentiment such as 🔥 (fire, symbolizing that the market is “heating up”), 💎 (gem-stone, symbolizing that an asset is valuable), 🚀 (rocket, symbolizing that the market is going up), 🤑 (money-mouth-face, symbolizing that the poster is excited about making money), and 📈 (chart with upwards trend). Many of these emojis are much less used in non-financial contexts.</p>',
        10: '<p>The red “emoji cloud” in Fig. 3 shows the emojis used in Tweets labeled as bearish by the poster. Some of the prominent emojis that most likely carry a bearish sentiment include 🐻 (bear-face), 🩸 (drop of blood, symbolizing losing or “bleeding”), 📉 (chart with downwards trend), 🚨 (police car revolving light, symbolizing an emergency or a crisis), and 💩 (pile of poo). Note that the posts labeled as bearish by users include some clearly bullish emojis, such as 🤑 or 📈, albeit at a lower frequency compared to the posts labeled as bullish.</p>',
        11: '<p>emojis at a higher frequency in the “emoji cloud”. However, some emojis seem to be larger than both the bullish and the bearish “emoji cloud”, such as 🤷 (shrug emoji), 😆 (grinning squinting face) and 🙄 (face with rolling eyes). Note that some of the emojis present in the emoji clouds are modifiers such as 🏿 (skin-tone modifier) or ♂️ (gender modifier). Emoji modifiers are added on top of original emojis in order to change certain characteristics such as the skin tone or gender of the emoji. Some emojis, such as 😂, are popular among internet users in general and not just in a financial context [61].</p>',
        13: '<blockquote class="text-example"><p>—&gt; and ✔ weren’t decoded correctly.<br>Let’s use ftfy 🌠 to fix that…</p></blockquote>',
        15: '',
        17: '',
    }

    def cleanup(soup, images):
        for p in list(soup.find_all('p')):
            text = p.get_text(' ',strip=True)
            if text.startswith('Symbol S&P 500 Bitcoin Dogecoin Apple GameStop'):
                p.decompose()  # Text extraction of the same table, already restored.
        # The source's (a)/(b) panel labels remain as native text immediately
        # below the corresponding two-panel plots.
    apply('financial-microblog-emojis', replacements, cleanup)


def reflexivity_figure():
    """Retain exact PDF plot vectors while making their captions native text."""
    import pymupdf
    path = ROOT / 'content' / 'reflexivity-threshold.html'
    soup = BeautifulSoup(path.read_text(), 'html.parser')
    image = soup.find('img', alt=lambda a: a and a.startswith('Figure 1: complete reflexivity-threshold'))
    if image is None:
        return
    pdf = pymupdf.open(ROOT / 'docs/papers/reflexivity-threshold/paper.pdf')
    page = pdf[6]
    page.set_cropbox(pymupdf.Rect(107.5, 68, 505.5, 199))
    folder = ROOT / 'docs/papers/reflexivity-threshold/figures'
    folder.mkdir(exist_ok=True)
    (folder / 'threshold-plots.svg').write_text(page.get_svg_image())
    image['src'] = 'figures/threshold-plots.svg'
    image['alt'] = 'The reflexivity threshold: retraining steps versus spectral radius (a) and normalized distance to equilibrium over iterations (b). Original plot vectors from the linked PDF.'
    figure = image.find_parent('figure')
    figure['class'] = ['paper-figure']
    caption = figure.find('figcaption')
    caption.insert(0, BeautifulSoup(prose(r'\textbf{(b)} Normalized distance to equilibrium (log scale) under repeated retraining. Subcritical instances contract geometrically, while the plotted supercritical instances move away from equilibrium. The non-normal subcritical curve shows transient growth before contraction.'), 'html.parser'))
    caption.insert(0, BeautifulSoup(prose(r'\textbf{(a)} Number of retraining steps needed to satisfy $\|w_t-w^\star\|_q\le\delta$. Convergence slows sharply as $\rho(\Gamma)$ approaches 1 from below. Supercritical $\rho$ values are not plotted as iterates do not converge within the 1,000-iteration cap.'), 'html.parser'))
    path.write_text(str(soup))


if __name__ == '__main__':
    reflexivity()
    emojis()
    reflexivity_figure()
