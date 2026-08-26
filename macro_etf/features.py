import numpy as np


# Features with a persistent secular trend -- convert to percent change rather than raw
# level, since the rate of change matters more than the level itself for these.
# Value is the number of months between recordings (real_gdp is quarterly).
PCT_CHANGE_FEATURES = {
    'cpi': 1,
    'retail_sales': 1,
    'm2': 1,
    'close_spy': 1,
    'close_qqq': 1,
    'close_oil': 1,
    'real_gdp': 3,
}

# Non-negative, heavy right-tailed features with rare extreme spikes (mostly COVID-driven) --
# log1p before z-scoring so the outlier months don't dominate a linear model's fit.
LOG_TRANSFORM_FEATURES = [
    'initial_claims',
    'close_vix',
    'volume_spy',
    'volume_qqq',
    'volume_oil',
    'personal_savings_rate',
]


def build_features(df):
    '''
    Apply per-feature transforms ahead of z-scoring:
      - PCT_CHANGE_FEATURES: converted to percent change.
      - LOG_TRANSFORM_FEATURES: log1p transform.
      - everything else: left as a raw level, to be z-scored downstream.
    '''
    X = df.copy()

    for feat, lag in PCT_CHANGE_FEATURES.items():
        X[f'{feat}_percent_change'] = X[feat].pct_change(periods=lag)
        X = X.drop(feat, axis=1)

    for feat in LOG_TRANSFORM_FEATURES:
        X[feat] = np.log1p(X[feat])

    return X


if __name__ == "__main__":
    pass
