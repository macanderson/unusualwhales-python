# OptionsFlows

Types:

```python
from unusualwhales.types import OptionsFlowRetrieveResponse, OptionsFlowListResponse
```

Methods:

- <code title="get /options/flow/{symbol}">client.options_flows.<a href="./src/unusualwhales/resources/options_flows.py">retrieve</a>(symbol, \*\*<a href="src/unusualwhales/types/options_flow_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/options_flow_retrieve_response.py">OptionsFlowRetrieveResponse</a></code>
- <code title="get /options/flow">client.options_flows.<a href="./src/unusualwhales/resources/options_flows.py">list</a>(\*\*<a href="src/unusualwhales/types/options_flow_list_params.py">params</a>) -> <a href="./src/unusualwhales/types/options_flow_list_response.py">OptionsFlowListResponse</a></code>

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

# News

Types:

```python
from unusualwhales.types import NewsListResponse
```

Methods:

- <code title="get /news">client.news.<a href="./src/unusualwhales/resources/news.py">list</a>(\*\*<a href="src/unusualwhales/types/news_list_params.py">params</a>) -> <a href="./src/unusualwhales/types/news_list_response.py">NewsListResponse</a></code>

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

# Options

## Chain

Types:

```python
from unusualwhales.types.options import ChainRetrieveResponse
```

Methods:

- <code title="get /options/chain/{symbol}">client.options.chain.<a href="./src/unusualwhales/resources/options/chain.py">retrieve</a>(symbol, \*\*<a href="src/unusualwhales/types/options/chain_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/options/chain_retrieve_response.py">ChainRetrieveResponse</a></code>

## Expirations

Types:

```python
from unusualwhales.types.options import ExpirationRetrieveResponse
```

Methods:

- <code title="get /options/expirations/{symbol}">client.options.expirations.<a href="./src/unusualwhales/resources/options/expirations.py">retrieve</a>(symbol) -> <a href="./src/unusualwhales/types/options/expiration_retrieve_response.py">ExpirationRetrieveResponse</a></code>

## Greeks

Types:

```python
from unusualwhales.types.options import GreekRetrieveResponse
```

Methods:

- <code title="get /options/greeks/{symbol}">client.options.greeks.<a href="./src/unusualwhales/resources/options/greeks.py">retrieve</a>(symbol, \*\*<a href="src/unusualwhales/types/options/greek_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/options/greek_retrieve_response.py">GreekRetrieveResponse</a></code>

## Historical

Types:

```python
from unusualwhales.types.options import HistoricalRetrieveResponse
```

Methods:

- <code title="get /options/historical/{symbol}">client.options.historical.<a href="./src/unusualwhales/resources/options/historical.py">retrieve</a>(symbol, \*\*<a href="src/unusualwhales/types/options/historical_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/options/historical_retrieve_response.py">HistoricalRetrieveResponse</a></code>

## Contract

Types:

```python
from unusualwhales.types.options import ContractRetrieveResponse
```

Methods:

- <code title="get /options/contract/{optionSymbol}">client.options.contract.<a href="./src/unusualwhales/resources/options/contract.py">retrieve</a>(option_symbol) -> <a href="./src/unusualwhales/types/options/contract_retrieve_response.py">ContractRetrieveResponse</a></code>

## Contracts

Types:

```python
from unusualwhales.types.options import ContractListResponse
```

Methods:

- <code title="get /options/contracts">client.options.contracts.<a href="./src/unusualwhales/resources/options/contracts.py">list</a>(\*\*<a href="src/unusualwhales/types/options/contract_list_params.py">params</a>) -> <a href="./src/unusualwhales/types/options/contract_list_response.py">ContractListResponse</a></code>

# Seasonality

## Stocks

Types:

```python
from unusualwhales.types.seasonality import StockRetrieveResponse
```

Methods:

- <code title="get /seasonality/stocks/{symbol}">client.seasonality.stocks.<a href="./src/unusualwhales/resources/seasonality/stocks.py">retrieve</a>(symbol, \*\*<a href="src/unusualwhales/types/seasonality/stock_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/seasonality/stock_retrieve_response.py">StockRetrieveResponse</a></code>

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
from unusualwhales.types.market import IndexRetrieveResponse
```

Methods:

- <code title="get /market/indices">client.market.indices.<a href="./src/unusualwhales/resources/market/indices.py">retrieve</a>() -> <a href="./src/unusualwhales/types/market/index_retrieve_response.py">IndexRetrieveResponse</a></code>

## Movers

Types:

```python
from unusualwhales.types.market import MoverRetrieveResponse
```

Methods:

- <code title="get /market/movers">client.market.movers.<a href="./src/unusualwhales/resources/market/movers.py">retrieve</a>(\*\*<a href="src/unusualwhales/types/market/mover_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/market/mover_retrieve_response.py">MoverRetrieveResponse</a></code>

## Sectors

Types:

```python
from unusualwhales.types.market import SectorRetrieveResponse
```

Methods:

- <code title="get /market/sectors">client.market.sectors.<a href="./src/unusualwhales/resources/market/sectors.py">retrieve</a>(\*\*<a href="src/unusualwhales/types/market/sector_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/market/sector_retrieve_response.py">SectorRetrieveResponse</a></code>

## News

Types:

```python
from unusualwhales.types.market import NewsRetrieveResponse
```

Methods:

- <code title="get /market/news">client.market.news.<a href="./src/unusualwhales/resources/market/news.py">retrieve</a>(\*\*<a href="src/unusualwhales/types/market/news_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/market/news_retrieve_response.py">NewsRetrieveResponse</a></code>
