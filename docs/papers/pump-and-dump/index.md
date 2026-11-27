# What drives cryptocurrency pump and dump schemes: Coin versus market factors?

Source: [https://amahrous.com/papers/pump-and-dump/](https://amahrous.com/papers/pump-and-dump/)

[← Ahmed Mahrous’s homepage](https://amahrous.com/#research)

Lanouar Charfeddine and Ahmed Mahrous

*Finance Research Letters, 67, 105861* · 2024 · ABDC rank: A · IF 7.1

[PDF](https://amahrous.com/papers/pump-and-dump/paper.pdf) · [Read full text](https://amahrous.com/papers/pump-and-dump/#full-text) · [BibTeX](https://amahrous.com/papers/pump-and-dump/citation.bib) · [DOI](https://doi.org/10.1016/j.frl.2024.105861) · [Cite](https://amahrous.com/papers/pump-and-dump/#citation)

## TL;DR

An empirical study of coin-level and market-level factors associated with cryptocurrency pump-and-dump schemes.

## Abstract

This paper investigates both coin-specific and market-based factors that drive cryptocurrency pump-and-dump schemes. It analyzes a data set comprising 1457 pump events that occurred from January 3, 2018, to January 2, 2022. Empirical findings, derived from binary cross-sectional regression models, reveal several characteristics that increase the likelihood of cryptocurrencies being pumped. These include lower market capitalization, lower trading volume, greater social media popularity, increased developer activity, and fewer exchanges trading them. Furthermore, the study employs count time-series models to examine market-based factors. The results indicate that periods of higher volatility or uncertainty are associated with an increase in pre-announced pump-and-dump activities. Additionally, the analysis shows that macroeconomic factors and specific time-related effects – such as Sundays, certain months, and the COVID-19 period – are significant in explaining the frequency of pump occurrences. Based on these findings, the article discusses several targeted recommendations.

## Citation

Lanouar Charfeddine and Ahmed Mahrous. 2024. What drives cryptocurrency pump and dump schemes: Coin versus market factors?. Finance Research Letters, 67, 105861. [doi:10.1016/j.frl.2024.105861](https://doi.org/10.1016/j.frl.2024.105861).

```bibtex
@article{pump-and-dump-2024,
  author = {Charfeddine, Lanouar and Mahrous, Ahmed},
  title = {{What drives cryptocurrency pump and dump schemes: Coin versus market factors?}},
  year = {2024},
  doi = {10.1016/j.frl.2024.105861},
  publisher = {Elsevier BV},
  journal = {Finance Research Letters},
  volume = {67},
  pages = {105861},
  eid = {105861},
  url = {https://doi.org/10.1016/j.frl.2024.105861}
}
```

## Full text

### **1. Introduction**

The cryptocurrency market’s rapid growth has been accompanied by a concerning increase in market manipulation. Such manipulation undermines market trust and results in financial losses for many victims (Dhawan and Putnin, š, 2023). Our paper focuses on a relatively new form of manipulation termed ‘‘pre-announced pump-and-dump’’, which differs from traditional pumpand-dump schemes in key ways. First, the details and intent are publicly announced on social media platforms like Telegram. Second, these schemes are more accessible to smaller-scale investors. Third, pre-announced pump-and-dump schemes have faced practically no regulatory or legal actions.

The impact of this specific type of manipulation can be staggering. Dhawan and Putnin, š (2023) find that up to 23 million individuals are involved in these schemes. Hamrick et al. (2021) identify more than 3000 schemes in 6 months. Hu et al. (2023) identify more than 1000 Telegram groups related to these schemes, with one pump involving 27 million USD in 5 min. In our sample, around 25% of cryptocurrencies currently listed on Binance have been targeted, with the percentage increasing for delisted coins. One cryptocurrency has been targeted 26 times, with price increases up to 1821% in less than a minute. These schemes primarily

✩ The authors would like to express their gratitude to the Editor-in-Chief, the Associate Editor, and the two anonymous referees for their invaluable comments and suggestions. This paper represents an enhanced version of a chapter from the second author’s master’s thesis, and we extend our thanks to the examiners, Dr. Nicolla Borri, Dr. Karim Mimouni, and Dr. Mazen Al Masri, for their insightful feedback. The statements made herein are solely the responsibility of the authors, who are also responsible for any remaining errors.

∗ Corresponding author. *E-mail addresses:* lcharfeddine@qu.edu.qa (L. Charfeddine), ahmed.mahrous@kaust.edu.sa (A. Mahrous). https://doi.org/10.1016/j.frl.2024.105861 Received 18 January 2024; Received in revised form 10 July 2024; Accepted 13 July 2024 Available online 3 August 2024

1544-6123/© 2024 The Author(s). Published by Elsevier Inc. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).

### L. Charfeddine and A. Mahrous

target small to medium cryptocurrencies but can affect larger cryptocurrencies (Canh et al., 2019) and the broader economy (Yue et al., 2021; Kurka, 2019).

Despite existing studies, a focused examination of factors increasing the risk of these schemes is lacking. This paper addresses this gap by investigating various contributing factors. Our research contributes to the literature in several ways: providing novel insights into these schemes by investigating behavioral-based, market-based, coin-specific, macroeconomic, time-effect, and COVID19 variables; utilizing both time-series and cross-sectional approaches; and challenging some previous research findings, such as the significance of social media variables and the linear effect of coin size on the likelihood of being pumped.

Our research contributes to the cryptocurrency pump-and-dump literature in several ways. First, it provides novel insights into these schemes by investigating how behavioral-based, market-based, coin-specific, macroeconomic, time-effect, and COVID-19 variables explain their occurrence frequency. Second, this is the first paper to use both time-series and cross-sectional approaches to show that a simple, yet robust, methodology using various count and binary regression models can effectively analyze cryptocurrency pump-and-dump schemes. Third, by using a different sample, methodology, and proxy variables, we challenge previous research findings. For example, contrary to Nghiem et al. (2021), we show that social media variables significantly explain this manipulation. Additionally, our results indicate that coin size has a linear effect on the likelihood of being pumped, contradicting Dhawan and Putnin, š (2023).

The rest of the paper is organized as follows. Section 2 describes the data and econometric models used. Section 3 presents the empirical findings and discusses them in comparison to previous studies. Section 4 concludes and provides policy recommendations.

### **2. Materials and methods**

#### *2.1. Data and variable description*

The dataset for pump occurrences, covering January 3, 2018, to January 2, 2022, includes 1457 pumps from over 100 Telegram groups. We gathered most of the data from FRED, Binance, CoinGecko, CoinMarketCap, and a crypto-sentiment index website. The dates of pump events and the names of the targeted coins were sourced from La Morgia et al. (2020) and Hu et al. (2023). Integrating data from these studies enhances our ability to compare our findings with previous work.

To ensure quality analysis, we undertook a diligent data-cleaning process. This involved removing duplicate pump events coordinated by multiple groups. We also performed extensive analysis to verify data accuracy. This included confirming that most recorded events led to a rapid increase followed by a rapid decrease in the value of the targeted coin within seconds or minutes of the pump announcement, as expected.

All 1457 pumps were analyzed for market-based factors, while the analysis of coin-specific factors used only 325 pumps from Binance due to data availability.<sup>1</sup>

Our study uses 19 explanatory variables: 8 for coin-specific factors and 11 for market-based factors. The eight coin-specific factors, extracted from the CoinGecko API,<sup>2</sup> reflect aspects like coin size and liquidity, development activity, social media engagement, and the number of exchanges where a coin is listed.

The eleven market-based factors include Bitcoin market data from CoinMarketCap, economic indicators from FRED, and a cryptosentiment index. They also include dummy variables for COVID-19, months, and days of the week. A detailed description of all variables is in Table 5 (supplementary document).

#### *2.2. Econometric models*

We consider two classes of limited dependent variable models to examine factors explaining the occurrence (binary data) and frequency (count data) of pump-and-dump schemes. For the first class, we use two binary regression models: the Logit model as the main one and the Probit for robustness (reported in the supplementary document). The dependent variable is assigned a value of one if a coin is subject to a pump-and-dump scheme and zero otherwise. For the second class, we use two count data models: (1) the negative binomial regression model for monthly and weekly data and (2) the Poisson regression model for daily data. Here, the dependent variable represents the count of pump-and-dump events within a specified period (monthly, weekly, or daily). Some variables are omitted from certain models due to limited data availability or to prevent multicollinearity. *i. Logit and Probit Models*

The general form of the Logit and Probit models is given by:

[Figure, table, or displayed equation from PDF page 2 (figure in original article)](https://amahrous.com/papers/pump-and-dump/#fulltext-page-2)

> 1 Binance provided the most accessible, complete, and standardized data. Additionally, many previously manipulated coins have been delisted from Binance, limiting data for these coins.
> 
>  
> 
> 2 https://www.coingecko.com/en/api/

### L. Charfeddine and A. Mahrous

**Table 1**

Descriptive statistics on the number of pumps for monthly, weekly, and daily frequencies.

<table><tr><th></th><th>Mean</th><th>Median</th><th>Mode</th><th>St. Dev.</th><th>Minimum</th><th>Maximum</th><th>Count</th><th>Zero</th></tr><tr><td>Monthly</td><td>11.4</td><td>10.5</td><td>12</td><td>6.5</td><td>1</td><td>31</td><td>48</td><td>0%</td></tr><tr><td>Weekly</td><td>2.6</td><td>2.0</td><td>2</td><td>2.0</td><td>0</td><td>10</td><td>209</td><td>10%</td></tr><tr><td>Daily</td><td>0.4</td><td>0.0</td><td>0</td><td>0.6</td><td>0</td><td>4</td><td>1461</td><td>69%</td></tr></table>

where *𝐻* ( *.* ) is a function taking values strictly between zero and one. For the Logit model, *𝐻* ( *.* ) is the logistic function; for the Probit model, it is the standard normal cumulative distribution function. Size *𝑖* is either the Market Cap or Volume for coin *𝑖* , depending on the model.

*ii. Standard Poisson and Negative Binomial Regressions*

The Poisson regression model specifies the conditional mean of the daily pump count *𝑦* as follows:

[Figure, table, or displayed equation from PDF page 3 (figure in original article)](https://amahrous.com/papers/pump-and-dump/#fulltext-page-3)

[Figure, table, or displayed equation from PDF page 3 (figure in original article)](https://amahrous.com/papers/pump-and-dump/#fulltext-page-3)

where *𝑒𝑥𝑝* ( *.* ) is the exponential function, **𝐲𝐭** is the daily number of pumps, **𝐱𝐭** is the vector of covariates at time *𝑡* , and ***𝜷*** is the vector of parameters to be estimated, including the intercept. This model ensures the conditional mean is positive since the number of pumps cannot be negative.

The negative binomial model is given by:

[Figure, table, or displayed equation from PDF page 3 (figure in original article)](https://amahrous.com/papers/pump-and-dump/#fulltext-page-3)

where *ℎ𝑡* = *𝑒𝑥𝑝* ( *𝜖𝑡* ) is assumed to have a one-parameter gamma distribution: *𝐺* ( *𝜃, 𝜃* ) with mean 1 and variance 1∕ *𝜃* . The vector **𝐱𝐭** includes the set of independent variables used to explain the number of pumps during a period.

For both models in Eqs. (1) and (2), the vector **𝐱𝐭** comprises several variables, including BTCRet, BTCVar, UMCSent, AltSent, VIX, EPU, Inflation, Interest, COVID-19, and time-effects.

#### *2.2.1. Robustness results*

To enhance robustness, we used several techniques. For instance, both Logit and Probit models for binary regressions yielded equivalent results. Moreover, we applied the ASINH transformation to mitigate skewness and outliers. In addition, quartile analysis tested for non-linear relationships in coin size.

For count data, we used the Poisson Goodness of Fit Test to confirm adherence to a Poisson distribution and the Cameron & Trivedi test to check for overdispersion, opting for the negative binomial model when necessary. The Proportion of Zeros Z-test ruled out excess zeros.<sup>3</sup> Preliminary correlations matched most econometric results. Findings remained consistent with time effects and alternative proxy variables (e.g., Market Cap vs. Volume). The Link and RESET tests did not detect misspecification or omitted variable bias. To prevent reverse causality, we excluded coin characteristics one week before and after each pump; Granger-causality tests did not detect reverse causality.

### **3. Results**

#### *3.1. Descriptive statistics and preliminary results*

#### *3.1.1. Coin-specific factors*

Fig. 1 shows distributions and correlations for coin-specific factors. Several preliminary conclusions can be drawn. First, the distributions differ between pumped and non-pumped coins (see the diagonal of the plot and the first column). This suggests these variables may explain the likelihood of a coin being pumped.

Second, the Spearman rank correlation coefficients (in the cells above the diagonal) show that most explanatory variables significantly correlate with the likelihood of a coin being pumped. For instance, market capitalization, trading volume, public interest score, and the number of exchanges are negatively correlated with pump likelihood (first row). In contrast, community score and developer score are positively correlated with pump likelihood.

Based on Fig. 1, only circulated supply and liquidity scores are not correlated with the likelihood of a coin being pumped. For all variables except the public interest score, the sign and significance of correlation coefficients match the marginal effects in Table 3.

#### *3.1.2. Market-based factors*

For the market-based factors analysis, we report descriptive statistics for dependent and explanatory variables, as well as the correlation between pump frequency and various explanatory variables.

Table 1 reports basic statistics on the number of pumps for monthly, weekly, and daily frequencies. The sample data spans 48 months, 209 weeks, and 1461 days, with an average of over 11 pumps per month, about 3 per week, and less than 1 per day.

> 3 Results from zero-inflated models were not significantly different, enhancing robustness.

### L. Charfeddine and A. Mahrous

[Figure, table, or displayed equation from PDF page 4 (figure in original article)](https://amahrous.com/papers/pump-and-dump/#fulltext-page-4)

**Fig. 1.** Spearman rank correlation and distribution analysis for coin-specific factors.

This figure presents a pairplot comparing various variables between pumped (red) and non-pumped (green) coins. Variables include Market Capitalization (MktCap), Trading Volume (Vol), Circulating Supply (CSupply), Community Score (Comm), Developer Score (Dev), Liquidity Score (Liq), Public Interest Score (Publ), Number of Exchanges (NumExch), and Coin Age (Age). The diagonal shows density plots, the upper triangle shows Spearman rank correlation coefficients with significance (\*=p *\<* 0.10, \*\*=p *\<* 0.05, \*\*\*=p *\<* 0.01), and the lower triangle shows scatter plots, with the first column using violin plots and bar charts for distributions/counts.

In Panels A and B of Table 2, we present descriptive statistics for the weekly explanatory variables and the Spearman rank correlation coefficients, respectively. Panel A shows significant fluctuation in all variables over the analysis period. For example, BTC mean returns fluctuated between −5.83 and 3.72, averaging 0.08. BTC volatility also varied widely, averaging 0.16, ranging from near zero to 3.52. Macroeconomic factors showed strong variation, influenced partly by the COVID-19 pandemic (Maouchi et al., 2022; Montasser et al., 2022; Boubaker et al., 2023).

Panel B of Table 2 shows significant correlations between pump frequency and most explanatory variables, particularly bitcoin returns and volatility, macroeconomic indicators, uncertainty proxies, inflation, and interest rates.

#### *3.2. Econometric models results*

#### *3.2.1. Coin-specific factors results*

Table 3 presents the Logit regression results, identifying factors that significantly affect the likelihood of a cryptocurrency experiencing a pre-announced pump-and-dump scheme. The findings align with the preliminary correlation analysis in Fig. 1. Consistent with the literature (Victor and Hagemann, 2019; Tsuchiya, 2021; Nghiem et al., 2021; Dhawan and Putnin, š, 2023), smaller cryptocurrencies are more susceptible to such manipulations.

Manipulators may prefer smaller coins because they are easier to impact with less capital, face less regulatory scrutiny, and can generate more hype. This size effect is consistent whether using market capitalization or trading volume as the proxy for size.

To examine the potential non-linear relationship between a cryptocurrency’s size and the likelihood of market manipulation, our regression model includes dummy variables for market cap and trading volume quartiles. Contrary to Dhawan and Putnin, š (2023), we observed no non-linear trends. Assessing quartile size variables in isolation (see Table 7 in the supplementary document) showed a linear decrease in the likelihood of a pump with increasing market capitalization. For trading volume, the likelihood of being pumped was lower for the largest coins (Q3 and Q4) compared to the smallest coins (Q1). Including additional explanatory

### L. Charfeddine and A. Mahrous

**Table 2**

Descriptive statistics and Spearman rank correlation analysis for Market-based factors.

<table><tr><th></th><th>BTCRet</th><th>BTCVar</th><th>VIX</th><th>EPU</th><th>Inflation</th><th>Interest</th><th>AltSent</th></tr><tr><th>Panel A:</th><th>Descriptive statistics</th><th>for Weekly</th><th>data</th><th></th><th></th><th></th><th></th></tr><tr><td>Mean</td><td>0.08</td><td>0.16</td><td>20.22</td><td>161.04</td><td>1.85</td><td>1.86</td><td>46.11</td></tr><tr><td>Median</td><td>0.21</td><td>0.10</td><td>17.99</td><td>119.23</td><td>1.66</td><td>1.84</td><td>42.86</td></tr><tr><td>St. Dev.</td><td>1.53</td><td>0.28</td><td>8.65</td><td>113.03</td><td>0.81</td><td>0.52</td><td>21.60</td></tr><tr><td>Minimum</td><td>-5.83</td><td>0.00</td><td>9.34</td><td>46.85</td><td>0.55</td><td>0.21</td><td>10.29</td></tr><tr><td>Maximum</td><td>3.72</td><td>3.52</td><td>74.62</td><td>601.16</td><td>3.21</td><td>3.12</td><td>94.00</td></tr><tr><td>Panel B:</td><td>Spearman Rank</td><td>Correlation</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Monthly</td><td>0.392***</td><td>0.293**</td><td>0.143</td><td>0.34**</td><td>-0.165</td><td>-0.268*</td><td>0.191</td></tr><tr><td>Weekly</td><td>0.147**</td><td>0.154**</td><td>0.181***</td><td>0.218***</td><td>-0.23***</td><td>-0.172**</td><td>0.071</td></tr><tr><td>Daily</td><td>0.000</td><td>0.033</td><td>0.07***</td><td>0.106***</td><td>-0.13***</td><td>-0.08***</td><td>0.015</td></tr></table>

Panel A outlines descriptive statistics for market-based explanatory variables for weekly data. Panel B presents the Spearman rank correlation between these explanatory variables and the number of pumps for monthly, weekly, and daily data. The factors include Bitcoin Price Return (BTCRet), Bitcoin Price Variance (BTCVar), CBOE Volatility Index (VIX), Economic Policy Uncertainty Index (EPU), Inflation rate, Interest rate, and Crypto Fear & Greed Index (AltSent). \* Statistical significance =p\<0.10. \*\* Statistical significance =p\<0.05. \*\*\* Statistical significance =p\<0.01.

### **Table 3**

Logit model estimates: Coin-specific factors.

<table><tr><th></th><th>MktCap</th><th></th><th>Volume</th><th></th></tr><tr><th>Size</th><th>−6.99***</th><th>–</th><th>−4.28**</th><th>–</th></tr><tr><td></td><td>(−3.92)</td><td></td><td>(−2.60)</td><td></td></tr><tr><td>SizeQ1</td><td>–</td><td>0.29***</td><td>–</td><td>0.17*</td></tr><tr><td></td><td></td><td>(3.39)</td><td></td><td>(1.91)</td></tr><tr><td>SizeQ2</td><td>–</td><td>0.20**</td><td>–</td><td>0.21**</td></tr><tr><td></td><td></td><td>(2.52)</td><td></td><td>(2.40)</td></tr><tr><td>SizeQ3</td><td>–</td><td>0.16**</td><td>–</td><td>0.18**</td></tr><tr><td></td><td></td><td>(2.20)</td><td></td><td>(2.14)</td></tr><tr><td>CSupply</td><td>0.16</td><td>0.05</td><td>−0.07</td><td>−0.14</td></tr><tr><td></td><td>(0.34)</td><td>(0.11)</td><td>(−0.16)</td><td>(−0.31)</td></tr><tr><td>ComScore</td><td>5.83**</td><td>5.98**</td><td>5.05**</td><td>5.51**</td></tr><tr><td></td><td>(1.77)</td><td>(1.80)</td><td>(1.57)</td><td>(1.68)</td></tr><tr><td>DevScore</td><td>2.07***</td><td>2.19***</td><td>1.71***</td><td>2.08***</td></tr><tr><td></td><td>(2.18)</td><td>(2.29)</td><td>(1.76)</td><td>(2.20)</td></tr><tr><td>LiqScore</td><td>0.63</td><td>−0.67</td><td>0.87</td><td>−0.12</td></tr><tr><td></td><td>(0.12)</td><td>(−0.12)</td><td>(0.16)</td><td>(−0.02)</td></tr><tr><td>PubScore</td><td>−4.11</td><td>−8.04</td><td>−8.20</td><td>−9.01</td></tr><tr><td></td><td>(−0.54)</td><td>(−0.92)</td><td>(−0.97)</td><td>(−1.04)</td></tr><tr><td>NumExch</td><td>−0.67***</td><td>−0.89***</td><td>−1.17***</td><td>−1.45***</td></tr><tr><td></td><td>(−1.45)</td><td>(−1.95)</td><td>(−2.33)</td><td>(−3.15)</td></tr><tr><td>Age</td><td>0.35***</td><td>0.29***</td><td>0.29***</td><td>0.28***</td></tr><tr><td></td><td>(3.50)</td><td>(3.05)</td><td>(3.04)</td><td>(2.88)</td></tr></table>

The table presents results from two Logit models. The dependent variable is the likelihood of a coin being pumped. Independent variables are Size (either Market Capitalization or Trading Volume), Circulating Supply (CSupply), Community Score (ComScore), Developer Score (DevScore), Liquidity Score (LiqScore), Public Interest Score (PubScore), number of exchanges a coin is listed on (NumExch),coin age in months (Age), and Size quartiles. Marginal effects are shown with Z-statistics in parentheses. For detailed variable descriptions, see Table 5 in the supplementary document. \* Statistical significance =p\<0.10.

\*\* Statistical significance =p\<0.05.

\*\*\* Statistical significance =p\<0.01.

variables, as detailed in Table 3, the linear results for market capitalization persisted. For trading volume, only the largest coins (Q4) continued to show a significantly lower probability of being pumped compared to the smallest coins (Q1).

As for CoinGecko scores, some are significant in explaining which cryptocurrencies are more likely to be pumped. Cryptocurrencies with higher social media activity (ComScore) and more developer activity (DevScore) are more likely to be pumped, ceteris paribus. Manipulators may find coins with more online engagement easier to hype. These results are consistent with Li et al. (2021) but challenge Nghiem et al. (2021), who found social media data ineffective in predicting which coins would be pumped.

For NumExch, the results show that cryptocurrencies listed on fewer exchanges are more likely to be targets of pump-and-dump schemes. Manipulators may avoid coins where price increases can be arbitraged away through other exchanges. If the price rises

### L. Charfeddine and A. Mahrous

**Table 4**

Market-based factors regression results.

<table><tr><th></th><th>Monthly</th><th></th><th>Weekly</th><th>Daily</th><th></th></tr><tr><th></th><th>Without TE</th><th>With TE</th><th>Without TE</th><th>Without TE</th><th>With TE</th></tr><tr><td>BTCRet</td><td>2.78**</td><td>2.56**</td><td>2.17**</td><td>−0.30</td><td>−0.18</td></tr><tr><td></td><td>(2.44)</td><td>(2.01)</td><td>(2.22)</td><td>(−0.89)</td><td>(−0.53)</td></tr><tr><td>BTCVar</td><td>2.63**</td><td>3.22***</td><td>1.01***</td><td>1.13**</td><td>1.45***</td></tr><tr><td></td><td>(2.07)</td><td>(2.97)</td><td>(3.53)</td><td>(2.31)</td><td>(2.96)</td></tr><tr><td>UMCSent</td><td>14.92**</td><td>13.69**</td><td>–</td><td>–</td><td>–</td></tr><tr><td></td><td>(2.35)</td><td>(2.30)</td><td></td><td></td><td></td></tr><tr><td>AltSent</td><td>1.85</td><td>1.32</td><td>0.31</td><td>0.05</td><td>0.05</td></tr><tr><td></td><td>(0.86)</td><td>(0.61)</td><td>(0.86)</td><td>(1.38)</td><td>(1.45)</td></tr><tr><td>VIX</td><td>–</td><td>–</td><td>0.65</td><td>0.16***</td><td>0.15***</td></tr><tr><td></td><td></td><td></td><td>(1.13)</td><td>(3.38)</td><td>(3.20)</td></tr><tr><td>EPU</td><td>11.36***</td><td>14.30***</td><td>–</td><td>0.10***</td><td>0.05</td></tr><tr><td></td><td>(3.17)</td><td>(4.59)</td><td></td><td>(2.68)</td><td>(1.45)</td></tr><tr><td>Inflation</td><td>4.58</td><td>4.50</td><td>–</td><td>−0.28***</td><td>−0.30***</td></tr><tr><td></td><td>(1.01)</td><td>(1.31)</td><td></td><td>(−3.60)</td><td>(−4.02)</td></tr><tr><td>Interest</td><td>–</td><td>–</td><td>0.09</td><td>0.12**</td><td>0.07</td></tr><tr><td></td><td></td><td></td><td>(0.19)</td><td>(2.04)</td><td>(1.24)</td></tr><tr><td>COVID19</td><td>8.47**</td><td>3.78</td><td>1.54**</td><td>−0.04</td><td>−0.01</td></tr><tr><td></td><td>(2.42)</td><td>(0.81)</td><td>(2.21)</td><td>(−0.51)</td><td>(−0.20)</td></tr><tr><td>PoissonGOF</td><td>0.00***</td><td></td><td>0.00***</td><td>0.22</td><td></td></tr><tr><td>Cameron &amp; Trivedi</td><td>0.02**</td><td></td><td>0.04**</td><td>0.35</td><td></td></tr><tr><td>ZeroesPropZTest</td><td>0.51</td><td></td><td>0.06*</td><td>0.36</td><td></td></tr></table>

This table presents the regression results of market-based factors on the number of pumps. Factors include Bitcoin Return (BTCRet), Bitcoin Variance (BTCVar), Consumer Sentiment (UMCSent), Crypto Fear & Greed Index (AltSent), Volatility Index (VIX), Economic Policy Uncertainty (EPU), Inflation, Interest Rate, and COVID-19 dummy. Marginal effects are shown without and with time-effects (TE), with Z-statistics in parentheses. Complete results with time-effect variables are in the supplementary document (Table 8). January (5.94\*\*), March (4.38\*), April (5.62\*\*), June (3.12\*), and August (6.08\*\*) positively affect pump frequency, while November (−3.43\*) has a negative effect. Sunday (0.22\*\*\*) positively affects pump frequency compared to other days. Robustness tests include Poisson Goodness of Fit (PoissonGOF), Cameron & Trivedi test, and proportion of zeros Z-test. \* Statistical significance =p\<0.10. \*\* Statistical significance =p\<0.05. \*\*\* Statistical significance =p\<0.01.

on only one exchange, arbitrageurs can buy from other exchanges and sell on the pumped exchange, putting downward pressure on the price, counteracting the pump.

For the age of a coin (Age), older cryptocurrencies are more likely to be targeted for pumps. Older coins may attract more attention from manipulators.

Some variables were not significant. Circulating supply (CSupply) is unsurprisingly not significant, as it is an arbitrary number set by the coin developers. Public Interest Score (PubScore), based on website and search engine popularity, is also not significant. Similarly, Liquidity Score (LiqScore) is not significant.<sup>4</sup>

#### *3.2.2. Market-based factors results*

Table 4 presents the relationship between market-based factors and the frequency of pre-announced pump-and-dump schemes. The Poisson Goodness of Fit (GOF) test confirmed a Poisson distribution for daily data. However, for monthly and weekly data, the Cameron & Trivedi test identified overdispersion, leading us to use negative binomial regression models. Despite 69% zero occurrences in the daily data, a proportion z-test indicated the number of zeros does not exceed the expected amount in a Poisson distribution, eliminating the need for zero-inflated models.

As Bitcoin return (BTCRet) increases, the number of pumps rises for both monthly and weekly data. Higher Bitcoin volatility (BTCVar) is associated with more pumps across all frequencies.

The consumer sentiment index (UMCSent) positively correlates with the number of pumps monthly. However, the cryptocurrency sentiment index (AltSent) is not significant at any frequency.

Both the VIX index (market volatility proxy) and the Economic Policy Uncertainty (EPU) Index show a significant positive relationship with the number of pump-and-dump schemes in monthly and daily data. Increased volatility and uncertainty may foster speculation, facilitating these schemes.

For daily data, the inflation rate shows a significant negative relationship with pump-and-dump schemes, while the interest rate shows a significant positive relationship. This suggests that differing economic conditions, reflected in inflation and interest rates, influence market the prevalence of market manipulation.

> 4 Liquidity Score is not perfectly correlated with trading volume, as CoinGecko uses a sophisticated calculation method.

### L. Charfeddine and A. Mahrous

The monthly and weekly models show some evidence that pump frequency increased during the first two months after COVID-19 lockdowns. While this increase might not be clear from econometric models, it is evident in the preliminary analysis in Figure 3 in the supplementary document. This rise is expected due to the surge in online activity, retail investor participation, and economic uncertainty (Ortmann et al., 2020; Akhtaruzzaman et al., 2021). Note that crises can affect different markets differently (Boubaker et al., 2022).

Time-effects show that different months have varying numbers of pumps compared to December. Sundays tend to have the highest number of pumps, likely because it is a weekend in many countries.

Since our research on market-based factors in pump-and-dump schemes is novel, direct comparisons with existing literature are limited. The closest study is by Dhawan and Putnin, š (2023), who found that higher levels in a cryptocurrency gambling index correlate with more pump-and-dump schemes. This supports our hypothesis that increased speculation due to market volatility and uncertainty increases pump activity.

### **4. Conclusion and policy implications**

This study empirically analyzes the drivers behind pre-announced pump-and-dump schemes in the cryptocurrency market, focusing on coin-specific and market-wide factors. Results indicate that smaller cryptocurrencies with higher social media and development activity and fewer exchange listings are more susceptible to manipulation. Such schemes are more frequent during periods of higher BTC returns and volatility, increased economic/market uncertainty, and lower inflation/interest rates. Additionally, Sunday sees the most pumps, and certain months experience more/fewer pumps.

The findings enhance the understanding of cryptocurrency market dynamics, informing regulatory actions and investor strategies. Regulators and exchanges should focus on smaller cryptocurrencies with high social media and GitHub activity, especially during volatile markets and on Sundays. Investors can use these insights to avoid pump-and-dump schemes. The increase in market manipulation during COVID-19 warrants attention.

To mitigate these schemes, regulators, exchanges, and social media platforms should use advanced tools to track suspicious activities. Regulators should collaborate with exchanges and platforms to penalize accounts and identify individuals for legal action, possibly requiring cross-border cooperation. Robust Know Your Customer procedures are essential. Service providers can offer investors alerts and educational resources. Investors should report suspicious activities to authorities.

Despite insightful findings, this study has limitations. It focuses on manipulations by Telegram groups targeting cryptocurrencies on Binance. While most pre-announced pumps are organized on these platforms, the findings may not fully apply to smaller exchanges or other manipulation types. The dataset also likely misses unannounced or unreported pump-and-dump events. Additionally, the dynamic nature of the cryptocurrency market means influencing factors may evolve, necessitating continuous research.

Future research could analyze unannounced pumps, manipulation-related social media posts, less-studied manipulation types or asset classes, and factors determining manipulation impact. As the cryptocurrency market evolves, this paper aids in safeguarding its integrity.

### **CRediT authorship contribution statement**

**Lanouar Charfeddine:** Writing – review & editing, Writing – original draft, Visualization, Validation, Supervision, Software, Project administration, Methodology, Investigation, Formal analysis, Conceptualization. **Ahmed Mahrous:** Writing – review & editing, Writing – original draft, Software, Methodology, Investigation, Formal analysis, Data curation, Conceptualization.

### **Declaration of competing interest**

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

### **Data availability**

Data will be made available on request.

### **Appendix A. Supplementary data**

Supplementary material related to this article can be found online at https://doi.org/10.1016/j.frl.2024.105861.

### L. Charfeddine and A. Mahrous

### **References**

 
- Akhtaruzzaman, M., Boubaker, S., Sensoy, A., 2021. Financial contagion during COVID–19 crisis. Finance Res. Lett. 38, 101604.

- Boubaker, S., Goodell, J.W., Kumar, S., Sureka, R., 2023. COVID-19 and finance scholarship: A systematic and bibliometric analysis. Int. Rev. Financ. Anal. 85, 102458.

- Boubaker, S., Goodell, J.W., Pandey, D.K., Kumari, V., 2022. Heterogeneous impacts of wars on global equity markets: Evidence from the invasion of Ukraine. Finance Res. Lett. 48, 102934.

- Canh, N.P., Wongchoti, U., Thanh, S.D., Thong, N.T., 2019. Systematic risk in cryptocurrency market: Evidence from DCC-MGARCH model. Finance Res. Lett. 29, 90–100.

- Dhawan, A., Putnin, š, T.J., 2023. A new wolf in town? Pump-and-dump manipulation in cryptocurrency markets. Rev. Finance 27 (3), 935–975.

- Hamrick, J., Rouhi, F., Mukherjee, A., Feder, A., Gandal, N., Moore, T., Vasek, M., 2021. An examination of the cryptocurrency pump-and-dump ecosystem. Inf. Process. Manage. 58 (4), 102506.

- Hu, S., Zhang, Z., Lu, S., He, B., Li, Z., 2023. Sequence-based target coin prediction for cryptocurrency pump-and-dump. Proc. ACM Manag. Data 1 (1), 1–19.

Kurka, J., 2019. Do cryptocurrencies and traditional asset classes influence each other? Finance Res. Lett. 31, 38–46.

 
- La Morgia, M., Mei, A., Sassi, F., Stefa, J., 2020. Pump and dumps in the bitcoin era: Real time detection of cryptocurrency market manipulations. In: 2020 29th International Conference on Computer Communications and Networks. ICCCN, IEEE, pp. 1–9.

- Li, T., Shin, D., Wang, B., 2021. Cryptocurrency pump-and-dump schemes. Available at SSRN 3267041.

- Maouchi, Y., Charfeddine, L., El Montasser, G., 2022. Understanding digital bubbles amidst the COVID-19 pandemic: Evidence from DeFi and NFTs. Finance Res. Lett. 47, 102584. http://dx.doi.org/10.1016/j.frl.2021.102584, URL https://www.sciencedirect.com/science/article/pii/S1544612321005341.

- Montasser, G.E., Charfeddine, L., Benhamed, A., 2022. COVID-19, cryptocurrencies bubbles and digital market efficiency: sensitivity and similarity analysis. Finance Res. Lett. 46, 102362. http://dx.doi.org/10.1016/j.frl.2021.102362, URL https://www.sciencedirect.com/science/article/pii/S1544612321003652.

- Nghiem, H., Muric, G., Morstatter, F., Ferrara, E., 2021. Detecting cryptocurrency pump-and-dump frauds using market and social signals. Expert Syst. Appl. 182, 115284.

- Ortmann, R., Pelster, M., Wengerek, S.T., 2020. COVID-19 and investor behavior. Finance Res. Lett. 37, 101717.

- Tsuchiya, T., 2021. Profitability of cryptocurrency pump and dump schemes. Dig. Finance 3 (2), 149–167.

- Victor, F., Hagemann, T., 2019. Cryptocurrency pump and dump schemes: Quantification and detection. In: 2019 International Conference on Data Mining Workshops. ICDMW, IEEE, pp. 244–251.

- Yue, Y., Li, X., Zhang, D., Wang, S., 2021. How cryptocurrency affects economy? A network analysis using bibliometric methods. Int. Rev. Financ. Anal. 77, 101869.

Last updated: October 2026.
