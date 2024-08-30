# -*- coding: utf-8 -*-  
if 82 - 82: Iii1i
import warnings
warnings . filterwarnings ( "ignore" , category = DeprecationWarning )
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
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
try :
 import md5
 import urllib2
except :
 import hashlib as md5
 import urllib . request as urllib2
 if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
try :
 import ssl
 ssl . _create_default_https_context = ssl . _create_unverified_context
except :
 pass
 if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
try :
 from urllib import urlencode
except :
 from urllib . parse import urlencode
 if 98 - 98: I11iiIi11i1I % oOO
i1ii1 = os . getenv ( "DATASERVER" , "http://q.fmz.com" )
if 63 - 63: iI1iI11Ii111
I11II1Ii = sys . version_info [ 0 ] >= 3
iIi = globals ( )
iIi [ 'NaN' ] = None
iIi [ 'null' ] = None
iIi [ 'true' ] = True
iIi [ 'false' ] = False
if 76 - 76: i11 / i1 . Ii . i1i1i1111I + I11iiIi11i1I
if 31 - 31: IIiIIiIi11I1 * oOO / OooOoo
oOooo0OOO = hasattr
def hasattr ( obj , method ) :
 try :
  return oOooo0OOO ( obj , method )
 except :
  return False
  if 53 - 53: Ii * Oo * ooo000 . i1iiIII111
if I11II1Ii :
 iIi [ 'xrange' ] = range
 ii1Ii = str
else :
 ii1Ii = basestring
 if 55 - 55: iI1iII1I1I1i + i1
def Iii11iiiiI ( s ) :
 if I11II1Ii :
  return json . loads ( s . decode ( 'utf-8' ) )
 return json . loads ( s )
 if 63 - 63: ooo000 / I1Ii1I1 . Iii1i - ooo000
def OO0000 ( s ) :
 if I11II1Ii :
  return s . decode ( 'utf-8' )
 return s
 if 92 - 92: I1I / I1I + iI1iI11Ii111 . oOO
def Iio0 ( s ) :
 if I11II1Ii :
  return s . encode ( 'utf-8' )
 return str ( s )
 if 11 - 11: i11 . i1i1i1111I
 if 87 - 87: Oo - iI1iI11Ii111
iiI1111IIi1 = 1 << 0
oOo00O = 1 << 1
OoO = 1 << 2
ii1IiIiiII = 1 << 3
I1I111i11I = 1 << 4
iii11i = 1 << 5
Oo0Oo00O0OO = 1 << 6
iIIiiIi1Ii1I = 1 << 7
oo0 = 1 << 8
if 20 - 20: IiIIii11Ii . oOO % Ooo0Ooo / Ii / oOo0O00
def oo0o0oO ( ) :
 oooOo = tempfile . gettempdir ( ) + '/cache'
 if not os . path . exists ( oooOo ) :
  try :
   os . mkdir ( oooOo )
  except :
   pass
 return oooOo
 if 23 - 23: Ooo0Ooo + i1 * I1Ii1I1 + Oo * Ii - IIiIIiIi11I1
def iIIiii1iI ( url ) :
 OOO = urllib2 . Request ( url )
 OOO . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
 OooOoo0OO0OO0 = urllib2 . urlopen ( OOO )
 IiIi1Ii1111 = OooOoo0OO0OO0 . read ( )
 if OooOoo0OO0OO0 . info ( ) . get ( 'Content-Encoding' ) == 'gzip' :
  IiIi1Ii1111 = zlib . decompress ( IiIi1Ii1111 , 16 + zlib . MAX_WBITS )
 return IiIi1Ii1111
 if 95 - 95: I1I * Ooo0Ooo + i1iiIII111 . i1iiIII111 % Oo * oOo0O00
class OO0O0oo :
 @ staticmethod
 def _skip ( arr , period ) :
  O0o00OO0oOOo = 0
  OOO0o0O0o = 0
  for OOO0o0O0o in xrange ( 0 , len ( arr ) ) :
   if arr [ OOO0o0O0o ] is not None :
    O0o00OO0oOOo += 1
   if O0o00OO0oOOo == period :
    break
  return OOO0o0O0o
  if 85 - 85: oOo0O00
 @ staticmethod
 def _sum ( arr , num ) :
  o0Ooo = 0.0
  for ii in xrange ( 0 , num ) :
   if arr [ ii ] is not None :
    o0Ooo += arr [ ii ]
  return o0Ooo
  if 61 - 61: iI1iII1I1I1i . iI1iI11Ii111 - ooo000 / ooo000 - i1
 @ staticmethod
 def _avg ( arr , num ) :
  if len ( arr ) == 0 :
   return 0
  o0Ooo = 0.0
  iIiI1 = 0
  for ii in xrange ( 0 , min ( len ( arr ) , num ) ) :
   if arr [ ii ] is not None :
    o0Ooo += arr [ ii ]
    iIiI1 += 1
  if iIiI1 == 0 :
   return 0
  return o0Ooo / iIiI1
  if 32 - 32: iI1iII1I1I1i
 @ staticmethod
 def _zeros ( n ) :
  return [ 0.0 ] * n
  if 18 - 18: I11iiIi11i1I * i11 % iI1iII1I1I1i + i11
 @ staticmethod
 def _set ( arr , start , end , value ) :
  for ii in xrange ( start , min ( len ( arr ) , end ) ) :
   arr [ ii ] = value
   if 93 - 93: oOO - I1Ii1I1 - IIiIIiIi11I1 * ooOOO - i1
 @ staticmethod
 def _diff ( a , b ) :
  OoOOo0OoOOO0 = [ None ] * len ( b )
  for ii in xrange ( 0 , len ( b ) ) :
   if a [ ii ] is not None and b [ ii ] is not None :
    OoOOo0OoOOO0 [ ii ] = a [ ii ] - b [ ii ]
  return OoOOo0OoOOO0
  if 11 - 11: i1 / ooo000
 @ staticmethod
 def _move_diff ( a ) :
  OoOOo0OoOOO0 = [ None ] * ( len ( a ) - 1 )
  for ii in xrange ( 1 , len ( a ) ) :
   OoOOo0OoOOO0 [ ii - 1 ] = a [ ii ] - a [ ii - 1 ]
  return OoOOo0OoOOO0
  if 89 - 89: I1I * i1i1i1111I
 @ staticmethod
 def _cmp ( arr , start , end , cmpFunc ) :
  O0OOooO = arr [ start ]
  for ii in xrange ( start , end ) :
   O0OOooO = cmpFunc ( arr [ ii ] , O0OOooO )
  return O0OOooO
  if 50 - 50: Iii1i * ooo000 % Iii1i - oOo0O00 + ooo000
 @ staticmethod
 def _filt ( records , n , attr , iv , cmpFunc ) :
  if len ( records ) < 2 :
   return None
  O0OOooO = iv
  ooOOOoOO0 = 0
  if n != 0 :
   ooOOOoOO0 = len ( records ) - min ( len ( records ) - 1 , n ) - 1
  for ii in xrange ( len ( records ) - 2 , ooOOOoOO0 - 1 , - 1 ) :
   if records [ ii ] is not None :
    if attr is not None :
     O0OOooO = cmpFunc ( O0OOooO , records [ ii ] [ attr ] )
    else :
     O0OOooO = cmpFunc ( O0OOooO , records [ ii ] )
  return O0OOooO
  if 87 - 87: I1Ii1I1 * OooOoo - oOO % Iii1i
 @ staticmethod
 def _ticks ( records ) :
  if len ( records ) == 0 :
   return [ ]
  if isinstance ( records [ 0 ] , int ) or isinstance ( records [ 0 ] , float ) :
   return records
   if 51 - 51: Iii1i % Ooo0Ooo . iI1iII1I1I1i / Ii / ooOOO
  OOOOO = [ None ] * len ( records )
  for ii in xrange ( 0 , len ( records ) ) :
   OOOOO [ ii ] = records [ ii ] [ 'Close' ]
  return OOOOO
  if 36 - 36: i1i1i1111I + Iii1i - oOO * Ii
 @ staticmethod
 def _sma ( S , period ) :
  oo0ooooo0ooo = OO0O0oo . _zeros ( len ( S ) )
  OOO0o0O0o = OO0O0oo . _skip ( S , period )
  OO0O0oo . _set ( oo0ooooo0ooo , 0 , OOO0o0O0o , None )
  if OOO0o0O0o < len ( S ) :
   o0Ooo = 0
   for ii in xrange ( OOO0o0O0o , len ( S ) ) :
    if ii == OOO0o0O0o :
     o0Ooo = OO0O0oo . _sum ( S , ii + 1 )
    else :
     o0Ooo += S [ ii ] - S [ ii - period ]
    oo0ooooo0ooo [ ii ] = o0Ooo / period
  return oo0ooooo0ooo
  if 61 - 61: iI1iI11Ii111 . iI1iII1I1I1i / ooOOO * I1Ii1I1 + i11 % Oo
 @ staticmethod
 def _smma ( S , period ) :
  oo0ooooo0ooo = OO0O0oo . _zeros ( len ( S ) )
  OOO0o0O0o = OO0O0oo . _skip ( S , period )
  OO0O0oo . _set ( oo0ooooo0ooo , 0 , OOO0o0O0o , None )
  if OOO0o0O0o < len ( S ) :
   oo0ooooo0ooo [ OOO0o0O0o ] = OO0O0oo . _avg ( S , OOO0o0O0o + 1 )
   for ii in xrange ( OOO0o0O0o + 1 , len ( S ) ) :
    oo0ooooo0ooo [ ii ] = ( oo0ooooo0ooo [ ii - 1 ] * ( period - 1 ) + S [ ii ] ) / period
  return oo0ooooo0ooo
  if 100 - 100: Oo + iI1iI11Ii111
 @ staticmethod
 def _ema ( S , period ) :
  oo0ooooo0ooo = OO0O0oo . _zeros ( len ( S ) )
  I1II1ii111i = 2.0 / ( period + 1 )
  OOO0o0O0o = OO0O0oo . _skip ( S , period )
  OO0O0oo . _set ( oo0ooooo0ooo , 0 , OOO0o0O0o , None )
  if OOO0o0O0o < len ( S ) :
   oo0ooooo0ooo [ OOO0o0O0o ] = OO0O0oo . _avg ( S , OOO0o0O0o + 1 )
   for ii in xrange ( OOO0o0O0o + 1 , len ( S ) ) :
    oo0ooooo0ooo [ ii ] = ( ( S [ ii ] - oo0ooooo0ooo [ ii - 1 ] ) * I1II1ii111i ) + oo0ooooo0ooo [ ii - 1 ]
  return oo0ooooo0ooo
  if 14 - 14: i11 + iI1iI11Ii111 . IiIIii11Ii . Ooo0Ooo % IiIIii11Ii * i1i1i1111I
