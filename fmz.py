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
try:
    import md5
    import urllib2
except:
    import hashlib as md5
    import urllib.request as urllib2

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

def json_loads(s):
    if isPython3:
        return json.loads(s.decode('utf-8'))
    return json.loads(s)

def safe_str(s):
    if isPython3:
        return s.encode('utf-8')
    return str(s)

CLUSTER_IP = os.getenv("CLUSTER_IP", "120.27.135.154")
CLUSTER_DOMAIN = os.getenv("CLUSTER_DOMAIN", "q.botvs.net")

BT_Status = 1 << 0
BT_Symbols = 1 << 1
BT_Indicators = 1 << 2
BT_Chart = 1 << 3
BT_ProfitLogs = 1 << 4
BT_RuntimeLogs = 1 << 5
BT_CloseProfitLogs = 1 << 6
BT_Accounts = 1 << 7
BT_Accounts_PnL = 1 << 8

def getCacheDir():
    tmpCache = tempfile.gettempdir()+ '/cache'
    if not os.path.exists(tmpCache):
        try:
            os.mkdir(tmpCache)
        except:
            pass
    return tmpCache

def httpGet(url, customHost=None):
    req = urllib2.Request(url)
    req.add_header('Accept-Encoding', 'gzip, deflate')
    if customHost is not None:
        req.add_header('Host', customHost)
    resp = urllib2.urlopen(req)
    data = resp.read()
    if resp.info().get('Content-Encoding') == 'gzip':
        data = zlib.decompress(data, 16+zlib.MAX_WBITS)
    return data

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
        raise Exception('Please install %s module for python' % self.__name)

class MyList(list):
    def __init__(self, data):
        super(MyList, self).__init__(data)
        self.__data = data
    def __getattr__(self, attr):
        ret = []
        for item in self.__data:
            ret.append(item[attr])
        if HasTALib:
            ret = numpy.array(ret)
        setattr(self, attr, ret)
        return ret

HasTALib = False
try:
    import talib
    import numpy
    HasTALib = True
except ImportError:
    talib = DummyModule('talib')

API_ERR_SUCCESS = 0
API_ERR_FAILED = -1
API_ERR_EOF = -2

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

def JoinArgs(args):
    arr = []
    for item in args:
        if hasattr(item, 'savefig') and callable(item.savefig):
            d = io.BytesIO()
            item.savefig(d, format="png")
            arr.append('`data:image/png;base64,%s`'%(base64.b64encode(d.getvalue()).decode('utf-8')))
        elif isinstance(item, dict) and item.get('type') == 'table' and item.get('cols'):
            arr.append('`%s`' % json.dumps(item))
        else:
            arr.append(str(item))
    return safe_str(' '.join(arr))

class _CSTRUCT(ctypes.Structure):
    def toObj(self):
        obj = {}
        for k, v in self._fields_:
            obj[k] = getattr(self, k)
        return dic2obj(obj)

class _TICKER(_CSTRUCT):
    _fields_ = [("Time", ctypes.c_ulonglong), 
            ("High", ctypes.c_double), 
            ("Low", ctypes.c_double), 
            ("Sell", ctypes.c_double), 
            ("Buy", ctypes.c_double), 
            ("Last", ctypes.c_double), 
            ("Volume", ctypes.c_double)]

class _RECORD(_CSTRUCT):
    _fields_ = [("Time", ctypes.c_ulonglong), 
            ("Open", ctypes.c_double), 
            ("High", ctypes.c_double), 
            ("Low", ctypes.c_double), 
            ("Close", ctypes.c_double), 
            ("Volume", ctypes.c_double)]

class _MARKET_ORDER(_CSTRUCT):
    _fields_ = [("Price", ctypes.c_double), ("Amount", ctypes.c_double)]

class _ACCOUNT(_CSTRUCT):
    _fields_ = [("Balance", ctypes.c_double), 
            ("FrozenBalance", ctypes.c_double), 
            ("Stocks", ctypes.c_double), 
            ("FrozenStocks", ctypes.c_double)]

