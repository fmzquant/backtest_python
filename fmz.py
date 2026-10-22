# -*- coding: utf-8 -*-  

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

import sys
import os
import platform
import base64
import time
import datetime
import json
import tempfile
import zlib
import math
import ctypes 
import traceback
import socket
import signal
import copy
import inspect
import io
import struct
import threading
import uuid
try:
    import md5
    import urllib2
except:
    import hashlib as md5
    import urllib.request as urllib2

try:
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
except:
    pass

try:
    from urllib import urlencode
except:
    from urllib.parse import urlencode

DATASERVER = os.getenv("DATASERVER", "http://q.fmz.com")

isPython3 = sys.version_info[0] >= 3
gg = globals()
gg['NaN'] = None
gg['null'] = None
gg['true'] = True
gg['false'] = False

# https://hynek.me/articles/hasattr/
saved_hasattr = hasattr    
def hasattr(obj, method):
    try:
        return saved_hasattr(obj, method)
    except:
        return False

if isPython3:
    gg['xrange'] = range
    string_types = str
else:
    string_types = basestring

def json_loads(s):
    if isPython3:
        return json.loads(s.decode('utf-8'))
    return json.loads(s)

def b2s(s):
    if isPython3:
        return s.decode('utf-8')
    return s

def safe_str(s):
    if isPython3:
        return s.encode('utf-8')
    return str(s)


BT_Status = 1 << 0
BT_Symbols = 1 << 1
BT_Indicators = 1 << 2
BT_Chart = 1 << 3
BT_ProfitLogs = 1 << 4
BT_RuntimeLogs = 1 << 5
BT_CloseProfitLogs = 1 << 6
BT_Accounts = 1 << 7
BT_Accounts_PnL = 1 << 8

def writeAtomic(path, data):
    # 并发的回测进程可能同时取同一份数据：先写临时文件再改名，别人看到的文件总是完整的
    tmp = '%s.%d.tmp' % (path, os.getpid())
    with open(tmp, 'wb') as f:
        f.write(data)
    getattr(os, 'replace', os.rename)(tmp, path)


def taskUUID():
    # 回测宿主（集群容器、托管者）设的任务标记；旧版托管者设的是 BOTVS_TASK_UUID，全部升级后去掉
    return os.getenv("TASK_UUID") or os.getenv("BOTVS_TASK_UUID")

def getCacheDir():
    tmpCache = tempfile.gettempdir()+ '/cache'
    if not os.path.exists(tmpCache):
        try:
            os.mkdir(tmpCache)
        except:
            pass
    return tmpCache

def httpErrorBody(e):
    # HTTPError 的正文只能读一次：读过就记在异常上
    if not hasattr(e, '_body'):
        e._body = e.read()
        if e.info().get('Content-Encoding') == 'gzip':
            try:
                e._body = zlib.decompress(e._body, 16+zlib.MAX_WBITS)
            except:
                pass
    return e._body

def httpGet(url, body=None):
    try:
        req = urllib2.Request(url, data=body.encode('utf-8') if body is not None else None)
        req.add_header('Accept-Encoding', 'gzip, deflate')
        if body is not None:
            req.add_header('Content-Type', 'application/json')
        resp = urllib2.urlopen(req)
        data = resp.read()
        if resp.info().get('Content-Encoding') == 'gzip':
            data = zlib.decompress(data, 16+zlib.MAX_WBITS)
        return data
    except urllib2.HTTPError as e:
        headers = dict(e.info())
        error_body = httpErrorBody(e)
        print("urllib2.HTTPError - Code: %s, URL: %s, Headers: %s, Body: %s" % (e.code, e.url, headers, error_body))
        raise

class Std:
    @staticmethod
    def _skip(arr, period):
        k = 0
        j = 0
        for j in xrange(0, len(arr)):
            if arr[j] is not None:
                k+=1
            if k == period:
                break
        return j

    @staticmethod
    def _sum(arr, num):
        s = 0.0
        for i in xrange(0, num):
            if arr[i] is not None:
                s += arr[i]
        return s

    @staticmethod
    def _avg(arr, num):
        if len(arr) == 0:
            return 0
        s = 0.0
        n = 0
        for i in xrange(0, min(len(arr), num)):
            if arr[i] is not None:
                s += arr[i]
                n += 1
        if n == 0:
            return 0
        return s / n

    @staticmethod
    def _zeros(n):
        return [0.0] * n 

    @staticmethod
    def _set(arr, start, end, value):
        for i in xrange(start, min(len(arr), end)):
            arr[i] = value

    @staticmethod
    def _diff(a, b):
        d = [None] * len(b)
        for i in xrange(0, len(b)):
            if a[i] is not None and b[i] is not None:
                d[i] = a[i] - b[i]
        return d

    @staticmethod
    def _move_diff(a):
        d = [None] * (len(a)-1)
        for i in xrange(1, len(a)):
            d[i-1] = a[i] - a[i-1]
        return d

    @staticmethod
    def _cmp(arr, start, end, cmpFunc):
        v = arr[start]
        for i in xrange(start, end):
            v = cmpFunc(arr[i], v)
        return v

    @staticmethod
    def _filt(records, n, attr, iv, cmpFunc):
        if len(records) < 2:
            return None
        v = iv
        pos = 0
        if n != 0:
            pos = len(records) - min(len(records)-1, n) - 1
        for i in xrange(len(records)-2, pos-1, -1):
            if records[i] is not None:
                if attr is not None:
                    v = cmpFunc(v, records[i][attr])
                else:
                    v = cmpFunc(v, records[i])
        return v

    @staticmethod
    def _ticks(records):
        if len(records) == 0:
            return []
        if isinstance(records[0], int) or isinstance(records[0], float):
            return records

        ticks = [None] * len(records)
        for i in xrange(0, len(records)):
            ticks[i] = records[i]['Close']
        return ticks

    @staticmethod
    def _sma(S, period):
        R = Std._zeros(len(S))
        j = Std._skip(S, period)
        Std._set(R, 0, j, None)
        if j < len(S):
            s = 0
            for i in xrange(j, len(S)):
                if i == j:
                    s = Std._sum(S, i+1)
                else:
                    s += S[i] - S[i-period]
                R[i] = s / period
        return R

    @staticmethod
    def _smma(S, period):
        R = Std._zeros(len(S))
        j = Std._skip(S, period)
        Std._set(R, 0, j, None)
        if j < len(S):
            R[j] = Std._avg(S, j+1)
            for i in xrange(j+1, len(S)):
                R[i] = (R[i-1] * (period-1) + S[i]) / period
        return R

    @staticmethod
    def _ema(S, period):
        R = Std._zeros(len(S))
        multiplier = 2.0 / (period + 1)
        j = Std._skip(S, period)
        Std._set(R, 0, j, None)
        if j < len(S):
            R[j] = Std._avg(S, j+1)
            for i in xrange(j+1, len(S)):
                R[i] = ((S[i] - R[i-1] ) * multiplier) + R[i-1]
        return R