class oOoOO0O0 :
 def __init__ ( self , logPtr = None ) :
  self . _logPtr = logPtr
  if 20 - 20: I11iiIi11i1I / ooOOO * oOO % IIiIIiIi11I1
 def _log ( self , name , * args ) :
  if self . _logPtr is not None :
   self . _logPtr ( name , Iio0 ( ',' . join ( map ( str , args ) ) ) )
   if 60 - 60: iI1iI11Ii111 * i1iiIII111 + i1i1i1111I / ooOOO
 @ staticmethod
 def Highest ( records , n , attr = None ) :
  return OO0O0oo . _filt ( records , n , attr , 5e-324 , max )
  if 58 - 58: iI1iI11Ii111 - i11
 @ staticmethod
 def Lowest ( records , n , attr = None ) :
  return OO0O0oo . _filt ( records , n , attr , 1.7976931348623157e+308 , min )
  if 86 - 86: Iii1i + i1iiIII111 - IIiIIiIi11I1 / I1I
 def MA ( self , records , period = 9 ) :
  self . _log ( 'MA' , period )
  if 46 - 46: ooOOO + ooOOO % oOO
  return OO0O0oo . _sma ( OO0O0oo . _ticks ( records ) , period )
  if 2 - 2: i1i1i1111I / Ooo0Ooo / oOO - IIiIIiIi11I1 / IIiIIiIi11I1
 def SMA ( self , records , period = 9 ) :
  self . _log ( 'SMA' , period )
  if 58 - 58: i1i1i1111I
  return OO0O0oo . _sma ( OO0O0oo . _ticks ( records ) , period )
  if 38 - 38: i1 - oOo0O00
 def EMA ( self , records , period = 9 ) :
  self . _log ( 'EMA' , period )
  if 85 - 85: IIiIIiIi11I1 + I11iiIi11i1I % Ooo0Ooo + oOO * i1iiIII111
  return OO0O0oo . _ema ( OO0O0oo . _ticks ( records ) , period )
  if 46 - 46: ooOOO - ooOOO + Oo / I1I * Oo + oOO
 def MACD ( self , records , fastEMA = 12 , slowEMA = 26 , signalEMA = 9 ) :
  self . _log ( 'MACD' , fastEMA , slowEMA , signalEMA )
  if 98 - 98: I1I / IIiIIiIi11I1 / iI1iI11Ii111 + i11 % Oo + I1I
  OOOOO = OO0O0oo . _ticks ( records )
  ooOo00o = OO0O0oo . _ema ( OOOOO , slowEMA )
  o0 = OO0O0oo . _ema ( OOOOO , fastEMA )
  if 38 - 38: IIiIIiIi11I1 / Iii1i . oOo0O00 % IIiIIiIi11I1 - i1iiIII111 - I1Ii1I1
  IiiIIi111 = OO0O0oo . _diff ( o0 , ooOo00o )
  if 7 - 7: iI1iI11Ii111 / oOo0O00
  i1I = OO0O0oo . _ema ( IiiIIi111 , signalEMA )
  III1II11i = OO0O0oo . _diff ( IiiIIi111 , i1I )
  return [ IiiIIi111 , i1I , III1II11i ]
  if 79 - 79: I1I . I1I * i1i1i1111I + i1 / oOO / i1i1i1111I
 def BOLL ( self , records , period = 20 , multiplier = 2 ) :
  self . _log ( 'BOLL' , period , multiplier )
  if 21 - 21: Ooo0Ooo
  OooO0O = OO0O0oo . _ticks ( records )
  OOO0o0O0o = period - 1
  while OOO0o0O0o < len ( OooO0O ) and ( OooO0O [ OOO0o0O0o ] is None ) :
   OOO0o0O0o += 1
  ooO000oOo0o0 = OO0O0oo . _zeros ( len ( OooO0O ) )
  Iiii = OO0O0oo . _zeros ( len ( OooO0O ) )
  OoO0O0OO0 = OO0O0oo . _zeros ( len ( OooO0O ) )
  OO0O0oo . _set ( ooO000oOo0o0 , 0 , OOO0o0O0o , None )
  OO0O0oo . _set ( Iiii , 0 , OOO0o0O0o , None )
  OO0O0oo . _set ( OoO0O0OO0 , 0 , OOO0o0O0o , None )
  iIiI1 = 0.0
  for ii in xrange ( OOO0o0O0o , len ( OooO0O ) ) :
   if ii == OOO0o0O0o :
    for O0o00OO0oOOo in xrange ( 0 , period ) :
     iIiI1 += OooO0O [ O0o00OO0oOOo ]
   else :
    iIiI1 = iIiI1 + OooO0O [ ii ] - OooO0O [ ii - period ]
   O0o = iIiI1 / period
   OoOOo0OoOOO0 = 0
   for O0o00OO0oOOo in xrange ( ii + 1 - period , ii + 1 ) :
    OoOOo0OoOOO0 += ( OooO0O [ O0o00OO0oOOo ] - O0o ) * ( OooO0O [ O0o00OO0oOOo ] - O0o )
   OOooo000o0O = math . sqrt ( OoOOo0OoOOO0 / period )
   i11IIi1I1 = O0o + ( multiplier * OOooo000o0O )
   oOOOO0ooO = O0o - ( multiplier * OOooo000o0O )
   ooO000oOo0o0 [ ii ] = i11IIi1I1
   Iiii [ ii ] = O0o
   OoO0O0OO0 [ ii ] = oOOOO0ooO
  return [ ooO000oOo0o0 , Iiii , OoO0O0OO0 ]
  if 53 - 53: oOo0O00 - ooo000 * Ii % i1i1i1111I - ooOOO + i1iiIII111
 def KDJ ( self , records , n = 9 , k = 3 , d = 3 ) :
  self . _log ( 'KDJ' , n , k , d )
  if 15 - 15: Iii1i % oOO * Ooo0Ooo - Ii
  II1IiiI1iII = OO0O0oo . _zeros ( len ( records ) )
  OO0O0oo . _set ( II1IiiI1iII , 0 , n - 1 , None )
  o0i1i1Ii = OO0O0oo . _zeros ( len ( records ) )
  ii1iI1I11 = OO0O0oo . _zeros ( len ( records ) )
  OOoO0oOo0 = OO0O0oo . _zeros ( len ( records ) )
  if 66 - 66: i1i1i1111I / Ooo0Ooo + I11iiIi11i1I + Iii1i + oOo0O00 + iI1iI11Ii111
  o0OOO00OO = OO0O0oo . _zeros ( len ( records ) )
  oo0OoOoO0O0OO = OO0O0oo . _zeros ( len ( records ) )
  for ii in xrange ( 0 , len ( records ) ) :
   o0OOO00OO [ ii ] = records [ ii ] [ 'High' ]
   oo0OoOoO0O0OO [ ii ] = records [ ii ] [ 'Low' ]
   if 85 - 85: IIiIIiIi11I1 / OooOoo . iI1iI11Ii111 % Oo + Oo - I11iiIi11i1I
  for ii in xrange ( 0 , len ( records ) ) :
   if ii >= ( n - 1 ) :
    ooO0ooOOO00O0 = records [ ii ] [ 'Close' ]
    I1II11I1i1ii = OO0O0oo . _cmp ( o0OOO00OO , ii - ( n - 1 ) , ii + 1 , max )
    ooOo00oOo0Ooo = OO0O0oo . _cmp ( oo0OoOoO0O0OO , ii - ( n - 1 ) , ii + 1 , min )
    II1IiiI1iII [ ii ] = ( 100 * ( ( ooO0ooOOO00O0 - ooOo00oOo0Ooo ) / ( I1II11I1i1ii - ooOo00oOo0Ooo ) ) ) if I1II11I1i1ii != ooOo00oOo0Ooo else 100
    o0i1i1Ii [ ii ] = float ( 1 * II1IiiI1iII [ ii ] + ( k - 1 ) * o0i1i1Ii [ ii - 1 ] ) / k
    ii1iI1I11 [ ii ] = float ( 1 * o0i1i1Ii [ ii ] + ( d - 1 ) * ii1iI1I11 [ ii - 1 ] ) / d
   else :
    o0i1i1Ii [ ii ] = ii1iI1I11 [ ii ] = 50.0
    II1IiiI1iII [ ii ] = 0.0
   OOoO0oOo0 [ ii ] = 3 * o0i1i1Ii [ ii ] - 2 * ii1iI1I11 [ ii ]
   if 42 - 42: oOo0O00
  for ii in xrange ( 0 , n - 1 ) :
   o0i1i1Ii [ ii ] = ii1iI1I11 [ ii ] = OOoO0oOo0 [ ii ] = None
  return [ o0i1i1Ii , ii1iI1I11 , OOoO0oOo0 ]
  if 46 - 46: OooOoo - I11iiIi11i1I / Ooo0Ooo
 def RSI ( self , records , period = 14 ) :
  self . _log ( 'RSI' , period )
  if 73 - 73: I1Ii1I1 / i1i1i1111I / ooo000 % i1 % iI1iI11Ii111 - OooOoo
  iIiI1 = period
  IIII1iII11ii = OO0O0oo . _zeros ( len ( records ) )
  OO0O0oo . _set ( IIII1iII11ii , 0 , len ( IIII1iII11ii ) , None )
  if len ( records ) < iIiI1 :
   return IIII1iII11ii
   if 57 - 57: oOo0O00 % Ooo0Ooo * ooOOO
  OOOOO = OO0O0oo . _ticks ( records )
  OOOoo = OO0O0oo . _move_diff ( OOOOO )
  OO0Oo0OOo00 = OOOoo [ : iIiI1 ]
  i11IIi1I1 = 0.0
  Ii1Ii1 = 0.0
  for ii in xrange ( 0 , len ( OO0Oo0OOo00 ) ) :
   if OO0Oo0OOo00 [ ii ] >= 0 :
    i11IIi1I1 += OO0Oo0OOo00 [ ii ]
   else :
    Ii1Ii1 += OO0Oo0OOo00 [ ii ]
  i11IIi1I1 /= iIiI1
  Ii1Ii1 /= iIiI1
  Ii1Ii1 = - Ii1Ii1
  if Ii1Ii1 != 0 :
   I111i1i11iII = i11IIi1I1 / Ii1Ii1
  else :
   I111i1i11iII = 0
  IIII1iII11ii [ iIiI1 ] = 100 - 100 / ( 1 + I111i1i11iII )
  IiiII1Iiii1I1 = 0.0
  oOO0Oo = 0.0
  oo00 = 0.0
  for ii in xrange ( iIiI1 + 1 , len ( OOOOO ) ) :
   IiiII1Iiii1I1 = OOOoo [ ii - 1 ]
   if IiiII1Iiii1I1 > 0 :
    oOO0Oo = IiiII1Iiii1I1
    oo00 = 0.0
   else :
    oOO0Oo = 0.0
    oo00 = - IiiII1Iiii1I1
   i11IIi1I1 = ( i11IIi1I1 * ( iIiI1 - 1 ) + oOO0Oo ) / iIiI1
   Ii1Ii1 = ( Ii1Ii1 * ( iIiI1 - 1 ) + oo00 ) / iIiI1
   I111i1i11iII = 0 if Ii1Ii1 == 0 else ( i11IIi1I1 / Ii1Ii1 )
   IIII1iII11ii [ ii ] = 100 - 100 / ( 1 + I111i1i11iII )
  return IIII1iII11ii
  if 87 - 87: IiIIii11Ii % ooo000 . ooOOO . oOO
 def OBV ( self , records ) :
  self . _log ( 'OBV' )
  if 16 - 16: ooOOO + ooo000 % IiIIii11Ii * Oo
  if len ( records ) == 0 :
   return [ ]
   if 87 - 87: Iii1i - i11
  if 'Close' not in records [ 0 ] :
   raise "self.OBV argument must KLine"
   if 72 - 72: i1 % i1i1i1111I * iI1iII1I1I1i
  oo0ooooo0ooo = OO0O0oo . _zeros ( len ( records ) )
  for ii in xrange ( 0 , len ( records ) ) :
   if ii == 0 :
    oo0ooooo0ooo [ ii ] = records [ ii ] [ 'Volume' ]
   elif records [ ii ] [ 'Close' ] >= records [ ii - 1 ] [ 'Close' ] :
    oo0ooooo0ooo [ ii ] = oo0ooooo0ooo [ ii - 1 ] + records [ ii ] [ 'Volume' ]
   else :
    oo0ooooo0ooo [ ii ] = oo0ooooo0ooo [ ii - 1 ] - records [ ii ] [ 'Volume' ]
  return oo0ooooo0ooo
  if 90 - 90: Ooo0Ooo * OooOoo . Ii
 def ATR ( self , records , period = 14 ) :
  self . _log ( 'ATR' , period )
  if 5 - 5: Oo - i1 . oOO
  if len ( records ) == 0 :
   return [ ]
  if 'Close' not in records [ 0 ] :
   raise "self.ATR argument must KLine"
   if 18 - 18: IiIIii11Ii - oOO * iI1iI11Ii111 - OooOoo
  oo0ooooo0ooo = OO0O0oo . _zeros ( len ( records ) )
  o0OOo0OoO = 0.0
  iIiI1 = 0.0
  for ii in xrange ( 0 , len ( records ) ) :
   oo0O00O = 0
   if ii == 0 :
    oo0O00O = records [ ii ] [ 'High' ] - records [ ii ] [ 'Low' ]
   else :
    oo0O00O = max ( records [ ii ] [ 'High' ] - records [ ii ] [ 'Low' ] , abs ( records [ ii ] [ 'High' ] - records [ ii - 1 ] [ 'Close' ] ) , abs ( records [ ii - 1 ] [ 'Close' ] - records [ ii ] [ 'Low' ] ) )
   o0OOo0OoO += oo0O00O
   if ii < period :
    iIiI1 = o0OOo0OoO / ( ii + 1 )
   else :
    iIiI1 = ( ( ( period - 1 ) * iIiI1 ) + oo0O00O ) / period
   oo0ooooo0ooo [ ii ] = iIiI1
  return oo0ooooo0ooo
  if 8 - 8: I1I + iI1iII1I1I1i . I1I . i11
 def Alligator ( self , records , jawLength = 13 , teethLength = 8 , lipsLength = 5 ) :
  self . _log ( 'Alligator' , jawLength , teethLength , lipsLength )
  if 3 - 3: i1iiIII111
  OOOOO = [ ]
  for ii in xrange ( 0 , len ( records ) ) :
   OOOOO . append ( ( records [ ii ] [ 'High' ] + records [ ii ] [ 'Low' ] ) / 2 )
  return [
 [ None ] * 8 + OO0O0oo . _smma ( OOOOO , jawLength ) ,
  [ None ] * 5 + OO0O0oo . _smma ( OOOOO , teethLength ) ,
  [ None ] * 3 + OO0O0oo . _smma ( OOOOO , lipsLength )
  ]
  if 32 - 32: I1I % i1i1i1111I
 def CMF ( self , records , period = 20 ) :
  self . _log ( 'CMF' , period )
  if 98 - 98: iI1iI11Ii111 / i1 / OooOoo + Iii1i % ooOOO
  iIii1iiiIi = [ ]
  oOoo = 0.0
  ooOOO00oO0o0o = 0.0
  OooOOO0oO0Oo = [ ]
  IiiiI11111I = [ ]
  for ii in xrange ( 0 , len ( records ) ) :
   OoOOo0OoOOO0 = 0.0
   if records [ ii ] [ 'High' ] != records [ ii ] [ 'Low' ] :
    OoOOo0OoOOO0 = ( 2 * records [ ii ] [ 'Close' ] - records [ ii ] [ 'Low' ] - records [ ii ] [ 'High' ] ) / ( records [ ii ] [ 'High' ] - records [ ii ] [ 'Low' ] ) * records [ ii ] [ 'Volume' ]
   OooOOO0oO0Oo . append ( OoOOo0OoOOO0 )
   IiiiI11111I . append ( records [ ii ] [ 'Volume' ] )
   oOoo += OoOOo0OoOOO0
   ooOOO00oO0o0o += records [ ii ] [ 'Volume' ]
   if ii >= period :
    oOoo -= OooOOO0oO0Oo . pop ( 0 )
    ooOOO00oO0o0o -= IiiiI11111I . pop ( 0 )
   iIii1iiiIi . append ( oOoo / ooOOO00oO0o0o )
  return iIii1iiiIi
  if 49 - 49: oOo0O00 % I11iiIi11i1I - Ooo0Ooo % Oo . oOO
  if 93 - 93: iI1iII1I1I1i - i1
class OOO0oOOO0 :
 def __init__ ( self , name ) :
  self . __name = name
  sys . modules [ 'talib' ] = self
 def __getattr__ ( self , attr ) :
  raise Exception ( 'Please install %s module for python' % self . __name )
  if 33 - 33: IIiIIiIi11I1 / i1i1i1111I . i1i1i1111I
class I11 ( list ) :
 def __init__ ( self , data ) :
  super ( I11 , self ) . __init__ ( data )
  self . __data = data
 def __getattr__ ( self , attr ) :
  if attr . startswith ( '_' ) :
   raise AttributeError
  iIii1iiiIi = [ ]
  for oo000O0oOO in self . __data :
   iIii1iiiIi . append ( oo000O0oOO [ attr ] )
  if o0OOo0 :
   iIii1iiiIi = numpy . array ( iIii1iiiIi )
  setattr ( self , attr , iIii1iiiIi )
  return iIii1iiiIi
  if 65 - 65: IIiIIiIi11I1 / i1
o0OOo0 = False
try :
 import talib
 import numpy
 o0OOo0 = True
except ImportError :
 talib = OOO0oOOO0 ( 'talib' )
 if 14 - 14: IiIIii11Ii % ooOOO . iI1iI11Ii111
I11111i111 = 0
oO0O = - 1
OoIi1 = - 2
if 82 - 82: i1i1i1111I
class IIIiII1I ( dict ) :
 def __getattr__ ( self , name ) :
  if name in self :
   return self [ name ]
  else :
   raise AttributeError ( "no attribute '%s'" % name )
   if 100 - 100: i1i1i1111I % OooOoo . i11 / i1i1i1111I . ooOOO
 def __setattr__ ( self , name , value ) :
  self [ name ] = value
  if 57 - 57: IIiIIiIi11I1 - iI1iII1I1I1i % ooOOO - I11iiIi11i1I / IiIIii11Ii . Ooo0Ooo
 def __delattr__ ( self , name ) :
  if name in self :
   del self [ name ]
  else :
   raise AttributeError ( "no attribute '%s'" % name )
   if 15 - 15: iI1iI11Ii111 * I11iiIi11i1I - oOo0O00
