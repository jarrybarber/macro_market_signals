# Data Dictionary

Descriptions of every feature pulled from FRED (Federal Reserve Bank of St. Louis) and Yahoo
Finance, and why each one was chosen. Sourced and pre-processed in
`notebooks/01_data_collection.ipynb`; the field names below match the features produced there.

## FRED Data

**cpi**: Consumer Price Index. A measure of inflation that tracks how the basic cost of goods and services changes over time. This works by tracking a *basket* of goods (e.g., food, gas, housing, healthcare, etc) over time and determining the cost of such a basket. There are multiple ways that baskets are defined, and thus multiple forms of CPI.

**unemployment**: The percentage of people who actively want to work but currently aren't, typically due to a job shortage or low wages.

**yield_spread**: The difference in the interest rate between a 10 year US treasury bond and a 2 year bond. Typically the yield of a 10 year bond is higher than that of a 2 year bond, since money is being committed for a longer term. If the economy starts to falter and investors lose confidence in its near-term health then they will sell their short term bonds (2 year) and buy long term bonds (10 year) which causes the price of short term bonds to decrease and long term bonds to increase. During times of extreme economic chaos the yield_spread can become negative, meaning the effective interest of the 2 year bond is higher than the 10 year bond. This yield spread inversion has preceeded every US recession since 1970, making it a useful predictor of market health. Note that there hasn't been a recession every single time this inversion has occurred.

**fed_funds_rate**: The interest rate at which banks lend money to each other overnight. The Fed increases this to reduce inflation when the economy is too hot. If this value is increasing over time then the Fed is actively trying to slow the economy down. If this goes up then it becomes more expensive to borrow money and so becomes more difficult for companies to grow. Also, any business that has large loans will have to start making larger interest payments which means they will have less capital for growth.

**credit_spread**: The difference in yield between a corporate bond and a US treasury bond. A US bond is considered a very safe investment as it isn't expected to default on its debt. A corporate bond on the other hand is more risky and so investors expect a higher rate of return. If the economy is doing well then investors do not expect corporations to go bust and so are more willing to consider interest rates slightly higher than the US treasury bonds. If the economy is not doing well then investors will demand higher interest rates, which causes the credit_spread to grow. The credit_spread often reacts faster to market conditions than stocks do.

**financial_stress**: This is a composite index that attempts to track overall market stress. This works by taking 18 stress-based indices, performing principal component analysis (PCA) and using the first component as the index. PCA identifies base vectors that describe the greatest amount of variability in a dataset. By taking the first principal component, we are in essence creating a new index that combines the 18 other indices weighted by importance.

**ted_spread (DISCONTINUED)**: the difference between the 3-month LIBOR rate (what banks charge to borrow from each other) and the 3-month US treasury bond yield. This reflects how much the banks no longer trust each other to remain solvent overnight. If this suddenly jumps then banks think there is a high probability that other banks will fail, which is a terrible sign for the economy. It also means that banks are no longer lending to businesses and customers which again negatively influences the economy.

**industrial_production**: a direct measure of how much physical stuff the US economy is generating (mining, manufacturing, utilities). The value is relative to the 2017 value, with values over 100 representing higher output. This is a useful index in that it directly measures physical output and is not dependent on how people are *feeling* about the economy.

**retail_sales**: measures the total dollar value of sales made through US retailers each month. This value makes up ~70% of the US GDP and so is a good measure of how the US economy is doing right now. Note that this is **not** inflation adjustested, meaning that I should adjust it myself to get an accurate picture of overall economic health. Especially important right now as inflation has been relatively high recently.

**leading_indicators (DISCONTINUED)**: this is another composite index built that attempts to predict how well the economy will be doing in 6-12 months from now. It incorporates building permits, jobless claims, stock prices, yield spread, consumer expectations, and others. This may be redundant as I already have many of these indices in my data, but it may serve as a useful comparison index in terms of how well my future model performs.

**real_gdp**: Captures all spending in a country: consumer spending, investments, government spending, net exports. Nominal GDP measures the GDP using the current currency value, while the real GDP uses one reference value for the currency by adjusting for inflation. This is only released quarterly rather than monthly, so I will have to figure out how to deal with that issue in my data/model.

**consumer_sentiment**: A sort of vibe-check on how the average consumer feels about the economy. The value is determined by surveying 500 homes and asking questions such as "Are you better or worse off financially than a year ago?" or "Is now a good time to buy a major household item (car, hot tub)?" If the resulting measure is above 100 then consumers are optimistic, below then pessimistic. This can capture uncertainty in the market due to global events that have not yet had a chance to effect the markets (e.g., Iran war oil crisis).

**housing_starts**: the number of houses or housing units that had started construction in the last month. Housing construction is heavily dependent on interest rates because builders require loans to build the homes and buyers need to get mortgages to pay for them. The number of housing starts generally reacts faster to changes in the Fed rate than other measures. This is because building a house requires months of planning and if the builders lose confidence that there will be demand or that it will be too expensive, they will decrease the number of houses they are building.

**building_permits**: Similar to housing starts, but this number should change even earlier. Building permits are approved near the beginning of a construction project and if there is a dropoff then builders are likely pulling back on the number of houses they are going to build. This is a leading indicator. Likely higher co-linear with housing_starts, may be a good idea to just use one, or to consider the ratio between them as a widening gap could indicate an abrupt housing market slowdown.

**m2**: a measure of total money supply in the economy. How much money exists and is readily available for spending. M1 = total physical cash and money in checkings accounts. M2 = M1 + savings accounts + money market funds + CDs / GICs. If this value increases then there is more money in the economy and so inflation rises. If it decreases then there are deflationary pressures to consider. M2 often increases 1-2 years *before* inflation starts to increase, making it a leading indicator.

**initial_claims**: measures the number of people filing for unemployment claims for the first time each week. This is measured more often than monthly jobs reports, gives a better immediate measure of economic health.

**job_openings**: how much employers want to hire people, rather than the number of people without jobs. Employeers often pull back on hiring before they resort to laying people off and so this is a leading indicator of how employers are feeling about their economic future.

## Yahoo Finance Data

4 tickers available on Yahoo Finance:

**spy**: This is an ETF that aims to follow the S&P 500 exactly. The S&P 500 index is determined by 500 of the largest US companies, weighted by the market-capitalization of each company. This means that the index is very top-heavy, with the 10 ten companies (mostly tech darlings) accounting for roughly 35% of the index's value.

**qqq**: This is an ETF that aims to follow the NASDAQ-100 exactly. Similarly to the S&P 500, the Nasdaq-100 is calculated using 100 of the largest US companies, weighted by their market caps. Key differences include NASDAQ not including the financial sector, the companies must be listed on the NASDAQ exchange, there is no profitability requirement (the S&P 500 has one), and there are limits on the proportion each company can take up of the index. The Nasdaq is significantly more concentrated than the S&P 500, with 40-50% of it being taken up by the top 5-6 companies (generally tech darlings).

**oil**: This is a calculated as the average price of a barrel of oil on the futures market. In this case, the futures market is made up of contracts which specify that someone will buy or sell a specific amount of oil at a given date.

**vix**: VIX is a measure of fear and anxiety in the market. If VIX goes up, there are signals that traders believe the market will deteriorate in the next several months. VIX is calculated using the futures market. If buyers think that prices will fall then they will buy more *puts* to protect their portfolios. If many of these are being purchased then their price will increase. VIX measures that increase and uses it to gauge market sentiment.