class TAInstance:
    def __init__(self, logPtr = None):
        self._logPtr = logPtr

    def _log(self, name, *args):
        if self._logPtr is not None:
            self._logPtr(name, safe_str(','.join(map(str, args))))

    @staticmethod
    def Highest(records, n, attr=None):
        return Std._filt(records, n, attr, 5e-324, max)

    @staticmethod
    def Lowest(records, n, attr=None):
        return Std._filt(records, n, attr, 1.7976931348623157e+308, min)

    def MA(self, records, period=9):
        self._log('MA', period)

        return Std._sma(Std._ticks(records), period)

    def SMA(self, records, period=9):
        self._log('SMA', period)

        return Std._sma(Std._ticks(records), period)

    def EMA(self, records, period=9):
        self._log('EMA', period)

        return Std._ema(Std._ticks(records), period)

    def MACD(self, records, fastEMA=12, slowEMA=26, signalEMA=9):
        self._log('MACD', fastEMA, slowEMA, signalEMA)

        ticks = Std._ticks(records)
        slow = Std._ema(ticks, slowEMA)
        fast = Std._ema(ticks, fastEMA)
        # DIF
        dif = Std._diff(fast, slow)
        # DEA
        sig = Std._ema(dif, signalEMA)
        histogram = Std._diff(dif, sig)
        return [ dif, sig, histogram]

    def BOLL(self, records, period=20, multiplier=2):
        self._log('BOLL', period, multiplier)

        S = Std._ticks(records)
        j = period - 1
        while j < len(S) and (S[j] is None):
            j+=1
        UP = Std._zeros(len(S))
        MB = Std._zeros(len(S))
        DN = Std._zeros(len(S))
        Std._set(UP, 0, j, None)
        Std._set(MB, 0, j, None)
        Std._set(DN, 0, j, None)
        n = 0.0
        for i in xrange(j, len(S)):
            if i == j:
                for k in xrange(0, period):
                    n += S[k]
            else:
                n = n + S[i] - S[i - period]
            ma = n / period
            d = 0
            for k in xrange(i+1-period, i+1):
                d += (S[k] - ma) * (S[k] - ma)
            stdev = math.sqrt(d / period)
            up = ma + (multiplier * stdev)
            dn = ma - (multiplier * stdev)
            UP[i] = up
            MB[i] = ma
            DN[i] = dn
        return [UP, MB, DN]

    def KDJ(self, records, n=9, k=3, d=3):
        self._log('KDJ', n, k, d)

        RSV = Std._zeros(len(records))
        Std._set(RSV, 0, n - 1, None)
        K = Std._zeros(len(records))
        D = Std._zeros(len(records))
        J = Std._zeros(len(records))

        hs = Std._zeros(len(records))
        ls = Std._zeros(len(records))
        for i in xrange(0, len(records)):
            hs[i] = records[i]['High']
            ls[i] = records[i]['Low']

        for i in xrange(0, len(records)):
            if i >= (n - 1):
                c = records[i]['Close']
                h = Std._cmp(hs, i - (n - 1), i + 1, max)
                l = Std._cmp(ls, i - (n - 1), i + 1, min)
                RSV[i] = (100 * ((c - l) / (h - l))) if h != l else 100
                K[i] = float(1 * RSV[i] + (k - 1) * K[i - 1]) / k
                D[i] = float(1 * K[i] + (d - 1) * D[i - 1]) / d
            else:
                K[i] = D[i] = 50.0
                RSV[i] = 0.0
            J[i] = 3 * K[i] - 2 * D[i]
        # remove prefix
        for i in xrange(0, n-1):
            K[i] = D[i] = J[i] = None
        return [K, D, J]

    def RSI(self, records, period=14):
        self._log('RSI', period)

        n = period
        rsi = Std._zeros(len(records))
        Std._set(rsi, 0, len(rsi), None)
        if len(records) < n:
            return rsi

        ticks = Std._ticks(records)
        deltas = Std._move_diff(ticks)
        seed = deltas[:n]
        up = 0.0
        down = 0.0
        for i in xrange(0, len(seed)):
            if seed[i] >= 0:
                up += seed[i]
            else:
                down += seed[i]
        up /= n
        down /= n
        down = -down
        if down != 0:
            rs = up / down
        else:
            rs = 0
        rsi[n] = 100 - 100 / (1 + rs)
        delta = 0.0
        upval = 0.0
        downval = 0.0
        for i in xrange(n+1, len(ticks)):
            delta = deltas[i - 1]
            if delta > 0:
                upval = delta
                downval = 0.0
            else:
                upval = 0.0
                downval = -delta
            up = (up * (n - 1) + upval) / n
            down = (down * (n - 1) + downval) / n
            rs = 0 if down == 0 else (up / down)
            rsi[i] = 100 - 100 / (1 + rs)
        return rsi

    def OBV(self, records):
        self._log('OBV')

        if len(records) == 0:
            return []

        if 'Close' not in records[0]:
            raise "self.OBV argument must KLine"

        R = Std._zeros(len(records))
        for i in xrange(0, len(records)):
            if i == 0:
                R[i] = records[i]['Volume']
            elif records[i]['Close'] >= records[i - 1]['Close']:
                R[i] = R[i - 1] + records[i]['Volume']
            else:
                R[i] = R[i - 1] - records[i]['Volume']
        return R

    def ATR(self, records, period=14):
        self._log('ATR', period)

        if len(records) == 0:
            return []
        if 'Close' not in records[0]:
            raise "self.ATR argument must KLine"

        R = Std._zeros(len(records))
        m = 0.0
        n = 0.0
        for i in xrange(0, len(records)):
            TR = 0
            if i == 0:
                TR = records[i]['High'] - records[i]['Low']
            else:
                TR = max(records[i]['High'] - records[i]['Low'], abs(records[i]['High'] - records[i - 1]['Close']), abs(records[i - 1]['Close'] - records[i]['Low']))
            m += TR
            if i < period:
                n = m / (i + 1)
            else:
                n = (((period - 1) * n) + TR) / period
            R[i] = n
        return R

    def Alligator(self, records, jawLength=13, teethLength=8, lipsLength=5):
        self._log('Alligator', jawLength, teethLength, lipsLength)
        
        ticks = []
        for i in xrange(0, len(records)):
            ticks.append((records[i]['High'] + records[i]['Low']) / 2)
        return [
            [None]*8+Std._smma(ticks, jawLength), # // jaw (blue)
            [None]*5+Std._smma(ticks, teethLength), # teeth (red)
            [None]*3+Std._smma(ticks, lipsLength) # lips (green)
        ]

    def CMF(self, records, period=20):
        self._log('CMF', period)

        ret = []
        sumD = 0.0
        sumV = 0.0
        arrD = []
        arrV = []
        for i in xrange(0, len(records)):
            d = 0.0
            if records[i]['High'] != records[i]['Low']:
                d = (2 * records[i]['Close'] - records[i]['Low'] - records[i]['High']) / (records[i]['High'] - records[i]['Low']) * records[i]['Volume']
            arrD.append(d)
            arrV.append(records[i]['Volume'])
            sumD += d
            sumV += records[i]['Volume']
            if i >= period:
                sumD -= arrD.pop(0)
                sumV -= arrV.pop(0)
            ret.append(sumD / sumV)
        return ret
# end of TA

class DummyModule:
    def __init__(self, name):
        self.__name = name
        sys.modules['talib'] = self
    def __getattr__(self, attr):
        if attr == '__file__':
            return 'talib.py'
        raise Exception('Please install %s module for python (%s)' % (self.__name, attr))

class MyList(list):
    def __init__(self, data):
        super(MyList, self).__init__(data)
        self.__data = data
    def __getattr__(self, attr):
        if attr.startswith('_'):
            raise AttributeError
        ret = []
        for item in self.__data:
            ret.append(item[attr])
        if HasTALib:
            ret = numpy.array(ret, dtype='float64')
        setattr(self, attr, ret)
        return ret

HasTALib = False
try:
    import talib
    import numpy
    HasTALib = True
except ImportError:
    talib = DummyModule('talib')


class dic2obj(dict):
    def __getattr__(self, name):
        if name in self:
            return self[name]
        else:
            raise AttributeError("no attribute '%s'" % name)

    def __setattr__(self, name, value):
        self[name] = value

    def __delattr__(self, name):
        if name in self:
            del self[name]
        else:
            raise AttributeError("no attribute '%s'" % name)