def i1iiiIii ( args ) :
 OooO0Oo = [ ]
 for oo000O0oOO in args :
  if hasattr ( oo000O0oOO , 'savefig' ) and callable ( oo000O0oOO . savefig ) :
   OoOOo0OoOOO0 = io . BytesIO ( )
   oo000O0oOO . savefig ( OoOOo0OoOOO0 , format = "png" )
   OooO0Oo . append ( '`data:image/png;base64,%s`' % ( base64 . b64encode ( OoOOo0OoOOO0 . getvalue ( ) ) . decode ( 'utf-8' ) ) )
  elif isinstance ( oo000O0oOO , dict ) and oo000O0oOO . get ( 'type' ) == 'table' and oo000O0oOO . get ( 'cols' ) :
   OooO0Oo . append ( '`%s`' % json . dumps ( oo000O0oOO ) )
  else :
   OooO0Oo . append ( str ( oo000O0oOO ) )
 return Iio0 ( ' ' . join ( OooO0Oo ) )
 if 17 - 17: i1 % oOO % IiIIii11Ii * i1i1i1111I
class ooOoO0O0 ( ctypes . Structure ) :
 def toObj ( self ) :
  OoOoOo = { }
  for O0o00OO0oOOo , OOo in self . _fields_ :
   if O0o00OO0oOOo [ 0 ] . isupper ( ) :
    O0OOooO = getattr ( self , O0o00OO0oOOo )
    if isinstance ( O0OOooO , bytes ) :
     O0OOooO = O0OOooO . decode ( )
    OoOoOo [ O0o00OO0oOOo ] = O0OOooO
  return IIIiII1I ( OoOoOo )
  if 32 - 32: ooo000 % i1i1i1111I % oOo0O00 - i1iiIII111
class Ii11 ( ooOoO0O0 ) :
 _fields_ = [ ( "Time" , ctypes . c_ulonglong ) ,
 ( "Open" , ctypes . c_double ) ,
 ( "High" , ctypes . c_double ) ,
 ( "Low" , ctypes . c_double ) ,
 ( "Sell" , ctypes . c_double ) ,
 ( "Buy" , ctypes . c_double ) ,
 ( "Last" , ctypes . c_double ) ,
 ( "Volume" , ctypes . c_double ) ,
 ( "OpenInterest" , ctypes . c_double ) ,
 ( "data" , ctypes . c_char_p ) ,
 ( "data_size" , ctypes . c_uint ) ,
 ]
 if 15 - 15: I1I % IiIIii11Ii + OooOoo * Oo / OooOoo
class o0o0 ( ooOoO0O0 ) :
 _fields_ = [ ( "Time" , ctypes . c_ulonglong ) ,
 ( "Open" , ctypes . c_double ) ,
 ( "High" , ctypes . c_double ) ,
 ( "Low" , ctypes . c_double ) ,
 ( "Close" , ctypes . c_double ) ,
 ( "Volume" , ctypes . c_double ) ,
 ( "OpenInterest" , ctypes . c_double ) ]
 if 10 - 10: IIiIIiIi11I1 * iI1iII1I1I1i
class OOoOoOO0OO0o ( ooOoO0O0 ) :
 _fields_ = [ ( "Price" , ctypes . c_double ) , ( "Amount" , ctypes . c_double ) ]
 if 46 - 46: oOo0O00 . iI1iII1I1I1i - Ii . oOo0O00 + i1i1i1111I
class I111iI11i ( ooOoO0O0 ) :
 _fields_ = [ ( "Balance" , ctypes . c_double ) ,
 ( "FrozenBalance" , ctypes . c_double ) ,
 ( "Stocks" , ctypes . c_double ) ,
 ( "FrozenStocks" , ctypes . c_double ) ]
 if 42 - 42: I11iiIi11i1I - Ii / Oo - i1i1i1111I + I11iiIi11i1I
class i1II1 ( ooOoO0O0 ) :
 _fields_ = [ ( "Currency" , ctypes . c_char * 31 ) ,
 ( "Amount" , ctypes . c_double ) ,
 ( "FrozenAmount" , ctypes . c_double ) ]
 if 67 - 67: IiIIii11Ii / oOo0O00 + Ooo0Ooo - i11 + Ii
class oo00OOO ( ooOoO0O0 ) :
 _fields_ = [ ( "Id" , ctypes . c_ulonglong ) ,
 ( "Price" , ctypes . c_double ) ,
 ( "Amount" , ctypes . c_double ) ,
 ( "DealAmount" , ctypes . c_double ) ,
 ( "AvgPrice" , ctypes . c_double ) ,
 ( "Type" , ctypes . c_uint ) ,
 ( "Offset" , ctypes . c_uint ) ,
 ( "Status" , ctypes . c_uint ) ,
 ( "Symbol" , ctypes . c_char * 31 ) ,
 ( "ContractType" , ctypes . c_char * 31 ) ]
 if 93 - 93: OooOoo % i1i1i1111I + OooOoo % oOo0O00 + ooo000 * OooOoo
class II1Ii11111 ( ooOoO0O0 ) :
 _fields_ = [ ( "Id" , ctypes . c_ulonglong ) ,
 ( "Time" , ctypes . c_ulonglong ) ,
 ( "Price" , ctypes . c_double ) ,
 ( "Amount" , ctypes . c_double ) ,
 ( "Type" , ctypes . c_uint ) ]
 if 12 - 12: Ooo0Ooo * IiIIii11Ii % IiIIii11Ii . I1Ii1I1 + i1iiIII111 / IIiIIiIi11I1
class iiiI ( ooOoO0O0 ) :
 _fields_ = [ ( "MarginLevel" , ctypes . c_double ) ,
 ( "Amount" , ctypes . c_double ) ,
 ( "FrozenAmount" , ctypes . c_double ) ,
 ( "Price" , ctypes . c_double ) ,
 ( "Profit" , ctypes . c_double ) ,
 ( "Margin" , ctypes . c_double ) ,
 ( "Type" , ctypes . c_uint ) ,
 ( "Symbol" , ctypes . c_char * 31 ) ,
 ( "ContractType" , ctypes . c_char * 31 ) ]
def iI1i1Iiii11i ( ) :
 raise EOFError ( )
 if 93 - 93: Ooo0Ooo . i1 + i11 - oOo0O00
class ooOOoO00OO :
 routineId = 0
 def __init__ ( self , v ) :
  self . isWait = False
  self . v = v
  ooOOoO00OO . routineId += 1
  if 99 - 99: I11iiIi11i1I - Ooo0Ooo % I1Ii1I1
 def wait ( self , timeout = 0 ) :
  if self . isWait :
   return ( None , False )
  self . isWait = True
  return ( self . v , True )
  if 26 - 26: ooOOO / IIiIIiIi11I1 . oOO + I11iiIi11i1I . Oo
 def __repr__ ( self ) :
  return '<Go %d>' % ooOOoO00OO . routineId
  if 37 - 37: I1Ii1I1
