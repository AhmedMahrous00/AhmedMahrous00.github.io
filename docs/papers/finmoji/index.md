# FinMoji: A framework for emoji-driven sentiment analysis in financial social media

Source: [https://amahrous.com/papers/finmoji/](https://amahrous.com/papers/finmoji/)

[← Ahmed Mahrous’s homepage](https://amahrous.com/#research)

Ahmed Mahrous, Jens Schneider, and [Roberto Di Pietro](https://cemse.kaust.edu.sa/profiles/roberto-di-pietro)

*ACM Transactions on the Web, 20(3), Article 35* · 2026 · Q1 · IF 4.9

[PDF](https://amahrous.com/papers/finmoji/paper.pdf) · [Read full text](https://amahrous.com/papers/finmoji/#full-text) · [BibTeX](https://amahrous.com/papers/finmoji/citation.bib) · [DOI](https://doi.org/10.1145/3829331) · [arXiv](https://arxiv.org/abs/2605.09469) · [Code](https://github.com/AhmedMahrous00/finmoji_replication) · [Data](https://drive.google.com/drive/folders/1vqhm8Fxb9hOSRlsrdLqIsnJlIkYjXJgp?usp=sharing) · [Cite](https://amahrous.com/papers/finmoji/#citation)

## TL;DR

On about 528,000 emoji-containing StockTwits posts, emoji-only sentiment models reach F1 ≈ 0.75, versus ≈ 0.88 for text-and-emoji models, with substantially lower computational cost. Financial emoji usage also differs from general social-media usage.

## Abstract

This article explores the use of emojis in financial sentiment analysis, focusing on the social media platform StockTwits. Emojis, increasingly prevalent in digital communication, have potential as compact indicators of investor sentiment, which can be critical for predicting market trends. Our study examines whether emojis alone can serve as reliable proxies for financial sentiment and how they compare with traditional text-based analysis. We conduct a series of experiments using logistic regression and transformer models. We further analyze the performance, computational efficiency, and data requirements of emoji-based versus text-based sentiment classification. Using a balanced dataset of about 528,000 emoji-containing StockTwits posts, we find that emoji-only models achieve F1 ≈ 0.75, lower than text–emoji combined models (F1 ≈ 0.88) but with far lower computational cost—a useful feature where time is at a premium, such as in high-frequency trading. Furthermore, certain emojis and emoji pairs exhibit strong predictive power for market sentiment, demonstrating over 90% accuracy in predicting bullish or bearish trends. Finally, our research also reveals extreme statistical differences in emoji usage between financial and general social media contexts, stressing the need for domain-specific sentiment analysis models.

## Citation

Ahmed Mahrous, Jens Schneider, and Roberto Di Pietro. 2026. FinMoji: A framework for emoji-driven sentiment analysis in financial social media. ACM Transactions on the Web, 20(3), 1–30. [doi:10.1145/3829331](https://doi.org/10.1145/3829331).

```bibtex
@article{finmoji-2026,
  author = {Mahrous, Ahmed and Schneider, Jens and Di Pietro, Roberto},
  title = {{FinMoji: A framework for emoji-driven sentiment analysis in financial social media}},
  year = {2026},
  doi = {10.1145/3829331},
  publisher = {Association for Computing Machinery (ACM)},
  journal = {ACM Transactions on the Web},
  volume = {20},
  number = {3},
  pages = {1--30},
  url = {https://doi.org/10.1145/3829331}
}
```

## Full text

### 1. Introduction

Emojis have become a ubiquitous feature of human culture, acting as compact symbols that express a wide range of emotions, objects, ideas, and intentions in digital communication. More than 90% of the online population uses emojis ([Daniel, 2021](https://amahrous.com/papers/finmoji/#bib.bib20)). More than 20% of Tweets contain emojis ([Broni, 2021](https://amahrous.com/papers/finmoji/#bib.bib10)). Billions of emojis are sent daily on Facebook Messenger ([Burge, 2017](https://amahrous.com/papers/finmoji/#bib.bib13)). Emojis accompany around 40% of text on Instagram, with their usage rapidly increasing ([Dimson, 2015](https://amahrous.com/papers/finmoji/#bib.bib25)).

This proliferation of emojis is not confined to casual communications alone; the realm of financial social media has been impacted by emoji use as well. Emojis, now integral to the lexicon of online communication, can serve as highly valuable indicators to analyze financial contexts. They offer rich information about emotions and opinions of users, conveying investor sentiment and market perceptions ([Mahrous et al., 2023](https://amahrous.com/papers/finmoji/#bib.bib50); [Mahmoudi et al., 2022](https://amahrous.com/papers/finmoji/#bib.bib49)). This understanding of market sentiment can be highly valuable for predicting or analyzing market trends and can thus be used in trading algorithms, financial analysis, or investment strategies ([Bashir et al., 2024](https://amahrous.com/papers/finmoji/#bib.bib6); [jun Gu et al., 2024](https://amahrous.com/papers/finmoji/#bib.bib37)). VanEck’s Social Sentiment ETF<sup>[1](https://amahrous.com/papers/finmoji/#footnote1)</sup>, a fund with tens of millions of dollars, is solely based on investor sentiment aggregated from online sources such as social media. Financial social media sentiment indices are also strongly followed by market participants and offered by prestigious professional service firms such as Bloomberg and Thomson Reuters.

While emojis have been studied heavily in general contexts, they remain understudied in the context of financial social media. Financial social media involves a specialized vocabulary of words and symbols that largely differs from general-purpose use, necessitating context-specific analysis. Moreover, unlike previous studies that merely enhance textual sentiment analysis using emojis as additional features, our study shifts the focus to investigating emojis as standalone indicators of financial sentiment. Treating emojis as standalone indicators of financial sentiment is important for several reasons. If emojis alone can provide meaningful sentiment signals, they could serve as a more intuitive, faster, more efficient, and language-independent tool for financial analysis. Moreover, they could help analyze posts that do not include text but include only emojis.

Since emojis constitute a much smaller and simpler set of symbols compared to full text, processing them can be significantly faster. In fast-paced financial markets, where microseconds can make a difference in trading decisions, faster sentiment analysis can provide a significant competitive advantage ([Aquilina et al., 2022](https://amahrous.com/papers/finmoji/#bib.bib2)). Working with emojis reduces the complexity of the data, leading to more efficient algorithmic processing. With fewer unique symbols than there are words, models can be trained and deployed with lower computational overhead. This efficiency not only speeds up analysis but also reduces the costs associated with large-scale data processing. Due to the lower complexity, sentiment analysis models based solely on emojis might be effectively trained using smaller datasets than those required for text-based models. This could be especially advantageous in specialized contexts where large volumes of labeled data are hard to obtain. Emojis can also transcend language barriers because they are universally recognized symbols ([Kejriwal et al., 2021](https://amahrous.com/papers/finmoji/#bib.bib40); [Guntuku et al., 2019b](https://amahrous.com/papers/finmoji/#bib.bib33)). This means that sentiment analysis based solely on emojis can be applied globally without the need for translation or adaptation to different languages, making the analysis models more applicable in diverse international markets. Moreover, many social media posts, particularly on platforms where brevity is required, may consist mainly of emojis. By focusing on emojis as standalone sentiment indicators, analysts can capture the sentiment of these posts, which traditional text-based approaches would fail to analyze properly.

This leads us to the following research question.

What is the role of emojis in financial sentiment analysis, with respect to performance, computational efficiency, data requirements, patterns of use; and what are the differences between financial and generic use?

Specifically, we seek to answer the following sub-questions.

 
- Q1 

  How well can emojis alone serve as a proxy for public sentiment in finance?

- Q2 

  How does the computational speed of sentiment classification using only emojis compare to text-based methods?

- Q3 

  How much data is needed to successfully train logistic regression and transformer-based models to predict financial sentiment trends (“bullish”, “bearish”) in social media micro-messages using text-only, emoji-only, and text-with-emoji data?

- Q4 

  How significant is the difference in emoji usage between financial social media and non-financial social media?

#### 1.1. Contributions

Through addressing the mentioned research questions, we make the following contributions to the existing literature.

- • 

  Superior Financial Sentiment Classification Accuracy. Using a balanced dataset of 528,000 StockTwits posts (evenly split between bullish and bearish), our best text+emoji model achieves an F<sub>1</sub> score of 0.88, while the emoji-only variant reaches F${}_{1}\approx 0.75$. Although lower in accuracy, the emoji-only model retains most of the predictive power at a fraction of the computational and data demands, demonstrating that emojis alone encode substantial sentiment information in financial communication.

- • 

  Efficacy of Emoji-Only Models. We demonstrate that emoji-only models can achieve accuracy comparable to text-based models but at substantially lower data requirements. As little as 1,000 posts used for training can be sufficient to achieve competitive accuracy, but at a significantly decreased training and inference time (cf. Figs. [12](https://amahrous.com/papers/finmoji/#S7.F12) and [14](https://amahrous.com/papers/finmoji/#S7.F14)), especially if logistic regression is used. This gain in inference speed is highly relevant in contexts such as high-frequency trading.

- • 

  Robust Emoji Sentiment Lexicon Construction. We employ a simple yet effective method to develop an emoji sentiment lexicon. In Section [6](https://amahrous.com/papers/finmoji/#S6), we demonstrate that certain emojis and emoji pairs have strong predictive power (above 90%) for sentiment classification. This facilitates rapid sentiment analysis.

- • 

  Distinct Emoji Usage Patterns in Financial Contexts. We identify extreme differences in emoji usage between financial and general social media contexts (cf. Section [5](https://amahrous.com/papers/finmoji/#S5)). Compared to previous research, our method related to this difference is more direct and explainable.

- • 

  Analysis of Various Machine Learning Models. We also evaluate various models, highlighting the efficiency of logistic regression compared to transformers in emoji analysis and addressing tokenization issues in Hugging Face models (cf. Subsection [7.2](https://amahrous.com/papers/finmoji/#S7.SS2)).

- • 

  Data Sharing.The code and data needed to replicate our results are publicly available at [https://github.com/AhmedMahrous00/finmoji\_replication](https://github.com/AhmedMahrous00/finmoji_replication).

#### 1.2. Organization

The rest of this paper is organized as follows. Section [2](https://amahrous.com/papers/finmoji/#S2) presents existing research on emojis in sentiment analysis, particularly within the financial domain, highlighting key gaps that our paper addresses. Section [3](https://amahrous.com/papers/finmoji/#S3) details our methodology and data, including data collection, pre-processing, and a section-by-section description of the methodologies employed. Section [4](https://amahrous.com/papers/finmoji/#S4) provides a descriptive analysis of emoji usage in our StockTwits data, detailing trends in emoji frequency, sentiment-based emoji distributions, and the comparative complexity of textual versus emoji data. This section motivates the value of incorporating emojis in financial sentiment analysis. Section [5](https://amahrous.com/papers/finmoji/#S5) compares emoji usage patterns between StockTwits and $\mathbb{X}$ (formerly Twitter)<sup>[2](https://amahrous.com/papers/finmoji/#footnote2)</sup>, showcasing differences in emoji distributions and statistical tests. This section motivates the importance of developing models specific to financial platforms like StockTwits, rather than applying models designed for general social media platforms such as $\mathbb{X}$ (Twitter). To further illustrate the value of emojis in financial sentiment analysis, Section [6](https://amahrous.com/papers/finmoji/#S6) demonstrates single and pair emoji sentiment polarity by assessing their presence in bullish versus bearish posts. Section [7](https://amahrous.com/papers/finmoji/#S7) compares the accuracy and speed of various sentiment analysis algorithms applied to text and emoji data. Subsection [7.1](https://amahrous.com/papers/finmoji/#S7.SS1) evaluates the performance of logistic regression models trained on text, emojis, and a combination of both. Subsection [7.2](https://amahrous.com/papers/finmoji/#S7.SS2) replicates the analysis for a transformer-based model. This subsection also explores the impact of training sample size and sequence length on model performance. Subsection [7.3](https://amahrous.com/papers/finmoji/#S7.SS3) presents the performance of various machine learning models for emoji-based sentiment analysis, demonstrating the consistency and robustness of our findings across different models. Subsection [7.4](https://amahrous.com/papers/finmoji/#S7.SS4) compares the performance of various transformer-based sentiment analysis models on text and emoji data, demonstrating the rationale for selecting Twitter-RoBERTa as the primary model. Section [8](https://amahrous.com/papers/finmoji/#S8) synthesizes the key findings of this study, explores their implications, acknowledges limitations, and outlines potential directions for future research. Section [10](https://amahrous.com/papers/finmoji/#S10) concludes.

### 2. Related Work

Sentiment analysis of social media microblogs proved valuable across diverse domains, such as politics, marketing, and finance ([Du et al., 2024](https://amahrous.com/papers/finmoji/#bib.bib26); [Demirel et al., 2025](https://amahrous.com/papers/finmoji/#bib.bib23); [Gündüz and Demirel, 2025](https://amahrous.com/papers/finmoji/#bib.bib31)). Researchers have employed both lexicon-based techniques (e.g., VADER, NRC, SO-CAL) ([Kahraman et al., 2025](https://amahrous.com/papers/finmoji/#bib.bib38); [Kahraman-Gokalp et al., 2024](https://amahrous.com/papers/finmoji/#bib.bib39)) and advanced deep learning models (e.g., BERT transformers) ([Gardazi et al., 2025](https://amahrous.com/papers/finmoji/#bib.bib29)) to interpret microblogs’ sentiment. The advantage of lexicon-based techniques is that they are generally more interpretable and significantly faster/cheaper ([van der Veen and Bleich, 2025](https://amahrous.com/papers/finmoji/#bib.bib68)).

The value of emojis in sentiment analysis is increasingly gaining attention ([Zhou et al., 2024](https://amahrous.com/papers/finmoji/#bib.bib70)). While extensive research has explored the use of emojis in general contexts, their application in financial sentiment analysis remains less examined. This section synthesizes related research, highlights gaps, and reviews the studies that are most closely related to our work.

Research on the use of emojis in financial sentiment analysis is relatively scarce. We identified only approximately 40 publications that mention emojis in the context of finance. Most of this work uses emojis in addition to text to enhance sentiment analysis. Several studies ([Mahmoudi et al., 2018](https://amahrous.com/papers/finmoji/#bib.bib48); [Omar and Lasrado, 2023](https://amahrous.com/papers/finmoji/#bib.bib54); [Renault, 2020](https://amahrous.com/papers/finmoji/#bib.bib55)) demonstrate that the inclusion of emojis can significantly improve the accuracy of investor sentiment analysis.

Emojis have also been found useful in predictive systems for financial markets. For example, [Gálvez and Gravano (2017)](https://amahrous.com/papers/finmoji/#bib.bib28) analyze financial sentiment on an Argentinean stock message board, converting emojis to textual descriptions during preprocessing. They find that emojis are valuable features for predicting stock prices. Similarly, [Reschke and Strych (2024)](https://amahrous.com/papers/finmoji/#bib.bib56) demonstrate that emojis, even when analyzed independently of text, possess standalone predictive value for stock prices based on their analysis of financial posts on Reddit. [Vamossy (2021)](https://amahrous.com/papers/finmoji/#bib.bib67) uses emojis to help classify StockTwits posts into seven emotional states: neutral, happy, sad, anger, disgust, surprise, and fear. His analysis shows that these emotional states are predictive of company earnings and stock returns. For cryptocurrency markets, [Zuo et al. (2024)](https://amahrous.com/papers/finmoji/#bib.bib71) utilize GPT-4 and BERT to analyze emoji sentiment on Twitter and demonstrate its predictive power for Bitcoin price movements and market volatility.

Furthermore, emojis contribute to the credibility assessment of financial social media accounts. [Bouadjenek et al. (2023)](https://amahrous.com/papers/finmoji/#bib.bib9) discover distinct emoji usage patterns among StockTwits users who are more credible and give more accurate stock market predictions. [Shiri et al. (2023)](https://amahrous.com/papers/finmoji/#bib.bib61) extend this to Twitter, suggesting that emoji usage can be used to distinguish between genuine and spam posts on financial social media.

The inclusion of emojis into sentiment lexicons tailored for financial social media has been another topic of research. Chen et al. ([Chen et al., 2018a](https://amahrous.com/papers/finmoji/#bib.bib14); [Chen et al., 2019](https://amahrous.com/papers/finmoji/#bib.bib15)) have constructed a sentiment dictionary for StockTwits, incorporating 115 emojis, to capture the sentiment of financial social media. [Kulakowski and Frasincar (2023)](https://amahrous.com/papers/finmoji/#bib.bib43) develop a “language-universal cryptocurrency emoji sentiment lexicon”, abstracting from the natural language used in posts.

Table [1](https://amahrous.com/papers/finmoji/#S2.T1) lists eight papers—filtered from the broader research work—that are most relevant to our research, as they utilize emojis in sentiment analysis algorithms for financial social media.

Table 1. Review of Sentiment Analysis Studies Using Emojis in Financial Contexts. This table compares various sentiment analysis models across different studies, stating the models used, test data size, data sources, highest recorded accuracies, and whether they address sub-questions Q1 to Q4 (cf. Section [1](https://amahrous.com/papers/finmoji/#S1)). Abbreviations: NB = Naïve Bayes, Reg = Regression, SVM = Support Vector Machine, RF = Random Forest, MLP = Multilayer Perceptron, RNN = Recurrent Neural Network, CNN = Convolutional Neural Network, Tr = Transformer, Rule = Rule-based Algorithm. “k” stands for thousand; “unbal/bal” refers to unbalanced/balanced datasets; AC = accuracy; AUC = area under the curve; MCC = Matthews correlation coefficient; F<sub>1</sub> = F<sub>1</sub> Score. The test data size and performance are recorded for emoji-only analysis if the study includes such analysis and for text-with-emoji analysis otherwise. The highest achieved performance is recorded for studies with different models. Our models reach the highest reported performance (F<sub>1</sub> = 0.88) among all reviewed works.

<table> <tr> <th scope="col">Ref.</th> <th scope="col">Models</th> <th scope="col">Source</th> <th scope="col">Test Data</th> <th scope="col">Performance</th> <th scope="col">Q1</th> <th scope="col">Q2</th> <th scope="col">Q3</th> <th scope="col">Q4</th> <th scope="col">EmojiOnly</th> <th scope="col">TextOnly</th> <th scope="col">Text+Emoji</th></tr> <tr> <td>(<a href="https://amahrous.com/papers/finmoji/#bib.bib55">Renault, 2020</a>)</td> <td>  NB, Reg<br> SVM, RF<br> MLP </td> <td>StockTwits</td> <td>250k (bal.)</td> <td>  0.50 MCC </td> <td>✗</td> <td>✗</td> <td>✓</td> <td>✗</td> <td>✗</td> <td>✓</td> <td>✓</td></tr> <tr> <td>(<a href="https://amahrous.com/papers/finmoji/#bib.bib48">Mahmoudi et al., 2018</a>)</td> <td>  NB, Reg,<br> SVM, RNN,<br> CNN </td> <td>StockTwits</td> <td>  566k (unbal.)<br> 434k (bal.) </td> <td>0.49 MCC</td> <td>✗</td> <td>✗</td> <td>✗</td> <td>✓</td> <td>✗</td> <td>✓</td> <td>✓</td></tr> <tr> <td>(<a href="https://amahrous.com/papers/finmoji/#bib.bib53">Nasekin and Chen, 2020</a>)</td> <td>RNN</td> <td>StockTwits</td> <td>564k (unbal.)</td> <td>  0.90 F<sub>1</sub> (bullish)<br> 0.58 F<sub>1</sub> (bearish) </td> <td>✗</td> <td>✗</td> <td>✗</td> <td>✗</td> <td>✗</td> <td>✗</td> <td>✓</td></tr> <tr> <td>(<a href="https://amahrous.com/papers/finmoji/#bib.bib69">Wilksch and Abramova, 2023</a>)</td> <td>  Tr, Reg,<br> SVM, Rule </td> <td>  $\mathbb{X}$ (Twitter)<br> StockTwits </td> <td>  2,500<br> 2,510 </td> <td>  0.83 AUC<br> 0.73 AUC </td> <td>✗</td> <td>✗</td> <td>✗</td> <td>✓</td> <td>✗</td> <td>✗</td> <td>✓</td></tr> <tr> <td>(<a href="https://amahrous.com/papers/finmoji/#bib.bib14">Chen et al., 2018a</a>)</td> <td>Rule</td> <td>StockTwits</td> <td>2,030 (unbal.)</td> <td>0.40 F1</td> <td>✗</td> <td>✗</td> <td>✗</td> <td>✓</td> <td>✗</td> <td>✗</td> <td>✓</td></tr> <tr> <td>(<a href="https://amahrous.com/papers/finmoji/#bib.bib43">Kulakowski and Frasincar, 2023</a>)</td> <td>Tr, SVM</td> <td>StockTwits</td> <td>11,984 (unbal.)</td> <td>0.48 F1</td> <td>✓</td> <td>✗</td> <td>✗</td> <td>✗</td> <td>✓</td> <td>✓</td> <td>✗</td></tr> <tr> <td>(<a href="https://amahrous.com/papers/finmoji/#bib.bib49">Mahmoudi et al., 2022</a>)</td> <td>  SVM, Reg,<br> RF </td> <td>StockTwits</td> <td>Undeclared</td> <td>  0.47 F1 </td> <td>✓</td> <td>✗</td> <td>✗</td> <td>✓</td> <td>✓</td> <td>✓</td> <td>✓</td></tr> <tr> <td>Ours</td> <td>Tr, Reg</td> <td>StockTwits</td> <td>528k (bal.)</td> <td>0.88 F1</td> <td>✓</td> <td>✓</td> <td>✓</td> <td>✓</td> <td>✓</td> <td>✓</td> <td>✓</td></tr> </table>

[Renault (2020)](https://amahrous.com/papers/finmoji/#bib.bib55) analyzes a balanced dataset of 1 million StockTwits posts, finding that including emojis, punctuation, and bigrams significantly enhances sentiment classification accuracy. Notably, his findings suggest that more complex and time-consuming methods, such as random forests or neural networks, do not necessarily outperform simpler approaches like multinomial Naïve Bayes or logistic regression. Furthermore, he observes diminishing increases in sentiment classification accuracy with increasing data sizes. A critical aspect of Renault’s research is his meticulous evaluation of different preprocessing techniques, revealing that standard tasks such as removing stopwords using the NLTK<sup>[3](https://amahrous.com/papers/finmoji/#footnote3)</sup> stopwords corpus, Part-Of-Speech (POS) tagging, and stemming fail to improve or even negatively impact accuracy in financial social media ([Renault, 2020](https://amahrous.com/papers/finmoji/#bib.bib55)).

Similarly, [Mahmoudi et al. (2018)](https://amahrous.com/papers/finmoji/#bib.bib48) utilize a vast StockTwits dataset, which exceeds 63 million posts, to develop a state-of-the-art sentiment classifier for financial social media. They report a significant improvement in accuracy, with a 44–47% higher Matthews correlation coefficient (MCC) ([Matthews, 1975](https://amahrous.com/papers/finmoji/#bib.bib52)) when emojis are included. Contrary to Renault’s findings ([Renault, 2020](https://amahrous.com/papers/finmoji/#bib.bib55)), they demonstrate that neural networks outperform simpler methods in financial sentiment analysis. Furthermore, they emphasize the importance of domain-specific models for financial social media sentiment analysis, showing that domain-specific word embeddings significantly outperform general-domain ones.

[Wilksch and Abramova (2023)](https://amahrous.com/papers/finmoji/#bib.bib69) utilize a much smaller dataset of 10,000 financial posts on Twitter, which are manually labeled by the authors, to experiment with different sentiment classification models and to develop their own. They affirm that domain-specific models perform significantly better than “generic off-the-shelf models like VADER ([Hutto and Gilbert, 2014](https://amahrous.com/papers/finmoji/#bib.bib36)),” thus reinforcing the importance of tailored approaches in financial sentiment analysis. In a similar observation to that of [Renault (2020)](https://amahrous.com/papers/finmoji/#bib.bib55), they demonstrate that simpler models, such as logistic regression, can match the accuracy of more complex models like deep neural networks, but with greater computational efficiency and reduced risks of overfitting. However, they also note significant limitations with logistic regression, particularly its shortcomings in learning more complex word dependencies, such as negation, which could impair its performance in analyzing certain posts. Furthermore, their research reveals that models trained on data from financial Twitter posts underperform when applied to StockTwits data, illustrating the challenge of platform dependency in sentiment analysis.

[Nasekin and Chen (2020)](https://amahrous.com/papers/finmoji/#bib.bib53) also explore developing a sentiment classifier for financial social media, utilizing around 560,000 labeled StockTwits posts. They incorporate emojis in their model and manage to achieve their highest F<sub>1</sub> score of 0.90 using an LSTM ([Hochreiter and Schmidhuber, 1997](https://amahrous.com/papers/finmoji/#bib.bib35); [Gers et al., 2000](https://amahrous.com/papers/finmoji/#bib.bib30)) model, but their model is heavily skewed towards bullish sentiment, achieving a low F<sub>1</sub> score of only 0.58 on bearish posts. [Chen et al. (2018a)](https://amahrous.com/papers/finmoji/#bib.bib14) utilize 334,000 labeled StockTwits posts to construct a financial microblogging sentiment dictionary. Their dictionary includes more than 100 emojis and performs better than the seminal dictionary developed on formal financial texts by [Loughran and McDonald (2011)](https://amahrous.com/papers/finmoji/#bib.bib45).

While the previously-mentioned studies incorporate emojis alongside text in their models, the studies by [Kulakowski and Frasincar (2023)](https://amahrous.com/papers/finmoji/#bib.bib43) and [Mahmoudi et al. (2022)](https://amahrous.com/papers/finmoji/#bib.bib49) uniquely stand out within our review. They are the only ones who test financial sentiment analysis using emojis exclusively, without any accompanying text.

[Kulakowski and Frasincar (2023)](https://amahrous.com/papers/finmoji/#bib.bib43) fine-tune the transformer-based BERTweet ([Dat Quoc et al., 2020](https://amahrous.com/papers/finmoji/#bib.bib21)) model utilizing 1.875 million posts (labeled and unlabeled) from StockTwits. They also develop a language-universal cryptocurrency emoji (LUKE) sentiment lexicon using 91,758 StockTwits posts. They tested sentiment analysis using only this emoji lexicon for sentiment analysis, but achieved a low F<sub>1</sub> score of 0.4816.

[Mahmoudi et al. (2022)](https://amahrous.com/papers/finmoji/#bib.bib49) utilize more than 6 million StockTwits posts (each containing at least one emoji) to perform a comprehensive study of emojis in financial social media. They show that using domain-specific (in contrast to domain-independent) emoji embeddings is highly valuable for both sentiment classification and price predictions. They also demonstrate the significant difference between financial and general emojis using cluster analysis. They develop an emoji sentiment lexicon and use emoji-only data to test their sentiment analysis algorithm. However, they only achieve relatively low accuracy, with an F<sub>1</sub> score of 0.39.

While these works show that emojis are useful for sentiment analysis, significant gaps and limitations still exist within this area of study. Firstly, there is a noticeable inconsistency in the methodologies used across studies. For instance, the sentiment analysis problem is converted to binary classification in some studies and non-binary in others. Different studies also employ various balancing techniques, choosing to oversample, undersample, or analyze unbalanced data. Furthermore, the accuracy metrics reported are often inconsistent, hindering direct comparisons. The wide variety of model specifications and pre-processing options contributes to this inconsistency. With respect to emojis, some studies convert them to their textual descriptions, while others treat them as independent symbols. Additionally, some studies use domain-general models such as VADER ([Hutto and Gilbert, 2014](https://amahrous.com/papers/finmoji/#bib.bib36)), which have been shown to be less effective in financial sentiment analysis. Many of the studies also rely on relatively small and unbalanced datasets, which limits the robustness and generalizability of their findings. The lack of standardization and oversight of critical details in methodologies contributes to varying sentiment classification accuracies, with some papers achieving very low accuracy.

Among the many gaps existent around this topic, the ones focused on in our analysis (and listed in our research sub-questions), remain insufficiently addressed. While [Kulakowski and Frasincar (2023)](https://amahrous.com/papers/finmoji/#bib.bib43) and [Mahmoudi et al. (2022)](https://amahrous.com/papers/finmoji/#bib.bib49) have addressed sub-question Q1, they have achieved very low accuracy in their sentiment classification. [Mahmoudi et al. (2022)](https://amahrous.com/papers/finmoji/#bib.bib49) also address this gap very briefly as a side-analysis of their other main ideas and, therefore, ignore mentioning many details. [Renault (2020)](https://amahrous.com/papers/finmoji/#bib.bib55) addresses sub-question Q3 only partially, not testing the dataset size requirements of using emojis-only or text-only data. [Renault (2020)](https://amahrous.com/papers/finmoji/#bib.bib55) also does not mention whether the test set was kept fixed for all the dataset sizes, a crucial detail of such an experiment. Sub-question Q4 has been addressed more extensively than the other sub-questions. However, most of the papers addressing it compare models using combined text and emoji data. Only [Mahmoudi et al. (2022)](https://amahrous.com/papers/finmoji/#bib.bib49) focus exclusively on emojis, using a different methodology than ours. We believe that our methodology, presented in Section [5](https://amahrous.com/papers/finmoji/#S5), can help demonstrate and quantify the difference in emoji usage between domains in a more explainable manner. To the best of our knowledge, no study other than ours has addressed sub-question Q2.

#### Summary of Novelty.

In summary, our main contributions are demonstrating the *effectiveness and efficiency* of emoji-only sentiment analysis models in the context of financial social media. Most prior finance sentiment studies augment text with emojis but do not investigate an emoji-only model (e.g., [Renault (2020)](https://amahrous.com/papers/finmoji/#bib.bib55)). In contrast, we evaluate emoji-only, text-only, and text+emoji models. As summarized in Table [1](https://amahrous.com/papers/finmoji/#S2.T1), our models achieve a markedly higher overall performance (F<sub>1</sub> = 0.88) than all prior studies, most of which report F<sub>1</sub> scores or equivalent metrics below 0.50 on data sources similar ours. To the best of our knowledge, only [Mahmoudi et al. (2022)](https://amahrous.com/papers/finmoji/#bib.bib49) and [Kulakowski and Frasincar (2023)](https://amahrous.com/papers/finmoji/#bib.bib43) attempt emoji-only analysis, both being lexicon-based and both achieving F<sub>1</sub> $<0.5$. Relative to them, we show substantially stronger emoji-only effectiveness with F<sub>1</sub> $\approx 0.75$. Notably, we find that a simple Logistic Regression model performs on par with a Transformer model in the emoji-only setting (F${}_{1}{=}0.76$ in both cases), highlighting that emoji sentiment signals are linearly separable and do not require deep contextual embeddings.   
In addition, we introduce formal cross-domain tests to compare between financial and non-financial social media, motivating finance-specific analysis—something prior studies did not do. We also provide practical insights, including a tokenizer audit across BERT-family models showing that most mistreat emojis, while Twitter-RoBERTa preserves them; such guidance can inform future sentiment-analysis research. While the previous two papers intuitively argue for the efficiency of using emojis, they do not empirically demonstrate it. We do, providing an integrated efficiency study: computational efficiency measurements (training/inference time), learning curves showing reduced data needs—an important advantage in data-scarce contexts—and context-length sensitivity demonstrating that emoji-only peaks at short contexts, further strengthening the efficiency argument. Taken together, our results demonstrate the effectiveness and efficiency of using emoji-only models in financial social media sentiment analysis in a way that previous studies did not.

### 3. Data and Methods

In this section, we describe our data and discuss the methodologies used in the different sections of this paper.

#### 3.1. Data

We begin by gathering 18.5 million posts that were published by users on the social media platform StockTwits. Each one of these posts had the cash tag of at least one stock or cryptocurrency. As detailed in Table [2](https://amahrous.com/papers/finmoji/#S3.T2), the composition of our sample mirrors the platform’s user interests, with a significant portion dedicated to discussions surrounding the S&P 500 index, major cryptocurrencies like Bitcoin, and popular meme stocks and coins such as GameStop and Dogecoin. The remaining posts encompass conversations about large-cap stocks like Apple, established cryptocurrencies like Ethereum, and indices tracking assets like gold.

Table 2. Distribution of Posts by Financial Asset. This table illustrates the percentage of posts within our dataset mentioning particular financial assets.

<table> <tr> <th scope="col"></th> <th scope="col">S&amp;P 500</th> <th scope="col">Bitcoin</th> <th scope="col">Dogecoin</th> <th scope="col">Apple</th> <th scope="col">GameStop</th> <th scope="col">Shiba Inu</th> <th scope="col">Others</th></tr> <tr> <td>Percentage</td> <td>33%</td> <td>15%</td> <td>12%</td> <td>10%</td> <td>7%</td> <td>7%</td> <td>16%</td></tr> </table>

Spanning from February 2009 to October 2022, our dataset provides a comprehensive view of financial social media activities over time. Fig. [1](https://amahrous.com/papers/finmoji/#S3.F1) illustrates the distribution of posts by year, highlighting the surge in activity from 2018 onwards, with 2021 accounting for nearly half of the total posts. We attribute this to the COVID-19 pandemic, with lockdowns and home offices driving the population of many countries into a more online-centric lifestyle, paired with shop closures making spending money in physical outlets harder or impossible.

![Figure 1 . Distribution of Posts by Year of Publishing. This figure shows the percentage of total posts per year from 2009 to 2022 within our dataset.](https://amahrous.com/papers/finmoji/figures/PostsByYear.webp) 

Figure 1. Distribution of Posts by Year of Publishing. This figure shows the percentage of total posts per year from 2009 to 2022 within our dataset.

While our initial dataset comprises 18.5 million posts, only 14% incorporate emojis, narrowing our focus to approximately 2.5 million posts. Further refinement was necessary as not all posts included user-labeled sentiment, a crucial element for supervised machine learning. This results in a subset of 1.7 million labeled posts. However, a significant imbalance is present, with bullish sentiment dominating at 85%. To some extent, this aligns with the global economic situation of that time—The S&P 500 doubled from 2018 to 2021, gaining 28.7% in 2021 alone. However, such an imbalance, whether rooted in economic reasons or not, hinders the generalization of a model, especially when market trends change. Thus, to ensure the effectiveness of our sentiment analysis algorithms, we opted to balance the data by undersampling the majority class. Consequently, our final dataset contains 528,000 posts evenly split between bullish and bearish sentiment, each containing at least one emoji and referencing a specific stock or cryptocurrency via hashtag. Fig. [2](https://amahrous.com/papers/finmoji/#S3.F2) illustrates our process.

![Figure 2 . Data Filtration Process. This series of pie charts illustrates the progressive stages of data filtering from the initial dataset to the final balanced sample. Colors represent sentiment classification: green f](https://amahrous.com/papers/finmoji/figures/mergedPiesArrows.webp) 

Figure 2. Data Filtration Process. This series of pie charts illustrates the progressive stages of data filtering from the initial dataset to the final balanced sample. Colors represent sentiment classification: green for bullish, red for bearish, and grey for unlabeled posts.

Several factors motivated our choice of StockTwits as the data source. Primarily, StockTwits offers a unique advantage in that it allows users to explicitly label their posts with their sentiment—either bullish, indicating an expectation of price increases, or bearish, suggesting anticipated price declines. This readily available sentiment data proves invaluable for training supervised learning algorithms. Furthermore, research has demonstrated that StockTwits data exhibits a lower prevalence of low-quality content, such as spam, compared to platforms like Twitter, as evidenced by [Bouadjenek et al. (2023)](https://amahrous.com/papers/finmoji/#bib.bib9).

Fig. [3](https://amahrous.com/papers/finmoji/#S3.F3) provides a visual representation of StockTwits user demographics based on data from web analytics company Similarweb ([SimilarWeb, 2023](https://amahrous.com/papers/finmoji/#bib.bib62)). Notably, the platform exhibits a predominantly male user base. The age distribution is relatively diverse, with the largest segment comprising adults aged 25 to 44. Users primarily hail from English-speaking countries, particularly the USA, which aligns with the overwhelming majority of posts being in English. This demographic information is pertinent to our analysis as research has shown that informal language and emoji usage on social media can vary significantly across genders, age groups, and cultures ([Kejriwal et al., 2021](https://amahrous.com/papers/finmoji/#bib.bib40); [Chen et al., 2024](https://amahrous.com/papers/finmoji/#bib.bib16); [Chen et al., 2018b](https://amahrous.com/papers/finmoji/#bib.bib17)).

![Figure 3 . Demographic Breakdown of StockTwits Users. This figure illustrates the demographic composition of StockTwits users, highlighting gender distribution, age groups, and geographic locations. Data sourced from ( S](https://amahrous.com/papers/finmoji/figures/StockTwitsDemographics.webp) 

Figure 3. Demographic Breakdown of StockTwits Users. This figure illustrates the demographic composition of StockTwits users, highlighting gender distribution, age groups, and geographic locations. Data sourced from ([SimilarWeb, 2023](https://amahrous.com/papers/finmoji/#bib.bib62)).

#### 3.2. Methodologies

##### 3.2.1. Emoji Usage: Descriptive Analysis

Section [4](https://amahrous.com/papers/finmoji/#S4) investigates emoji usage patterns within our StockTwits dataset. We analyze the distribution of emojis per post, considering both unique and total occurrences, as depicted in Fig. [5](https://amahrous.com/papers/finmoji/#S4.F5). This figure further illustrates the average monthly emoji usage from February 2009 to July 2022, encompassing all 18.5 million posts. To visualize emoji prevalence, we generate emoji clouds (Fig. [6](https://amahrous.com/papers/finmoji/#S4.F6)) using the wordcloud package<sup>[4](https://amahrous.com/papers/finmoji/#footnote4)</sup> and the Symbola font for the emojis, focusing on the 2.6 million posts containing emojis. Lastly, Table [3](https://amahrous.com/papers/finmoji/#S4.T3) presents percentile distributions for the number of textual characters and emojis based on the balanced subset of 528,000 emoji-containing posts.

##### 3.2.2. Emoji Usage: StockTwits versus $\mathbb{X}$ (Twitter)

Section [5](https://amahrous.com/papers/finmoji/#S5) compares emoji usage between StockTwits and $\mathbb{X}$ (Twitter). We analyze our StockTwits dataset alongside a publicly available Twitter dataset<sup>[5](https://amahrous.com/papers/finmoji/#footnote5)</sup>, employing the Mann-Whitney U ([Mann and Whitney, 1947](https://amahrous.com/papers/finmoji/#bib.bib51)) and Kolmogorov-Smirnov ([Berger and Zhou, 2014](https://amahrous.com/papers/finmoji/#bib.bib8); [Smirnov, 1948](https://amahrous.com/papers/finmoji/#bib.bib64)) tests to assess differences in the relative frequency distributions of emojis. To test distributional differences in emoji use across platforms, we also compute the chi-square statistic and its effect size via Cramér’s $V$ ([Cramér, 1946](https://amahrous.com/papers/finmoji/#bib.bib19)):

<table> <tbody><tr> <td rowspan="1">(1)</td> <td></td> <td>$\displaystyle V$</td> <td>$\displaystyle=\sqrt{\chi^{2}/\left(n\times\min\left(k-1,r-1\right)\right)},$</td> <td></td></tr></tbody> </table>

where $n$ is the total observation count and $k$ and $r$ are the numbers of columns and rows. In our case, columns and rows correspond to platform and emoji occurrences. This approach is appropriate because both variables are categorical; the chi-square test assesses whether their distributions differ beyond random variation, while Cramér’s $V$ quantifies the strength of this association on a standardized $[0,1]$ scale. To compare datasets of equal sample sizes, we randomly sampled 2.6 million tweets from the larger Twitter dataset. 2.6 million is also the number of StockTwits posts in our dataset containing at least one emoji. The tests focus on the presence of emojis within posts, disregarding the number of repetitions. For these tests, our analysis considers the presence of an emoji within a post rather than its frequency, meaning that multiple occurrences of the same emoji within a single post are counted only once.

##### 3.2.3. Emoji Sentiment Scores

Section [6](https://amahrous.com/papers/finmoji/#S6) focuses on assessing the sentiment associated with individual emojis. We analyze the 528,000 user-labeled posts containing emojis, focusing on the 50 most frequently used emojis while disregarding multiple occurrences within a single post. For each of these emojis, we calculate a bullish and bearish sentiment score using the following formula.

<table> <tbody><tr> <td></td> <td>Bullish (Bearish) Sentiment Score</td> <td>$\displaystyle=\frac{\text{Number of bullish (bearish) posts containing the emoji}}{\text{Total number of posts containing the emoji}}$</td> <td></td></tr></tbody> </table>

This approach provides a simple yet robust measure of the sentiment conveyed by each emoji.

Focusing on the top 50 most frequently used emojis enhances the reliability of our analysis, as less frequent emojis exhibit greater volatility in their sentiment scores. This selection strategy ensures a more robust assessment, with the least frequent emoji in our top 50 (✌️) still appearing in 3,242 posts.

We extend this sentiment polarity analysis to pairs of emojis as well. We find the 50 most frequently used emoji pairs (two emojis that are different but co-exist in the same post). We avoid double-or-more counting: if two emojis are mentioned multiple times in the same post, regardless of order, this is counted as only one co-occurrence. As an example, (🚀 💎 💎 🚀) would be considered as only one co-occurrence of the pair (💎 🚀). We use the same formula used for the single emoji analysis to calculate bullish and bearish sentiment scores for each pair of emojis. Again, using only the 50 most used emoji pairs increases the robustness of our analysis. The least utilized emoji pair from the top 50 (💀 🔥) is used in 1,154 different posts.

In Fig. [10](https://amahrous.com/papers/finmoji/#S6.F10), we calculate the percentage of bullish and bearish labels given to posts, grouped by the number of unique emojis they contain. For instance, the first group shows the posts that contain one unique emoji or repetitions of it; for this group and each of the other groups, we calculate the percentage of posts that are labeled as bullish and those that are labeled as bearish to construct the two bars. We do this for ten groups, with the first group having only one unique emoji and the last group having ten or more unique emojis.

##### 3.2.4. Emoji Sentiment Analysis Algorithms

![Figure 4 . Methodology at a Glance. Pre-processing (yellow) generates three datasets containing only text, only emojis, and text with emojis. We then feed each dataset into both a logistic regression model (blue, cf. Sub](https://amahrous.com/papers/finmoji/figures/newOverview.svg) 

Figure 4. Methodology at a Glance. Pre-processing (yellow) generates three datasets containing only text, only emojis, and text with emojis. We then feed each dataset into both a logistic regression model (blue, cf. Subsection [7.1](https://amahrous.com/papers/finmoji/#S7.SS1)) and a transformer-based model (pink, cf. Subsection [7.2](https://amahrous.com/papers/finmoji/#S7.SS2)).

###### 3.2.4.1 Logistic Regression

Subsection [7.1](https://amahrous.com/papers/finmoji/#S7.SS1) uses the 528,000 labeled posts that include emojis. A regular expression tokenizer with a specific pattern (` \w+|[^\s] `) is used to tokenize the data. This custom tokenizer is designed to capture word characters and any non-whitespace character, including emojis, separating them into individual tokens. To transform the tokenized data into a TF-IDF (Term Frequency–Inverse Document Frequency) matrix ([Spärck Jones, 1972](https://amahrous.com/papers/finmoji/#bib.bib65)), we employ the TfidfVectorizer implementation available in Scikit-learn<sup>[6](https://amahrous.com/papers/finmoji/#footnote6)</sup>. This step transforms textual/emoji data into numerical form that can be processed by the logistic regression model. TF-IDF quantifies the importance of a token in a post relative to the entire collection of 528,000 posts. We use the following log-normalized formula to assign a number to each token.

<table> <tbody><tr> <td></td> <td>$\displaystyle\text{TF-IDF}(\text{token})$</td> <td>$\displaystyle=\left(\frac{\text{Number of times the token appears in a post}}{\text{Total number of tokens in a post}}\right)$</td> <td></td></tr></tbody> <tbody><tr> <td rowspan="1">(2)</td> <td></td> <td></td> <td>$\displaystyle\quad\times\log\left(1+\frac{\text{Total number of posts}}{\text{Number of posts containing the token}}\right)$</td> <td></td></tr></tbody> </table>

We employ a standard train-test split, with 80% of the data allocated for training and the remaining 20% for testing using Scikit-learn’s train\_test\_split function. We then train a logistic regression model on the training set for the purpose of binary classification, predicting whether a post expresses bullish or bearish sentiment. We keep the default decision threshold of 0.5. We evaluate the performance of our model by comparing predicted and actual labels on the test set, utilizing metrics such as accuracy, precision, recall, and F<sub>1</sub> score derived from Scikit-learn’s classification\_report and confusion\_matrix functions.

Table [5](https://amahrous.com/papers/finmoji/#S7.T5) additionally presents speed metrics for the logistic regression model, including both training and inference times. Training time refers to the duration required to train the model on a subset of 80,000 posts, while inference time measures the time taken to predict the sentiment of 20,000 posts.

In Fig. [12](https://amahrous.com/papers/finmoji/#S7.F12), we present the accuracy of a logistic regression model for binary classification, which is trained using varying sample sizes. This model adheres to the methodologies described in the preceding sections. We test the model on a consistent and fixed dataset comprising 52,800 posts. To assess how much data is required to achieve sufficient accuracy, we randomly selected training sets of size 100, 1,000, 10,000, 100,000, and 400,000 posts from the original dataset

The aforementioned experiments were conducted on three variants of the data: posts containing only text (excluding emojis), posts consisting solely of emojis (excluding text), and posts that included both text and emojis.

To assess uncertainty in accuracy and speed metrics, we use a non-parametric bootstrap method: we draw $n$ samples with replacement from the test set, compute each metric, repeat $1000$ times, and report the 2.5${}^{\text{th}}$ and 97.5${}^{\text{th}}$ percentiles as 95% confidence intervals.

###### 3.2.4.2 Transformers

For Subsection [7.2](https://amahrous.com/papers/finmoji/#S7.SS2), we use 528,000 labeled posts that include emojis, with 10% (52,800 posts) reserved for testing. The remaining 90% are split into training (81% of the original set) and validation sets (9% of the original set). We employ the cardiffnlp/twitter-roberta-base-sentiment-latest model ([Barbieri et al., 2020](https://amahrous.com/papers/finmoji/#bib.bib5)) and its associated tokenizer. This model, selected based on its superior performance on our dataset (cf. Table [10](https://amahrous.com/papers/finmoji/#S7.T10)), builds on the RoBERTa-base architecture ([Liu et al., 2019](https://amahrous.com/papers/finmoji/#bib.bib44)) and is further pre-trained on approximately 124 million tweets and adapted for sentiment analysis. Since the model is initially designed for three-label sentiment classification, we adapt it for binary classification using the RobertaForSequenceClassification class from the Hugging Face<sup>[7](https://amahrous.com/papers/finmoji/#footnote7)</sup> transformers library. BERT-based models are chosen for our analysis due to their demonstrated state-of-the-art performance in sentiment analysis, as supported by previous research in both general social media ([Khan et al., 2025](https://amahrous.com/papers/finmoji/#bib.bib42); [Bashiri and Naderi, 2024](https://amahrous.com/papers/finmoji/#bib.bib7)) and financial contexts ([Mahendran et al., 2025](https://amahrous.com/papers/finmoji/#bib.bib47); [Cicekyurt and Bakal, 2025](https://amahrous.com/papers/finmoji/#bib.bib18); [Du et al., 2024](https://amahrous.com/papers/finmoji/#bib.bib26)).

Prior to training, each post is truncated or padded to 120 tokens. Based on the percentile distribution in Table [3](https://amahrous.com/papers/finmoji/#S4.T3), 99% of StockTwits posts in our dataset are under 484 characters ($\approx$ 100 BERT tokens), indicating that a sequence limit of 120 tokens almost guarantees full coverage. As shown in Table [8](https://amahrous.com/papers/finmoji/#S7.T8), extending context length beyond 50 tokens provides little F<sub>1</sub> accuracy improvement while significantly increasing computational demands. We therefore adopted 120 tokens as a conservative upper bound to ensure robustness across text-only and emoji-only settings. This value is also consistent with the 128-token window commonly used in large-scale tweet transformer models such as BERTweet ([Dat Quoc et al., 2020](https://amahrous.com/papers/finmoji/#bib.bib21)).

The model is then fine-tuned on our sample data for three epochs using the Hugging Face Trainer API, with a batch size of 32. The learning rate is dynamically adjusted using a cosine scheduler with restarts, and a warm-up phase of 50 steps is included to gradually increase the learning rate at the beginning of training. We utilize mixed-precision training (FP16) and gradient accumulation to enhance computational efficiency. We evaluate the performance of our model against the validation dataset at 10 predefined checkpoints, with the best-performing model weights saved for final assessment on the test dataset using accuracy, precision, recall, and F<sub>1</sub> score.

For the speed metrics in Table [7](https://amahrous.com/papers/finmoji/#S7.T7), we randomly selected 80,000 posts to measure training speed and 20,000 for inference speed. The same model configuration and tokenizer are used, with all posts truncated or padded to 120 tokens. We report training speed for a single epoch.

In Fig. [14](https://amahrous.com/papers/finmoji/#S7.F14), the identical model setup is applied, but we train on random subsets of the original training dataset: 100, 1,000, 10,000, 100,000, and 400,000 posts. Each subset is trained over three epochs, with accuracy measured on the original test dataset of 52,800 posts, and results are plotted in Fig. [14](https://amahrous.com/papers/finmoji/#S7.F14).

All experiments were conducted on three data variants: posts containing only text (excluding emojis), posts consisting solely of emojis (excluding text), and posts including both text and emojis.

We use the same non-parametric bootstrap method as before to assess uncertainty, that is, we draw $n$ samples with replacement from the test set, compute each metric, repeat $1000$ times, and report the 2.5${}^{\text{th}}$ and 97.5${}^{\text{th}}$ percentiles as 95% confidence intervals.

###### 3.2.4.3 Other Tested Models

In Subsection [7.3](https://amahrous.com/papers/finmoji/#S7.SS3), we explore the performance of various machine learning algorithms on sentiment analysis using only emoji data. This analysis uses the same data variant that includes only emojis, as discussed in previous sections. The methodology mirrors that of the logistic regression model described in Subsection [7.1](https://amahrous.com/papers/finmoji/#S7.SS1), employing the same RegexpTokenizer (` \w+|[^\s] `) and TF-IDF vectorizer. We utilize the dataset of 528,000 posts containing only emojis, with 80% allocated for training and 20% for evaluation.

We examine four different machine learning algorithms: Multinomial Naïve Bayes (MNB), Random Forest Classifier (RF), LightGBM Classifier (LGBM) ([Brownlee, 2021](https://amahrous.com/papers/finmoji/#bib.bib12)), and Linear Support Vector-Machine Classifier (LinearSVC). Each model is trained and evaluated using the same datasets as those used for the logistic regression model in Subsection [7.1](https://amahrous.com/papers/finmoji/#S7.SS1). Speed metrics are calculated similarly to those for the logistic regression models in Subsection [7.1](https://amahrous.com/papers/finmoji/#S7.SS1) and the transformer models in Subsection [7.2](https://amahrous.com/papers/finmoji/#S7.SS2), facilitating direct comparison. All experiments were conducted on the same hardware. The configurations for these models are set to their default parameters as specified in the scikit-learn module, except for the n\_jobs=-1 setting for the RF model to use all CPU cores during training.

##### 3.2.5. Huggingface Model Comparisons

In Subsection [7.4](https://amahrous.com/papers/finmoji/#S7.SS4), we employ the same methodology outlined in Subsection [7.2](https://amahrous.com/papers/finmoji/#S7.SS2), using the same pipeline and the Hugging Face Trainer API but with a variety of different models available on the Hugging Face platform. For each model (\*), we use the corresponding \*Tokenizer and \*ForSequenceClassification classes from the Hugging Face transformers library. A key distinction, however, is that for all models, except the one used in Subsection [7.2](https://amahrous.com/papers/finmoji/#S7.SS2), the attached tokenizer excludes emojis by default. Consequently, we preprocess by “demojizing” emojis, which involves converting emoji symbols into their respective textual descriptions or aliases. This preprocessing step is executed using the demojize function from the Python emoji library<sup>[8](https://amahrous.com/papers/finmoji/#footnote8)</sup>. All models are then fine-tuned using the same datasets consisting of text only, emojis only, and both text and emojis.

### 4. Emoji Usage: Descriptive Analysis

In this section, we conduct a descriptive analysis of emoji usage in StockTwits posts. Approximately 15% of the 18.5 million posts in our dataset include at least one emoji. The distribution of emojis per post shows a negative trend: the frequency of posts containing a given number of emojis decreases as the emoji count increases. This pattern is evident in Fig. [5](https://amahrous.com/papers/finmoji/#S4.F5) (left) and applies whether considering the total number of emojis or the count of distinct emojis per post. Notably, a significant portion of posts contain more than 10 emojis, suggesting potential advertisement or spam activity. [Shiri et al. (2023)](https://amahrous.com/papers/finmoji/#bib.bib61) find that patterns of emoji usage help in detecting spam in financial tweets. Fig. [5](https://amahrous.com/papers/finmoji/#S4.F5) (right) shows an explosive increase in the usage of emojis over time. From 2009 to 2016, the average number of emojis per post remained near zero. Subsequently, there was an exponential increase, with the average exceeding 1.0 by mid-2022. The rise in the usage of emojis is a well-documented phenomenon ([Broni, 2023](https://amahrous.com/papers/finmoji/#bib.bib11)), possibly caused by socio-cultural and technological shifts. The short-term variability in emoji usage over time presents an interesting area for further investigation.

![(a)](https://amahrous.com/papers/finmoji/figures/numEmojisDist.webp) 

(a)

![(b)](https://amahrous.com/papers/finmoji/figures/avgEmojiPerPost.webp) 

(b)

Figure 5. Emoji Usage in our Dataset. (a) Bar charts illustrating the percentage of posts containing various numbers of emojis, comparing total emoji counts (yellow) and unique emojis (red). (b) A time series detailing the average number of emojis used per post over time.

Fig. [6](https://amahrous.com/papers/finmoji/#S4.F6) highlights differences in emoji usage between bullish and bearish posts. For instance, the 🚀 emoji appears significantly more frequently (larger) in the bullish emoji cloud, whereas the 💩 emoji is more prominent in the bearish cloud. Additionally, the laughing emojis 😂 and 🤣 are prevalent in both clouds but are more pronounced in bearish posts. This could suggest that sarcasm, as indicated by the use of these emojis, is more common in bearish sentiments.

The gray cloud represents posts that have not been labeled by the poster, possibly indicating uncertainty. Emojis commonly associated with uncertainty, such as 🤷 and 🤔, are more prominent in the unlabeled emoji cloud compared to the bullish or bearish clouds. However, the presence of unlabeled posts does not necessarily imply uncertainty about sentiment. The frequent use of sentiment-specific emojis like 🚀 in the gray cloud indicates that some users may be confident in their sentiment but opt not to label their posts explicitly.

![(a)](https://amahrous.com/papers/finmoji/figures/bullishCloud.webp) 

(a)

![(b)](https://amahrous.com/papers/finmoji/figures/bearishCloud.webp) 

(b)

![(c)](https://amahrous.com/papers/finmoji/figures/emojiCloudGrey.webp) 

(c)

Figure 6. Emoji Clouds for Financial Microblogs. (a) Bullish (green/left), (b) Bearish (red/middle), and (c) Unlabeled (gray/right) emoji clouds, with emoji size reflecting frequency of use.

As shown in Table [3](https://amahrous.com/papers/finmoji/#S4.T3), the number of words in text-only data is significantly higher than the number of emojis in emoji-only data. Therefore, the information contained in emojis of a post can be analyzed by a model with significantly fewer tokens. This allows the analysis and inference to be faster and more efficient. The sentiment of a post containing many textual tokens might be summarized in just one emoji token. In sentiment analysis, emojis offer a lower lexical diversity and a smaller feature space compared to text due to their limited set of symbols. There are many fewer unique emojis than there are unique words. In our text-only data, there are around 227,000 unique words. In contrast, the emoji-only data contains fewer than 3,000 unique emojis. This smaller dimensionality simplifies machine learning models, resulting in less computational and data demands.

Table 3. Percentile Distribution of Text and Emoji Lengths in Posts. This table displays the character length distribution for text-only and emoji-only content across various percentiles, demonstrating the comparative brevity of emoji usage.

<table> <tr> <th scope="col">Percentile</th> <th scope="col">5<sup>th</sup></th> <th scope="col">25<sup>th</sup></th> <th scope="col">50<sup>th</sup></th> <th scope="col">75<sup>th</sup></th> <th scope="col">90<sup>th</sup></th> <th scope="col">95<sup>th</sup></th> <th scope="col">99<sup>th</sup></th></tr> <tr> <td>Text Length</td> <td>1</td> <td>20</td> <td>45</td> <td>90</td> <td>165</td> <td>248</td> <td>484</td></tr> <tr> <td>Emoji Length</td> <td>1</td> <td>1</td> <td>2</td> <td>4</td> <td>7</td> <td>11</td> <td>24</td></tr> </table>

### 5. Emoji Usage: StockTwits versus $\mathbb{X}$ (Twitter)

In this section, we compare emoji usage on two platforms: StockTwits and $\mathbb{X}$ (Twitter).

Fig. [7](https://amahrous.com/papers/finmoji/#S5.F7) shows emoji clouds of Twitter (blue/left, now $\mathbb{X}$) and of StockTwits (purple/right). Looking at the clouds, noticeable differences in emoji usage between the two platforms are immediately apparent. For instance, Twitter’s cloud contains more heart-related emojis (such as ❤️ or 😍), while StockTwits’ contains more money-related emojis (such as 💰 or 🤑). Different emojis are also much more prevalent on one platform than the other. For example, 🚀 and 💎 are much bigger in the StockTwits’ cloud compared to Twitter’s. However, some emojis seem to be used equally frequently on both platforms, particularly 😂 and 🔥.

![(a)](https://amahrous.com/papers/finmoji/figures/twitter_cloud.webp) 

(a)

![(b)](https://amahrous.com/papers/finmoji/figures/stocktwits_cloud.webp) 

(b)

Figure 7. Emoji Clouds for Twitter ($\mathbb{X}$) and StockTwits. (a) Twitter ($\mathbb{X}$) (blue/left) and (b) StockTwits (purple/right) emoji clouds visualize the frequency of emoji use on each platform. The size of each emoji indicates its relative frequency, showcasing distinct preferences for emojis on both platforms.

From Table [4](https://amahrous.com/papers/finmoji/#S5.T4), it is evident that the distribution of the 20 most used emojis on StockTwits likely differs from that on Twitter, particularly due to the prevalence of financially themed emojis, such as 🤑. Supporting this, both the Mann-Whitney U and the Kolmogorov-Smirnov tests indicate a highly significant difference in distributions ($p$-value \< 0.01). Supporting this, a chi-square test confirms a highly significant difference between platforms ($p<0.01$), with a large effect size (Cramér’s $V=0.599$). This finding underscores the need for context-specific sentiment analysis models tailored to financial social media, aligning with extensive research in the field that advocates for such approaches ([Du et al., 2024](https://amahrous.com/papers/finmoji/#bib.bib26); [Renault, 2020](https://amahrous.com/papers/finmoji/#bib.bib55); [Nasekin and Chen, 2020](https://amahrous.com/papers/finmoji/#bib.bib53); [Wilksch and Abramova, 2023](https://amahrous.com/papers/finmoji/#bib.bib69); [Kulakowski and Frasincar, 2023](https://amahrous.com/papers/finmoji/#bib.bib43)).

Table 4. Comparative Analysis of Emoji Usage on StockTwits and Twitter ($\mathbb{X}$). This table ranks the top 20 emojis used on both platforms, highlighting differences in frequency and specific emoji preferences.

<table> <tr> <th scope="col"></th> <th scope="col"></th> <th scope="col">🚀</th> <th scope="col">😂</th> <th scope="col">🤣</th> <th scope="col">🔥</th> <th scope="col">💎</th> <th scope="col">🤑</th> <th scope="col">💰</th> <th scope="col">👀</th> <th scope="col">🤔</th> <th scope="col">😎</th> <th scope="col">📈</th> <th scope="col">👍</th> <th scope="col">🐻</th> <th scope="col">🤡</th> <th scope="col">🦍</th> <th scope="col">💪</th> <th scope="col">🙌</th> <th scope="col">😁</th> <th scope="col">😆</th> <th scope="col">💥</th></tr> <tr> <td rowspan="2">Rank</td> <td>StockTwits</td> <td>1</td> <td>2</td> <td>3</td> <td>4</td> <td>5</td> <td>6</td> <td>7</td> <td>8</td> <td>9</td> <td>10</td> <td>11</td> <td>12</td> <td>13</td> <td>14</td> <td>15</td> <td>16</td> <td>17</td> <td>18</td> <td>19</td> <td>20</td></tr> <tr> <td>Twitter</td> <td>97</td> <td>1</td> <td>13</td> <td>5</td> <td>71</td> <td>215</td> <td>80</td> <td>17</td> <td>15</td> <td>24</td> <td>281</td> <td>31</td> <td>233</td> <td>358</td> <td>664.5</td> <td>47</td> <td>34</td> <td>26</td> <td>74</td> <td>35</td></tr> <tr> <td rowspan="2">Rel. Freq.</td> <td>StockTwits</td> <td>15.78%</td> <td>12.3%</td> <td>6.82%</td> <td>4.95%</td> <td>4.80%</td> <td>3.37%</td> <td>3.28%</td> <td>2.87%</td> <td>2.67%</td> <td>2.59%</td> <td>2.32%</td> <td>2.27%</td> <td>2.19%</td> <td>1.76%</td> <td>1.64%</td> <td>1.63%</td> <td>1.52%</td> <td>1.47%</td> <td>1.43%</td> <td>1.34%</td></tr> <tr> <td>Twitter</td> <td>0.31%</td> <td>13.27%</td> <td>1.41%</td> <td>4.14%</td> <td>0.44%</td> <td>0.12%</td> <td>0.37%</td> <td>1.29%</td> <td>1.30%</td> <td>0.90%</td> <td>0.09%</td> <td>0.83%</td> <td>0.11%</td> <td>0.06%</td> <td>0.02%</td> <td>0.59%</td> <td>0.75%</td> <td>0.86%</td> <td>0.39%</td> <td>0.73%</td></tr> </table>

### 6. Emoji Sentiment Scores

In this section, we score emojis based on their presence in bullish versus bearish posts. For every emoji, we calculate the percentage of posts that are bullish versus bearish when that particular emoji is present.

The bars in Fig. [8](https://amahrous.com/papers/finmoji/#S6.F8) represent the percentage of posts that are bullish/bearish, given that an emoji is present. As shown in Fig. [8](https://amahrous.com/papers/finmoji/#S6.F8), some emojis can serve as strong predictors of the sentiment for a post. For instance, in our sample, 96% of posts that contain 🚀 are bullish, and 97% of posts that contain 🩸 are bearish. Such findings highlight the predictive value some emojis have in financial sentiment analysis, enabling highly efficient sentiment classification.

![Figure 8 . Sentiment Score of Individual Emojis. This bar chart displays the proportion of bullish (green) and bearish (red) posts associated with the 50 most used emojis, highlighting specific emojis as strong predictor](https://amahrous.com/papers/finmoji/figures/emojiScoreInd.webp) 

Figure 8. Sentiment Score of Individual Emojis. This bar chart displays the proportion of bullish (green) and bearish (red) posts associated with the 50 most used emojis, highlighting specific emojis as strong predictors of market sentiment.

Fig. [9](https://amahrous.com/papers/finmoji/#S6.F9) reveals that most emojis retain their sentiment scores whether analyzed individually or as part of a pair. However, there are notable exceptions. The ❤️ emoji is typically indicative of positive sentiment when analyzed alone, but also appears in two of the most bearish pairs. A similar observation applies to the 🔥 and 💰 emojis to some extent, given the bearish combinations of 💩 with 🔥 and 🐻 with 💰. In the first case, the ❤️ may just be used in the meaning of “to like”, potentially disclosing a short position of the original poster. In the second case, 💩 and 🐻 act as negations, figurative speech, or qualitative modifiers, e.g., “🐻 on 🔥”. It is worth pointing out in this context that such modifiers (especially negations) in natural language historically posed challenges for NLP. The reason is that they necessitated either longer attention (in the case of transformers) or longer N-grams (in the case of Bag-of-Words approaches).

The finding that an individual or pair of emojis is highly bullish or bearish can be used to create efficient sentiment analysis algorithms. We can have a level of confidence that if an emoji or pair of emojis exists in a post, then it is either bullish/bearish. The sharp transition between bullish and bearish pairs also signals a low amount of ambiguity regarding the sentiment of emoji pairs.

![Figure 9 . Sentiment Score of Emoji Pairs. This bar chart displays the proportion of bullish (green) and bearish (red) posts associated with the 50 most used emoji pairs.](https://amahrous.com/papers/finmoji/figures/emojiScoresPairs.webp) 

Figure 9. Sentiment Score of Emoji Pairs. This bar chart displays the proportion of bullish (green) and bearish (red) posts associated with the 50 most used emoji pairs.

Additionally, some emojis, such as the 🤔, are frequently used alone and so do not appear in the most common pairs. Moreover, the prevalence of laughing emojis like 😂 and 🤣 in bearish pairs indicates they may be used to convey sarcasm, mock optimism, or express self-deprecating humor. We also notice that the score for pairs is skewed towards bearish. This raises the question of whether the number of emojis in a post can also be predictive of its sentiment.

Fig. [10](https://amahrous.com/papers/finmoji/#S6.F10) displays the distribution of bullish and bearish sentiment across posts categorized by the number of emojis used. Posts containing two to five emojis exhibit a higher likelihood of expressing bullish sentiment, with a peak observed at three emojis. However, as the number of emojis surpasses five, a clear shift towards bearish sentiment emerges, culminating in posts with ten or more emojis demonstrating the highest proportion of bearish sentiment (this could be considered a “pictogram rant”). The frequency of posts decreases with increasing emoji counts, resembling an exponential decay pattern.

All these insights gained from analyzing the use and distribution of emojis in these posts lead us to hypothesize that emojis may carry a meaning strong enough to classify sentiment using relatively shallow or simple models. Consequently, we opted to also include logistic regression in our experiments, aiming for high inference speed that is beneficial for sentiment analysis in high-frequency trading, where even microseconds matter ([Aquilina et al., 2022](https://amahrous.com/papers/finmoji/#bib.bib2)).

![Figure 10 . Emoji Count versus Sentiment and Frequency. This chart displays the percentage of bullish (green) and bearish (red) posts based on the number of unique emojis used, along with the frequency (blue line) of pos](https://amahrous.com/papers/finmoji/figures/numEmojis.webp) 

Figure 10. Emoji Count versus Sentiment and Frequency. This chart displays the percentage of bullish (green) and bearish (red) posts based on the number of unique emojis used, along with the frequency (blue line) of posts for each emoji count.

### 7. Emoji Sentiment Analysis Algorithms

In this section, we perform sentiment analysis using only emojis.

#### 7.1. Logistic Regression

Table [5](https://amahrous.com/papers/finmoji/#S7.T5) presents the accuracy and speed metrics for logistic regression, comparing using text only, emoji only, and text plus emojis. As expected, text plus emojis performs the best, with an F<sub>1</sub> score of 0.82. It is worth noting, though, that including text (as opposed to only emojis) in the sentiment analysis is only able to boost the F<sub>1</sub> score by 7 percentage points (up from 0.75). In addition, using only text fares marginally better (0.76) than using only emojis. This supports our hypothesis that emojis in financial social media carry strong meaning in an extremely compact form. Furthermore, this accuracy is surprisingly good, given the simplicity and speed of the logistic regression model.

The higher precision metric of the emojis-only model (compared to the text-only) means that it is more likely to be accurate when labeling a post as bullish, but the lower recall metric means that it is more likely to miss posts that are bullish. The trade-off between precision and recall can be controlled by changing the decision threshold. However, for the sake of easier reproducibility, we kept the default decision threshold of 0.5 for all models.

As expected, using only emojis has an advantage in terms of computational efficiency. Another major benefit of using emojis in financial social media is that they are arguably more generalizable across cultures compared to text and, thus, could be valuable for cross-language generalization (left for future work).

Table 5. Performance of Logistic Regression Models. This table compares the accuracy and speed of logistic regression models trained on text only, emojis only, and text with emojis. Time is measured in seconds. We report average and 95% confidence intervals in square brackets. Both training and inference processes were executed on a 13<sup>th</sup> Gen Intel Core i9-13900H laptop CPU with 32GB of RAM.

<table> <tr> <th scope="col"></th> <th scope="col">Text only</th> <th scope="col">Emojis only</th> <th scope="col">Text + Emojis</th></tr> <tr> <td>Accuracy Metrics</td> <td></td> <td></td> <td></td></tr> <tr> <td>Recall</td> <td>0.762 [0.758, 0.766]</td> <td>0.754 [0.750, 0.757]</td> <td>0.824 [0.821, 0.827]</td></tr> <tr> <td>Precision</td> <td>0.762 [0.758, 0.765]</td> <td>0.755 [0.752, 0.759]</td> <td>0.824 [0.820, 0.827]</td></tr> <tr> <td>F<sub>1</sub> Score</td> <td>0.761 [0.757, 0.765]</td> <td>0.754 [0.750, 0.758]</td> <td>0.824 [0.821, 0.827]</td></tr> <tr> <td>Speed Metrics</td> <td></td> <td></td> <td></td></tr> <tr> <td>Training time (s)</td> <td>4.106 [3.870, 4.310]</td> <td>3.400 [3.218, 3.586]</td> <td>4.654 [4.486, 4.961]</td></tr> <tr> <td>Inference time (s)</td> <td>0.003 [0.002, 0.003]</td> <td>0.001 [0.001, 0.002]</td> <td>0.003 [0.002, 0.003]</td></tr> </table>

![(a) Emoji Only](https://amahrous.com/papers/finmoji/figures/emojiLR_CM.svg) 

(a) Emoji Only

![(b) Text Only](https://amahrous.com/papers/finmoji/figures/textOnlyLR_CM.svg) 

(b) Text Only

![(c) Text and Emoji](https://amahrous.com/papers/finmoji/figures/TextAndEmojiLR_CM.svg) 

(c) Text and Emoji

Figure 11. Confusion Matrices of Logistic Regression Models. This figure displays confusion matrices for logistic regression models trained on emojis only (a), text only (b), and text with emojis (c). The matrices compare the models’ predicted sentiment labels (bullish or bearish) with the true labels.

Fig. [12](https://amahrous.com/papers/finmoji/#S7.F12) depicts the model accuracy as a function of training data size. With its logarithmic X-axis scale, the figure clearly demonstrates “diminishing returns”—the increase in accuracy decreases as the training data size increases significantly, approaching a horizontal asymptote of the theoretical maximum accuracy possible with the given models.

When the model is trained on text only, the accuracy starts at 50.1% for 100 posts and increases as more data is used, reaching approximately 75.2% accuracy with 400,000 posts. The model trained on only emojis starts with 63.4% accuracy for 100 posts and also demonstrates a steeper curve than text only, achieving about 75.7% accuracy with 400,000 posts. The model trained with both text and emojis starts with a higher accuracy of 58.3% at 100 posts and shows a steeper increase in accuracy as the sample size grows, reaching about 82.4% with 400,000 posts.

One of the advantages of using emojis only, as shown in Fig. [12](https://amahrous.com/papers/finmoji/#S7.F12), is the ability to train on a lower amount of data. In this figure, we see that the logistic regression model, when trained on only 1,000 posts, achieves an accuracy of around 72% on a test sample of 50,000 posts, indicating a potential advantage in contexts where training data is limited. In contrast, a text-only model requires over 10,000 posts to surpass 70% accuracy. This discrepancy highlights the efficiency of using emojis for sentiment analysis, as they allow for achieving high accuracy with fewer training samples.

![Figure 12 . Impact of Training Sample Size on Logistic Regression Model Accuracy. This figure illustrates the relationship between training sample size and model accuracy for logistic regression models trained on text on](https://amahrous.com/papers/finmoji/figures/sampleSizeLR.webp) 

Figure 12. Impact of Training Sample Size on Logistic Regression Model Accuracy. This figure illustrates the relationship between training sample size and model accuracy for logistic regression models trained on text only (blue line), emojis only (green line), and text with emojis (orange line). Accuracy is evaluated on the same separate test set of 50,000 posts.

Table 6. Entropy and Vocabulary Statistics (Top 90% Frequency Mass)

<table> <tr> <th scope="col">Metric</th> <th scope="col">Value</th></tr> <tr> <td>Word entropy</td> <td>9.52 bits</td></tr> <tr> <td>Emoji entropy</td> <td>6.72 bits</td></tr> <tr> <td>Average word length</td> <td>5.48 characters</td></tr> <tr> <td>Unique words</td> <td>5,042</td></tr> <tr> <td>Unique emojis</td> <td>267</td></tr> </table>

Because emojis’ efficiency advantages relate to how compactly information is encoded, entropy measurements provide a natural way to compare text and emojis. As shown in Table [6](https://amahrous.com/papers/finmoji/#S7.T6), the top-90% word distribution yields an entropy of 9.52 bits. This value is lower than Shannon’s classical estimate of 11.82 bits per word for printed English ([Shannon, 1951](https://amahrous.com/papers/finmoji/#bib.bib60)). A lower entropy reflects a more homogeneous language in the shorter-form financial social media compared to printed English. The average word length in our dataset is 5.48 characters, slightly higher than Shannon’s reference value of 4.5 letters but in line with other studies on social media text ([Smirnov, 2017](https://amahrous.com/papers/finmoji/#bib.bib63)).

In contrast, emoji usage is more concentrated, with the top-90% mass consisting of 267 emojis and producing an entropy of 6.72 bits. The corresponding top-90% vocabulary for words is much larger (5,042 words), reflecting the broader range of textual content relative to emojis.

#### 7.2. Transformer

Table [7](https://amahrous.com/papers/finmoji/#S7.T7) presents the performance of a transformer ([Ashish et al., 2017](https://amahrous.com/papers/finmoji/#bib.bib4)) model on text only, emojis only, and both text and emojis datasets. Similar to the logistic regression model shown in Table [5](https://amahrous.com/papers/finmoji/#S7.T5), the transformer model demonstrates the highest accuracy when analyzing data that includes both text and emojis. However, unlike the logistic regression model, the transformer shows better performance with text-only data than with emoji-only data. This indicates that the transformer model was able to capture more information about the meaning of text, which is presumably more complex than capturing information about the meaning of emojis. This is likely because short emoji sequences do not fully exploit the transformer’s attention mechanism.

The relative simplicity of emoji analysis is further highlighted by the comparable performance of the simpler logistic regression model and the more complex transformer model on emoji-only data. For emojis-only, using transformers may be excessive, as simpler models can achieve similar levels of accuracy with greater efficiency.

Table 7. Performance of the Twitter-RoBERTa Model. This table compares the accuracy and speed of the model when trained on text only, emojis only, and text with emojis. Time is measured in seconds. We report average and 95% confidence intervals in square brackets. Both training and inference processes were executed on a 13<sup>th</sup> Gen Intel Core i9-13900H laptop CPU with 32GB of RAM.

<table> <tr> <th scope="col"></th> <th scope="col">Text only</th> <th scope="col">Emojis only</th> <th scope="col">Text + Emojis</th></tr> <tr> <td>Accuracy Metrics</td> <td></td> <td></td> <td></td></tr> <tr> <td>Recall</td> <td>0.841 [0.838, 0.844]</td> <td>0.763 [0.759, 0.766]</td> <td>0.884 [0.880, 0.886]</td></tr> <tr> <td>Precision</td> <td>0.841 [0.838, 0.844]</td> <td>0.765 [0.761, 0.768]</td> <td>0.884 [0.881, 0.887]</td></tr> <tr> <td>F<sub>1</sub> Score</td> <td>0.841 [0.838, 0.844]</td> <td>0.762 [0.758, 0.766]</td> <td>0.883 [0.880, 0.886]</td></tr> <tr> <td>Speed Metrics</td> <td></td> <td></td> <td></td></tr> <tr> <td>Training time (s)</td> <td>93 [92, 97]</td> <td>95 [94, 95]</td> <td>95 [95, 97]</td></tr> <tr> <td>Inference time (s)</td> <td>19 [18, 28]</td> <td>22 [21, 24]</td> <td>22 [21, 26]</td></tr> </table>

![(a) Emoji Only](https://amahrous.com/papers/finmoji/figures/emojiTR_CM.svg) 

(a) Emoji Only

![(b) Text Only](https://amahrous.com/papers/finmoji/figures/textOnlyTR_CM.svg) 

(b) Text Only

![(c) Text and Emoji](https://amahrous.com/papers/finmoji/figures/TextAndEmojiTR_CM.svg) 

(c) Text and Emoji

Figure 13. Confusion Matrices of Transformer-based Twitter-roBERTa Models. This figure displays confusion matrices for Twitter-roBERTa models trained on emojis only (a), text only (b), and text with emojis (c). The matrices compare the models’ predicted sentiment labels (bullish or bearish) with the true labels.

Similar to the results shown for the regression model in Fig. [12](https://amahrous.com/papers/finmoji/#S7.F12), the transformer model demonstrates higher accuracy on emoji-only data, even when trained with a relatively small dataset (1,000 posts) and tested on 50,000 posts. However, in contrast to the regression model, the transformer’s complexity allows it to derive greater benefits from a larger text dataset. This advantage is reflected in the increasing accuracy observed in the text-only model (blue line).

One of the hyperparameters that can have a significant impact on training/inference speed is the context length (that is, the maximum number of tokens used to predict the next token). Naturally, having longer contexts requires more computational resources and memory. As shown in Table [8](https://amahrous.com/papers/finmoji/#S7.T8), we see that, quite intuitively, emoji-only data requires smaller context lengths to achieve its highest accuracy. For instance, emoji-only data reaches its highest accuracy in a context of 10 or 20 tokens, while text-only data requires 50 tokens. This is expected as, in general, posts contain significantly fewer emojis than text (cf. Table [3](https://amahrous.com/papers/finmoji/#S4.T3)). However, the speed decreased less than expected. For 3 to 20 tokens, the speed is mostly constant, decreasing slightly for 50 tokens and almost halving for 120 tokens. The self-attention mechanism at the core of transformer models exhibits quadratic time and space complexity relative to input length ([Keles et al., 2023](https://amahrous.com/papers/finmoji/#bib.bib41)). Therefore, increasing the maximum token length from 3 to 120 should increase the time complexity by a factor of 1,600. However, the increase in practice can be significantly different. The reason is that modern computing architectures tend to be severely limited by memory bandwidth. Various levels of caches are used to improve memory bandwidth at a reasonable cost to hardware vendors, but cache sizes remain generally limited. As a result of a transformer requiring additional memory depending linearly on the context length (“KV cache”), smaller context lengths benefit disproportionately from such hardware caches. As shown in Table [8](https://amahrous.com/papers/finmoji/#S7.T8), increasing the context length from 3 to 120 increases the time needed to train and infer by only approximately $2{\times}$.

![Figure 14 . Impact of Training Sample Size on Transformer-based Twitter-RoBERTa Model Accuracy. This figure illustrates the relationship between training sample size and model accuracy for Twitter-RoBERTa models trained](https://amahrous.com/papers/finmoji/figures/sampleSizeTR.webp) 

Figure 14. Impact of Training Sample Size on Transformer-based Twitter-RoBERTa Model Accuracy. This figure illustrates the relationship between training sample size and model accuracy for Twitter-RoBERTa models trained on text only (blue line), emojis only (green line), and text with emojis (orange line). Accuracy is evaluated on the same separate test set of 50,000 posts.

Table 8. Effect of Context Length on Model Performance and Speed. This table demonstrates the impact of varying sequence max-length on the F<sub>1</sub> score, training speed, and inference speed of Twitter-RoBERTa models trained on text-only and emoji-only data. Time is measured in seconds. Both training and inference processes were executed on a 13<sup>th</sup> Gen Intel Core i9-13900H laptop CPU with 32GB of RAM.

<table> <tr> <th scope="col">Sequence Max-Length</th> <th scope="col">3</th> <th scope="col">10</th> <th scope="col">20</th> <th scope="col">50</th> <th scope="col">120</th></tr> <tr> <td>F1 Score</td> <td></td> <td></td> <td></td> <td></td> <td></td></tr> <tr> <td>Text-Only</td> <td>0.64</td> <td>0.76</td> <td>0.81</td> <td>0.83</td> <td>0.82</td></tr> <tr> <td>Emoji-Only</td> <td>0.64</td> <td>0.74</td> <td>0.76</td> <td>0.75</td> <td>0.76</td></tr> <tr> <td>Training Speed</td> <td></td> <td></td> <td></td> <td></td> <td></td></tr> <tr> <td>Text-Only</td> <td>272</td> <td>266</td> <td>275</td> <td>291</td> <td>510</td></tr> <tr> <td>Emoji-Only</td> <td>264</td> <td>266</td> <td>271</td> <td>286</td> <td>469</td></tr> <tr> <td>Inference Speed</td> <td></td> <td></td> <td></td> <td></td> <td></td></tr> <tr> <td>Text-Only</td> <td>18</td> <td>18</td> <td>19</td> <td>20</td> <td>37</td></tr> <tr> <td>Emoji-Only</td> <td>18</td> <td>18</td> <td>17</td> <td>19</td> <td>34</td></tr> </table>

#### 7.3. Other Tested Models

In this section, we explore the performance of various machine learning models on the emoji dataset as potential baseline models against the more complex transformer model. These models were selected for their relative simplicity and computational efficiency, which could offer practical advantages in financial sentiment analysis. Here, simplicity refers to the model architecture and number of trainable parameters compared to the heavier deep-learning transformer models tested, while computational efficiency is evaluated empirically using training time and inference time as reported in Table [9](https://amahrous.com/papers/finmoji/#S7.T9).

Table [9](https://amahrous.com/papers/finmoji/#S7.T9) indicates that all models achieve an accuracy (F<sub>1</sub> scores) competitive with the transformer model when using emoji-only data, while offering much faster speeds and greater computational efficiency. Among the baseline models—we used Multinomial Naïve Bayes (MNB), Random Forest (RF), Light Gradient Boosting Machine (LGBM), Linear Support Vector Classification (SVC), and Logistic Regression (Reg),—we generally observe uniform accuracy (F<sub>1</sub> Score), indicating robust effectiveness across different modeling techniques.

However, there are some significant differences in training and inference times among the tested models. RF requires significantly more time to train than the other models, making it the least efficient in terms of speed. LGBM also shows longer training times, but it is faster than RF. MNB, SVC, and Reg are all relatively fast, with MNB being the fastest, approximately ten times faster than training Reg.

Table 9. Performance Comparison of Baseline Machine Learning Models on Emoji Data. This table evaluates the accuracy and speed of various baseline models, including Multinomial Naïve Bayes (MNB), Random Forest (RF), LightGBM (LGBM), and LinearSVC (SVC), in comparison to the Logistic Regression (Reg) and Transformer (Tr) models, all using emoji-only data. Time is measured in seconds. Both training and inference processes were executed on a 13<sup>th</sup> Gen Intel Core i9-13900H laptop CPU with 32GB of RAM.

<table> <tr> <th scope="col"></th> <th scope="col">MNB</th> <th scope="col">RF</th> <th scope="col">LGBM</th> <th scope="col">SVC</th> <th scope="col">Reg</th> <th scope="col">Tr</th></tr> <tr> <td>Accuracy</td> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td></tr> <tr> <td>Recall</td> <td>0.72</td> <td>0.72</td> <td>0.68</td> <td>0.72</td> <td>0.72</td> <td>0.73</td></tr> <tr> <td>Precision</td> <td>0.77</td> <td>0.79</td> <td>0.80</td> <td>0.77</td> <td>0.78</td> <td>0.79</td></tr> <tr> <td>F1 Score</td> <td>0.74</td> <td>0.76</td> <td>0.74</td> <td>0.75</td> <td>0.75</td> <td>0.76</td></tr> <tr> <td>Speed</td> <td></td> <td></td> <td></td> <td></td> <td></td> <td></td></tr> <tr> <td>Training time</td> <td>0.03</td> <td>31.91</td> <td>2.76</td> <td>0.57</td> <td>0.29</td> <td>498</td></tr> <tr> <td>Inference time</td> <td>0.003</td> <td>0.58</td> <td>0.04</td> <td>0.002</td> <td>0.001</td> <td>38</td></tr> </table>

#### 7.4. Huggingface Model Comparisons

In this section, we evaluate various transformer models from Huggingface, focusing on their application in financial social media sentiment analysis. This analysis was performed in order to choose the best transformer model to test in Subsection [7.2](https://amahrous.com/papers/finmoji/#S7.SS2).

Each model reviewed in Table [10](https://amahrous.com/papers/finmoji/#S7.T10) is based on the BERT ([Devlin et al., 2018](https://amahrous.com/papers/finmoji/#bib.bib24)) architecture, a well-known implementation of the transformer framework.

Twitter-RoBERTa ([Loureiro et al., 2022](https://amahrous.com/papers/finmoji/#bib.bib46)) is a model designed for sentiment analysis of general Twitter posts. It is pre-trained on approximately 124 million tweets and fine-tuned on the TweetEval dataset (which includes more than 100,000 manually annotated tweets ([Rosenthal et al., 2019](https://amahrous.com/papers/finmoji/#bib.bib58))).

FinBERT ([Araci, 2019](https://amahrous.com/papers/finmoji/#bib.bib3)) is a model designed for sentiment analysis of financial news articles. It pre-trains the BERT model on 1.8 million financial news articles published by Reuters (TRC2<sup>[9](https://amahrous.com/papers/finmoji/#footnote9)</sup>). It is then fine-tuned on the Financial PhraseBank dataset<sup>[10](https://amahrous.com/papers/finmoji/#footnote10)</sup>, which consists of 4,845 financial news articles with manually annotated sentiment. By the nature of the data, this model has probably not seen any emojis before.

DistilBERT ([Sanh et al., 2019](https://amahrous.com/papers/finmoji/#bib.bib59)) is a general language model designed to output the same probabilities as the BERT model, but it is smaller and faster. It is pre-trained on BookCorpus<sup>[11](https://amahrous.com/papers/finmoji/#footnote11)</sup> and the English Wikipedia<sup>[12](https://amahrous.com/papers/finmoji/#footnote12)</sup>. Using this model for sentiment analysis requires the addition of a classification layer, as it is not designed for text classification. This is accomplished with the DistilBertForSequenceClassification class from the Hugging Face transformers library. By the nature of the data, this model has probably not seen any emojis before.

FinancialBERT ([Hazourli, 2022](https://amahrous.com/papers/finmoji/#bib.bib34)) is a model designed for sentiment analysis of formal financial texts. It pre-trains the BERT model on financial news articles published by Reuters and Bloomberg, combined with a variety of corporate reports and earnings call transcripts. Similar to FinBERT, it then fine-tunes the pre-trained model on the Financial PhraseBank dataset. By the nature of the data, this model has probably not seen any emojis before.

CryptoBERT<sup>[13](https://amahrous.com/papers/finmoji/#footnote13)</sup> is a model designed for sentiment analysis of cryptocurrency-related texts. This is achieved by fine-tuning FinBERT using a small corpus of labeled cryptocurrency-related texts.

FinTwitBERT ([Stephan Akkerman, 2023](https://amahrous.com/papers/finmoji/#bib.bib66)) is a model designed for the sentiment analysis of financial tweets. It is pre-trained on 10 million financial tweets and then fine-tuned on around 40,000 human-labeled financial tweets (which are augmented by over 1 million synthetic tweets). It seems that this model has not incorporated emojis properly during fine-tuning, as evidenced by its performance on emojis; for instance, it has failed to classify a post consisting of only several rockets (🚀) as bullish, as a good model would.

Table 10. F<sub>1</sub> Scores of Fine-tuned Transformer-based BERT Models. This table presents the F<sub>1</sub> scores achieved by various BERT models when trained on text only, emojis only, and text with emojis.

<table> <tr> <th scope="col">F1 Score</th> <th scope="col">Text only</th> <th scope="col">Emojis only</th> <th scope="col">Text + Emojis</th></tr> <tr> <td>Model</td> <td></td> <td></td> <td></td></tr> <tr> <td>Twitter-RoBERTa</td> <td>0.84</td> <td>0.76</td> <td>0.88</td></tr> <tr> <td>FinBERT</td> <td>0.82</td> <td>0.69</td> <td>0.87</td></tr> <tr> <td>DistilBERT</td> <td>0.81</td> <td>0.69</td> <td>0.87</td></tr> <tr> <td>FinancialBERT</td> <td>0.80</td> <td>0.69</td> <td>0.86</td></tr> <tr> <td>CryptoBERT</td> <td>0.81</td> <td>0.69</td> <td>0.87</td></tr> <tr> <td>FinTwitBERT</td> <td>0.81</td> <td>0.69</td> <td>0.87</td></tr> </table>

It is noticeable that the models perform generally similarly, except for Twitter-RoBERTa. The similarity in performance signals the existence of a sharp decision boundary that all models converge to after fine-tuning. The models are also all derived from the same BERT architecture. Without fine-tuning them on our data, the models achieve significantly more varying accuracy; this variation is possibly due to the data they have been trained on initially, which does not include any social media or financial data for some of the models. Note that we fine-tuned and tested all models using the exact same data sample.

Some of the models remove emojis during the tokenization process. For them, we demojized the emojis. Demojizing emojis means converting emojis to their textual aliases or descriptions <sup>[14](https://amahrous.com/papers/finmoji/#footnote14)</sup>. The best-performing model was Twitter-RoBERTa, which is the only model tested that does not remove emojis during tokenization. The performance of Twitter-RoBERTa with and without demojizing is similar. So, it seems that the increased performance is specific to the way the model was pre-trained, taking emojis into consideration, while the other models excluded emojis.

For example, when processing a sentence containing multiple emojis, the tokenizer for Twitter-RoBERTa retains and correctly interprets emojis. After encoding these into numbers and then decoding them back to the text, the sentence is rendered as: \<s\>🔍👀 different tokenizers 🔣➡️🔢 emojis differently.\</s\>. In contrast, the tokenizers from all the other models tested failed to recognize emojis. After their encoding and subsequent decoding, they replace emojis with a placeholder token \[UNK\] (“unknown”), resulting in the following processed output for the above input: \[CLS\] \[UNK\] different tokenizers \[UNK\] emojis differently. \[SEP\]. This indicates that these models are either not trained to handle emojis or are designed to ignore them, possibly because they focus on data that does not include emojis, such as formal financial text or English books.

### 8. Discussion

This section discusses the main results of the paper, highlights implications, acknowledges limitations, and outlines future research directions.

#### 8.1. Results

In this study, we examined the role of emojis in financial sentiment analysis. Our objective was to determine the effectiveness and efficiency of using emojis for sentiment analysis in financial contexts, assessing aspects like accuracy performance, computational efficiency, data requirements, and usage patterns. Our research used data from 18.5 million posts, involving both a descriptive analysis of emoji usage and a comparative analysis using different sentiment analysis models. Our exploration revealed several key insights. While integrating both text and emojis yielded the highest accuracy in sentiment classification, using emojis alone demonstrated effective accuracy, with the added benefit of significantly lower data requirements and computational costs. Specific emojis and emoji pairs exhibited strong predictive power (above 90%) for bullish or bearish sentiment, highlighting their potential for efficient and rapid sentiment analysis. Our analysis also quantified the extreme difference in emoji usage between financial and general social media, emphasizing the need for domain-specific sentiment analysis models. Another surprising finding is that models trained on just 1,000 posts can achieve relatively high accuracy when emojis are considered, even when tested on a larger sample of 50,000 posts, highlighting the training dataset-size advantage working with emojis offers for sentiment analysis.

By utilizing transformer models and properly incorporating emojis, we achieved a sentiment classification accuracy of 0.88 F<sub>1</sub> score, surpassing the performance reported in several previous studies. Furthermore, our experimentation with various models, including traditional machine learning algorithms and transformer-based models, provided valuable insights into their accuracy and efficiency. For instance, the simpler logistic regression model performs on par with more complex and costly transformer models when analyzing emoji-only data. We also critically note that many Hugging Face models exclude emojis during tokenization, which impacts their effectiveness in contexts where emojis carry significant semantic weight.

#### 8.2. Implications

This study has several significant implications for financial sentiment analysis. Analyzing emoji usage offers valuable insights regarding investor behavior that can be used for models about financial and economic factors. Notably, emoji-based sentiment analysis, which requires fewer data and computational resources than traditional text-based methods, is particularly promising for high-frequency trading (where even microseconds matter ([Aquilina et al., 2022](https://amahrous.com/papers/finmoji/#bib.bib2))) and other scenarios where time, resources, or data may be limited. Moreover, the distinctive emoji usage patterns in financial social media—distinct from those observed in general social media—highlight the need for domain-specific sentiment analysis models. For instance, we observed that current emoji recommendation systems in popular mobile keyboards are not optimized for financial posts, suggesting a potential area for further research and development. Our research encourages the creation of specialized models that take into consideration the unique lexicon, including emojis, used in financial social media. By showing that emojis alone can achieve considerable accuracy in sentiment classification, this study aims to contribute to a paradigm shift in the use of emojis for financial sentiment analysis.

Table 11. Correlation between Frequency of Rockets and Asset Price and Volatility Index Changes.

<table> <tr> <th scope="col"></th> <th scope="col">QQQ</th> <th scope="col">BTC</th> <th scope="col">VIX</th></tr> <tr> <td>$\mathrm{Corr}(Rockets,\,\cdot)$</td> <td>0.4962</td> <td>0.5211</td> <td>-0.4046</td></tr> </table>

Interpretability and Practicality. The correlations reported in Table [11](https://amahrous.com/papers/finmoji/#S8.T11) serve as a pilot demonstration that emoji-based sentiment signals align with market dynamics. The Rocket Index—constructed as the daily proportion of posts containing the 🚀 emoji—moves positively with Bitcoin and Nasdaq 100 index returns, and negatively with the CBOE Volatility Index (VIX) index. This pattern confirms intuition: rocket emojis typically express enthusiasm and confidence, which rise during market upswings and decline when volatility or fear (VIX) increases. This interpretability strengthens the practical case for emoji-only approaches: they are transparent, language-agnostic, and computationally lightweight, yet remain relevant to real investor behavior. Such models can thus serve as efficient, explainable proxies for market sentiment in real-time applications.

#### 8.3. Limitations

While this study contributes valuable insights into the use of emojis for financial sentiment analysis, it is important to recognize its limitations. The analysis was confined to data sourced from StockTwits, which, while comprehensive and relevant, does not necessarily represent emoji usage across other platforms where financial discussions occur, such as Twitter or professional financial forums. StockTwits users predominantly communicate in English and come from specific demographic backgrounds, primarily within the United States ([SimilarWeb, 2023](https://amahrous.com/papers/finmoji/#bib.bib62)). This demographic concentration may not accurately reflect global financial social media, where cultural differences significantly influence emoji usage ([Guntuku et al., 2019a](https://amahrous.com/papers/finmoji/#bib.bib32)). The sentiment analysis conducted was binary, classifying posts as either bullish or bearish. This approach may oversimplify the complex emotions and sentiments expressed in financial discussions, such as uncertainty, caution, and speculation, which are also valuable for understanding market dynamics. It is also useful to note that emojis evolve in their usage and meanings over time, influenced by socio-cultural and technological changes ([Robertson et al., 2021](https://amahrous.com/papers/finmoji/#bib.bib57)).

Emoji-based sentiment analysis also faces an information challenge: emojis can be used sarcastically, ironically, or in combinations whose meaning depends on conversational context. Such nuances are hard to capture with emoji-only models and likely explain why text–emoji models perform better.

Another limitation is potential community bias. StockTwits activity is mostly driven by retail investors and sub-communities such as speculative meme-stock traders. Their posting styles differ from those of institutional or other investors. As a result, the model may overrepresent certain emojis. This effect is mitigated by including a diverse set of assets—including equities from the S&P 500, major cryptocurrencies, and the gold index—which together reflect the major discussions on the platform. However, the learned patterns are still valuable for the community they represent, which forms a significant part of online financial discussion. Prior studies show that emoji use varies across communities and cultures ([Guntuku et al., 2019a](https://amahrous.com/papers/finmoji/#bib.bib32); [Demirel et al., 2024](https://amahrous.com/papers/finmoji/#bib.bib22)), suggesting that such sub-cultural variation is normal in social media rather than unique to our dataset.

From an ethical standpoint, systems built only on emoji-based sentiment could be manipulated. For example, coordinated groups might flood discussions with specific emojis to create artificial optimism or pessimism. Future work should explore ways to detect such adversarial behaviors and adjust sentiment models to reduce the impact of such manipulation.

#### 8.4. Future Work

There are several promising areas of future research related to the topic of this study. One potential area of investigation is the creation of emoji-based financial sentiment indices, which could offer efficient and interpretable insights into market sentiment. Additionally, moving beyond binary sentiment classification, future research could explore the use of emojis for multinomial sentiment analysis to capture a broader spectrum of emotions and states relevant to financial decision-making, such as fear, greed, hope, rationality, and uncertainty. This approach would provide a more nuanced understanding of the emotions of financial markets, recognizing that investors with different states may impact the market differently, even if their overall sentiment (bullish or bearish) appears similar.

A formal study to establish that emojis in financial social media are culturally unbiased and, thus, can be used to help NLP models to generalize across different languages is also a very interesting research direction—albeit, the data at hand indicates a strong imbalance toward English on the StockTwits platform.

Beyond sentiment detection, emojis also hold the potential for identifying complex linguistic structures, such as sarcasm in financial communications, or for detecting spam. Moreover, investigating how emoji usage correlates with post-engagement could yield insights into the ways emojis influence investor interactions.

While our study demonstrates the effectiveness of emojis in sentiment analysis, there remains room for improvement in both sentiment analysis models and emoji lexicons. Future research can attempt to improve the accuracy or efficiency of financial sentiment analysis models. By sharing our code and methodology, we aim to facilitate reproducibility and encourage further research in this domain. We believe this can enable researchers to build upon our findings and improve the accuracy of financial sentiment analysis models, particularly given the limitations observed in previous studies. Additionally, there is a significant opportunity for future research to compare the effectiveness of different financial sentiment analysis models and emoji lexicons.

### 9. Ethical Compliance

All data used in this study were collected from publicly accessible StockTwits messages. The dataset contains only publicly posted content and does not include any private or direct messages. We process the data solely for academic research purposes and focus on aggregate sentiment patterns, without attempting to infer emotions or behavior of individual users. Under the European Union’s General Data Protection Regulation’s (GPDR) ([European Parliament and the Council of the European Union, 2016](https://amahrous.com/papers/finmoji/#bib.bib27)) academic-research exemption (Article 85, pp. 16–17), we process only publicly available information for scholarly purposes, and—since no private user data is involved—our procedures fall under the GDPR’s legitimate-interest basis (Article 6(1)(f), p. 12). In line with the GDPR principle of data minimisation, we restrict our analysis and discard any material not essential to our research objectives.

### 10. Conclusions

Our research demonstrates that emojis, often ignored in previous work and removed during preprocessing, hold significant value in financial sentiment analysis. Our findings suggest that emoji-based sentiment classification is not only effective but also computationally efficient, requiring significantly less data and processing power compared to text-based models.

The results show that models incorporating both text and emojis achieved the highest classification performance, with an F<sub>1</sub> score of 0.88 on a balanced dataset of 528,000 StockTwits posts (evenly split between bullish and bearish). Emoji-only models achieved F${}_{1}\approx 0.75$, capturing most of the predictive signal of the combined models while being substantially more computationally efficient. This efficiency makes them particularly attractive for time-sensitive financial applications such as high-frequency trading, where even microseconds matter ([Aquilina et al., 2022](https://amahrous.com/papers/finmoji/#bib.bib2)). Furthermore, our results indicate that even small training datasets (as few as 1,000 labeled posts) can train accurate sentiment classifiers when using emojis, whereas text-based models require significantly larger datasets to achieve comparable accuracy.

The emoji sentiment lexicon developed in this paper also provides insights into why emojis achieve such efficiency—certain emojis and emoji pairs alone can predict sentiment with over 90% accuracy. Another key insight from our analysis is that simpler models, such as logistic regression, achieve comparable accuracy to more complex transformer-based models when trained on emoji-only data. This indicates that emojis, as compact sentiment indicators, reduce the need for sophisticated deep learning architectures in financial sentiment analysis. Finally, our comparative analysis of emoji usage between financial and general social media contexts confirmed that financial platforms exhibit distinct emoji patterns, underscoring the necessity of domain-specific sentiment analysis models.

### Reproducibility and Data Availability

Code and data are publicly available at [https://github.com/AhmedMahrous00/finmoji\_replication](https://github.com/AhmedMahrous00/finmoji_replication).

### Acknowledgments

We would like to thank the anonymous reviewers for their valuable comments and suggestions.

The research reported in this publication was supported by funding from King Abdullah University of Science and Technology (KAUST) - Center of Excellence for Generative AI - under award number 5940.

### Notes

1. [https://www.vaneck.com/us/en/investments/social-sentiment-etf-buzz/overview/](https://www.vaneck.com/us/en/investments/social-sentiment-etf-buzz/overview/)[↩](https://amahrous.com/papers/finmoji/#ref-footnote1)
2. In this paper, we use the terms “Twitter” and “$\mathbb{X}$” interchangeably to refer to the same platform.[↩](https://amahrous.com/papers/finmoji/#ref-footnote2)
3. [https://www.nltk.org](https://www.nltk.org)[↩](https://amahrous.com/papers/finmoji/#ref-footnote3)
4. [https://pypi.org/project/wordcloud/](https://pypi.org/project/wordcloud/)[↩](https://amahrous.com/papers/finmoji/#ref-footnote4)
5. [https://www.kaggle.com/datasets/rexhaif/emojifydata-en?resource=download&select=emojitweets-01-04-2018.txt](https://www.kaggle.com/datasets/rexhaif/emojifydata-en?resource=download&select=emojitweets-01-04-2018.txt)[↩](https://amahrous.com/papers/finmoji/#ref-footnote5)
6. [https://scikit-learn.org](https://scikit-learn.org)[↩](https://amahrous.com/papers/finmoji/#ref-footnote6)
7. [https://huggingface.co](https://huggingface.co)[↩](https://amahrous.com/papers/finmoji/#ref-footnote7)
8. [https://pypi.org/project/emoji/](https://pypi.org/project/emoji/)[↩](https://amahrous.com/papers/finmoji/#ref-footnote8)
9. [https://trec.nist.gov/data/reuters/reuters.html](https://trec.nist.gov/data/reuters/reuters.html)[↩](https://amahrous.com/papers/finmoji/#ref-footnote9)
10. [https://github.com/vrunm/Text-Classification-Financial-Phrase-Bank](https://github.com/vrunm/Text-Classification-Financial-Phrase-Bank)[↩](https://amahrous.com/papers/finmoji/#ref-footnote10)
11. [https://yknzhu.wixsite.com/mbweb](https://yknzhu.wixsite.com/mbweb)[↩](https://amahrous.com/papers/finmoji/#ref-footnote11)
12. [https://huggingface.co/datasets/wikipedia](https://huggingface.co/datasets/wikipedia)[↩](https://amahrous.com/papers/finmoji/#ref-footnote12)
13. [https://huggingface.co/kk08/CryptoBERT](https://huggingface.co/kk08/CryptoBERT)[↩](https://amahrous.com/papers/finmoji/#ref-footnote13)
14. [https://pypi.org/project/emoji/](https://pypi.org/project/emoji/)[↩](https://amahrous.com/papers/finmoji/#ref-footnote14)

### References

 
- Aquilina et al. (2022)  Matteo Aquilina, Eric Budish, and Peter O’neill. 2022.  Quantifying the high-frequency trading “arms race”.  *The Quarterly Journal of Economics* 137, 1 (2022), 493–564.

- Araci (2019)  Dogu Araci. 2019.  FinBERT: Financial sentiment analysis with pre-trained language models.  , 10 pages.

- Ashish et al. (2017)  Vaswani Ashish, Shazeer Noam, Parmar Niki, Uszkoreit Jakob, Jones Llion, Gomez Aidan, Kaiser Lukasz, and Polosukhin Illia. 2017.  Attention Is All You Need. In *Advances in Neural Information Processing Systems (NeurIPS)*, Vol. 30. Curran Associates, Inc., Red Hook, NY, USA, 11 pages.

- Barbieri et al. (2020)  Francesco Barbieri, Jose Camacho-Collados, Luis Espinosa-Anke, and Leonardo Neves. 2020.  TweetEval: Unified Benchmark and Comparative Evaluation for Tweet Classification. In *Proceedings of Findings of EMNLP*. Association of Computational Linguistics, Stroudsburg, PA, USA, 1644–1650.

- Bashir et al. (2024)  Usman Bashir, Umar Nawaz Kayani, Shoaib Khan, Ali Polat, Muntazir Hussain, and Ahmet Faruk Aysan. 2024.  Investor sentiment and stock price crash risk: The mediating role of analyst herding.  *Computers in Human Behavior Reports* 13 (2024), 100371.

- Bashiri and Naderi (2024)  Hadis Bashiri and Hassan Naderi. 2024.  Comprehensive review and comparative analysis of transformer models in sentiment analysis.  *Knowledge and Information Systems* 66, 12 (2024), 7305–7361.

- Berger and Zhou (2014)  Vance W Berger and YanYan Zhou. 2014.  Kolmogorov–Smirnov test: Overview.  *Wiley statsref: Statistics reference online* (2014).

- Bouadjenek et al. (2023)  Mohamed Reda Bouadjenek, Scott Sanner, and Ga Wu. 2023.  A user-centric analysis of social media for stock market prediction.  *ACM Transactions on the Web* 17, 2 (2023), 1–22.

- Broni (2021)  Keith Broni. 2021.  Emoji Use at All-Time High.  Emojipedia Blog.   [https://blog.emojipedia.org/emoji-use-at-all-time-high/](https://blog.emojipedia.org/emoji-use-at-all-time-high/)  Accessed on October 28, 2025.

- Broni (2023)  Keith Broni. 2023.  10 Years of Emojipedia.  Emojipedia Blog.   [https://blog.emojipedia.org/10-years-of-emojipedia-10-years-of-record-breaking-emoji-popularity/](https://blog.emojipedia.org/10-years-of-emojipedia-10-years-of-record-breaking-emoji-popularity/)  Accessed on October 28, 2025.

- Brownlee (2021)  Jason Brownlee. 2021.  Gradient Boosting with Scikit-Learn, XGBoost, LightGBM, and CatBoost.  Machine Learning Mastery.   [https://machinelearningmastery.com/gradient-boosting-with-scikit-learn-xgboost-lightgbm-and-catboost/](https://machinelearningmastery.com/gradient-boosting-with-scikit-learn-xgboost-lightgbm-and-catboost/)  Accessed on October 28, 2025.

- Burge (2017)  Jeremy Burge. 2017.  5 Billion Emojis Sent Daily on Messenger.  Emojipedia Blog.   [https://blog.emojipedia.org/5-billion-emojis-sent-daily-on-messenger/](https://blog.emojipedia.org/5-billion-emojis-sent-daily-on-messenger/)  Accessed on October 28, 2025.

- Chen et al. (2018a)  Chung-Chi Chen, Hen-Hsen Huang, and Hsin-Hsi Chen. 2018a.  NTUSD-Fin: a market sentiment dictionary for financial social media data applications. In *Proceedings of the 1st Financial Narrative Processing Workshop (FNP 2018)*. European Language Resources Association (ELRA), Paris, France, 37–43.

- Chen et al. (2019)  Cathy Yi-Hsuan Chen, Li Guo, and Thomas Renault. 2019.  What Makes Cryptocurrencies Special? Investor Sentiment and Return Predictability.  *Investor Sentiment and Return Predictability* (2019), 36 pages.

- Chen et al. (2024)  Yihua Chen, Xingchen Yang, Hannah Howman, and Ruth Filik. 2024.  Individual differences in emoji comprehension: Gender, age, and culture.  *Plos one* 19, 2 (2024), e0297379.

- Chen et al. (2018b)  Z. Chen, X. Lu, W. Ai, H. Li, Mei, Q., and X. Liu. 2018b.  Through a gender lens: Learning usage patterns of emojis from large-scale android users. In *Proc. World Wide Web Conference*. ACM, New York, NY, 763–772.

- Cicekyurt and Bakal (2025)  Emre Cicekyurt and Gokhan Bakal. 2025.  Enhancing Sentiment Analysis in Stock Market Tweets Through BERT-Based Knowledge Transfer.  *Computational Economics* 48 (2025), 1–23.  Issue 1.

- Cramér (1946)  Harald Cramér. 1946.  *Mathematcal Methods of Statistics*.  Princeton University Press, Princeton, NJ, USA, Chapter 21. The two-dimensional case, 282.

- Daniel (2021)  Jennifer Daniel. 2021.  Emoji Frequency.  Unicode Consortium.   [https://home.unicode.org/emoji/emoji-frequency/](https://home.unicode.org/emoji/emoji-frequency/)  Accessed on October 28, 2025.

- Dat Quoc et al. (2020)  Nguyen Dat Quoc, Vu Thanh, and Nguyen Anh Tuan. 2020.  BERTweet: A pre-trained language model for English Tweets. In *Proceedings of the 2020 Conference on Empirical Methods in Natural Language Processing: System Demonstrations*. Association of Computational Linguistics, Stroudsburg, PA, USA, 9–14.

- Demirel et al. (2024)  Sadettin Demirel, Elif Kahraman, and Uğur Gündüz. 2024.  A text mining analysis of the change in status of the Hagia Sophia on Twitter: the political discourse and its reflections on the public opinion.  *Atlantic Journal of Communication* 32, 1 (2024), 63–90.

- Demirel et al. (2025)  Sadettin Demirel, Elif Kahraman-Gokalp, and Uğur Gündüz. 2025.  From optimism to concern: Unveiling sentiments and perceptions surrounding ChatGPT on Twitter.  *International Journal of Human–Computer Interaction* 41, 12 (2025), 7292–7314.

- Devlin et al. (2018)  Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2018.  BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding.  arXiv Preprint arXiv:1810.04805v2. , 16 pages.

- Dimson (2015)  Thomas Dimson. 2015.  Emojineering Part 1: Machine Learning for Emoji Trends.  Instagram Engineering Blog.   [https://instagram-engineering.com/emojineering-part-1-machine-learning-for-emoji-trends-7f5f9cb979ad](https://instagram-engineering.com/emojineering-part-1-machine-learning-for-emoji-trends-7f5f9cb979ad)  Accessed on October 28, 2025.

- Du et al. (2024)  Kelvin Du, Frank Xing, Rui Mao, and Erik Cambria. 2024.  Financial sentiment analysis: Techniques and applications.  *Comput. Surveys* 56, 9 (2024), 1–42.

- European Parliament and the Council of the European Union (2016)  European Parliament and the Council of the European Union. 2016.  Regulaton (EU) 2016/679 (General Date Protection Regulation).  [https://gdpr-info.eu/](https://gdpr-info.eu/).  *Official Journal of the European Union* (2016), L119/1–88.

- Gálvez and Gravano (2017)  Ramiro H Gálvez and Agustín Gravano. 2017.  Assessing the usefulness of online message board mining in automatic stock prediction systems.  *Journal of Computational Science* 19 (2017), 43–56.

- Gardazi et al. (2025)  Nadia Mushtaq Gardazi, Ali Daud, Muhammad Kamran Malik, Amal Bukhari, Tariq Alsahfi, and Bader Alshemaimri. 2025.  BERT applications in natural language processing: a review.  *Artificial Intelligence Review* 58, 6 (2025), 1–49.

- Gers et al. (2000)  Felix Gers, Jürgen Schmidhuber, and Fred Cummins. 2000.  Learning to forget: Continual prediction with LSTM.  *Neural Computation* 12, 10 (2000), 2451–2471.

- Gündüz and Demirel (2025)  Uğur Gündüz and Sadettin Demirel. 2025.  Metaverse-related perceptions and sentiments on Twitter: evidence from text mining and network analysis.  *Electronic Commerce Research* 25, 3 (2025), 1453–1483.

- Guntuku et al. (2019a)  Sharath Chandra Guntuku, Mingyang Li, Louis Tay, and Lyle H. Ungar. 2019a.  Studying Cultural Differences in Emoji Usage across the East and the West. In *Proceedings of the International AAAI Conference on Web and Social Media*, Vol. 13. AAAI, Westminster, UK, 226–235.

- Guntuku et al. (2019b)  Sharath Chandra Guntuku Guntuku, Mingyang Li, Louis Tay, and Lyle H. Ungar. 2019b.  Studying Cultural Differences in Emoji Usage across the East and the West. In *International AAAI Conference on Web and Social Media (ICWSM)*. AAAI, Westminster, UK, 226–235.

- Hazourli (2022)  Ahmed Hazourli. 2022.  FinBERT: a pretrained language model for financial text mining.  *International Joint Conference on Artificial Intelligence Organization* 2 (2022), 4513–4519.

- Hochreiter and Schmidhuber (1997)  Sepp Hochreiter and Jürgen Schmidhuber. 1997.  Long Short-Term Memory.  *Neural Computation* 9, 8 (1997), 1735–1780.

- Hutto and Gilbert (2014)  Clayton Hutto and Eric Gilbert. 2014.  VADER: A parsimonious rule-based model for sentiment analysis of social media text. In *Proceedings of the international AAAI conference on web and social media*, Vol. 8. AAAI, Washington, D.C., USA, 216–225.  Issue 1.

- jun Gu et al. (2024)  Wen jun Gu, Yi hao Zhong, Shi zun Li, Chang song Wei, Li ting Dong, Zhuo yue Wang, and Chao Yan. 2024.  Predicting stock prices with finbert-lstm: Integrating news sentiment analysis. In *Proceedings of the 2024 8th International Conference on Cloud and Big Data Computing*. ACM, New York City, NY, USA, 67–72.

- Kahraman et al. (2025)  Elif Kahraman, Sadettin Demirel, and Uğur Gündüz. 2025.  COVID-19 vaccines in twitter ecosystem: Analyzing perceptions and attitudes by sentiment and text analysis method.  *Journal of Public Health* 33, 5 (2025), 965–979.

- Kahraman-Gokalp et al. (2024)  Elif Kahraman-Gokalp, Sadettin Demirel, and Uğur Gündüz. 2024.  Exploring the surge of negativity during the COVID-19 pandemic: computational text and sentiment analysis across eight newsrooms’ tweets.  *Atlantic Journal of Communication* 32, 2 (2024), 298–324.

- Kejriwal et al. (2021)  Mayank Kejriwal, Qile Wang, Hongyu Li, and Lu Wang. 2021.  An empirical study of emoji usage on Twitter in linguistic and national contexts.  *Online Social Networks and Media* 24 (2021), #100149.

- Keles et al. (2023)  Feyza Duman Keles, Pruthuvi Mahesakya Wijewardena, and Chinmay Hegde. 2023.  On the computational complexity of self-attention. In *International Conference on Algorithmic Learning Theory*. PMLR, Westminster, UK, 597–619.

- Khan et al. (2025)  Amit Khan, Dipankar Majumdar, and Bikromadittya Mondal. 2025.  Sentiment analysis of emoji fused reviews using machine learning and Bert.  *Scientific Reports* 15, 1 (2025), 7538.

- Kulakowski and Frasincar (2023)  Mikolaj Kulakowski and Flavius Frasincar. 2023.  Sentiment Classification of Cryptocurrency-Related Social Media Posts.  *IEEE Intelligent Systems* 38, 4 (2023), 5–9.

- Liu et al. (2019)  Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke Zettlemoyer, and Veselin Stoyanov. 2019.  RoBERTa: A Robustly Optimized BERT Pretraining Approach.  arXiv preprint arXiv:1907.11692v1. , 13 pages.

- Loughran and McDonald (2011)  Tim Loughran and Bill McDonald. 2011.  When is a liability not a liability? Textual analysis, dictionaries, and 10-Ks.  *The Journal of finance* 66, 1 (2011), 35–65.

- Loureiro et al. (2022)  Daniel Loureiro, Francesco Barbieri, Leonardo Neves, Luis Espinosa Anke, and Jose Camacho-Collados. 2022.  TimeLMs: Diachronic language models from Twitter.  arXiv preprint arXiv:2202.03829. , 10 pages.

- Mahendran et al. (2025)  Manish Barath Mahendran, Aswin Kumar Gokul, Poornima Lakshmi, and S Pavithra. 2025.  Comparative Advances in Financial Sentiment Analysis: A Review of BERT, FinBert, and Large Language Models. In *2025 3rd International Conference on Intelligent Data Communication Technologies and Internet of Things (IDCIoT)*. IEEE, New York City, NY, USA, 39–45.

- Mahmoudi et al. (2018)  Nader Mahmoudi, Paul Docherty, and Pablo Moscato. 2018.  Deep neural networks understand investors better.  *Decision Support Systems* 112 (2018), 23–34.

- Mahmoudi et al. (2022)  Nader Mahmoudi, Łukasz P Olech, and Paul Docherty. 2022.  A comprehensive study of domain-specific emoji meanings in sentiment classification.  *Computational Management Science* 19, 2 (2022), 159–197.

- Mahrous et al. (2023)  Ahmed Mahrous, Jens Schneider, and Roberto Di Pietro. 2023.  The Role of Emojis in Sentiment Analysis of Financial Microblogs. In *2023 Fourth International Conference on Intelligent Data Science Technologies and Applications (IDSTA)*. IEEE, New York City, NY, USA, 76–84.

- Mann and Whitney (1947)  Henry Mann and Donald Whitney. 1947.  On a Test of Whether one of Two Random Variables is Stochastically Larger then the Other.  *Annals of Mathematical Statistics* 18, 1 (1947), 50–60.

- Matthews (1975)  B.W. Matthews. 1975.  Comparison of the predicted and observed secondary structure of T4 phage lysozyme.  *Biochimica et Biophysica Acta (BBA) - Protein Structure* 405, 2 (1975), 442–451.

- Nasekin and Chen (2020)  Sergey Nasekin and Cathy Yi-Hsuan Chen. 2020.  Deep learning-based cryptocurrency sentiment construction.  *Digital Finance* 2, 1 (2020), 39–67.

- Omar and Lasrado (2023)  Hibaq Omar and Lester Allan Lasrado. 2023.  Uncover Social Media Interactions On Cryptocurrencies Using Social Set Analysis (SSA).  *Procedia Computer Science* 219 (2023), 161–169.

- Renault (2020)  Thomas Renault. 2020.  Sentiment analysis and machine learning in finance: a comparison of methods and models on one million messages.  *Digital Finance* 2, 1-2 (2020), 1–13.

- Reschke and Strych (2024)  Felix Reschke and Jan-Oliver Strych. 2024.  Emojis and stock returns.  *Review of Behavioral Finance* 16, 2 (2024), 223–233.

- Robertson et al. (2021)  Alexander Robertson, Farhana Ferdousi Liza, Dong Nguyen, Barbara McGillivray, and Scott A. Hale. 2021.  Semantic Journeys: Quantifying Change in Emoji Meaning from 2012–2018.  , 10 pages.

- Rosenthal et al. (2019)  Sara Rosenthal, Noura Farra, and Preslav Nakov. 2019.  SemEval-2017 task 4: Sentiment analysis in Twitter.  arXiv preprint arXiv:1912.00741. , 17 pages.

- Sanh et al. (2019)  Victor Sanh, Lysandre Debut, Julien Chaumond, and Thomas Wolf. 2019.  DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter.  , 5 pages.

- Shannon (1951)  Claude E Shannon. 1951.  Prediction and entropy of printed English.  *Bell system technical journal* 30, 1 (1951), 50–64.

- Shiri et al. (2023)  Mohammad Shiri, Oleksii Dubovyk, Golbarg Roghaniaraghi, and Sampath Jayarathna. 2023.  Meme it Up: Patterns of Emoji Usage on Twitter. In *2023 IEEE 24th International Conference on Information Reuse and Integration for Data Science (IRI)*. IEEE, New York City, NY, USA, 205–210.

- SimilarWeb (2023)  SimilarWeb. 2023.  StockTwits Website Traffic Statistics.  SimilarWeb.   [https://www.similarweb.com/website/stocktwits.com/#geography](https://www.similarweb.com/website/stocktwits.com/#geography)  Accessed on October 28, 2025.

- Smirnov (2017)  Ivan Smirnov. 2017.  The digital flynn effect: Complexity of posts on social media increases over time. In *International Conference on Social Informatics*. Springer, 24–30.

- Smirnov (1948)  Nickolay Smirnov. 1948.  Table for estimating the goodness of fit of empirical distributions.  *Annals of Mathematical Statistics* 19, 2 (1948), 279–281.

- Spärck Jones (1972)  K. Spärck Jones. 1972.  A Statistical Interpretation of Term Specificity and Its Application in Retrieval.  *Journal of Documentation* 28, 1 (1972), 11––21.

- Stephan Akkerman (2023)  Tim Koornstra Stephan Akkerman. 2023.  FinTwitBERT: A Specialized Language Model for Financial Tweets.  [https://github.com/TimKoornstra/FinTwitBERT](https://github.com/TimKoornstra/FinTwitBERT).    Accessed October 28, 2025.

- Vamossy (2021)  Domonkos F Vamossy. 2021.  Investor emotions and earnings announcements.  *Journal of Behavioral and Experimental Finance* 30 (2021), 100474.

- van der Veen and Bleich (2025)  A Maurits van der Veen and Erik Bleich. 2025.  The advantages of lexicon-based sentiment analysis in an age of machine learning.  *PloS one* 20, 1 (2025), e0313092.

- Wilksch and Abramova (2023)  Moritz Wilksch and Olga Abramova. 2023.  PyFin-sentiment: Towards a machine-learning-based model for deriving sentiment from financial tweets.  *International Journal of Information Management Data Insights* 3, 1 (2023), #100171.

- Zhou et al. (2024)  Giulio Zhou, Sydelle De Souza, Ella Markham, Oghenetekevwe Kwakpovwe, and Sumin Zhao. 2024.  Semantics and Sentiment: Cross-lingual Variations in Emoji Use. In *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing (EMNLP)*. Association for Computational Linguistics, Stroudsburg, PA, USA, 18698–18712.   [https://doi.org/10.18653/v1/2024.emnlp-main.1041](https://doi.org/10.18653/v1/2024.emnlp-main.1041)

- Zuo et al. (2024)  Xiaorui Zuo, Yao-Tsung Chen, and Wolfgang Härdle. 2024.  Emoji Driven Crypto Assets Market Reactions.  arXiv preprint arXiv:2402.10481. , 29 pages.

Last updated: October 2026.
