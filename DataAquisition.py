
#pip install python-binance
from binance.client import Client

class candlestick:

    def __init__(self, currCandle):
        self.openTime = currCandle[0]
        self.closeTime = currCandle[6]
        self. candleOpen = currCandle[1]
        self.candleHigh = currCandle[2]
        self.candleLow = currCandle[3]
        self.candleClose = currCandle[4]
        self.candleVolume = currCandle[5]
        self.quoteAssetVolume = currCandle[7]
        self.numberTrade = currCandle[8]
        self.takerBuyBaseAssetVol = currCandle[9]
        self.takerBuyQuoteAssetVol = currCandle[10]

class coinClass:
    def __init__(self, coinName, allCandleObjects):
        self.name = coinName
        self.allCandleObjects = allCandleObjects


#Initializes keys and links to exchange account
api_key = 'CFQvKQ9Xuf7L6mf8i7qqCoDmrK9C6XzGibUWXvTB4nagC3OblBlMTj49BNHV3qjN'
api_secret = 'PTJVaWQd9DCW2ysn7ATdLf1T9F8eheEe29mEVfIx9BML92N1dC95nk7jfn8tFplM'
client = Client(api_key, api_secret)

TIMEFRAME = Client.KLINE_INTERVAL_1HOUR
parseList = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'BCCUSDT', 'NEOUSDT', 'LTCUSDT', 'QTUMUSDT', 'ADAUSDT', 'XRPUSDT', 'EOSUSDT', 'TUSDUSDT', 'IOTAUSDT', 'XLMUSDT', 'ONTUSDT', 'TRXUSDT', 'ETCUSDT', 'ICXUSDT', 'VENUSDT', 'NULSUSDT', 'VETUSDT', 'PAXUSDT', 'BCHABCUSDT', 'BCHSVUSDT', 'USDCUSDT', 'LINKUSDT', 'WAVESUSDT', 'BTTUSDT', 'USDSUSDT', 'ONGUSDT', 'HOTUSDT', 'ZILUSDT', 'ZRXUSDT', 'FETUSDT', 'BATUSDT', 'XMRUSDT', 'ZECUSDT', 'IOSTUSDT', 'CELRUSDT', 'DASHUSDT', 'NANOUSDT', 'OMGUSDT']

rawAllCandleObjects = []
rawCoinList = []

for coin in parseList:
    candleList = client.get_klines(symbol=coin, interval=TIMEFRAME)
    allCandleObjects = []
    for i in range(len(candleList)):
        rawAllCandleObjects.append(candleList[(len(candleList) - 2) - i])
    rawCoinList.append(rawAllCandleObjects)