class OoOooOOoOo :
 def __init__ ( self , lib , ctx , idx , opt , cfg ) :
  self . lib = lib
  self . ctx = ctx
  self . idx = ctypes . c_int ( idx )
  self . opt = opt
  self . cfg = cfg
  self . name = cfg [ "Id" ]
  self . label = cfg [ "Label" ]
  self . currency = '%s_%s' % ( cfg [ "BaseCurrency" ] , cfg [ "QuoteCurrency" ] )
  self . quoteCurrency = cfg [ "QuoteCurrency" ]
  self . maxBarLen = cfg . get ( 'MaxBarLen' , 1000 )
  self . period = opt [ 'Period' ]
  self . ct = ''
  self . records_cache = { }
  if 51 - 51: i1 + i1i1i1111I - i1 + i1iiIII111 . Oo
 def Go ( self , method , * args ) :
  return ooOOoO00OO ( getattr ( self , method ) ( * args ) )
  if 92 - 92: OooOoo + Ii / IIiIIiIi11I1 + OooOoo * IIiIIiIi11I1 * iI1iII1I1I1i
 def GetName ( self ) :
  return self . name
  if 79 - 79: i1i1i1111I
 def GetLabel ( self ) :
  return self . label
  if 3 - 3: OooOoo / i11 % I11iiIi11i1I
 def GetCurrency ( self ) :
  return self . currency
  if 55 - 55: oOo0O00
 def GetQuoteCurrency ( self ) :
  return self . quoteCurrency
  if 31 - 31: Ii . Ooo0Ooo / i11
 def GetUSDCNY ( self ) :
  self . lib . api_Exchange_GetUSDCNY . restype = ctypes . c_double
  return self . lib . api_Exchange_GetUSDCNY ( self . ctx , self . idx )
  if 59 - 59: Oo
 def SetMaxBarLen ( self , n ) :
  self . maxBarLen = n
  if 64 - 64: Iii1i % I11iiIi11i1I * i1 % OooOoo * oOo0O00
 def SetPrecision ( self , a , b ) :
  self . lib . api_Exchange_SetPrecision ( self . ctx , self . idx , ctypes . c_double ( a ) , ctypes . c_double ( b ) )
  if 55 - 55: i11
 def GetRate ( self ) :
  self . lib . api_Exchange_GetRate . restype = ctypes . c_double
  return self . lib . api_Exchange_GetRate ( self . ctx , self . idx )
  if 46 - 46: Ooo0Ooo % I1Ii1I1
 def SetProxy ( self , s ) :
  pass
  if 86 - 86: I11iiIi11i1I . i1i1i1111I + oOO % I11iiIi11i1I % Iii1i % ooo000
 def SetTimeout ( self , ms ) :
  pass
  if 61 - 61: ooo000
 def SetBase ( self , s ) :
  OoOoOo000o00O = ctypes . c_char_p ( )
  self . lib . api_Exchange_SetBase ( self . ctx , self . idx , Iio0 ( s ) , ctypes . byref ( OoOoOo000o00O ) )
  i1I1i1I = OO0000 ( OoOoOo000o00O . value )
  self . lib . api_free ( OoOoOo000o00O )
  return i1I1i1I
  if 90 - 90: I1Ii1I1 * i1i1i1111I / iI1iII1I1I1i * Ii
 def GetBase ( self ) :
  OoOoOo000o00O = ctypes . c_char_p ( )
  self . lib . api_Exchange_GetBase ( self . ctx , self . idx , ctypes . byref ( OoOoOo000o00O ) )
  i1I1i1I = OO0000 ( OoOoOo000o00O . value )
  self . lib . api_free ( OoOoOo000o00O )
  return i1I1i1I
  if 38 - 38: I1I . Ii
 def SetCurrency ( self , s ) :
  OooO0Oo = s . split ( '_' )
  if len ( OooO0Oo ) == 2 :
   self . currency = s
   self . quoteCurrency = OooO0Oo [ 1 ]
   return self . lib . api_Exchange_SetCurrency ( self . ctx , self . idx , Iio0 ( s ) )
   if 41 - 41: ooo000 % IIiIIiIi11I1 % ooOOO
 def SetRate ( self , rate = 1.0 ) :
  self . lib . api_Exchange_SetRate . restype = ctypes . c_double
  return self . lib . api_Exchange_SetRate ( self . ctx , self . idx , ctypes . c_double ( rate ) )
  if 5 - 5: oOo0O00 / Ii + i1iiIII111 * Oo + Ooo0Ooo + ooo000
 def GetTrades ( self , symbol = '' ) :
  OoO0OO0 = ctypes . c_uint ( 0 )
  oOoO0o0OOooO0 = ctypes . c_void_p ( )
  iIii1iiiIi = self . lib . api_Exchange_GetTrades ( self . ctx , self . idx , Iio0 ( symbol ) , ctypes . byref ( OoO0OO0 ) , ctypes . byref ( oOoO0o0OOooO0 ) )
  if 38 - 38: i11 - Ooo0Ooo * I1Ii1I1
  if iIii1iiiIi == I11111i111 :
   iIiI1 = OoO0OO0 . value
   Oo0O0OO0o = [ ]
   if iIiI1 > 0 :
    I111iii = ( II1Ii11111 * iIiI1 ) . from_address ( oOoO0o0OOooO0 . value )
    for ii in range ( 0 , iIiI1 ) :
     Oo0O0OO0o . append ( I111iii [ ii ] . toObj ( ) )
    self . lib . api_free ( oOoO0o0OOooO0 )
   return Oo0O0OO0o
  elif iIii1iiiIi == oO0O :
   return None
  iI1i1Iiii11i ( )
  if 78 - 78: Ii - i1i1i1111I / IiIIii11Ii / ooo000 + Ii % i11
 def SetData ( self , name , data ) :
  if not isinstance ( data , ii1Ii ) :
   data = json . dumps ( data )
  return self . lib . api_Exchange_SetData ( self . ctx , self . idx , Iio0 ( name ) , Iio0 ( data ) )
  if 20 - 20: IiIIii11Ii - iI1iII1I1I1i + iI1iI11Ii111 . I11iiIi11i1I / ooo000 + i1iiIII111
 def GetData ( self , name , timeout = 60000 , offset = 0 ) :
  OoOoOo000o00O = Ii11 ( )
  iIii1iiiIi = self . lib . api_Exchange_GetData ( self . ctx , self . idx , ctypes . byref ( OoOoOo000o00O ) , Iio0 ( name ) , int ( timeout ) , int ( offset ) )
  if iIii1iiiIi == I11111i111 :
   return IIIiII1I ( { 'Time' : OoOoOo000o00O . Time , 'Data' : json . loads ( OoOoOo000o00O . data [ : OoOoOo000o00O . data_size ] ) if OoOoOo000o00O . data_size > 0 else None } )
  elif iIii1iiiIi == oO0O :
   return None
  iI1i1Iiii11i ( )
  if 84 - 84: Oo / I1Ii1I1 . IIiIIiIi11I1
 def GetTickers ( self ) :
  return [ ]
  if 67 - 67: Oo % ooOOO + iI1iII1I1I1i * I1I
 def GetMarkets ( self ) :
  return { }
  if 79 - 79: IIiIIiIi11I1 * Oo / OooOoo
 def GetTicker ( self , symbol = '' ) :
  OoOoOo000o00O = Ii11 ( )
  iIii1iiiIi = self . lib . api_Exchange_GetTicker ( self . ctx , self . idx , Iio0 ( symbol ) , ctypes . byref ( OoOoOo000o00O ) )
  if iIii1iiiIi == I11111i111 :
   return OoOoOo000o00O . toObj ( )
  elif iIii1iiiIi == oO0O :
   return None
  iI1i1Iiii11i ( )
  if 10 - 10: iI1iII1I1I1i / i1iiIII111 . IiIIii11Ii * i1i1i1111I
 def IO ( self , k , v = 0 ) :
  if k == 'currency' :
   return self . SetCurrency ( v )
  return self . lib . api_Exchange_IO ( self . ctx , self . idx , Iio0 ( k ) , int ( v ) )
  if 71 - 71: oOo0O00 + I1Ii1I1 / I11iiIi11i1I + Oo / I1I
 def GetDepth ( self , symbol = '' ) :
  iiI11II1i = ctypes . c_uint ( 0 )
  iI11I1 = ctypes . c_uint ( 0 )
  oOoO0o0OOooO0 = ctypes . c_void_p ( )
  iIii1iiiIi = self . lib . api_Exchange_GetDepth ( self . ctx , self . idx , Iio0 ( symbol ) , ctypes . byref ( iiI11II1i ) , ctypes . byref ( iI11I1 ) , ctypes . byref ( oOoO0o0OOooO0 ) )
  if 53 - 53: i1i1i1111I % i1iiIII111 / i1i1i1111I * iI1iII1I1I1i
  if iIii1iiiIi == I11111i111 :
   iIiI1 = iiI11II1i . value + iI11I1 . value
   O000 = [ ]
   i1ii1iIi = [ ]
   if iIiI1 > 0 :
    I111iii = ( OOoOoOO0OO0o * iIiI1 ) . from_address ( oOoO0o0OOooO0 . value )
    for ii in range ( 0 , iIiI1 ) :
     if ii < iiI11II1i . value :
      O000 . append ( I111iii [ ii ] . toObj ( ) )
     else :
      i1ii1iIi . append ( I111iii [ ii ] . toObj ( ) )
    self . lib . api_free ( oOoO0o0OOooO0 )
   return IIIiII1I ( { 'Asks' : O000 , 'Bids' : i1ii1iIi } )
  elif iIii1iiiIi == oO0O :
   return None
  iI1i1Iiii11i ( )
  if 21 - 21: i1 * I11iiIi11i1I + oOo0O00
 def GetRecords ( self , symbol = '' , period = - 1 , limit = 0 ) :
  if isinstance ( symbol , int ) :
   limit = period
   period = symbol
   symbol = ''
  if period == - 1 :
   period = int ( self . period / 1000 )
  OoO0OO0 = ctypes . c_uint ( 0 )
  oOoO0o0OOooO0 = ctypes . c_void_p ( )
  iIii1iiiIi = self . lib . api_Exchange_GetRecords ( self . ctx , self . idx , Iio0 ( symbol ) , ctypes . c_long ( int ( period ) ) , ctypes . c_long ( int ( limit ) ) , ctypes . byref ( OoO0OO0 ) , ctypes . byref ( oOoO0o0OOooO0 ) )
  if 11 - 11: oOO / OooOoo + oOo0O00
  if iIii1iiiIi == I11111i111 :
   iIiI1 = OoO0OO0 . value
   Oo0O0OO0o = [ ]
   if iIiI1 > 0 :
    I111iii = ( o0o0 * iIiI1 ) . from_address ( oOoO0o0OOooO0 . value )
    for ii in range ( 0 , iIiI1 ) :
     Oo0O0OO0o . append ( I111iii [ ii ] . toObj ( ) )
    self . lib . api_free ( oOoO0o0OOooO0 )
   O0o00OO0oOOo = '%s/%s/%d' % ( self . currency , self . ct , period )
   ooO0ooOOO00O0 = self . records_cache . get ( O0o00OO0oOOo , None )
   if ooO0ooOOO00O0 is None or len ( ooO0ooOOO00O0 ) == 0 :
    if len ( Oo0O0OO0o ) > self . maxBarLen :
     Oo0O0OO0o = Oo0O0OO0o [ len ( Oo0O0OO0o ) - self . maxBarLen : ]
    self . records_cache [ O0o00OO0oOOo ] = Oo0O0OO0o
   else :
    i1ii1111I1i = 0 if len ( ooO0ooOOO00O0 ) == 0 else ooO0ooOOO00O0 [ - 1 ] [ 'Time' ]
    for i1oO00oO00O0O in Oo0O0OO0o :
     OOo = i1oO00oO00O0O [ 'Time' ]
     if OOo == i1ii1111I1i :
      ooO0ooOOO00O0 [ - 1 ] = i1oO00oO00O0O
     elif OOo > i1ii1111I1i :
      ooO0ooOOO00O0 . append ( i1oO00oO00O0O )
      if len ( ooO0ooOOO00O0 ) > self . maxBarLen :
       ooO0ooOOO00O0 . pop ( 0 )
      i1ii1111I1i = OOo
   return I11 ( self . records_cache [ O0o00OO0oOOo ] )
  elif iIii1iiiIi == oO0O :
   return None
  iI1i1Iiii11i ( )
  if 62 - 62: ooo000 * oOo0O00
 def GetAssets ( self ) :
  OoO0OO0 = ctypes . c_uint ( 0 )
  oOoO0o0OOooO0 = ctypes . c_void_p ( )
  iIii1iiiIi = self . lib . api_Exchange_GetAssets ( self . ctx , self . idx , ctypes . byref ( OoO0OO0 ) , ctypes . byref ( oOoO0o0OOooO0 ) )
  if 59 - 59: Ii
  if iIii1iiiIi == I11111i111 :
   iIiI1 = OoO0OO0 . value
   Oo0O0OO0o = [ ]
   if iIiI1 > 0 :
    I111iii = ( i1II1 * iIiI1 ) . from_address ( oOoO0o0OOooO0 . value )
    for ii in range ( 0 , iIiI1 ) :
     Oo0O0OO0o . append ( I111iii [ ii ] . toObj ( ) )
    self . lib . api_free ( oOoO0o0OOooO0 )
   return Oo0O0OO0o
  elif iIii1iiiIi == oO0O :
   return None
  iI1i1Iiii11i ( )
  if 21 - 21: IIiIIiIi11I1 - I1I - i11 + OooOoo
 def GetAccount ( self ) :
  OoOoOo000o00O = I111iI11i ( )
  iIii1iiiIi = self . lib . api_Exchange_GetAccount ( self . ctx , self . idx , ctypes . byref ( OoOoOo000o00O ) )
  if iIii1iiiIi == I11111i111 :
   return OoOoOo000o00O . toObj ( )
  elif iIii1iiiIi == oO0O :
   return None
  iI1i1Iiii11i ( )
  if 41 - 41: IiIIii11Ii + OooOoo - I11iiIi11i1I + Oo % i1 + iI1iII1I1I1i
 def Buy ( self , price , amount = None , * extra ) :
  iIii1iiiIi = self . lib . api_Exchange_Trade ( self . ctx , self . idx , 0 , ctypes . c_double ( price ) , ctypes . c_double ( amount ) , i1iiiIii ( extra ) )
  if iIii1iiiIi > 0 :
   return int ( iIii1iiiIi )
  elif iIii1iiiIi == oO0O :
   return None
  iI1i1Iiii11i ( )
  if 16 - 16: i1 - Oo / Ii
 def Sell ( self , price , amount = None , * extra ) :
  iIii1iiiIi = self . lib . api_Exchange_Trade ( self . ctx , self . idx , 1 , ctypes . c_double ( price ) , ctypes . c_double ( amount ) , i1iiiIii ( extra ) )
  if iIii1iiiIi > 0 :
   return int ( iIii1iiiIi )
  elif iIii1iiiIi == oO0O :
   return None
  iI1i1Iiii11i ( )
  if 38 - 38: Ooo0Ooo % I1Ii1I1 / iI1iI11Ii111 + i1iiIII111
 def CreateOrder ( self , symbol , side , price , amount = None , * extra ) :
  iIii1iiiIi = self . lib . api_Exchange_CreateOrder ( self . ctx , self . idx , Iio0 ( symbol ) , Iio0 ( side ) , ctypes . c_double ( price ) , ctypes . c_double ( amount ) , i1iiiIii ( extra ) )
  if iIii1iiiIi > 0 :
   return int ( iIii1iiiIi )
  elif iIii1iiiIi == oO0O :
   return None
  iI1i1Iiii11i ( )
  if 25 - 25: I11iiIi11i1I - iI1iII1I1I1i
 def GetOrders ( self , symbol = '' ) :
  OoO0OO0 = ctypes . c_uint ( 0 )
  oOoO0o0OOooO0 = ctypes . c_void_p ( )
  iIii1iiiIi = self . lib . api_Exchange_GetOrders ( self . ctx , self . idx , Iio0 ( symbol ) , ctypes . byref ( OoO0OO0 ) , ctypes . byref ( oOoO0o0OOooO0 ) )
  if 64 - 64: Iii1i - ooo000 . I11iiIi11i1I
  if iIii1iiiIi == I11111i111 :
   iIiI1 = OoO0OO0 . value
   Oo0O0OO0o = [ ]
   if iIiI1 > 0 :
    I111iii = ( oo00OOO * iIiI1 ) . from_address ( oOoO0o0OOooO0 . value )
    for ii in range ( 0 , iIiI1 ) :
     Oo0O0OO0o . append ( I111iii [ ii ] . toObj ( ) )
    self . lib . api_free ( oOoO0o0OOooO0 )
   return Oo0O0OO0o
  elif iIii1iiiIi == oO0O :
   return None
  iI1i1Iiii11i ( )
  if 59 - 59: iI1iI11Ii111 / IiIIii11Ii
 def GetHistoryOrders ( self , symbol = '' , since = 0 , limit = 0 ) :
  OoO0OO0 = ctypes . c_uint ( 0 )
  oOoO0o0OOooO0 = ctypes . c_void_p ( )
  iIii1iiiIi = self . lib . api_Exchange_GetHistoryOrders ( self . ctx , self . idx , Iio0 ( symbol ) , ctypes . c_longlong ( since ) , ctypes . c_longlong ( limit ) , ctypes . byref ( OoO0OO0 ) , ctypes . byref ( oOoO0o0OOooO0 ) )
  if 7 - 7: oOo0O00
  if iIii1iiiIi == I11111i111 :
   iIiI1 = OoO0OO0 . value
   Oo0O0OO0o = [ ]
   if iIiI1 > 0 :
    I111iii = ( oo00OOO * iIiI1 ) . from_address ( oOoO0o0OOooO0 . value )
    for ii in range ( 0 , iIiI1 ) :
     Oo0O0OO0o . append ( I111iii [ ii ] . toObj ( ) )
    self . lib . api_free ( oOoO0o0OOooO0 )
   return Oo0O0OO0o
  elif iIii1iiiIi == oO0O :
   return None
  iI1i1Iiii11i ( )
  if 64 - 64: IIiIIiIi11I1 * oOO + Oo . OooOoo - ooOOO
 def Log ( self , orderType , price , amount = 0 , * extra ) :
  iIii1iiiIi = self . lib . api_Exchange_Log ( self . ctx , self . idx , ctypes . c_int ( orderType ) , ctypes . c_double ( price ) , ctypes . c_double ( amount ) , i1iiiIii ( extra ) )
  if orderType == 2 :
   return bool ( iIii1iiiIi )
  if iIii1iiiIi > 0 :
   return int ( iIii1iiiIi )
   if 94 - 94: IiIIii11Ii - ooo000 . Ii
 def GetOrder ( self , orderId ) :
  OoOoOo000o00O = oo00OOO ( )
  iIii1iiiIi = self . lib . api_Exchange_GetOrder ( self . ctx , self . idx , ctypes . c_int ( orderId ) , ctypes . byref ( OoOoOo000o00O ) )
  if iIii1iiiIi == I11111i111 :
   return OoOoOo000o00O . toObj ( )
  elif iIii1iiiIi == oO0O :
   return None
  iI1i1Iiii11i ( )
  if 73 - 73: IiIIii11Ii / oOo0O00 % ooo000 . iI1iII1I1I1i % oOO
 def CancelOrder ( self , orderId , * extra ) :
  self . lib . api_Exchange_CancelOrder . restype = ctypes . c_bool
  iIii1iiiIi = self . lib . api_Exchange_CancelOrder ( self . ctx , self . idx , ctypes . c_int ( orderId ) , i1iiiIii ( extra ) )
  if iIii1iiiIi == OoIi1 :
   iI1i1Iiii11i ( )
  return iIii1iiiIi == I11111i111
  if 36 - 36: i11 * OooOoo . ooo000 . i1iiIII111 + oOO
 def GetContractType ( self ) :
  return self . ct
  if 47 - 47: i11 / I11iiIi11i1I
 def GetPeriod ( self ) :
  return int ( self . period / 1000 )
  if 52 - 52: Ii . OooOoo . i1iiIII111 * I11iiIi11i1I - iI1iII1I1I1i
 def SetContractType ( self , symbol ) :
  OoOoOo000o00O = ctypes . c_char_p ( )
  iIii1iiiIi = self . lib . api_Exchange_SetContractType ( self . ctx , self . idx , Iio0 ( symbol ) , ctypes . byref ( OoOoOo000o00O ) )
  if iIii1iiiIi == I11111i111 :
   self . ct = symbol
   if OoOoOo000o00O :
    i1I1i1I = Iii11iiiiI ( OoOoOo000o00O . value )
    self . lib . api_free ( OoOoOo000o00O )
    return i1I1i1I
   else :
    return True
  elif iIii1iiiIi == oO0O :
   return None
  iI1i1Iiii11i ( )
  if 20 - 20: OooOoo % i11 + I1Ii1I1 + i11 - oOo0O00
 def SetMarginLevel ( self , symbol , level = None ) :
  if isinstance ( symbol , int ) or isinstance ( symbol , float ) :
   level , symbol = symbol , level
  if not symbol :
   symbol = ''
  self . lib . api_Exchange_SetMarginLevel . restype = ctypes . c_bool
  return self . lib . api_Exchange_SetMarginLevel ( self . ctx , self . idx , Iio0 ( symbol ) , ctypes . c_int ( level ) )
  if 76 - 76: I11iiIi11i1I % IIiIIiIi11I1 % iI1iI11Ii111
 def SetDirection ( self , direction ) :
  self . lib . api_Exchange_SetMarginLevel . restype = ctypes . c_bool
  return self . lib . api_Exchange_SetDirection ( self . ctx , self . idx , Iio0 ( direction ) )
  if 39 - 39: IiIIii11Ii . Oo + iI1iI11Ii111 - oOo0O00
 def GetPositions ( self , symbol = '' ) :
  OoO0OO0 = ctypes . c_uint ( 0 )
  oOoO0o0OOooO0 = ctypes . c_void_p ( )
  iIii1iiiIi = self . lib . api_Exchange_GetPositions ( self . ctx , self . idx , Iio0 ( symbol ) , ctypes . byref ( OoO0OO0 ) , ctypes . byref ( oOoO0o0OOooO0 ) )
  if 93 - 93: Iii1i * IIiIIiIi11I1 % iI1iI11Ii111 + i1 % Ii * iI1iI11Ii111
  if iIii1iiiIi == I11111i111 :
   iIiI1 = OoO0OO0 . value
   Oo0O0OO0o = [ ]
   if iIiI1 > 0 :
    I111iii = ( iiiI * iIiI1 ) . from_address ( oOoO0o0OOooO0 . value )
    for ii in range ( 0 , iIiI1 ) :
     Oo0O0OO0o . append ( I111iii [ ii ] . toObj ( ) )
    self . lib . api_free ( oOoO0o0OOooO0 )
   return Oo0O0OO0o
  elif iIii1iiiIi == oO0O :
   return None
  iI1i1Iiii11i ( )
  if 62 - 62: i11 % ooo000
 def GetPosition ( self ) :
  return self . GetPositions ( )
  if 19 - 19: Ii / Oo % Iii1i / i1iiIII111 - OooOoo - Ooo0Ooo
