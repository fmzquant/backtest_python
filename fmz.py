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

def getCacheDir():
    tmpCache = tempfile.gettempdir()+ '/cache'
    if not os.path.exists(tmpCache):
        try:
            os.mkdir(tmpCache)
        except:
            pass
    return tmpCache

def httpGet(url):
    try:
        req = urllib2.Request(url)
        req.add_header('Accept-Encoding', 'gzip, deflate')
        resp = urllib2.urlopen(req)
        data = resp.read()
        if resp.info().get('Content-Encoding') == 'gzip':
            data = zlib.decompress(data, 16+zlib.MAX_WBITS)
        return data
    except urllib2.HTTPError as e:
        headers = dict(e.info())
        error_body = e.read()
        if e.info().get('Content-Encoding') == 'gzip':
            try:
                error_body = zlib.decompress(error_body, 16+zlib.MAX_WBITS)
            except:
                pass
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
        for k, t in self._fields_:
            if k[0].isupper():
                v = getattr(self, k)
                if k == 'Info' and hasattr(v, 's_js'):
                    if v.s_js_size > 0:
                        v = json.loads(v.s_js[:v.s_js_size])
                    else:
                        v = None
                if isinstance(v, bytes):
                    v = v.decode()
                obj[k] = v
        return dic2obj(obj)

class _INFO(_CSTRUCT):
    _fields_ = [("s_js", ctypes.c_char_p),
            ("s_js_size", ctypes.c_uint)]

class _TICKER(_CSTRUCT):
    _fields_ = [("Time", ctypes.c_ulonglong), 
            ("Symbol", ctypes.c_char * 31),
            ("Open", ctypes.c_double), 
            ("High", ctypes.c_double), 
            ("Low", ctypes.c_double), 
            ("Sell", ctypes.c_double), 
            ("Buy", ctypes.c_double), 
            ("Last", ctypes.c_double), 
            ("Volume", ctypes.c_double),
            ("OpenInterest", ctypes.c_double),
            ("Info", _INFO)]

class _FUNDING(_CSTRUCT):
    _fields_ = [("Time", ctypes.c_ulonglong), 
            ("Rate", ctypes.c_double), 
            ("Interval", ctypes.c_uint), 
            ("Symbol", ctypes.c_char * 31)]

class _RECORD(_CSTRUCT):
    _fields_ = [("Time", ctypes.c_ulonglong), 
            ("Open", ctypes.c_double), 
            ("High", ctypes.c_double), 
            ("Low", ctypes.c_double), 
            ("Close", ctypes.c_double), 
            ("Volume", ctypes.c_double), 
            ("OpenInterest", ctypes.c_double)]

class _MARKET_ORDER(_CSTRUCT):
    _fields_ = [("Price", ctypes.c_double), ("Amount", ctypes.c_double)]

class _ACCOUNT(_CSTRUCT):
    _fields_ = [("Balance", ctypes.c_double), 
            ("FrozenBalance", ctypes.c_double), 
            ("Stocks", ctypes.c_double), 
            ("FrozenStocks", ctypes.c_double),
            ("Equity", ctypes.c_double), 
            ("UPnL", ctypes.c_double)]

class _ASSET(_CSTRUCT):
    _fields_ = [("Currency", ctypes.c_char * 31), 
            ("Amount", ctypes.c_double), 
            ("FrozenAmount", ctypes.c_double)]

class _ORDER(_CSTRUCT):
    _fields_ = [("Id", ctypes.c_ulonglong), 
            ("Price", ctypes.c_double), 
            ("Amount", ctypes.c_double), 
            ("DealAmount", ctypes.c_double), 
            ("AvgPrice", ctypes.c_double), 
            ("Type", ctypes.c_uint), 
            ("Offset", ctypes.c_uint), 
            ("Status", ctypes.c_uint), 
            ("Symbol", ctypes.c_char * 31),
            ("ContractType", ctypes.c_char * 31)]

class _TRADE(_CSTRUCT):
    _fields_ = [("Id", ctypes.c_ulonglong), 
            ("Time", ctypes.c_ulonglong),
            ("Price", ctypes.c_double), 
            ("Amount", ctypes.c_double),
            ("Type", ctypes.c_uint)] 

class _POSITION(_CSTRUCT):
    _fields_ = [("MarginLevel", ctypes.c_double), 
            ("Amount", ctypes.c_double), 
            ("FrozenAmount", ctypes.c_double), 
            ("Price", ctypes.c_double), 
            ("Profit", ctypes.c_double), 
            ("Margin", ctypes.c_double), 
            ("Type", ctypes.c_uint), 
            ("Symbol", ctypes.c_char * 31),
            ("ContractType", ctypes.c_char * 31)]
