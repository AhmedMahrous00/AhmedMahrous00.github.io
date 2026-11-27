# The reflexivity threshold: A phase transition for multi-agent performative prediction

Source: [https://amahrous.com/papers/reflexivity-threshold/](https://amahrous.com/papers/reflexivity-threshold/)

[← Ahmed Mahrous’s homepage](https://amahrous.com/#research)

Ahmed Mahrous and [Roberto Di Pietro](https://cemse.kaust.edu.sa/profiles/roberto-di-pietro)

*NeurIPS 2026 · Accepted* · 2026 · ICORE A\*

[PDF](https://amahrous.com/papers/reflexivity-threshold/paper.pdf) · [Read full text](https://amahrous.com/papers/reflexivity-threshold/#full-text) · [BibTeX](https://amahrous.com/papers/reflexivity-threshold/citation.bib) · [arXiv](https://arxiv.org/abs/2610.29577) · [Simulation code](https://github.com/AhmedMahrous00/reflexivity-threshold) · [Cite](https://amahrous.com/papers/reflexivity-threshold/#citation)

## TL;DR

Under the stated sensitivity and curvature assumptions, a reflexivity matrix with spectral radius below one guarantees convergence of repeated retraining. Above one, we construct noisy systems where every local-information learner incurs expected cumulative excess loss growing linearly for horizons up to order 1/(ρ(Γ) − 1).

## Abstract

Many learning systems are performative: once deployed, their predictions change the data distribution on which future models are trained. In multi-agent settings, this feedback is routed through a network of interacting learners, so stability depends not only on the strength of performativity but also on who affects whom. We study repeated retraining in multi-agent performative prediction and identify a spectral threshold that separates stable learning from worst-case learning obstruction. Prior work often collapses cross-agent feedback into a scalar contraction constant, missing this network structure. We instead introduce the reflexivity matrix Γ, which records how strongly one agent’s deployment can move another agent’s best response, defined from per-agent gradient sensitivities and curvature parameters. The threshold occurs when the spectral radius of this matrix crosses one. Below the threshold, repeated retraining converges geometrically to a unique performatively stable equilibrium, with cumulative excess loss bounded uniformly in the time horizon. Above the threshold, we construct noisy supercritical instances in which every local-information learner incurs expected cumulative excess loss growing linearly for horizons up to order 1/(ρ(Γ) − 1). Together, these results characterize the threshold behavior through upper and lower bounds and recover the single-agent scalar threshold from prior work as a special case.

## Citation

Ahmed Mahrous and Roberto Di Pietro. 2026. The reflexivity threshold: A phase transition for multi-agent performative prediction. Advances in Neural Information Processing Systems.

```bibtex
@inproceedings{reflexivity-threshold-2026,
  author = {Mahrous, Ahmed and Di Pietro, Roberto},
  title = {{The reflexivity threshold: A phase transition for multi-agent performative prediction}},
  year = {2026},
  booktitle = {Advances in Neural Information Processing Systems},
  note = {Accepted at NeurIPS 2026},
  url = {https://arxiv.org/abs/2610.29577}
}
```

## Full text

### 1 Introduction

Many learning systems, once deployed, change the environment that later generates their training data. A credit scoring model can change how applicants behave; an algorithmic trading strategy can move the price data on which future strategies are trained. This feedback effect is the focus of performative prediction. Existing theory largely studies the case of one learner facing the consequences of its own deployment. Many real systems, however, contain multiple learners whose deployments *jointly* shape the environment.

The multi-agent setting is not simply a larger version of the single-agent problem; it introduces different difficulties. Feedback can travel across agents: one agent’s deployment changes the data distribution, which changes another agent’s retraining problem, which may itself affect the data distribution or other agents. Stability therefore depends not only on the overall strength of performativity, but also on how feedback is routed through the agent network.

We ask whether there is a general threshold separating stable multi-agent performative learning from unavoidable learning failure. When does repeated retraining converge to a stable equilibrium?

We answer this question through a reflexivity matrix $\Gamma$ with entries $\Gamma_{ij}:=a_{ij}/\mu_{i}$, measuring how strongly agent $j$’s deployment can move agent $i$’s best response, after normalizing by the curvature of agent $i$’s objective. Thus $\Gamma$ records who affects whom, and how strongly, in the performative feedback network.

Our main result is a phase transition at $\rho(\Gamma)=1$, where $\rho(\Gamma)$ is the spectral radius of $\Gamma$. This quantity captures the largest asymptotic amplification factor of the feedback network. If $\rho(\Gamma)<1$, cross-agent feedback dissipates: repeated retraining is a contraction in a Perron–Frobenius weighted norm, converges geometrically to a unique performatively stable equilibrium, and incurs bounded cumulative excess loss. Above the threshold, this positive guarantee cannot be extended. We construct supercritical systems in which every decentralized local-information learner suffers cumulative loss that grows linearly with time, regardless of the retraining rule. Under sensitivity and curvature assumptions, the spectral radius of the reflexivity matrix gives a sharp boundary for general stability guarantees: below one, all systems satisfying our assumptions contract, while above one, there exist supercritical systems for which decentralized learning incurs linear cumulative loss.

#### Contributions.

First, we introduce the reflexivity matrix $\Gamma$, a nonnegative matrix whose entry $\Gamma_{ij}$ records how strongly agent $j$’s deployment can move agent $i$’s best response, as determined by per-agent gradient sensitivities and curvature constants. We prove an entrywise best-response sensitivity bound that reduces nonlinear retraining dynamics with general strongly convex losses to a spectral comparison through $\Gamma$, making Perron–Frobenius theory available. Second, we prove the subcritical side of the threshold: if $\rho(\Gamma)<1$, repeated retraining is a contraction in a Perron–Frobenius weighted norm, yielding a unique performatively stable equilibrium, geometric convergence from any initialization, and cumulative dynamic excess loss bounded uniformly in the time horizon. Third, we prove the supercritical side: for a rank-one family with $\rho(\Gamma)=1+\varepsilon$, every decentralized local-information learner incurs cumulative excess loss $\Omega(\Delta^{2}T)$ over horizons $T=O(1/\varepsilon)$. Together, these results identify $\rho(\Gamma)=1$ as a boundary for general stability guarantees under primitive gradient-sensitivity and curvature assumptions, and recover the single-agent scalar threshold from prior work when $k=1$.

### 2 Related Work

This paper draws on three lines of research. The first is the single-agent theory of performative prediction, which introduces the framework we extend. The second is the multi-agent theory of performative prediction and decision-dependent games, which is where our contribution is most directly positioned. The third is the combined tradition of spectral methods for network games and statistical lower bound techniques, from which we import two standard technical tools.

#### Performative prediction.

[Perdomo et al. (2020)](https://amahrous.com/papers/reflexivity-threshold/#bib.bib16) introduced performative prediction in a single-agent setting, formalizing performative stability and convergence of repeated retraining under sensitivity conditions. Subsequent work largely retained this single-agent viewpoint while extending the framework to stochastic, causal, nonconvex, and sequential settings ([Mendler-Dünner et al., 2020](https://amahrous.com/papers/reflexivity-threshold/#bib.bib11); [Miller et al., 2021](https://amahrous.com/papers/reflexivity-threshold/#bib.bib12); [Brown et al., 2022](https://amahrous.com/papers/reflexivity-threshold/#bib.bib4); [Hardt et al., 2022](https://amahrous.com/papers/reflexivity-threshold/#bib.bib8); [Mofakhami et al., 2023](https://amahrous.com/papers/reflexivity-threshold/#bib.bib13); [Mandal et al., 2023](https://amahrous.com/papers/reflexivity-threshold/#bib.bib10)). Closest to our threshold result, [Anagnostides et al. (2026)](https://amahrous.com/papers/reflexivity-threshold/#bib.bib1) established hardness and lower bounds at the single-agent scalar threshold. We depart from this line by studying decentralized multi-agent retraining, where performative feedback is cross-agent and the scalar threshold is replaced by the spectral condition $\rho(\Gamma)=1$.

#### Multi-agent performativity.

The multi-agent extension is the most direct predecessor of our work, and the literature divides into three strands.

The first establishes scalar contraction conditions for convergence. [Narang et al. (2023)](https://amahrous.com/papers/reflexivity-threshold/#bib.bib14) formalized $n$-player performative prediction with a scalar aggregate threshold $\rho<1$, and analogous scalar conditions appear in cooperative consensus learning ([Li et al., 2022](https://amahrous.com/papers/reflexivity-threshold/#bib.bib9)), decentralized games with coupled constraints ([Yan and Cao, 2024](https://amahrous.com/papers/reflexivity-threshold/#bib.bib21)), and a Wasserstein-free variant ([Zhong et al., 2025](https://amahrous.com/papers/reflexivity-threshold/#bib.bib22)). We depart from this strand on two axes. We replace the scalar aggregate with a matrix $\Gamma$ that preserves per-agent-pair feedback, and we pair the upper bound with a worst-case information-theoretic lower bound above the threshold.

The second develops spectral characterizations in special models. [Wang et al. (2023)](https://amahrous.com/papers/reflexivity-threshold/#bib.bib20) derived a necessary-and-sufficient spectral condition for a linear-quadratic mean-squared-error model on multiplex networks. Their spectral object is a weighted adjacency matrix with exogenous structure, and the condition is specific to the linear-quadratic model. Our $\Gamma$ is built from primitive per-agent quantities, applies to general strongly convex losses, and is paired with a lower bound.

The third identifies dynamical phase transitions. [Piliouras and Yu (2023)](https://amahrous.com/papers/reflexivity-threshold/#bib.bib17) proved a transition from stability to Li–Yorke chaos as update aggressiveness grows under scalar aggregate influence. Their threshold is dynamical and concerns the long-run behavior of specific update rules; ours is information-theoretic and applies to every decentralized local-information learner. [Farina and Perdomo (2026)](https://amahrous.com/papers/reflexivity-threshold/#bib.bib7) show that, for bounded losses, no-regret online learning yields approximate performative stability of a mixture over joint deployment histories, without regularity assumptions on the distribution maps. Our subcritical result guarantees geometric convergence of the last retraining iterate to a unique performatively stable equilibrium under curvature and sensitivity assumptions.

#### Spectral methods and lower bounds.

Two technical traditions supply tools used in our analysis without serving as competing frameworks. Spectral conditions for equilibrium uniqueness and stability are well established in network games ([Ballester et al., 2006](https://amahrous.com/papers/reflexivity-threshold/#bib.bib2); [Bramoullé et al., 2014](https://amahrous.com/papers/reflexivity-threshold/#bib.bib3); [Parise and Ozdaglar, 2019](https://amahrous.com/papers/reflexivity-threshold/#bib.bib15)), where the spectral radius governs payoff coupling: agent $j$’s action enters agent $i$’s utility directly. In our setting, it governs distributional feedback through $D(w)$, and $\Gamma$ is built from gradient sensitivities and curvature constants rather than payoff coefficients. Our lower bound uses the two-point method ([Tsybakov, 2009](https://amahrous.com/papers/reflexivity-threshold/#bib.bib19)); recent extensions to interactive ([Chen et al., 2024](https://amahrous.com/papers/reflexivity-threshold/#bib.bib5)) and decision-dependent ([Cutler et al., 2024](https://amahrous.com/papers/reflexivity-threshold/#bib.bib6)) settings do not cover our performative learning setting. Our construction is tailored to multi-agent performative feedback over a finite horizon.

### 3 Model

This section specifies the multi-agent performative prediction model used throughout the paper. We describe the agents, their objectives, the dynamics of repeated retraining, and the assumptions that underlie the reduction of Section [4](https://amahrous.com/papers/reflexivity-threshold/#S4).

There are $k$ agents. Each agent $i\in\{1,\dots,k\}$ chooses a deployment $w_{i}$ from a feasible set $\mathcal{W}_{i}=\mathbb{R}^{d_{i}}$. The joint deployment profile is $w:=(w_{1},\dots,w_{k})\in\mathcal{W}:=\mathcal{W}_{1}\times\cdots\times\mathcal{W}_{k}$. The deployed profile induces a shared endogenous distribution $D(w)$ over observations $z\in\mathcal{Z}$. This distribution represents the data-generating process that all agents face after the profile $w$ has been deployed. The dependence of $D$ on $w$ captures the performative nature of the system: the environment that agents observe is shaped by their own collective actions.

Each agent $i$ has a loss function $\ell_{i}:\mathcal{W}_{i}\times\mathcal{Z}\to\mathbb{R}$ and aims to minimize its performative risk

<table> <tbody><tr> <td></td> <td>$$F_{i}(u_{i};w)\;:=\;\mathbb{E}_{z\sim D(w)}\big[\ell_{i}(u_{i};z)\big].$$</td> <td></td> <td rowspan="1">(1)</td></tr></tbody> </table>

The two arguments of $F_{i}$ play distinct roles. The first, $u_{i}$, is the candidate action optimized by agent $i$. The second, $w$, is the deployed profile that determines the environment through $D(w)$. Retraining couples these roles by replacing the deployed profile with agents’ optimized actions.

For each agent $i$ and each deployed profile $w$, the best response is

<table> <tbody><tr> <td></td> <td>$$B_{i}(w)\;:=\;\argmin_{u_{i}\in\mathcal{W}_{i}}F_{i}(u_{i};w).$$</td> <td></td> <td rowspan="1">(2)</td></tr></tbody> </table>

Assumption [1](https://amahrous.com/papers/reflexivity-threshold/#Thmassumption1) below ensures that this minimizer exists and is unique. The joint best-response map is $B(w):=\big(B_{1}(w),\dots,B_{k}(w)\big)$. An equilibrium of the system is a profile that is consistent with every agent’s best response.

###### Definition 1 (Performatively stable equilibrium).

A profile $w^{\star}\in\mathcal{W}$ is a *performatively stable equilibrium* if $w^{\star}=B(w^{\star})$.

At a performatively stable equilibrium, each agent’s deployed action is optimal for the distribution induced by the joint deployment. Existence of such an equilibrium is not assumed; it is derived in Section [5](https://amahrous.com/papers/reflexivity-threshold/#S5) as a consequence of the spectral condition on the reflexivity matrix.

We study the repeated retraining dynamics in which every agent simultaneously replaces its current deployment with its best response,

<table> <tbody><tr> <td></td> <td>$$w_{t+1}=B(w_{t}),\qquad t=0,1,2,\dots,$$</td> <td></td> <td rowspan="1">(3)</td></tr></tbody> </table>

with initialization $w_{0}\in\mathcal{W}$. The central question of the paper is when the sequence $\{w_{t}\}$ converges to a performatively stable equilibrium, and when convergence fails.

#### Main assumptions.

Three assumptions are used throughout the paper. The first two are local to individual agents and enter the reduction of Section [4](https://amahrous.com/papers/reflexivity-threshold/#S4). The third is a mild regularity condition on the feasible sets that allows application of Banach’s fixed-point theorem.

###### Assumption 1 (Strong convexity in own action).

For each agent $i$ and every fixed deployed profile $w\in\mathcal{W}$, the map $u_{i}\mapsto F_{i}(u_{i};w)$ is $\mu_{i}$-strongly convex on $\mathcal{W}_{i}$, with $\mu_{i}>0$.

Strong convexity makes $B_{i}(w)$ unique and quantifies agent $i$’s resistance to gradient perturbations. Larger $\mu_{i}$ means that the best response is less sensitive to changes in the data distribution.

###### Assumption 2 (Gradient sensitivity to the deployed profile).

For each $i$, $F_{i}$ is continuously differentiable in $u_{i}$, and there exist nonnegative constants $a_{ij}\geq 0$ for all $i,j\in\{1,\dots,k\}$ such that for every agent $i$, every candidate action $u_{i}\in\mathcal{W}_{i}$, and every pair of deployed profiles $w,w^{\prime}\in\mathcal{W}$,

<table> <tbody><tr> <td></td> <td>$$\|\nabla_{u_{i}}F_{i}(u_{i};w)-\nabla_{u_{i}}F_{i}(u_{i};w^{\prime})\|\;\leq\;\sum_{j=1}^{k}a_{ij}\,\|w_{j}-w_{j}^{\prime}\|.$$</td> <td></td></tr></tbody> </table>

Gradient sensitivity quantifies how a change in the deployed profile affects each agent’s first-order condition. The coefficient $a_{ij}$ measures how much agent $j$’s deployment disturbs agent $i$’s gradient. If agent $j$ has no effect on agent $i$’s optimization problem, then $a_{ij}=0$. Larger values of $a_{ij}$ indicate stronger cross-agent coupling. The diagonal coefficient $a_{ii}$ captures agent $i$’s own self-reflexive effect through the environment.

Assumptions [1](https://amahrous.com/papers/reflexivity-threshold/#Thmassumption1) and [2](https://amahrous.com/papers/reflexivity-threshold/#Thmassumption2) are the only two channels through which agents interact mathematically in this paper. Every downstream result is derived from these two assumptions and their combination in Section [4](https://amahrous.com/papers/reflexivity-threshold/#S4). The reflexivity matrix $\Gamma$ of Section [4](https://amahrous.com/papers/reflexivity-threshold/#S4) is built from exactly the parameters $\{\mu_{i}\}$ and $\{a_{ij}\}$ introduced here.

###### Assumption 3 (Unconstrained domains).

Each feasible set is $\mathcal{W}_{i}=\mathbb{R}^{d_{i}}$.

This makes $\mathcal{W}$ complete under the norms used below, enabling Banach’s fixed-point theorem, and ensures that retraining stays in $\mathcal{W}$.

Throughout, $x_{i}$ denotes agent $i$’s block of a vector $x\in\mathbb{R}^{d_{1}}\times\cdots\times\mathbb{R}^{d_{k}}$, with Euclidean norm $\|\cdot\|$. The spectral radius of $M$ is $\rho(M)$, and for $q\in\mathbb{R}_{++}^{k}$ we write $\|x\|_{q}:=\max_{i}\|x_{i}\|/q_{i}$.

### 4 The Reduction: From Retraining Dynamics to $\Gamma$

The retraining dynamics $w_{t+1}=B(w_{t})$ are nonlinear and couple all $k$ agents through the shared endogenous distribution $D(w)$. Direct analysis of these dynamics is difficult without additional structure. This section introduces the reduction used throughout the paper: under the assumptions of Section [3](https://amahrous.com/papers/reflexivity-threshold/#S3), changes in the nonlinear map $B$ are bounded entrywise by a nonnegative matrix $\Gamma$. The spectral properties of $\Gamma$ can therefore be used to bound the dynamics of $B$.

The first step bounds the shift in any agent’s best response induced by a shift in the deployed profile. The bound is linear and decomposes cleanly across agents.

###### Theorem 2 (Best-response sensitivity).

Under Assumptions [1](https://amahrous.com/papers/reflexivity-threshold/#Thmassumption1)–[2](https://amahrous.com/papers/reflexivity-threshold/#Thmassumption2) and [3](https://amahrous.com/papers/reflexivity-threshold/#Thmassumption3), for every agent $i$ and every pair of deployed profiles $w,w^{\prime}$,

<table> <tbody><tr> <td></td> <td>$$\|B_{i}(w)-B_{i}(w^{\prime})\|\;\leq\;\sum_{j=1}^{k}\frac{a_{ij}}{\mu_{i}}\,\|w_{j}-w_{j}^{\prime}\|.$$</td> <td></td></tr></tbody> </table>

###### Proof.

Fix an agent $i$ and let $u_{i}:=B_{i}(w)$ and $u_{i}^{\prime}:=B_{i}(w^{\prime})$. First-order optimality gives $\nabla_{u_{i}}F_{i}(u_{i};w)=0$ and $\nabla_{u_{i}}F_{i}(u_{i}^{\prime};w^{\prime})=0$. Strong convexity of $F_{i}(\cdot;w)$ (Assumption [1](https://amahrous.com/papers/reflexivity-threshold/#Thmassumption1)) yields $\mu_{i}\|u_{i}-u_{i}^{\prime}\|\leq\|\nabla_{u_{i}}F_{i}(u_{i};w)-\nabla_{u_{i}}F_{i}(u_{i}^{\prime};w)\|$. Substituting the first optimality condition and then the second gives $\mu_{i}\|u_{i}-u_{i}^{\prime}\|\leq\|\nabla_{u_{i}}F_{i}(u_{i}^{\prime};w)\|=\|\nabla_{u_{i}}F_{i}(u_{i}^{\prime};w)-\nabla_{u_{i}}F_{i}(u_{i}^{\prime};w^{\prime})\|$. The right-hand side is a gradient difference at a fixed action $u_{i}^{\prime}$ across two deployed profiles, which Assumption [2](https://amahrous.com/papers/reflexivity-threshold/#Thmassumption2) bounds by $\sum_{j}a_{ij}\,\|w_{j}-w_{j}^{\prime}\|$. Dividing by $\mu_{i}>0$ yields the claim. ∎

The proof uses each structural assumption once: gradient sensitivity bounds the performative change in agent $i$’s gradient, and strong convexity converts it into a best-response change. Their interaction appears only through $a_{ij}/\mu_{i}$, the ratio of agent $j$’s disturbance to agent $i$’s curvature, which measures how much $j$ can shift $i$’s best response.

The weights in Theorem [2](https://amahrous.com/papers/reflexivity-threshold/#Thmtheorem2) define the central object of the paper.

###### Definition 3 (Reflexivity matrix).

The *reflexivity matrix* is the $k\times k$ nonnegative matrix $\Gamma$ with entries $\Gamma_{ij}:=a_{ij}/\mu_{i}$, for $i,j=1,\dots,k$.

In terms of $\Gamma$, Theorem [2](https://amahrous.com/papers/reflexivity-threshold/#Thmtheorem2) states that for every $i$ and every $w,w^{\prime}$,

<table> <tbody><tr> <td></td> <td>$$\|B_{i}(w)-B_{i}(w^{\prime})\|\;\leq\;\sum_{j=1}^{k}\Gamma_{ij}\,\|w_{j}-w_{j}^{\prime}\|.$$</td> <td></td> <td rowspan="1">(4)</td></tr></tbody> </table>

The vector of best-response shifts is therefore dominated entrywise by the product of $\Gamma$ with the vector of action shifts.

The matrix $\Gamma$ is the central reduction object. It is built from primitive per-agent quantities rather than imposed as an aggregate Lipschitz constant, and its nonnegativity makes Perron–Frobenius theory available for the weighted-norm contraction argument below. The rank-one construction in Section [6](https://amahrous.com/papers/reflexivity-threshold/#S6) saturates ([4](https://amahrous.com/papers/reflexivity-threshold/#S4.E4)) along the Perron direction, so the same spectral radius governs both the upper and lower sides of the threshold.

For a direct comparison with [Narang et al. (2023)](https://amahrous.com/papers/reflexivity-threshold/#bib.bib14), consider scalar agents with quadratic losses $\ell_{i}(u_{i};z_{i})=\tfrac{1}{2}(u_{i}-z_{i})^{2}$ and deterministic observations $z=Cw$, where $C\geq 0$. Here $\mu_{i}=1$, the data-gradient Lipschitz constants are $\beta_{i}=1$, and the full-profile Wasserstein sensitivities are $\gamma_{i}=\|C_{i:}\|_{2}$. Their scalar aggregate condition becomes $\sqrt{\sum_{i}\gamma_{i}^{2}}=\|C\|_{F}<1$, whereas ours is $\rho(C)<1$, since $\Gamma=C$. Because $\rho(C)\leq\|C\|_{F}$, our certificate is never more restrictive in this common subclass and can be strictly stronger. For example, if $C=cP$ with $P$ a cyclic permutation matrix, then $\rho(C)=c$ but $\|C\|_{F}=c\sqrt{k}$. Thus, for $k^{-1/2}<c<1$, the matrix condition certifies convergence while the scalar aggregate condition does not.

### 5 Subcritical Regime: Contraction and Bounded Excess Loss

This section proves the positive side of the threshold. Under the assumptions of Section [3](https://amahrous.com/papers/reflexivity-threshold/#S3), if $\rho(\Gamma)<1$, then the retraining map is a contraction in a Perron–Frobenius weighted norm. This yields a unique performatively stable equilibrium, geometric convergence from any initialization, and a cumulative excess-loss bound that does not grow with the time horizon.

#### Contraction via Perron–Frobenius.

For two retraining trajectories $w_{t}$ and $w^{\prime}_{t}$, let $d_{i,t}:=\|w_{i,t}-w^{\prime}_{i,t}\|$. Inequality ([4](https://amahrous.com/papers/reflexivity-threshold/#S4.E4)) gives $d_{t+1}\leq\Gamma d_{t}$ entrywise, hence $d_{t}\leq\Gamma^{t}d_{0}$. Since $\rho(\Gamma)<1$, the matrix powers vanish, directly explaining why deviations decay. Perron–Frobenius theory supplies positive weights $q$ with $\Gamma q\leq\alpha q$ for some $\alpha<1$, converting this matrix comparison into a one-step contraction in $\|\cdot\|_{q}$ and allowing Banach’s theorem to establish existence and uniqueness of the equilibrium.

###### Theorem 4 (Weighted contraction below threshold).

Suppose Assumptions [1](https://amahrous.com/papers/reflexivity-threshold/#Thmassumption1)–[2](https://amahrous.com/papers/reflexivity-threshold/#Thmassumption2) and [3](https://amahrous.com/papers/reflexivity-threshold/#Thmassumption3) hold, and $\rho(\Gamma)<1$. Then there exist a positive vector $q\in\mathbb{R}^{k}_{++}$ and a constant $\alpha\in(0,1)$ such that

<table> <tbody><tr> <td></td> <td>$$\|B(w)-B(w^{\prime})\|_{q}\;\leq\;\alpha\,\|w-w^{\prime}\|_{q}\qquad\text{for all }w,w^{\prime}\in\mathcal{W},$$</td> <td></td></tr></tbody> </table>

where the weighted norm is defined by

<table> <tbody><tr> <td></td> <td>$$\|x\|_{q}\;:=\;\max_{1\leq i\leq k}\frac{\|x_{i}\|}{q_{i}}.$$</td> <td></td></tr></tbody> </table>

###### Proof.

Since $\Gamma$ is nonnegative and $\rho(\Gamma)<1$, Perron–Frobenius theory guarantees the existence of a vector $q\in\mathbb{R}^{k}_{++}$ and a constant $\alpha\in(0,1)$ satisfying

<table> <tbody><tr> <td></td> <td>$$\sum_{j=1}^{k}\Gamma_{ij}\,q_{j}\;\leq\;\alpha\,q_{i}\qquad\text{for every }i.$$</td> <td></td> <td rowspan="1">(5)</td></tr></tbody> </table>

If $\Gamma$ is reducible, apply the argument to the perturbed matrix $\Gamma_{\eta}:=\Gamma+\eta\mathbf{1}\mathbf{1}^{\top}$ for $\eta>0$ chosen small enough that $\rho(\Gamma_{\eta})<1$; the strictly positive Perron eigenvector $q$ of $\Gamma_{\eta}$ then satisfies $\Gamma q\leq\Gamma_{\eta}q=\rho(\Gamma_{\eta})q$, and we set $\alpha:=\rho(\Gamma_{\eta})\in(\rho(\Gamma),1)$.

Fix $w,w^{\prime}\in\mathcal{W}$ and an agent $i$. By the definition of the weighted norm, $\|w_{j}-w_{j}^{\prime}\|\leq q_{j}\,\|w-w^{\prime}\|_{q}$ for every $j$. Substituting this bound into the best-response sensitivity inequality ([4](https://amahrous.com/papers/reflexivity-threshold/#S4.E4)) and then applying ([5](https://amahrous.com/papers/reflexivity-threshold/#S5.E5)) yields

<table> <tbody><tr> <td></td> <td>$$\|B_{i}(w)-B_{i}(w^{\prime})\|\;\leq\;\sum_{j=1}^{k}\Gamma_{ij}\,q_{j}\,\|w-w^{\prime}\|_{q}\;\leq\;\alpha\,q_{i}\,\|w-w^{\prime}\|_{q}.$$</td> <td></td></tr></tbody> </table>

Dividing by $q_{i}>0$ and taking the maximum over $i$ gives the claim. ∎

Equivalently, for any $\alpha\in(\rho(\Gamma),1)$, one can choose positive weights $q$ such that $\Gamma q\leq\alpha q$. The contraction factor can therefore be made arbitrarily close to $\rho(\Gamma)$. The proof uses only two facts: $\Gamma$ is nonnegative and $\rho(\Gamma)<1$.

The contraction theorem gives the standard fixed-point consequences. Since $B$ is a contraction on the complete space $(\mathcal{W},\|\cdot\|_{q})$, Banach’s fixed-point theorem applies.

###### Corollary 5 (Existence, uniqueness, and geometric convergence).

Under the conditions of Theorem [4](https://amahrous.com/papers/reflexivity-threshold/#Thmtheorem4):

 
1. 1. 

  The retraining map $B$ admits a unique fixed point $w^{\star}\in\mathcal{W}$, which is the unique performatively stable equilibrium of the system.

2. 2. 

  For every initialization $w_{0}\in\mathcal{W}$, the iterates $w_{t+1}=B(w_{t})$ satisfy

  <table> <tbody><tr> <td></td> <td>$$\|w_{t}-w^{\star}\|_{q}\;\leq\;\alpha^{t}\,\|w_{0}-w^{\star}\|_{q}\qquad\text{for every }t\geq 0.$$</td> <td></td></tr></tbody> </table>

###### Proof.

Assumption [3](https://amahrous.com/papers/reflexivity-threshold/#Thmassumption3) ensures that $\mathcal{W}$ is complete under $\|\cdot\|_{q}$ and that $B$ maps $\mathcal{W}$ into itself. Theorem [4](https://amahrous.com/papers/reflexivity-threshold/#Thmtheorem4) shows that $B$ is an $\alpha$-contraction with $\alpha\in(0,1)$. Banach’s fixed-point theorem yields the unique fixed point $w^{\star}$. Iterating the contraction inequality with $w=w_{t}$ and $w^{\prime}=w^{\star}$ gives the geometric convergence bound. ∎

Corollary [5](https://amahrous.com/papers/reflexivity-threshold/#Thmtheorem5) gives the basic learnability result in the subcritical regime. The system has a unique performatively stable equilibrium, and repeated retraining reaches it at a geometric rate from any initialization. The condition is stated through $\Gamma$, which is constructed from primitive per-agent quantities.

If retraining instead satisfies $\|w_{t+1}-B(w_{t})\|_{q}\leq\eta_{t}$, then

<table> <tbody><tr> <td></td> <td>$$\|w_{t+1}-w^{\star}\|_{q}\leq\alpha\|w_{t}-w^{\star}\|_{q}+\eta_{t}.$$</td> <td></td></tr></tbody> </table>

Appendix [C](https://amahrous.com/papers/reflexivity-threshold/#A3) gives the resulting error bound and its interpretation for empirical retraining with controlled gradient error.

Contraction of the state dynamics alone does not give a performance bound. To control cumulative excess loss, we add smoothness in each agent’s own action.

###### Assumption 4 (Smoothness in own action).

For each agent $i$ and every fixed deployed profile $w$, the map $u_{i}\mapsto F_{i}(u_{i};w)$ is $L_{i}$-smooth.

The natural benchmark in a time-varying environment is the current best response. At round $t$, agent $i$ deploys $w_{i,t}$, while the action minimizing its risk under the current profile $w_{t}$ is $B_{i}(w_{t})$. The gap between these two actions is the instantaneous excess loss, and summing over agents and rounds gives

<table> <tbody><tr> <td></td> <td>$$\widetilde{\mathrm{Reg}}_{T}\;:=\;\sum_{t=0}^{T-1}\sum_{i=1}^{k}\Big(F_{i}(w_{i,t};w_{t})-F_{i}(B_{i}(w_{t});w_{t})\Big).$$</td> <td></td> <td rowspan="1">(6)</td></tr></tbody> </table>

This benchmark compares each deployment to the best response in the environment it actually faces. It also avoids assumptions on how objective values vary with the deployed profile. Bounds against the fixed equilibrium comparator require such assumptions and are therefore treated separately.

###### Corollary 6 (Bounded cumulative dynamic excess loss).

Under Assumptions [1](https://amahrous.com/papers/reflexivity-threshold/#Thmassumption1)–[2](https://amahrous.com/papers/reflexivity-threshold/#Thmassumption2), [3](https://amahrous.com/papers/reflexivity-threshold/#Thmassumption3), and [4](https://amahrous.com/papers/reflexivity-threshold/#Thmassumption4), and assuming $\rho(\Gamma)<1$, there exists a constant $C>0$ depending only on $\Gamma$, $q$, and $\{L_{i}\}$ such that

<table> <tbody><tr> <td></td> <td>$$\widetilde{\mathrm{Reg}}_{T}\;\leq\;\frac{C}{1-\alpha^{2}}\,\|w_{0}-w^{\star}\|_{q}^{2}\qquad\text{for every }T\geq 1.$$</td> <td></td></tr></tbody> </table>

In particular, the cumulative excess loss is bounded uniformly in the horizon $T$.

###### Proof.

Fix $t\geq 1$ and $i$. The best response $B_{i}(w_{t})$ minimizes $u_{i}\mapsto F_{i}(u_{i};w_{t})$, which is $L_{i}$-smooth by Assumption [4](https://amahrous.com/papers/reflexivity-threshold/#Thmassumption4). Standard smoothness gives

<table> <tbody><tr> <td></td> <td>$$F_{i}(w_{i,t};w_{t})-F_{i}(B_{i}(w_{t});w_{t})\;\leq\;\frac{L_{i}}{2}\,\|w_{i,t}-B_{i}(w_{t})\|^{2}.$$</td> <td></td> <td rowspan="1">(7)</td></tr></tbody> </table>

For $t\geq 1$, the dynamics ([3](https://amahrous.com/papers/reflexivity-threshold/#S3.E3)) give $w_{i,t}=B_{i}(w_{t-1})$, so

<table> <tbody><tr> <td></td> <td>$$\|w_{i,t}-B_{i}(w_{t})\|\;=\;\|B_{i}(w_{t-1})-B_{i}(w_{t})\|\;\leq\;\sum_{j=1}^{k}\Gamma_{ij}\,\|w_{j,t-1}-w_{j,t}\|,$$</td> <td></td></tr></tbody> </table>

where the inequality is ([4](https://amahrous.com/papers/reflexivity-threshold/#S4.E4)). Using $\|w_{j,t}-w_{j,t-1}\|\leq q_{j}\|w_{t}-w_{t-1}\|_{q}$ gives

<table> <tbody><tr> <td></td> <td>$$\|w_{i,t}-B_{i}(w_{t})\|\;\leq\;\Big(\sum_{j=1}^{k}\Gamma_{ij}q_{j}\Big)\|w_{t}-w_{t-1}\|_{q}.$$</td> <td></td></tr></tbody> </table>

Substituting into ([7](https://amahrous.com/papers/reflexivity-threshold/#S5.E7)) and summing over $i$ gives

<table> <tbody><tr> <td></td> <td>$$\sum_{i=1}^{k}\Big(F_{i}(w_{i,t};w_{t})-F_{i}(B_{i}(w_{t});w_{t})\Big)\;\leq\;C^{\prime}\,\|w_{t}-w_{t-1}\|_{q}^{2},$$</td> <td></td></tr></tbody> </table>

for a constant $C^{\prime}$ absorbing the $L_{i}$ and the row-sum factors $\big(\sum_{j}\Gamma_{ij}q_{j}\big)^{2}$. By Corollary [5](https://amahrous.com/papers/reflexivity-threshold/#Thmtheorem5) and the triangle inequality,

<table> <tbody><tr> <td></td> <td>$$\|w_{t}-w_{t-1}\|_{q}\;\leq\;\|w_{t}-w^{\star}\|_{q}+\|w_{t-1}-w^{\star}\|_{q}\;\leq\;(1+\alpha)\,\alpha^{t-1}\,\|w_{0}-w^{\star}\|_{q},$$</td> <td></td></tr></tbody> </table>

so the per-round excess loss decays as $\alpha^{2(t-1)}$. Summing the geometric series from $t=1$ to $T-1$ gives a contribution of order $\|w_{0}-w^{\star}\|_{q}^{2}/(1-\alpha^{2})$. For $t=0$, $\|w_{0}-B(w_{0})\|_{q}\leq\|w_{0}-w^{\star}\|_{q}+\|B(w^{\star})-B(w_{0})\|_{q}\leq(1+\alpha)\|w_{0}-w^{\star}\|_{q}$, which fits the same geometric series. Combining yields the claim. ∎

The bound depends on the initialization and the contraction factor but not on the time horizon, with the $1/(1-\alpha^{2})$ factor arising from the geometric decay of the one-step gap together with smoothness. Below the threshold, cumulative excess loss is thus $O(1)$; Section [6](https://amahrous.com/papers/reflexivity-threshold/#S6) constructs supercritical instances with $\Omega(T)$ cumulative excess loss over a critical horizon.

The geometric bound gives iteration complexity $O\!\left(\log(\|w_{0}-w^{\star}\|_{q}/\delta)/(-\log\alpha)\right)$ to accuracy $\delta$. This bound and the factor $1/(1-\alpha^{2})$ deteriorate as $\alpha\to 1^{-}$. Figure [1](https://amahrous.com/papers/reflexivity-threshold/#S6.F1) illustrates the slowdown in a rescaled linear family as $\rho(\Gamma)$ approaches one.

### 6 Supercritical Regime

Section [5](https://amahrous.com/papers/reflexivity-threshold/#S5) established that $\rho(\Gamma)<1$ is sufficient for geometric convergence and bounded cumulative excess loss. Whether the supercritical regime produces an intrinsic learning obstruction is delicate: failure of contraction does not by itself imply information-theoretic impossibility, since with enough observations a learner may recover the correct equilibrium even when repeated retraining diverges. We show that the threshold has a sharp negative side in the worst case. For every $\varepsilon>0$, we construct a supercritical family with $\rho(\Gamma)=1+\varepsilon$ in which any decentralized local-information learner - one that at each round uses only its own history of observations and actions - incurs linear cumulative excess loss for $T=O(1/\varepsilon)$ rounds.

![fig iteration complexity](https://amahrous.com/papers/reflexivity-threshold/figures/fig_iteration_complexity.svg)

(a) Number of retraining steps needed to satisfy $\|w_{t}-w^{\star}\|_{q}\leq\delta$. Convergence slows sharply as $\rho(\Gamma)$ approaches $1$ from below. Only subcritical values are plotted, with a computational cap of $10{,}000$ iterations and a displayed vertical range up to $1{,}000$.

![fig rho sweep five lines](https://amahrous.com/papers/reflexivity-threshold/figures/fig_rho_sweep_five_lines.svg)

(b) Normalized distance to equilibrium (log scale) under repeated retraining. Subcritical instances contract geometrically, while the plotted supercritical instances move away from equilibrium. The non-normal subcritical curve shows transient growth before contraction.

Figure 1: The reflexivity threshold. The simulations show that convergence slows as $\rho(\Gamma)$ approaches $1$ from below. Below the threshold, repeated retraining moves geometrically toward equilibrium; above the threshold, the plotted trajectories move away from equilibrium. Setup details are in Appendix [B](https://amahrous.com/papers/reflexivity-threshold/#A2).

All agents know the model parameters $(\Gamma_{\varepsilon},\Delta,\sigma_{\varepsilon}^{2},v)$; only the hidden parameter $\nu$ is unknown.

###### Definition 7 (Decentralized local-information learner).

A *decentralized local-information learner* is a policy profile $A=(A_{1},\dots,A_{k})$ in which agent $i$’s action $w_{i,t}$ at round $t$ is measurable with respect to the private history $\mathcal{H}_{i,t}^{\mathrm{pre}}:=\sigma\big(w_{i,0:t-1},\;Y_{i,0:t-1},\;U_{i,0:t}\big)$, where $Y_{i,s}$ is agent $i$’s private observation at round $s$ and $U_{i,s}$ is agent $i$’s internal randomization.

No agent observes the full system state: each sees only its own signal, without access to other agents’ actions or observations. The lower bound applies to any learner satisfying this constraint, regardless of the algorithm used within each agent.

#### Hard family.

The construction places all endogenous amplification along a single direction, which simplifies the analysis and makes the separation between the two environments explicit.

Fix $\varepsilon\in(0,1]$ and a unit vector $v\in\mathbb{R}^{k}$ with nonnegative entries. Define the reflexivity matrix

<table> <tbody><tr> <td></td> <td>$$\Gamma_{\varepsilon}\;:=\;(1+\varepsilon)\,vv^{\top}.$$</td> <td></td> <td rowspan="1">(8)</td></tr></tbody> </table>

The matrix $\Gamma_{\varepsilon}$ is nonnegative, symmetric, and rank one, with single nonzero eigenvalue $1+\varepsilon$, so $\rho(\Gamma_{\varepsilon})=1+\varepsilon$. The system is therefore supercritical by construction, with $\varepsilon$ measuring the distance above the threshold. Each agent has $d_{i}=1$ and $\mathcal{W}_{i}=\mathbb{R}$, and the quadratic loss gives $\mu_{i}=1$, so the abstract reflexivity matrix of Section [4](https://amahrous.com/papers/reflexivity-threshold/#S4) coincides with $\Gamma_{\varepsilon}$ in this construction.

The environment contains a hidden binary parameter $\nu\in\{-1,+1\}$ that determines the true state of the world. Fix an amplitude $\Delta>0$ and let the noise variance be $\sigma_{\varepsilon}^{2}:=8\Delta^{2}/\varepsilon$. The observation model is

<table> <tbody><tr> <td></td> <td>$$Y_{t}\;=\;\nu\Delta v+\Gamma_{\varepsilon}w_{t}+\xi_{t},\qquad\xi_{t}\sim\mathcal{N}(0,\sigma_{\varepsilon}^{2}I_{k}),$$</td> <td></td> <td rowspan="1">(9)</td></tr></tbody> </table>

where each agent $i$ observes only the coordinate $Y_{i,t}$.

Each agent uses quadratic loss $\ell_{i}(a;y):=\tfrac{1}{2}(a-y)^{2}$, which gives the performative risk

<table> <tbody><tr> <td></td> <td>$$F_{i}(a;w,\nu)\;=\;\frac{1}{2}\Big(a-\nu\Delta v_{i}-(\Gamma_{\varepsilon}w)_{i}\Big)^{2}+\frac{\sigma_{\varepsilon}^{2}}{2}.$$</td> <td></td> <td rowspan="1">(10)</td></tr></tbody> </table>

The additive constant $\sigma_{\varepsilon}^{2}/2$ cancels in differences and is dropped below. Minimizing over $a$ gives the best-response map $B(w;\nu)=\nu\Delta v+\Gamma_{\varepsilon}w$. The fixed-point equation $w^{\star,\nu}=B(w^{\star,\nu};\nu)$ has the explicit solution

<table> <tbody><tr> <td></td> <td>$$w^{\star,\nu}\;=\;(I-\Gamma_{\varepsilon})^{-1}\nu\Delta v\;=\;-\frac{\nu\Delta}{\varepsilon}\,v.$$</td> <td></td> <td rowspan="1">(11)</td></tr></tbody> </table>

The last equality uses the identity $(I-\Gamma_{\varepsilon})v=-\varepsilon v$, which follows from the definition ([8](https://amahrous.com/papers/reflexivity-threshold/#S6.E8)).

The two equilibria $w^{\star,+}$ and $w^{\star,-}$ are therefore located at distance $2\Delta/\varepsilon$ along $v$. As $\varepsilon$ decreases, these equilibria move apart, and the geometric penalty for choosing the wrong sign grows. This divergence is the mechanism that converts slow information acquisition into large cumulative excess loss.

The instantaneous excess performative loss at round $t$ is

<table> <tbody><tr> <td></td> <td>$$r_{t}^{\nu}\;:=\;\sum_{i=1}^{k}\Big(F_{i}(w_{i,t};w_{t},\nu)-F_{i}(w_{i}^{\star,\nu};w^{\star,\nu},\nu)\Big),$$</td> <td></td> <td rowspan="1">(12)</td></tr></tbody> </table>

and the cumulative excess loss over $T$ rounds is $\mathrm{Reg}_{T}^{\nu}(A):=\sum_{t=0}^{T-1}r_{t}^{\nu}$.

The subcritical result uses a dynamic comparator (the current best response $B_{i}(w_{t})$), whereas ([12](https://amahrous.com/papers/reflexivity-threshold/#S6.E12)) uses the fixed equilibrium comparator $w^{\star,\nu}$: the dynamic comparator measures one-step adaptation to the current caused environment, while the equilibrium comparator measures whether the learner identifies the correct stable equilibrium. In the supercritical construction these goals decouple, so the equilibrium comparator is the appropriate benchmark for the two-environment testing argument. For the quadratic family in ([10](https://amahrous.com/papers/reflexivity-threshold/#S6.E10)) the two comparators in fact yield identical instantaneous excess loss, so the $\Omega(\Delta^{2}T)$ bound holds under either benchmark.

###### Theorem 8 (Linear lower bound in a supercritical family).

There exist absolute constants $c_{0},c_{1}>0$ such that the following holds. For every $\varepsilon\in(0,1]$, in the supercritical family defined by ([8](https://amahrous.com/papers/reflexivity-threshold/#S6.E8))–([9](https://amahrous.com/papers/reflexivity-threshold/#S6.E9)) with $\sigma_{\varepsilon}^{2}=8\Delta^{2}/\varepsilon$, every decentralized local-information learner $A$ satisfies

<table> <tbody><tr> <td></td> <td>$$\frac{1}{2}\,\mathbb{E}_{+}\big[\mathrm{Reg}_{T}^{+}(A)\big]+\frac{1}{2}\,\mathbb{E}_{-}\big[\mathrm{Reg}_{T}^{-}(A)\big]\;\geq\;c_{1}\,\Delta^{2}\,T\qquad\text{for every }T\leq c_{0}/\varepsilon.$$</td> <td></td></tr></tbody> </table>

In particular,

<table> <tbody><tr> <td></td> <td>$$\sup_{\nu\in\{-1,+1\}}\mathbb{E}_{\nu}\big[\mathrm{Reg}_{T}^{\nu}(A)\big]\;\geq\;c_{1}\,\Delta^{2}\,T\qquad\text{for every }T\leq c_{0}/\varepsilon.$$</td> <td></td></tr></tbody> </table>

The proof proceeds in three steps. Step 1 shows that the two environments $\nu=+1$ and $\nu=-1$ remain statistically indistinguishable over the critical horizon. Step 2 shows that misidentifying the environment forces the learner into a region of large excess loss. Step 3 combines these two facts.

###### Proof sketch; full proof in Appendix [A](https://amahrous.com/papers/reflexivity-threshold/#A1).

The argument has two parts.

*Indistinguishability.* We prove the KL bound under a stronger centralized observation model that reveals the full profile $w_{t}$ and vector observation $Y_{t}$; the bound therefore also applies to decentralized learners. Conditional on the realized pre-observation history $\mathcal{F}_{t}$, the action $w_{t}$ is fixed by the learner’s policy. Under the two hypotheses, the next observation is Gaussian with common covariance $\sigma_{\varepsilon}^{2}I_{k}$ and conditional means differing by $2\Delta v$. The per-round Kullback–Leibler divergence is therefore $\|2\Delta v\|^{2}/(2\sigma_{\varepsilon}^{2})=\varepsilon/4$, using $\|v\|=1$ and $\sigma_{\varepsilon}^{2}=8\Delta^{2}/\varepsilon$. By the chain rule for KL divergence and Pinsker’s inequality, the total variation distance remains bounded away from one for all $t\leq c_{0}/\varepsilon$, so the optimal equal-prior testing error is bounded below by an absolute constant $p_{0}>0$.

*Geometric cost of misidentification.* The two equilibria ([11](https://amahrous.com/papers/reflexivity-threshold/#S6.E11)) lie at $\pm(\Delta/\varepsilon)v$, so on the event that the midpoint decoder picks the wrong sign, $|\langle w_{t}-w^{\star,\nu},v\rangle|\geq\Delta/\varepsilon$. The closed form $r_{t}^{\nu}=\tfrac{1}{2}\|(I-\Gamma_{\varepsilon})(w_{t}-w^{\star,\nu})\|^{2}$ together with $(I-\Gamma_{\varepsilon})v=-\varepsilon v$ then gives $r_{t}^{\nu}\geq\Delta^{2}/2$ on that event. The factor $\varepsilon$ from the contraction of $(I-\Gamma_{\varepsilon})$ along $v$ cancels exactly with the factor $1/\varepsilon$ from the equilibrium separation, which is why the obstruction survives the limit $\varepsilon\to 0$ and produces a horizon of order $1/\varepsilon$.

Combining the two parts: averaging over $\nu$ and using equal-prior testing error at least $p_{0}$ gives $\tfrac{1}{2}\mathbb{E}_{+}[r_{t}^{+}]+\tfrac{1}{2}\mathbb{E}_{-}[r_{t}^{-}]\geq p_{0}\Delta^{2}/2$ for every $t\leq c_{0}/\varepsilon$, and summing yields the claim with $c_{1}=p_{0}/2$. ∎

The positive theorem assumes exact population best responses, whereas the lower bound concerns noisy observations over a finite horizon, with $\sigma_{\varepsilon}^{2}=8\Delta^{2}/\varepsilon$. The proof bounds indistinguishability even for a centralized learner observing the same signals, so communication alone does not remove this obstruction in the constructed family.

### 7 Discussion

#### Reflexivity matrix and interpretation.

The framework replaces a scalar Lipschitz constant with the reflexivity matrix $\Gamma$, whose entries $a_{ij}/\mu_{i}$ retain the per-pair structure of performative feedback. This matters because two systems with the same scalar bound can have different stability behavior if their feedback is routed through different agent networks. The Perron weights $q$ in Theorem [4](https://amahrous.com/papers/reflexivity-threshold/#Thmtheorem4) encode this heterogeneity by rescaling agents according to their role in the collective retraining dynamics. When $k=1$, $\Gamma$ reduces to the scalar ratio $a_{11}/\mu_{1}$, recovering the single-agent contraction threshold of [Perdomo et al. (2020)](https://amahrous.com/papers/reflexivity-threshold/#bib.bib16). More generally, $\rho(\Gamma)=1$ separates dissipative feedback, where repeated retraining contracts, from supercritical feedback, where uniform stability guarantees fail. We use *reflexivity* for this deployment-to-data channel, following the financial-market terminology of [Soros (1987)](https://amahrous.com/papers/reflexivity-threshold/#bib.bib18); we do not formalize the broader economic concept.

#### Beyond the spectral radius.

The threshold $\rho(\Gamma)=1$ governs asymptotic behavior, but finite-horizon dynamics can depend on finer matrix properties and initial conditions. One important case is non-normality: $\|\Gamma^{t}\|$ may grow transiently even if $\rho(\Gamma)<1$, as illustrated by the non-normal subcritical trajectory in Panel [1(b)](https://amahrous.com/papers/reflexivity-threshold/#S6.F1.sf2). Thus the spectral radius identifies the asymptotic threshold, while quantities such as the numerical range or pseudospectra may better capture finite-horizon amplification. We leave this refinement to future work.

#### Empirical measurement.

The framework identifies a stability quantity, $\rho(\Gamma)$, that is measurable in principle but difficult to identify empirically. Each entry $a_{ij}$ is counterfactual: it describes how agent $i$’s gradient would respond to alternative deployments by agent $j$, while $\mu_{i}$ is also not directly observed. Estimation is therefore a causal identification problem, since common system shocks may affect both agent $j$’s deployment and agent $i$’s gradient. Testing whether estimated values of $\rho(\Gamma)$ predict observed instability is a concrete direction for future work. The primitive bounds are useful when $B$ is defined implicitly by a nonlinear optimizer: curvature and pairwise gradient sensitivity can be bounded without solving or differentiating the full best-response map. The certificate can be conservative and depends on the chosen block geometry; failure of $\rho(\Gamma)<1$ alone does not diagnose instability. As a design lever, adding a fixed-reference quadratic penalty $\tfrac{\lambda_{i}}{2}\|u_{i}-u_{i}^{\mathrm{ref}}\|^{2}$ replaces $\Gamma_{ij}$ by $a_{ij}/(\mu_{i}+\lambda_{i})$, potentially restoring the certificate, while changing the objective and generally the equilibrium.

#### Limitations and extensions.

Several modeling choices delimit our results. The main guarantees assume strong convexity in each agent’s own action and exact best-response retraining; Appendix [C](https://amahrous.com/papers/reflexivity-threshold/#A3) controls approximate retraining under explicit error bounds. Sharper finite-sample rates, weaker curvature assumptions, and gradient updates remain directions for future work. We also treat the reflexivity matrix as fixed across rounds. If the interaction structure evolves, a natural extension is to study time-varying matrices $\Gamma_{t}$, where tools such as joint spectral radii may be needed to characterize stability. The lower bound establishes that no universal positive guarantee can extend above the threshold, since at least one supercritical family forces linear cumulative excess loss; it does not assert that every supercritical $\Gamma$ is unlearnable. Characterizing which supercritical systems remain learnable is open for future work. Coordination among agents may shift the threshold, while damped retraining is a natural design lever for stabilizing otherwise unstable systems.

### Acknowledgments and Disclosure of Funding

This work received no funding. The authors declare no competing interests.

### References

 
- Anagnostides et al. \[2026\]  Ioannis Anagnostides, Rohan Chauhan, Ioannis Panageas, Tuomas Sandholm, and Jingming Yan.  On the computational complexity of performative prediction.  *arXiv preprint arXiv:2601.20180*, 2026.

- Ballester et al. \[2006\]  Coralio Ballester, Antoni Calvó-Armengol, and Yves Zenou.  Who’s who in networks. wanted: The key player.  *Econometrica*, 74(5):1403–1417, 2006.

- Bramoullé et al. \[2014\]  Yann Bramoullé, Rachel Kranton, and Martin D’Amours.  Strategic interaction and networks.  *American Economic Review*, 104(3):898–930, 2014.

- Brown et al. \[2022\]  Gavin Brown, Shlomi Hod, and Iden Kalemaj.  Performative prediction in a stateful world.  In *Proceedings of the 25th International Conference on Artificial Intelligence and Statistics*, volume 151 of *Proceedings of Machine Learning Research*, pages 6045–6061. PMLR, 2022.

- Chen et al. \[2024\]  Fan Chen, Dylan J. Foster, Yanjun Han, Jian Qian, Alexander Rakhlin, and Yunbei Xu.  Assouad, Fano, and Le Cam with interaction: A unifying lower bound framework and characterization for bandit learnability.  In *Advances in Neural Information Processing Systems*, volume 37, 2024.

- Cutler et al. \[2024\]  Joshua Cutler, Mateo Díaz, and Dmitriy Drusvyatskiy.  Stochastic approximation with decision-dependent distributions: Asymptotic normality and optimality.  *Journal of Machine Learning Research*, 25(90):1–49, 2024.

- Farina and Perdomo \[2026\]  Gabriele Farina and Juan Carlos Perdomo.  The stability of online algorithms in performative prediction.  *arXiv preprint arXiv:2602.24207*, 2026.

- Hardt et al. \[2022\]  Moritz Hardt, Meena Jagadeesan, and Celestine Mendler-Dünner.  Performative power.  In *Advances in Neural Information Processing Systems*, volume 35, 2022.

- Li et al. \[2022\]  Qiang Li, Chung-Yiu Yau, and Hoi-To Wai.  Multi-agent performative prediction with greedy deployment and consensus seeking agents.  In *Advances in Neural Information Processing Systems*, volume 35, 2022.

- Mandal et al. \[2023\]  Debmalya Mandal, Stelios Triantafyllou, and Goran Radanovic.  Performative reinforcement learning.  In *Proceedings of the 40th International Conference on Machine Learning*, volume 202 of *Proceedings of Machine Learning Research*, pages 23642–23680. PMLR, 2023.

- Mendler-Dünner et al. \[2020\]  Celestine Mendler-Dünner, Juan C. Perdomo, Tijana Zrnic, and Moritz Hardt.  Stochastic optimization for performative prediction.  In *Advances in Neural Information Processing Systems*, volume 33, pages 4929–4939, 2020.

- Miller et al. \[2021\]  John P. Miller, Juan C. Perdomo, and Tijana Zrnic.  Outside the echo chamber: Optimizing the performative risk.  In *Proceedings of the 38th International Conference on Machine Learning*, volume 139 of *Proceedings of Machine Learning Research*, pages 7710–7720. PMLR, 2021.

- Mofakhami et al. \[2023\]  Mehrnaz Mofakhami, Ioannis Mitliagkas, and Gauthier Gidel.  Performative prediction with neural networks.  In *Proceedings of the 26th International Conference on Artificial Intelligence and Statistics*, volume 206 of *Proceedings of Machine Learning Research*, pages 11079–11093. PMLR, 2023.

- Narang et al. \[2023\]  Adhyyan Narang, Evan Faulkner, Dmitriy Drusvyatskiy, Maryam Fazel, and Lillian J. Ratliff.  Multiplayer performative prediction: Learning in decision-dependent games.  *Journal of Machine Learning Research*, 24(202):1–56, 2023.

- Parise and Ozdaglar \[2019\]  Francesca Parise and Asuman Ozdaglar.  A variational inequality framework for network games: Existence, uniqueness, convergence and sensitivity analysis.  *Games and Economic Behavior*, 114:47–82, 2019.

- Perdomo et al. \[2020\]  Juan C. Perdomo, Tijana Zrnic, Celestine Mendler-Dünner, and Moritz Hardt.  Performative prediction.  In *Proceedings of the 37th International Conference on Machine Learning*, volume 119 of *Proceedings of Machine Learning Research*, pages 7599–7609. PMLR, 2020.

- Piliouras and Yu \[2023\]  Georgios Piliouras and Fang-Yi Yu.  Multi-agent performative prediction: From global stability and optimality to chaos.  In *Proceedings of the 24th ACM Conference on Economics and Computation*, pages 1047–1074, 2023.

- Soros \[1987\]  George Soros.  *The Alchemy of Finance: Reading the Mind of the Market*.  Simon and Schuster, New York, 1987.

- Tsybakov \[2009\]  Alexandre B. Tsybakov.  *Introduction to Nonparametric Estimation*.  Springer, 2009.

- Wang et al. \[2023\]  Xiaolu Wang, Chung-Yiu Yau, and Hoi-To Wai.  Network effects in performative prediction games.  In *Proceedings of the 40th International Conference on Machine Learning*, volume 202 of *Proceedings of Machine Learning Research*, pages 36514–36540. PMLR, 2023.

- Yan and Cao \[2024\]  Wenjing Yan and Xuanyu Cao.  Decentralized noncooperative games with coupled decision-dependent distributions.  In *Advances in Neural Information Processing Systems*, volume 37, 2024.

- Zhong et al. \[2025\]  Guangzheng Zhong, Yang Liu, and Jiming Liu.  Towards performatively stable equilibria in decision-dependent games for arbitrary data distribution maps.  *arXiv preprint*, 2025.

### Appendix A Full Proof of Theorem [8](https://amahrous.com/papers/reflexivity-threshold/#Thmtheorem8)

This appendix gives the full proof of Theorem [8](https://amahrous.com/papers/reflexivity-threshold/#Thmtheorem8), expanding the sketch in Section [6](https://amahrous.com/papers/reflexivity-threshold/#S6). We retain the same notation: $P_{\nu}$ denotes the law of the full system trajectory under learner $A$ in environment $\nu\in\{-1,+1\}$, and $\mathcal{F}_{t}$ denotes the history up to and including the action $w_{t}$ but excluding the observation $Y_{t}$.

###### Proof of Theorem [8](https://amahrous.com/papers/reflexivity-threshold/#Thmtheorem8).

*Step 1: Bounding the Kullback–Leibler divergence.* The KL bound is proved under a stronger centralized observation model in which the learner sees the full profile $w_{t}$ and vector observation $Y_{t}$. Since decentralized learners observe only part of this information, the same indistinguishability bound applies to the learners in Theorem [8](https://amahrous.com/papers/reflexivity-threshold/#Thmtheorem8). Conditional on the realized pre-observation history $\mathcal{F}_{t}$, the action $w_{t}$ is fixed by the learner’s policy. The observation $Y_{t}$ is then drawn from a Gaussian whose mean differs between the two environments only through the term $\nu\Delta v$. Specifically,

<table> <tbody><tr> <td></td> <td>$$P_{\nu}(Y_{t}\mid\mathcal{F}_{t})\;=\;\mathcal{N}\big(\nu\Delta v+\Gamma_{\varepsilon}w_{t},\,\sigma_{\varepsilon}^{2}I_{k}\big).$$</td> <td></td></tr></tbody> </table>

The means differ by $2\Delta v$, and the covariance matrices are identical. The Kullback–Leibler divergence between two Gaussians with common covariance $\sigma^{2}I$ and mean difference $\mu$ equals $\|\mu\|^{2}/(2\sigma^{2})$. Applying this formula and using $\sigma_{\varepsilon}^{2}=8\Delta^{2}/\varepsilon$,

<table> <tbody><tr> <td></td> <td>$$\mathrm{KL}\big(P_{+}(Y_{t}\mid\mathcal{F}_{t})\,\|\,P_{-}(Y_{t}\mid\mathcal{F}_{t})\big)\;=\;\frac{\|2\Delta v\|^{2}}{2\sigma_{\varepsilon}^{2}}\;=\;\frac{2\Delta^{2}}{\sigma_{\varepsilon}^{2}}\;=\;\frac{\varepsilon}{4}.$$</td> <td></td></tr></tbody> </table>

By the chain rule for Kullback–Leibler divergence, the total divergence after $t$ rounds is

<table> <tbody><tr> <td></td> <td>$$\mathrm{KL}\big(P_{+}^{t}\,\|\,P_{-}^{t}\big)\;=\;\frac{t\varepsilon}{4}.$$</td> <td></td> <td rowspan="1">(13)</td></tr></tbody> </table>

Choose $c_{0}:=1/2$. For every $t\leq c_{0}/\varepsilon$, Pinsker’s inequality gives

<table> <tbody><tr> <td></td> <td>$$\mathrm{TV}(P_{+}^{t},P_{-}^{t})\;\leq\;\sqrt{\frac{1}{2}\mathrm{KL}(P_{+}^{t}\,\|\,P_{-}^{t})}\;\leq\;\sqrt{\frac{t\varepsilon}{8}}\;\leq\;\sqrt{1/16}\;=\;\frac{1}{4}.$$</td> <td></td></tr></tbody> </table>

The minimax testing error for deciding $\nu$ from the observed history is therefore bounded below by an absolute constant $p_{0}>0$, independent of $\varepsilon$ and $t$.

*Step 2: Geometric cost of misidentification.* Define the midpoint decoder

<table> <tbody><tr> <td></td> <td>$$\widehat{\nu}_{t}\;:=\;\argmin_{s\in\{-1,+1\}}\|w_{t}-w^{\star,s}\|.$$</td> <td></td></tr></tbody> </table>

On the event $\{\widehat{\nu}_{t}\neq\nu\}$, the action $w_{t}$ lies at least as close to the incorrect equilibrium as to the correct one. Using ([11](https://amahrous.com/papers/reflexivity-threshold/#S6.E11)), the two equilibria lie on opposite sides of the origin along $v$ at distance $\Delta/\varepsilon$ each. The midpoint between them is the origin, so $\widehat{\nu}_{t}\neq\nu$ implies $\nu\langle w_{t},v\rangle\geq 0$. Consequently,

<table> <tbody><tr> <td></td> <td>$$|\langle w_{t}-w^{\star,\nu},v\rangle|\;\geq\;\frac{\Delta}{\varepsilon}\qquad\text{on }\{\widehat{\nu}_{t}\neq\nu\}.$$</td> <td></td> <td rowspan="1">(14)</td></tr></tbody> </table>

For the quadratic family, the equilibrium identity $w^{\star,\nu}=\nu\Delta v+\Gamma_{\varepsilon}w^{\star,\nu}$ implies $F_{i}(w_{i}^{\star,\nu};w^{\star,\nu},\nu)=\sigma_{\varepsilon}^{2}/2$. Substituting into ([12](https://amahrous.com/papers/reflexivity-threshold/#S6.E12)) and summing over $i$ gives

<table> <tbody><tr> <td></td> <td>$$r_{t}^{\nu}\;=\;\frac{1}{2}\,\|w_{t}-\nu\Delta v-\Gamma_{\varepsilon}w_{t}\|^{2}\;=\;\frac{1}{2}\,\|(I-\Gamma_{\varepsilon})(w_{t}-w^{\star,\nu})\|^{2},$$</td> <td></td> <td rowspan="1">(15)</td></tr></tbody> </table>

where the second equality uses $\nu\Delta v=(I-\Gamma_{\varepsilon})w^{\star,\nu}$.

The identity $(I-\Gamma_{\varepsilon})v=-\varepsilon v$ implies that $(I-\Gamma_{\varepsilon})$ contracts the direction $v$ by the factor $\varepsilon$. Combining ([14](https://amahrous.com/papers/reflexivity-threshold/#A1.E14)) with the lower bound

<table> <tbody><tr> <td></td> <td>$$\|(I-\Gamma_{\varepsilon})(w_{t}-w^{\star,\nu})\|\;\geq\;|\langle(I-\Gamma_{\varepsilon})(w_{t}-w^{\star,\nu}),v\rangle|\;=\;\varepsilon\,|\langle w_{t}-w^{\star,\nu},v\rangle|,$$</td> <td></td></tr></tbody> </table>

and substituting ([14](https://amahrous.com/papers/reflexivity-threshold/#A1.E14)),

<table> <tbody><tr> <td></td> <td>$$\|(I-\Gamma_{\varepsilon})(w_{t}-w^{\star,\nu})\|\;\geq\;\varepsilon\cdot\frac{\Delta}{\varepsilon}\;=\;\Delta\qquad\text{on }\{\widehat{\nu}_{t}\neq\nu\}.$$</td> <td></td></tr></tbody> </table>

Substituting into ([15](https://amahrous.com/papers/reflexivity-threshold/#A1.E15)) yields

<table> <tbody><tr> <td></td> <td>$$r_{t}^{\nu}\;\geq\;\frac{\Delta^{2}}{2}\qquad\text{on }\{\widehat{\nu}_{t}\neq\nu\}.$$</td> <td></td> <td rowspan="1">(16)</td></tr></tbody> </table>

The factor $\varepsilon$ from the contraction of $(I-\Gamma_{\varepsilon})$ and the factor $1/\varepsilon$ from the equilibrium separation cancel exactly. This cancellation is why the lower bound survives the limit $\varepsilon\to 0$ and produces a horizon of order $1/\varepsilon$ rather than a faster-vanishing horizon.

*Step 3: Combining the bounds.* Taking expectation of ([16](https://amahrous.com/papers/reflexivity-threshold/#A1.E16)) under environment $\nu$ gives

<table> <tbody><tr> <td></td> <td>$$\mathbb{E}_{\nu}[r_{t}^{\nu}]\;\geq\;\frac{\Delta^{2}}{2}\,P_{\nu}(\widehat{\nu}_{t}\neq\nu).$$</td> <td></td></tr></tbody> </table>

Averaging over $\nu\in\{-1,+1\}$,

<table> <tbody><tr> <td></td> <td>$$\frac{1}{2}\mathbb{E}_{+}[r_{t}^{+}]+\frac{1}{2}\mathbb{E}_{-}[r_{t}^{-}]\;\geq\;\frac{\Delta^{2}}{2}\cdot\frac{1}{2}\Big(P_{+}(\widehat{\nu}_{t}\neq+1)+P_{-}(\widehat{\nu}_{t}\neq-1)\Big).$$</td> <td></td></tr></tbody> </table>

The bracketed quantity is twice this decoder’s equal-prior error, which is at least the optimal equal-prior testing error and hence at least $p_{0}$ by Step 1 for every $t\leq c_{0}/\varepsilon$. Therefore,

<table> <tbody><tr> <td></td> <td>$$\frac{1}{2}\mathbb{E}_{+}[r_{t}^{+}]+\frac{1}{2}\mathbb{E}_{-}[r_{t}^{-}]\;\geq\;\frac{p_{0}\Delta^{2}}{2}\qquad\text{for every }t\leq c_{0}/\varepsilon.$$</td> <td></td></tr></tbody> </table>

Summing over $t=0,\dots,T-1$ gives the first claim with $c_{1}:=p_{0}/2$. The supremum bound follows because the maximum over $\nu$ dominates the average. ∎

### Appendix B Simulation Details for Figure [1](https://amahrous.com/papers/reflexivity-threshold/#S6.F1)

All instances have $k=100$. The sparse matrices have zero diagonal; each off-diagonal position is independently selected with probability $0.15$ and assigned a uniform $[0,1]$ weight, before rescaling to the target spectral radius. The non-normal instance is constructed separately as described below. Code, seeds, and commands to reproduce the figures are provided in the supplementary simulation artifact.

#### Panel [1(a)](https://amahrous.com/papers/reflexivity-threshold/#S6.F1.sf1) (phase diagram).

With seed $0$, we generate $20$ sparse base matrices with spectral radius one. Each is paired with $5$ Gaussian initial states normalized to $\|w_{0}\|_{q}=1$ using its positive right Perron vector $q$. The dynamics are $w_{t+1}=\Gamma w_{t}$ with $w^{\star}=0$. For each $\rho$ on a grid of $200$ values in $[0.5,1.5]$, densely sampled near one, we rescale the base to $\Gamma=\rho\Gamma_{\mathrm{base}}$ and record the first iteration at which $\|w_{t}\|_{q}\leq 10^{-3}$, with computational cap $T_{\max}=10{,}000$. The curve reports the median and interquartile band across the $100$ trajectories. Only $\rho<1$ values are evaluated for hitting times and plotted; the vertical display is limited to $1{,}000$. The same Perron weights are used across rescalings of each base.

#### Panel [1(b)](https://amahrous.com/papers/reflexivity-threshold/#S6.F1.sf2) (trajectories).

With seed $20260439$, each sparse baseline at $\rho\in\{0.50,0.99,1.01,1.50\}$ uses $100$ independent draws of a matrix and of vectors $b,w_{0}$ whose coordinates are Gaussian with standard deviation $1/\sqrt{k}$. We simulate $w_{t+1}=b+\Gamma w_{t}$ for $200$ steps and compute $w^{\star}=(I-\Gamma)^{-1}b$. The non-normal instance uses a fixed dense upper-triangular $\Gamma=0.5I+sU$, where $U$ has ones strictly above the diagonal and $s$ is chosen so that $\|\Gamma\|_{2}/\rho(\Gamma)=10$. It uses $b=0$ and $100$ Gaussian initial states normalized to Euclidean unit norm. Each curve reports the mean of $\log_{10}(\|w_{t}-w^{\star}\|_{2}/\|w_{0}-w^{\star}\|_{2}+10^{-12})$, with pointwise interquartile bands. The horizontal zero line marks the initial normalized distance.

Since the experiments are synthetic simulations, they can be reproduced with standard CPU resources.

### Appendix C Approximate and Empirical Retraining

###### Proposition 9 (Robustness to retraining errors).

Under the conditions of Theorem [4](https://amahrous.com/papers/reflexivity-threshold/#Thmtheorem4), let $q,\alpha$ be its weights and contraction factor, and let $w^{\star}$ be the unique equilibrium. Suppose the deployed iterates satisfy $\|w_{t+1}-B(w_{t})\|_{q}\leq\eta_{t}$ with $\eta_{t}\geq 0$. Then, for every $t\geq 0$,

<table> <tbody><tr> <td></td> <td>$$\|w_{t}-w^{\star}\|_{q}\leq\alpha^{t}\|w_{0}-w^{\star}\|_{q}+\sum_{s=0}^{t-1}\alpha^{t-1-s}\eta_{s}.$$</td> <td></td></tr></tbody> </table>

If $\sup_{t}\eta_{t}\leq\bar{\eta}$, then $\limsup_{t\to\infty}\|w_{t}-w^{\star}\|_{q}\leq\bar{\eta}/(1-\alpha)$; if $\eta_{t}\to 0$, the iterates converge to $w^{\star}$.

In particular, suppose agent $i$ retrains to an exact minimizer $w_{i,t+1}$ of a differentiable empirical risk $\widehat{F}_{i,t}$ on $\mathbb{R}^{d_{i}}$. On any event where

<table> <tbody><tr> <td></td> <td>$$\sup_{u_{i}\in\mathbb{R}^{d_{i}}}\|\nabla\widehat{F}_{i,t}(u_{i})-\nabla_{u_{i}}F_{i}(u_{i};w_{t})\|\leq g_{i,t}\quad\text{for every }i,t,$$</td> <td></td></tr></tbody> </table>

the same conclusions hold with $\eta_{t}=\max_{i}g_{i,t}/(\mu_{i}q_{i})$.

###### Proof.

The triangle inequality and Theorem [4](https://amahrous.com/papers/reflexivity-threshold/#Thmtheorem4) give

<table> <tbody><tr> <td></td> <td>$$\|w_{t+1}-w^{\star}\|_{q}\leq\|w_{t+1}-B(w_{t})\|_{q}+\|B(w_{t})-B(w^{\star})\|_{q}\leq\eta_{t}+\alpha\|w_{t}-w^{\star}\|_{q}.$$</td> <td></td></tr></tbody> </table>

Iterating this inequality proves the bound. For bounded errors, the geometric sum is at most $\bar{\eta}/(1-\alpha)$. For vanishing errors, split the sum into a finite prefix, which vanishes as $t\to\infty$, and a tail bounded by $\sup_{s\geq S}\eta_{s}/(1-\alpha)$, then let $S\to\infty$.

For empirical retraining, first-order optimality gives $\nabla\widehat{F}_{i,t}(w_{i,t+1})=0$. Strong convexity of $F_{i}(\cdot;w_{t})$ and $\nabla_{u_{i}}F_{i}(B_{i}(w_{t});w_{t})=0$ imply

<table> <tbody><tr> <td></td> <td>$$\mu_{i}\|w_{i,t+1}-B_{i}(w_{t})\|\leq\|\nabla_{u_{i}}F_{i}(w_{i,t+1};w_{t})\|\leq g_{i,t}.$$</td> <td></td></tr></tbody> </table>

Dividing by $\mu_{i}q_{i}$ and maximizing over agents gives the claimed $\eta_{t}$. ∎

This is a conditional stability statement: obtaining probabilities or sample-size rates for the gradient-error event requires additional statistical assumptions on the losses and samples.

### NeurIPS Paper Checklist

1. 1. 

  Claims

2. Question: Do the main claims made in the abstract and introduction accurately reflect the paper’s contributions and scope?

3. Answer: \[Yes\]

4. Justification: The abstract and introduction state the main theoretical claims: the reflexivity matrix framework, the subcritical contraction result, and the supercritical lower bound. The scope is qualified through the stated assumptions, including strong convexity, exact best-response retraining, and decentralized local information.

5. Guidelines:

   
    - • 

      The answer \[N/A\]  means that the abstract and introduction do not include the claims made in the paper.

    - • 

      The abstract and/or introduction should clearly state the claims made, including the contributions made in the paper and important assumptions and limitations. A \[No\]  or \[N/A\]  answer to this question will not be perceived well by the reviewers.

    - • 

      The claims made should match theoretical and experimental results, and reflect how much the results can be expected to generalize to other settings.

    - • 

      It is fine to include aspirational goals as motivation as long as it is clear that these goals are not attained by the paper.

6. 2. 

  Limitations

7. Question: Does the paper discuss the limitations of the work performed by the authors?

8. Answer: \[Yes\]

9. Justification: The paper discusses limitations in Section 7.

10. Guidelines:

   
    - • 

      The answer \[N/A\]  means that the paper has no limitation while the answer \[No\]  means that the paper has limitations, but those are not discussed in the paper.

    - • 

      The authors are encouraged to create a separate “Limitations” section in their paper.

    - • 

      The paper should point out any strong assumptions and how robust the results are to violations of these assumptions (e.g., independence assumptions, noiseless settings, model well-specification, asymptotic approximations only holding locally). The authors should reflect on how these assumptions might be violated in practice and what the implications would be.

    - • 

      The authors should reflect on the scope of the claims made, e.g., if the approach was only tested on a few datasets or with a few runs. In general, empirical results often depend on implicit assumptions, which should be articulated.

    - • 

      The authors should reflect on the factors that influence the performance of the approach. For example, a facial recognition algorithm may perform poorly when image resolution is low or images are taken in low lighting. Or a speech-to-text system might not be used reliably to provide closed captions for online lectures because it fails to handle technical jargon.

    - • 

      The authors should discuss the computational efficiency of the proposed algorithms and how they scale with dataset size.

    - • 

      If applicable, the authors should discuss possible limitations of their approach to address problems of privacy and fairness.

    - • 

      While the authors might fear that complete honesty about limitations might be used by reviewers as grounds for rejection, a worse outcome might be that reviewers discover limitations that aren’t acknowledged in the paper. The authors should use their best judgment and recognize that individual actions in favor of transparency play an important role in developing norms that preserve the integrity of the community. Reviewers will be specifically instructed to not penalize honesty concerning limitations.

11. 3. 

  Theory assumptions and proofs

12. Question: For each theoretical result, does the paper provide the full set of assumptions and a complete (and correct) proof?

13. Answer: \[Yes\]

14. Justification: The theoretical results state their assumptions explicitly, including strong convexity, gradient sensitivity, unconstrained domains, smoothness, and the decentralized information model. Proofs are provided in the main text for the subcritical results, and the full proof of the lower bound is provided in Appendix A.

15. Guidelines:

   
    - • 

      The answer \[N/A\]  means that the paper does not include theoretical results.

    - • 

      All the theorems, formulas, and proofs in the paper should be numbered and cross-referenced.

    - • 

      All assumptions should be clearly stated or referenced in the statement of any theorems.

    - • 

      The proofs can either appear in the main paper or the supplemental material, but if they appear in the supplemental material, the authors are encouraged to provide a short proof sketch to provide intuition.

    - • 

      Inversely, any informal proof provided in the core of the paper should be complemented by formal proofs provided in appendix or supplemental material.

    - • 

      Theorems and Lemmas that the proof relies upon should be properly referenced.

16. 4. 

  Experimental result reproducibility

17. Question: Does the paper fully disclose all the information needed to reproduce the main experimental results of the paper to the extent that it affects the main claims and/or conclusions of the paper (regardless of whether the code and data are provided or not)?

18. Answer: \[Yes\]

19. Justification: The simulation setup details are described in Appendix [B](https://amahrous.com/papers/reflexivity-threshold/#A2). The simulation code, seeds, dependencies, and reproduction commands are provided in the supplementary material.

20. Guidelines:

   
    - • 

      The answer \[N/A\]  means that the paper does not include experiments.

    - • 

      If the paper includes experiments, a \[No\]  answer to this question will not be perceived well by the reviewers: Making the paper reproducible is important, regardless of whether the code and data are provided or not.

    - • 

      If the contribution is a dataset and/or model, the authors should describe the steps taken to make their results reproducible or verifiable.

    - • 

      Depending on the contribution, reproducibility can be accomplished in various ways. For example, if the contribution is a novel architecture, describing the architecture fully might suffice, or if the contribution is a specific model and empirical evaluation, it may be necessary to either make it possible for others to replicate the model with the same dataset, or provide access to the model. In general. releasing code and data is often one good way to accomplish this, but reproducibility can also be provided via detailed instructions for how to replicate the results, access to a hosted model (e.g., in the case of a large language model), releasing of a model checkpoint, or other means that are appropriate to the research performed.

    - • 

      While NeurIPS does not require releasing code, the conference does require all submissions to provide some reasonable avenue for reproducibility, which may depend on the nature of the contribution. For example

       
          1. (a) 

            If the contribution is primarily a new algorithm, the paper should make it clear how to reproduce that algorithm.

          2. (b) 

            If the contribution is primarily a new model architecture, the paper should describe the architecture clearly and fully.

          3. (c) 

            If the contribution is a new model (e.g., a large language model), then there should either be a way to access this model for reproducing the results or a way to reproduce the model (e.g., with an open-source dataset or instructions for how to construct the dataset).

          4. (d) 

            We recognize that reproducibility may be tricky in some cases, in which case authors are welcome to describe the particular way they provide for reproducibility. In the case of closed-source models, it may be that access to the model is limited in some way (e.g., to registered users), but it should be possible for other researchers to have some path to reproducing or verifying the results.

21. 5. 

  Open access to data and code

22. Question: Does the paper provide open access to the data and code, with sufficient instructions to faithfully reproduce the main experimental results, as described in supplemental material?

23. Answer: \[Yes\]

24. Justification: The simulations use synthetic matrices and do not rely on external datasets. The supplementary material includes the simulation code, seeds, dependencies, and instructions to reproduce Figure [1](https://amahrous.com/papers/reflexivity-threshold/#S6.F1).

25. Guidelines:

   
    - • 

      The answer \[N/A\]  means that paper does not include experiments requiring code.

    - • 

      Please see the NeurIPS code and data submission guidelines ([https://neurips.cc/public/guides/CodeSubmissionPolicy](https://neurips.cc/public/guides/CodeSubmissionPolicy)) for more details.

    - • 

      While we encourage the release of code and data, we understand that this might not be possible, so \[No\]  is an acceptable answer. Papers cannot be rejected simply for not including code, unless this is central to the contribution (e.g., for a new open-source benchmark).

    - • 

      The instructions should contain the exact command and environment needed to run to reproduce the results. See the NeurIPS code and data submission guidelines ([https://neurips.cc/public/guides/CodeSubmissionPolicy](https://neurips.cc/public/guides/CodeSubmissionPolicy)) for more details.

    - • 

      The authors should provide instructions on data access and preparation, including how to access the raw data, preprocessed data, intermediate data, and generated data, etc.

    - • 

      The authors should provide scripts to reproduce all experimental results for the new proposed method and baselines. If only a subset of experiments are reproducible, they should state which ones are omitted from the script and why.

    - • 

      At submission time, to preserve anonymity, the authors should release anonymized versions (if applicable).

    - • 

      Providing as much information as possible in supplemental material (appended to the paper) is recommended, but including URLs to data and code is permitted.

26. 6. 

  Experimental setting/details

27. Question: Does the paper specify all the training and test details (e.g., data splits, hyperparameters, how they were chosen, type of optimizer) necessary to understand the results?

28. Answer: \[Yes\]

29. Justification: Details needed to understand the results of the simulations are given in the main text. Appendix B specifies the full details for Figure 1. The code is also provided.

30. Guidelines:

   
    - • 

      The answer \[N/A\]  means that the paper does not include experiments.

    - • 

      The experimental setting should be presented in the core of the paper to a level of detail that is necessary to appreciate the results and make sense of them.

    - • 

      The full details can be provided either with the code, in appendix, or as supplemental material.

31. 7. 

  Experiment statistical significance

32. Question: Does the paper report error bars suitably and correctly defined or other appropriate information about the statistical significance of the experiments?

33. Answer: \[Yes\]

34. Justification: Panel [1(a)](https://amahrous.com/papers/reflexivity-threshold/#S6.F1.sf1) reports medians with interquartile bands across base matrices and initializations. Panel [1(b)](https://amahrous.com/papers/reflexivity-threshold/#S6.F1.sf2) reports mean log-distances with pointwise interquartile bands across the draws described in Appendix [B](https://amahrous.com/papers/reflexivity-threshold/#A2).

35. Guidelines:

   
    - • 

      The answer \[N/A\]  means that the paper does not include experiments.

    - • 

      The authors should answer \[Yes\]  if the results are accompanied by error bars, confidence intervals, or statistical significance tests, at least for the experiments that support the main claims of the paper.

    - • 

      The factors of variability that the error bars are capturing should be clearly stated (for example, train/test split, initialization, random drawing of some parameter, or overall run with given experimental conditions).

    - • 

      The method for calculating the error bars should be explained (closed form formula, call to a library function, bootstrap, etc.)

    - • 

      The assumptions made should be given (e.g., Normally distributed errors).

    - • 

      It should be clear whether the error bar is the standard deviation or the standard error of the mean.

    - • 

      It is OK to report 1-sigma error bars, but one should state it. The authors should preferably report a 2-sigma error bar than state that they have a 96% CI, if the hypothesis of Normality of errors is not verified.

    - • 

      For asymmetric distributions, the authors should be careful not to show in tables or figures symmetric error bars that would yield results that are out of range (e.g., negative error rates).

    - • 

      If error bars are reported in tables or plots, the authors should explain in the text how they were calculated and reference the corresponding figures or tables in the text.

36. 8. 

  Experiments compute resources

37. Question: For each experiment, does the paper provide sufficient information on the computer resources (type of compute workers, memory, time of execution) needed to reproduce the experiments?

38. Answer: \[No\]

39. Justification: The paper does not currently report compute resources for the simulations. Since the experiments are synthetic simulations rather than large-scale training runs, they can be reproduced with standard CPU resources; this is stated in Appendix B.

40. Guidelines:

   
    - • 

      The answer \[N/A\]  means that the paper does not include experiments.

    - • 

      The paper should indicate the type of compute workers CPU or GPU, internal cluster, or cloud provider, including relevant memory and storage.

    - • 

      The paper should provide the amount of compute required for each of the individual experimental runs as well as estimate the total compute.

    - • 

      The paper should disclose whether the full research project required more compute than the experiments reported in the paper (e.g., preliminary or failed experiments that didn’t make it into the paper).

41. 9. 

  Code of ethics

42. Question: Does the research conducted in the paper conform, in every respect, with the NeurIPS Code of Ethics [https://neurips.cc/public/EthicsGuidelines](https://neurips.cc/public/EthicsGuidelines)?

43. Answer: \[Yes\]

44. Justification: The work is theoretical and uses synthetic simulations only. It does not involve human subjects, private data, scraped data, deployed systems, or high-risk model release, and the authors have reviewed the NeurIPS Code of Ethics.

45. Guidelines:

   
    - • 

      The answer \[N/A\]  means that the authors have not reviewed the NeurIPS Code of Ethics.

    - • 

      If the authors answer \[No\] , they should explain the special circumstances that require a deviation from the Code of Ethics.

    - • 

      The authors should make sure to preserve anonymity (e.g., if there is a special consideration due to laws or regulations in their jurisdiction).

46. 10. 

  Broader impacts

47. Question: Does the paper discuss both potential positive societal impacts and negative societal impacts of the work performed?

48. Answer: \[No\]

49. Justification: The paper is foundational and is not tied to a deployed system. We do not identify a clear direct path to negative applications, and the paper does not include a dedicated discussion of positive and negative societal impacts.

50. Guidelines:

   
    - • 

      The answer \[N/A\]  means that there is no societal impact of the work performed.

    - • 

      If the authors answer \[N/A\]  or \[No\] , they should explain why their work has no societal impact or why the paper does not address societal impact.

    - • 

      Examples of negative societal impacts include potential malicious or unintended uses (e.g., disinformation, generating fake profiles, surveillance), fairness considerations (e.g., deployment of technologies that could make decisions that unfairly impact specific groups), privacy considerations, and security considerations.

    - • 

      The conference expects that many papers will be foundational research and not tied to particular applications, let alone deployments. However, if there is a direct path to any negative applications, the authors should point it out. For example, it is legitimate to point out that an improvement in the quality of generative models could be used to generate Deepfakes for disinformation. On the other hand, it is not needed to point out that a generic algorithm for optimizing neural networks could enable people to train models that generate Deepfakes faster.

    - • 

      The authors should consider possible harms that could arise when the technology is being used as intended and functioning correctly, harms that could arise when the technology is being used as intended but gives incorrect results, and harms following from (intentional or unintentional) misuse of the technology.

    - • 

      If there are negative societal impacts, the authors could also discuss possible mitigation strategies (e.g., gated release of models, providing defenses in addition to attacks, mechanisms for monitoring misuse, mechanisms to monitor how a system learns from feedback over time, improving the efficiency and accessibility of ML).

51. 11. 

  Safeguards

52. Question: Does the paper describe safeguards that have been put in place for responsible release of data or models that have a high risk for misuse (e.g., pre-trained language models, image generators, or scraped datasets)?

53. Answer: \[N/A\]

54. Justification: The paper does not release artifacts with substantial misuse risk. The only released artifacts are synthetic simulation code.

55. Guidelines:

   
    - • 

      The answer \[N/A\]  means that the paper poses no such risks.

    - • 

      Released models that have a high risk for misuse or dual-use should be released with necessary safeguards to allow for controlled use of the model, for example by requiring that users adhere to usage guidelines or restrictions to access the model or implementing safety filters.

    - • 

      Datasets that have been scraped from the Internet could pose safety risks. The authors should describe how they avoided releasing unsafe images.

    - • 

      We recognize that providing effective safeguards is challenging, and many papers do not require this, but we encourage authors to take this into account and make a best faith effort.

56. 12. 

  Licenses for existing assets

57. Question: Are the creators or original owners of assets (e.g., code, data, models), used in the paper, properly credited and are the license and terms of use explicitly mentioned and properly respected?

58. Answer: \[N/A\]

59. Justification: The paper does not use existing datasets, pretrained models, or third-party code assets as part of the research contribution. The work is theoretical and uses synthetic simulations.

60. Guidelines:

   
    - • 

      The answer \[N/A\]  means that the paper does not use existing assets.

    - • 

      The authors should cite the original paper that produced the code package or dataset.

    - • 

      The authors should state which version of the asset is used and, if possible, include a URL.

    - • 

      The name of the license (e.g., CC-BY 4.0) should be included for each asset.

    - • 

      For scraped data from a particular source (e.g., website), the copyright and terms of service of that source should be provided.

    - • 

      If assets are released, the license, copyright information, and terms of use in the package should be provided. For popular datasets, [paperswithcode.com/datasets](https://paperswithcode.com/datasets) has curated licenses for some datasets. Their licensing guide can help determine the license of a dataset.

    - • 

      For existing datasets that are re-packaged, both the original license and the license of the derived asset (if it has changed) should be provided.

    - • 

      If this information is not available online, the authors are encouraged to reach out to the asset’s creators.

61. 13. 

  New assets

62. Question: Are new assets introduced in the paper well documented and is the documentation provided alongside the assets?

63. Answer: \[Yes\]

64. Justification: The paper releases synthetic simulation code and seeds. These assets are accompanied by documentation describing the simulation procedure, dependencies, commands needed to reproduce the figures, and an appropriate license.

65. Guidelines:

   
    - • 

      The answer \[N/A\]  means that the paper does not release new assets.

    - • 

      Researchers should communicate the details of the dataset/code/model as part of their submissions via structured templates. This includes details about training, license, limitations, etc.

    - • 

      The paper should discuss whether and how consent was obtained from people whose asset is used.

    - • 

      At submission time, remember to anonymize your assets (if applicable). You can either create an anonymized URL or include an anonymized zip file.

66. 14. 

  Crowdsourcing and research with human subjects

67. Question: For crowdsourcing experiments and research with human subjects, does the paper include the full text of instructions given to participants and screenshots, if applicable, as well as details about compensation (if any)?

68. Answer: \[N/A\]

69. Justification: The paper does not involve crowdsourcing or research with human subjects.

70. Guidelines:

   
    - • 

      The answer \[N/A\]  means that the paper does not involve crowdsourcing nor research with human subjects.

    - • 

      Including this information in the supplemental material is fine, but if the main contribution of the paper involves human subjects, then as much detail as possible should be included in the main paper.

    - • 

      According to the NeurIPS Code of Ethics, workers involved in data collection, curation, or other labor should be paid at least the minimum wage in the country of the data collector.

71. 15. 

  Institutional review board (IRB) approvals or equivalent for research with human subjects

72. Question: Does the paper describe potential risks incurred by study participants, whether such risks were disclosed to the subjects, and whether Institutional Review Board (IRB) approvals (or an equivalent approval/review based on the requirements of your country or institution) were obtained?

73. Answer: \[N/A\]

74. Justification: The paper does not involve human subjects research, so IRB approval or equivalent review is not applicable.

75. Guidelines:

   
    - • 

      The answer \[N/A\]  means that the paper does not involve crowdsourcing nor research with human subjects.

    - • 

      Depending on the country in which research is conducted, IRB approval (or equivalent) may be required for any human subjects research. If you obtained IRB approval, you should clearly state this in the paper.

    - • 

      We recognize that the procedures for this may vary significantly between institutions and locations, and we expect authors to adhere to the NeurIPS Code of Ethics and the guidelines for their institution.

    - • 

      For initial submissions, do not include any information that would break anonymity (if applicable), such as the institution conducting the review.

76. 16. 

  Declaration of LLM usage

77. Question: Does the paper describe the usage of LLMs if it is an important, original, or non-standard component of the core methods in this research? Note that if the LLM is used only for writing, editing, or formatting purposes and does *not* impact the core methodology, scientific rigor, or originality of the research, declaration is not required.

78. Answer: \[N/A\]

79. Justification: The core methodology, theoretical results, simulations, and proofs do not use LLMs as an important, original, or non-standard research component. Any LLM use was limited to writing, editing, or formatting assistance and does not affect the scientific methodology.

80. Guidelines:

   
    - • 

      The answer \[N/A\]  means that the core method development in this research does not involve LLMs as any important, original, or non-standard components.

    - • 

      Please refer to our LLM policy in the NeurIPS handbook for what should or should not be described.

Last updated: October 2026.