class I1I11i1i1i ( object ) :
 def __init__ ( self , lib , ctx , js ) :
  self . lib = lib
  self . ctx = ctx
  self . lib . api_Chart_New ( self . ctx , Iio0 ( json . dumps ( js ) ) )
  if 72 - 72: IIiIIiIi11I1 * ooo000 % i1iiIII111
 def update ( self , js ) :
  self . lib . api_Chart_New ( self . ctx , Iio0 ( json . dumps ( js ) ) )
  if 23 - 23: i1iiIII111 % IiIIii11Ii % ooOOO * i11
 def add ( self , seriesIdx , d , replaceId = None ) :
  OoOoOo = [ seriesIdx , d ]
  if replaceId is not None :
   OoOoOo . append ( replaceId )
  self . lib . api_Chart_Add ( self . ctx , Iio0 ( json . dumps ( OoOoOo ) ) )
  if 62 - 62: ooOOO / oOO
 def reset ( self , keep = 0 ) :
  self . lib . api_Chart_Reset ( self . ctx , keep )
  if 39 - 39: oOo0O00 + I1I
class OO00OOo00 ( ) :
 def __init__ ( self , lib , ctx , options = { } ) :
  options [ "__isCandle" ] = True
  self . chart = I1I11i1i1i ( lib , ctx , options )
  self . bar = None
  self . overlay = options . get ( "overlay" , False )
  self . preTime = 0
  self . runtime = { "plots" : [ ] , "signals" : [ ] , "titles" : { } , "count" : 0 }
  if 70 - 70: IiIIii11Ii - oOo0O00 / oOo0O00 . i1i1i1111I
 def trim ( self , obj ) :
  OO0Ooo0O00Oo = { }
  for O0o00OO0oOOo in obj :
   if obj [ O0o00OO0oOOo ] is not None :
    OO0Ooo0O00Oo [ O0o00OO0oOOo ] = obj [ O0o00OO0oOOo ]
  return OO0Ooo0O00Oo
  if 14 - 14: iI1iI11Ii111 * i1 / I11iiIi11i1I . i1 / Ii
 def newPlot ( self , obj ) :
  I1Ii1ii = self . trim ( obj )
  if "overlay" not in I1Ii1ii :
   I1Ii1ii [ "overlay" ] = self . overlay
  if I1Ii1ii [ "type" ] != 'shape' and I1Ii1ii [ "type" ] != 'bgcolor' and I1Ii1ii [ "type" ] != 'barcolor' :
   if "title" not in I1Ii1ii or len ( I1Ii1ii [ "title" ] ) == 0 or I1Ii1ii [ "title" ] in self . runtime [ "titles" ] :
    I1Ii1ii [ "title" ] = '<' + I1Ii1ii . get ( "title" , "plot" ) + '_' + str ( self . runtime [ "count" ] ) + '>'
   self . runtime [ "count" ] += 1
   if "title" in I1Ii1ii :
    self . runtime [ "titles" ] [ I1Ii1ii [ "title" ] ] = True
  return I1Ii1ii
  if 71 - 71: IIiIIiIi11I1 - IIiIIiIi11I1
  if 84 - 84: i1iiIII111 + oOo0O00
 def begin ( self , bar ) :
  self . bar = bar
  if 83 - 83: i1i1i1111I
 def reset ( self , remain = 0 ) :
  self . chart . reset ( remain )
  self . preTime = 0
  if 84 - 84: oOO / Ii * Ooo0Ooo / Ii / ooo000
 def close ( self ) :
  if self . bar [ "Time" ] < self . preTime :
   return
   if 64 - 64: oOo0O00 * Ii
  IiIi1Ii1111 = {
 "timestamp" : self . bar [ "Time" ] ,
 "open" : self . bar [ "Open" ] ,
 "high" : self . bar [ "High" ] ,
 "low" : self . bar [ "Low" ] ,
 "close" : self . bar [ "Close" ] ,
 "volume" : self . bar . get ( "Volume" , 0 ) ,
 }
  if 2 - 2: i11 % i1iiIII111 . oOo0O00
  for O0o00OO0oOOo in [ "plots" , "signals" ] :
   if len ( self . runtime [ O0o00OO0oOOo ] ) > 0 :
    if "runtime" not in IiIi1Ii1111 :
     IiIi1Ii1111 [ "runtime" ] = { }
    IiIi1Ii1111 [ "runtime" ] [ O0o00OO0oOOo ] = self . runtime [ O0o00OO0oOOo ]
    if 59 - 59: I11iiIi11i1I % OooOoo - iI1iII1I1I1i % I1I + i1iiIII111 . I1Ii1I1
  if self . preTime == self . bar [ "Time" ] :
   self . chart . add ( 0 , IiIi1Ii1111 , - 1 )
  else :
   self . chart . add ( 0 , IiIi1Ii1111 )
   if 94 - 94: ooOOO * I1Ii1I1 * i1iiIII111 . oOo0O00
  self . preTime = self . bar [ "Time" ]
  self . runtime [ "plots" ] = [ ]
  self . runtime [ "signals" ] = [ ]
  self . runtime [ "titles" ] = { }
  self . runtime [ "count" ] = 0
  if 73 - 73: I1Ii1I1 / ooo000 % I11iiIi11i1I - i1i1i1111I + Oo - I1Ii1I1
 def plot ( self , series = None , title = None , color = None , linewidth = 1 , style = "line" , trackprice = None , histbase = 0 , offset = 0 , join = False , editable = False , show_last = None , display = "all" , overlay = None ) :
  if series is None or self . bar [ "Time" ] < self . preTime :
   return
   if 18 - 18: i1 + ooOOO . i1 - iI1iII1I1I1i
  self . runtime [ "plots" ] . append ( self . newPlot ( {
 "series" : series ,
 "overlay" : overlay ,
 "title" : title ,
 "join" : join ,
 "color" : color ,
 "histbase" : histbase ,
 "type" : style ,
 "lineWidth" : linewidth ,
 "display" : display ,
 "offset" : offset
 } ) )
  return len ( self . runtime [ "plots" ] ) - 1
  if 97 - 97: oOo0O00 + iI1iI11Ii111 % Iii1i
 def barcolor ( self , color , offset = None , editable = False , show_last = None , title = None , display = "all" ) :
  if display != "all" or self . bar [ "Time" ] < self . preTime :
   return
  self . runtime [ "plots" ] . append ( self . newPlot ( {
 "type" : 'barcolor' ,
 "title" : title ,
 "color" : color ,
 "offset" : offset ,
 "showLast" : show_last ,
 "display" : display
 } ) )
  if 34 - 34: i1 + Oo . oOo0O00 - ooo000 / I11iiIi11i1I * oOo0O00
 def plotarrow ( self , series , title = None , colorup = "#00ff00" ,
 colordown = "#ff0000" ,
 offset = 0 ,
 minheight = 5 ,
 maxheight = 100 ,
 editable = False , show_last = None , display = "all" , overlay = None ) :
  if display != "all" or self . bar [ "Time" ] < self . preTime :
   return
   if 89 - 89: oOo0O00
  self . runtime [ "plots" ] . append ( self . newPlot ( {
 "series" : series ,
 "title" : title ,
 "colorup" : colorup ,
 "colordown" : colordown ,
 "offset" : offset ,
 "minheight" : minheight ,
 "maxheight" : maxheight ,
 "showLast" : show_last ,
 "type" : "shape" ,
 "style" : "arrow" ,
 "display" : display ,
 "overlay" : overlay
 } ) )
  if 48 - 48: i1 / IIiIIiIi11I1 / iI1iII1I1I1i / i11 * IiIIii11Ii
 def hline ( self , price , title = None , color = None , linestyle = "dashed" , linewidth = None , editable = False , display = "all" , overlay = None ) :
  if display != "all" or self . bar [ "Time" ] < self . preTime :
   return
   if 54 - 54: IIiIIiIi11I1 % I1I % i11 / I11iiIi11i1I . I11iiIi11i1I - IiIIii11Ii
  self . runtime [ "plots" ] . append ( self . newPlot ( {
 "title" : title ,
 "price" : price ,
 "overlay" : overlay ,
 "color" : color ,
 "type" : 'hline' ,
 "lineStyle" : linestyle ,
 "lineWidth" : linewidth ,
 "display" : display
 } ) )
  return len ( self . runtime [ "plots" ] ) - 1
  if 10 - 10: Ii . I11iiIi11i1I % iI1iI11Ii111 / OooOoo % I1Ii1I1
  if 42 - 42: Oo - I1I * iI1iI11Ii111 * i1i1i1111I - I11iiIi11i1I
 def bgcolor ( self , color , offset = None , editable = None , show_last = None , title = None , display = "all" , overlay = None ) :
  if display != "all" or self . bar [ "Time" ] < self . preTime :
   return
  self . runtime [ "plots" ] . append ( self . newPlot ( {
 "title" : title ,
 "overlay" : overlay ,
 "color" : color ,
 "type" : 'bgcolor' ,
 "showLast" : show_last ,
 "offset" : offset
 } ) )
  if 58 - 58: iI1iII1I1I1i
  if 17 - 17: iI1iII1I1I1i - Ii % iI1iII1I1I1i % oOo0O00 * Iii1i
 def plotchar ( self , series , title = None , char = None , location = "abovebar" , color = None , offset = None , text = None , textcolor = None , editable = None , size = "auto" , show_last = None , display = "all" , overlay = None ) :
  if ( location != "absolute" and series is None ) or ( location == "absolute" and series is None ) or char is None or self . bar [ "Time" ] < self . preTime :
   return
   if 51 - 51: I1I . i1i1i1111I % Ii
  self . runtime [ "plots" ] . append ( self . newPlot ( {
 "overlay" : overlay ,
 "type" : "shape" ,
 "style" : "char" ,
 "char" : char ,
 "series" : series ,
 "location" : location ,
 "color" : color ,
 "offset" : offset ,
 "size" : size ,
 "text" : text ,
 "textColor" : textcolor
 } ) )
  if 55 - 55: i1i1i1111I * Ii % i1i1i1111I
  if 61 - 61: oOo0O00
  if 53 - 53: Ooo0Ooo / IiIIii11Ii
 def plotshape ( self , series , title = None , style = None , location = "abovebar" , color = None , offset = None , text = None , textcolor = None , editable = None , size = "auto" , show_last = None , display = "all" , overlay = None ) :
  if ( location != "absolute" and series is None ) or ( location == "absolute" and series is None ) or self . bar [ "Time" ] < self . preTime :
   return
   if 49 - 49: ooo000 - oOO . IiIIii11Ii / Oo
  self . runtime [ "plots" ] . append ( self . newPlot ( {
 "type" : "shape" ,
 "overlay" : overlay ,
 "title" : title ,
 "size" : size ,
 "style" : style ,
 "series" : series ,
 "location" : location ,
 "color" : color ,
 "offset" : offset ,
 "text" : text ,
 "textColor" : textcolor
 } ) )
  if 23 - 23: I11iiIi11i1I - i1 / Iii1i . iI1iII1I1I1i + oOO
 def plotcandle ( self , open , high , low , close , title = None , color = None , wickcolor = None , editable = None , show_last = None , bordercolor = None , display = "all" , overlay = None ) :
  if display != "all" or self . bar [ "Time" ] < self . preTime :
   return
   if 55 - 55: i1 - iI1iII1I1I1i / OooOoo + I1I + Oo
  self . runtime [ "plots" ] . append ( self . newPlot ( {
 "price" : high ,
 "open" : open ,
 "high" : high ,
 "low" : low ,
 "close" : close ,
 "title" : title ,
 "color" : color ,
 "wickColor" : wickcolor ,
 "showLast" : show_last ,
 "borderColor" : bordercolor ,
 "type" : "candle" ,
 "display" : display ,
 "overlay" : overlay ,
 } ) )
  if 5 - 5: i11 - i1 . i1i1i1111I / i11 . iI1iII1I1I1i . i11
 def fill ( self , plot1 , plot2 , color = None , title = None , editable = None , show_last = None , fillgaps = None , display = "all" ) :
  if self . bar [ "Time" ] < self . preTime :
   return
  if plot1 >= 0 and plot2 >= 0 and plot1 < len ( self . runtime [ "plots" ] ) and plot2 < len ( self . runtime [ "plots" ] ) and display == "all" :
   OO0Ooo0O00Oo = self . runtime [ "plots" ] [ plot1 ]
   if "fill" not in OO0Ooo0O00Oo :
    OO0Ooo0O00Oo [ "fill" ] = [ ]
   OO0Ooo0O00Oo [ "fill" ] . append ( self . trim ( {
 "value" : self . runtime [ "plots" ] [ plot2 ] [ "series" ] ,
 "color" : color ,
 "showLast" : show_last
 } ) )
   if 87 - 87: i1 . Ii * iI1iII1I1I1i - oOO / Ii / OooOoo
 def signal ( self , direction , price , qty , id = None ) :
  if self . bar [ "Time" ] < self . preTime :
   return
  o0O000OoOo00o = {
 "id" : id or direction ,
 "avgPrice" : price ,
 "qty" : qty
 }
  if direction == "buy" or direction == "long" :
   o0O000OoOo00o [ "direction" ] = "long"
  elif direction == "sell" or direction == "short" :
   o0O000OoOo00o [ "direction" ] = "short"
  elif direction == "closesell" or direction == "closeshort" :
   o0O000OoOo00o [ "direction" ] = "close"
   o0O000OoOo00o [ "closeDirection" ] = "short"
  elif direction == "closebuy" or direction == "closelong" :
   o0O000OoOo00o [ "direction" ] = "close"
   o0O000OoOo00o [ "closeDirection" ] = "long"
   if 53 - 53: Ii + iI1iI11Ii111 % I1Ii1I1
  if o0O000OoOo00o [ "direction" ] or o0O000OoOo00o [ "closeDirection" ] :
   self . runtime [ "signals" ] . append ( o0O000OoOo00o )
   if 81 - 81: oOO - Ii - ooo000 + i1iiIII111 % Ooo0Ooo * Ooo0Ooo
def Ii1IiiI1 ( s , default ) :
 I1 = default
 if len ( s ) < 2 :
  return I1
 O0oOoOoO0o = int ( s [ : - 1 ] )
 ooO0ooOOO00O0 = s [ - 1 ]
 if ooO0ooOOO00O0 == 'd' :
  I1 = O0oOoOoO0o * 60000 * 60 * 24
 elif ooO0ooOOO00O0 == 'm' :
  I1 = O0oOoOoO0o * 60000
 elif ooO0ooOOO00O0 == 'm' :
  I1 = O0oOoOoO0o * 60000
 return I1
 if 58 - 58: oOO . I1I * Ii
