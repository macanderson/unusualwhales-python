# Stocks

Types:

```python
from unusualwhales.types import StockRetrieveResponse
```

Methods:

- <code title="get /stocks/price/{symbol}">client.stocks.<a href="./src/unusualwhales/resources/stocks/stocks.py">retrieve</a>(symbol) -> <a href="./src/unusualwhales/types/stock_retrieve_response.py">StockRetrieveResponse</a></code>

## Screener

Types:

```python
from unusualwhales.types.stocks import ScreenerGetResponse, ScreenerPostResponse
```

Methods:

- <code title="get /stocks/screener">client.stocks.screener.<a href="./src/unusualwhales/resources/stocks/screener.py">get</a>(\*\*<a href="src/unusualwhales/types/stocks/screener_get_params.py">params</a>) -> <a href="./src/unusualwhales/types/stocks/screener_get_response.py">ScreenerGetResponse</a></code>
- <code title="post /stocks/screener">client.stocks.screener.<a href="./src/unusualwhales/resources/stocks/screener.py">post</a>(\*\*<a href="src/unusualwhales/types/stocks/screener_post_params.py">params</a>) -> <a href="./src/unusualwhales/types/stocks/screener_post_response.py">ScreenerPostResponse</a></code>

## News

Types:

```python
from unusualwhales.types.stocks import NewsListResponse
```

Methods:

- <code title="get /news">client.stocks.news.<a href="./src/unusualwhales/resources/stocks/news.py">list</a>(\*\*<a href="src/unusualwhales/types/stocks/news_list_params.py">params</a>) -> <a href="./src/unusualwhales/types/stocks/news_list_response.py">NewsListResponse</a></code>

## Quote

Types:

```python
from unusualwhales.types.stocks import QuoteRetrieveResponse
```

Methods:

- <code title="get /stocks/quote/{symbol}">client.stocks.quote.<a href="./src/unusualwhales/resources/stocks/quote.py">retrieve</a>(symbol) -> <a href="./src/unusualwhales/types/stocks/quote_retrieve_response.py">QuoteRetrieveResponse</a></code>

## Historical

Types:

```python
from unusualwhales.types.stocks import HistoricalRetrieveResponse
```

Methods:

