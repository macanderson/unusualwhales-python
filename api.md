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

- <code title="get /stocks/price/{symbol}">client.stocks.<a href="./src/unusualwhales/resources/stocks.py">retrieve</a>(symbol) -> <a href="./src/unusualwhales/types/stock_retrieve_response.py">StockRetrieveResponse</a></code>

# News

Types:

```python
from unusualwhales.types import NewsListResponse
```

Methods:

- <code title="get /news">client.news.<a href="./src/unusualwhales/resources/news.py">list</a>(\*\*<a href="src/unusualwhales/types/news_list_params.py">params</a>) -> <a href="./src/unusualwhales/types/news_list_response.py">NewsListResponse</a></code>