def O00ooo0000oO ( s ) :
 Iiii1i = s
 o00oOo0OOOO00 = { }
 for OO0OOo in Iiii1i . split ( '\n' ) :
  OO0OOo = OO0OOo . strip ( )
  if ':' not in OO0OOo :
   continue
  OooO0Oo = OO0OOo . split ( ':' , 1 )
  if len ( OooO0Oo ) == 2 :
   O0o00OO0oOOo = OooO0Oo [ 0 ] . strip ( )
   O0OOooO = OooO0Oo [ 1 ] . strip ( )
   o00oOo0OOOO00 [ O0o00OO0oOOo ] = O0OOooO
 OOOOo = o00oOo0OOOO00 . get ( 'pnl' , 'true' )
 iI = o00oOo0OOOO00 . get ( 'dataServer' , i1ii1 )
 I1 = Ii1IiiI1 ( o00oOo0OOOO00 . get ( 'period' , '1h' ) , 60000 * 60 )
 OoOo = Ii1IiiI1 ( o00oOo0OOOO00 . get ( 'basePeriod' , '' ) , 0 )
 if 49 - 49: IIiIIiIi11I1 / i1iiIII111 % IIiIIiIi11I1 + IIiIIiIi11I1 * iI1iII1I1I1i
 Ii11o0o0oo0ooO = [ ]
 for i1i in json . loads ( o00oOo0OOOO00 . get ( 'exchanges' , '[]' ) ) :
  OooO0Oo = i1i [ 'currency' ] . upper ( ) . split ( '_' )
  if len ( OooO0Oo ) == 1 :
   OooO0Oo . append ( 'CNY' if 'CTP' in i1i [ 'eid' ] else 'USD' )
  if OoOo == 0 :
   OoOo = 60000 * 60
   if I1 == 86400000 :
    OoOo = 60000 * 60
   elif I1 == 3600000 :
    OoOo = 60000 * 30
   elif I1 == 1800000 :
    OoOo = 60000 * 15
   elif I1 == 900000 :
    OoOo = 60000 * 5
   elif I1 == 300000 :
    OoOo = 60000
  iIIi1111I1 = {
 'Huobi' : [ 150 , 200 ] ,
 'OKX' : [ 150 , 200 ] ,
 'Binance' : [ 150 , 200 ] ,
 'Futures_BitMEX' : [ 8 , 10 ] ,
 'Futures_OKX' : [ 30 , 30 ] ,
 'Futures_HuobiDM' : [ 30 , 30 ] ,
 'Futures_CTP' : [ 25 , 25 ] ,
 'Futures_XTP' : [ 30 , 130 ] ,
 }
  if 63 - 63: Iii1i
  o0O0 = i1i . get ( 'fee' )
  if o0O0 is None :
   o0O0 = iIIi1111I1 . get ( i1i [ 'eid' ] , [ 2000 , 2000 ] )
  else :
   o0O0 = [ int ( o0O0 [ 0 ] * 10000 ) , int ( o0O0 [ 1 ] * 10000 ) ]
   if 90 - 90: I1Ii1I1 - Oo . OooOoo % I1I / I11iiIi11i1I % ooOOO
  OoOOO0o0 = {
 "Balance" : i1i . get ( 'balance' , 10000.0 ) ,
 "Stocks" : i1i . get ( 'stocks' , 3.0 ) ,
 "BaseCurrency" : OooO0Oo [ 0 ] ,
 "QuoteCurrency" : OooO0Oo [ 1 ] ,
 "BasePeriod" : OoOo ,
 "FeeDenominator" : 6 ,
 "FeeMaker" : o0O0 [ 0 ] ,
 "FeeTaker" : o0O0 [ 1 ] ,
 "FeeMin" : i1i . get ( 'feeMin' , 0 ) ,
 "Id" : i1i [ 'eid' ] ,
 "Label" : i1i [ 'eid' ]
 }
  Ii11o0o0oo0ooO . append ( OoOOO0o0 )
  if 29 - 29: i1i1i1111I * Ii * i1i1i1111I
 O0Oo0o0o = {
 "DataServer" : iI ,
 "MaxChartLogs" : 800 ,
 "MaxProfitLogs" : 800 ,
 "MaxRuntimeLogs" : 800 ,
 "NetDelay" : 200 ,
 "Period" : I1 ,
 "RetFlags" : iiI1111IIi1 | OoO | iIIiiIi1Ii1I | ii1IiIiiII | iii11i | I1I111i11I ,
 "TimeBegin" : int ( time . mktime ( datetime . datetime . strptime ( o00oOo0OOOO00 . get ( 'start' , '2019-02-01 00:00:00' ) , "%Y-%m-%d %H:%M:%S" ) . timetuple ( ) ) ) ,
 "TimeEnd" : int ( time . mktime ( datetime . datetime . strptime ( o00oOo0OOOO00 . get ( 'end' , '2019-02-10 00:00:00' ) , "%Y-%m-%d %H:%M:%S" ) . timetuple ( ) ) ) ,
 "UpdatePeriod" : 5000
 }
 I1I1i1ii = 86400
 Iii1I1 = O0Oo0o0o [ 'TimeEnd' ] - O0Oo0o0o [ 'TimeBegin' ]
 if Iii1I1 / 3600 <= 2 :
  I1I1i1ii = 60
 elif Iii1I1 / 86400 <= 2 :
  I1I1i1ii = 300
 elif Iii1I1 / 86400 < 30 :
  I1I1i1ii = 3600
 O0Oo0o0o [ 'SnapshotPeriod' ] = I1I1i1ii * 1000
 if OOOOo == 'true' :
  O0Oo0o0o [ 'RetFlags' ] |= oo0
 return { 'Exchanges' : Ii11o0o0oo0ooO , 'Options' : O0Oo0o0o }
 if 73 - 73: I1Ii1I1 . Iii1i + iI1iI11Ii111 / ooo000 / oOo0O00 . I1Ii1I1
class I1II1i11i11I ( ) :
 pass
 if 7 - 7: Ooo0Ooo
