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

# OptionsFlows

Types:

```python
from unusualwhales.types import OptionsFlowRetrieveResponse, OptionsFlowListResponse
```

Methods:

- <code title="get /options/flow/{symbol}">client.options_flows.<a href="./src/unusualwhales/resources/options_flows.py">retrieve</a>(symbol, \*\*<a href="src/unusualwhales/types/options_flow_retrieve_params.py">params</a>) -> <a href="./src/unusualwhales/types/options_flow_retrieve_response.py">OptionsFlowRetrieveResponse</a></code>
- <code title="get /options/flow">client.options_flows.<a href="./src/unusualwhales/resources/options_flows.py">list</a>(\*\*<a href="src/unusualwhales/types/options_flow_list_params.py">params</a>) -> <a href="./src/unusualwhales/types/options_flow_list_response.py">OptionsFlowListResponse</a></code>