class _ORDER(_CSTRUCT):
    _fields_ = [("Id", ctypes.c_ulonglong), 
            ("Price", ctypes.c_double), 
            ("Amount", ctypes.c_double), 
            ("DealAmount", ctypes.c_double), 
            ("AvgPrice", ctypes.c_double), 
            ("Type", ctypes.c_uint), 
            ("Status", ctypes.c_uint), 
            ("ContractType", ctypes.c_char * 31)]

class _POSITION(_CSTRUCT):
    _fields_ = [("MarginLevel", ctypes.c_ulonglong), 
            ("Amount", ctypes.c_double), 
            ("FrozenAmount", ctypes.c_double), 
            ("Price", ctypes.c_double), 
            ("Profit", ctypes.c_double), 
            ("Margin", ctypes.c_double), 
            ("Type", ctypes.c_uint), 
            ("ContractType", ctypes.c_char * 31)]
def EOF():
    raise EOFError()

class AsyncRet:
    routineId = 0
    def __init__(self, v):
        self.isWait = False
        self.v = v
        AsyncRet.routineId += 1

    def wait(self, timeout=-1):
        if self.isWait:
            return (None, False)
        self.isWait = True
        return (self.v, True)

    def __repr__(self):
        return '<Go %d>' % AsyncRet.routineId