class i111IIi ( object ) :
 def __init__ ( self , task = None , autoRun = False , gApis = None , progressCallback = None ) :
  self . _joinResult = None
  self . gs = threading . Lock ( )
  if gApis is None :
   if __name__ == "__main__" :
    gApis = globals ( )
   else :
    gApis = dict ( inspect . getmembers ( inspect . stack ( ) [ 1 ] [ 0 ] ) ) [ "f_globals" ]
    if 82 - 82: IIiIIiIi11I1 - IiIIii11Ii / oOO
  if task is None :
   task = O00ooo0000oO ( gApis [ '__doc__' ] )
  elif hasattr ( task , 'upper' ) :
   task = O00ooo0000oO ( task )
   if 49 - 49: iI1iI11Ii111 / ooo000 * i11 . oOo0O00
  if progressCallback is not None :
   self . progressCallback = progressCallback
   if 32 - 32: i1i1i1111I . OooOoo + OooOoo - ooo000 * IiIIii11Ii + Oo
  self . httpGetPtr = ctypes . CFUNCTYPE ( ctypes . c_int , ctypes . c_char_p , ctypes . POINTER ( ctypes . c_char_p ) , ctypes . POINTER ( ctypes . c_int ) , ctypes . POINTER ( ctypes . c_int ) ) ( self . httpGetCallback )
  self . progessCallbackPtr = ctypes . CFUNCTYPE ( None , ctypes . c_char_p ) ( self . progressCallback )
  iIIIii = platform . system ( )
  iI111Iii = platform . architecture ( ) [ 0 ]
  if platform . processor ( ) == "arm" :
   iI111Iii = 'arm64' if iI111Iii == '64bit' else 'arm'
  self . os = '%s/%s' % ( iIIIii . lower ( ) , iI111Iii )
  Ii11IIiIII = 'backtest_py_%s_%s_v2.so' % ( iIIIii . lower ( ) , iI111Iii )
  i1i1IiiIIII = 'md5_v2.json'
  iIII = os . path . join ( "./depends" , Ii11IIiIII )
  if not os . path . exists ( iIII ) :
   OOOI1iIiiIiII1 = { }
   oooOo = oo0o0oO ( )
   OOO00oOO0 = os . path . join ( oooOo , i1i1IiiIIII )
   if os . path . exists ( OOO00oOO0 ) :
    IiIII11 = open ( OOO00oOO0 , 'rb' ) . read ( )
    if os . getenv ( "BOTVS_TASK_UUID" ) is None or "0effa06859fb56230e100371bc1e1660" in str ( IiIII11 ) :
     OOOI1iIiiIiII1 = Iii11iiiiI ( IiIII11 )
   iIII = os . path . join ( oooOo , Ii11IIiIII )
   oOOOOo0 = False
   if not os . path . exists ( iIII ) :
    oOOOOo0 = True
   else :
    i1i1I1iII1iI = md5 . md5 ( open ( iIII , 'rb' ) . read ( ) ) . hexdigest ( )
    if i1i1I1iII1iI != OOOI1iIiiIiII1 . get ( Ii11IIiIII , None ) :
     oOOOOo0 = True
     oOoO0o0OOoO0 = os . path . join ( oooOo , i1i1I1iII1iI )
     try :
      os . rename ( iIII , oOoO0o0OOoO0 )
      os . remove ( oOoO0o0OOoO0 )
     except :
      pass
   if oOOOOo0 :
    open ( iIII , 'wb' ) . write ( iIIiii1iI ( task [ "Options" ] [ "DataServer" ] + "/dist/depends/" + Ii11IIiIII ) )
    open ( OOO00oOO0 , 'wb' ) . write ( iIIiii1iI ( task [ "Options" ] [ "DataServer" ] + "/dist/depends/" + i1i1IiiIIII ) )
  else :
   print ( "load from debug mode" , iIII )
  O00O0oO000 = ctypes . CDLL ( os . path . abspath ( iIII ) )
  O00O0oO000 . api_backtest . restype = ctypes . c_void_p
  i11Ii = ctypes . c_void_p ( O00O0oO000 . api_backtest ( Iio0 ( json . dumps ( task ) ) , self . httpGetPtr , self . progessCallbackPtr ) )
  if not i11Ii :
   raise 'Initialize backtest engine error'
  self . ctx = i11Ii
  self . lib = O00O0oO000
  self . cache = { }
  self . kvdb = { }
  self . cRetryDelay = 3000
  if 83 - 83: iI1iI11Ii111 . ooo000 * Ooo0Ooo + Iii1i . Oo
  Ii11o0o0oo0ooO = [ ]
  ii = 0
  for i1oO00oO00O0O in task [ "Exchanges" ] :
   Ii11o0o0oo0ooO . append ( OoOooOOoOo ( O00O0oO000 , i11Ii , ii , task [ "Options" ] , i1oO00oO00O0O ) )
   ii += 1
   if 34 - 34: I11iiIi11i1I % oOO
  for O0o00OO0oOOo in dir ( self ) :
   if O0o00OO0oOOo . startswith ( 'g_' ) :
    gApis [ O0o00OO0oOOo [ 2 : ] ] = getattr ( self , O0o00OO0oOOo )
    if 75 - 75: i1 % IiIIii11Ii - iI1iII1I1I1i - iI1iI11Ii111 * I11iiIi11i1I * OooOoo
  self . realTime = time . time
  time . time = self . g_PyTime
  gApis [ '__name__' ] = '__main__'
  gApis [ "TA" ] = oOoOO0O0 ( self . _logTA )
  gApis [ 'exchanges' ] = Ii11o0o0oo0ooO
  gApis [ 'exchange' ] = Ii11o0o0oo0ooO [ 0 ]
  gApis [ 'ext' ] = I1II1i11i11I ( )
  gApis [ 'time' ] = time
  gApis [ 'null' ] = None
  gApis [ 'true' ] = True
  gApis [ 'false' ] = False
  gApis [ "ORDER_STATE_PENDING" ] = 0
  gApis [ "ORDER_STATE_CLOSED" ] = 1
  gApis [ "ORDER_STATE_CANCELED" ] = 2
  gApis [ "ORDER_STATE_UNKNOWN" ] = 3
  gApis [ "ORDER_TYPE_BUY" ] = 0
  gApis [ "ORDER_TYPE_SELL" ] = 1
  gApis [ "ORDER_OFFSET_OPEN" ] = 0
  gApis [ "ORDER_OFFSET_CLOSE" ] = 1
  if 45 - 45: IIiIIiIi11I1
  gApis [ "PD_LONG" ] = 0
  gApis [ "PD_SHORT" ] = 1
  gApis [ "PD_LONG_YD" ] = 2
  gApis [ "PD_SHORT_YD" ] = 3
  if 14 - 14: i1i1i1111I - OooOoo . IiIIii11Ii
  gApis [ "LOG_TYPE_BUY" ] = 0
  gApis [ "LOG_TYPE_SELL" ] = 1
  gApis [ "LOG_TYPE_CANCEL" ] = 2
  gApis [ "LOG_TYPE_ERROR" ] = 3
  gApis [ "LOG_TYPE_PROFIT" ] = 4
  gApis [ "LOG_TYPE_LOG" ] = 5
  gApis [ "LOG_TYPE_RESTART" ] = 6
  if 40 - 40: I1I - IIiIIiIi11I1 % IiIIii11Ii
  gApis [ "PERIOD_M1" ] = 60 * 1
  gApis [ "PERIOD_M3" ] = 60 * 3
  gApis [ "PERIOD_M5" ] = 60 * 5
  gApis [ "PERIOD_M15" ] = 60 * 15
  gApis [ "PERIOD_M30" ] = 60 * 30
  gApis [ "PERIOD_H1" ] = 60 * 60
  gApis [ "PERIOD_H2" ] = 60 * 60 * 2
  gApis [ "PERIOD_H4" ] = 60 * 60 * 4
  gApis [ "PERIOD_H6" ] = 60 * 60 * 6
  gApis [ "PERIOD_H12" ] = 60 * 60 * 12
  gApis [ "PERIOD_D1" ] = 60 * 60 * 24
  gApis [ "PERIOD_D3" ] = 60 * 60 * 24 * 3
  gApis [ "PERIOD_W1" ] = 60 * 60 * 24 * 7
  if 61 - 61: iI1iII1I1I1i
  if autoRun :
   try :
    gApis [ 'main' ] ( )
   except EOFError :
    pass
   self . Join ( )
   if 93 - 93: i1iiIII111 - oOo0O00 . Oo . i1iiIII111 . Oo * I1Ii1I1
 def httpGetCallback ( self , path , ptr_buf , ptr_size , ptr_need_free ) :
  iiI1IIiI1i = path . decode ( 'utf8' )
  oooOo = oo0o0oO ( )
  Ii11iI1I = oooOo + '/botvs_kline_' + md5 . md5 ( path ) . hexdigest ( )
  IiIi1Ii1111 = None
  try :
   if os . path . exists ( Ii11iI1I ) :
    IiIi1Ii1111 = open ( Ii11iI1I , 'rb' ) . read ( )
    Ii11iI1I = None
   else :
    IiIi1Ii1111 = iIIiii1iI ( iiI1IIiI1i )
    if len ( IiIi1Ii1111 ) > 0 :
     open ( Ii11iI1I , 'wb' ) . write ( IiIi1Ii1111 )
  except :
   pass
  if IiIi1Ii1111 is None :
   return 1
  ptr_size . contents . value = len ( IiIi1Ii1111 )
  ptr_need_free . contents . value = 0
  oooO0o0o0oOOo = ctypes . create_string_buffer ( IiIi1Ii1111 )
  ptr_buf . contents . value = ctypes . addressof ( oooO0o0o0oOOo )
  self . cache [ Ii11iI1I ] = oooO0o0o0oOOo
  return 0
  if 59 - 59: ooOOO
 def progressCallback ( self , st ) :
  pass
  if 86 - 86: i1iiIII111 % ooo000 % ooo000 % iI1iI11Ii111
 def _logTA ( self , name , args ) :
  self . lib . api_LogTA ( self . ctx , name , args )
  if 15 - 15: iI1iII1I1I1i + I1Ii1I1 % oOo0O00
 def g_Unix ( self ) :
  self . lib . api_Unix . restype = ctypes . c_ulonglong
  return self . lib . api_Unix ( self . ctx )
  if 79 - 79: OooOoo . Oo + oOo0O00 / I1Ii1I1 . IiIIii11Ii
 def g_UnixNano ( self ) :
  self . lib . api_UnixNano . restype = ctypes . c_ulonglong
  return self . lib . api_UnixNano ( self . ctx )
  if 89 - 89: ooo000 % Ooo0Ooo
 def g_PyTime ( self ) :
  return float ( self . g_UnixNano ( ) ) / 1e9
  if 77 - 77: ooo000 % Ooo0Ooo
 def g_Sleep ( self , n ) :
  if self . lib . api_Sleep ( self . ctx , ctypes . c_double ( n ) ) != 0 :
   iI1i1Iiii11i ( )
   if 24 - 24: oOO * I1Ii1I1 * I1Ii1I1 % IIiIIiIi11I1
 def g_EnableLog ( self , flag = True ) :
  self . lib . api_EnableLog ( self . ctx , ctypes . c_bool ( flag ) )
  if 37 - 37: i1iiIII111 / iI1iII1I1I1i
 def g_Log ( self , * extra ) :
  self . lib . api_Log ( self . ctx , i1iiiIii ( extra ) )
  if 80 - 80: IiIIii11Ii
 def g_LogReset ( self , keep = 0 ) :
  self . lib . api_LogReset ( self . ctx , ctypes . c_int ( keep ) )
  if 2 - 2: I1I / oOO - IIiIIiIi11I1 % Ooo0Ooo
 def g_LogVacuum ( self ) :
  pass
  if 88 - 88: iI1iII1I1I1i - I1Ii1I1 - iI1iI11Ii111 . Iii1i
 def g_LogStatus ( self , * extra ) :
  self . lib . api_LogStatus ( self . ctx , i1iiiIii ( extra ) )
  if 98 - 98: Ii + ooOOO
 def g_LogProfit ( self , profit , * extra ) :
  self . lib . api_LogProfit ( self . ctx , ctypes . c_double ( profit ) , i1iiiIii ( extra ) )
  if 29 - 29: I1Ii1I1 + iI1iI11Ii111 - IIiIIiIi11I1 * I11iiIi11i1I % Oo
 def g_LogProfitReset ( self , keep = 0 ) :
  self . lib . api_LogProfitReset ( self . ctx , ctypes . c_int ( keep ) )
  if 74 - 74: ooOOO
 def g_LogError ( self , * extra ) :
  self . lib . api_LogError ( self . ctx , i1iiiIii ( extra ) )
  if 100 - 100: oOO + iI1iII1I1I1i . I1I % Oo - i1
 def g_Panic ( self , * extra ) :
  self . lib . api_LogError ( self . ctx , i1iiiIii ( extra ) )
  iI1i1Iiii11i ( )
  if 39 - 39: iI1iII1I1I1i
 def g_GetLastError ( self ) :
  return ''
  if 34 - 34: iI1iII1I1I1i . i1 . I1I
 def g_MD5 ( self , s ) :
  return md5 . md5 ( Iio0 ( s ) ) . hexdigest ( )
  if 95 - 95: IiIIii11Ii * i11 * Ooo0Ooo * i11 / OooOoo
 def g_HttpQuery ( self , * args ) :
  return 'dummy'
  if 27 - 27: iI1iI11Ii111 . IiIIii11Ii
 def g_JSONParse ( self , s ) :
  return json . loads ( s )
  if 69 - 69: oOO % i1iiIII111 / oOo0O00
 def g_UUID ( self ) :
  return str ( uuid . uuid4 ( ) )
  if 38 - 38: I11iiIi11i1I + Oo * Ooo0Ooo / ooOOO . OooOoo
 def g_StrDecode ( self , s , c = 'gbk' ) :
  self . g_LogError ( "sandbox not support StrDecode" )
  if 90 - 90: OooOoo / i1iiIII111
 def g_EnableLogLocal ( self , b ) :
  pass
  if 32 - 32: IIiIIiIi11I1 - iI1iI11Ii111 / ooOOO * Ooo0Ooo * iI1iII1I1I1i - i1i1i1111I
 def g_Dial ( self , * args ) :
  self . g_LogError ( "sandbox not support Dial" )
  if 82 - 82: ooo000
 def g_Mail ( self , * args ) :
  return True
  if 66 - 66: IiIIii11Ii + IIiIIiIi11I1 - iI1iI11Ii111 + i1i1i1111I . iI1iII1I1I1i * IiIIii11Ii
 def g_GetCommand ( self ) :
  return ''
  if 9 - 9: I1I - I1I - ooOOO - oOo0O00 + i1iiIII111
 def g_GetMeta ( self ) :
  return None
  if 71 - 71: iI1iI11Ii111 / i1iiIII111 - Ii * Oo . iI1iII1I1I1i
 def g_SetErrorFilter ( self , s ) :
  pass
  if 3 - 3: I1Ii1I1
 def g_GetOS ( self ) :
  return self . os
  if 57 - 57: Ooo0Ooo . OooOoo / oOo0O00 * I1Ii1I1
 def g_Version ( self ) :
  return '3.3'
  if 36 - 36: IiIIii11Ii
 def g_IsVirtual ( self ) :
  return True
  if 33 - 33: IiIIii11Ii
 def g_Chart ( self , js ) :
  return I1I11i1i1i ( self . lib , self . ctx , js )
  if 86 - 86: Ii / oOo0O00 - i1 * i1i1i1111I - Oo * Iii1i
 def g_KLineChart ( self , js = { } ) :
  return OO00OOo00 ( self . lib , self . ctx , js )
  if 28 - 28: OooOoo . i1 % iI1iII1I1I1i % Iii1i
 def g_GetPid ( self ) :
  return os . getpid ( )
  if 2 - 2: Oo + OooOoo - i1i1i1111I - ooo000 / Oo . Oo
 def g__Cross ( self , arr1 , arr2 ) :
  if len ( arr1 ) != len ( arr2 ) :
   raise Exception ( "cross array length not equal" )
  iIiI1 = 0
  for ii in range ( len ( arr1 ) - 1 , - 1 , - 1 ) :
   if arr1 [ ii ] is None or arr2 [ ii ] is None :
    break
   if arr1 [ ii ] < arr2 [ ii ] :
    if iIiI1 > 0 :
     break
    iIiI1 -= 1
   elif arr1 [ ii ] > arr2 [ ii ] :
    if iIiI1 < 0 :
     break
    iIiI1 += 1
   else :
    break
  return iIiI1
  if 41 - 41: OooOoo + OooOoo - OooOoo
 def g__G ( self , k = '__wtf__' , v = '__wtf__' ) :
  if k == '__wtf__' :
   return 1
  elif k is None :
   self . kvdb = { }
  else :
   k = k . lower ( )
   if v is None :
    if hasattr ( self . kvdb , k ) :
     delattr ( self . kvdb , k )
   elif v == '__wtf__' :
    return self . kvdb . get ( k , None )
   elif v is not None :
    self . kvdb [ k ] = v
    if 9 - 9: Iii1i % I1Ii1I1 % IiIIii11Ii - I1I * OooOoo
 def g__CDelay ( self , d ) :
  if d > 0 :
   self . cRetryDelay = d
   if 53 - 53: iI1iII1I1I1i * i1i1i1111I / OooOoo . iI1iI11Ii111 . ooo000
 def g__C ( self , pfn , * arg ) :
  while True :
   iIii1iiiIi = pfn ( * arg )
   if iIii1iiiIi == False or iIii1iiiIi is None :
    self . g_Sleep ( self . cRetryDelay )
   else :
    return iIii1iiiIi
 def g__D ( self , date = None , fmt = None ) :
  if date is None :
   date = self . g_Unix ( )
  if fmt is None :
   fmt = '%Y-%m-%d %H:%M:%S'
  return time . strftime ( fmt , time . localtime ( date ) )
  if 45 - 45: OooOoo + ooOOO / i1i1i1111I * i1
 def g__T ( self , a , b = None ) :
  OoOoOo000o00O = str ( a )
  if b is not None :
   OoOoOo000o00O = str ( a ) + '|' + str ( b )
  return '[trans]' + OoOoOo000o00O + '[/trans]'
  if 71 - 71: i11 % Iii1i + oOo0O00 * I11iiIi11i1I / i11
 def g__N ( self , n , precision = 4 ) :
  if precision < 0 :
   I1iiII = 10 ** - precision
   return n - ( n % I1iiII )
  else :
   i11i1iIIi = 1 / ( 10 ** ( max ( 10 , precision + 5 ) ) )
   return int ( ( n + i11i1iIIi ) * ( 10 ** precision ) ) / ( 10 ** precision )
   if 50 - 50: IiIIii11Ii - I1Ii1I1 % i1i1i1111I - iI1iI11Ii111 . i1i1i1111I
 def Show ( self ) :
  import matplotlib . pyplot as plt
  from matplotlib import ticker
  try :
   from IPython import get_ipython
   get_ipython ( ) . run_line_magic ( 'matplotlib' , 'inline' )
   from pandas . plotting import register_matplotlib_converters
   register_matplotlib_converters ( )
  except :
   pass
   if 2 - 2: Ii / ooo000 . I11iiIi11i1I
   if 37 - 37: I11iiIi11i1I * Ooo0Ooo - ooo000 * oOO . i11 % OooOoo
  def oo0oo0 ( self ) :
   try :
    IiIi1Ii1111 = json . loads ( self . Join ( ) . decode ( 'utf-8' ) )
   except :
    return
   o00oOo0OOOO00 = { }
   o00oOo0OOOO00 [ 'timeStamp' ] = [ ]
   o00oOo0OOOO00 [ 'assets' ] = [ ]
   o00oOo0OOOO00 [ 'surplus' ] = [ ]
   o00oOo0OOOO00 [ 'loss' ] = [ ]
   o00oOo0OOOO00 [ 'moneyUse' ] = [ ]
   o00oOo0OOOO00 [ 'unit' ] = ''
   O0000oO0O0o = 0
   for ii in IiIi1Ii1111 [ 'Snapshots' ] :
    if not ii [ 1 ] :
     continue
    iIio0000o = 0
    ii1iiII111IiI = 0
    for ooOOOoOO0 in range ( 0 , len ( ii [ 1 ] ) ) :
     oo000O0oOO = ii [ 1 ] [ ooOOOoOO0 ]
     IiiIII1iI111i = IiIi1Ii1111 [ 'Task' ] [ 'Exchanges' ] [ ooOOOoOO0 ]
     OOoO0oOoOo = oo000O0oOO [ 'Symbols' ]
     if OOoO0oOoOo :
      i1iiiiiIIIiii = 0
      ooO0OOo = 0
      o0ooo0oOoO = 0
      Oo0OoOo = 0
      for O0oOO0Oo00ooo in OOoO0oOoOo :
       if 'Long' in OOoO0oOoOo [ O0oOO0Oo00ooo ] :
        o0O00 = OOoO0oOoOo [ O0oOO0Oo00ooo ] [ 'Long' ]
        i1iiiiiIIIiii += o0O00 [ 'Margin' ]
        ooO0OOo += o0O00 [ 'Profit' ]
       if 'Short' in OOoO0oOoOo [ O0oOO0Oo00ooo ] :
        I1Oo0 = OOoO0oOoOo [ O0oOO0Oo00ooo ] [ 'Short' ]
        i1iiiiiIIIiii += I1Oo0 [ 'Margin' ]
        ooO0OOo += I1Oo0 [ 'Profit' ]
       if 'Stocks' in OOoO0oOoOo [ O0oOO0Oo00ooo ] :
        o0ooo0oOoO += ( OOoO0oOoOo [ O0oOO0Oo00ooo ] [ 'Stocks' ] + OOoO0oOoOo [ O0oOO0Oo00ooo ] [ 'FrozenStocks' ] ) * OOoO0oOoOo [ O0oOO0Oo00ooo ] [ 'Last' ]
        Oo0OoOo += ( OOoO0oOoOo [ O0oOO0Oo00ooo ] [ 'Stocks' ] + OOoO0oOoOo [ O0oOO0Oo00ooo ] [ 'FrozenStocks' ] - IiiIII1iI111i [ 'Stocks' ] ) * OOoO0oOoOo [ O0oOO0Oo00ooo ] [ 'Last' ]
        if 31 - 31: Ii - ooOOO / Ii . i1
      if oo000O0oOO [ 'QuoteCurrency' ] == 'CNY' :
       iIio0000o += oo000O0oOO [ 'Balance' ] + oo000O0oOO [ 'FrozenBalance' ] + ooO0OOo + i1iiiiiIIIiii
       ii1iiII111IiI += i1iiiiiIIIiii / iIio0000o
       o00oOo0OOOO00 [ 'unit' ] = '(CNY)'
      elif 'Futures_' in oo000O0oOO [ 'Id' ] :
       if oo000O0oOO [ 'QuoteCurrency' ] == 'USDT' :
        iIio0000o += oo000O0oOO [ 'Balance' ] + oo000O0oOO [ 'FrozenBalance' ] + ooO0OOo + i1iiiiiIIIiii
        ii1iiII111IiI += i1iiiiiIIIiii / iIio0000o
        o00oOo0OOOO00 [ 'unit' ] = '(USDT)'
       else :
        iIio0000o += oo000O0oOO [ 'Stocks' ] + oo000O0oOO [ 'FrozenStocks' ] + ooO0OOo + i1iiiiiIIIiii
        ii1iiII111IiI += i1iiiiiIIIiii / iIio0000o
        o00oOo0OOOO00 [ 'unit' ] = '(%s)' % ( oo000O0oOO [ "BaseCurrency" ] , )
      else :
       iIio0000o += oo000O0oOO [ 'Balance' ] + oo000O0oOO [ 'FrozenBalance' ] + o0ooo0oOoO
       ii1iiII111IiI += abs ( Oo0OoOo ) / iIio0000o
       o00oOo0OOOO00 [ 'unit' ] = '(USD)'
    o00oOo0OOOO00 [ 'timeStamp' ] . append ( datetime . datetime . fromtimestamp ( ii [ 0 ] / 1000 ) . date ( ) )
    o00oOo0OOOO00 [ 'assets' ] . append ( iIio0000o )
    o00oOo0OOOO00 [ 'moneyUse' ] . append ( ii1iiII111IiI )
    if O0000oO0O0o != 0 :
     O0o0o0o0O = iIio0000o - O0000oO0O0o
     if O0o0o0o0O > 0 :
      o00oOo0OOOO00 [ 'surplus' ] . append ( O0o0o0o0O )
      o00oOo0OOOO00 [ 'loss' ] . append ( 0 )
     elif O0o0o0o0O < 0 :
      o00oOo0OOOO00 [ 'surplus' ] . append ( 0 )
      o00oOo0OOOO00 [ 'loss' ] . append ( O0o0o0o0O )
     else :
      o00oOo0OOOO00 [ 'surplus' ] . append ( 0 )
      o00oOo0OOOO00 [ 'loss' ] . append ( 0 )
    else :
     o00oOo0OOOO00 [ 'surplus' ] . append ( 0 )
     o00oOo0OOOO00 [ 'loss' ] . append ( 0 )
    O0000oO0O0o = iIio0000o
   return o00oOo0OOOO00
   if 10 - 10: Ii % OooOoo - oOo0O00 / i1iiIII111 + ooo000
   if 90 - 90: i1iiIII111 + ooOOO - i1i1i1111I / OooOoo / Oo % OooOoo
  plt . rcParams [ 'axes.unicode_minus' ] = False
  if 14 - 14: iI1iII1I1I1i - i1iiIII111
  if 53 - 53: oOO
  IiIi1Ii1111 = oo0oo0 ( self )
  if IiIi1Ii1111 :
   oOOOooo0O = IiIi1Ii1111 [ 'timeStamp' ]
   iIio0000o = IiIi1Ii1111 [ 'assets' ]
   iii1iII = IiIi1Ii1111 [ 'surplus' ]
   IiiII1 = IiIi1Ii1111 [ 'loss' ]
   ii1iiII111IiI = IiIi1Ii1111 [ 'moneyUse' ]
   iiiiiiiii = IiIi1Ii1111 [ 'unit' ]
   if 52 - 52: i1i1i1111I * iI1iI11Ii111 % ooOOO
   plt . figure ( figsize = ( 14 , 8 ) )
   plt . subplots_adjust ( left = 0.090 , right = 0.930 )
   plt . subplots_adjust ( hspace = 0 , wspace = 0 )
   ii1 = plt . subplot ( 311 )
   plt . title ( u'Backtest' , fontsize = 18 )
   plt . grid ( linestyle = '--' , color = '#D9D9D9' )
   plt . plot ( oOOOooo0O , iIio0000o , color = '#3A859E' , label = u'Equity %s %f' % ( iiiiiiiii , iIio0000o [ - 1 ] ) )
   plt . fill_between ( oOOOooo0O , min ( iIio0000o ) , iIio0000o , color = '#D0DBE8' , alpha = .5 )
   plt . legend ( loc = 'upper left' )
   ii1 = plt . subplot ( 312 )
   plt . grid ( linestyle = '--' , color = '#D9D9D9' )
   plt . bar ( oOOOooo0O , iii1iII , color = 'r' )
   plt . bar ( oOOOooo0O , IiiII1 , color = 'g' )
   plt . legend ( loc = 'upper left' , labels = [ u'Win' + iiiiiiiii , u'Loss' + iiiiiiiii ] )
   if 57 - 57: i1iiIII111 . Oo
   ii1 = plt . subplot ( 313 )
   plt . grid ( linestyle = '--' , color = '#D9D9D9' )
   plt . plot ( oOOOooo0O , ii1iiII111IiI , color = '#EBB000' , label = 'Utilization' )
   ii1 . yaxis . set_major_formatter ( ticker . PercentFormatter ( xmax = 1 , decimals = 1 ) )
   plt . fill_between ( oOOOooo0O , 0 , ii1iiII111IiI , color = '#FFFBEB' , alpha = .5 )
   plt . legend ( loc = 'upper left' )
   if 6 - 6: I1Ii1I1 . Ooo0Ooo % ooo000 * IIiIIiIi11I1
   plt . show ( )
  else :
   print ( 'No data' )
   if 4 - 4: Ooo0Ooo * IiIIii11Ii / I1Ii1I1 / ooOOO
 def Join ( self , report = False ) :
  self . gs . acquire ( )
  if self . _joinResult is None :
   self . lib . api_Join . restype = ctypes . c_char_p
   OoOoOo000o00O = self . lib . api_Join ( self . ctx )
   self . lib . api_Release ( self . ctx )
   self . _joinResult = OoOoOo000o00O
  self . gs . release ( )
  time . time = self . realTime
  if not report :
   return self . _joinResult
  import pandas as pd
  try :
   from pandas . plotting import register_matplotlib_converters
   register_matplotlib_converters ( )
  except :
   pass
  iIii1iiiIi = json . loads ( self . _joinResult )
  OOOOo = [ ]
  Oo00 = [ ]
  II1IiiIIi = None
  o0o00oO0OO0O = None
  OOooO0oo = 'stocks'
  for i1oO00oO00O0O in iIii1iiiIi [ 'Snapshots' ] :
   IiiIII1iI111i = i1oO00oO00O0O [ 1 ] [ 0 ]
   o0O0oooo0 = float ( 'nan' )
   o0o00oO0OO0O = IiiIII1iI111i [ 'Id' ]
   I1ii1IIiii = .0
   Oo00O00o0oO = .0
   ooooo0oo0 = .0
   for o0ooO0o in IiiIII1iI111i [ 'Assets' ] :
    if IiiIII1iI111i [ 'QuoteCurrency' ] == o0ooO0o [ 'Currency' ] :
     I1ii1IIiii += o0ooO0o [ 'Amount' ] + o0ooO0o [ 'FrozenAmount' ]
     ooooo0oo0 += o0ooO0o [ 'Commission' ]
    elif IiiIII1iI111i [ 'BaseCurrency' ] == o0ooO0o [ 'Currency' ] :
     Oo00O00o0oO += o0ooO0o [ 'Amount' ] + o0ooO0o [ 'FrozenAmount' ]
    else :
     oo = IiiIII1iI111i [ 'Symbols' ] . get ( o0ooO0o [ 'Currency' ] + '_' + IiiIII1iI111i [ 'QuoteCurrency' ] , None )
     if oo :
      I1ii1IIiii += ( o0ooO0o [ 'Amount' ] + o0ooO0o [ 'FrozenAmount' ] ) * oo [ 'Last' ]
      ooooo0oo0 += o0ooO0o [ 'Commission' ] * oo [ 'Last' ]
   iIiI11I1iI = IiiIII1iI111i [ 'Symbols' ]
   if o0o00oO0OO0O == 'Futures_CTP' or o0o00oO0OO0O == 'Futures_XTP' :
    OOooO0oo = 'balance'
    if iIiI11I1iI :
     for o0Ooo in iIiI11I1iI :
      ooOOOoOO0 = IiiIII1iI111i [ 'Symbols' ] [ o0Ooo ]
      for OOo in [ 'Long' , 'Short' ] :
       if OOo in ooOOOoOO0 :
        I1ii1IIiii += ooOOOoOO0 [ OOo ] [ 'Margin' ] + ooOOOoOO0 [ OOo ] [ 'Profit' ]
    OOOOo . append ( [ IiiIII1iI111i [ 'Balance' ] + IiiIII1iI111i [ 'FrozenBalance' ] , ooooo0oo0 , I1ii1IIiii ] )
   elif 'Futures_' in o0o00oO0OO0O :
    Oo0O = .0
    o0ooO0o = .0
    if iIiI11I1iI :
     for o0Ooo in iIiI11I1iI :
      ooOOOoOO0 = IiiIII1iI111i [ 'Symbols' ] [ o0Ooo ]
      for OOo in [ 'Long' , 'Short' ] :
       if OOo in ooOOOoOO0 :
        Oo0O += ooOOOoOO0 [ OOo ] [ 'Margin' ] + ooOOOoOO0 [ OOo ] [ 'Profit' ]
    if IiiIII1iI111i [ 'QuoteCurrency' ] == 'USDT' :
     OOooO0oo = 'USDT'
     o0ooO0o = I1ii1IIiii
    else :
     OOooO0oo = IiiIII1iI111i [ 'BaseCurrency' ]
     o0ooO0o = Oo00O00o0oO
    OOOOo . append ( [ o0ooO0o , ooooo0oo0 , o0ooO0o + Oo0O ] )
   else :
    if II1IiiIIi is None and iIiI11I1iI :
     for o0Ooo in IiiIII1iI111i [ 'Symbols' ] :
      II1IiiIIi = o0Ooo
      break
    if II1IiiIIi is not None :
     o0O0oooo0 = IiiIII1iI111i [ 'Symbols' ] [ II1IiiIIi ] [ 'Last' ]
    OOOOo . append ( [ o0O0oooo0 , I1ii1IIiii , Oo00O00o0oO , ooooo0oo0 , I1ii1IIiii + ( Oo00O00o0oO * o0O0oooo0 ) ] )
   Oo00 . append ( pd . Timestamp ( i1oO00oO00O0O [ 0 ] , unit = 'ms' , tz = 'Asia/Shanghai' ) )
  O000o0oOO00Ooo0o = [ "close" , "balance" , "stocks" , "fee" , "net" ]
  if 'Futures_' in o0o00oO0OO0O :
   O000o0oOO00Ooo0o = [ OOooO0oo , "fee" , "net" ]
  return pd . DataFrame ( OOOOo , index = Oo00 , columns = O000o0oOO00Ooo0o )
  if 90 - 90: iI1iI11Ii111 - I1Ii1I1 . i1iiIII111 % i1 % iI1iI11Ii111
