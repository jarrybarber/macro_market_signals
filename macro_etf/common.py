from pathlib import Path

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