class Exchange:
    def __init__(self, lib, ctx, idx, opt, cfg):
        self.lib = lib
        self.ctx = ctx
        self.idx = ctypes.c_int(idx)
        self.opt = opt
        self.cfg = cfg
        self.name = cfg["Id"]
        self.label = cfg["Label"]
        self.currency = '%s_%s' % (cfg["BaseCurrency"], cfg["QuoteCurrency"])
        self.quoteCurrency = cfg["QuoteCurrency"]
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

    def GetQuoteCurrency(self):
        return self.quoteCurrency

    def GetUSDCNY(self):
        self.lib.api_Exchange_GetUSDCNY.restype = ctypes.c_double
        return self.lib.api_Exchange_GetUSDCNY(self.ctx, self.idx)

    def SetPrecision(self, a, b):
        pass

    def GetRate(self):
        self.lib.api_Exchange_GetRate.restype = ctypes.c_double
        return self.lib.api_Exchange_GetRate(self.ctx, self.idx)

    def SetProxy(self, s):
        pass

    def SetTimeout(self, ms):
        pass

    def SetRate(self, rate=1.0):
        self.lib.api_Exchange_SetRate.restype = ctypes.c_double
        return self.lib.api_Exchange_SetRate(self.ctx, self.idx, ctypes.c_double(rate))

    def GetTrades(self):
        return []

    def GetTicker(self):
        r = _TICKER()
        ret = self.lib.api_Exchange_GetTicker(self.ctx, self.idx, ctypes.byref(r))
        if ret == API_ERR_SUCCESS:
            return r.toObj()
        elif ret == API_ERR_FAILED:
            return None
        EOF()

    def IO(self, k, v = 0):
        return self.lib.api_Exchange_IO(self.ctx, self.idx, str(k), int(v))

    def GetDepth(self):
        ask_len = ctypes.c_uint(0)
        bid_len = ctypes.c_uint(0)
        buf_ptr = ctypes.c_void_p()
        ret = self.lib.api_Exchange_GetDepth(self.ctx, self.idx, ctypes.byref(ask_len), ctypes.byref(bid_len), ctypes.byref(buf_ptr))

        if ret == API_ERR_SUCCESS:
            n = ask_len.value + bid_len.value
            asks = []
            bids = []
            if n > 0:
                group_array = (_MARKET_ORDER * n).from_address(buf_ptr.value)
                for i in range(0, n):
                    if i < ask_len.value:
                        asks.append(group_array[i].toObj())
                    else:
                        bids.append(group_array[i].toObj())
                self.lib.api_free(buf_ptr)
            return dic2obj({'Asks': asks, 'Bids': bids})
        elif ret == API_ERR_FAILED:
            return None
        EOF()

    def GetRecords(self, period=-1):
        if period == -1:
            period = self.period
        r_len = ctypes.c_uint(0)
        buf_ptr = ctypes.c_void_p()
        ret = self.lib.api_Exchange_GetRecords(self.ctx, self.idx, ctypes.c_long(period), ctypes.byref(r_len), ctypes.byref(buf_ptr))

        if ret == API_ERR_SUCCESS:
            n = r_len.value
            eles = []
            if n > 0:
                group_array = (_RECORD * n).from_address(buf_ptr.value)
                for i in range(0, n):
                    eles.append(group_array[i].toObj())
                self.lib.api_free(buf_ptr)
            k = '%s/%d' % (self.ct, period)
            c = self.records_cache.get(k, None)
            if c is None or len(c) == 0:
                self.records_cache[k] = eles
            else:
                preTime = 0 if len(c) == 0 else c[-1]['Time']
                for ele in eles:
                    t = ele['Time']
                    if t == preTime:
                        c[-1] = ele
                    elif t > preTime:
                        c.append(ele)
                        preTime = t
            return MyList(self.records_cache[k])
        elif ret == API_ERR_FAILED:
            return None
        EOF()

    def GetAccount(self):
        r = _ACCOUNT()
        ret = self.lib.api_Exchange_GetAccount(self.ctx, self.idx, ctypes.byref(r))
        if ret == API_ERR_SUCCESS:
            return r.toObj()
        elif ret == API_ERR_FAILED:
            return None
        EOF()

    def Buy(self, price, amount=None, *extra):
        ret = self.lib.api_Exchange_Trade(self.ctx, self.idx, 0, ctypes.c_double(price), ctypes.c_double(amount), JoinArgs(extra))
        if ret > 0:
            return int(ret)
        elif ret == API_ERR_FAILED:
            return None
        EOF()

    def Sell(self, price, amount=None, *extra):
        ret = self.lib.api_Exchange_Trade(self.ctx, self.idx, 1, ctypes.c_double(price), ctypes.c_double(amount), JoinArgs(extra))
        if ret > 0:
            return int(ret)
        elif ret == API_ERR_FAILED:
            return None
        EOF()

    def GetOrders(self):
        r_len = ctypes.c_uint(0)
        buf_ptr = ctypes.c_void_p()
        ret = self.lib.api_Exchange_GetOrders(self.ctx, self.idx, ctypes.byref(r_len), ctypes.byref(buf_ptr))

        if ret == API_ERR_SUCCESS:
            n = r_len.value
            eles = []
            if n > 0:
                group_array = (_ORDER * n).from_address(buf_ptr.value)
                for i in range(0, n):
                    eles.append(group_array[i].toObj())
                self.lib.api_free(buf_ptr)
            return eles
        elif ret == API_ERR_FAILED:
            return None
        EOF()

    def GetOrder(self, orderId):
        r = _ORDER()
        ret = self.lib.api_Exchange_GetOrder(self.ctx, self.idx, ctypes.c_int(orderId), ctypes.byref(r))
        if ret == API_ERR_SUCCESS:
            return r.toObj()
        elif ret == API_ERR_FAILED:
            return None
        EOF()

    def CancelOrder(self, orderId, *extra):
        self.lib.api_Exchange_CancelOrder.restype = ctypes.c_bool
        ret = self.lib.api_Exchange_CancelOrder(self.ctx, self.idx, ctypes.c_int(orderId), JoinArgs(extra))
        if ret == API_ERR_EOF:
            EOF()
        return ret == API_ERR_SUCCESS

    def SetContractType(self, symbol):
        r = ctypes.c_char_p()
        ret = self.lib.api_Exchange_SetContractType(self.ctx, self.idx, safe_str(symbol), ctypes.byref(r))
        if ret == API_ERR_SUCCESS:
            self.ct = symbol
            if r:
                detail = json_loads(r.value)
                self.lib.api_free(r)
                return detail
            else:
                return True
        elif ret == API_ERR_FAILED:
            return None
        EOF()

    def SetMarginLevel(self, level):
        self.lib.api_Exchange_SetMarginLevel.restype = ctypes.c_bool
        return self.lib.api_Exchange_SetMarginLevel(self.ctx, self.idx, ctypes.c_int(level))

    def SetDirection(self, direction):
        self.lib.api_Exchange_SetMarginLevel.restype = ctypes.c_bool
        return self.lib.api_Exchange_SetDirection(self.ctx, self.idx, safe_str(direction))

    def GetPosition(self):
        r_len = ctypes.c_uint(0)
        buf_ptr = ctypes.c_void_p()
        ret = self.lib.api_Exchange_GetPosition(self.ctx, self.idx, ctypes.byref(r_len), ctypes.byref(buf_ptr))

        if ret == API_ERR_SUCCESS:
            n = r_len.value
            eles = []
            if n > 0:
                group_array = (_POSITION * n).from_address(buf_ptr.value)
                for i in range(0, n):
                    eles.append(group_array[i].toObj())
                self.lib.api_free(buf_ptr)
            return eles
        elif ret == API_ERR_FAILED:
            return None
        EOF()