class II1i ( ) :
 def __init__ ( self , task , session ) :
  self . session = session
  self . task = task
  self . gApis = { }
  self . tpls = task [ 'Code' ]
  del task [ 'Code' ]
  self . ctx = i111IIi ( task = self . task , gApis = self . gApis , progressCallback = self . progressCallback )
  if 31 - 31: I1Ii1I1 + i1i1i1111I * i1iiIII111
 def progressCallback ( self , st ) :
  if self . session is None :
   return
  self . session . sendall ( struct . pack ( '!II' , Iii11iiiiI ( st ) [ 'TaskStatus' ] , len ( st ) ) + st )
  if 58 - 58: ooOOO
 def waitStop ( self , ctx ) :
  if self . session is None :
   return
  try :
   iiIIi1iiII1Ii = b''
   OO0OoO00 = 0
   self . session . settimeout ( None )
   while True :
    if OO0OoO00 > 0 :
     if len ( iiIIi1iiII1Ii ) - 4 >= OO0OoO00 :
      if iiIIi1iiII1Ii [ 4 : 4 + OO0OoO00 ] == b'stop' :
       ctx . Join ( )
       self . session . close ( )
       os . _exit ( 2 )
      break
    elif len ( iiIIi1iiII1Ii ) >= 4 :
     OO0OoO00 , = struct . unpack ( '!I' , iiIIi1iiII1Ii [ : 4 ] )
     continue
    iiIIi1iiII1Ii += self . session . recv ( ( OO0OoO00 - ( len ( iiIIi1iiII1Ii ) - 4 ) ) if OO0OoO00 > 0 else 4 )
  except :
   pass
   if 98 - 98: I1Ii1I1 / i1i1i1111I - oOo0O00 . i1iiIII111 . Oo + i1i1i1111I
 def exit_handler ( self , signum , frame ) :
  signal . signal ( signal . SIGINT , signal . SIG_IGN )
  self . ctx . Join ( )
  self . session . shutdown ( socket . SHUT_RDWR )
  os . _exit ( 0 )
  if 44 - 44: I1Ii1I1 - i1i1i1111I
 def Run ( self ) :
  signal . signal ( signal . SIGINT , self . exit_handler )
  if self . session and platform . system ( ) == 'Windows' :
   OOo = threading . Thread ( target = self . waitStop , args = ( self . ctx , ) )
   OOo . setDaemon ( True )
   OOo . start ( )
  try :
   I1I1iI1i1Ii = False
   iiiI111 = len ( self . tpls )
   for ii in xrange ( 0 , iiiI111 ) :
    OoooO0 = self . tpls [ ii ]
    oO = copy . copy ( self . gApis )
    for II1 in OoooO0 [ 1 ] :
     oO [ II1 [ 0 ] ] = II1 [ 1 ]
    O0oOO0Oo00ooo = OoooO0 [ 0 ] + "\n\nif 'init' in locals() and callable(init):\n    init()\n"
    if ii == iiiI111 - 1 :
     O0oOO0Oo00ooo += "\nmain()\nif 'onexit' in globals():\n    onexit()"
    if not I1I1iI1i1Ii and 'matplotlib' in O0oOO0Oo00ooo :
     I1I1iI1i1Ii = True
     try :
      __import__ ( 'matplotlib' ) . use ( 'Agg' )
     except :
      pass
    exec ( O0oOO0Oo00ooo . replace ( '\r\n' , '\n' ) , oO )
  except ( EOFError , SystemExit ) :
   pass
  except :
   ooo , IIi , OO0Oo00Oo = sys . exc_info ( )
   OooO0Oo = [ x for x in traceback . extract_tb ( OO0Oo00Oo ) if x [ 0 ] == '<string>' ]
   if OooO0Oo :
    OoOoOOO = [ 'Traceback (most recent call last):\n' ]
    OoOoOOO = OoOoOOO + traceback . format_list ( OooO0Oo )
   else :
    OoOoOOO = [ ]
   OoOoOOO = OoOoOOO + traceback . format_exception_only ( ooo , IIi )
   self . ctx . g_LogError ( '' . join ( OoOoOOO ) )
  self . ctx . Join ( )
  self . session . shutdown ( socket . SHUT_RDWR )
  if 34 - 34: iI1iI11Ii111 + Ii
class i1IooO0O00O0o ( ) :
 def send ( self , * args ) :
  pass
 def sendall ( self , * args ) :
  pass
 def close ( self , * args ) :
  pass
 def shutdown ( self , * args ) :
  pass
  if 61 - 61: ooo000 . Ii * I11iiIi11i1I
if __name__ == '__main__' :
 uuid = os . getenv ( "BOTVS_TASK_UUID" )
 iiiiiiiIi = None
 if uuid == 'dummy' :
  iiiiiiiIi = iIi [ 's' ]
 else :
  iiiiiiiIi = i1IooO0O00O0o ( )
 if iiiiiiiIi is not None :
  II1i ( __cfg__ , iiiiiiiIi ) . Run ( )
  if 88 - 88: OooOoo / ooOOO % i1i1i1111I + i1i1i1111I
  if 50 - 50: oOO - ooOOO + iI1iII1I1I1i % i11 . iI1iI11Ii111