def _status_arg(item):
    """LogStatus 参数整形，对齐 JS：字典 / 列表 → JSON 文本（NaN / ±inf 写 null），前端据此渲染
    状态栏组件；单独传的 NaN / ±inf 写成文字 nan / inf；其余原样。表格由调用方先包好反引号。"""
    if isinstance(item, float) and (math.isnan(item) or math.isinf(item)):
        return str(item)
    if isinstance(item, (dict, list, tuple)):
        try:
            # NaN / ±inf：先按 JSON 记号写出，读回时换成 None（null），与 JS JSON.stringify 一致。
            # 不用递归辅助函数：打包混淆器不改推导式里的函数名，递归调用会变成未定义的名字。
            plain = json.loads(json.dumps(item, default=str), parse_constant=lambda c: None)
            return json.dumps(plain, separators=(',', ':'), ensure_ascii=not isPython3)
        except Exception:
            return str(item)
    return item


def JoinArgs(args, status=False):
    arr = []
    for item in args:
        if hasattr(item, 'savefig') and callable(item.savefig):
            d = io.BytesIO()
            item.savefig(d, format="png")
            arr.append('`data:image/png;base64,%s`'%(base64.b64encode(d.getvalue()).decode('utf-8')))
        elif isinstance(item, dict) and item.get('type') == 'table' and item.get('cols'):
            arr.append('`%s`' % json.dumps(item))
        elif status and isinstance(item, (dict, list, tuple, float)):
            # 只有 LogStatus：字典 / 列表转 JSON（与 JS 一致），Log 等其它日志保持原样
            arr.append(str(_status_arg(item)))
        else:
            arr.append(str(item))
    return safe_str(' '.join(arr))

def _t(v):
    """bytes -> str (JoinArgs and friends return bytes on Python 3)"""
    if isinstance(v, bytes):
        return v.decode('utf-8', 'replace')
    return v

_enc = json.JSONEncoder(separators=(',', ':'), allow_nan=False).encode
_scan = json.decoder.JSONDecoder(object_hook=dic2obj).scan_once

class _Api(object):
    """The one entry into the engine (api_call, the same call table as JS): name + JSON args -> value.
    The engine only reports how a call ended; the exceptions are raised here: the end of the
    backtest is EOFError, an engine error is Exception(message). NaN/inf arguments are refused
    (ValueError) rather than silently turned into something else."""
    def __init__(self, lib, ctx):
        lib.api_call.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p, ctypes.c_size_t]
        lib.api_call.restype = ctypes.c_char_p
        self.call = lib.api_call
        self.ctx = ctx

    def __call__(self, name, *args):
        a = _enc(args).encode('utf-8')
        r = self.call(self.ctx, name, a, len(a)).decode('utf-8')
        c = r[0]
        if c == 'r':
            return _scan(r, 1)[0]
        if c == 'x':
            raise EOFError()
        raise Exception(_scan(r, 1)[0])

def _ticker(t):
    if t is not None and 'Info' not in t:
        t['Info'] = None
    return t

def _keyed(v, keys):
    """Rebuild dicts in the field order Python strategies have always printed"""
    if v is None:
        return None
    return [dic2obj([(k, d[k]) for k in keys if k in d]) for d in v]

_POSITION_KEYS = ('MarginLevel', 'Amount', 'FrozenAmount', 'Price', 'Profit', 'Margin', 'Type', 'Symbol', 'ContractType')

def _positions(v):
    v = _keyed(v, _POSITION_KEYS)
    if v is not None:
        for p in v:
            if not p.get('ContractType'):
                p.pop('ContractType', None)
    return v

def _order_id(r):
    return int(r) if r is not None and r > 0 else None

class AsyncRet:
    routineId = 0
    def __init__(self, v):
        self.isWait = False
        self.v = v
        AsyncRet.routineId += 1

    def wait(self, timeout=0):
        if self.isWait:
            return (None, False)
        self.isWait = True
        return (self.v, True)

    def __repr__(self):
        return '<Go %d>' % AsyncRet.routineId

