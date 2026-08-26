# macro_eft_timing
This is a side project in which I aim to learn about financial markets by creating models to predict future financial conditions. I download a wide array of publically available financial data and use that to train models to predict future values of GDP and ETFs such as QQQ. I also design a buy/sell strategy for these ETFs using predicted future values and compare the results to a simple buy-and-hold strategy.

This project is broken down into 4 notebooks:
1) Data Collection
2) Exploratory Data Analysis
3) Feature Engineering
4) Model Creation and Analysis


## Part 1: Data Collection and Pre-processing

The work relating to this section can be found in notebooks/01_data_collection.ipynb.

The goal for this notebook is to load financial data from FRED (Federal Reserve Bank of St. Louis) and Yahoo Finance which is later used to train models that predict future market health. See [DATA.md](DATA.md) for a description of each pulled feature and why it was chosen.

The data is also pre-processed, meaning that data is aligned, sampling frequencies matched and features adjusted to better represent what is known about these features for a given date. Specifics of the pre-processing is described in the notebook.

## Part 2: Exploratory Data Analysis

The work relating to this section can be found in notebooks/02_eda_macro_health.ipynb.

With the data loaded, synced, merged and shiften, I next set out to explore the data to determine what forms it takes (what are trends present? how does the data change during large economic events?) I also create a correlation matrix to gauge how much variability there is in the data and whether some set of features provide the same information.

## Part 3: Feature Engineering

The work relating to this section can be found in notebooks/03_feature_engineering.ipynb.

Here I perform feature engineering, using the variables collected in part 1 to create valid inputs for predictive models created in part 4. This involves transforming the variables so that outliers are don't dominate models and removing trends so that future values are interprettable by the models. The variables are also regularized (z-score) so that their values are all of roughly the same magnitude which makes training the models easier. 

## Part 4: Model Creation and Analysis

The work relating to this section can be found in notebooks/04_model_and_signals.ipynb.

Models are trained using a walk-forward cross-validation method to predict future GDP and QQQ values. Four models are trained: ridge, random_forest, xgboost, and lightgbm. Model accuracy is determined using root mean squared error and correlation between predictions and actual values. A simple buy-and-sell method is created to determine if model predictions can be used to outcompete the simpler buy-and-hold stock-purchasing method.

## Conclusion

Here I set out to see whether publicly available macroeconomic and market data could be used to predict GDP and QQQ movements. In addition, predictions on QQQ movements were tested to see if they could be used to beat a simple buy-and-hold strategy. The results mostly confirm the efficient market hypothesis with the models modestly beating a "predict the training mean" baseline for near-term GDP and QQQ, but struggled to beat baseline for longer-horizon GDP (12 months) and offered only weak directional signal for QQQ overall. The resulting buy/sell strategy edged out buy-and-hold ($3.99 vs $3.68 on $1 invested over the ~7 year test period), but the margin is small enough, and the underlying model's individual predictive power weak enough, that this difference is more likely due to chance than a real, exploitable edge.

The most useful takeaways were less about the specific outputs and more about the process: time-aware feature engineering (respecting real-world reporting lags to avoid lookahead bias), walk-forward cross-validation for evaluating time series models, and staying skeptical of results that look too good; several early versions of the buy/sell test had bugs that made the strategy look far more impressive than it actually was.

Natural next steps: increasing the sampling frequency (e.g. weekly instead of monthly) for a more statistically meaningful test of the buy/sell strategy, exploring whether GDP predictions could improve QQQ predictions, and implementing PCA exploration in notebook 2 to see if a reduced set of macro factors captures the same signal as the full feature set.