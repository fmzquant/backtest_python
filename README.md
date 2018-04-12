# backtest_python
BotVS backtest engine python package

support python2 and python3
## install
pip install https://github.com/botvs/backtest_python/archive/master.zip
## simple example

```
'''backtest
start: 2018-02-19 00:00:00
end: 2018-03-22 12:00:00
period: 15m
exchanges: [{"eid":"OKEX","currency":"LTC_BTC","balance":3,"stocks":0}]
'''
from botvs import *
backtest = VCtx()
print exchange.GetAccount()
```
## documentation
https://www.botvs.com/api