class Exchange:
    def __init__(self, api, idx, opt, cfg):
        self.api = api
        self.idx = idx
        self.opt = opt
        self.cfg = cfg
        self.name = cfg["Id"]
        self.label = cfg["Label"]
        self.currency = '%s_%s' % (cfg["BaseCurrency"], cfg["QuoteCurrency"])
        self.baseCurrency = cfg["BaseCurrency"]
        self.quoteCurrency = cfg["QuoteCurrency"]
        self.maxBarLen = cfg.get('MaxBarLen', 1000)
        self.period = opt['Period']
        self.ct = ''
        self.records_cache = {}

    def Go(self, method, *args):
        return AsyncRet(getattr(self, method)(*args))

    def GetName(self):
        return self.name

    def GetLabel(self):
        return self.label

    def GetCurrency(self):
        return self.currency

    def GetBaseCurrency(self):
        return self.baseCurrency

    def GetQuoteCurrency(self):
        return self.quoteCurrency

    def GetUSDCNY(self):
        return self.api(b'Exchange_GetUSDCNY', self.idx)

    def SetMaxBarLen(self, n):
        self.maxBarLen = n

    def SetPrecision(self, a, b):
        self.api(b'Exchange_SetPrecision', self.idx, a, b)

    def GetRate(self):
        return self.api(b'Exchange_GetRate', self.idx)

    def SetProxy(self, s):
        pass

    def SetTimeout(self, ms):
        pass

    def SetBase(self, s):
        return self.api(b'Exchange_SetBase', self.idx, s)

    def GetBase(self):
        return self.api(b'Exchange_GetBase', self.idx)

    def SetCurrency(self, s):
        arr = s.split('_')
        if len(arr) == 2:
            self.currency = s
            self.quoteCurrency = arr[1]
            return self.api(b'Exchange_SetCurrency', self.idx, s)

    def SetRate(self, rate=1.0):
        return self.api(b'Exchange_SetRate', self.idx, rate)

    def GetTrades(self, symbol=''):
        return _keyed(self.api(b'Exchange_GetTrades', self.idx, symbol), ('Id', 'Time', 'Price', 'Amount', 'Type'))

    def SetData(self, name, data):
        if not isinstance(data, string_types):
            data = json.dumps(data)
        return int(self.api(b'Exchange_SetData', self.idx, name, data))

    def GetData(self, name, timeout=60000, offset=0):
        r = self.api(b'Exchange_GetData', self.idx, name, int(timeout), int(offset))
        if r is None:
            return None
        return dic2obj({'Time': int(r['Time']), 'Data': json.loads(r['Data']) if r['Data'] else None})

    def GetTickers(self):
        v = self.api(b'Exchange_GetTickers', self.idx)
        if v is not None:
            for t in v:
                _ticker(t)
        return v

    def GetMarkets(self):
        return json.loads(self.api(b'Exchange_GetMarkets', self.idx))

    def GetTicker(self, symbol=''):
        return _ticker(self.api(b'Exchange_GetTicker', self.idx, symbol))

    def GetFundings(self, symbol=''):
        return self.api(b'Exchange_GetFundings', self.idx, symbol)

    def IO(self, k, v = 0, *more):
        if k == 'currency':
            return self.SetCurrency(v)
        if k in ('isMarketOpen', 'ismarketopen'):
            # 参数（时间戳、"CN"、品种）原样交给引擎；什么都没传时不补 0（0 会被当成时间戳）
            args = (v,) + more if (more or v != 0) else ()
            return dic2obj(self.api(b'Exchange_IO', self.idx, k, *args))
        return self.api(b'Exchange_IO', self.idx, k, int(v))

    def GetDepth(self, symbol=''):
        d = self.api(b'Exchange_GetDepth', self.idx, symbol)
        if d is None:
            return None
        orders, n = d['Orders'], d['AsksLen']
        return dic2obj({'Asks': orders[:n], 'Bids': orders[n:n + d['BidsLen']]})

    def GetRecords(self, symbol='', period=-1, limit=0):
        if isinstance(symbol, int):
            limit = period
            period = symbol
            symbol = ''
        if period == -1:
            period = int(self.period/1000)
        eles = self.api(b'Exchange_GetRecords', self.idx, symbol, int(period))
        if eles is None:
            return None
        k = '%s/%s/%s/%d' % (self.currency, symbol, self.ct, period)
        c = self.records_cache.get(k, None)
        if c is None or len(c) == 0:
            if len(eles) > self.maxBarLen:
                eles = eles[len(eles)-self.maxBarLen:]
            self.records_cache[k] = eles
        else:
            preTime = 0 if len(c) == 0 else c[-1]['Time']
            for ele in eles:
                t = ele['Time']
                if t == preTime:
                    c[-1] = ele
                elif t > preTime:
                    c.append(ele)
                    if len(c) > self.maxBarLen:
                        c.pop(0)
                    preTime = t
        r = MyList(self.records_cache[k])
        if limit > 0:
            r = MyList(r[-limit:])
        return r

    def GetAssets(self):
        return _keyed(self.api(b'Exchange_GetAssets', self.idx), ('Currency', 'Amount', 'FrozenAmount'))

    def GetAccount(self):
        return self.api(b'Exchange_GetAccount', self.idx)

    def Buy(self, price, amount=None, *extra):
        return _order_id(self.api(b'Exchange_Buy', self.idx, price, amount, _t(JoinArgs(extra))))

    def Sell(self, price, amount=None, *extra):
        return _order_id(self.api(b'Exchange_Sell', self.idx, price, amount, _t(JoinArgs(extra))))

    def CreateOrder(self, symbol, side, price, amount=None, *extra):
        return _order_id(self.api(b'Exchange_CreateOrder', self.idx, symbol, side, price, amount, _t(JoinArgs(extra))))

    def ModifyOrder(self, orderId, side, price, amount=None, *extra):
        return _order_id(self.api(b'Exchange_ModifyOrder', self.idx, orderId, side, price, amount, _t(JoinArgs(extra))))

    def GetOrders(self, symbol=''):
        return self.api(b'Exchange_GetOrders', self.idx, symbol, False)

    def GetHistoryOrders(self, symbol='', since=0, limit = 0):
        if isinstance(symbol, int):
            limit = since
            since = symbol
            symbol = ''
        return self.api(b'Exchange_GetHistoryOrders', self.idx, symbol, False, since, limit)

    def GetOrder(self, orderId):
        return self.api(b'Exchange_GetOrder', self.idx, orderId, False)

    def CancelOrder(self, orderId, *extra):
        return self.api(b'Exchange_CancelOrder', self.idx, orderId, False, _t(JoinArgs(extra))) is True

    # condition orders
    def CreateConditionOrder(self, symbol, side, amount, condition, *extra):
        return _order_id(self.api(b'Exchange_CreateConditionOrder', self.idx, symbol, side, amount, json.dumps(condition), _t(JoinArgs(extra))))

    def ModifyConditionOrder(self, orderId, side, amount, condition, *extra):
        return _order_id(self.api(b'Exchange_ModifyConditionOrder', self.idx, orderId, side, amount, json.dumps(condition), _t(JoinArgs(extra))))

    def GetConditionOrders(self, symbol=''):
        return self.api(b'Exchange_GetOrders', self.idx, symbol, True)

    def GetHistoryConditionOrders(self, symbol='', since=0, limit = 0):
        if isinstance(symbol, int):
            limit = since
            since = symbol
            symbol = ''
        return self.api(b'Exchange_GetHistoryOrders', self.idx, symbol, True, since, limit)

    def GetConditionOrder(self, orderId):
        return self.api(b'Exchange_GetOrder', self.idx, orderId, True)

    def CancelConditionOrder(self, orderId, *extra):
        return self.api(b'Exchange_CancelOrder', self.idx, orderId, True, _t(JoinArgs(extra))) is True

    def Log(self, orderType, price, amount=0, *extra):
        ret = self.api(b'Exchange_Log', self.idx, orderType, price, amount, _t(JoinArgs(extra)))
        if orderType == 2:
            return bool(ret)
        if ret > 0:
            return int(ret)

    def GetContractType(self):
        return self.ct

    def GetPeriod(self):
        return int(self.period/1000)

    def SetContractType(self, symbol):
        r = self.api(b'Exchange_SetContractType', self.idx, symbol)
        if r is None:
            return None
        self.ct = symbol
        return json.loads(r) if r else True

    def SetMarginLevel(self, symbol, level=None):
        if isinstance(symbol, int) or isinstance(symbol, float):
            level, symbol = symbol, level
        if not symbol:
            symbol = ''
        return self.api(b'Exchange_SetMarginLevel', self.idx, symbol, level)

    def SetDirection(self, direction):
        return self.api(b'Exchange_SetDirection', self.idx, direction)

    def GetPositions(self, symbol=''):
        return _positions(self.api(b'Exchange_GetPositions', self.idx, symbol))

    def GetPosition(self):
        return self.GetPositions()

class Chart(object):
    def __init__(self, api, js):
        self.api = api
        self.api(b'Chart_New', json.dumps(js))

    def update(self, js):
        self.api(b'Chart_New', json.dumps(js))

    def add(self, seriesIdx, d, replaceId=None):
        obj = [seriesIdx, d]
        if replaceId is not None:
            obj.append(replaceId)
        self.api(b'Chart_Add', json.dumps(obj))

    def reset(self, keep=0):
        self.api(b'Chart_Reset', keep)

