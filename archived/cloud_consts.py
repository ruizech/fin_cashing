from enum import Enum, unique

# domain
API_URL = 'https://api-cloud.bitmart.com'
# API_URL = 'http://api-cloud.bitmartdev.com'


# http header
CONTENT_TYPE = 'Content-Type'
X_BM_KEY = 'X-BM-KEY'
X_BM_SIGN = 'X-BM-SIGN'
X_BM_TIMESTAMP = 'X-BM-TIMESTAMP'

# http header
APPLICATION_JSON = 'application/json'

GET = "GET"
POST = "POST"
DELETE = "DELETE"

# system url
API_SYSTEM_TIME_URL = '/system/time'
API_SYSTEM_SERVICE_URL = '/system/service'

# spot url
API_SPOT_CURRENCIES_URL = '/spot/v1/currencies'
API_SPOT_SYMBOLS_URL = '/spot/v1/symbols'
API_SPOT_SYMBOLS_DETAILS_URL = '/spot/v1/symbols/details'
API_SPOT_TICKER_URL = '/spot/v1/ticker'
API_SPOT_STEPS_URL = '/spot/v1/steps'
API_SPOT_SYMBOLS_KLINE_URL = '/spot/v1/symbols/kline'
API_SPOT_SYMBOLS_BOOK_URL = '/spot/v1/symbols/book'
API_SPOT_SYMBOLS_TRADES_URL = '/spot/v1/symbols/trades'
API_SPOT_WALLET_URL = '/spot/v1/wallet'
API_SPOT_SUBMIT_BATCH_ORDERS_URL = '/spot/v1/batch_orders'
API_SPOT_SUBMIT_ORDER_URL = '/spot/v1/submit_order'
API_SPOT_CANCEL_ORDER_URL = '/spot/v1/cancel_order'
API_SPOT_CANCEL_ORDERS_URL = '/spot/v1/cancel_orders'
API_SPOT_ORDER_DETAIL_URL = '/spot/v1/order_detail'
API_SPOT_ORDERS_URL = '/spot/v1/orders'
API_SPOT_TRADES_URL = '/spot/v1/trades'
API_SPOT_CUSTOM_ORDER_URL = '/spot/custom'
API_SUB_TO_MAIN_URL = '/account/sub-account/main/v1/sub-to-main'
API_MAIN_TO_SUB_URL = '/account/sub-account/main/v1/main-to-sub'
# contract url
API_CONTRACT_CURRENCIES_URL = '/contract/v1/ifcontract/contracts'
API_CONTRACT_PNLS_URL = '/contract/v1/ifcontract/pnls'
API_CONTRACT_INDEXES_URL = '/contract/v1/ifcontract/indexes'
API_CONTRACT_TICKERS_URL = '/contract/v1/ifcontract/tickers'
API_CONTRACT_QUOTE_URL = '/contract/v1/ifcontract/quote'
API_CONTRACT_INDEX_QUOTE_URL = '/contract/v1/ifcontract/indexquote'
API_CONTRACT_TRADES_URL = '/contract/v1/ifcontract/trades'
API_CONTRACT_DEPTH_URL = '/contract/v1/ifcontract/depth'
API_CONTRACT_FUNDING_RATE_URL = '/contract/v1/ifcontract/fundingrate'
API_CONTRACT_USER_ORDERS_URL = '/contract/v1/ifcontract/userOrders'
API_CONTRACT_USER_ORDER_INFO_URL = '/contract/v1/ifcontract/userOrderInfo'
API_CONTRACT_USER_SUBMIT_ORDER_URL = '/contract/v1/ifcontract/submitOrder'
API_CONTRACT_USER_BATCH_ORDERS_URL = '/contract/v1/ifcontract/batchOrders'
API_CONTRACT_CANCEL_ORDERS_URL = '/contract/v1/ifcontract/cancelOrders'
API_CONTRACT_USER_TRADES_URL = '/contract/v1/ifcontract/userTrades'
API_CONTRACT_ORDER_TRADES_URL = '/contract/v1/ifcontract/orderTrades'
API_CONTRACT_ACCOUNTS_URL = '/contract/v1/ifcontract/accounts'
API_CONTRACT_USER_POSITIONS_URL = '/contract/v1/ifcontract/userPositions'
API_CONTRACT_USER_LIQ_RECORDS_URL = '/contract/v1/ifcontract/userLiqRecords'
API_CONTRACT_POSITION_FEE_URL = '/contract/v1/ifcontract/positionFee'
API_CONTRACT_MARGIN_OPER_URL = '/contract/v1/ifcontract/marginOper'




@unique
class Auth(Enum):
    NONE = 1
    KEYED = 2
    SIGNED = 3