def EOF():
    raise EOFError()

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
    def __init__(self, lib, ctx, idx, opt, cfg):
        self.lib = lib
        self.ctx = ctx
        self.idx = ctypes.c_int(idx)
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
        self.lib.api_Exchange_GetUSDCNY.restype = ctypes.c_double
        return self.lib.api_Exchange_GetUSDCNY(self.ctx, self.idx)

    def SetMaxBarLen(self, n):
        self.maxBarLen = n

    def SetPrecision(self, a, b):
        self.lib.api_Exchange_SetPrecision(self.ctx, self.idx, ctypes.c_double(a), ctypes.c_double(b))

    def GetRate(self):
        self.lib.api_Exchange_GetRate.restype = ctypes.c_double
        return self.lib.api_Exchange_GetRate(self.ctx, self.idx)

    def SetProxy(self, s):
        pass

    def SetTimeout(self, ms):
        pass

    def SetBase(self, s):
        r = ctypes.c_char_p()
        self.lib.api_Exchange_SetBase(self.ctx, self.idx, safe_str(s), ctypes.byref(r))
        detail = b2s(r.value)
        self.lib.api_free(r)
        return detail

    def GetBase(self):
        r = ctypes.c_char_p()
        self.lib.api_Exchange_GetBase(self.ctx, self.idx, ctypes.byref(r))
        detail = b2s(r.value)
        self.lib.api_free(r)
        return detail

    def SetCurrency(self, s):
        arr = s.split('_')
        if len(arr) == 2:
            self.currency = s
            self.quoteCurrency = arr[1]
            return self.lib.api_Exchange_SetCurrency(self.ctx, self.idx, safe_str(s))

    def SetRate(self, rate=1.0):
        self.lib.api_Exchange_SetRate.restype = ctypes.c_double
        return self.lib.api_Exchange_SetRate(self.ctx, self.idx, ctypes.c_double(rate))

    def GetTrades(self, symbol=''):
        r_len = ctypes.c_uint(0)
        buf_ptr = ctypes.c_void_p()
        ret = self.lib.api_Exchange_GetTrades(self.ctx, self.idx, safe_str(symbol), ctypes.byref(r_len), ctypes.byref(buf_ptr))

        if ret == API_ERR_SUCCESS:
            n = r_len.value
            eles = []
            if n > 0:
                group_array = (_TRADE * n).from_address(buf_ptr.value)
                for i in range(0, n):
                    eles.append(group_array[i].toObj())
                self.lib.api_free(buf_ptr)
            return eles
        elif ret == API_ERR_FAILED:
            return None
        EOF()

    def SetData(self, name, data):
        if not isinstance(data, string_types):
            data = json.dumps(data)
        return self.lib.api_Exchange_SetData(self.ctx, self.idx, safe_str(name), safe_str(data))

    def GetData(self, name, timeout=60000, offset=0):
        r = _TICKER()
        ret = self.lib.api_Exchange_GetData(self.ctx, self.idx, ctypes.byref(r), safe_str(name), int(timeout), int(offset))
        if ret == API_ERR_SUCCESS:
            return dic2obj({'Time': r.Time, 'Data': json.loads(r.Info.s_js[:r.Info.s_js_size]) if r.Info.s_js_size > 0 else None})
        elif ret == API_ERR_FAILED:
            return None
        EOF()

    def GetTickers(self):
        r_len = ctypes.c_uint(0)
        buf_ptr = ctypes.c_void_p()
        ret = self.lib.api_Exchange_GetTickers(self.ctx, self.idx, ctypes.byref(r_len), ctypes.byref(buf_ptr))

        if ret == API_ERR_SUCCESS:
            n = r_len.value
            eles = []
            if n > 0:
                group_array = (_TICKER * n).from_address(buf_ptr.value)
                for i in range(0, n):
                    eles.append(group_array[i].toObj())
                self.lib.api_free(buf_ptr)
            return eles
        elif ret == API_ERR_FAILED:
            return None
        EOF()

    def GetMarkets(self):
        r = ctypes.c_char_p()
        self.lib.api_Exchange_GetMarkets(self.ctx, self.idx, ctypes.byref(r))
        ret = json.loads(b2s(r.value))
        self.lib.api_free(r)
        return ret


    def GetTicker(self, symbol=''):
        r = _TICKER()
        ret = self.lib.api_Exchange_GetTicker(self.ctx, self.idx, safe_str(symbol), ctypes.byref(r))
        if ret == API_ERR_SUCCESS:
            return r.toObj()
        elif ret == API_ERR_FAILED:
            return None
        EOF()

    def GetFundings(self, symbol=''):
        r_len = ctypes.c_uint(0)
        buf_ptr = ctypes.c_void_p()
        ret = self.lib.api_Exchange_GetFundings(self.ctx, self.idx, safe_str(symbol), ctypes.byref(r_len), ctypes.byref(buf_ptr))

        if ret == API_ERR_SUCCESS:
            n = r_len.value
            eles = []
            if n > 0:
                group_array = (_FUNDING * n).from_address(buf_ptr.value)
                for i in range(0, n):
                    eles.append(group_array[i].toObj())
                self.lib.api_free(buf_ptr)
            return eles
        elif ret == API_ERR_FAILED:
            return None
        EOF()

    def IO(self, k, v = 0):
        if k == 'currency':
            return self.SetCurrency(v)
        return self.lib.api_Exchange_IO(self.ctx, self.idx, safe_str(k), int(v))

    def GetDepth(self, symbol=''):
        ask_len = ctypes.c_uint(0)
        bid_len = ctypes.c_uint(0)
        buf_ptr = ctypes.c_void_p()
        ret = self.lib.api_Exchange_GetDepth(self.ctx, self.idx, safe_str(symbol), ctypes.byref(ask_len), ctypes.byref(bid_len), ctypes.byref(buf_ptr))

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

    def GetRecords(self, symbol='', period=-1, limit=0):
        if isinstance(symbol, int):
            limit = period
            period = symbol
            symbol = ''
        if period == -1:
            period = int(self.period/1000)
        r_len = ctypes.c_uint(0)
        buf_ptr = ctypes.c_void_p()
        ret = self.lib.api_Exchange_GetRecords(self.ctx, self.idx, safe_str(symbol), ctypes.c_long(int(period)), ctypes.c_long(int(limit)), ctypes.byref(r_len), ctypes.byref(buf_ptr))

        if ret == API_ERR_SUCCESS:
            n = r_len.value
            eles = []
            if n > 0:
                group_array = (_RECORD * n).from_address(buf_ptr.value)
                for i in range(0, n):
                    eles.append(group_array[i].toObj())
                self.lib.api_free(buf_ptr)
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
                r = r[-limit:]
            return r
        elif ret == API_ERR_FAILED:
            return None
        EOF()

    def GetAssets(self):
        r_len = ctypes.c_uint(0)
        buf_ptr = ctypes.c_void_p()
        ret = self.lib.api_Exchange_GetAssets(self.ctx, self.idx, ctypes.byref(r_len), ctypes.byref(buf_ptr))

        if ret == API_ERR_SUCCESS:
            n = r_len.value
            eles = []
            if n > 0:
                group_array = (_ASSET * n).from_address(buf_ptr.value)
                for i in range(0, n):
                    eles.append(group_array[i].toObj())
                self.lib.api_free(buf_ptr)
            return eles
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

    def CreateOrder(self, symbol, side, price, amount=None, *extra):
        ret = self.lib.api_Exchange_CreateOrder(self.ctx, self.idx, safe_str(symbol), safe_str(side), ctypes.c_double(price), ctypes.c_double(amount), JoinArgs(extra))
        if ret > 0:
            return int(ret)
        elif ret == API_ERR_FAILED:
            return None
        EOF()

    def GetOrders(self, symbol=''):
        r_len = ctypes.c_uint(0)
        buf_ptr = ctypes.c_void_p()
        ret = self.lib.api_Exchange_GetOrders(self.ctx, self.idx, safe_str(symbol), ctypes.byref(r_len), ctypes.byref(buf_ptr))

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

    def GetHistoryOrders(self, symbol='', since=0, limit = 0):
        if isinstance(symbol, int):
            limit = since
            since = symbol
            symbol = ''
        r_len = ctypes.c_uint(0)
        buf_ptr = ctypes.c_void_p()
        ret = self.lib.api_Exchange_GetHistoryOrders(self.ctx, self.idx, safe_str(symbol), ctypes.c_longlong(since), ctypes.c_longlong(limit), ctypes.byref(r_len), ctypes.byref(buf_ptr))

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

    def Log(self, orderType, price, amount=0, *extra):
        ret = self.lib.api_Exchange_Log(self.ctx, self.idx, ctypes.c_int(orderType), ctypes.c_double(price), ctypes.c_double(amount), JoinArgs(extra))
        if orderType == 2:
            return bool(ret)
        if ret > 0:
            return int(ret)

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

    def GetContractType(self):
        return self.ct

    def GetPeriod(self):
        return int(self.period/1000)

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

    def SetMarginLevel(self, symbol, level=None):
        if isinstance(symbol, int) or isinstance(symbol, float):
            level, symbol = symbol, level
        if not symbol:
            symbol = ''
        self.lib.api_Exchange_SetMarginLevel.restype = ctypes.c_bool
        return self.lib.api_Exchange_SetMarginLevel(self.ctx, self.idx, safe_str(symbol), ctypes.c_int(level))

    def SetDirection(self, direction):
        self.lib.api_Exchange_SetMarginLevel.restype = ctypes.c_bool
        return self.lib.api_Exchange_SetDirection(self.ctx, self.idx, safe_str(direction))

    def GetPositions(self, symbol=''):
        r_len = ctypes.c_uint(0)
        buf_ptr = ctypes.c_void_p()
        ret = self.lib.api_Exchange_GetPositions(self.ctx, self.idx, safe_str(symbol), ctypes.byref(r_len), ctypes.byref(buf_ptr))

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

    def GetPosition(self):
        return self.GetPositions()

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

