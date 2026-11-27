# SoK: A structured analysis of economic and technical stablecoin-related research

Source: [https://amahrous.com/papers/stablecoin-sok/](https://amahrous.com/papers/stablecoin-sok/)

[← Ahmed Mahrous’s homepage](https://amahrous.com/#research)

Ahmed Mahrous, Maurantonio Caprolu, and [Roberto Di Pietro](https://cemse.kaust.edu.sa/profiles/roberto-di-pietro)

*IEEE International Conference on Blockchain and Cryptocurrency (ICBC 2025)* · 2025 · 18.2% acceptance

[PDF](https://amahrous.com/papers/stablecoin-sok/paper.pdf) · [Read full text](https://amahrous.com/papers/stablecoin-sok/#full-text) · [BibTeX](https://amahrous.com/papers/stablecoin-sok/citation.bib) · [DOI](https://doi.org/10.1109/icbc64466.2025.11114650) · [Cite](https://amahrous.com/papers/stablecoin-sok/#citation)

## TL;DR

A structured account of economic and technical research on stablecoins.

## Abstract

Stablecoins, with a capitalization exceeding 200 billion USD as of January 2025, have shown significant growth in both supported transactions and volumes, with annual transaction volumes exceeding 10 trillion dollars in 2023 and nearly doubling that figure in 2024. This exceptional growth has attracted the attention of traditional financial institutions, with an increasing number of governments exploring the potential of Central Bank Digital Currencies (CBDCs). Although academia has recognized the importance of stablecoins, research in this area remains fragmented, incomplete, and sometimes contradictory.

In this Systematization of Knowledge (SoK), we aim to address the cited gap with a structured literature analysis, correlating recent contributions to present a picture of the complex economic and technical aspects of stablecoins. To achieve this, we identify the main research questions and categorize scientific contributions accordingly, identifying data sources, methodologies, and open research questions. Our analysis reveals numerous significant findings across economic and technical domains. It also highlights significant research gaps, including limited studies on security and privacy, underexplored stablecoins, and unexamined stablecoin failure cases, paving the way for further research in the domain.

## Citation

Ahmed Mahrous, Maurantonio Caprolu, and Roberto Di Pietro. 2025. SoK: A structured analysis of economic and technical stablecoin-related research. 2025 IEEE International Conference on Blockchain and Cryptocurrency (ICBC), 1–21. [doi:10.1109/icbc64466.2025.11114650](https://doi.org/10.1109/icbc64466.2025.11114650).

```bibtex
@inproceedings{stablecoin-sok-2025,
  author = {Mahrous, Ahmed and Caprolu, Maurantonio and Di Pietro, Roberto},
  title = {{SoK: A structured analysis of economic and technical stablecoin-related research}},
  year = {2025},
  doi = {10.1109/icbc64466.2025.11114650},
  publisher = {IEEE},
  booktitle = {2025 IEEE International Conference on Blockchain and Cryptocurrency (ICBC)},
  pages = {1--21},
  url = {https://doi.org/10.1109/icbc64466.2025.11114650}
}
```

## Full text

### I. INTRODUCTION

A stablecoin is a class of digital assets designed to maintain a stable value relative to a reference asset or basket of assets. Stablecoins play an essential role in the digital finance ecosystem, addressing one of the primary limitations of cryptocurrencies—price volatility—while leveraging the benefits of blockchain technology. They enable numerous use cases in the DeFi ecosystem—from low volatility collateral for DeFi treasuries, derivatives, and loans to a stable medium of exchange and store of value. They also expand foreign currency accessibility, particularly in regions with large unbanked populations or restrictive capital controls.

Stablecoins achieve price stability through various mechanisms, including full or partial collateralization, algorithmic control of supply, or a combination thereof. For instance, a widely used algorithmic stability mechanism is supply rebase. In this mechanism, if the price is above the peg, more tokens are minted and distributed to holders, and if below the peg, tokens are burned. Often, this is combined with other algorithmic mechanisms, such as dual-token stabilization, where the impact of minting or burning is absorbed by

holders of a secondary, more risky token instead of directly affecting stablecoin holders. Despite the growing importance of stablecoins, reflected in academia through the increasing volume of the literature on the topic, research in this area is still in its early stages, with fragmented results and sometimes questionable methodologies. Stablecoin research explores a diverse array of topics, reflecting the interplay of economic and technical aspects. In terms of economic research, significant efforts have focused on understanding the price dynamics of stablecoins, their interconnectedness with other assets and external forces, and their stability. Meanwhile, technical studies have explored novel design proposals, stabilization mechanisms, causes and impacts of failures, and issues related to security and privacy. The interdisciplinary nature of stablecoin research, integrating concepts from computer science, finance, and related fields, is reflected in the wide range of methodologies and data sources it employs. Data sources include, among others, cryptocurrency price and trading volume data, blockchain transaction data from explorers such as Etherscan, and synthetic data. Methodologies include, among others, econometric models (e.g. regression, GARCH, and VAR—formal theoretical modeling), network analysis, review of stablecoin white papers, and system design frameworks. Given the recency of stablecoin research, significant research gaps exist. These include gaps in critical areas such as the privacy and security of stablecoins, unexamined failure cases, the analysis of underexplored unique stablecoins, and unstudied governance mechanisms.

The fragmented nature of stablecoin studies and the diversity of the issues at stake make it challenging to synthesize insights. Our SoK aims to fill this gap. Existing surveys often focus on particular stablecoin projects (mainly investigating their stabilization mechanisms) rather than providing a broad review of academic studies. This contrasts with our approach, which seeks to synthesize current literature and guide future research. While two recent literature reviews \[7, 84\] offer valuable insights, they are limited in scope and depth. For instance, Ante et al. \[7\] reviewed only 22 empirical studies, and Li et al. \[84\] focused on three predefined questions about stabilization mechanisms and payment applicability rather than a more holistic analysis of stablecoin literature.

**Rise and importance of stablecoins:** The significant im-

pact of stablecoins in the financial market is highlighted by their overall capitalization and transaction volume. The combined market capitalization of stablecoins surpasses $200 billion as of the time of this writing<sup>1</sup> , a more than thirty-fold increase since the start of 2020 \[33\]. As for 2024, volume amounted to 8 *.* 5 trillion across 1 *.* 1 billion transactions<sup>2</sup> in the second quarter of 2024 (ending June 2024). Stablecoin transaction volumes more than doubled Visa’s 3 *.* 9 trillion in transactions over the same period. An expected future rise in institutional and governmental interest and increased adoption of DeFi will lead to a further increase in stablecoin significance. Corporations, including BlackRock \[19\], PayPal \[100\], JPMorgan Chase \[104\], and Facebook \[119\] have proposed or developed their own stablecoin.

The rationale behind this remarkable growth can be attributed to several key features. These include seamless crossborder transactions, programmability, enhanced liquidity, support for DeFi applications, and a reliable medium of exchange within digital ecosystems. Their increasing adoption by institutional investors, payment networks, and central banks highlights their transformative potential in reshaping the global financial infrastructure. Furthermore, as regulatory frameworks continue to evolve, stablecoins are positioned to drive financial inclusion and improve efficiency in global finance.

At the time of writing, more than 99% of stablecoins by market capitalization are pegged to the USD<sup>3</sup> . The proliferation of USD-collateralized stablecoins beyond the currency’s traditional uses increases demand for the USD— provided that it supplements, rather than displaces, existing demand—thereby reinforcing its geopolitical influence. Moreover, when USD-collateralized stablecoins replace local currencies in certain nations, they challenge those nations’ monetary sovereignty and establish de-facto dollarization \[83\]. Such geopolitical dynamics heighten the motivation of governments around the world to develop their own stablecoin solutions. According to the Atlantic Council’s CBDC Tracker, 44 countries are piloting central bank digital currencies (CBDCs), including major economies such as China and the Eurozone \[9\]. This SoK intends to shed light on such a critical element of the crypto ecosystem.

**Contributions:** Our paper uniquely contributes to the field by systematically categorizing the stablecoin literature, summarizing and analyzing key findings, methodologies, and data sources, and identifying significant open research questions. Our main contributions can be summarized as follows.

 
- We identify 13 main research questions in stablecoinrelated literature and categorize existing studies accordingly;

- We summarize findings from the literature, simplifying complex analyses and highlighting areas of agreement and disagreement among researchers;

> 1https://forbes.com/digital-assets/categories/stablecoins/?sh=46fd218a1cd0
> 
>  
> 
> 2https://a16zcrypto.com/posts/article/state-of-crypto-report-2024/
> 
>  
> 
> 3https://defillama.com/stablecoins

 
- We detail the data sources and methodologies used to address the research questions;

- After critically reviewing methodologies and conclusions, we identify significant research gaps, areas of contention, and new research questions;

**Roadmap:** The rest of this paper is organized as follows. Section II presents existing surveys and SoK papers related to stablecoins, highlighting their limitations. Section III details the methodology of our SoK, including the search strategy, research categorization, and objectives. Sections IV and V present the core of our analysis, exploring the economic and technical dimensions of stablecoin research, respectively. Section VI discusses several of the significant findings and research gaps, as well as offers general insights about the reviewed research works. Section VII concludes the paper by providing a general overview of the SoK’s insights, contributions, and future research directions.

### II. RELATED WORK

Despite the importance of the topic, there is a lack of systematic literature reviews focusing on stablecoins. Most existing surveys emphasize reviewing stablecoin projects (e.g., focusing on associated white papers) rather than stablecoinrelated academic literature \[127, 30, 101, 91, 92\]. Only two papers offer a review of the literature \[7, 84\], but neither of them provides a comprehensive understanding of stablecoinrelated academic work, as shown in the following.

First, Ante et al. \[7\] provided a significantly narrower contribution compared to our Systemization of Knowledge (SoK), examining only 22 empirical studies categorized into three main topics. Our SoK not only covers a broader range of topics but also includes more papers on the main topics identified in \[7\]. Furthermore, we explore papers with greater depth, analyzing not only their results but also their methodologies, data sources, and research gaps.

Second, while a more extensive set of research papers is considered in \[84\] compared to \[7\], the approach in \[84\] differs significantly from ours. Specifically, Li et al. \[84\] constructed a survey paper that focuses on the structure, stabilization mechanisms, and applicability of stablecoins as a payment system. In contrast, our SoK provides a more comprehensive analysis, examining a broader body of stablecoin-related literature. This results in the coverage of topics not covered in \[84\], such as price modeling of stablecoins, interconnectedness with other assets, and failures of stablecoins. Additionally, we provide more detailed coverage of the topics included in \[84\].

Table I compares surveys and SoKs related to stablecoins with our paper. The papers we analyzed for this SoK are systematically categorized in Table II, with their contributions discussed in detail in the subsequent sections.

### III. METHODOLOGY, CATEGORIZATION, AND OBJECTIVES

Our paper aimed to provide a more systematic, extensive, and in-depth review of the academic literature related to stablecoins. To do that, we queried the Scopus Search Engine to identify papers that mention “stablecoin” in the

COMPARISON OF STABLECOIN SURVEYS/SOK

<table><tr><th>Paper</th><th>Systematic Lit-<br>erature Review</th><th>Categorization<br>of Literature</th><th>Comprehensive<br>Overview of<br>Literature</th><th>Research Gaps<br>Identified</th><th>Methodologies<br>Identified</th><th>Data Sources<br>Identified</th></tr><tr><td>[7]</td><td></td><td></td><td>✗</td><td></td><td></td><td></td></tr><tr><td>[84]</td><td></td><td></td><td>✗</td><td></td><td>✗</td><td>✗</td></tr><tr><td>[127]</td><td>✗</td><td>✗</td><td>✗</td><td></td><td>✗</td><td>✗</td></tr><tr><td>[30]</td><td>✗</td><td>✗</td><td>✗</td><td>✗</td><td>✗</td><td>✗</td></tr><tr><td>[101]</td><td>✗</td><td>✗</td><td>✗</td><td></td><td>✗</td><td>✗</td></tr><tr><td>[91]</td><td>✗</td><td>✗</td><td>✗</td><td>✗</td><td>✗</td><td>✗</td></tr><tr><td>[92]</td><td>✗</td><td>✗</td><td>✗</td><td></td><td>✗</td><td>✗</td></tr><tr><td>Our Paper</td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

title, abstract, or keywords. Due to the broad scope of the designed query, we obtained a large and diverse collection of Scopus-indexed papers related to stablecoins, ensuring a comprehensive analysis of the relevant literature. The results from this query were also cross-checked with searches from Google Scholar. This resulted in 239 documents.

The query used to search for papers on the Scopus Search Engine is the following:

TITLE-ABS-KEY (stablecoin\* OR "stable coin\*") LOAD-DATE \< 20240611 AND (LIMIT-TO (DOCTYPE,"ar") OR LIMIT-TO (DOCTYPE,"cp") OR LIMIT-TO (DOCTYPE,"re") OR LIMIT-TO (DOCTYPE,"cr")) AND (LIMIT-TO (LANGUAGE,"English"))

Some documents have been removed due to being inaccessible, i.e., behind paywalls, no longer available in their publisher digital library, etc. (11 papers), not being in English (1 paper), or not focusing significantly on Stablecoins (18 papers). The remaining 209 documents have been analyzed to determine their topic of analysis.

Our analysis focuses on two primary domains—the economic and technical aspects of stablecoins. Within each domain, we identified the main research questions and categorized them into seven distinct sub-categories. Then, we analyzed all the 209 papers and we included in our study only those that made a significant contribution to addressing at least one of the identified research questions. Table II reports the 13 research questions to give a clearer overview of this categorization. The number of papers in each macro-category, sub-category, and research question is between parentheses. The 111 considered papers have been analyzed in depth to highlight their results, methodologies, and datasets and to identify common research gaps and open questions. This information is synthesized for all the papers in each research question.

**Structure of the SoK:** This paper provides a systematic overview of the economic and technical research questions addressed in stablecoin-related academic literature. While connections between research questions are discussed where rele-

vant, each question is analyzed in depth by correlating results, methodology, and lessons learned from all the papers that contributed significantly to addressing this particular question. Insights derived from this analysis are integrated throughout the discussion, with research gaps identified and addressed at the end of each sub-category. This structure allows readers to easily locate the findings, methodologies, and research gaps most relevant to their interests, minimizing search efforts. For convenience, Table II presents a broad overview of all discussed research questions.

### IV. ECONOMIC ANALYSIS

This section synthesizes stablecoin research within the macro-category of economic analysis, which includes three subcategories: stablecoins’ interconnectedness with other markets and factors, stability analysis, and price and ecosystem modeling. Six research questions are addressed under this category, and the results and methodologies of related studies are synthesized. Research gaps are analyzed collectively for each sub-category.

### *A. Stablecoin Price/Volume Correlation With Other Factors*

### *(1)* ***How Does The Price Of Stablecoins Move In Relationship To The Price Of Other Financial Assets?***

The stability of stablecoins is especially evident during periods of high market volatility, such as the COVID-19 pandemic and geopolitical events like the Russia-Ukraine war. During these times, many financial assets experience heightened volatility, whereas stablecoins tend to maintain relative stability \[116, 14, 78, 62\]. This low or negative correlation with other assets enables stablecoins to act as a hedge against market downturns, offering investors a means to reduce portfolio risk \[4, 49, 79\].

However, the effectiveness of stablecoins as safe havens or hedging instruments depends significantly on the type of stablecoin and prevailing market conditions. Gold-backed stablecoins like PAX Gold (PAXG) and Perth Mint Gold Token (PMGT) serve as strong diversifiers during normal market conditions and as robust safe havens during bear markets for certain asset classes \[15\]. In contrast, USD-pegged stablecoins, such as Tether (USDT) and USD Coin (USDC),

MACRO-CATEGORIES, SUB-CATEGORIES, AND RESEARCH QUESTIONS. NUMBER OF RELATED PAPERS IS IN PARENTHESES.

<table><tr><th>Macro-<br>Category</th><th>Sub-Category</th><th>Research Questions</th></tr><tr><td rowspan="6">Economic<br>Analysis<br>(72)</td><td rowspan="2">Stablecoin Price/Volume<br>Correlation with Other Factors<br>(48)</td><td>How does the price of stablecoins move in relationship to the price of other financial assets? (37)</td></tr><tr><td>How do macroeconomic, blockchain, media, social, climate and regulatory factors interact with stable-<br>coins? (11)</td></tr><tr><td rowspan="2">Stablecoin Stability Analysis (13)</td><td>How stable are stablecoins in general market conditions? (8)</td></tr><tr><td>How stable are stablecoins during periods of market turbulence or crisis? (5)</td></tr><tr><td rowspan="2">Price Modeling (11)</td><td>What are the properties of stablecoins’ prices in terms of linearity, stationarity, time-variation, regime-<br>switching, normality, heavy-tails, and autoregressive behavior, etc.? (9)</td></tr><tr><td>How can actors in stablecoin ecosystems be modeled using computational simulations? (2)</td></tr><tr><td rowspan="7">Technical<br>Analysis<br>(39)</td><td>Design and Implementation (13)</td><td>How can we improve the design and implementation of stablecoins? (13)</td></tr><tr><td>Stablecoin Mechanisms (14)</td><td>What are the characteristics of stabilization mechanisms used in stablecoins? (14)</td></tr><tr><td rowspan="2">Failure Analysis (8)</td><td>What are the causes of previous stablecoin failures? (4)</td></tr><tr><td>What are the impacts of previous stablecoin failures? (4)</td></tr><tr><td rowspan="3">Security and Privacy (4)</td><td>What are the privacy concerns related to CBDCs, and how are they being addressed? (1)</td></tr><tr><td>What are the security threats related to CBDCs and stablecoins? (2)</td></tr><tr><td>How can market manipulation related to stablecoins be detected? (1)</td></tr></table>

outperform gold-pegged stablecoins in reducing portfolio risk during periods of financial distress \[116, 39, 46\]. This can be attributed to the higher volatility of gold compared to the USD \[116\] and the specific mechanisms of certain stablecoins, such as Digix Gold \[39\]. Additionally, USD-pegged stablecoins benefit from larger market capitalization and more reputable issuers.

*Insight 1:* There is a consensus among researchers that stablecoins generally exhibit low or negative correlation with both cryptocurrencies and traditional assets, particularly during market stress.

Beyond their effectiveness as portfolio diversifiers, stablecoins have also been studied to detect their influence on other financial markets. Tether, for example, holds reserves—including money market funds—to back its issued stablecoins. Tether’s buying or selling of these reserve assets can significantly impact the market prices of these reserves \[120\]. Additionally, stablecoins like TrueUSD, USD Coin, and Tether have a dynamic and bidirectional causal relationship with crude oil prices \[54\]. This relationship likely reflects the interplay between the underlying asset, the US dollar, and oil prices.

Other studies have examined the interaction between stablecoins and cryptocurrencies. Grobys and Huynh \[57\] observed that jumps in Tether prices can predict a fall in Bitcoin prices, while Alexander et al. \[2\] highlighted the role of Tethermargined contracts in transmitting volatility to Bitcoin prices. Traders often move assets between stablecoins and non-stable cryptocurrencies, depending on the market sentiment. As they get more bearish, they transfer their money from volatile cryptocurrencies to stablecoins, a phenomenon termed “flightto-cryptosafety”. Leveraged margined contracts amplify this relationship by enabling the transfer of larger sums. Several

other authors, including Paeng et al. \[99\] and Gubareva et al. \[59\], have similarly identified bidirectional causality and spillover effects between stablecoins, major cryptocurrencies, and traditional financial assets, highlighting the increasing connectivity of stablecoin markets within the broader financial system. However, this growing interdependence can reduce the effectiveness of stablecoins as portfolio diversifiers.

Conversely, some studies challenge the extent of these spillover effects. Chen and Chang \[27\] and Kołodziejczyk \[79\] reported minimal causality and spillover effects between stablecoins and other assets like cryptocurrencies or stocks, emphasizing stablecoins’ relative stability. These contrasting findings are likely due to differences in methodologies, data granularity, sample periods, and model specifications. For instance, Grobys and Huynh \[57\] applied the methodology of Barndorff-Nielsen and Shephard \[13\] to high-frequency hourly price data spanning November 2018 to June 2021. In contrast, Chen and Chang \[27\] employed a combination of GARCH and VAR models on lower-frequency daily price data over a broader period from July 2014 to February 2022.

*Insight 2:* The presence of spillovers between volatile cryptocurrencies and stablecoins remains subject to ongoing debate.

**Methodologies** A range of econometric models has been employed to capture dependencies between the time series of stablecoin prices and other financial assets. These models reflect the need to account for characteristics such as volatility clustering, non-linear relationships, and behavior under extreme market conditions. These include GARCH, copula, quantile-based, dummy regression, vector autoregression, vector error correction, causality, and transfer entropy models.

Among these, GARCH models and their variants have been the most commonly employed. For example, \[116\],

\[46\], and \[78\] employ GARCH models to analyze volatility dependencies. Asymmetric variants, such as EGARCH and GJR-GARCH, are sometimes chosen because negative price shocks can cause greater volatility in other assets compared to positive shocks \[78\], \[116\], \[46\]. Additionally, DCC-GARCH models are applied in \[116\] and \[46\] to capture time-varying relationships between assets.

Compared to GARCH models, copula models better capture non-linear dependencies and have been employed by several authors \[15, 27\]. Similarly, quantile-based models address nonlinearity by analyzing comovements across different quantiles of the price distribution. Accounting for non-linearity is important because non-linearity has been documented in stablecoins’ time series \[88, 102\].

Regression models with dummy variables were used in \[14\] and \[49\]. The authors regressed stablecoin price returns against dummy variables corresponding to significant declines in other assets, helping to classify stablecoins as safe havens.

Vector Error Correction (VEC) and Vector Autoregression (VAR) models were employed in \[4\] and \[99\]. These models capture the lead-lag relationship and cointegration between stablecoins and other assets. Gubareva et al. \[59\] utilized a causality test to analyze the predictive relationships between stablecoins and other financial assets across different quantiles. Paeng et al. \[99\] used a VAR model with quantile Granger causality.

Ghabri et al. \[54\] used transfer entropy to study the information flow between energy markets, cryptocurrencies, and stablecoins. An advantage of the transfer entropy model is that it is nonparametric, requiring fewer assumptions about the underlying data-generating process.

*Insight 3:* The most commonly used econometric models (e.g., VAR, VEC, GARCH, regression) do not take into account the specific behaviors of stablecoin time series which have been demonstrated by other researchers, such as non-linearity.

***(2) How Do Macroeconomic, Blockchain, Media, Social, Climate, and Regulatory Factors Interact With Stablecoins***

Studies have found that higher U.S. federal funds rates and Chinese interbank rates reduce stablecoin prices and their price volatility while increasing their trading volumes \[95\]. The price decrease is likely due to a shift in capital from stablecoins to interest-bearing assets like bonds or savings accounts following an interest rate hike. However, it remains unclear why stablecoin price volatility decreases despite the drop in prices.

Bojaj et al. \[21\] explored the macroeconomic effects of stablecoin adoption in Montenegro. They found that while stablecoins positively impact GDP, they may struggle to maintain their peg during market crashes, potentially destabilizing the economy.

Osman et al. \[98\] reported that economic sentiment significantly impacts the cryptocurrency market, especially during periods of uncertainty (e.g., COVID-19). Negative economic sentiment can increase demand for stablecoins as safe assets. Media announcements have a heterogeneous impact on stablecoin transaction volumes. For example, Tether (USDT) is

particularly influenced by media reports, with both positive and negative news leading to increases in trading volumes. Decentralized stablecoins like DAI are more sensitive to institutional announcements compared to centralized stablecoins such as USDC and USDT \[38\].

Ante and Saggu \[5\] found a bidirectional causal relationship between stablecoin transaction fees and stablecoin transactions: high fees deter users from transacting using stablecoins, and increased demand for stablecoin transactions drives up transaction fees as users compete for the limited capacity on the network.

Environmental variables, such as *CO* 2 emissions and temperature anomalies, significantly predict the returns of volatile cryptocurrencies like Bitcoin and Ethereum. However, these environmental factors do not predict the returns of stablecoins like Tether (USDT) and TrueUSD. This indicates that investors do not associate stablecoin returns with environmental factors due to their non-energy-intensive nature \[29\].

Ayadi et al. \[10\] explored the impact of CBDCs on stablecoins, finding that the CBDC Uncertainty Index is negatively related to stablecoin returns. High uncertainty around CBDC developments can decrease stablecoin valuations, reflecting investors’ concerns about competition or regulatory uncertainties.

Also, governmental regulatory policies can significantly affect stablecoins. For instance, the Chinese government’s regulatory actions in May 2021 had a markedly negative impact on the cryptocurrency market, including stablecoins \[110\]. Chinese regulators announced that cryptocurrencies could not be used as currency and prohibited many cryptocurrencyrelated services.

*Insight 4:* Stablecoin markets are influenced by a variety of factors, including interest rates, economic sentiment and uncertainty, and regulatory policies.

*Insight 5:* Stablecoin activity has been found to influence macroeconomic factors, transaction fees on blockchains, and the traditional finance market (e.g., Tether’s reserve asset purchases impacting money markets).

**Methodologies:** To address the research question, ”How do macroeconomic, media, social, environmental, or regulatory factors interact with stablecoins?” researchers have employed a range of econometric and statistical methods, including GARCH, Granger causality, VAR, and regression models. For instance, Nguyen et al. \[95\] used GARCH and EGARCH models to analyze the impact of interest rates on stablecoin prices, selecting EGARCH to account for the asymmetric effects of interest rate increases and decreases. Similarly, Ante and Saggu \[5\] applied time-varying Granger causality to investigate the bidirectional relationship between Ethereum transaction fees and economic activity in stablecoins, highlighting the robustness of time-varying methods in capturing relationships that evolve with market conditions.

Bojaj et al. \[21\] utilized a Bayesian VAR model to forecast the macroeconomic effects of stablecoin shocks on the Montenegrin GDP. However, the lack of sufficient control variables

in their model suggests the possibility of confounding factors influencing both stablecoins and GDP.

Another group of authors, including de l’Etang \[38\] and Su et al. \[110\], adopted event study approaches, measuring abnormal price and trading volume changes surrounding media announcements or regulatory developments.

Predictive regression models have also been employed. For example, Clark et al. \[29\] regressed stablecoin returns on variables related to CO2 emissions and temperature anomalies.

Meanwhile, Ayadi et al. \[10\] used a Cross-Quantilogram model to analyze non-linear correlations between CBDCuncertainty and CBDC-attention indices<sup>4</sup> and changes in stablecoin prices and trading volumes across different quantiles.

**Research Gaps:** This category of research focuses on the comovement of stablecoins with other assets or factors. However, only one paper discusses the comovement of different stablecoins with each other \[111\]. This study is limited to five prominent stablecoins, using a relatively short sample period of 1.5 years, and relies solely on daily pricing data. In addition, the investigation does not consider non-linear relationships or regime changes. Future research should encompass a broader selection of stablecoins and use more sophisticated methodologies, possibly incorporating high-frequency data.

There also remains a debate regarding whether the correlation identified between stablecoins (particularly Tether) and cryptocurrencies (particularly Bitcoin) is a causative one. Griffin and Shams \[56\] argued, for instance, that there is a causal relationship as Tether issuances manipulate Bitcoin prices upwards, while other authors (e.g., Wei \[118\]) argued against this—we provide a more detailed analysis of the reasons behind these conflicting results in Section VI.

Only one paper studies the impact of interest rates on stablecoins \[95\]. This study is not conclusive. It studies a relatively short sample of one year, which is not enough given the infrequent and longer-term nature of interest-rate changes.

Moreover, the relationship between stablecoins and other unstudied factors is necessary. For example, there might be a significant relationship between activity on some DeFi platforms and stablecoins, such as Aave (a platform offering stablecoin lending), Curve Finance (a stablecoin trading decentralized exchange), and Yearn Finance (a platform that optimizes yield from stablecoins). There is also a lack of studies on the impact of announcements by stablecoin providers on their own stablecoins. The relationship between stablecoins and emerging markets, e.g., Brazil, Nigeria, Turkey, Indonesia, and India, also necessitates more attention since some stablecoins are heavily used in those countries \[108\].

Overall, 51 different stablecoins are studied in this area. The most studied stablecoins are USDT (52 papers), USDC (34 papers), DAI (20 papers), TUSD (16 papers), BUSD (14 papers), USDP (13 papers), GUSD (11 papers), and HUSD (5 papers). Despite the relatively high number of stablecoins analyzed in existing work, there exists a significant opportunity for conducting research on stablecoin projects that have

received limited to no attention from academia. This can give us insight into the stablecoins that have different characteristics from the ones considered in existing studies. One example of a different stablecoin, which has been neglected by academic investigations so far, is RAI. Unlike the majority of stablecoins that are pegged to a fixed price (usually one USD), RAI uses a Proportional-Integral-Derivative (PID) mechanism to dynamically adjust the peg value.

### *B. Stablecoin Stability Analysis*

### ***(3) How Stable Are Stablecoins In General Market Conditions?***

The findings from seven papers suggest that stablecoins, despite their intended stability, exhibit varying degrees of instability in general market conditions. Grobys et al. \[58\] highlighted that stablecoins display unpredictable volatility. Zhao et al. \[124\] found that there are scenarios where the stability mechanisms of stablecoins fail, causing volatility. Hoang and Baur \[67\] emphasized that stablecoins are relatively stable compared to Bitcoin but less so than fiat currencies, being influenced by Bitcoin’s volatility. Duan and Urquhart \[42\] revealed that many stablecoins deviate from their $1 peg, although some, like BUSD, correct these deviations more effectively than decentralized stablecoins like DAI. FernandezMejia \[47\] discussed how systemic risks make stablecoins experience volatility, but also noted stablecoins’ mean-reversion characteristics. Hairudin and Mohamad \[61\] reinforced this by demonstrating that stablecoins, especially USDT, exhibit mean reversion and lower volatility compared to cryptocurrencies like Bitcoin and Ethereum.

Overall, while stablecoins tend to be less volatile than other cryptocurrencies, they are far from perfectly stable, with their volatility influenced by market conditions, systemic risks, and design mechanisms. However, being more volatile than intended does not make them valueless; the fact that they have significantly lower volatility than non-stable cryptocurrencies makes them of practical value to the market.

*Insight 6:* Stablecoins exhibit significantly lower volatility compared to non-stable cryptocurrencies but are still not as stable as the fiat currencies they are pegged to. *Insight 7:* Some stablecoins are more stable than others. Generally, algorithmic stablecoins are less stable than collateralized ones.

**Methodologies:** To assess the stability of stablecoins in general market conditions, researchers used descriptive statistics, power law analysis, hypothesis testing, stationarity analysis, formal theoretical modeling, and wavelet analysis. Descriptive statistics, such as standard deviation, mean, and range, are commonly used; for a perfectly stable stablecoin, all these measures would equal zero. Power law analysis has been applied to model the returns of stablecoins, with a power law exponent below three indicating that extreme events contribute to persistent volatility \[58\]. It is important to note that the power law focuses on the tail behavior of distributions, modeling returns above a certain threshold. For instance, Grobys et al. \[58\] identified a volatility threshold of 0.175, above

which the power law signals instability—though this does not imply instability under normal conditions. Hoang and Baur \[67\] applied statistical hypothesis tests like the Chi-square test to determine whether the standard deviation of the stablecoin price series is significantly greater than zero. Additionally, Duan and Urquhart \[42\] tested for stationarity of stablecoin returns around zero, where a lack of stationarity would indicate regime changes and deviations from zero average returns.

Wavelet analysis, used in \[61\], allows researchers to assess the volatility of a time series across a range of frequencies or time scales. This is useful because a time series might be, for instance, not volatile over the long term but show volatility over short-term timescales, or vice versa.

Charoenwong et al. \[25\] used several computer science theories (undecidability and the Halting Problem) to analyze algorithmic mechanisms in stablecoin stability, transforming economic stability questions into computational abstractions.

Zhao et al. \[124\] developed a formal modeling framework utilizing six classes of timed automata to represent stablecoin expansion, contraction, traders, and exchanges. Using the Uppaal model checker, they simulated all possible state transitions of the system, uncovering scenarios where expansion or contraction mechanisms fail due to undesirable trader behaviors. Empirical validation of these theoretical findings with blockchain transaction data revealed that trader behaviors contributed to stability failures in stablecoins such as Basis Cash and Ampleforth.

### ***(4) How Stable Are Stablecoins During Periods Of Market Turbulence Or Crisis?***

During the COVID-19 pandemic, gold-backed stablecoins exhibited heightened volatility, with some surpassing Bitcoin in instability \[69\]. Unlike real gold, many gold-backed stablecoins failed to act as safe havens. Nevertheless, some gold-backed stablecoins performed better than others (e.g., PAX Gold). Other custodian-based USD-pegged stablecoins like Tether (USDT) and USD Coin (USDC) maintained low volatility and grew in market capitalization, while on-chain collateralized stablecoins like DAI experienced higher instability \[71\].

The Terra-Luna collapse caused volatility across multiple stablecoins, yet collateral-backed stablecoins experienced increased demand and maintained relative stability \[37\]. The Silicon Valley Bank crisis particularly impacted USDC due to its exposure to failed banks, but it quickly recovered, showcasing resilience \[60\]. The FTX collapse led to significant fluctuations in USDC and USDT, with both experiencing greater instability than Bitcoin and Ethereum \[60\]. These findings indicate that while stablecoins demonstrate some resilience, they are susceptible to unexpected volatility and external shocks during crises, with the impact varying based on the stablecoin’s characteristics and its relationship to the crisis.

*Insight 8:* Stablecoins, while generally more stable than nonstable cryptocurrencies, are not immune to volatility during market crises, with different crises impacting different stablecoins differently.

**Methodologies:** Methodologies similar to those employed in addressing the previous research question may also be applied here but with an adaptation to an event-study framework in order to examine volatility during specific events or crises. For instance, De Blasis et al. \[37\] measured abnormal returns during the UST collapse. Abnormal returns refer to the difference between realized and expected returns. Hairudin and Mohamad \[60\] used wavelet analysis during several crises, including the FTX collapse and the COVID pandemic. Jalan et al. \[69\] calculated realized variance (the square of the price changes) during the COVID-19 pandemic. In addition to the methodologies mentioned in the previous research question, the quantile-root test has been used in \[69\]. Quantile Unit Root tests are used to determine if a time series is stationary or not by examining the stationarity of different quantiles of its distribution. This is useful because extreme market conditions will fall in upper or lower quantiles.

**Research Gaps:** Studies on stablecoin stability focus on collateralized designs, such as USDT, USDC, and DAI, while the stability of purely algorithmic stablecoins remains understudied. Greater comparative analysis is needed to compare the stability of stablecoins with different characteristics (e.g., collateralized vs. algorithmic, varying collateral ratios, and varying algorithmic mechanisms) as highlighted in \[58, 71, 124\]. Furthermore, research should study the stability of stablecoins during crises not covered by current research, such as the 2018 Cryptocrash or the Celsius Network collapse. The COVID-19 crisis is studied only in \[69\] and using exclusively daily price data; utilizing higher frequency data can offer more insight into the sudden impacts of this crisis.

Moreover, none of the studies utilize blockchain transaction data. While price data is useful in measuring volatility, blockchain transaction data can offer insights into the behaviors that led to this volatility.

### *C. Price Modeling*

### ***(5) What Are The Properties of Stablecoins’ Prices In Terms Of Linearity, Time-Variation, Regime-Switching, Normality, And Autoregressive Behavior, etc.?***

Non-linearity and regime-switching are prominent characteristics of stablecoins’ price behavior. Maiti et al. \[88\] found that, unlike many volatile cryptocurrencies, USDT’s returns exhibit significant non-linearity, particularly during the COVID-19 pandemic. They also identified shifts between different market conditions, leading to the use of regimeswitching models like Threshold Autoregressive (TAR) and Smooth Transition Autoregressive (STAR) to capture these dynamics. Similarly, Pernice \[102\] analyzed 11 fully collateralized stablecoins and observed a dual-regime behavior: one where price stability is maintained through arbitrage and another during extreme market conditions with more dramatic corrections. Their findings provide evidence of trend-reversion, where prices return to expected values through arbitrage mechanisms, modeled using the Caginalp-Balenovic asset flow dynamics model \[23\].

In terms of long memory, Ahmed and Bouri \[1\] discovered that Tether, USD Coin, and Binance USD exhibit spurious long memory. This suggests that apparent long-range autocorrelations in the data are driven by structural breaks rather than genuine persistence in the time series.

Stablecoins also demonstrate heavy-tailed distributions, reflecting their susceptibility to extreme price movements. Levene \[82\] found that USDT, DAI, and USDC exhibit distributions with tails heavier than those of a Gaussian distribution, a common feature of financial time series influenced by extreme market conditions.

*Insight 9:* Stablecoin price time series demonstrate nonlinearity, regime-switching behavior, autoregressive patterns, spurious long-memory, and heavy-tailed distributions.

**Methodologies:** Researchers have employed a variety of methodologies to analyze stablecoin price behaviors. To detect non-linearity, Maiti et al. \[88\] and Ahmed and Bouri \[1\] used the Brock-Dechert-Scheinkman (BDS) and Lagrange Multiplier tests. Stationarity has been examined using the Augmented-Dickey-Fuller Test (ADF) \[88\], though ADF’s assumptions of linearity and absence of regime switches make it less suitable for stablecoins.

The presence of heavy-tailed distributions was analyzed by Levene \[82\] using Goodness-of-Fit tests, including the JensenShannon Divergence and Kolmogorov-Smirnov Two-Sample tests. Long-memory properties were investigated in \[1\] using a combination of Rescaled Range, Log Periodogram, Exact Local Whittle, and ARFIMA methods; this use of several methods is a good example of the required robustness.

A range of methodologies were used to identify regimeswitching and structural breaks. Maiti et al. \[88\] used Threshold and Smooth Transition Autoregressive models, while Pernice \[102\] employed fixed-effects panel regression and the Qu test. Ahmed and Bouri \[1\] utilized Bai and Perron Structural Break Tests.

Despite the methodological rigor, three of the four studies (\[88, 1, 82\]) relied solely on daily price data, which may obscure intraday volatility.

***(6) How Can Actors In Stablecoin Ecosystems Be Modeled Using Computational Simulations?*** Only two papers address this research question, both authored by the same researchers \[16, 17\]. These studies introduce an open-source simulation tool that models investor buy/sell behavior within the MakerDAO stablecoin ecosystem. This tool can be used to study how DAI prices are affected by various parameters related to investors, MakerDAO, and collateral (ETH).

**Methodologies:** The tool models investors as maintaining portfolios that include DAI, with decisions to buy, sell, mint, or burn DAI influenced by Markowitz’s Optimal Portfolio Theory. These decisions affect the price of DAI through changes in supply and demand. Key parameters impacting the optimal portfolio include the expected returns of USD, ETH, and DAI; the covariance matrix of these assets; investors’ risk tolerance; and MakerDAO’s interest rates, liquidation ratio, and transaction fees.

While the model offers insights into the mechanisms that stabilize the DAI stablecoin, it has some limitations. Firstly, the model is designed to analyze situations where one parameter is varied while others remain constant; in reality, parameters can vary together, creating a combined effect. Secondly, the model assumes a single-collateral DAI, which is outdated as the platform has transitioned to a multi-collateral system. Thirdly, the demand and supply of DAI can be impacted by factors not included in the model, such as competition with other stablecoins.

**Research Gaps:** Authors studying stablecoin price modeling highlight several avenues for future research. Maiti et al. \[88\] emphasized the need to identify the most effective nonlinear models, particularly during crises when stablecoin price processes are subject to shocks. Additionally, there is limited use of machine learning methods in stablecoin modeling, with only two papers \[121, 53\] exploring this approach, leaving ample room for experimentation.

Arbitrage opportunities in stablecoin markets also remain underexplored. Ba˘gcı et al. \[11\] demonstrated that a simple rule-based model was profitable, but this was the only study investigating arbitrage profits from trading stablecoins and did not include periods of market shocks. Future research could focus on developing more sophisticated trading algorithms and testing their performance under varying market conditions.

Another promising direction is comparing the effectiveness of different models for forecasting stablecoin prices. Future work could evaluate neural networks used in \[121\], regression models from \[40, 94\], and rule-based algorithms like the one in \[11\]. Developing a standardized benchmark for model comparison would also be valuable.

### V. TECHNICAL ANALYSIS

This section synthesizes stablecoin research within the technical analysis macro-category, which includes four subcategories: design and implementation of stablecoin systems, stabilization mechanisms, failure analysis, and security and privacy. Seven research questions are addressed under this category, and the results and methodologies of related studies are synthesized. Research gaps are analyzed collectively for each sub-category.

### *A. Design And Implementation*

### ***(7) How Can We Improve The Design And Implementation of Stablecoins?***

The main proposals for improving the design and implementation of stablecoins include the following: pegging a stablecoin to a basket of fiat currencies; using physical diamonds as collateral; adjusting the exchange rate to deter speculative attacks; developing novel stablecoins that combine a high-risk token with a low-risk stablecoin; modifying minting costs to influence supply; issuing bonds to regulate supply; designing a stablecoin tailored for radio spectrum trading; and relying on arbitrageurs and third-party investors to mitigate collateral risk.

Giudici et al. \[55\] proposed a stablecoin design that is not pegged to a single currency but to a basket of fiat currencies and demonstrates the increased stability of this approach. Asadov et al. \[8\] analyzed the history of several precious metals and found that a stablecoin backed by a combination of gold-silver (88:12 ratio) optimizes stability. Bandara et al. \[12\] introduced a system backed by redeemable physical diamonds, while Tsai et al. \[115\] suggested a stablecoin design where the collateral is held by custodian banks and certificates of ownership are traded on the blockchain.

Dong and Boutaba \[41\] introduced Elasticoin, a stablecoin system that uses Proofs of Sequential Work (PoSW) to reduce volatility by dynamically adjusting the minting cost. The system adjusts the computational effort required to mint in order to increase or decrease the supply of minted coins.

Routledge and Zetlin-Jones \[103\] proposed a stablecoin design that prevents speculative attacks. A speculative attack is when traders heavily sell a currency because they expect its value to fall, leading to a self-fulfilling prophecy. Their solution employs a dynamic exchange rate adjustment, temporarily lowering the peg to make attacks more costly. Using formal mathematical proofs, the authors demonstrate that this policy reduces the likelihood of speculative attacks. Unlike conventional approaches, which aim to push prices toward the peg, this method strategically moves the exchange rate away from it to stabilize the system.

Heinonen \[66\] proposed a stablecoin system with two wallets: Investment and Saving wallets. The Investment wallet absorbs more risk. If demand increases and the price of the stablecoin rises above the peg, the system increases the coin supply, distributing it proportionally to users’ Investment wallet balances. Conversely, if demand decreases, the system reduces supply by deducting from the Investment wallet balances. To address cases where users lack sufficient funds to absorb reductions, the authors introduce “antimoney”, a credit mechanism allowing negative balances, capped by the user’s Saving wallet balance.

Kazemian et al. \[72\] introduced FRAX, a stablecoin that transitions from full to partial collateralization as adoption grows. A secondary token, FXS, absorbs volatility during the partial collateralization phase. Users mint FRAX by depositing less than $1 in collateral and supplementing it with FXS. The percentage of collateral vs. FXS needed depends on a dynamic ratio. This ratio adjusts to maintain stability: if FRAX trades above the peg, the ratio is lowered, allowing more FRAX to be minted and vice versa. Moreover, as demand for FRAX grows, the need for FXS increases, raising its price and rewarding stablecoin holders.

Zahnentferner et al. \[122\] also proposed a system where a secondary token represents the collateral value in excess of $1. However, the system relies on excess reserves to mitigate against potential collateral price drops. Moreover, the authors propose that the system temporarily restricts stablecoin sales in extreme market scenarios, allowing time for collateral prices to recover.

Das and Venkataraman \[36\] proposed a fiat-pegged stable-

coin system collateralized with Ethereum (ETH). However, unlike the previous proposal in \[122\], collateral in excess of $1 is not provided by the stablecoin owners but by external investors. These investors assume the collateral’s volatility risk while benefiting from its potential appreciation and also earning a share of transaction fees. Upon redemption, collateral value in excess of $1 is returned to these investors. This concept closely resembles the red-black coin system proposed by Salehi et al. \[107\].

Zhang and Zhao \[123\] introduced SCoin, a stablecoin system for blockchain-based trading in the radio frequency spectrum. The Spectrum Resource Management Center (SRMC) issues SCoins and manages spectrum transactions through smart contracts. Spectrum Trading Service Providers (STSPs) obtain spectrum rights from SRMC to trade with users. Access nodes connect users via various infrastructures like satellites and mobile networks. A Delegated Proof of Stake mechanism validates transactions, considering both SCoin holdings and spectrum interference, discouraging abuse of the spectrum by large coin holders. After analyzing the previous stablecoin proposals, we noticed that some designs share significant similarities. For instance, both Tsai et al. \[115\] and Bandara et al. \[12\] proposed asset-backed stablecoins using redeemable physical collateral stored in custodian banks, differing primarily in the type of asset (fiat currency versus diamonds).

Moreover, several authors proposed a stablecoin that utilizes a secondary volatile token that represents residual collateral value \[72, 122, 36\]. However, they have some differences. For example, FRAX \[72\] is the only one that transitions to partial collateralization. And in \[36\], external investors provide the excess collateral. Both the proposals in \[72\] and \[122\] have been implemented and received notable market success.

Some of the proposals are also similar to stablecoins that have been previously implemented. For instance, the basketbacked stablecoin proposed in\[55\] is similar to the idea behind Libra (renamed Diem). Similarly, the dual-token mechanisms in \[122, 66, 72\] share features with MakerDAO’s DAI, though they introduce some uniqueness. Additionally, some papers (e.g., \[86\]) propose well-established mechanisms like arbitrage, open-market operations, and bond issuance.

**Methodologies:** This section employs different methodologies, including economic modeling, blockchain implementation, formal verification, and scenario analysis.

Stablecoins pegged to a basket of currencies rely on the comovements of the basket’s currencies for stability. Techniques like variable decomposition and vector autoregression (VAR) help analyze these comovements by assessing how changes in one currency affect others \[55\]. A basket with highly correlated currencies provides less diversification, reducing stability per Modern Portfolio Theory \[89\]. Researchers can optimize risk by factoring in each currency’s historical variance and their covariances. Quantifying risk can be done using measures such as variance or Value-at-Risk \[86\].

In the design of stablecoins, game theory is a useful tool, modeling the behavior of relevant actors and incentivizing them to behave in ways that serve stablecoin stability. For

example, game theory has been used to analyze speculative attacks with a system of traders and attackers \[103\]. Attackers can overwhelm the supply of stablecoins in a short period of time, destabilizing it. However, they show using gametheoretic modeling that their design would make it unprofitable for attackers to do so.

*Insight 10:* Game theory models related to stablecoins assume independent traders, ignoring herd behaviors. They also overlook other relevant phenomena such as the effects of deleveraging spirals or arbitrageurs.

The proposed implementation of stablecoins takes blockchain and smart contract design into consideration. Some researchers implemented innovative algorithmic stability rules using Ethereum smart contracts \[103, 36\]. Ethereum is the most popular platform, providing many heavily-tested tools, an active developer community, and wide integration with DeFi protocols. Zahnentferner et al. \[122\] used Cardano and Ergo to implement their stablecoin design. These platforms help formally verify the reliability of their implementations. Dong and Boutaba \[41\] utilized Ergo’s blockchain, which is suitable for implementing innovative consensus mechanisms. Bandara et al. \[12\] utilized a permissioned blockchain, allowing more centralized control.

To test the stability of the proposed stablecoins against different possible scenarios, synthetic data has been generated using techniques like Monte Carlo simulations \[86\]. Some researchers also utilized formal verification or mathematical proofs to illustrate the level of stability. For example, Zahnentferner et al. \[122\] used bounded model checking and interactive theorem proving with Isabelle (a higher-order logic theorem proof assistant) to demonstrate the stability of their design.

**Research Gaps:** There is significant potential for novel stablecoin proposals, including those based on flexible pegs (e.g., RAI<sup>5</sup> ) or baskets of assets, as highlighted in \[55\]. Privacy and security remain underexplored areas, particularly for stablecoins and CBDCs \[55, 93, 109\]. Assessing the security levels of different stablecoin designs is crucial, as is the development of rigorous formal verification methods and standardized security audits for stablecoins to reduce the risk of exploits. Furthermore, a framework is needed to understand the tradeoffs between security, privacy, transparency, efficiency, and regulatory oversight. In this regard, reconciling user privacy with AML/KYC compliance is an essential challenge. Proposals for privacy-preserving stablecoins could address this gap.

Additionally, more robust scenario analysis and stress testing are necessary to uncover potential failure points before they arise in practice. Developing a standardized testing framework would facilitate this. Stability assessments should also consider varying levels of adoption, as some designs, such as \[72\], argue that greater adoption enhances stability.

The lack of regulatory and industry standards compliance is a significant challenge for stablecoins, as highlighted in \[44\].

5https://reflexer.finance/

Developing proposals that align with these standards could enable broader adoption, particularly among institutions that require strict compliance.

Another future research avenue is related to CBDCs. CBDCs carry the promise of revolutionizing monetary policy through novel monetary policy tools such as programmable negative interest rates, expiration dates on money, and smart contract-based taxation. Research on the design and implementation of these tools could reveal new possibilities.

Moreover, most existing stablecoin proposals focus on full or partial collateralization. Fully algorithmic stablecoins, however, remain underexplored despite offering key advantages such as reduced reliance on trusted custodians and greater capital efficiency.

### *B. Stablecoin Mechanisms*

### ***(8) What Are The Characteristics Of Stabilization Mechanisms Used In Stablecoins?***

Fifteen papers analyze the stabilization mechanisms used in stablecoins. The simplest mechanism is full collateralization. Full collateralization means that users must deposit assets equal to or greater than the peg value with a custodian in order to receive stablecoins. Using cryptocurrency as collateral for fiat-pegged stablecoins introduces volatility risk. This risk can be mitigated by requiring over-collateralization. If the value of the cryptocurrency collateral falls below a certain threshold, the system liquidates the collateral to maintain the peg. The most popular stablecoin utilizing such a mechanism is DAI \[92, 75\].

Partially collateralized stablecoins reduce the reserve ratio, holding, for example, $0.70 for every $1 issued. This lower collateralization allows issuers to invest the remaining funds in more volatile assets, offering potential rewards but introducing additional risk. Under-collateralized and non-collateralized stablecoin systems rely on algorithmic mechanisms to ensure stability.

Algorithmic stability mechanisms noted in the reviewed papers include seigniorage shares, increasing supply by issuing coins, supply rebase, dynamic transaction fees, dynamic lending rates, dynamic mining rewards, automated market operations, issuing bonds, dynamic collateral ratios, and preventing users from selling for a limited period of time \[91, 101, 50, 80\].

One prominent algorithmic mechanism is the use of seigniorage shares. In this context, seigniorage refers to issuing secondary tokens related to the stablecoin to absorb volatility \[92, 107\]. For example, in the red-black model \[107\], users deposit volatile cryptocurrencies and receive stablecoins and “red” tokens. The red tokens represent the excess value of the collateral. If the price of the collateral increases, red token holders benefit from amplified returns. The red tokens represent the excess value of the collateral. To illustrate, assume the ETH collateral deposited is worth $1.50; the user gets $1.00 worth of stablecoins and $0.50 worth of red tokens. If the price of ETH increases by 10%, then the collateral deposited would be worth $1.65. The value of the stablecoin

remains $1.00, while the red coin becomes worth $0.65 (an increase of 30%). If the collateral price decreases significantly, the owners of red coins can lose all their investment, while the stablecoin owner will be forced to liquidate the collateral, losing nothing in the process. Secondary tokens can grant their holders a share in the profit of the stablecoin system and/or voting power.

Another algorithmic mechanism is supply rebase, which refers to a mechanism where stablecoins are burnt automatically to decrease supply and increase the price \[101, 92\]. Stablecoins can be burnt from all or a subset of users, depending on the specific stablecoin system.

Fees can also be automatically adjusted to impact supply and demand. For example, increasing transaction fees can discourage transfers, reducing demand. Other fee types include minting fees, withdrawal fees, and borrowing-related fees, all of which can influence supply and demand \[91\]. For instance, decreasing the fees associated with borrowing (e.g., loanorigination fees) can increase demand for the stablecoin and raise prices. At the protocol layer, systems can dynamically adjust mining costs. Increasing mining costs reduces the incentive to mine new stablecoins, thereby limiting supply \[91\].

Automated market operations (AMO) refers to the buying or selling of assets on the market to influence the price of the stablecoin \[91, 101\]. For instance, the issuer can use its reserves to buy the stablecoin, pushing up its price. This can be done automatically with smart contracts.

Another used mechanism to stabilize algorithmic stablecoins is the issuance of bonds. If the price falls below the peg, the issuer can reduce the supply of stablecoins by issuing bonds that users can purchase using stablecoins \[92\]. These bonds promise future payment after the crisis subsides. This is analogous to how traditional central banks issue bonds to reduce money supply.

For partially collateralized stablecoins, the system can algorithmically change the required collateral to impact stablecoin supply \[92\]. Decreasing the required collateral would increase supply, as more stablecoins can be minted for the same amount of collateral provided by users.

These algorithmic mechanisms, however, are not without their risks. Studies highlight that algorithmic stablecoins often exhibit higher volatility compared to collateralized designs \[70\]. Charoenwong et al. \[25\] demonstrated theoretically that guaranteeing the stability of purely algorithmic stablecoins is not possible; this finding seems to go against other papers that show confidence in algorithmic stabilization mechanisms, including \[41\]. Despite these challenges, algorithmic stablecoins are not without value, as a currency can still be useful even without absolute and guaranteed stability. Moreover, the majority of stablecoin proposals are not fully algorithmic. In this regard, Heinonen \[66\] claimed to formally verify the stability of a partially collateralized system that integrates algorithmic mechanisms.

*Insight 11:* Stablecoins that are not fully collateralized use algorithmic mechanisms to control supply and demand.

*Insight 12:* Despite their higher empirical instability and the theoretical impossibility of guaranteed stability, algorithmic stablecoins offer value through greater capital efficiency and the absence of a need for a trusted centralized custodian.

**Methodologies:** The most common methodology used to examine stablecoins’ stabilization mechanisms is to analyze stablecoin-related material (white papers and official documentation, project websites, blogs, etc.) \[101, 92, 30, 84\]. For example, Pernice et al. \[101\] “surveyed white papers, websites, and, when available, price data of 24 stablecoin projects”, classifying each stablecoin based on its type of collateralization, its exchange rate regime, and its use of various stabilization techniques. Clark et al. \[30\] analyzed 185 articles from CoinDesk<sup>6</sup> , finding information about 25 stablecoins. Based on this information, they classified each stablecoin into one of five stability mechanisms.

Other papers examine stabilization mechanisms through empirical analysis. For instance, Lyons and Viswanath-Natraj \[87\] examined arbitrage activity using blockchain transactions where users mint USDT from Tether treasury and sell it for profit in secondary markets, bringing the price of USDT down to the mint cost. Similarly, Kj¨aer et al. \[75\] empirically studied the stabilization mechanisms of the stablecoin system MakerDAO. MakerDAO issues the stablecoin DAI and accepts ETH as collateral. If the price of ETH drops below the collateralization ratio, a liquidation function is automatically called. This function offers the ETH collateral for auction to repay the DAI to the system. These stabilization mechanisms are enforced through contract calls on the Ethereum blockchain. Kj¨aer et al. \[75\] analyzed these contract calls and the movement of funds between contracts to assess collateralization ratios, liquidation events, and auction effectiveness.

**Research Gaps:** Improving stability mechanisms in stablecoins remains a key area of ongoing research. Researchers have proposed interesting ideas to be studied further such as incorporating algorithmic adjustments to the structure of stablecoins \[92\].For example, this could include analyzing how stability algorithms perform under different market conditions and developing algorithms that automatically change the mechanisms based on current conditions \[92\].

Another critical research area is understanding the effects of different stability mechanisms (e.g., algorithmic vs. custodianbased) and governance structures, such as different voting protocols (e.g., token-weighted or quadratic voting) on the success, stability, efficiency, and equity of stablecoin ecosystems. This research question can be addressed by comparing different ecosystems, as suggested in \[125\], or the same ecosystems before and after structural changes. It can also be addressed through theoretical modeling and conceptual analysis, potentially drawing analogies from traditional monetary policy.

Charoenwong et al. \[25\] formally demonstrated that purely algorithmic stablecoins cannot achieve provable stability. Building on this, future research could focus on hybrid

6https://coindesk.com/

stablecoins that combine algorithmic mechanisms with collateralization, such as DAI and FRAX, which represent a significant portion of the stablecoin market. Additionally, scenario analysis and stress testing of stability mechanisms are critical for identifying vulnerabilities and ensuring resilience, as emphasized in \[75\].

### *C. Failure Analysis*

***(9) What Are The Causes Of Previous Stablecoin Failures?***

Four papers discuss the factors that lead to stablecoin failure. Two of them analyze the failure of Terra \[22, 28\]. At its peak, UST (Terra’s algorithmic stablecoin) had a market capitalization of approximately $18 billion, while LUNA (Terra’s native token) had a market capitalization of over $40 billion. UST maintained its peg to the dollar by offering arbitrage opportunities between LUNA and UST. Terra allowed users to burn $1 worth of LUNA to mint 1 UST. In this sense, UST was backed by LUNA. Users’ trust, speculative investment, high staking rewards, and the large amounts of money backing the Terra platform are all factors that gave LUNA market value. Terra could keep issuing more UST as long as the value of LUNA grew. However, this system was fragile, as a large enough fall in LUNA’s market value would mean that there is not enough LUNA to back the $1 value of all issued UST. It is reported that attackers (with short positions) accumulated a significant amount of UST and suddenly dumped this large amount into a Curve-3pool \[22\]. This caused downward pressure on the price, causing a rapid de-pegging of UST. The Terra’s protocol began minting more LUNA in an attempt to restore the peg. However, this was a mismanaged policy as it caused hyperinflation of LUNA, leading to further rapid declines. As users had less confidence, selling demand increased. There were not enough assets to back the value of UST. This case highlights the vulnerability of algorithmic stablecoins to extreme market events.

Drawing parallels with the case of UST, Saengchote and Samphantharak \[105\] analyzed the fall of the Iron Finance algorithmic stablecoin. IRON was backed by a combination of USDC and TITAN (the ecosystem’s native token). When large TITAN holders began selling their tokens, the price declined. Saengchote and Samphantharak \[105\] detected multiple bubble-like patterns in IRON before the collapse. The author argues that algorithmic stablecoins relying on secondary tokens with no collateral are inherently prone to such bubbles, making them vulnerable to collapse when these bubbles subside. Saengchote and Samphantharak \[105\] also showed that sophisticated users (large addresses, experienced participants, and those minting rather than buying) exited faster and more profitably.

Further theoretical insights into stablecoin failures are provided by Klages-Mundt and Minca \[76\], who developed a model of deleveraging spirals. Deleveraging spirals happen when stablecoin collateral drops significantly, triggering automatic liquidations of the collateral to prevent undercollateralization. This increases the supply of the collateral in the market, which puts downward pressure on the price

of this collateral, causing more liquidations. This concept of deleveraging spirals can also be seen in traditional economics. The 2008 Financial Crisis, where the decline in mortgagebacked securities led to margin calls and massive sales, is a classic example.

*Insight 13:* Deleveraging spirals, coordinated selling attacks, and redemption runs (analogous to traditional bank runs) are possible causes of stablecoin failures.

**Methodologies:** All of the four papers use a case-study methodology to understand the causes of specific failure cases. Briola et al. \[22\] used a network model with cryptocurrencies as nodes and correlations in their price movements as edges. Network metrics such as centrality measures showed that Bitcoin played a role in the collapse of TerraLuna. Similarly, Saengchote and Samphantharak \[105\] examined blockchain transactions on the Polygon network to study the downfall of Iron Finance. This analysis incorporated data on token minting, redemptions, and swap pool withdrawals. Using the Generalized Supremum Augmented Dickey-Fuller (GSADF) test, the authors identified bubble-like price patterns, while regression models revealed factors driving user behavior during the collapse. In another study, Cho \[28\] employed Granger causality tests to see if the value of UST obtainable by swapping it for LUNA influenced the market price of UST, suggesting that under-compensation of UST drove down the market price. Finally, Klages-Mundt and Minca \[76\] developed a theoretical stochastic model to demonstrate how leverage and liquidations can trigger stablecoin failures through deleveraging spirals. The model includes collateral value, stablecoin supply, collateralization ratio, and stablecoin price as main parameters. The model shows that negative shocks to collateral value trigger liquidations, pushing the price of the stablecoin to infinity. The model used in \[76\] has a key limitation that contributes to this seemingly impractical result. Mainly, the authors ignore the role of arbitrage mechanisms, where arbitrageurs mint new coins (increasing supply) and then sell them in the secondary market for a profit, bringing the price down.

### ***(10) What Are The Impacts Of Previous Stablecoin Failures?***

Two papers focus their analysis on the impacts of the failure of stablecoins (particularly TerraUSD or UST) \[74, 81\]. They found that the collapse of TerraUSD (UST) directly caused significant financial losses, harmed several DeFi protocols, spread financial damage across blockchains, and reduced investor confidence in algorithmic stablecoins.

One paper states that the failure of this stablecoin caused the destruction of over $30 billion in value in just a week \[74\]. The failure affected multiple other DeFi protocols that were involved with UST. For instance, many liquidity pools on decentralized exchanges like UniSwap and Curve used UST as a primary asset. When UST collapsed, the value of these pools collapsed. Lending protocols like Aave or Compound allowed users to borrow or lend UST \[74\]. The failure of UST did not only affect the Terra blockchain but also other blockchains that it was bridged to \[74\]. Moreover, the collapse of UST also

caused a crisis of confidence in the entire DeFi ecosystem, as investors lost trust in algorithmic stablecoins. All these impacts demonstrate the systemic risk of DeFi protocols.

**Methodologies:** Kitzler et al. \[74\] used network analysis with nodes representing Ethereum smart contracts or DeFi protocols and edges transactions between these nodes. Using network properties like degree distribution and centrality measures, the authors show the level of interconnectedness of the DeFi ecosystem and how the failure of UST affects the network.

Lee et al. \[81\] used the Diebold-Yilmaz (DY) Spillover Framework to study how the crash of Terra-LUNA spilled over to other cryptocurrencies. An extension of the Vector Autoregression (VAR) model, the DY framework has some advantages, including being order-invariant and being able to capture time-varying relationships. The DY framework also more clearly quantifies the overall interdependence in the system. Additionally, the authors used Effective Transfer Entropy (ETE) in a methodology designed to capture information flow between cryptocurrency price time series. Unlike the DY framework, ETE does not assume linearity, is more robust to nonstationarity, and can identify causal relationships.

**Research Gaps:** Future research ideas proposed by the reviewed papers include analyzing more spillovers related to stablecoin failures \[81, 74\], proposing policies or methods to mitigate the risk of failures \[28\], analyzing user behavior during DeFi failures using blockchain transaction data \[105, 76\], and developing better models that can help predict failures \[48\].

Klages-Mundt and Minca \[76\] have identified deleveraging spirals as a powerful dynamic behind stablecoin collapse. This insight raises an important research question: how can deleveraging spirals in stablecoins be prevented? None of the reviewed papers answer this question.

Moreover, the majority of papers studying stablecoin failures focused on the TerraLuna case, leaving a need to study other cases of stablecoin failures (e.g., Basis Cash, NuBits, Iron Finance, BeanStalk, Deus Finance, flexUSD, Acala USD).

### *D. Security And Privacy*

### ***(11) What Are The Privacy Concerns Related To CBDCs And How Are They Being Addressed?***

Only one paper focuses on the privacy of stablecoins. Tronnier \[113\] analyzed how 78 different central banks address privacy in their CBDC-related publications and pilot projects, uncovering several valuable findings.

The analysis revealed that most central banks either do not address privacy or discuss it only superficially. However, some central banks prioritize privacy more extensively, with the most notable being the Bank of Canada, the Bank of Italy, the European Central Bank (ECB), and the Monetary Authority of Singapore. Other central banks, such as those of France, Thailand, and Denmark, also engage in more detailed discussions on privacy.

A common challenge highlighted is the trade-off between central bank oversight and user privacy. For example, Know-

Your-Customer (KYC) procedures, required by central banks for regulatory compliance, inherently reduce privacy.

To address such concerns, central banks proposed various privacy-enhancing mechanisms. Specific to Europe, the General Data Protection Regulation (GDPR) defines transaction data as personal data and restricts its processing. Central banks, including the Norges Bank (Norway), argue that GDPR compliance must be integrated into CBDC design, significantly enhancing transaction privacy. Other proposed measures include ensuring that user identity data is not published on the blockchain and offering users cryptographically signed IDs.

Several central banks propose mechanisms for anonymous payments. For example, the European Central Bank (ECB) suggests using anonymity vouchers, which can be purchased from third-party intermediaries to enable small anonymous CBDC transactions. Privacy-enhancing technologies such as zero-knowledge proofs and differential privacy, highlighted by the Bank of Canada, offer additional tools to safeguard user privacy. Other techniques, such as zero-knowledge proofs and differential privacy, both highlighted by the Bank of Canada, offer additional tools to protect user privacy. To prevent longterm tracking of users’ transactions, rotating public keys is mentioned as a technique to increase anonymity.

The Dutch Central Bank proposes separating transaction data from user balance data, limiting access to intermediaries. The ECB pilot project discusses chain snipping as a method to reset transaction history, preventing the creation of longterm knowledge graphs of users’ payment activity. Additional privacy-enhancing methods, including multi-party computation, enclave computing, and permissioned distributed ledger technology, are also mentioned by several central banks.

**Methodologies:** The methodology of Tronnier \[113\] conducted a systematic literature review of CBDC-related publications by 78 central banks. The study systematically searched each central bank’s website for relevant documents and supplemented this with Google searches using keywords such as ”CBDC,” ”Central Bank Digital Currency,” and the name or country of the central bank. Only complete, Englishlanguage publications that directly addressed CBDCs and privacy considerations were included in the analysis. The authors categorized central banks based on how extensively they covered privacy, focusing exclusively on retail CBDCs while excluding wholesale CBDCs intended for interbank settlements.

### ***(12) What Are The Security Threats Related To CBDCs And Stablecoins?***

Only two papers focus on security threats related to CBDCs or stablecoins.

Hans et al. \[63\] identified 39 CBDC security threats using the STRIDE modeling framework. Among these, more threats were related to Spoofing (7), Tampering (10), and Information Disclosure (12), while fewer were associated with Denial of Service (4), Repudiation (2), and Elevation of Privilege (4).

Many threats identified were general cybersecurity threats, not specific to CBDCs or distributed ledger technology (DLT). These include attackers impersonating legitimate users in cus-

tomer support interactions, introducing backdoors by tampering with hardware during chip manufacturing and deploying Trojan malware or SQL injections. Other general examples are supply chain attacks, SMS interception, network eavesdropping, server flooding to disable access, manipulating access policies for privilege escalation, and exploiting vulnerabilities in user interfaces to gain admin access.

However, several threats were specific to CBDCs and DLT. These include attackers masquerading as legitimate nodes using compromised certificates, exploiting cryptographic vulnerabilities (e.g., collision attacks), falsifying transaction records within the ledger, and targeting intermediaries like miners, financial institutions, and oracles. Additionally, sending false transactions to overwhelm the consensus mechanism poses a unique threat to DLT-based systems.

Mell et al. \[90\] highlighted additional security threats associated with Central Bank Digital Currencies (CBDCs). These include the unauthorized creation of stablecoins caused by software defects and the theft of on-chain collateral due to vulnerabilities in smart contract code. Other risks involve malicious updates to smart contracts. Furthermore, attackers gaining control of a majority of mining hardware or staked funds can exploit the system.

**Methodologies:** Hans et al. \[63\] employed threat modeling using the STRIDE methodology after creating an abstract high-level architecture of a CBDC. STRIDE classifies threats into six categories: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege \[73\]. The abstracted system includes key entities (e.g., central banks, financial institutions, and end-users) and their interactions. Specific use cases for this abstract CBDC were developed, illustrating workflows for transactions and access controls. Sequence diagrams illustrate the interactions among entities in both permissioned and permissionless blockchain environments, as well as in account-based and token-based access scenarios. Threats were identified by analyzing the abstracted system architecture and the modeled use cases.

In contrast, Mell et al. \[90\] consulted a range of research papers and reports from reputable sources, such as the Federal Reserve System and the U.S. Treasury, to identify security threats. However, the specific methodology they used for this process is not explained.

### ***(13) How Can Market Manipulation Related To Stablecoins Be Detected?***

One paper focuses on detecting market manipulation related to stablecoins. Zhu et al. \[126\] introduced an efficient method for detecting market manipulators in blockchain-based networks, including stablecoins. The method detects traders who played roles in destabilizing the Terra stablecoin.

**Methodologies:** The market manipulation detection method presented in \[126\] centers on identifying nodes in the network that have a significant but short-lived influence, with the argument being that such nodes are more likely to be manipulators. The authors rank nodes using a scoring method called Node Frequency-Inverse Appearance Frequency (NF-IAF). This method is inspired by Term Frequency-Inverse Document

Frequency (TF-IDF), a widely used metric in information retrieval. NF measures how frequently a node participates in a specific motif relative to all nodes participating in that motif. IAF quantifies how rare a node’s participation in a motif is across all days; rare appearances are more significant. Motifs, in this context, are recurring patterns of interaction between three nodes in the network. Only 5 of the 16 possible three-node motif patterns are included in the analysis. These include motifs where a central node receives/sends transactions from/to two other nodes and the wash-trading or moneylaundering motif with a circular trading pattern (A to B to C to A).

**Research Gaps:** Research on the security and privacy of stablecoins and CBDCs is surprisingly limited, with only four relevant papers identified in our literature search. This is despite the security and privacy of stablecoins and CBDCs being a significant issue for many reasons, including their impacts on user trust, protection against hacks and manipulation, ethical considerations, and regulatory compliance. This gap presents significant opportunities for future research.

Potential areas of investigation include analyzing methods to enhance privacy in stablecoins and CBDCs, measuring user demand for privacy, assessing the trade-offs between privacy and factors such as efficiency, transparency, scalability, and regulatory control, and designing and implementing privacyfocused stablecoins. In this regard, the only contribution is \[113\]. This study analyzes publications by central banks to examine their discussions about privacy. Although interesting, this work excluded any non-English publication, which should be considered in future research, neglecting the position of non-English-speaking countries regarding end-user privacy in CBDCs.

Security breaches can result not only in the possible loss of money but also in the destabilization of entire economies, particularly in the case of CBDCs. Stablecoins are interconnected with the entire DeFi ecosystem and potentially with traditional finance, increasing the systemic risk of security breaches. Hans et al. \[63\] identified many security threats using the STRIDE methodology. Other researchers can use different methodologies, such as attack tree analysis or analysis of stablecoin smart contract code. Moreover, Hans et al. \[63\] performed the analysis on a general abstraction of stablecoins. Future research can analyze actual projects and provide a comparative analysis of their security. This can help investors be aware of which stablecoins are more or less secure. The usage of AI for both attacking and defending stablecoin security is also a promising area of research.

### VI. DISCUSSION

In this section, we first discuss the research trends within the two macro-categories considered in this study, highlighting the areas that have been extensively investigated and identifying research questions that remain under-explored. Next, we address additional research gaps observed during our analysis, including research questions with conflicting results from

different contributions. Finally, we discuss the various data types and sources commonly used in this research domain.

### *A. Research Trends*

Some research questions have received significantly more attention than others, as shown by Table II. Fundamental topics, such as the extent of stablecoins’ stability and the mechanisms that make them stable, naturally attract greater focus. Additionally, certain research questions are easier to address, as they require less specialized knowledge, rely on more accessible data, or involve less time-consuming methodologies. For example, the research question related to the correlation between stablecoin prices and the prices of other assets is the focus of more than 30% of the papers in our SoK. This question can be addressed using price data, which is easily accessible through data aggregators or exchanges. While daily price data from sources like CoinMarketCap is widely used due to its accessibility, it is often less valuable than higher-granularity price data (e.g., minute-by-minute) that is usually not available on public datasets and must be selfcollected by researchers. This issue is discussed in more detail in Subsection VI-C.

In contrast, other research questions have received attention from only a few papers or, in some cases, just one, highlighting the potential existence of research gaps in these areas. For example, only two papers analyze security concerns related to stablecoins, and they do so in a broad and conceptual manner without analyzing specific stablecoins. Only one paper focuses on privacy issues, specifically discussing how central banks address privacy in their publications \[113\]. This paper adequately addresses the research question regarding the importance central banks assign to privacy in CBDCs. It does so by systematically analyzing documents from 78 central banks and categorizing them based on the emphasis they place on privacy in CBDCs. However, several other research questions related to privacy in stablecoins remain unexplored. These include the implementation of privacy-preserving mechanisms in stablecoins and the current levels of privacy in the existing stablecoins.

Furthermore, only four papers investigate the causes and impacts of stablecoin failures, and they focus exclusively on two cases: TerraLuna and IRON \[22, 77, 105, 28\]. By analyzing blockchain transaction data, they identify underlying causes, including liquidity pool attacks, misaligned incentives (a flawed stablecoin redemption mechanism), and deleveraging spirals. They also quantify the impacts of the failures to the magnitude of tens of billions of USD. Numerous other stablecoin failures have been documented in the grey literature but remain understudied, including Basis Cash, NuBits, Iron Finance, BeanStalk, Deus Finance, flexUSD, and Acala USD. Different projects use distinct designs; their analysis can reveal novel common failure risk factors for stablecoins. For example, many sources in the grey literature reported that several stablecoins have failed due to smart-contract exploits \[85\], governance manipulation using flash loans \[68\], and regulatory constraints \[35\]. Studying more cases also strengthens the

generalizability of stablecoin failure reasons. It also sheds light on the mechanisms that failed to prevent failure.

A few papers discuss market manipulation related to stablecoins. The techniques and attacks studied focus on one of two mechanisms. The first is minting unbacked stablecoins to inflate the prices of other cryptocurrencies \[56\]. The second is related to speculative attacks where attackers accumulate large amounts of stablecoin and suddenly sell them in an attempt to de-peg the stablecoin and benefit from short positions \[103, 22, 105\]. Building a taxonomy of manipulation techniques relevant to stablecoins and records of previous manipulation cases, along with their impacts, can be a promising future research direction. Investigating how to mitigate the risk of manipulation is also an active area of research.

### *B. Other Research Gaps and Conflicting Results*

Several research gaps persist also within the research questions that received greater attention. For example, out of the 37 papers studying the relationship of markets of different assets, only one paper analyzes the relationship of the stablecoins with respect to each other. Moreover, the stability of some important stablecoins has not been examined, with the majority of papers focusing on USDT, USDC, and DAI only. The second research question includes papers studying the impact of different environmental factors on stablecoin markets. However, some factors are understudied (e.g., interest rates, news announcements, and regulatory factors), and some potentially impactful aspects are not studied at all (e.g., activity on different DeFi platforms, emerging market activity, and announcements of stablecoin issuers).

There are also research questions with conflicting results, possibly requiring more robust research to settle the debates. One example is related to the relationship between the prices of stablecoins and the value of Bitcoin. For instance, Hatem et al. \[64\] and Chen and Chang \[27\] reached opposing results regarding the impact of Bitcoin price movements on stablecoins’. The likely explanation for this conflict lies in the sensitivity of the econometric methods used in these studies to factors such as model specifications, data granularity, and sample periods.

There is also a conflict regarding whether stablecoin issuance is used to manipulate other cryptocurrencies. Griffin and Shams \[56\], for example, argued that Tether issuances were used to inflate Bitcoin prices, while Wei \[118\] found no evidence of such manipulation. Griffin and Shams \[56\] used clustering and regression models on highly granular intraday transaction-level blockchain data, while Wei \[118\] used Granger Causality and VAR models on daily price data. When evaluating both papers, \[56\] appeared to have a stronger methodology for addressing the topic of Tether manipulation of Bitcoin prices. This is because Griffin and Shams \[56\] used more granular data, allowing the precise timing of the impacts of Tether minting transactions on Bitcoin prices and trading volume. In general, markets react very quickly to new substantial information, and the daily granularity used in \[118\] can mask these quick reactions. Griffin and Shams \[56\] did

not just examine the correlation of prices but used on-chain data to trace Tether flows through particular exchanges and identified the specific accounts using the minted Tether to prop up Bitcoin prices and trading volumes. This allowed them to offer a multifaceted analysis that approaches the problem from different angles and supports conclusions with a more robust methodological framework.

Another area of conflict relates to the stability of algorithmic stablecoins. While several papers propose various algorithmic stablecoin designs (e.g., \[41, 66\]), their theoretical instability \[25\] and empirical volatility have been highlighted \[70\]. This conflict arises, in part, from the theoretical impossibility of guaranteeing absolute stability \[25\], contrasted with the practical efforts to achieve relative stability through algorithmic mechanisms. However, such theoretical limitations do not entirely rule out the possibility of achieving practical, albeit imperfect, stabilization. Furthermore, the stability of algorithmic stablecoins can vary across different designs. The theoretical instability of stablecoins has been demonstrated in a single paper \[25\], focusing solely on a purely algorithmic design.

There is also mixed evidence on the stability of stablecoins during crises. Different authors achieved different results depending on the specific stablecoins and the particular crises studied. In some crises, some investors may prefer traditional (supposedly) safer assets like government-backed securities over stablecoins, leading to outflows from the stablecoin market \[96\]. This was evident during the SVB banking crisis, as stablecoins held a significant amount of reserves with failed banks. The FTX exchange crisis, on the other hand, prompted investors to seek refuge in stablecoins \[52\]. Different stablecoins are also impacted differently during the same crisis. For instance, during the Silicon Valley Bank crisis<sup>7</sup> , the stablecoins USDC, DAI, and TrueUSD dropped significantly below the peg, while USDT and BUSD maintained relative stability \[51\]. These findings demonstrate that the behavior of stablecoins during crises cannot be generalized, as it varies significantly between different stablecoins and across different crisis events.

As a side note, a significant portion of the papers analyzed in this study address central bank digital currencies (CBDCs). Although CBDCs are not confined to being stablecoins, those examined in our analysis exhibit a focus on stability. This emphasis on stability aligns with the economic objectives of central banks, who aim to keep their currencies a stable store of value and medium of exchange, reducing uncertainty.

*C. Data Types*

This section highlights and discusses the data sources researchers have relied on for stablecoin-related research. By categorizing and analyzing these data sources, we aim to provide guidance for future research.

 
- **Cryptocurrency Market Data:** This is the most common data type used by the reviewed papers. Market data

mainly involves price, but it can also refer to other information, including volume and market capitalization. This type of data is easily accessible from cryptocurrency market data aggregators, such as CoinGecko \[32\], and CoinMarketCap \[34\], which provide a reliable snapshot of the cryptocurrency market at any given moment by collecting data from numerous exchanges, applying volumeweighted averages, and performing data quality checks. Cryptocurrency exchanges, such as Binance \[18\] and Coinbase \[31\], also offer different types of market data. However, the resulting snapshot would be limited to that platform, while aggregators can collect and process data from multiple exchanges to present a broader picture of the market.

Market data has been widely used in various areas of research. For example, many studies rely on price data to explore the relationships between stablecoins and other assets \[57, 27, 79\]. Other studies use volume data to assess the impact of external factors, such as media announcements, on stablecoin market activity \[6, 106\]. *Insight 14:* The granularity of the data is crucial. Daily snapshots miss the volatility that can potentially shake stablecoins and trigger market chaos.

 
- **Blockchain Data:** Blockchain data includes all the information stored on-chain, i.e., permanently added in the cryptocurrency ledger, such as transactions, smart contracts, etc. On-chain data allows researchers to analyze the transaction network of cryptocurrencies, enabling investigations like new issuances and transfer of digital coins between users.

For example, Griffin and Shams \[56\] analyzed blockchain transactions and found that stablecoin issuances impact the Bitcoin market. Many researchers also focus on stablecoin transactions during market collapses \[74, 22, 105\]. In particular, Zhu et al. \[126\] detected manipulation patterns within stablecoin transaction data. Blockchain data can be collected by deploying a full node of the cryptocurrency network, which downloads the ledger from the peer-to-peer network. However, this process is time-consuming and requires specialized knowledge of the cryptocurrency network. As a result, many researchers turn to more accessible sources, such as blockchain explorers (e.g., Etherscan \[45\], Omni Explorer \[97\], and Tronscan \[114\]), specialized data platforms (e.g., Dune Analytics \[43\], The Graph Protocol \[112\]), and publicly available datasets (e.g., Ethereum ETL \[20\], Chartalist repository \[26\]).

Despite their accessibility, these sources have some limitations. Researchers must place trust in blockchain explorers or other third parties to accurately extract data from the blockchain ledgers. In this regard, some researchers have pointed out inaccuracies in data from blockchain explorers \[24, 65\].

 
- **Traditional Financial Data:** This type of data is used to study the relationship between traditional financial assets and stablecoin markets. Traditional financial data used in

the considered papers includes market data of traditional assets (e.g., stocks \[116\] and commodities \[15\]) and macroeconomic indicators (e.g., interest rates \[95\] and GDP \[21\]).

 
- **Synthetic Data:** Synthetic data has primarily been used to simulate market conditions and evaluate the performance of proposed stablecoin designs. For example, Monte Carlo simulations have been utilized by various authors for these purposes \[94, 86\].

- **Stablecoin Documentation:** This includes white papers, technical reports, and official documentation released by stablecoin projects. These documentations serve as a source of information for understanding the design and mechanisms of stablecoin projects. For example, several papers included a survey of such documents to categorize stablecoins based on their mechanisms \[91, 101, 92, 76\].

- **Social Media:** Some of the reviewed papers use Twitter posts to gauge market sentiment and its relationship to stablecoin markets \[3, 106\]. Note that this approach is sensitive to both the subset of posts analyzed and the methodology used for sentiment classification.

- **News Articles:** Used in several papers \[10, 38, 98\], news articles can be analyzed using natural language processing tools to assess their impacts on stablecoin markets. Sentiment analysis of news articles has led to the development of indices, such as the CBDC Uncertainty and CBDC Attention indices \[117\], which can be directly utilized by researchers.

### VII. CONCLUSION

As the adoption of stablecoins grows and interest by consumers and institutions builds up, research related to stablecoins becomes more valuable. However, the wide range of research directions, the multitude of research questions, and the diverse methodological approaches—often producing contrasting results—make it challenging to derive a comprehensive understanding of state-of-the-art stablecoin technologies from the existing literature.

To fill this gap, in this SoK, we systematically analyzed existing work addressing the technological and economic aspects of stablecoins. In particular, we identified key research questions from a comprehensive body of literature, synthesizing and analyzing the diverse findings. A wide variety of methodologies and data sources are identified and critically examined. Methodologies range from econometric analysis to machine learning models and system designs. Data sources are also varied, including data from exchanges, blockchain explorers, and news articles. Considerations for methodologies and data sources are mentioned in this paper, including the importance of including exogenous crises when assessing stablecoin stability and the importance of using models that take into consideration documented characteristics of stablecoin prices (e.g., non-linearity and their heavy-tailed nature).

Our analysis also reveals considerable gaps in the literature, such as limited research on the security and privacy of stablecoins, under-explored stablecoins, and unexamined stablecoin

failure cases. Finally, several future research avenues are mentioned, inspired by our critical analysis of the literature, with the aim of providing a better understanding and management of stablecoins as they become a more and more relevant part of the global economy.

### REFERENCES

 
- \[1\] Mohamed Shaker Ahmed and Elie Bouri. Long memory and structural breaks of cryptocurrencies trading volume. *Eurasian Economic Review* , 13(3):469–497, 2023.

- \[2\] Carol Alexander, Daniel F Heck, and Andreas Kaeck. The role of binance in bitcoin volatility transmission. *Applied Mathematical Finance* , 29(1):1–32, 2022.

- \[3\] Fahad Ali, Elie Bouri, Nader Naifar, Syed Jawad Hussain Shahzad, and Mohammad AlAhmad. An examination of whether gold-backed islamic cryptocurrencies are safe havens for international islamic equity markets. *Research in International Business and Finance* , 63: 101768, 2022.

- \[4\] Chika Anastesia Anisiuba, Obiamaka P Egbo, Felix C Alio, Chuka Ifediora, Ebele C Igwemeka, CO Odidi, and Hillary Chijindu Ezeaku. Analysis of cryptocurrency dynamics in the emerging market economies: does reinforcement or substitution effect prevail? *Sage Open* , 11(1):21582440211002516, 2021.

- \[5\] Lennart Ante and Aman Saggu. Time-varying bidirectional causal relationships between transaction fees and economic activity of subsystems utilizing the ethereum blockchain network. *Journal of Risk and Financial Management* , 17(1):19, 2024.

- \[6\] Lennart Ante, Ingo Fiedler, and Elias Strehle. The impact of transparent money flows: Effects of stablecoin transfers on the returns and trading volume of bitcoin. *Technological Forecasting and Social Change* , 170: 120851, 2021.

- \[7\] Lennart Ante, Ingo Fiedler, Jan Marius Willruth, and Fred Steinmetz. A systematic literature review of empirical research on stablecoins. *FinTech* , 2(1):34–47, 2023.

- \[8\] Alam Asadov, Ramazan Yildirim, and Mansur Masih. Toward greater stability in stablecoins: Empirical evidence from an analysis of precious metals. *Borsa Istanbul Review* , 23(5):1152–1172, 2023.

- \[9\] Atlantic Council. Central bank digital currency (cbdc) tracker. https://www.atlanticcouncil.org/cbdctracker/. Accessed: 01/03/2025.

- \[10\] Ahmed Ayadi, Yosra Ghabri, and Khaled Guesmi. Directional predictability from central bank digital currency to cryptocurrencies and stablecoins. *Research in International Business and Finance* , 65:101909, 2023.

- \[11\] Mahmut Ba˘gcı, Pınar Kaya Soylu, and Selc¸uk Kıran. The symmetric and asymmetric algorithmic trading strategies for the stablecoins. *Computational Economics* , pages 1–22, 2024.

- \[12\] Eranga Bandara, Dalvo Diamante, Steven Saltzman, RJ Richards, Sachin Shetty, Ravi Mukkamala, Xueping Liang, and Abdul Rahman. Gemcash—towards a diamond redeemable stable-growth coin. In *2022 International Conference on Cyber-Physical Social Intelligence (ICCSI)* , pages 104–109. IEEE, 2022.

- \[13\] Ole E Barndorff-Nielsen and Neil Shephard. Econometrics of testing for jumps in financial economics using bipower variation. *Journal of financial Econometrics* , 4 (1):1–30, 2006.

- \[14\] Dirk G Baur and Lai T Hoang. A crypto safe haven against bitcoin. *Finance Research Letters* , 38:101431, 2021.

- \[15\] Rihab Belguith, Yasmine Snene Manzli, Azza Bejaoui, and Ahmed Jeribi. Can gold-backed cryptocurrencies have dynamic hedging and safe-haven abilities against defi and nft assets? *Digital Business* , 4(2):100077, 2024.

- \[16\] Shreyas Bhat, Ayten Kahya, Rohit Kumar, and Bhaskar Krishnamachari. Simulating the makerdao stablecoin. In *2021 IEEE International Conference on Blockchain and Cryptocurrency (ICBC)* , pages 1–2. IEEE, 2021.

- \[17\] Shreyas Bhat, Ayten Betul Kahya, Bhaskar Krishnamachari, and Rohit Kumar. Daisim: A computational simulator for the makerdao stablecoin. In *4th International Symposium on Foundations and Applications of Blockchain 2021 (FAB 2021)* . Schloss DagstuhlLeibniz-Zentrum f¨ur Informatik, 2021.

- \[18\] Binance. Binance api documentation. https://binanc e-docs.github.io/apidocs/spot/en/, 2024. Accessed: 01/03/2025.

- \[19\] BlackRock. Blackrock stablecoin. https://en.cryptonom ist.ch/2025/01/03/blackrock-and-frax-launched-the-s tablecoin-frxusd-tokenized-by-securitize/. Accessed: 01-03-2025.

- \[20\] Blockchain ETL. Ethereum etl: Exporting the ethereum blockchain. https://ethereum-etl.readthedocs.io/en/lates t/google-bigquery/, 2024.

- \[21\] Martin M Bojaj, Milica Muhadinovic, Andrej Bracanovic, Andrej Mihailovic, Mladen Radulovic, Ivan Jolicic, Igor Milosevic, and Veselin Milacic. Forecasting macroeconomic effects of stablecoin adoption: A bayesian approach. *Economic Modelling* , 109:105792, 2022.

- \[22\] Antonio Briola, David Vidal-Tom´as, Yuanrong Wang, and Tomaso Aste. Anatomy of a stablecoin’s failure: The terra-luna case. *Finance Research Letters* , 51: 103358, 2023.

- \[23\] Gunduz Caginalp and D Balenovich. Asset flow and momentum: Deterministic and stochastic equations. *Philosophical Transactions of the Royal Society of London. Series A: Mathematical, Physical and Engineering Sciences* , 357(1758):2119–2133, 1999.

- \[24\] Maurantonio Caprolu, Matteo Pontecorvi, Matteo Signorini, Carlos Segarra, and Roberto Di Pietro. Analysis and patterns of unknown transactions in bitcoin. In *2021 IEEE international conference on blockchain*

- *(Blockchain)* , pages 170–179. IEEE, 2021.

- \[25\] Ben Charoenwong, Robert M Kirby, and Jonathan Reiter. Computer science abstractions to help reason about decentralized stablecoin design. *IEEE Access* , 2023.

- \[26\] Chartalist Team. Chartalist repository: A dataset for cryptocurrency market analysis. https://github.com/Cha rtalist/chartalist, 2024.

- \[27\] Kuo-Shing Chen and Shen-Ho Chang. Volatility comovement between bitcoin and stablecoins: Bekk–garch and copula–dcc–garch approaches. *Axioms* , 11(6):259, 2022.

- \[28\] Jaewoo Cho. A token economics explanation for the de-pegging of the algorithmic stablecoin: Analysis of the case of terra. *Ledger* , 8, 2023.

- \[29\] Ephraim Clark, Amine Lahiani, and Salma MeftehWali. Cryptocurrency return predictability: What is the role of the environment? *Technological Forecasting and Social Change* , 189:122350, 2023.

- \[30\] Jeremy Clark, Didem Demirag, and Mahsa Moosavi. Sok: demystifying stablecoins. *Communications of the ACM, Forthcoming* , 2019.

- \[31\] Coinbase. Coinbase api documentation. https://docs .cdp.coinbase.com/exchange/docs/welcome, 2024. Accessed: 01/03/2025.

- \[32\] CoinGecko. Coingecko: Cryptocurrency data platform. https://www.coingecko.com, 2024. Accessed: 01/03/2025.

- \[33\] CoinGecko. State of stablecoins: 2024, 2024. URL https://www.coingecko.com/research/publications/stat e-of-stablecoins-2024. Accessed: 01/03/2025.

- \[34\] CoinMarketCap. Coinmarketcap: Cryptocurrency market capitalizations. https://coinmarketcap.com, 2024. Accessed: 01/03/2025.

- \[35\] Brady Dale. Basis stablecoin confirms shutdown, blaming ’regulatory constraints’, December 2018. URL https://www.coindesk.com/markets/2018/12/13/basi s-stablecoin-confirms-shutdown-blaming-regulatory-c onstraints/. Accessed: 01/03/2025.

- \[36\] Souradeep Das and Revathi Venkataraman. Incentivized third party collateralization for stablecoins. *arXiv preprint arXiv:2309.11521* , 2023.

- \[37\] Riccardo De Blasis, Luca Galati, Alexander Webb, and Robert I Webb. Intelligent design: stablecoins (in) stability and collateral during market turbulence. *Financial Innovation* , 9(1):85, 2023.

- \[38\] Filezac de l’Etang. Dollar’s role in institutional and media impact on stablecoins. *Finance Research Letters* , 61:104999, 2024.

- \[39\] Antonio D´ıaz, Carlos Esparcia, and Diego Hu´elamo. Stablecoins as a tool to mitigate the downside risk of cryptocurrency portfolios. *The North American Journal of Economics and Finance* , 64:101838, 2023.

- \[40\] Antoine Djogbenou, Emre Inan, and Joann Jasiak. Time-varying coefficient dar model and stability measures for stablecoin prices: An application to tether. *Journal of International Money and Finance* , 139:

102946, 2023.

 
- \[41\] Yuhao Dong and Raouf Boutaba. Elasticoin: Lowvolatility cryptocurrency with proofs of sequential work. In *2019 ieee international conference on blockchain and cryptocurrency (icbc)* , pages 205–209. IEEE, 2019.

- \[42\] Kun Duan and Andrew Urquhart. The instability of stablecoins. *Finance Research Letters* , 52:103573, 2023.

- \[43\] Dune Analytics. Dune analytics. https://dune.com, 2024.

- \[44\] Barry Eichengreen and Ganesh Viswanath-Natraj. Stablecoins and central bank digital currencies: policy and regulatory challenges. *Asian Economic Papers* , 21(1): 29–46, 2022.

- \[45\] Etherscan.io. Etherscan: The ethereum blockchain explorer. https://etherscan.io, 2024.

- \[46\] Jingyu Feng, Ying Yuan, and Mingxuan Jiang. Are stablecoins better safe havens or hedges against global stock markets than other assets? comparative analysis during the covid-19 pandemic. *International Review of Economics & Finance* , 92:275–301, 2024.

- \[47\] Julian Fernandez-Mejia. Extremely stablecoins. *Finance Research Letters* , 63:105268, 2024.

- \[48\] Stefano Ferretti and Marco Furini. Cryptocurrency turmoil: Unraveling the collapse of a unified stablecoin (ustc) through twitter as a passive sensor. *Sensors* , 24 (4):1270, 2024.

- \[49\] Manoel Fernando Alonso Gadi and Miguel-Angel Sicilia. Analyzing safe haven, hedging and diversifier characteristics of heterogeneous cryptocurrencies against g7 and brics market indexes. *Journal of Risk and Financial Management* , 15(12):572, 2022.

- \[50\] Gregory Gadzinski, Alessio Castello, and Florie Mazzorana. Stablecoins: Does design affect stability? *Finance Research Letters* , 53:103611, 2023.

- \[51\] Luca Galati and Francesco Capalbo. Silicon valley bank bankruptcy and stablecoins stability. *International Review of Financial Analysis* , 91:103001, 2024.

- \[52\] Luca Galati, Alexander Webb, and Robert I Webb. Market behaviors around bankruptcy and frozen funds withdrawal: Trading stranded assets on ftx. *Journal of Economics and Business* , page 106196, 2024.

- \[53\] Alfredo Enrique Benitez Gasca, Ricardo Torres Mendoza, and Jenardo Nosedal-Sanchez. Forecast of the optimal activation function for the stablecoins using neural network. In *Proceedings of the 20th International Conference on Modelling and Applied Simulation (MAS 2021)* , Coyoac´an, Ciudad de M´exico, M´exico, 2021. The Authors. ISBN 978-88-85741-61-4. doi: 10.46354/i3m.2021.mas.010. URL https://doi.org/10.4 6354/i3m.2021.mas.010.

- \[54\] Yosra Ghabri, Oussama Ben Rhouma, Marj\`ene Gana, Khaled Guesmi, and Ramzi Benkraiem. Information transmission among energy markets, cryptocurrencies, and stablecoins under pandemic conditions. *International Review of Financial Analysis* , 82:102197, 2022.

- \[55\] Paolo Giudici, Thomas Leach, and Paolo Pagnottoni.

Libra or librae? basket based stablecoins to mitigate foreign exchange volatility spillovers. *Finance Research Letters* , 44:102054, 2022.

 
- \[56\] John M Griffin and Amin Shams. Is bitcoin really untethered? *The Journal of Finance* , 75(4):1913–1964, 2020.

- \[57\] Klaus Grobys and Toan Luu Duc Huynh. When tether says “jump!” bitcoin asks “how low?”. *Finance Research Letters* , 47:102644, 2022.

- \[58\] Klaus Grobys, Juha Junttila, James W Kolari, and Niranjan Sapkota. On the stability of stablecoins. *Journal of Empirical Finance* , 64:207–223, 2021.

- \[59\] Mariya Gubareva, Ahmed Bossman, and Tamara Teplova. Stablecoins as the cornerstone in the linkage between the digital and conventional financial markets. *The North American Journal of Economics and Finance* , 68:101979, 2023.

- \[60\] Aiman Hairudin and Azhar Mohamad. A fractal theory of investor demand for cryptocurrencies. *Applied Economics Letters* , pages 1–7, 2024.

- \[61\] Aiman Hairudin and Azhar Mohamad. The isotropy of cryptocurrency volatility. *International Journal of Finance & Economics* , 29(3):3779–3810, 2024.

- \[62\] Filip Hampl, Dagmar V´agnerov´a Linnertov´a, and Mat´uˇs Horv´ath. Crypto havens during war times? evidence from the russian invasion of ukraine. *The North American Journal of Economics and Finance* , 71:102093, 2024.

- \[63\] Jaqueline Hans, Sajjad Khan, and Davor Svetinovic. Blockchain cbdc security threats using stride. In *2023 Fifth International Conference on Blockchain Computing and Applications (BCCA)* , pages 522–529. IEEE, 2023.

- \[64\] BRIK Hatem, Jihene El Ouakdi, and Zied Ftiti. Roles of stable versus nonstable cryptocurrencies in bitcoin market dynamics. *Research in International Business and Finance* , 62:101720, 2022.

- \[65\] Zhiguo He, Jiasun Li, and Zhengxun Wu. Don’t trust, verify: The case of slashing from a popular ethereum explorer. In *Companion Proceedings of the ACM Web Conference 2023* , pages 1078–1084, 2023.

- \[66\] Henri T Heinonen. On creation of a stablecoin based on the morini’s scheme of inv&sav wallets and antimoney. In *2021 IEEE International Conference on Blockchain (Blockchain)* , pages 409–416. IEEE, 2021.

- \[67\] Lai T Hoang and Dirk G Baur. How stable are stablecoins? *The European Journal of Finance* , pages 1–17, 2021.

- \[68\] Immunefi. Hack analysis: Beanstalk governance attack, april 2022, January 2023. URL https://medium.com/i mmunefi/hack-analysis-beanstalk-governance-attack-a pril-2022-f42788fc821e. Accessed: 01/03/2025.

- \[69\] Akanksha Jalan, Roman Matkovskyy, and Larisa Yarovaya. “shiny” crypto assets: A systemic look at gold-backed cryptocurrencies during the covid-19 pandemic. *International Review of Financial Analysis* ,

78:101958, 2021.

 
- \[70\] Klaudia Jarno and Hanna Kołodziejczyk. Does the design of stablecoins impact their volatility? *Journal of Risk and Financial Management* , 14(2):42, 2021.

- \[71\] Clemens Jeger, Bruno Rodrigues, Eder Scheid, and Burkhard Stiller. Analysis of stablecoins during the global covid-19 pandemic. In *2020 Second International Conference on Blockchain Computing and Applications (BCCA)* , pages 30–37. IEEE, 2020.

- \[72\] Sam Kazemian, Jason Huan, Jonathan Shomroni, and Kedar Iyer. Frax: A fractional-algorithmic stablecoin protocol. In *2022 IEEE International Conference on Blockchain (Blockchain)* , pages 406–411. IEEE, 2022.

- \[73\] Rafiullah Khan, Kieran McLaughlin, David Laverty, and Sakir Sezer. Stride-based threat modeling for cyberphysical systems. In *2017 IEEE PES Innovative Smart Grid Technologies Conference Europe (ISGT-Europe)* , pages 1–6. IEEE, 2017.

- \[74\] Stefan Kitzler, Friedhelm Victor, Pietro Saggese, and Bernhard Haslhofer. Disentangling decentralized finance (defi) compositions. *ACM Transactions on the Web* , 17(2):1–26, 2023.

- \[75\] Martin Kj¨aer, Monika Di Angelo, and Gernot Salzer. Empirical evaluation of makerdao’s resilience. In *2021 3rd Conference on Blockchain Research & Applications for Innovative Networks and Services (BRAINS)* , pages 193–200. IEEE, 2021.

- \[76\] Ariah Klages-Mundt and Andreea Minca. While stability lasts: A stochastic model of noncustodial stablecoins. *Mathematical Finance* , 32(4):943–981, 2022.

- \[77\] Ariah Klages-Mundt, Dominik Harz, Lewis Gudgeon, Jun-You Liu, and Andreea Minca. Stablecoins 2.0: Economic foundations and risk-based models. In *Proceedings of the 2nd ACM Conference on Advances in Financial Technologies* , pages 59–79, 2020.

- \[78\] Agata Kliber. Looking for a safe haven against american stocks during covid-19 pandemic. *The North American Journal of Economics and Finance* , 63:101825, 2022.

- \[79\] Hanna Kołodziejczyk. Stablecoins as diversifiers, hedges and safe havens: A quantile coherency approach. *The North American Journal of Economics and Finance* , 66:101912, 2023.

- \[80\] Dimitrios Koutsoupakis. Are stable cryptocurrencies exempted from impossible trinity? *Journal of Economic Studies* , 48(8):1480–1496, 2020.

- \[81\] Seungju Lee, Jaewook Lee, and Yunyoung Lee. Dissecting the terra-luna crash: Evidence from the spillover effect and information flow. *Finance Research Letters* , 53:103590, 2023.

- \[82\] Mark Levene. A hypothesis test for the goodness-offit of the marginal distribution of a time series with application to stablecoin data. *Engineering Proceedings* , 5(1):10, 2021.

- \[83\] Cangshu Li and Yan Shen. The potential impacts and risks of global stablecoins. *China Economic Journal* , 14(1):39–51, 2021.

- \[84\] Dun Li, Dezhi Han, Tien-Hsiung Weng, Zibin Zheng, Hongzhi Li, and Kuan-Ching Li. On stablecoin: Ecosystem, architecture, mechanism and applicability as payment method. *Computer Standards & Interfaces* , 87:103747, 2024.

- \[85\] Cheyenne Ligon and Shaurya Malwa. Defi platform acala’s stablecoin falls 99 URL https://www.coindesk .com/tech/2022/08/15/acalas-stablecoin-falls-99-perce nt-after-hackers-issue-13-billion-tokens/. Accessed: 01/03/2025.

- \[86\] Qiushan Liu, Lang Yu, and Chang Jia. Mover: stabilize decentralized finance system with practical risk management. In *2020 2nd Conference on Blockchain Research & Applications for Innovative Networks and Services (BRAINS)* , pages 55–56. IEEE, 2020.

- \[87\] Richard K Lyons and Ganesh Viswanath-Natraj. What keeps stablecoins stable? *Journal of International Money and Finance* , 131:102777, 2023.

- \[88\] Moinak Maiti, Zoran Grubisic, and Darko B Vukovic. Dissecting tether’s nonlinear dynamics during covid-19. *Journal of Open Innovation: Technology, Market, and Complexity* , 6(4):161, 2020.

- \[89\] Harry Markowitz. Modern portfolio theory. *Journal of Finance* , 7(11):77–91, 1952.

- \[90\] Peter Mell, Peter Mell, and Dylan Yaga. *Understanding stablecoin technology and related security considerations* . US Department of Commerce, National Institute of Standards and Technology, 2023.

- \[91\] Makiko Mita, Kensuke Ito, Shohei Ohsawa, and Hideyuki Tanaka. What is stablecoin?: A survey on price stabilization mechanisms for decentralized payment systems. In *2019 8th International Congress on Advanced Applied Informatics (IIAI-AAI)* , pages 60–66. IEEE, 2019.

- \[92\] Amani Moin, Kevin Sekniqi, and Emin Gun Sirer. Sok: A classification framework for stablecoin designs. In *Financial Cryptography and Data Security: 24th International Conference, FC 2020, Kota Kinabalu, Malaysia, February 10–14, 2020 Revised Selected Papers 24* , pages 174–197. Springer, 2020.

- \[93\] Ra´ul Morales-Resendiz, Jorge Ponce, Pablo Picardo, Andr´es Velasco, Bobby Chen, Le´on Sanz, Gabriela Guiborg, Bj¨orn Segendorff, Jos´e Luis Vasquez, John Arroyo, et al. Implementing a retail cbdc: Lessons learned and key insights. *Latin American Journal of Central Banking* , 2(1):100022, 2021.

- \[94\] Abra˜ao DC Nascimento, Maria CS Lima, Hassan Bakouch, and Najla Qarmalah. Scaled muth–arma process applied to finance market. *Mathematics* , 11(8):1908, 2023.

- \[95\] Thach VH Nguyen, Thai Vu Hong Nguyen, Thanh Cong Nguyen, Thu Thi Anh Pham, and Quan MP Nguyen. Stablecoins versus traditional cryptocurrencies in response to interbank rates. *Finance Research Letters* , 47:102744, 2022.

- \[96\] Nico Oefele, Dirk G Baur, and Lee A Smales. Flight-

to-quality—money market mutual funds and stablecoins during the march 2023 banking crisis. *Economics Letters* , 234:111464, 2024.

 
- \[97\] Omni Foundation. Omni explorer. https://omniexplorer .info, 2024.

- \[98\] Myriam Ben Osman, Christian Urom, Khaled Guesmi, and Ramzi Benkraiem. Economic sentiment and the cryptocurrency market in the post-covid-19 era. *International Review of Financial Analysis* , 91:102962, 2024.

- \[99\] Seongcheol Paeng, Dave Senteney, and Taewon Yang. Spillover effects, lead and lag relationships, and stable coins time series. *The Quarterly Review of Economics and Finance* , 95:45–60, 2024.

- \[100\] PayPal. Paypal usd. https://www.paypal.com/us/di gital-wallet/manage-money/crypto/pyusd. Accessed: 01/03/2025.

- \[101\] Ingolf GA Pernice, Sebastian Henningsen, Roman Proskalovich, Martin Florian, Hermann Elendner, and Bj¨orn Scheuermann. Monetary stabilization in cryptocurrencies–design approaches and open questions. In *2019 crypto valley conference on blockchain technology (cvcbt)* , pages 47–59. IEEE, 2019.

- \[102\] Ingolf Gunnar Anton Pernice. On stablecoin price processes and arbitrage. In *Financial Cryptography and Data Security. FC 2021 International Workshops: CoDecFin, DeFi, VOTING, and WTSC, Virtual Event, March 5, 2021, Revised Selected Papers 25* , pages 124– 135. Springer, 2021.

- \[103\] Bryan Routledge and Ariel Zetlin-Jones. Currency stability using blockchain technology. *Journal of Economic Dynamics and Control* , 142:104155, 2022.

- \[104\] Mary-Ann Russon. Jpmorgan launches jpm coin. https: //www.bbc.com/news/business-47240760. Accessed: 01/03/2025.

- \[105\] Kanis Saengchote and Krislert Samphantharak. Digital money creation and algorithmic stablecoin run. *Finance Research Letters* , 64:105435, 2024.

- \[106\] Aman Saggu. The intraday bitcoin response to tether minting and burning events: Asymmetry, investor sentiment, and “whale alerts” on twitter. *Finance Research Letters* , 49:103096, 2022.

- \[107\] Mehdi Salehi, Jeremy Clark, and Mohammad Mannan. Red-black coins: Dai without liquidations. In *Financial Cryptography and Data Security. FC 2021 International Workshops: CoDecFin, DeFi, VOTING, and WTSC, Virtual Event, March 5, 2021, Revised Selected Papers 25* , pages 136–145. Springer, 2021.

- \[108\] Krisztian Sandor. Stablecoins increasingly used for savings, payments in emerging countries, but crypto trading still leads: Report. *Yahoo Finance* , September 2024. URL https://finance.yahoo.com/news/stablecoins-inc reasingly-used-savings-payments-164500240.html. Accessed: 01/03/2025.

- \[109\] Vijak Sethaput and Supachate Innet. Blockchain application for central bank digital currencies (cbdc). *Cluster Computing* , 26(4):2183–2197, 2023.

- \[110\] Jin Su, Xinran Li, Mingchen Zhang, and Ziyao Jin. Analysis of regulation policies in may 2021 on cryptocurrency market. In *Proceedings of the 2022 6th International Conference on E-Business and Internet* , pages 175–181, 2022.

- \[111\] Binh Nguyen Thanh, Thai Nguyen Vu Hong, Huy Pham, Thanh Nguyen Cong, and Thu Pham Thi Anh. Are the stabilities of stablecoins connected? *Journal of Industrial and Business Economics* , 50(3):515–525, 2023.

- \[112\] The Graph Foundation. The graph protocol: Decentralized data querying for blockchain networks. https: //thegraph.com, 2024.

- \[113\] Fr´ed´eric Tronnier. Privacy in payment in the age of central bank digital currency. In *Privacy and Identity Management: 15th IFIP WG 9.2, 9.6/11.7, 11.6/SIG 9.2. 2 International Summer School, Maribor, Slovenia, September 21–23, 2020, Revised Selected Papers 15* , pages 96–114. Springer, 2021.

- \[114\] Tronscan.org. Tronscan: Blockchain explorer for the tron network. https://tronscan.org, 2024.

- \[115\] Wei-Tek Tsai, Weijing Xiang, Shuai Wang, and Enyan Deng. A new digital-currency model based on certificates. In *International Conference on Smart Computing and Communication* , pages 23–34. Springer, 2022.

- \[116\] Gang-Jin Wang, Xin-yu Ma, and Hao-yu Wu. Are stablecoins truly diversifiers, hedges, or safe havens against traditional cryptocurrencies as their name suggests? *Research in International Business and Finance* , 54:101225, 2020.

- \[117\] Yizhi Wang, Brian M Lucey, Samuel A Vigne, and Larisa Yarovaya. The effects of central bank digital currencies news on financial markets. *Technological Forecasting and Social Change* , 180:121715, 2022.

- \[118\] Wang Chun Wei. The impact of tether grants on bitcoin. *Economics Letters* , 171:19–22, 2018.

- \[119\] Tom Wilson and Pete Schroeder. Facebook-backed crypto project diem. https://www.reuters.com/tech nology/facebook-backed-crypto-project-diem-launc h-us-stablecoin-major-shift-2021-05-12/. Accessed: 01/03/2025.

- \[120\] Gabriel Shui Tang Wu and Pak Ho Leung. Do assetbacked stablecoins spread crypto volatility to traditional financial assets? evidence from tether. *Economics Letters* , 229:111213, 2023.

- \[121\] Wei Yin, Ziling Chen, Xinxin Luo, and Berna KirkulakUludag. Forecasting cryptocurrencies’ price with the financial stress index: a graph neural network prediction strategy. *Applied Economics Letters* , 31(7):630–639, 2024.

- \[122\] Joachim Zahnentferner, Dmytro Kaidalov, Jean-Fr´ed´eric Etienne, and Javier D´ıaz. Djed: A formally verified crypto-backed autonomous stablecoin protocol. In *2023 IEEE International Conference on Blockchain and Cryptocurrency (ICBC)* , pages 1–9. IEEE, 2023.

- \[123\] Haolin Zhang and Youping Zhao. Enhancing economic

security in blockchain-based spectrum trading: A stablecoin approach. In *2023 9th International Conference on Computer and Communications (ICCC)* , pages 2503– 2507. IEEE, 2023.

 
- \[124\] Wenqi Zhao, Hui Li, and Yuming Yuan. Understand volatility of algorithmic stablecoin: Modeling, verification and empirical analysis. In *Financial Cryptography and Data Security. FC 2021 International Workshops: CoDecFin, DeFi, VOTING, and WTSC, Virtual Event, March 5, 2021, Revised Selected Papers 25* , pages 97– 108. Springer, 2021.

- \[125\] Xi Zhao, Peilin Ai, Fujun Lai, Xin Luo, and Jose Benitez. Task management in decentralized autonomous

organization. *Journal of Operations Management* , 68(67):649–674, 2022.

 
- \[126\] Jason Zhu, Arijit Khan, and Cuneyt Gurcan Akcora. Data depth and core-based trend detection on blockchain transaction networks. *Frontiers in Blockchain* , 7:1342956, 2024.

- \[127\] Jin Zhu, Jun Zou, Yingxia Jing, Weiwei Yao, Yifan Mo, and Zibin Zheng. A survey of blockchain-based stablecoin: Cryptocurrencies and central bank digital currencies. In *International Conference on Blockchain and Trustworthy Systems* , pages 177–193. Springer, 2022.

Last updated: October 2026.