- <code title="get /stocks/historical/{symbol}">client.stocks.historical.<a href="./src/unusualwhales/resources/stocks/historical.py">retrieve</a>(symbol, \*\*<a href="src/unusualwhales/types/stocks/historical_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/stocks/historical_retrieve_response.py">HistoricalRetrieveResponse</a></code>

## Company

Types:

```python
from unusualwhales.types.stocks import CompanyRetrieveResponse
```

Methods:

- <code title="get /stocks/company/{symbol}">client.stocks.company.<a href="./src/unusualwhales/resources/stocks/company.py">retrieve</a>(symbol) -> <a href="./src/unusualwhales/types/stocks/company_retrieve_response.py">CompanyRetrieveResponse</a></code>

## Financials

Types:

```python
from unusualwhales.types.stocks import FinancialRetrieveResponse
```

Methods:

- <code title="get /stocks/financials/{symbol}">client.stocks.financials.<a href="./src/unusualwhales/resources/stocks/financials.py">retrieve</a>(symbol, \*\*<a href="src/unusualwhales/types/stocks/financial_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/stocks/financial_retrieve_response.py">FinancialRetrieveResponse</a></code>

## Earnings

Types:

```python
from unusualwhales.types.stocks import EarningRetrieveResponse
```

Methods:

- <code title="get /stocks/earnings/{symbol}">client.stocks.earnings.<a href="./src/unusualwhales/resources/stocks/earnings.py">retrieve</a>(symbol) -> <a href="./src/unusualwhales/types/stocks/earning_retrieve_response.py">EarningRetrieveResponse</a></code>

## Dividends

Types:

```python
from unusualwhales.types.stocks import DividendRetrieveResponse
```

Methods:

- <code title="get /stocks/dividends/{symbol}">client.stocks.dividends.<a href="./src/unusualwhales/resources/stocks/dividends.py">retrieve</a>(symbol, \*\*<a href="src/unusualwhales/types/stocks/dividend_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/stocks/dividend_retrieve_response.py">DividendRetrieveResponse</a></code>

# Congress

## Trades

Types:

```python
from unusualwhales.types.congress import TradeListResponse
```

Methods:

- <code title="get /congress/trades">client.congress.trades.<a href="./src/unusualwhales/resources/congress/trades.py">list</a>(\*\*<a href="src/unusualwhales/types/congress/trade_list_params.py">params</a>) -> <a href="./src/unusualwhales/types/congress/trade_list_response.py">TradeListResponse</a></code>

## Members

Types:

```python
from unusualwhales.types.congress import MemberListResponse
```

Methods:

- <code title="get /congress/members">client.congress.members.<a href="./src/unusualwhales/resources/congress/members.py">list</a>() -> <a href="./src/unusualwhales/types/congress/member_list_response.py">MemberListResponse</a></code>

# Institutions

Types:

```python
from unusualwhales.types import InstitutionListResponse
```

Methods:

- <code title="get /institutions/list">client.institutions.<a href="./src/unusualwhales/resources/institutions/institutions.py">list</a>() -> <a href="./src/unusualwhales/types/institution_list_response.py">InstitutionListResponse</a></code>

## Trades

Types:

```python
from unusualwhales.types.institutions import TradeListResponse
```

Methods:

- <code title="get /institutions/trades">client.institutions.trades.<a href="./src/unusualwhales/resources/institutions/trades.py">list</a>(\*\*<a href="src/unusualwhales/types/institutions/trade_list_params.py">params</a>) -> <a href="./src/unusualwhales/types/institutions/trade_list_response.py">TradeListResponse</a></code>

## Activity

Types:

```python
from unusualwhales.types.institutions import ActivityRetrieveResponse
```

Methods:

- <code title="get /institutional/activity">client.institutions.activity.<a href="./src/unusualwhales/resources/institutions/activity.py">retrieve</a>(\*\*<a href="src/unusualwhales/types/institutions/activity_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/institutions/activity_retrieve_response.py">ActivityRetrieveResponse</a></code>

# Darkpool

## Transactions

Types:

```python
from unusualwhales.types.darkpool import TransactionRetrieveResponse, TransactionListResponse
```

Methods:

- <code title="get /darkpool/transactions/{symbol}">client.darkpool.transactions.<a href="./src/unusualwhales/resources/darkpool/transactions.py">retrieve</a>(symbol, \*\*<a href="src/unusualwhales/types/darkpool/transaction_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/darkpool/transaction_retrieve_response.py">TransactionRetrieveResponse</a></code>
- <code title="get /darkpool/transactions">client.darkpool.transactions.<a href="./src/unusualwhales/resources/darkpool/transactions.py">list</a>(\*\*<a href="src/unusualwhales/types/darkpool/transaction_list_params.py">params</a>) -> <a href="./src/unusualwhales/types/darkpool/transaction_list_response.py">TransactionListResponse</a></code>

# Etf

Types:

```python
from unusualwhales.types import EtfListResponse
```

Methods:

- <code title="get /etf/list">client.etf.<a href="./src/unusualwhales/resources/etf/etf.py">list</a>() -> <a href="./src/unusualwhales/types/etf_list_response.py">EtfListResponse</a></code>

## Holdings

Types:

```python
from unusualwhales.types.etf import HoldingListResponse
```

Methods:

- <code title="get /etf/holdings">client.etf.holdings.<a href="./src/unusualwhales/resources/etf/holdings.py">list</a>(\*\*<a href="src/unusualwhales/types/etf/holding_list_params.py">params</a>) -> <a href="./src/unusualwhales/types/etf/holding_list_response.py">HoldingListResponse</a></code>

## Tide

Types:

```python
from unusualwhales.types.etf import TideRetrieveResponse
```

Methods:

- <code title="get /etf/tide">client.etf.tide.<a href="./src/unusualwhales/resources/etf/tide.py">retrieve</a>(\*\*<a href="src/unusualwhales/types/etf/tide_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/etf/tide_retrieve_response.py">TideRetrieveResponse</a></code>

## Sectors

Types:

```python
from unusualwhales.types.etf import SectorRetrieveResponse, SectorListResponse
```

Methods:

- <code title="get /etf/sectors">client.etf.sectors.<a href="./src/unusualwhales/resources/etf/sectors.py">retrieve</a>(\*\*<a href="src/unusualwhales/types/etf/sector_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/etf/sector_retrieve_response.py">SectorRetrieveResponse</a></code>
- <code title="get /etf/sectors/list">client.etf.sectors.<a href="./src/unusualwhales/resources/etf/sectors.py">list</a>() -> <a href="./src/unusualwhales/types/etf/sector_list_response.py">SectorListResponse</a></code>

# OptionsFlows

Types:

```python
from unusualwhales.types import OptionsFlowRetrieveResponse, OptionsFlowListResponse
```

Methods:

- <code title="get /options/flow/{symbol}">client.options_flows.<a href="./src/unusualwhales/resources/options_flows/options_flows.py">retrieve</a>(symbol, \*\*<a href="src/unusualwhales/types/options_flow_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/options_flow_retrieve_response.py">OptionsFlowRetrieveResponse</a></code>
- <code title="get /options/flow">client.options_flows.<a href="./src/unusualwhales/resources/options_flows/options_flows.py">list</a>(\*\*<a href="src/unusualwhales/types/options_flow_list_params.py">params</a>) -> <a href="./src/unusualwhales/types/options_flow_list_response.py">OptionsFlowListResponse</a></code>

## Chain

Types:

```python
from unusualwhales.types.options_flows import ChainRetrieveResponse
```

Methods:

- <code title="get /options/chain/{symbol}">client.options_flows.chain.<a href="./src/unusualwhales/resources/options_flows/chain.py">retrieve</a>(symbol, \*\*<a href="src/unusualwhales/types/options_flows/chain_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/options_flows/chain_retrieve_response.py">ChainRetrieveResponse</a></code>

## Expirations

Types:

```python
from unusualwhales.types.options_flows import ExpirationRetrieveResponse
```

Methods:

- <code title="get /options/expirations/{symbol}">client.options_flows.expirations.<a href="./src/unusualwhales/resources/options_flows/expirations.py">retrieve</a>(symbol) -> <a href="./src/unusualwhales/types/options_flows/expiration_retrieve_response.py">ExpirationRetrieveResponse</a></code>

## Greeks

Types:

```python
from unusualwhales.types.options_flows import GreekRetrieveResponse
```

Methods:

- <code title="get /options/greeks/{symbol}">client.options_flows.greeks.<a href="./src/unusualwhales/resources/options_flows/greeks.py">retrieve</a>(symbol, \*\*<a href="src/unusualwhales/types/options_flows/greek_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/options_flows/greek_retrieve_response.py">GreekRetrieveResponse</a></code>

## Historical

Types:

```python
from unusualwhales.types.options_flows import HistoricalRetrieveResponse
```

Methods:

- <code title="get /options/historical/{symbol}">client.options_flows.historical.<a href="./src/unusualwhales/resources/options_flows/historical.py">retrieve</a>(symbol, \*\*<a href="src/unusualwhales/types/options_flows/historical_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/options_flows/historical_retrieve_response.py">HistoricalRetrieveResponse</a></code>

## GreeksFlow

Types:

```python
from unusualwhales.types.options_flows import GreeksFlowRetrieveResponse
```

Methods:

- <code title="get /options/greekflow">client.options_flows.greeks_flow.<a href="./src/unusualwhales/resources/options_flows/greeks_flow.py">retrieve</a>(\*\*<a href="src/unusualwhales/types/options_flows/greeks_flow_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/options_flows/greeks_flow_retrieve_response.py">GreeksFlowRetrieveResponse</a></code>

## GreeksFlowExpiry

Types:

```python
from unusualwhales.types.options_flows import GreeksFlowExpiryRetrieveResponse
```

Methods:

- <code title="get /options/greekflow/expiry">client.options_flows.greeks_flow_expiry.<a href="./src/unusualwhales/resources/options_flows/greeks_flow_expiry.py">retrieve</a>(\*\*<a href="src/unusualwhales/types/options_flows/greeks_flow_expiry_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/options_flows/greeks_flow_expiry_retrieve_response.py">GreeksFlowExpiryRetrieveResponse</a></code>

## OiChange

Types:

```python
from unusualwhales.types.options_flows import OiChangeRetrieveResponse
```

Methods:

- <code title="get /options/oi_change/{symbol}">client.options_flows.oi_change.<a href="./src/unusualwhales/resources/options_flows/oi_change.py">retrieve</a>(symbol, \*\*<a href="src/unusualwhales/types/options_flows/oi_change_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/options_flows/oi_change_retrieve_response.py">OiChangeRetrieveResponse</a></code>

## TotalVolume

Types:

```python
from unusualwhales.types.options_flows import TotalVolumeRetrieveResponse
```

Methods:

- <code title="get /options/total_volume">client.options_flows.total_volume.<a href="./src/unusualwhales/resources/options_flows/total_volume.py">retrieve</a>(\*\*<a href="src/unusualwhales/types/options_flows/total_volume_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/options_flows/total_volume_retrieve_response.py">TotalVolumeRetrieveResponse</a></code>

## Contract

Types:

```python
from unusualwhales.types.options_flows import ContractRetrieveResponse
```

Methods:

- <code title="get /options/contract/{optionSymbol}">client.options_flows.contract.<a href="./src/unusualwhales/resources/options_flows/contract.py">retrieve</a>(option_symbol) -> <a href="./src/unusualwhales/types/options_flows/contract_retrieve_response.py">ContractRetrieveResponse</a></code>

# Seasonality

## Stocks

Types:

```python
from unusualwhales.types.seasonality import StockRetrieveResponse
```

Methods:

- <code title="get /seasonality/stocks/{symbol}">client.seasonality.stocks.<a href="./src/unusualwhales/resources/seasonality/stocks.py">retrieve</a>(symbol, \*\*<a href="src/unusualwhales/types/seasonality/stock_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/seasonality/stock_retrieve_response.py">StockRetrieveResponse</a></code>

# InsiderTrades

Types:

```python
from unusualwhales.types import InsiderTradeListResponse
```

Methods:

- <code title="get /insider/trades">client.insider_trades.<a href="./src/unusualwhales/resources/insider_trades.py">list</a>(\*\*<a href="src/unusualwhales/types/insider_trade_list_params.py">params</a>) -> <a href="./src/unusualwhales/types/insider_trade_list_response.py">InsiderTradeListResponse</a></code>

# Spike

## Detection

Types:

```python
from unusualwhales.types.spike import DetectionListResponse
```

Methods:

- <code title="get /spike/detection">client.spike.detection.<a href="./src/unusualwhales/resources/spike/detection.py">list</a>(\*\*<a href="src/unusualwhales/types/spike/detection_list_params.py">params</a>) -> <a href="./src/unusualwhales/types/spike/detection_list_response.py">DetectionListResponse</a></code>

# Calendar

## Economic

Types:

```python
from unusualwhales.types.calendar import EconomicRetrieveResponse
```

Methods:

- <code title="get /calendar/economic">client.calendar.economic.<a href="./src/unusualwhales/resources/calendar/economic.py">retrieve</a>(\*\*<a href="src/unusualwhales/types/calendar/economic_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/calendar/economic_retrieve_response.py">EconomicRetrieveResponse</a></code>

## Fda

Types:

```python
from unusualwhales.types.calendar import FdaRetrieveResponse
```

Methods:

- <code title="get /calendar/fda">client.calendar.fda.<a href="./src/unusualwhales/resources/calendar/fda.py">retrieve</a>(\*\*<a href="src/unusualwhales/types/calendar/fda_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/calendar/fda_retrieve_response.py">FdaRetrieveResponse</a></code>

# Correlations

Types:

```python
from unusualwhales.types import CorrelationListResponse
```

Methods:

- <code title="get /correlations">client.correlations.<a href="./src/unusualwhales/resources/correlations.py">list</a>(\*\*<a href="src/unusualwhales/types/correlation_list_params.py">params</a>) -> <a href="./src/unusualwhales/types/correlation_list_response.py">CorrelationListResponse</a></code>

# Analyst

## Ratings

Types:

```python
from unusualwhales.types.analyst import RatingRetrieveResponse
```

Methods:

- <code title="get /analyst/ratings/{symbol}">client.analyst.ratings.<a href="./src/unusualwhales/resources/analyst/ratings.py">retrieve</a>(symbol, \*\*<a href="src/unusualwhales/types/analyst/rating_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/analyst/rating_retrieve_response.py">RatingRetrieveResponse</a></code>

## UpgradesDowngrades

Types:

```python
from unusualwhales.types.analyst import UpgradesDowngradeListResponse
```

Methods:

- <code title="get /analyst/upgrades_downgrades">client.analyst.upgrades_downgrades.<a href="./src/unusualwhales/resources/analyst/upgrades_downgrades.py">list</a>(\*\*<a href="src/unusualwhales/types/analyst/upgrades_downgrade_list_params.py">params</a>) -> <a href="./src/unusualwhales/types/analyst/upgrades_downgrade_list_response.py">UpgradesDowngradeListResponse</a></code>

# Market

## Overview

Types:

```python
from unusualwhales.types.market import OverviewRetrieveResponse
```

Methods:

- <code title="get /market/overview">client.market.overview.<a href="./src/unusualwhales/resources/market/overview.py">retrieve</a>() -> <a href="./src/unusualwhales/types/market/overview_retrieve_response.py">OverviewRetrieveResponse</a></code>

## Indices

Types:

```python
from unusualwhales.types.market import IndexListResponse
```

Methods:

- <code title="get /market/indices">client.market.indices.<a href="./src/unusualwhales/resources/market/indices.py">list</a>() -> <a href="./src/unusualwhales/types/market/index_list_response.py">IndexListResponse</a></code>

## Movers

Types:

```python
from unusualwhales.types.market import MoverListResponse
```

Methods:

- <code title="get /market/movers">client.market.movers.<a href="./src/unusualwhales/resources/market/movers.py">list</a>(\*\*<a href="src/unusualwhales/types/market/mover_list_params.py">params</a>) -> <a href="./src/unusualwhales/types/market/mover_list_response.py">MoverListResponse</a></code>

## Sectors

Types:

```python
from unusualwhales.types.market import SectorListResponse
```

Methods:

- <code title="get /market/sectors">client.market.sectors.<a href="./src/unusualwhales/resources/market/sectors.py">list</a>(\*\*<a href="src/unusualwhales/types/market/sector_list_params.py">params</a>) -> <a href="./src/unusualwhales/types/market/sector_list_response.py">SectorListResponse</a></code>

## News

Types:

```python
from unusualwhales.types.market import NewsListResponse
```

Methods:

- <code title="get /market/news">client.market.news.<a href="./src/unusualwhales/resources/market/news.py">list</a>(\*\*<a href="src/unusualwhales/types/market/news_list_params.py">params</a>) -> <a href="./src/unusualwhales/types/market/news_list_response.py">NewsListResponse</a></code>

# Options

## Contracts

Types:

```python
from unusualwhales.types.options import ContractListResponse
```

Methods:

- <code title="get /options/contracts">client.options.contracts.<a href="./src/unusualwhales/resources/options/contracts.py">list</a>(\*\*<a href="src/unusualwhales/types/options/contract_list_params.py">params</a>) -> <a href="./src/unusualwhales/types/options/contract_list_response.py">ContractListResponse</a></code>
