# backtest_python

FMZ backtest engine python package
support python2 and python3, support Windows, Linux, Mac

## install
```
pip install https://github.com/fmzquant/backtest_python/archive/master.zip
```

## simple example
```python
'''backtest
start: 2018-02-19 00:00:00
end: 2018-03-22 12:00:00
period: 15m
exchanges: [{"eid":"OKEX","currency":"LTC_BTC","balance":3,"stocks":0}]
'''
from fmz import *
task = VCtx(__doc__) # initialize backtest engine from __doc__
print(exchange.GetAccount())
print(exchange.GetTicker())
print(task.Join()) # print backtest result
```

The config string can be generated automatically by saving the backtest configuration in the strategy edit page.

配置字符串可以通过策略编辑界面里的保存回测配置来自动生成

![meta](https://www.fmz.com/upload/asset/aa67494fc6306759753385bf7634ee4cd437f3f2.png) 
 
## documentation
https://www.fmz.com/api