class KLineChart():
    def __init__(self, api, options={}):
        options["__isCandle"] = True
        self.chart = Chart(api, options)
        self.bar = None
        self.overlay = options.get("overlay", False)
        self.preTime = 0
        self.runtime = { "plots": [], "signals": [], "titles": {}, "count": 0 }
        
    def trim(self, obj):
        dst = {}
        for k in obj:
            if obj[k] is not None:
                dst[k] = obj[k]
        return dst
        
    def newPlot(self, obj):
        shape = self.trim(obj)
        if "overlay" not in shape:
            shape["overlay"] = self.overlay
        if shape["type"] != 'shape' and shape["type"] != 'bgcolor' and shape["type"] != 'barcolor':
            if "title" not in shape or len(shape["title"]) == 0 or shape["title"] in self.runtime["titles"]:
                shape["title"] = '<' + shape.get("title","plot") + '_' + str(self.runtime["count"]) + '>'
            self.runtime["count"] += 1
            if "title" in shape:
                self.runtime["titles"][shape["title"]] = True
        return shape
    

    def begin(self, bar):
        self.bar = bar

    def reset(self, remain=0):
        self.chart.reset(remain)
        self.preTime = 0

    def close(self, bar=None):
        if bar:
            self.bar = bar

        if self.bar["Time"] < self.preTime:
            return

        data = {
            "timestamp": self.bar["Time"],
            "open": self.bar["Open"],
            "high": self.bar["High"],
            "low": self.bar["Low"],
            "close": self.bar["Close"],
            "volume": self.bar.get("Volume", 0),
        }

        for k in ["plots", "signals"]:
            if len(self.runtime[k]) > 0:
                if "runtime" not in data:
                    data["runtime"] = {}
                data["runtime"][k] = self.runtime[k]

        if self.preTime == self.bar["Time"]:
            self.chart.add(0, data, -1)
        else:
            self.chart.add(0, data)

        self.preTime = self.bar["Time"]
        self.runtime["plots"] = []
        self.runtime["signals"] = []
        self.runtime["titles"] = {}
        self.runtime["count"] = 0

    def plot(self, series=None, title=None, color=None, linewidth=1, style="line", trackprice=None, histbase=0, offset=0, join=False, editable=False, show_last=None, display ="all", overlay=None):
        if series is None or self.bar["Time"] < self.preTime:
            return

        self.runtime["plots"].append(self.newPlot({
            "series": series,
            "overlay": overlay,
            "title": title,
            "join": join,
            "color": color,
            "histbase": histbase,
            "type": style,
            "lineWidth": linewidth,
            "display": display,
            "offset": offset
        }))
        return len(self.runtime["plots"]) - 1

    def barcolor(self, color, offset=None, editable=False, show_last=None, title=None, display="all"):
        if display != "all" or self.bar["Time"] < self.preTime:
            return
        self.runtime["plots"].append(self.newPlot({
            "type": 'barcolor',
            "title": title,
            "color": color,
            "offset": offset,
            "showLast": show_last,
            "display": display
        }))
        
    def plotarrow(self, series, title=None, colorup="#00ff00",
        colordown = "#ff0000",
        offset = 0,
        minheight = 5,
        maxheight = 100,
        editable = False, show_last=None, display = "all", overlay = None):
        if display != "all" or self.bar["Time"] < self.preTime:
            return

        self.runtime["plots"].append(self.newPlot({
            "series": series,
            "title": title,
            "colorup": colorup,
            "colordown": colordown,
            "offset": offset,
            "minheight": minheight,
            "maxheight": maxheight,
            "showLast": show_last,
            "type": "shape",
            "style": "arrow",
            "display": display,
            "overlay": overlay
        }))
        
    def hline(self, price, title = None, color = None, linestyle = "dashed", linewidth = None, editable = False, display = "all", overlay = None):
        if display != "all" or self.bar["Time"] < self.preTime:
            return
        
        self.runtime["plots"].append(self.newPlot({
            "title": title,
            "price": price,
            "overlay": overlay,
            "color": color,
            "type": 'hline',
            "lineStyle": linestyle,
            "lineWidth": linewidth,
            "display": display
        }))
        return len(self.runtime["plots"]) - 1


    def bgcolor(self, color, offset=None, editable=None, show_last=None, title=None, display = "all", overlay=None):
        if display != "all" or self.bar["Time"] < self.preTime:
            return
        self.runtime["plots"].append(self.newPlot({
                "title": title,
                "overlay": overlay,
                "color": color,
                "type": 'bgcolor',
                "showLast": show_last,
                "offset": offset
            }))
    

    def plotchar(self, series, title=None, char=None, location = "abovebar", color=None, offset=None, text=None, textcolor=None, editable=None, size = "auto", show_last=None, display="all", overlay=None):
        if (location != "absolute" and series is None) or (location == "absolute" and series is None) or char is None or self.bar["Time"] < self.preTime:
            return

        self.runtime["plots"].append(self.newPlot({
            "overlay": overlay,
            "type": "shape",
            "style": "char",
            "char": char,
            "series": series,
            "location": location,
            "color": color,
            "offset": offset,
            "size": size,
            "text": text,
            "textColor": textcolor
        }))


 
    def plotshape(self, series, title=None, style=None, location="abovebar", color=None, offset=None, text=None, textcolor=None, editable=None, size = "auto", show_last=None, display="all", overlay=None):
        if (location != "absolute" and series is None) or (location == "absolute" and series is None) or self.bar["Time"] < self.preTime:
            return
        
        self.runtime["plots"].append(self.newPlot({
            "type": "shape",
            "overlay": overlay,
            "title": title,
            "size": size,
            "style": style,
            "series": series,
            "location": location,
            "color": color,
            "offset": offset,
            "text": text,
            "textColor": textcolor
        }))

    def plotcandle(self, open, high, low, close, title=None, color=None, wickcolor=None, editable=None, show_last=None, bordercolor=None, display="all", overlay=None):
        if display != "all" or self.bar["Time"] < self.preTime:
            return
 
        self.runtime["plots"].append(self.newPlot({
            "price": high,
            "open": open,
            "high": high,
            "low": low,
            "close": close,
            "title": title,
            "color": color,
            "wickColor": wickcolor,
            "showLast": show_last,
            "borderColor": bordercolor,
            "type": "candle",
            "display": display,
            "overlay": overlay,
        }))

    def fill(self, plot1, plot2, color=None, title=None, editable=None, show_last=None, fillgaps=None, display="all"):
        if self.bar["Time"] < self.preTime:
            return
        if plot1 >= 0 and plot2 >= 0 and plot1 < len(self.runtime["plots"]) and plot2 < len(self.runtime["plots"]) and display == "all":
            dst = self.runtime["plots"][plot1]
            if "fill" not in dst:
                dst["fill"] = []
            dst["fill"].append(self.trim({
                "value": self.runtime["plots"][plot2]["series"],
                "color": color,
                "showLast": show_last
            }))

    def signal(self, direction, price, qty, id=None):
        if self.bar["Time"] < self.preTime:
            return
        task = {
            "id": id or direction,
            "avgPrice": price,
            "qty": qty
        }
        if direction == "buy" or direction == "long":
            task["direction"] = "long"
        elif direction == "sell" or direction == "short":
            task["direction"] = "short"
        elif direction == "closesell" or direction == "closeshort":
            task["direction"] = "close"
            task["closeDirection"] = "short"
        elif direction == "closebuy" or direction == "closelong":
            task["direction"] = "close"
            task["closeDirection"] = "long"
            
        if task["direction"] or task["closeDirection"]:
            self.runtime["signals"].append(task)

def periodToMs(s, default):
    period = default
    if len(s) < 2:
        return period
    tmp = int(s[:-1])
    c = s[-1]
    if c == 'd':
        period = tmp * 60000 * 60 * 24
    elif c == 'm':
        period = tmp * 60000
    elif c == 'm':
        period = tmp * 60000
    return period

def parseTask(s):
    settings = s
    dic = {}
    for line in settings.split('\n'):
        line = line.strip()
        if ':' not in line:
            continue
        arr = line.split(':', 1)
        if len(arr) == 2:
            k = arr[0].strip()
            v = arr[1].strip()
            dic[k] = v
    pnl = dic.get('pnl', 'true')
    dataServer = dic.get('dataServer', DATASERVER)
    period = periodToMs(dic.get('period', '1h'), 60000 * 60)
    basePeriod = periodToMs(dic.get('basePeriod', ''), 0)

    exchanges = []
    for e in json.loads(dic.get('exchanges', '[]')):
        arr = e['currency'].upper().split('_')
        if len(arr) == 1:
            arr.append('CNY' if 'CTP' in e['eid'] else 'USD')
        if basePeriod == 0:
            basePeriod = 60000 * 60
            if period == 86400000:
                basePeriod = 60000 * 60
            elif period == 3600000:
                basePeriod = 60000 * 30
            elif period == 1800000:
                basePeriod = 60000 * 15
            elif period == 900000:
                basePeriod = 60000 * 5
            elif period == 300000:
                basePeriod = 60000
        feeDef = {
            'Huobi': [150, 200],
            'OKX': [150, 200],
            'Binance': [150, 200],
            'Futures_BitMEX': [8, 10],
            'Futures_OKX': [30, 30],
            'Futures_HuobiDM': [30, 30],
            'Futures_CTP': [25, 25],
            'Futures_XTP': [30, 130],
        }
        if e['eid'] == "Futures_CTP":
            dataServer = "http://q.youquant.com"

        fee = e.get('fee')
        if fee is None:
            fee = feeDef.get(e['eid'], [2000, 2000])
        else:
            fee = [int(fee[0]*10000), int(fee[1]*10000)]

        cfg = {
            "Balance": e.get('balance', 10000.0),
            "Stocks": e.get('stocks', 3.0),
            "BaseCurrency": arr[0],
            "QuoteCurrency": arr[1],
            "BasePeriod": basePeriod,
            "FeeDenominator": 6,
            "FeeMaker": fee[0],
            "FeeTaker": fee[1],
            "FeeMin": e.get('feeMin', 0),
            "Id": e['eid'],
            "Label": e['eid']
        }
        exchanges.append(cfg)

    options = {
        "DataServer": dataServer,
		"MaxChartLogs": 800,
		"MaxProfitLogs": 800,
		"MaxRuntimeLogs": 800,
		"NetDelay": 200,
		"Period": period,
		"RetFlags": BT_Status | BT_Indicators | BT_Accounts | BT_Chart | BT_RuntimeLogs | BT_ProfitLogs,
		"TimeBegin": int(time.mktime(datetime.datetime.strptime(dic.get('start', '2019-02-01 00:00:00'), "%Y-%m-%d %H:%M:%S").timetuple())),
		"TimeEnd": int(time.mktime(datetime.datetime.strptime(dic.get('end', '2019-02-10 00:00:00'), "%Y-%m-%d %H:%M:%S").timetuple())),
		"UpdatePeriod": 5000
	}
    snapshotPeriod = 86400
    testRange = options['TimeEnd'] - options['TimeBegin']
    if testRange / 3600 <= 2:
        snapshotPeriod = 60
    elif testRange / 86400 <= 2:
        snapshotPeriod = 300
    elif testRange / 86400 < 30:
        snapshotPeriod = 3600
    options['SnapshotPeriod'] = snapshotPeriod * 1000
    if pnl == 'true':
        options['RetFlags'] |= BT_Accounts_PnL
    return {'Exchanges': exchanges, 'Options': options}