class KLineChart():
    def __init__(self, lib, ctx, options={}):
        options["__isCandle"] = True
        self.chart = Chart(lib, ctx, options)
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

    def close(self):
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
        if platform.processor() == "arm":
            archName = 'arm64' if archName == '64bit' else 'arm'
        self.os = '%s/%s' % (osName.lower(), archName)
        soName = 'backtest_py_%s_%s_v2.so' % (osName.lower(), archName)
        crcFile = 'md5_v2.json'
        loader = os.path.join("./depends", soName)
        if not os.path.exists(loader):
            hdic = {}
            tmpCache = getCacheDir()
            js = os.path.join(tmpCache, crcFile)
            if os.path.exists(js):
                b = open(js, 'rb').read()
                if os.getenv("BOTVS_TASK_UUID") is None or "9b260c082670ed9bba9d36c33290ee63" in str(b):
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
                open(loader, 'wb').write(httpGet(task["Options"]["DataServer"] + "/dist/depends/" + soName))
                open(js, 'wb').write(httpGet(task["Options"]["DataServer"] + "/dist/depends/" + crcFile))
        else:
            print("load from debug mode", loader)
        lib = ctypes.CDLL(os.path.abspath(loader))
        lib.api_backtest.restype = ctypes.c_void_p
        ctx = ctypes.c_void_p(lib.api_backtest(safe_str(json.dumps(task)), self.httpGetPtr, self.progessCallbackPtr, None))
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
        gApis["ORDER_OFFSET_OPEN"] = 0
        gApis["ORDER_OFFSET_CLOSE"] = 1

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
        url = path.decode('utf8')
        tmpCache = getCacheDir()
        cacheFile = tmpCache+'/botvs_kline_'+md5.md5(path).hexdigest()
        data = None
        try:
            if os.path.exists(cacheFile):
                data = open(cacheFile, 'rb').read()
                cacheFile = None
            else:
                data = httpGet(url)
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

    def g_LogVacuum(self):
        pass

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
        return md5.md5(safe_str(s)).hexdigest()

    def g_HttpQuery(self, *args):
        return 'dummy'

    def g_HttpQuery_Go(self, *args):
        return AsyncRet('dummy')

    def g_JSONParse(self, s):
        return json.loads(s)

    def g_UUID(self):
        return str(uuid.uuid4())

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

    def g_Mail(self, *args):
        return True

    def g_Mail_Go(self, *args):
        return AsyncRet(True)

    def g_GetCommand(self):
        return ''

    def g_GetMeta(self):
        return None

    def g_SetErrorFilter(self, s):
        pass

    def g_SetChannelData(self, s):
        pass

    def g_GetChannelData(self, s):
        return ''

    def g_GetOS(self):
        return self.os

    def g_Version(self):
        return '3.3'

    def g_IsVirtual(self):
        return True

    def g_Chart(self, js):
        return Chart(self.lib, self.ctx, js)

    def g_KLineChart(self, js={}):
        return KLineChart(self.lib, self.ctx, js)

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
    btUUID = os.getenv("BOTVS_TASK_UUID")
    session = None
    if btUUID == 'dummy':
        session = gg['s']
    else:
        session = DummySession()
    if session is not None:
        Backtest(__cfg__, session).Run()


