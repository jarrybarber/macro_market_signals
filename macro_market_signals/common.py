from pathlib import Path
import pandas as pd

ROOT_DIR = Path(__file__).parent.parent
RAW_DATA_DIR = ROOT_DIR / 'data' / 'raw'
PROCESSED_DATA_DIR = ROOT_DIR / 'data' / 'processed'


FRED_INDICATORS = {
        # Inflation
        'cpi':                   'CPIAUCSL',
        # Labour Market
        'unemployment':          'UNRATE',
        # Credit & Financial Stress
        'yield_spread':          'T10Y2Y',
        'fed_funds_rate':        'FEDFUNDS',
        'credit_spread':         'BAA10Y',    # Corporate bond spread over treasuries — spikes before recessions
        'financial_stress':      'STLFSI4',   # St. Louis Fed stress index — composite risk gauge
        #'ted_spread':            'TEDRATE',   # (DISCONTINUED) Bank lending risk (LIBOR vs T-bill)
        # Growth & Activity
        'industrial_production': 'INDPRO',   # Real economic output
        'retail_sales':          'RSXFS',    # Consumer spending strength
        # 'leading_indicators':    'USSLIND',  # (DICONTINUED)Conference Board LEI — forward-looking composite
        'real_gdp':              'GDPC1',    # Quarterly, but the gold standard for recession ID 
        'consumer_sentiment':    'UMCSENT',
        # Consumer Health
        'credit_card_delinquency': 'DRCCLACBS',  # stress among lower-income households
        'personal_savings_rate':   'PSAVERT',    # drops when lower/middle income stressed
        # Housing (leading indicator of broader economy)
        'housing_starts':        'HOUST',    # New construction — sensitive to rates
        'building_permits':      'PERMIT',   # Even more forward-looking than starts
        # Money Supply & Liquidity
        'm2':                    'M2SL',     # Money supply — linked to inflation and liquidity
        # Labor Market (beyond unemployment rate)
        'initial_claims':        'ICSA',     # Weekly jobless claims — earliest recession signal
        'job_openings':          'JTSJOL',   # JOLTS — demand side of labor market
    }


TICKERS = {"spy": "SPY", 
           "qqq": "QQQ", 
           "vix": "^VIX", 
           "oil": "CL=F"}

POINTS_OF_INTEREST = pd.to_datetime([
    '2008-09-01',   # Roughly when the subprime mortgage crises occurred, causing banks to collapse and inducing a recession.
    '2020-03-01',   # This was the month when COVID lockdown restrictions hit the western world, resulting in 
                    # mass layoffs, massive government spending, and slowdown in the economy.
    '2022-06-01',   # When the Fed began to increase interest rates to counter inflationary pressures which resulted from
                    # monetary policies meant to ease economic strain during the COVID lockdowns.
    '2026-03-01'    # start of the US-Iran war, resulting in the shutdown of the Strait of Hormuz which restricted the flow
                    # of oil, fertalizers and other economically vital resources. Significant damage was also sustrained by
                    # oil production and shipping infrastructure. 
])

#The target values that my models will try to predict. 
# 'variable' refers to the variable in the dataframe that the target is determined from
# 'date_gap' refers to the number of months between where the target variable is drawn from and the date that the feature are drawn from
#       i.e., if date_gap = 3 then I am trying to predict the target variable's value in 3 months time using today's data.
MODELLING_TARGETS = {
    # Next quarter's GDP
    'gdp_3mo': {'variable': 'real_gdp', 
                'date_gap': 3},
    # GDP in a year from now
    'gdp_12mo':{'variable': 'real_gdp', 
                'date_gap': 12},
    # QQQ in a month from now
    'qqq_1mo': {'variable': 'close_qqq',
                'date_gap': 1},
    # QQQ in three months from now
    'qqq_3mo': {'variable': 'close_qqq',
                'date_gap': 3}
}