class Templates():
    pass

class VCtx(object):
    def __init__(self, task = None, autoRun=False, gApis = None, progressCallback=None):
        self._joinResult = None
        self.gs = threading.Lock()
        if gApis is None:
            if __name__ == "__main__":
                gApis = globals()
            else:
                gApis = dict(inspect.getmembers(inspect.stack()[1][0]))["f_globals"]

        if task is None:
            task = parseTask(gApis['__doc__'])
        elif hasattr(task, 'upper'):
            task = parseTask(task)

        if progressCallback is not None:
            self.progressCallback = progressCallback

        self.httpGetPtr = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.POINTER(ctypes.c_char_p), ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int))(self.httpGetCallback)
        self.progessCallbackPtr = ctypes.CFUNCTYPE(None, ctypes.c_char_p)(self.progressCallback)
        osName = platform.system()
        archName = platform.architecture()[0]
        # processor() is "arm" only on macOS; Linux reports "aarch64"/"armv7l" (or "")
        machine = platform.machine().lower()
        if platform.processor() == "arm" or machine.startswith("arm") or machine.startswith("aarch"):
            archName = 'arm64' if archName == '64bit' else 'arm'
        self.os = '%s/%s' % (osName.lower(), archName)
        soName = 'backtest_py_%s_%s.so' % (osName.lower(), archName)
        crcFile = 'md5.json'
        loader = os.path.join("./depends", soName)
        if not os.path.exists(loader):
            hdic = {}
            tmpCache = getCacheDir()
            js = os.path.join(tmpCache, crcFile)
            if os.path.exists(js):
                b = open(js, 'rb').read()
                if taskUUID() is None or "1187625e4ea168617ad55ca7b505d15b" in str(b):
                    hdic = json_loads(b)
            loader = os.path.join(tmpCache, soName)
            update = False
            if not os.path.exists(loader):
                update = True
            else:
                old = md5.md5(open(loader, 'rb').read()).hexdigest()
                if old != hdic.get(soName, None):
                    update = True
                    backup = os.path.join(tmpCache, old)
                    try:
                        os.rename(loader, backup)
                        os.remove(backup)
                    except:
                        pass
            if update:
                writeAtomic(loader, httpGet(task["Options"]["DataServer"] + "/dist/depends/" + soName))
                writeAtomic(js, httpGet(task["Options"]["DataServer"] + "/dist/depends/" + crcFile))
        else:
            print("load from debug mode", loader)
        lib = ctypes.CDLL(os.path.abspath(loader))
        if not hasattr(lib, 'api_call'):
            # 旧引擎库（站点 /dist/depends/ 或本地缓存里还是旧版）：接口不同，用不了
            raise Exception('backtest engine library %s is an old version (no api_call); update /dist/depends/ on the data server, or delete the cached file and run again' % loader)
        lib.api_backtest.restype = ctypes.c_void_p
        ctx = ctypes.c_void_p(lib.api_backtest(safe_str(json.dumps(task)), self.httpGetPtr, self.progessCallbackPtr, None))
        if not ctx:
            raise 'Initialize backtest engine error'
        self.ctx = ctx
        self.lib = lib
        self.api = _Api(lib, ctx)
        self.cache = {}
        self.kvdb = {}
        self.cRetryDelay = 3000
        # HOOK
        exchanges = []
        i = 0
        for ele in task["Exchanges"]:
            exchanges.append(Exchange(self.api, i, task["Options"], ele))
            i += 1

        for k in dir(self):
            if k.startswith('g_'):
                gApis[k[2:]] = getattr(self, k)

        self.realTime = time.time
        time.time = self.g_PyTime
        gApis['__name__'] = '__main__'
        gApis["TA"] = TAInstance(self._logTA)
        gApis['exchanges'] = exchanges
        gApis['exchange'] = exchanges[0]
        gApis['ext'] = Templates()
        gApis['time'] = time
        gApis['null'] = None
        gApis['true'] = True
        gApis['false'] = False
        gApis["ORDER_STATE_PENDING"] = 0
        gApis["ORDER_STATE_CLOSED"] = 1
        gApis["ORDER_STATE_CANCELED"] = 2
        gApis["ORDER_STATE_UNKNOWN"] = 3
        gApis["ORDER_TYPE_BUY"] = 0
        gApis["ORDER_TYPE_SELL"] = 1
        gApis["ORDER_OFFSET_OPEN"] = 0
        gApis["ORDER_OFFSET_CLOSE"] = 1

        gApis["ORDER_CONDITION_TYPE_OCO"] = 0
        gApis["ORDER_CONDITION_TYPE_TP"] = 1
        gApis["ORDER_CONDITION_TYPE_SL"] = 2
        gApis["ORDER_CONDITION_TYPE_GENERIC"] = 3

        gApis["PD_LONG"] = 0
        gApis["PD_SHORT"] = 1
        gApis["PD_LONG_YD"] = 2
        gApis["PD_SHORT_YD"] = 3

        gApis["LOG_TYPE_BUY"] = 0
        gApis["LOG_TYPE_SELL"] = 1
        gApis["LOG_TYPE_CANCEL"] = 2
        gApis["LOG_TYPE_ERROR"] = 3
        gApis["LOG_TYPE_PROFIT"] = 4
        gApis["LOG_TYPE_LOG"] = 5
        gApis["LOG_TYPE_RESTART"] = 6

        gApis["PERIOD_M1"] = 60 * 1
        gApis["PERIOD_M3"] = 60 * 3
        gApis["PERIOD_M5"] = 60 * 5
        gApis["PERIOD_M15"] = 60 * 15
        gApis["PERIOD_M30"] = 60 * 30
        gApis["PERIOD_H1"]  = 60 * 60
        gApis["PERIOD_H2"]  = 60 * 60 * 2
        gApis["PERIOD_H4"]  = 60 * 60 * 4
        gApis["PERIOD_H6"]  = 60 * 60 * 6
        gApis["PERIOD_H12"]  = 60 * 60 * 12
        gApis["PERIOD_D1"]  = 60 * 60 * 24
        gApis["PERIOD_D3"]  = 60 * 60 * 24 * 3
        gApis["PERIOD_W1"]  = 60 * 60 * 24  * 7

        if autoRun:
            try:
                gApis['main']()
            except EOFError:
                pass
            self.Join()

    def httpGetCallback(self, path, ptr_buf, ptr_size, ptr_need_free):
        # 普通行情为 GET；HttpQuery/Mail 在换行后附带 JSON 选项，按 POST 发送（同 JS worker、云端 loader），不缓存
        url = path.decode('utf8')
        body = None
        if '\n' in url:
            url, body = url.split('\n', 1)
        cacheFile = None if body is not None else getCacheDir()+'/http_'+md5.md5(path).hexdigest()
        data = None
        try:
            if cacheFile and os.path.exists(cacheFile):
                data = open(cacheFile, 'rb').read()
            else:
                data = httpGet(url, body)
                if cacheFile and len(data) > 0:
                    writeAtomic(cacheFile, data)
        except urllib2.HTTPError as e:
            # 数据服务自己回的错误状态（如品种不存在）照常交给引擎；网关报上游不可达才是网络错误
            if e.code not in (502, 503, 504):
                data = httpErrorBody(e)
            else:
                data = None
                err = 'HTTP %d' % e.code
        except Exception as e:
            data = None
            err = str(e)
        if data is None:
            # 取数失败交给引擎：返回非 0，缓冲区里是错误信息
            buf = ctypes.create_string_buffer(err.encode('utf-8', 'replace'))
            ptr_size.contents.value = len(buf.value)
            ptr_need_free.contents.value = 0
            ptr_buf.contents.value = ctypes.addressof(buf)
            self.cache = {0: buf}
            return 1
        ptr_size.contents.value = len(data)
        ptr_need_free.contents.value = 0
        str_buf = ctypes.create_string_buffer(data)
        ptr_buf.contents.value = ctypes.addressof(str_buf)
        # the engine copies the body before the callback returns; keep only the latest buffer alive
        self.cache = {0: str_buf}
        return 0

    def progressCallback(self, st):
        pass

    def _logTA(self, name, args):
        self.api(b'LogTA', _t(name), _t(args))

    def g_Unix(self):
        return self.api(b'Unix')

    def g_UnixNano(self):
        return self.api(b'UnixNano')

    def g_PyTime(self):
        return float(self.g_UnixNano())/1e9

    def g_Sleep(self, n):
        self.api(b'Sleep', n)

    def g_EnableLog(self, flag = True):
        self.api(b'EnableLog', bool(flag))

    def g_Log(self, *extra):
        self.api(b'Log', _t(JoinArgs(extra)))

    def g_LogReset(self, keep = 0):
        self.api(b'LogReset', keep)

    def g_LogVacuum(self):
        pass

    def g_LogStatus(self, *extra):
        self.api(b'LogStatus', _t(JoinArgs(extra, status=True)))

    def g_LogProfit(self, profit, *extra):
        self.api(b'LogProfit', profit, _t(JoinArgs(extra)))

    def g_LogProfitReset(self, keep = 0):
        self.api(b'LogProfitReset', keep)

    def g_LogError(self, *extra):
        self.api(b'LogError', _t(JoinArgs(extra)))

    def g_Panic(self, *extra):
        self.api(b'LogError', _t(JoinArgs(extra)))
        raise EOFError()

    def g_GetLastError(self):
        return ''

    def g_MD5(self, s):
        return md5.md5(safe_str(s)).hexdigest()

    def g_HttpQuery(self, url, options=None):
        # 同 JS 回测：经数据服务转发（选项按 POST 交给平台）；debug 时返回 {StatusCode, Length, Body, Header}。
        # 旧写法 HttpQuery(url, postData)：字符串是请求体，按 POST 发送
        if isinstance(options, str) and options:
            options = {'method': 'POST', 'body': options}
        ret = self.api(b'HttpQuery', url, json.dumps(options) if isinstance(options, dict) else '')
        if isinstance(options, dict) and options.get('debug'):
            obj = json.loads(ret)
            body = obj.get('body')
            ret = dic2obj({'StatusCode': obj.get('status'), 'Length': len(body) if body else 0, 'Body': body,
                           'Header': {k: [v] for k, v in (obj.get('headers') or {}).items()}})
        return ret

    def g_HttpQuery_Go(self, *args):
        return AsyncRet(self.g_HttpQuery(*args))

    def g_JSONParse(self, s):
        return json.loads(s)

    def g_UUID(self):
        return uuid.uuid4().hex.upper()

    def g_StrDecode(self, s, c='gbk'):
        self.g_LogError("sandbox not support StrDecode")

    def g_EnableLogLocal(self, b):
        pass

    def g_Dial(self, *args):
        self.g_LogError("sandbox not support Dial")

    def g_DBExec(self, *args):
        self.g_LogError("sandbox not support DBExec")

    def g_Encode(self, *args):
        self.g_LogError("sandbox not support Encode")

    def g_EventLoop(self, *args):
        self.g_LogError("sandbox not support EventLoop")

    def g_Mail(self, smtpServer='', smtpUsername='', smtpPassword='', mailTo='', title='', body=''):
        # 同 JS 回测：经数据服务转发
        return self.api(b'Mail', smtpServer, smtpUsername, smtpPassword, mailTo, title, body)

    def g_Mail_Go(self, *args):
        return AsyncRet(self.g_Mail(*args))

    def g_GetCommand(self):
        # 同实盘：没有交互命令时是 None
        return None

    def g_GetMeta(self):
        return None

    def g_SetErrorFilter(self, s):
        pass

    def g_SetChannelData(self, s):
        pass

    def g_GetChannelData(self, s=''):
        return ''

    def g_GetOS(self):
        return self.os

    def g_Version(self, detail=False):
        return self.api(b'Version', bool(detail))

    def g_IsVirtual(self):
        return True

    def g_Chart(self, js):
        return Chart(self.api, js)

    def g_KLineChart(self, js={}):
        return KLineChart(self.api, js)

    def g_GetPid(self):
        return os.getpid()

    def g__Cross(self, arr1, arr2):
        if len(arr1) != len(arr2):
            raise Exception("cross array length not equal")
        n = 0
        for i in range(len(arr1)-1, -1, -1):
            if arr1[i] is None or arr2[i] is None:
                break
            if arr1[i] < arr2[i]:
                if n > 0:
                    break
                n -= 1
            elif arr1[i] > arr2[i]:
                if n < 0:
                    break
                n += 1
            else:
                break
        return n

    def g__G(self, k='__wtf__', v='__wtf__'):
        if k == '__wtf__':
            return 1
        elif k is None:
            self.kvdb = {}
        else:
            k = k.lower()
            if v is None:
                self.kvdb.pop(k, None)
            elif v == '__wtf__':
                return self.kvdb.get(k, None)
            elif v is not None:
                self.kvdb[k] = v

    def g__CDelay(self, d):
        if d > 0:
            self.cRetryDelay = d

    def g__C(self, pfn, *arg):
        while True:
            ret = pfn(*arg)
            if ret == False or ret is None:
                self.g_Sleep(self.cRetryDelay)
            else:
                return ret
    def g__D(self, date=None, fmt=None):
        if date is None:
            date = self.g_Unix()
        if fmt is None:
            fmt = '%Y-%m-%d %H:%M:%S'
        return time.strftime(fmt, time.localtime(date))

    def g__T(self, a, b=None):
        r = str(a)
        if b is not None:
            r = str(a) + '|' + str(b)
        return '[trans]'+r+'[/trans]'

    def g__N(self, n, precision=4):
        if precision < 0:
            precision_factor = 10 ** -precision
            return n - (n % precision_factor)
        else:
            small_factor = 1 / (10 ** (max(10, precision + 5)))
            return int((n + small_factor) * (10 ** precision)) / (10 ** precision)

    def Show(self):
        import matplotlib.pyplot as plt
        from matplotlib import ticker
        try:
            from IPython import get_ipython
            get_ipython().run_line_magic('matplotlib', 'inline')
            from pandas.plotting import register_matplotlib_converters
            register_matplotlib_converters()
        except:
            pass


        def data_clean(self):
            try:
                data = json.loads(self.Join().decode('utf-8'))
            except:
                return
            dic = {}
            dic['timeStamp'] = []
            dic['assets'] = []
            dic['surplus'] = []
            dic['loss'] = []
            dic['moneyUse'] = []
            dic['unit'] = ''
            lastAssets = 0
            for i in data['Snapshots']:
                if not i[1]:
                    continue
                assets = 0
                moneyUse = 0
                for pos in range(0, len(i[1])):
                    item = i[1][pos]
                    acc = data['Task']['Exchanges'][pos]
                    position = item['Symbols']
                    if position:
                        margin = 0
                        profit = 0
                        holdSpot = 0
                        diffSpot = 0
                        for code in position:
                            if 'Long' in position[code]:
                                long = position[code]['Long']
                                margin += long['Margin']
                                profit += long['Profit']
                            if 'Short' in position[code]:
                                short = position[code]['Short']
                                margin += short['Margin']
                                profit += short['Profit']
                            if 'Stocks' in position[code]:
                                holdSpot += (position[code]['Stocks'] + position[code]['FrozenStocks']) * position[code]['Last']
                                diffSpot += (position[code]['Stocks'] + position[code]['FrozenStocks'] - acc['Stocks']) * position[code]['Last']

                        for asset in item['Assets']:
                            if item['QuoteCurrency'] == 'CNY':
                                assets += asset['Amount'] + asset['FrozenAmount'] + profit + margin
                                dic['unit'] = '(CNY)'
                            elif 'Futures_' in item['Id']:
                                if item['QuoteCurrency'] == 'USDT':
                                    assets += asset['Amount'] + asset['FrozenAmount'] + profit + margin
                                    dic['unit'] = '(USDT)'
                                else:
                                    assets += asset['Amount'] + asset['FrozenAmount'] + profit + margin
                                    dic['unit'] = '(%s)' % (item["BaseCurrency"], )
                            else:
                                assets += asset['Amount'] + asset['FrozenAmount'] + holdSpot
                                margin = abs(diffSpot)
                                dic['unit'] = '(USD)'
                            moneyUse += margin / assets if assets != 0 else 0
                dic['timeStamp'].append(datetime.datetime.fromtimestamp(i[0]/1000).date())
                dic['assets'].append(assets)
                dic['moneyUse'].append(moneyUse)
                if lastAssets != 0:
                    assetsDiff = assets - lastAssets
                    if assetsDiff > 0:
                        dic['surplus'].append(assetsDiff)
                        dic['loss'].append(0)
                    elif assetsDiff < 0:
                        dic['surplus'].append(0)
                        dic['loss'].append(assetsDiff)
                    else:
                        dic['surplus'].append(0)
                        dic['loss'].append(0)
                else:
                    dic['surplus'].append(0)
                    dic['loss'].append(0)
                lastAssets = assets
            return dic

        # plt.rcParams['font.sans-serif']=['SimHei']
        plt.rcParams['axes.unicode_minus']=False 
        
        # test
        data = data_clean(self)
        if data:
            x = data['timeStamp']
            assets = data['assets']
            surplus = data['surplus']
            loss = data['loss']
            moneyUse = data['moneyUse']
            unit = data['unit']

            plt.figure(figsize=(14, 8))
            plt.subplots_adjust(left=0.090, right=0.930)
            plt.subplots_adjust(hspace=0, wspace=0) 
            ax = plt.subplot(311) 
            plt.title(u'Backtest', fontsize=18) 
            plt.grid(linestyle='--', color='#D9D9D9')  
            plt.plot(x, assets, color='#3A859E', label=u'Equity %s %f' % (unit, assets[-1]))
            plt.fill_between(x, min(assets), assets, color='#D0DBE8', alpha=.5)
            plt.legend(loc='upper left')
            ax = plt.subplot(312)
            plt.grid(linestyle='--', color='#D9D9D9')
            plt.bar(x, surplus, color='r') 
            plt.bar(x, loss, color='g') 
            plt.legend(loc='upper left', labels=[u'Win' + unit, u'Loss' + unit])
            
            ax = plt.subplot(313)
            plt.grid(linestyle='--', color='#D9D9D9')
            plt.plot(x, moneyUse, color='#EBB000', label='Utilization')
            ax.yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))
            plt.fill_between(x, 0, moneyUse, color='#FFFBEB', alpha=.5)
            plt.legend(loc='upper left')
            # plt.get_current_fig_manager().full_screen_toggle()
            plt.show()
        else:
            print('No data')

    def Join(self, report=False):
        self.gs.acquire()
        if self._joinResult is None:
            self.lib.api_Join.restype = ctypes.c_char_p
            r = self.lib.api_Join(self.ctx)
            self.lib.api_Release(self.ctx)
            self._joinResult = r
        self.gs.release()
        time.time = self.realTime
        if not report:
            return self._joinResult
        import pandas as pd
        try:
            from pandas.plotting import register_matplotlib_converters
            register_matplotlib_converters()
        except:
            pass
        ret = json.loads(self._joinResult)
        pnl = []
        index = []
        margin_suffix = ''
        for ele in ret['Snapshots']:
            acc = ele[1][0]
            if not margin_suffix:
                margin_suffix = '(%s)' % (acc['MarginCurrency'], )
            pnl.append([acc['PnL'], acc['Utilization']*100])
            index.append(pd.Timestamp(ele[0], unit='ms', tz='Asia/Shanghai'))
        columns=["PnL"+margin_suffix, "Utilization(%)"]
        return pd.DataFrame(pnl, index=index, columns=columns)