class Chart(object):
    def __init__(self, lib, ctx, js):
        self.lib = lib
        self.ctx = ctx
        self.lib.api_Chart_New(self.ctx, safe_str(json.dumps(js)))

    def update(self, js):
        self.lib.api_Chart_New(self.ctx, safe_str(json.dumps(js)))

    def add(self, seriesIdx, d, replaceId=None):
        obj = [seriesIdx, d]
        if replaceId is not None:
            obj.append(replaceId)
        self.lib.api_Chart_Add(self.ctx, safe_str(json.dumps(obj)))

    def reset(self, keep=0):
        self.lib.api_Chart_Reset(self.ctx, keep)

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
    period = 60000 * 60
    periodStr = dic.get('period', '1h')
    tmp = int(periodStr[:-1])
    c = periodStr[-1]
    if c == 'd':
        period = tmp * 60000 * 60 * 24
    elif c == 'm':
        period = tmp * 60000
    elif c == 'm':
        period = tmp * 60000

    exchanges = []
    for e in json.loads(dic.get('exchanges', '[]')):
        arr = e['currency'].upper().split('_')
        if len(arr) == 1:
            arr.append('CNY' if 'CTP' in e['eid'] else 'USD')
        basePeriod = 60000 * 60
        if periodStr == '1d':
            basePeriod = 60000 * 60
        elif periodStr == '1h' or periodStr == '60m':
            basePeriod = 60000 * 30
        elif periodStr == '30m':
            basePeriod = 60000 * 15
        elif periodStr == '15m':
            basePeriod = 60000 * 5
        elif periodStr == '5m':
            basePeriod = 60000

        cfg = {
		"Balance": e.get('balance', 20000.0),
		"BaseCurrency": arr[0],
		"BasePeriod": e.get('baseperiod', basePeriod),
		"BasePrecision": 4,
		"DepthDeep": 5,
		"FaultTolerant": 0,
		"FeeDenominator": 5,
		"FeeMaker": e.get('feemaker', 75),
		"FeeTaker": e.get('feetaker', 80),
		"FeeMin": e.get('feemin', 0),
		"Id": e['eid'],
		"Label": e['eid'],
		"PriceTick": 1e-05,
		"QuoteCurrency": arr[1],
		"QuotePrecision": 8,
		"SlipPoint": 0,
		"Stocks": e.get('stocks', 6.0)
	}
        if e['eid'] == 'Futures_CTP':
            cfg['BasePrecision'] = 0
            cfg['QuotePrecision'] = 1
            cfg['DepthDeep'] = 1
        elif e['eid'] == 'Futures_OKCoin':
            cfg['BasePrecision'] = 0
            cfg['QuotePrecision'] = 5
        elif e['eid'] == 'Bitfinex':
            cfg['BasePrecision'] = 4
            cfg['QuotePrecision'] = 4
            cfg['PriceTick'] = 0.001
        elif e['eid'] == 'OKCoin_EN':
            cfg['BasePrecision'] = 3
            cfg['QuotePrecision'] = 3
            cfg['PriceTick'] = 0.01
        elif 'Futures' not in e['eid']:
            cfg['BasePrecision'] = 4
            cfg['QuotePrecision'] = 8
            cfg['PriceTick'] = 0.00000001
        exchanges.append(cfg)

    options = {
		"DataServer": "q.botvs.net",
		"MaxChartLogs": 800,
		"MaxProfitLogs": 800,
		"MaxRuntimeLogs": 800,
		"NetDelay": 200,
		"Period": period,
		"RetFlags": BT_Status | BT_Indicators | BT_Accounts | BT_Chart | BT_RuntimeLogs | BT_ProfitLogs,
		"SnapshortPeriod": basePeriod,
		"TimeBegin": int(time.mktime(datetime.datetime.strptime(dic.get('start', '2018-02-01 00:00:00'), "%Y-%m-%d %H:%M:%S").timetuple())),
		"TimeEnd": int(time.mktime(datetime.datetime.strptime(dic.get('end', '2018-02-05 00:00:00'), "%Y-%m-%d %H:%M:%S").timetuple())),
		"UpdatePeriod": 5000
	}
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
        if osName == 'Linux' and hasattr(os, 'uname') and 'arm' in os.uname()[4]:
            archName = 'arm'
        self.os = '%s/%s' % (osName.lower(), 'amd64' if archName == '64bit' else '386')
        soName = 'backtest_py_%s_%s.so' % (osName.lower(), archName)
        loader = os.path.join("./depends", soName)
        if not os.path.exists(loader):
            hdic = {}
            tmpCache = getCacheDir()
            js = os.path.join(tmpCache, 'md5.json')
            if os.path.exists(js):
                b = open(js, 'rb').read()
                if os.getenv("BOTVS_TASK_UUID") is None or "0e3386dac1844fe4728c0cdce13fa157" in str(b):
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
                open(loader, 'wb').write(httpGet("http://" + CLUSTER_IP + "/dist/depends/" + soName, CLUSTER_DOMAIN))
                open(js, 'wb').write(httpGet("http://" + CLUSTER_IP + "/dist/depends/md5.json", CLUSTER_DOMAIN))
        #declare
        lib = ctypes.CDLL(loader)
        lib.api_backtest.restype = ctypes.c_void_p
        ctx = ctypes.c_void_p(lib.api_backtest(json.dumps(task).encode('utf8'), self.httpGetPtr, self.progessCallbackPtr))
        if not ctx:
            raise 'Initialize backtest engine error'
        self.ctx = ctx
        self.lib = lib
        self.cache = {}
        self.kvdb = {}
        self.cRetryDelay = 3000
        # HOOK
        exchanges = []
        i = 0
        for ele in task["Exchanges"]:
            exchanges.append(Exchange(lib, ctx, i, task["Options"], ele))
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

        gApis["PERIOD_M1"] = 60000 * 1
        gApis["PERIOD_M3"] = 60000 * 3
        gApis["PERIOD_M5"] = 60000 * 5
        gApis["PERIOD_M15"] = 60000 * 15
        gApis["PERIOD_M30"] = 60000 * 30
        gApis["PERIOD_H1"]  = 60000 * 60
        gApis["PERIOD_D1"]  = 60000 * 60 * 24
        gApis["PERIOD_W1"]  = 60000 * 60 * 24  * 7
        if autoRun:
            try:
                gApis['main']()
            except EOFError:
                pass
            self.Join()

    def update(self):
        try:
            os.remove(os.path.join(getCacheDir(), 'md5.json'))
        except:
            pass

    def httpGetCallback(self, path, ptr_buf, ptr_size, ptr_need_free):
        url = 'http://' + CLUSTER_IP + path.decode('utf8')
        tmpCache = getCacheDir()
        cacheFile = tmpCache+'/botvs_kline_'+md5.md5(path).hexdigest()
        data = None
        try:
            if os.path.exists(cacheFile):
                data = open(cacheFile, 'rb').read()
                cacheFile = None
            else:
                data = httpGet(url, CLUSTER_DOMAIN)
                if len(data) > 0:
                    open(cacheFile, 'wb').write(data)
        except:
            pass
        if data is None:
            return 1
        ptr_size.contents.value = len(data)
        ptr_need_free.contents.value = 0
        str_buf = ctypes.create_string_buffer(data)
        ptr_buf.contents.value = ctypes.addressof(str_buf)
        self.cache[cacheFile] = str_buf #prevent to release
        return 0

    def progressCallback(self, st):
        pass

    def _logTA(self, name, args):
        self.lib.api_LogTA(self.ctx, name, args)

    def g_Unix(self):
        self.lib.api_Unix.restype = ctypes.c_ulonglong
        return self.lib.api_Unix(self.ctx)

    def g_UnixNano(self):
        self.lib.api_UnixNano.restype = ctypes.c_ulonglong
        return self.lib.api_UnixNano(self.ctx)

    def g_PyTime(self):
        return float(self.g_UnixNano())/1e9

    def g_Sleep(self, n):
        if self.lib.api_Sleep(self.ctx, ctypes.c_double(n)) != 0:
            EOF()

    def g_EnableLog(self, flag = True):
        self.lib.api_EnableLog(self.ctx, ctypes.c_bool(flag))

    def g_Log(self, *extra):
        self.lib.api_Log(self.ctx, JoinArgs(extra))
        
    def g_LogReset(self, keep = 0):
        self.lib.api_LogReset(self.ctx, ctypes.c_int(keep))

    def g_LogStatus(self, *extra):
        self.lib.api_LogStatus(self.ctx, JoinArgs(extra))

    def g_LogProfit(self, profit, *extra):
        self.lib.api_LogProfit(self.ctx, ctypes.c_double(profit), JoinArgs(extra))

    def g_LogProfitReset(self, keep = 0):
        self.lib.api_LogProfitReset(self.ctx, ctypes.c_int(keep))

    def g_LogError(self, *extra):
        self.lib.api_LogError(self.ctx, JoinArgs(extra))

    def g_Panic(self, *extra):
        self.lib.api_LogError(self.ctx, JoinArgs(extra))
        EOF()

    def g_GetLastError(self):
        return ''

    def g_MD5(self, s):
        return md5.md5(s).hexdigest()

    def g_HttpQuery(self, *args):
        return 'dummy'

    def g_EnableLogLocal(self, b):
        pass

    def g_Dial(self, *args):
        self.g_LogError("sandbox not support Dial")

    def g_Mail(self, *args):
        return True

    def g_GetCommand(self):
        return None

    def g_SetErrorFilter(self, s):
        pass

    def g_GetOS(self):
        return self.os

    def g_Version(self):
        return '3.3'

    def g_IsVirtual(self):
        return True

    def g_Chart(self, js):
        return Chart(self.lib, self.ctx, js)

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
                if hasattr(self.kvdb, k):
                    delattr(self.kvdb, k)
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

    def g__N(self, n, precision=4):
        d = pow(10, precision)
        return int(n*d) / float(d)

    def Join(self):
        self.gs.acquire()
        if self._joinResult is None:
            self.lib.api_Join.restype = ctypes.c_char_p
            r = self.lib.api_Join(self.ctx)
            self.lib.api_Release(self.ctx)
            self._joinResult = r
        self.gs.release()
        time.time = self.realTime
        return self._joinResult

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
    uuid = os.getenv("BOTVS_TASK_UUID")
    session = None
    if uuid == 'dummy':
        session = s
    else:
        session = DummySession()
    if session is not None:
        Backtest(__cfg__, session).Run()