class Backtest():
    def __init__(self, task, session):
        self.session = session
        self.task = task
        self.gApis = {}
        self.tpls = task['Code']
        del task['Code']
        self.ctx = VCtx(task = self.task, gApis = self.gApis, progressCallback = self.progressCallback)

    def progressCallback(self, st):
        if self.session is None:
            return
        self.session.sendall(struct.pack('!II', json_loads(st)['TaskStatus'], len(st)) + st)

    def waitStop(self, ctx):
        if self.session is None:
            return
        try:
            buf = b''
            ack = 0
            self.session.settimeout(None)
            while True:
                if ack > 0:
                    if len(buf) - 4 >= ack:
                        if buf[4:4+ack] == b'stop':
                            ctx.Join()
                            self.session.close()
                            os._exit(2)
                        break
                elif len(buf) >= 4:
                    ack, = struct.unpack('!I', buf[:4])
                    continue
                buf += self.session.recv((ack - (len(buf) - 4)) if ack > 0 else 4)
        except:
            pass

    def exit_handler(self, signum, frame):
        signal.signal(signal.SIGINT, signal.SIG_IGN)
        self.ctx.Join()
        self.session.shutdown(socket.SHUT_RDWR)
        os._exit(0)

    def Run(self):
        signal.signal(signal.SIGINT, self.exit_handler)
        if self.session and platform.system() == 'Windows':
            t = threading.Thread(target=self.waitStop, args=(self.ctx,))
            t.setDaemon(True)
            t.start()
        try:
            initPlot = False
            tplsLen = len(self.tpls)
            for i in xrange(0, tplsLen):
                tpl = self.tpls[i]
                vv = copy.copy(self.gApis)
                for pair in tpl[1]:
                    vv[pair[0]] = pair[1]
                code = tpl[0]+"\n\nif 'init' in locals() and callable(init):\n    init()\n"
                if i == tplsLen - 1:
                    code += "\nmain()\nif 'onexit' in globals():\n    onexit()"
                if not initPlot and 'matplotlib' in code:
                    initPlot = True
                    try:
                        __import__('matplotlib').use('Agg')
                    except:
                        pass
                exec(code.replace('\r\n', '\n'), vv)
        except (EOFError, SystemExit):
            pass
        except:
            etype, value, tb = sys.exc_info()
            arr = [x for x in traceback.extract_tb(tb) if x[0] == '<string>']
            if arr:
                tList = ['Traceback (most recent call last):\n']
                tList = tList + traceback.format_list(arr)
            else:
                tList = []
            tList = tList + traceback.format_exception_only(etype, value)
            self.ctx.g_LogError(''.join(tList))
        self.ctx.Join()
        self.session.shutdown(socket.SHUT_RDWR)

class DummySession():
    def send(self, *args):
        pass
    def sendall(self, *args):
        pass
    def close(self, *args):
        pass
    def shutdown(self, *args):
        pass

if __name__ == '__main__':
    btUUID = taskUUID()
    session = None
    if btUUID == 'dummy':
        session = gg['s']
    else:
        session = DummySession()
    if session is not None:
        Backtest(__cfg__, session).Run()


