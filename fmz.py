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
  return s . encode ( 'utf-8' )
 return str ( s )
 if 92 - 92: I1I / I1I + iI1iI11Ii111 . oOO
 if 8 - 8: Ii + iI1iI11Ii111 . I11iiIi11i1I - I1Ii1I1 % I11iiIi11i1I . i1i1i1111I
ii1iIi1i11i = 1 << 0
I111IIi11IiI = 1 << 1
o0OOOooO00oo = 1 << 2
IIii = 1 << 3
OO00 = 1 << 4
o0O0ooOoo00o = 1 << 5
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
   self . _logPtr ( name , OO0000 ( ',' . join ( map ( str , args ) ) ) )
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
 return OO0000 ( ' ' . join ( OooO0Oo ) )
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
 _fields_ = [ ( "Id" , ctypes . c_ulonglong ) ,
 ( "Price" , ctypes . c_double ) ,
 ( "Amount" , ctypes . c_double ) ,
 ( "DealAmount" , ctypes . c_double ) ,
 ( "AvgPrice" , ctypes . c_double ) ,
 ( "Type" , ctypes . c_uint ) ,
 ( "Offset" , ctypes . c_uint ) ,
 ( "Status" , ctypes . c_uint ) ,
 ( "ContractType" , ctypes . c_char * 31 ) ]
 if 67 - 67: IiIIii11Ii / oOo0O00 + Ooo0Ooo - i11 + Ii
class oo00OOO ( ooOoO0O0 ) :
 _fields_ = [ ( "Id" , ctypes . c_ulonglong ) ,
 ( "Time" , ctypes . c_ulonglong ) ,
 ( "Price" , ctypes . c_double ) ,
 ( "Amount" , ctypes . c_double ) ,
 ( "Type" , ctypes . c_uint ) ]
 if 93 - 93: OooOoo % i1i1i1111I + OooOoo % oOo0O00 + ooo000 * OooOoo
class II1Ii11111 ( ooOoO0O0 ) :
 _fields_ = [ ( "MarginLevel" , ctypes . c_double ) ,
 ( "Amount" , ctypes . c_double ) ,
 ( "FrozenAmount" , ctypes . c_double ) ,
 ( "Price" , ctypes . c_double ) ,
 ( "Profit" , ctypes . c_double ) ,
 ( "Margin" , ctypes . c_double ) ,
 ( "Type" , ctypes . c_uint ) ,
 ( "ContractType" , ctypes . c_char * 31 ) ]
def IIiIIiiIIi ( ) :
 raise EOFError ( )
 if 29 - 29: i1i1i1111I / oOo0O00
class iI1i1Iiii11i :
 routineId = 0
 def __init__ ( self , v ) :
  self . isWait = False
  self . v = v
  iI1i1Iiii11i . routineId += 1
  if 93 - 93: Ooo0Ooo . i1 + i11 - oOo0O00
 def wait ( self , timeout = 0 ) :
  if self . isWait :
   return ( None , False )
  self . isWait = True
  return ( self . v , True )
  if 97 - 97: i1 - i1 % IIiIIiIi11I1 + IiIIii11Ii / iI1iI11Ii111 * iI1iII1I1I1i
 def __repr__ ( self ) :
  return '<Go %d>' % iI1i1Iiii11i . routineId
  if 60 - 60: I11iiIi11i1I - Ooo0Ooo % I1Ii1I1
class ii1II1 :
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
  if 14 - 14: Oo % i1i1i1111I + ooOOO / I11iiIi11i1I - Ooo0Ooo / i1i1i1111I
 def Go ( self , method , * args ) :
  return iI1i1Iiii11i ( getattr ( self , method ) ( * args ) )
  if 29 - 29: Iii1i + Ii - I11iiIi11i1I - IiIIii11Ii
 def GetName ( self ) :
  return self . name
  if 31 - 31: IiIIii11Ii . Iii1i / Oo + i1iiIII111
 def GetLabel ( self ) :
  return self . label
  if 19 - 19: oOo0O00 . IIiIIiIi11I1
 def GetCurrency ( self ) :
  return self . currency
  if 90 - 90: IIiIIiIi11I1 * iI1iII1I1I1i
 def GetQuoteCurrency ( self ) :
  return self . quoteCurrency
  if 79 - 79: i1i1i1111I
 def GetUSDCNY ( self ) :
  self . lib . api_Exchange_GetUSDCNY . restype = ctypes . c_double
  return self . lib . api_Exchange_GetUSDCNY ( self . ctx , self . idx )
  if 3 - 3: OooOoo / i11 % I11iiIi11i1I
 def SetMaxBarLen ( self , n ) :
  self . maxBarLen = n
  if 55 - 55: oOo0O00
 def SetPrecision ( self , a , b ) :
  pass
  if 31 - 31: Ii . Ooo0Ooo / i11
 def GetRate ( self ) :
  self . lib . api_Exchange_GetRate . restype = ctypes . c_double
  return self . lib . api_Exchange_GetRate ( self . ctx , self . idx )
  if 59 - 59: Oo
 def SetProxy ( self , s ) :
  pass
  if 64 - 64: Iii1i % I11iiIi11i1I * i1 % OooOoo * oOo0O00
 def SetTimeout ( self , ms ) :
  pass
  if 55 - 55: i11
 def SetBase ( self , s ) :
  pass
  if 46 - 46: Ooo0Ooo % I1Ii1I1
 def SetCurrency ( self , s ) :
  OooO0Oo = s . split ( '_' )
  if len ( OooO0Oo ) == 2 :
   self . currency = s
   self . quoteCurrency = OooO0Oo [ 1 ]
   return self . lib . api_Exchange_SetCurrency ( self . ctx , self . idx , OO0000 ( s ) )
   if 86 - 86: I11iiIi11i1I . i1i1i1111I + oOO % I11iiIi11i1I % Iii1i % ooo000
 def SetRate ( self , rate = 1.0 ) :
  self . lib . api_Exchange_SetRate . restype = ctypes . c_double
  return self . lib . api_Exchange_SetRate ( self . ctx , self . idx , ctypes . c_double ( rate ) )
  if 61 - 61: ooo000
 def GetTrades ( self ) :
  OoOoOo000o00O = ctypes . c_uint ( 0 )
  i1I1i1I = ctypes . c_void_p ( )
  iIii1iiiIi = self . lib . api_Exchange_GetTrades ( self . ctx , self . idx , ctypes . byref ( OoOoOo000o00O ) , ctypes . byref ( i1I1i1I ) )
  if 90 - 90: I1Ii1I1 * i1i1i1111I / iI1iII1I1I1i * Ii
  if iIii1iiiIi == I11111i111 :
   iIiI1 = OoOoOo000o00O . value
   oo = [ ]
   if iIiI1 > 0 :
    I1I1II = ( oo00OOO * iIiI1 ) . from_address ( i1I1i1I . value )
    for ii in range ( 0 , iIiI1 ) :
     oo . append ( I1I1II [ ii ] . toObj ( ) )
    self . lib . api_free ( i1I1i1I )
   return oo
  elif iIii1iiiIi == oO0O :
   return None
  IIiIIiiIIi ( )
  if 5 - 5: oOo0O00 / Ii + i1iiIII111 * Oo + Ooo0Ooo + ooo000
 def SetData ( self , name , data ) :
  if not isinstance ( data , ii1Ii ) :
   data = json . dumps ( data )
  return self . lib . api_Exchange_SetData ( self . ctx , self . idx , OO0000 ( name ) , OO0000 ( data ) )
  if 96 - 96: i1iiIII111 - IIiIIiIi11I1 / IIiIIiIi11I1 * IiIIii11Ii
 def GetData ( self , name , timeout = 60000 , offset = 0 ) :
  oOoO0o0OOooO0 = Ii11 ( )
  iIii1iiiIi = self . lib . api_Exchange_GetData ( self . ctx , self . idx , ctypes . byref ( oOoO0o0OOooO0 ) , OO0000 ( name ) , int ( timeout ) , int ( offset ) )
  if iIii1iiiIi == I11111i111 :
   return IIIiII1I ( { 'Time' : oOoO0o0OOooO0 . Time , 'Data' : json . loads ( oOoO0o0OOooO0 . data [ : oOoO0o0OOooO0 . data_size ] ) if oOoO0o0OOooO0 . data_size > 0 else None } )
  elif iIii1iiiIi == oO0O :
   return None
  IIiIIiiIIi ( )
  if 38 - 38: i11 - Ooo0Ooo * I1Ii1I1
 def GetTicker ( self ) :
  oOoO0o0OOooO0 = Ii11 ( )
  iIii1iiiIi = self . lib . api_Exchange_GetTicker ( self . ctx , self . idx , ctypes . byref ( oOoO0o0OOooO0 ) )
  if iIii1iiiIi == I11111i111 :
   return oOoO0o0OOooO0 . toObj ( )
  elif iIii1iiiIi == oO0O :
   return None
  IIiIIiiIIi ( )
  if 89 - 89: iI1iII1I1I1i + IiIIii11Ii . Ooo0Ooo % ooOOO
 def IO ( self , k , v = 0 ) :
  if k == 'currency' :
   return self . SetCurrency ( v )
  return self . lib . api_Exchange_IO ( self . ctx , self . idx , OO0000 ( k ) , int ( v ) )
  if 82 - 82: i1i1i1111I
 def GetDepth ( self ) :
  O00ooo00Oo = ctypes . c_uint ( 0 )
  i1III = ctypes . c_uint ( 0 )
  i1I1i1I = ctypes . c_void_p ( )
  iIii1iiiIi = self . lib . api_Exchange_GetDepth ( self . ctx , self . idx , ctypes . byref ( O00ooo00Oo ) , ctypes . byref ( i1III ) , ctypes . byref ( i1I1i1I ) )
  if 73 - 73: i11
  if iIii1iiiIi == I11111i111 :
   iIiI1 = O00ooo00Oo . value + i1III . value
   IIIi1i1 = [ ]
   O0Oooo0 = [ ]
   if iIiI1 > 0 :
    I1I1II = ( OOoOoOO0OO0o * iIiI1 ) . from_address ( i1I1i1I . value )
    for ii in range ( 0 , iIiI1 ) :
     if ii < O00ooo00Oo . value :
      IIIi1i1 . append ( I1I1II [ ii ] . toObj ( ) )
     else :
      O0Oooo0 . append ( I1I1II [ ii ] . toObj ( ) )
    self . lib . api_free ( i1I1i1I )
   return IIIiII1I ( { 'Asks' : IIIi1i1 , 'Bids' : O0Oooo0 } )
  elif iIii1iiiIi == oO0O :
   return None
  IIiIIiiIIi ( )
  if 24 - 24: ooo000 % Oo % ooOOO + iI1iII1I1I1i
 def GetRecords ( self , period = - 1 ) :
  if period == - 1 :
   period = int ( self . period / 1000 )
  OoOoOo000o00O = ctypes . c_uint ( 0 )
  i1I1i1I = ctypes . c_void_p ( )
  iIii1iiiIi = self . lib . api_Exchange_GetRecords ( self . ctx , self . idx , ctypes . c_long ( int ( period ) ) , ctypes . byref ( OoOoOo000o00O ) , ctypes . byref ( i1I1i1I ) )
  if 28 - 28: IIiIIiIi11I1 + Oo / i1i1i1111I / I1Ii1I1 - iI1iII1I1I1i
  if iIii1iiiIi == I11111i111 :
   iIiI1 = OoOoOo000o00O . value
   oo = [ ]
   if iIiI1 > 0 :
    I1I1II = ( o0o0 * iIiI1 ) . from_address ( i1I1i1I . value )
    for ii in range ( 0 , iIiI1 ) :
     oo . append ( I1I1II [ ii ] . toObj ( ) )
    self . lib . api_free ( i1I1i1I )
   O0o00OO0oOOo = '%s/%s/%d' % ( self . currency , self . ct , period )
   ooO0ooOOO00O0 = self . records_cache . get ( O0o00OO0oOOo , None )
   if ooO0ooOOO00O0 is None or len ( ooO0ooOOO00O0 ) == 0 :
    if len ( oo ) > self . maxBarLen :
     oo = oo [ len ( oo ) - self . maxBarLen : ]
    self . records_cache [ O0o00OO0oOOo ] = oo
   else :
    II1i11IIi111 = 0 if len ( ooO0ooOOO00O0 ) == 0 else ooO0ooOOO00O0 [ - 1 ] [ 'Time' ]
    for IiiiiiIiI1 in oo :
     OOo = IiiiiiIiI1 [ 'Time' ]
     if OOo == II1i11IIi111 :
      ooO0ooOOO00O0 [ - 1 ] = IiiiiiIiI1
     elif OOo > II1i11IIi111 :
      ooO0ooOOO00O0 . append ( IiiiiiIiI1 )
      if len ( ooO0ooOOO00O0 ) > self . maxBarLen :
       ooO0ooOOO00O0 . pop ( 0 )
      II1i11IIi111 = OOo
   return I11 ( self . records_cache [ O0o00OO0oOOo ] )
  elif iIii1iiiIi == oO0O :
   return None
  IIiIIiiIIi ( )
  if 74 - 74: oOO - i11 / i1i1i1111I
 def GetAccount ( self ) :
  oOoO0o0OOooO0 = I111iI11i ( )
  iIii1iiiIi = self . lib . api_Exchange_GetAccount ( self . ctx , self . idx , ctypes . byref ( oOoO0o0OOooO0 ) )
  if iIii1iiiIi == I11111i111 :
   return oOoO0o0OOooO0 . toObj ( )
  elif iIii1iiiIi == oO0O :
   return None
  IIiIIiiIIi ( )
  if 9 - 9: IIiIIiIi11I1 - Ooo0Ooo % Ooo0Ooo
 def Buy ( self , price , amount = None , * extra ) :
  iIii1iiiIi = self . lib . api_Exchange_Trade ( self . ctx , self . idx , 0 , ctypes . c_double ( price ) , ctypes . c_double ( amount ) , i1iiiIii ( extra ) )
  if iIii1iiiIi > 0 :
   return int ( iIii1iiiIi )
  elif iIii1iiiIi == oO0O :
   return None
  IIiIIiiIIi ( )
  if 74 - 74: OooOoo
 def Sell ( self , price , amount = None , * extra ) :
  iIii1iiiIi = self . lib . api_Exchange_Trade ( self . ctx , self . idx , 1 , ctypes . c_double ( price ) , ctypes . c_double ( amount ) , i1iiiIii ( extra ) )
  if iIii1iiiIi > 0 :
   return int ( iIii1iiiIi )
  elif iIii1iiiIi == oO0O :
   return None
  IIiIIiiIIi ( )
  if 41 - 41: iI1iII1I1I1i . I11iiIi11i1I - OooOoo + iI1iI11Ii111 % OooOoo / Ooo0Ooo
 def GetOrders ( self ) :
  OoOoOo000o00O = ctypes . c_uint ( 0 )
  i1I1i1I = ctypes . c_void_p ( )
  iIii1iiiIi = self . lib . api_Exchange_GetOrders ( self . ctx , self . idx , ctypes . byref ( OoOoOo000o00O ) , ctypes . byref ( i1I1i1I ) )
  if 65 - 65: Oo
  if iIii1iiiIi == I11111i111 :
   iIiI1 = OoOoOo000o00O . value
   oo = [ ]
   if iIiI1 > 0 :
    I1I1II = ( i1II1 * iIiI1 ) . from_address ( i1I1i1I . value )
    for ii in range ( 0 , iIiI1 ) :
     oo . append ( I1I1II [ ii ] . toObj ( ) )
    self . lib . api_free ( i1I1i1I )
   return oo
  elif iIii1iiiIi == oO0O :
   return None
  IIiIIiiIIi ( )
  if 67 - 67: I1Ii1I1 + I1Ii1I1
 def Log ( self , orderType , price , amount = 0 , * extra ) :
  iIii1iiiIi = self . lib . api_Exchange_Log ( self . ctx , self . idx , ctypes . c_int ( orderType ) , ctypes . c_double ( price ) , ctypes . c_double ( amount ) , i1iiiIii ( extra ) )
  if orderType == 2 :
   return bool ( iIii1iiiIi )
  if iIii1iiiIi > 0 :
   return int ( iIii1iiiIi )
   if 42 - 42: IiIIii11Ii / oOo0O00 % ooOOO . oOO / OooOoo + oOo0O00
 def GetOrder ( self , orderId ) :
  oOoO0o0OOooO0 = i1II1 ( )
  iIii1iiiIi = self . lib . api_Exchange_GetOrder ( self . ctx , self . idx , ctypes . c_int ( orderId ) , ctypes . byref ( oOoO0o0OOooO0 ) )
  if iIii1iiiIi == I11111i111 :
   return oOoO0o0OOooO0 . toObj ( )
  elif iIii1iiiIi == oO0O :
   return None
  IIiIIiiIIi ( )
  if 79 - 79: I11iiIi11i1I . I1Ii1I1 * iI1iI11Ii111 % I1Ii1I1 / i11
 def CancelOrder ( self , orderId , * extra ) :
  self . lib . api_Exchange_CancelOrder . restype = ctypes . c_bool
  iIii1iiiIi = self . lib . api_Exchange_CancelOrder ( self . ctx , self . idx , ctypes . c_int ( orderId ) , i1iiiIii ( extra ) )
  if iIii1iiiIi == OoIi1 :
   IIiIIiiIIi ( )
  return iIii1iiiIi == I11111i111
  if 93 - 93: iI1iI11Ii111 + Iii1i . Ii . iI1iI11Ii111 * ooOOO
 def GetContractType ( self ) :
  return self . ct
  if 84 - 84: Ooo0Ooo % i11
 def GetPeriod ( self ) :
  return int ( self . period / 1000 )
  if 82 - 82: IIiIIiIi11I1
 def SetContractType ( self , symbol ) :
  oOoO0o0OOooO0 = ctypes . c_char_p ( )
  iIii1iiiIi = self . lib . api_Exchange_SetContractType ( self . ctx , self . idx , OO0000 ( symbol ) , ctypes . byref ( oOoO0o0OOooO0 ) )
  if iIii1iiiIi == I11111i111 :
   self . ct = symbol
   if oOoO0o0OOooO0 :
    Oo0OOOo0o = Iii11iiiiI ( oOoO0o0OOooO0 . value )
    self . lib . api_free ( oOoO0o0OOooO0 )
    return Oo0OOOo0o
   else :
    return True
  elif iIii1iiiIi == oO0O :
   return None
  IIiIIiiIIi ( )
  if 21 - 21: IIiIIiIi11I1 - I1I - i11 + OooOoo
 def SetMarginLevel ( self , level ) :
  self . lib . api_Exchange_SetMarginLevel . restype = ctypes . c_bool
  return self . lib . api_Exchange_SetMarginLevel ( self . ctx , self . idx , ctypes . c_int ( level ) )
  if 41 - 41: IiIIii11Ii + OooOoo - I11iiIi11i1I + Oo % i1 + iI1iII1I1I1i
 def SetDirection ( self , direction ) :
  self . lib . api_Exchange_SetMarginLevel . restype = ctypes . c_bool
  return self . lib . api_Exchange_SetDirection ( self . ctx , self . idx , OO0000 ( direction ) )
  if 16 - 16: i1 - Oo / Ii
 def GetPosition ( self ) :
  OoOoOo000o00O = ctypes . c_uint ( 0 )
  i1I1i1I = ctypes . c_void_p ( )
  iIii1iiiIi = self . lib . api_Exchange_GetPosition ( self . ctx , self . idx , ctypes . byref ( OoOoOo000o00O ) , ctypes . byref ( i1I1i1I ) )
  if 38 - 38: Ooo0Ooo % I1Ii1I1 / iI1iI11Ii111 + i1iiIII111
  if iIii1iiiIi == I11111i111 :
   iIiI1 = OoOoOo000o00O . value
   oo = [ ]
   if iIiI1 > 0 :
    I1I1II = ( II1Ii11111 * iIiI1 ) . from_address ( i1I1i1I . value )
    for ii in range ( 0 , iIiI1 ) :
     oo . append ( I1I1II [ ii ] . toObj ( ) )
    self . lib . api_free ( i1I1i1I )
   return oo
  elif iIii1iiiIi == oO0O :
   return None
  IIiIIiiIIi ( )
  if 25 - 25: I11iiIi11i1I - iI1iII1I1I1i
class OooO0Ooo0 ( object ) :
 def __init__ ( self , lib , ctx , js ) :
  self . lib = lib
  self . ctx = ctx
  self . lib . api_Chart_New ( self . ctx , OO0000 ( json . dumps ( js ) ) )
  if 46 - 46: Ii
 def update ( self , js ) :
  self . lib . api_Chart_New ( self . ctx , OO0000 ( json . dumps ( js ) ) )
  if 37 - 37: IIiIIiIi11I1 % oOO + Oo . Ooo0Ooo
 def add ( self , seriesIdx , d , replaceId = None ) :
  OoOoOo = [ seriesIdx , d ]
  if replaceId is not None :
   OoOoOo . append ( replaceId )
  self . lib . api_Chart_Add ( self . ctx , OO0000 ( json . dumps ( OoOoOo ) ) )
  if 18 - 18: IiIIii11Ii * IiIIii11Ii - Ii
 def reset ( self , keep = 0 ) :
  self . lib . api_Chart_Reset ( self . ctx , keep )
  if 52 - 52: iI1iI11Ii111
class IIiI1I1I11 ( ) :
 def __init__ ( self , lib , ctx , options = { } ) :
  options [ "__isCandle" ] = True
  self . chart = OooO0Ooo0 ( lib , ctx , options )
  self . bar = None
  self . overlay = options . get ( "overlay" , False )
  self . preTime = 0
  self . runtime = { "plots" : [ ] , "signals" : [ ] , "titles" : { } , "count" : 0 }
  if 79 - 79: OooOoo
 def trim ( self , obj ) :
  II1Iii1 = { }
  for O0o00OO0oOOo in obj :
   if obj [ O0o00OO0oOOo ] is not None :
    II1Iii1 [ O0o00OO0oOOo ] = obj [ O0o00OO0oOOo ]
  return II1Iii1
  if 66 - 66: Ii % Ii . i1iiIII111 / IIiIIiIi11I1
 def newPlot ( self , obj ) :
  o0oO0OoO00O = self . trim ( obj )
  if "overlay" not in o0oO0OoO00O :
   o0oO0OoO00O [ "overlay" ] = self . overlay
  if o0oO0OoO00O [ "type" ] != 'shape' and o0oO0OoO00O [ "type" ] != 'bgcolor' and o0oO0OoO00O [ "type" ] != 'barcolor' :
   if "title" not in o0oO0OoO00O or len ( o0oO0OoO00O [ "title" ] ) == 0 or o0oO0OoO00O [ "title" ] in self . runtime [ "titles" ] :
    o0oO0OoO00O [ "title" ] = '<' + o0oO0OoO00O . get ( "title" , "plot" ) + '_' + str ( self . runtime [ "count" ] ) + '>'
   self . runtime [ "count" ] += 1
   if "title" in o0oO0OoO00O :
    self . runtime [ "titles" ] [ o0oO0OoO00O [ "title" ] ] = True
  return o0oO0OoO00O
  if 76 - 76: I11iiIi11i1I % IIiIIiIi11I1 % iI1iI11Ii111
  if 39 - 39: IiIIii11Ii . Oo + iI1iI11Ii111 - oOo0O00
 def begin ( self , bar ) :
  self . bar = bar
  if 93 - 93: Iii1i * IIiIIiIi11I1 % iI1iI11Ii111 + i1 % Ii * iI1iI11Ii111
 def reset ( self , remain = 0 ) :
  self . chart . reset ( remain )
  self . preTime = 0
  if 62 - 62: i11 % ooo000
 def close ( self ) :
  if self . bar [ "Time" ] < self . preTime :
   return
   if 19 - 19: Ii / Oo % Iii1i / i1iiIII111 - OooOoo - Ooo0Ooo
  IiIi1Ii1111 = {
 "timestamp" : self . bar [ "Time" ] ,
 "open" : self . bar [ "Open" ] ,
 "high" : self . bar [ "High" ] ,
 "low" : self . bar [ "Low" ] ,
 "close" : self . bar [ "Close" ] ,
 "volume" : self . bar . get ( "Volume" , 0 ) ,
 }
  if 89 - 89: I11iiIi11i1I - i11
  for O0o00OO0oOOo in [ "plots" , "signals" ] :
   if len ( self . runtime [ O0o00OO0oOOo ] ) > 0 :
    if "runtime" not in IiIi1Ii1111 :
     IiIi1Ii1111 [ "runtime" ] = { }
    IiIi1Ii1111 [ "runtime" ] [ O0o00OO0oOOo ] = self . runtime [ O0o00OO0oOOo ]
    if 61 - 61: Ii * OooOoo * I1I % i1iiIII111 % IIiIIiIi11I1 * I11iiIi11i1I
  if self . preTime == self . bar [ "Time" ] :
   self . chart . add ( 0 , IiIi1Ii1111 , - 1 )
  else :
   self . chart . add ( 0 , IiIi1Ii1111 )
   if 49 - 49: iI1iII1I1I1i / i1iiIII111 % oOO
  self . preTime = self . bar [ "Time" ]
  self . runtime [ "plots" ] = [ ]
  self . runtime [ "signals" ] = [ ]
  self . runtime [ "titles" ] = { }
  self . runtime [ "count" ] = 0
  if 46 - 46: ooOOO * IIiIIiIi11I1 % i1 / oOO + i1 + oOo0O00
 def plot ( self , series = None , title = None , color = None , linewidth = 1 , style = "line" , trackprice = None , histbase = 0 , offset = 0 , join = False , editable = False , show_last = None , display = "all" , overlay = None ) :
  if series is None or self . bar [ "Time" ] < self . preTime :
   return
   if 99 - 99: I1I * IIiIIiIi11I1 * i1iiIII111
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
  if 62 - 62: ooOOO % Oo + iI1iI11Ii111
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
  if 87 - 87: ooo000 - OooOoo + Ii + i1i1i1111I + IiIIii11Ii
 def plotarrow ( self , series , title = None , colorup = "#00ff00" ,
 colordown = "#ff0000" ,
 offset = 0 ,
 minheight = 5 ,
 maxheight = 100 ,
 editable = False , show_last = None , display = "all" , overlay = None ) :
  if display != "all" or self . bar [ "Time" ] < self . preTime :
   return
   if 57 - 57: IIiIIiIi11I1 + I1I / ooOOO % ooOOO % Oo / i11
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
  if 95 - 95: i1 / I11iiIi11i1I . i1 / Oo . Ooo0Ooo
 def hline ( self , price , title = None , color = None , linestyle = "dashed" , linewidth = None , editable = False , display = "all" , overlay = None ) :
  if display != "all" or self . bar [ "Time" ] < self . preTime :
   return
   if 43 - 43: Oo - OooOoo * oOO . Ooo0Ooo / IIiIIiIi11I1 * IIiIIiIi11I1
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
  if 84 - 84: i1iiIII111 + oOo0O00
  if 83 - 83: i1i1i1111I
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
  if 84 - 84: oOO / Ii * Ooo0Ooo / Ii / ooo000
  if 64 - 64: oOo0O00 * Ii
 def plotchar ( self , series , title = None , char = None , location = "abovebar" , color = None , offset = None , text = None , textcolor = None , editable = None , size = "auto" , show_last = None , display = "all" , overlay = None ) :
  if ( location != "absolute" and series is None ) or ( location == "absolute" and series is None ) or char is None or self . bar [ "Time" ] < self . preTime :
   return
   if 2 - 2: i11 % i1iiIII111 . oOo0O00
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
  if 59 - 59: I11iiIi11i1I % OooOoo - iI1iII1I1I1i % I1I + i1iiIII111 . I1Ii1I1
  if 94 - 94: ooOOO * I1Ii1I1 * i1iiIII111 . oOo0O00
  if 73 - 73: I1Ii1I1 / ooo000 % I11iiIi11i1I - i1i1i1111I + Oo - I1Ii1I1
 def plotshape ( self , series , title = None , style = None , location = "abovebar" , color = None , offset = None , text = None , textcolor = None , editable = None , size = "auto" , show_last = None , display = "all" , overlay = None ) :
  if ( location != "absolute" and series is None ) or ( location == "absolute" and series is None ) or self . bar [ "Time" ] < self . preTime :
   return
   if 18 - 18: i1 + ooOOO . i1 - iI1iII1I1I1i
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
  if 97 - 97: oOo0O00 + iI1iI11Ii111 % Iii1i
 def plotcandle ( self , open , high , low , close , title = None , color = None , wickcolor = None , editable = None , show_last = None , bordercolor = None , display = "all" , overlay = None ) :
  if display != "all" or self . bar [ "Time" ] < self . preTime :
   return
   if 34 - 34: i1 + Oo . oOo0O00 - ooo000 / I11iiIi11i1I * oOo0O00
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
  if 89 - 89: oOo0O00
 def fill ( self , plot1 , plot2 , color = None , title = None , editable = None , show_last = None , fillgaps = None , display = "all" ) :
  if self . bar [ "Time" ] < self . preTime :
   return
  if plot1 >= 0 and plot2 >= 0 and plot1 < len ( self . runtime [ "plots" ] ) and plot2 < len ( self . runtime [ "plots" ] ) and display == "all" :
   II1Iii1 = self . runtime [ "plots" ] [ plot1 ]
   if "fill" not in II1Iii1 :
    II1Iii1 [ "fill" ] = [ ]
   II1Iii1 [ "fill" ] . append ( self . trim ( {
 "value" : self . runtime [ "plots" ] [ plot2 ] [ "series" ] ,
 "color" : color ,
 "showLast" : show_last
 } ) )
   if 48 - 48: i1 / IIiIIiIi11I1 / iI1iII1I1I1i / i11 * IiIIii11Ii
 def signal ( self , direction , price , qty , id = None ) :
  if self . bar [ "Time" ] < self . preTime :
   return
  O0oo00o0O0 = {
 "id" : id or direction ,
 "avgPrice" : price ,
 "qty" : qty
 }
  if direction == "buy" or direction == "long" :
   O0oo00o0O0 [ "direction" ] = "long"
  elif direction == "sell" or direction == "short" :
   O0oo00o0O0 [ "direction" ] = "short"
  elif direction == "closesell" or direction == "closeshort" :
   O0oo00o0O0 [ "direction" ] = "close"
   O0oo00o0O0 [ "closeDirection" ] = "short"
  elif direction == "closebuy" or direction == "closelong" :
   O0oo00o0O0 [ "direction" ] = "close"
   O0oo00o0O0 [ "closeDirection" ] = "long"
   if 91 - 91: iI1iI11Ii111 . Ii . oOO
  if O0oo00o0O0 [ "direction" ] or O0oo00o0O0 [ "closeDirection" ] :
   self . runtime [ "signals" ] . append ( O0oo00o0O0 )
   if 65 - 65: oOO % OooOoo
def IIi1i11Ii1 ( s , default ) :
 oo0OO0o0O = default
 if len ( s ) < 2 :
  return oo0OO0o0O
 oOo0o0oo = int ( s [ : - 1 ] )
 ooO0ooOOO00O0 = s [ - 1 ]
 if ooO0ooOOO00O0 == 'd' :
  oo0OO0o0O = oOo0o0oo * 60000 * 60 * 24
 elif ooO0ooOOO00O0 == 'm' :
  oo0OO0o0O = oOo0o0oo * 60000
 elif ooO0ooOOO00O0 == 'm' :
  oo0OO0o0O = oOo0o0oo * 60000
 return oo0OO0o0O
 if 55 - 55: i1i1i1111I * Ii % i1i1i1111I
def oOoo00 ( s ) :
 OOOOo000 = s
 Ii1 = { }
 for ooooOO000O0Oo in OOOOo000 . split ( '\n' ) :
  ooooOO000O0Oo = ooooOO000O0Oo . strip ( )
  if ':' not in ooooOO000O0Oo :
   continue
  OooO0Oo = ooooOO000O0Oo . split ( ':' , 1 )
  if len ( OooO0Oo ) == 2 :
   O0o00OO0oOOo = OooO0Oo [ 0 ] . strip ( )
   O0OOooO = OooO0Oo [ 1 ] . strip ( )
   Ii1 [ O0o00OO0oOOo ] = O0OOooO
 IiIi1ii = Ii1 . get ( 'pnl' , 'true' )
 oo0OO0o0O = IIi1i11Ii1 ( Ii1 . get ( 'period' , '1h' ) , 60000 * 60 )
 oooo0 = IIi1i11Ii1 ( Ii1 . get ( 'basePeriod' , '' ) , 0 )
 if 5 - 5: Ii % Ii / iI1iII1I1I1i - i1
 i1Ii = [ ]
 for OOo00 in json . loads ( Ii1 . get ( 'exchanges' , '[]' ) ) :
  OooO0Oo = OOo00 [ 'currency' ] . upper ( ) . split ( '_' )
  if len ( OooO0Oo ) == 1 :
   OooO0Oo . append ( 'CNY' if 'CTP' in OOo00 [ 'eid' ] else 'USD' )
  if oooo0 == 0 :
   oooo0 = 60000 * 60
   if oo0OO0o0O == 86400000 :
    oooo0 = 60000 * 60
   elif oo0OO0o0O == 3600000 :
    oooo0 = 60000 * 30
   elif oo0OO0o0O == 1800000 :
    oooo0 = 60000 * 15
   elif oo0OO0o0O == 900000 :
    oooo0 = 60000 * 5
   elif oo0OO0o0O == 300000 :
    oooo0 = 60000
  IIi111 = {
 'Huobi' : [ 150 , 200 ] ,
 'OKX' : [ 150 , 200 ] ,
 'Binance' : [ 150 , 200 ] ,
 'Futures_BitMEX' : [ 8 , 10 ] ,
 'Futures_OKX' : [ 30 , 30 ] ,
 'Futures_HuobiDM' : [ 30 , 30 ] ,
 'Futures_CTP' : [ 25 , 25 ] ,
 'Futures_XTP' : [ 30 , 130 ] ,
 }
  if 23 - 23: Ooo0Ooo * IIiIIiIi11I1 % IiIIii11Ii . ooo000 * i1iiIII111 % Ooo0Ooo
  oOo0Oo = OOo00 . get ( 'fee' )
  if oOo0Oo is None :
   oOo0Oo = IIi111 . get ( OOo00 [ 'eid' ] , [ 200 , 200 ] )
  else :
   oOo0Oo = [ int ( oOo0Oo [ 0 ] * 1000 ) , int ( oOo0Oo [ 1 ] * 1000 ) ]
   if 29 - 29: OooOoo * Ii - oOO
  O0oOoOoO0o = {
 "Balance" : OOo00 . get ( 'balance' , 10000.0 ) ,
 "BaseCurrency" : OooO0Oo [ 0 ] ,
 "BasePeriod" : oooo0 ,
 "BasePrecision" : 4 ,
 "DepthDeep" : 5 ,
 "DepthAmount" : 20 ,
 "FaultTolerant" : 0 ,
 "FeeDenominator" : 5 ,
 "FeeMaker" : oOo0Oo [ 0 ] ,
 "FeeTaker" : oOo0Oo [ 1 ] ,
 "FeeMin" : OOo00 . get ( 'feeMin' , 0 ) ,
 "Id" : OOo00 [ 'eid' ] ,
 "Label" : OOo00 [ 'eid' ] ,
 "PriceTick" : 1e-05 ,
 "QuoteCurrency" : OooO0Oo [ 1 ] ,
 "QuotePrecision" : 8 ,
 "SlipPoint" : 0 ,
 "Stocks" : OOo00 . get ( 'stocks' , 3.0 )
 }
  if OOo00 [ 'eid' ] == 'Futures_CTP' or OOo00 [ 'eid' ] == 'Futures_XTP' :
   O0oOoOoO0o [ 'BasePrecision' ] = 0
   O0oOoOoO0o [ 'QuotePrecision' ] = 1
   O0oOoOoO0o [ 'DepthDeep' ] = 1
   O0oOoOoO0o [ 'Stocks' ] = .0
  elif OOo00 [ 'eid' ] == 'Futures_OKX' or OOo00 [ 'eid' ] == 'Futures_HuobiDM' :
   O0oOoOoO0o [ 'BasePrecision' ] = 0
   O0oOoOoO0o [ 'QuotePrecision' ] = 5
  elif OOo00 [ 'eid' ] == 'Bitfinex' or OOo00 [ 'eid' ] == 'Binance' :
   O0oOoOoO0o [ 'BasePrecision' ] = 4
   O0oOoOoO0o [ 'QuotePrecision' ] = 4
   O0oOoOoO0o [ 'PriceTick' ] = 0.001
  elif OOo00 [ 'eid' ] == 'Futures_BitMEX' :
   O0oOoOoO0o [ 'PriceTick' ] = 0.5
   O00 = O0oOoOoO0o [ 'BasePeriod' ] / 60000
   if O00 == 15 or O00 == 30 :
    O0oOoOoO0o [ 'BasePeriod' ] = 300000
  elif 'Futures' not in OOo00 [ 'eid' ] :
   O0oOoOoO0o [ 'BasePrecision' ] = 4
   O0oOoOoO0o [ 'QuotePrecision' ] = 8
   O0oOoOoO0o [ 'PriceTick' ] = 0.00000001
  i1Ii . append ( O0oOoOoO0o )
  if 25 - 25: ooOOO
 oo0IIIii = {
 "DataServer" : i1ii1 ,
 "MaxChartLogs" : 800 ,
 "MaxProfitLogs" : 800 ,
 "MaxRuntimeLogs" : 800 ,
 "NetDelay" : 200 ,
 "Period" : oo0OO0o0O ,
 "RetFlags" : ii1iIi1i11i | o0OOOooO00oo | iIIiiIi1Ii1I | IIii | o0O0ooOoo00o | OO00 ,
 "TimeBegin" : int ( time . mktime ( datetime . datetime . strptime ( Ii1 . get ( 'start' , '2019-02-01 00:00:00' ) , "%Y-%m-%d %H:%M:%S" ) . timetuple ( ) ) ) ,
 "TimeEnd" : int ( time . mktime ( datetime . datetime . strptime ( Ii1 . get ( 'end' , '2019-02-10 00:00:00' ) , "%Y-%m-%d %H:%M:%S" ) . timetuple ( ) ) ) ,
 "UpdatePeriod" : 5000
 }
 iIi111iIi1III = 86400
 OOO0OO = oo0IIIii [ 'TimeEnd' ] - oo0IIIii [ 'TimeBegin' ]
 if OOO0OO / 3600 <= 2 :
  iIi111iIi1III = 60
 elif OOO0OO / 86400 <= 2 :
  iIi111iIi1III = 300
 elif OOO0OO / 86400 < 30 :
  iIi111iIi1III = 3600
 oo0IIIii [ 'SnapshotPeriod' ] = iIi111iIi1III * 1000
 if IiIi1ii == 'true' :
  oo0IIIii [ 'RetFlags' ] |= oo0
 return { 'Exchanges' : i1Ii , 'Options' : oo0IIIii }
 if 13 - 13: i1iiIII111 - IiIIii11Ii / Ooo0Ooo + iI1iI11Ii111 . OooOoo / Iii1i
class OooOoO ( ) :
 pass
 if 73 - 73: oOO - i1iiIII111
class O00OOo0Ooo00O ( object ) :
 def __init__ ( self , task = None , autoRun = False , gApis = None , progressCallback = None ) :
  self . _joinResult = None
  self . gs = threading . Lock ( )
  if gApis is None :
   if __name__ == "__main__" :
    gApis = globals ( )
   else :
    gApis = dict ( inspect . getmembers ( inspect . stack ( ) [ 1 ] [ 0 ] ) ) [ "f_globals" ]
    if 24 - 24: Ii * Ii % Ii . Ooo0Ooo . OooOoo
  if task is None :
   task = oOoo00 ( gApis [ '__doc__' ] )
  elif hasattr ( task , 'upper' ) :
   task = oOoo00 ( task )
   if 81 - 81: OooOoo . Iii1i
  if progressCallback is not None :
   self . progressCallback = progressCallback
   if 28 - 28: IiIIii11Ii - i11 . i11 * IIiIIiIi11I1 - Iii1i
  self . httpGetPtr = ctypes . CFUNCTYPE ( ctypes . c_int , ctypes . c_char_p , ctypes . POINTER ( ctypes . c_char_p ) , ctypes . POINTER ( ctypes . c_int ) , ctypes . POINTER ( ctypes . c_int ) ) ( self . httpGetCallback )
  self . progessCallbackPtr = ctypes . CFUNCTYPE ( None , ctypes . c_char_p ) ( self . progressCallback )
  IiO0 = platform . system ( )
  oo0i11II = platform . architecture ( ) [ 0 ]
  if platform . processor ( ) == "arm" :
   oo0i11II = 'arm64' if oo0i11II == '64bit' else 'arm'
  self . os = '%s/%s' % ( IiO0 . lower ( ) , oo0i11II )
  OOOooO0o00ooOOO0 = 'backtest_py_%s_%s.so' % ( IiO0 . lower ( ) , oo0i11II )
  oo0ooOO0O0o0 = os . path . join ( "./depends" , OOOooO0o00ooOOO0 )
  if not os . path . exists ( oo0ooOO0O0o0 ) :
   i11II = { }
   oooOo = oo0o0oO ( )
   iI111iiIii1i = os . path . join ( oooOo , 'md5.json' )
   if os . path . exists ( iI111iiIii1i ) :
    oo0o0O = open ( iI111iiIii1i , 'rb' ) . read ( )
    if os . getenv ( "BOTVS_TASK_UUID" ) is None or "4e58e517912cedacfe69e9428d6625e1" in str ( oo0o0O ) :
     i11II = Iii11iiiiI ( oo0o0O )
   oo0ooOO0O0o0 = os . path . join ( oooOo , OOOooO0o00ooOOO0 )
   Oo00o00OooOoo = False
   if not os . path . exists ( oo0ooOO0O0o0 ) :
    Oo00o00OooOoo = True
   else :
    Oo0OOOo = md5 . md5 ( open ( oo0ooOO0O0o0 , 'rb' ) . read ( ) ) . hexdigest ( )
    if Oo0OOOo != i11II . get ( OOOooO0o00ooOOO0 , None ) :
     Oo00o00OooOoo = True
     Oo000Oo0 = os . path . join ( oooOo , Oo0OOOo )
     try :
      os . rename ( oo0ooOO0O0o0 , Oo000Oo0 )
      os . remove ( Oo000Oo0 )
     except :
      pass
   if Oo00o00OooOoo :
    open ( oo0ooOO0O0o0 , 'wb' ) . write ( iIIiii1iI ( task [ "Options" ] [ "DataServer" ] + "/dist/depends/" + OOOooO0o00ooOOO0 ) )
    open ( iI111iiIii1i , 'wb' ) . write ( iIIiii1iI ( task [ "Options" ] [ "DataServer" ] + "/dist/depends/md5.json" ) )
    if 38 - 38: i1i1i1111I * i1i1i1111I
  o00o0OOO = ctypes . CDLL ( os . path . abspath ( oo0ooOO0O0o0 ) )
  o00o0OOO . api_backtest . restype = ctypes . c_void_p
  iI = ctypes . c_void_p ( o00o0OOO . api_backtest ( OO0000 ( json . dumps ( task ) ) , self . httpGetPtr , self . progessCallbackPtr ) )
  if not iI :
   raise 'Initialize backtest engine error'
  self . ctx = iI
  self . lib = o00o0OOO
  self . cache = { }
  self . kvdb = { }
  self . cRetryDelay = 3000
  if 57 - 57: Oo + i1i1i1111I / I1Ii1I1
  i1Ii = [ ]
  ii = 0
  for IiiiiiIiI1 in task [ "Exchanges" ] :
   i1Ii . append ( ii1II1 ( o00o0OOO , iI , ii , task [ "Options" ] , IiiiiiIiI1 ) )
   ii += 1
   if 56 - 56: oOO % Ooo0Ooo % Iii1i . i1i1i1111I
  for O0o00OO0oOOo in dir ( self ) :
   if O0o00OO0oOOo . startswith ( 'g_' ) :
    gApis [ O0o00OO0oOOo [ 2 : ] ] = getattr ( self , O0o00OO0oOOo )
    if 46 - 46: i11 . i1iiIII111 % Iii1i - Ooo0Ooo + ooo000
  self . realTime = time . time
  time . time = self . g_PyTime
  gApis [ '__name__' ] = '__main__'
  gApis [ "TA" ] = oOoOO0O0 ( self . _logTA )
  gApis [ 'exchanges' ] = i1Ii
  gApis [ 'exchange' ] = i1Ii [ 0 ]
  gApis [ 'ext' ] = OooOoO ( )
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
  if 100 - 100: oOO
  gApis [ "PD_LONG" ] = 0
  gApis [ "PD_SHORT" ] = 1
  gApis [ "PD_LONG_YD" ] = 2
  gApis [ "PD_SHORT_YD" ] = 3
  if 32 - 32: I1Ii1I1 % ooo000 * OooOoo / oOo0O00 + ooOOO
  gApis [ "LOG_TYPE_BUY" ] = 0
  gApis [ "LOG_TYPE_SELL" ] = 1
  gApis [ "LOG_TYPE_CANCEL" ] = 2
  gApis [ "LOG_TYPE_ERROR" ] = 3
  gApis [ "LOG_TYPE_PROFIT" ] = 4
  gApis [ "LOG_TYPE_LOG" ] = 5
  gApis [ "LOG_TYPE_RESTART" ] = 6
  if 64 - 64: I1Ii1I1 . Ooo0Ooo
  gApis [ "PERIOD_M1" ] = 60 * 1
  gApis [ "PERIOD_M3" ] = 60 * 3
  gApis [ "PERIOD_M5" ] = 60 * 5
  gApis [ "PERIOD_M15" ] = 60 * 15
  gApis [ "PERIOD_M30" ] = 60 * 30
  gApis [ "PERIOD_H1" ] = 60 * 60
  gApis [ "PERIOD_D1" ] = 60 * 60 * 24
  gApis [ "PERIOD_W1" ] = 60 * 60 * 24 * 7
  if autoRun :
   try :
    gApis [ 'main' ] ( )
   except EOFError :
    pass
   self . Join ( )
   if 36 - 36: IIiIIiIi11I1 + IiIIii11Ii . i1 + IIiIIiIi11I1
 def update ( self ) :
  try :
   os . remove ( os . path . join ( oo0o0oO ( ) , 'md5.json' ) )
  except :
   pass
   if 77 - 77: iI1iII1I1I1i / OooOoo . Iii1i + i1iiIII111 - i11
 def httpGetCallback ( self , path , ptr_buf , ptr_size , ptr_need_free ) :
  OOO00oOO0 = path . decode ( 'utf8' )
  oooOo = oo0o0oO ( )
  IiIII11 = oooOo + '/botvs_kline_' + md5 . md5 ( path ) . hexdigest ( )
  IiIi1Ii1111 = None
  try :
   if os . path . exists ( IiIII11 ) :
    IiIi1Ii1111 = open ( IiIII11 , 'rb' ) . read ( )
    IiIII11 = None
   else :
    IiIi1Ii1111 = iIIiii1iI ( OOO00oOO0 )
    if len ( IiIi1Ii1111 ) > 0 :
     open ( IiIII11 , 'wb' ) . write ( IiIi1Ii1111 )
  except :
   pass
  if IiIi1Ii1111 is None :
   return 1
  ptr_size . contents . value = len ( IiIi1Ii1111 )
  ptr_need_free . contents . value = 0
  oOOOOo0 = ctypes . create_string_buffer ( IiIi1Ii1111 )
  ptr_buf . contents . value = ctypes . addressof ( oOOOOo0 )
  self . cache [ IiIII11 ] = oOOOOo0
  return 0
  if 26 - 26: I1Ii1I1 % oOO * iI1iII1I1I1i . I1I * iI1iII1I1I1i
 def progressCallback ( self , st ) :
  pass
  if 38 - 38: Ooo0Ooo . IIiIIiIi11I1 * oOo0O00 / ooOOO / OooOoo * Ooo0Ooo
 def _logTA ( self , name , args ) :
  self . lib . api_LogTA ( self . ctx , name , args )
  if 49 - 49: iI1iII1I1I1i
 def g_Unix ( self ) :
  self . lib . api_Unix . restype = ctypes . c_ulonglong
  return self . lib . api_Unix ( self . ctx )
  if 77 - 77: ooo000 % I11iiIi11i1I % Ooo0Ooo * oOO
 def g_UnixNano ( self ) :
  self . lib . api_UnixNano . restype = ctypes . c_ulonglong
  return self . lib . api_UnixNano ( self . ctx )
  if 5 - 5: oOO * i1i1i1111I % Oo
 def g_PyTime ( self ) :
  return float ( self . g_UnixNano ( ) ) / 1e9
  if 99 - 99: IiIIii11Ii * I1Ii1I1
 def g_Sleep ( self , n ) :
  if self . lib . api_Sleep ( self . ctx , ctypes . c_double ( n ) ) != 0 :
   IIiIIiiIIi ( )
   if 83 - 83: iI1iI11Ii111 . ooo000 * Ooo0Ooo + Iii1i . Oo
 def g_EnableLog ( self , flag = True ) :
  self . lib . api_EnableLog ( self . ctx , ctypes . c_bool ( flag ) )
  if 34 - 34: I11iiIi11i1I % oOO
 def g_Log ( self , * extra ) :
  self . lib . api_Log ( self . ctx , i1iiiIii ( extra ) )
  if 75 - 75: i1 % IiIIii11Ii - iI1iII1I1I1i - iI1iI11Ii111 * I11iiIi11i1I * OooOoo
 def g_LogReset ( self , keep = 0 ) :
  self . lib . api_LogReset ( self . ctx , ctypes . c_int ( keep ) )
  if 45 - 45: IIiIIiIi11I1
 def g_LogVacuum ( self ) :
  pass
  if 14 - 14: i1i1i1111I - OooOoo . IiIIii11Ii
 def g_LogStatus ( self , * extra ) :
  self . lib . api_LogStatus ( self . ctx , i1iiiIii ( extra ) )
  if 40 - 40: I1I - IIiIIiIi11I1 % IiIIii11Ii
 def g_LogProfit ( self , profit , * extra ) :
  self . lib . api_LogProfit ( self . ctx , ctypes . c_double ( profit ) , i1iiiIii ( extra ) )
  if 61 - 61: iI1iII1I1I1i
 def g_LogProfitReset ( self , keep = 0 ) :
  self . lib . api_LogProfitReset ( self . ctx , ctypes . c_int ( keep ) )
  if 93 - 93: i1iiIII111 - oOo0O00 . Oo . i1iiIII111 . Oo * I1Ii1I1
 def g_LogError ( self , * extra ) :
  self . lib . api_LogError ( self . ctx , i1iiiIii ( extra ) )
  if 95 - 95: I1Ii1I1 % oOO
 def g_Panic ( self , * extra ) :
  self . lib . api_LogError ( self . ctx , i1iiiIii ( extra ) )
  IIiIIiiIIi ( )
  if 21 - 21: Ooo0Ooo % i1 - ooo000
 def g_GetLastError ( self ) :
  return ''
  if 81 - 81: Ooo0Ooo / ooo000
 def g_MD5 ( self , s ) :
  return md5 . md5 ( OO0000 ( s ) ) . hexdigest ( )
  if 4 - 4: I1I % iI1iI11Ii111 - ooo000 - I1I . ooOOO / i1i1i1111I
 def g_HttpQuery ( self , * args ) :
  return 'dummy'
  if 74 - 74: oOO
 def g_StrDecode ( self , s , c = 'gbk' ) :
  self . g_LogError ( "sandbox not support StrDecode" )
  if 24 - 24: I1I + Oo - ooOOO
 def g_EnableLogLocal ( self , b ) :
  pass
  if 86 - 86: i1iiIII111 % ooo000 % ooo000 % iI1iI11Ii111
 def g_Dial ( self , * args ) :
  self . g_LogError ( "sandbox not support Dial" )
  if 15 - 15: iI1iII1I1I1i + I1Ii1I1 % oOo0O00
 def g_Mail ( self , * args ) :
  return True
  if 79 - 79: OooOoo . Oo + oOo0O00 / I1Ii1I1 . IiIIii11Ii
 def g_GetCommand ( self ) :
  return ''
  if 89 - 89: ooo000 % Ooo0Ooo
 def g_GetMeta ( self ) :
  return None
  if 77 - 77: ooo000 % Ooo0Ooo
 def g_SetErrorFilter ( self , s ) :
  pass
  if 24 - 24: oOO * I1Ii1I1 * I1Ii1I1 % IIiIIiIi11I1
 def g_GetOS ( self ) :
  return self . os
  if 37 - 37: i1iiIII111 / iI1iII1I1I1i
 def g_Version ( self ) :
  return '3.3'
  if 80 - 80: IiIIii11Ii
 def g_IsVirtual ( self ) :
  return True
  if 2 - 2: I1I / oOO - IIiIIiIi11I1 % Ooo0Ooo
 def g_Chart ( self , js ) :
  return OooO0Ooo0 ( self . lib , self . ctx , js )
  if 88 - 88: iI1iII1I1I1i - I1Ii1I1 - iI1iI11Ii111 . Iii1i
 def g_KLineChart ( self , js = { } ) :
  return IIiI1I1I11 ( self . lib , self . ctx , js )
  if 98 - 98: Ii + ooOOO
 def g_GetPid ( self ) :
  return os . getpid ( )
  if 29 - 29: I1Ii1I1 + iI1iI11Ii111 - IIiIIiIi11I1 * I11iiIi11i1I % Oo
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
  if 74 - 74: ooOOO
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
    if 100 - 100: oOO + iI1iII1I1I1i . I1I % Oo - i1
 def g__CDelay ( self , d ) :
  if d > 0 :
   self . cRetryDelay = d
   if 39 - 39: iI1iII1I1I1i
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
  if 34 - 34: iI1iII1I1I1i . i1 . I1I
 def g__T ( self , a , b = None ) :
  oOoO0o0OOooO0 = str ( a )
  if b is not None :
   oOoO0o0OOooO0 = str ( a ) + '|' + str ( b )
  return '[trans]' + oOoO0o0OOooO0 + '[/trans]'
  if 95 - 95: IiIIii11Ii * i11 * Ooo0Ooo * i11 / OooOoo
 def g__N ( self , n , precision = 4 ) :
  OoOOo0OoOOO0 = pow ( 10 , precision )
  return int ( n * OoOOo0OoOOO0 ) / float ( OoOOo0OoOOO0 )
  if 27 - 27: iI1iI11Ii111 . IiIIii11Ii
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
   if 69 - 69: oOO % i1iiIII111 / oOo0O00
   if 38 - 38: I11iiIi11i1I + Oo * Ooo0Ooo / ooOOO . OooOoo
  def i1IiO00O ( self ) :
   try :
    IiIi1Ii1111 = json . loads ( self . Join ( ) . decode ( 'utf-8' ) )
   except :
    return
   Ii1 = { }
   Ii1 [ 'timeStamp' ] = [ ]
   Ii1 [ 'assets' ] = [ ]
   Ii1 [ 'surplus' ] = [ ]
   Ii1 [ 'loss' ] = [ ]
   Ii1 [ 'moneyUse' ] = [ ]
   Ii1 [ 'unit' ] = ''
   Oo0oO00O0 = 0
   for ii in IiIi1Ii1111 [ 'Snapshots' ] :
    if not ii [ 1 ] :
     continue
    OO0o0o0O0 = 0
    oOoOoOOOOO = 0
    for ooOOOoOO0 in range ( 0 , len ( ii [ 1 ] ) ) :
     oo000O0oOO = ii [ 1 ] [ ooOOOoOO0 ]
     I1iii1I = IiIi1Ii1111 [ 'Task' ] [ 'Exchanges' ] [ ooOOOoOO0 ]
     iIIi = oo000O0oOO [ 'Symbols' ]
     if iIIi :
      oo0OoOo0OOoO0 = 0
      i1I11iI1 = 0
      iio0o0 = 0
      o0o0oOooOo = 0
      for iIIiIi1 in iIIi :
       if 'Long' in iIIi [ iIIiIi1 ] :
        i1i11iII1i = iIIi [ iIIiIi1 ] [ 'Long' ]
        oo0OoOo0OOoO0 += i1i11iII1i [ 'Margin' ]
        i1I11iI1 += i1i11iII1i [ 'Profit' ]
       if 'Short' in iIIi [ iIIiIi1 ] :
        I1Iiiiii11I = iIIi [ iIIiIi1 ] [ 'Short' ]
        oo0OoOo0OOoO0 += I1Iiiiii11I [ 'Margin' ]
        i1I11iI1 += I1Iiiiii11I [ 'Profit' ]
       if 'Stocks' in iIIi [ iIIiIi1 ] :
        iio0o0 += ( iIIi [ iIIiIi1 ] [ 'Stocks' ] + iIIi [ iIIiIi1 ] [ 'FrozenStocks' ] ) * iIIi [ iIIiIi1 ] [ 'Last' ]
        o0o0oOooOo += ( iIIi [ iIIiIi1 ] [ 'Stocks' ] + iIIi [ iIIiIi1 ] [ 'FrozenStocks' ] - I1iii1I [ 'Stocks' ] ) * iIIi [ iIIiIi1 ] [ 'Last' ]
        if 45 - 45: OooOoo + ooOOO / i1i1i1111I * i1
      if oo000O0oOO [ 'QuoteCurrency' ] == 'CNY' :
       OO0o0o0O0 += oo000O0oOO [ 'Balance' ] + oo000O0oOO [ 'FrozenBalance' ] + i1I11iI1 + oo0OoOo0OOoO0
       oOoOoOOOOO += oo0OoOo0OOoO0 / OO0o0o0O0
       Ii1 [ 'unit' ] = '(CNY)'
      elif 'Futures_' in oo000O0oOO [ 'Id' ] :
       if oo000O0oOO [ 'QuoteCurrency' ] == 'USDT' :
        OO0o0o0O0 += oo000O0oOO [ 'Balance' ] + oo000O0oOO [ 'FrozenBalance' ] + i1I11iI1 + oo0OoOo0OOoO0
        oOoOoOOOOO += oo0OoOo0OOoO0 / OO0o0o0O0
        Ii1 [ 'unit' ] = '(USDT)'
       else :
        OO0o0o0O0 += oo000O0oOO [ 'Stocks' ] + oo000O0oOO [ 'FrozenStocks' ] + i1I11iI1 + oo0OoOo0OOoO0
        oOoOoOOOOO += oo0OoOo0OOoO0 / OO0o0o0O0
        Ii1 [ 'unit' ] = '(%s)' % ( oo000O0oOO [ "BaseCurrency" ] , )
      else :
       OO0o0o0O0 += oo000O0oOO [ 'Balance' ] + oo000O0oOO [ 'FrozenBalance' ] + iio0o0
       oOoOoOOOOO += abs ( o0o0oOooOo ) / OO0o0o0O0
       Ii1 [ 'unit' ] = '(USD)'
    Ii1 [ 'timeStamp' ] . append ( datetime . datetime . fromtimestamp ( ii [ 0 ] / 1000 ) . date ( ) )
    Ii1 [ 'assets' ] . append ( OO0o0o0O0 )
    Ii1 [ 'moneyUse' ] . append ( oOoOoOOOOO )
    if Oo0oO00O0 != 0 :
     oOo000o0OO0o = OO0o0o0O0 - Oo0oO00O0
     if oOo000o0OO0o > 0 :
      Ii1 [ 'surplus' ] . append ( oOo000o0OO0o )
      Ii1 [ 'loss' ] . append ( 0 )
     elif oOo000o0OO0o < 0 :
      Ii1 [ 'surplus' ] . append ( 0 )
      Ii1 [ 'loss' ] . append ( oOo000o0OO0o )
     else :
      Ii1 [ 'surplus' ] . append ( 0 )
      Ii1 [ 'loss' ] . append ( 0 )
    else :
     Ii1 [ 'surplus' ] . append ( 0 )
     Ii1 [ 'loss' ] . append ( 0 )
    Oo0oO00O0 = OO0o0o0O0
   return Ii1
   if 31 - 31: Oo - IIiIIiIi11I1 / i11 * i1i1i1111I
   if 68 - 68: IiIIii11Ii
  plt . rcParams [ 'axes.unicode_minus' ] = False
  if 41 - 41: iI1iI11Ii111 - Ooo0Ooo
  if 47 - 47: I1Ii1I1 * i1i1i1111I - iI1iI11Ii111 . Iii1i . ooOOO
  IiIi1Ii1111 = i1IiO00O ( self )
  if IiIi1Ii1111 :
   iIO0Oo0000 = IiIi1Ii1111 [ 'timeStamp' ]
   OO0o0o0O0 = IiIi1Ii1111 [ 'assets' ]
   IIi = IiIi1Ii1111 [ 'surplus' ]
   iII11111iI = IiIi1Ii1111 [ 'loss' ]
   oOoOoOOOOO = IiIi1Ii1111 [ 'moneyUse' ]
   ooII1 = IiIi1Ii1111 [ 'unit' ]
   if 78 - 78: oOo0O00
   plt . figure ( figsize = ( 14 , 8 ) )
   plt . subplots_adjust ( left = 0.090 , right = 0.930 )
   plt . subplots_adjust ( hspace = 0 , wspace = 0 )
   i1iII1 = plt . subplot ( 311 )
   plt . title ( u'Backtest' , fontsize = 18 )
   plt . grid ( linestyle = '--' , color = '#D9D9D9' )
   plt . plot ( iIO0Oo0000 , OO0o0o0O0 , color = '#3A859E' , label = u'Equity %s %f' % ( ooII1 , OO0o0o0O0 [ - 1 ] ) )
   plt . fill_between ( iIO0Oo0000 , min ( OO0o0o0O0 ) , OO0o0o0O0 , color = '#D0DBE8' , alpha = .5 )
   plt . legend ( loc = 'upper left' )
   i1iII1 = plt . subplot ( 312 )
   plt . grid ( linestyle = '--' , color = '#D9D9D9' )
   plt . bar ( iIO0Oo0000 , IIi , color = 'r' )
   plt . bar ( iIO0Oo0000 , iII11111iI , color = 'g' )
   plt . legend ( loc = 'upper left' , labels = [ u'Win' + ooII1 , u'Loss' + ooII1 ] )
   if 67 - 67: I1Ii1I1 + OooOoo + ooOOO * Oo * i1iiIII111 . Ooo0Ooo
   i1iII1 = plt . subplot ( 313 )
   plt . grid ( linestyle = '--' , color = '#D9D9D9' )
   plt . plot ( iIO0Oo0000 , oOoOoOOOOO , color = '#EBB000' , label = 'Utilization' )
   i1iII1 . yaxis . set_major_formatter ( ticker . PercentFormatter ( xmax = 1 , decimals = 1 ) )
   plt . fill_between ( iIO0Oo0000 , 0 , oOoOoOOOOO , color = '#FFFBEB' , alpha = .5 )
   plt . legend ( loc = 'upper left' )
   if 35 - 35: ooOOO . iI1iI11Ii111 * i1i1i1111I * iI1iII1I1I1i - I11iiIi11i1I
   plt . show ( )
  else :
   print ( 'No data' )
   if 47 - 47: IIiIIiIi11I1
 def Join ( self , report = False ) :
  self . gs . acquire ( )
  if self . _joinResult is None :
   self . lib . api_Join . restype = ctypes . c_char_p
   oOoO0o0OOooO0 = self . lib . api_Join ( self . ctx )
   self . lib . api_Release ( self . ctx )
   self . _joinResult = oOoO0o0OOooO0
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
  IiIi1ii = [ ]
  IIi1 = [ ]
  i1iiiiiIIIiii = None
  ooO0OOo = None
  o0ooo0oOoO = 'stocks'
  for IiiiiiIiI1 in iIii1iiiIi [ 'Snapshots' ] :
   I1iii1I = IiiiiiIiI1 [ 1 ] [ 0 ]
   Oo0OoOo = float ( 'nan' )
   ooO0OOo = I1iii1I [ 'Id' ]
   O0oOO0Oo00ooo = I1iii1I [ 'Balance' ] + I1iii1I [ 'FrozenBalance' ]
   o0O00 = I1iii1I [ 'Stocks' ] + I1iii1I [ 'FrozenStocks' ]
   I1 = I1iii1I . get ( 'Commission' , 0 )
   Oo0 = I1iii1I [ 'Symbols' ]
   if ooO0OOo == 'Futures_CTP' or ooO0OOo == 'Futures_XTP' :
    o0ooo0oOoO = 'balance'
    if Oo0 :
     for o0Ooo in Oo0 :
      ooOOOoOO0 = I1iii1I [ 'Symbols' ] [ o0Ooo ]
      for OOo in [ 'Long' , 'Short' ] :
       if OOo in ooOOOoOO0 :
        O0oOO0Oo00ooo += ooOOOoOO0 [ OOo ] [ 'Margin' ] + ooOOOoOO0 [ OOo ] [ 'Profit' ]
    IiIi1ii . append ( [ I1iii1I [ 'Balance' ] + I1iii1I [ 'FrozenBalance' ] , I1 , O0oOO0Oo00ooo ] )
   elif 'Futures_' in ooO0OOo :
    Iii1Iiii1 = .0
    O0o0o0o0O = .0
    if Oo0 :
     for o0Ooo in Oo0 :
      ooOOOoOO0 = I1iii1I [ 'Symbols' ] [ o0Ooo ]
      for OOo in [ 'Long' , 'Short' ] :
       if OOo in ooOOOoOO0 :
        Iii1Iiii1 += ooOOOoOO0 [ OOo ] [ 'Margin' ] + ooOOOoOO0 [ OOo ] [ 'Profit' ]
    if I1iii1I [ 'QuoteCurrency' ] == 'USDT' :
     o0ooo0oOoO = 'USDT'
     O0o0o0o0O = O0oOO0Oo00ooo
    else :
     o0ooo0oOoO = I1iii1I [ 'BaseCurrency' ]
     O0o0o0o0O = o0O00
    IiIi1ii . append ( [ O0o0o0o0O , I1 , O0o0o0o0O + Iii1Iiii1 ] )
   else :
    if i1iiiiiIIIiii is None and Oo0 :
     for o0Ooo in I1iii1I [ 'Symbols' ] :
      i1iiiiiIIIiii = o0Ooo
      break
    if i1iiiiiIIIiii is not None :
     Oo0OoOo = I1iii1I [ 'Symbols' ] [ i1iiiiiIIIiii ] [ 'Last' ]
    IiIi1ii . append ( [ Oo0OoOo , O0oOO0Oo00ooo , o0O00 , I1 , O0oOO0Oo00ooo + ( o0O00 * Oo0OoOo ) ] )
   IIi1 . append ( pd . Timestamp ( IiiiiiIiI1 [ 0 ] , unit = 'ms' , tz = 'Asia/Shanghai' ) )
  i1iiIIII = [ "close" , "balance" , "stocks" , "fee" , "net" ]
  if 'Futures_' in ooO0OOo :
   i1iiIIII = [ o0ooo0oOoO , "fee" , "net" ]
  return pd . DataFrame ( IiIi1ii , index = IIi1 , columns = i1iiIIII )
  if 90 - 90: i1iiIII111 + ooOOO - i1i1i1111I / OooOoo / Oo % OooOoo
class iIIIi1IiI ( ) :
 def __init__ ( self , task , session ) :
  self . session = session
  self . task = task
  self . gApis = { }
  self . tpls = task [ 'Code' ]
  del task [ 'Code' ]
  self . ctx = O00OOo0Ooo00O ( task = self . task , gApis = self . gApis , progressCallback = self . progressCallback )
  if 40 - 40: Oo + I1Ii1I1 . oOo0O00 * i11
 def progressCallback ( self , st ) :
  if self . session is None :
   return
  self . session . sendall ( struct . pack ( '!II' , Iii11iiiiI ( st ) [ 'TaskStatus' ] , len ( st ) ) + st )
  if 6 - 6: OooOoo + i1i1i1111I
 def waitStop ( self , ctx ) :
  if self . session is None :
   return
  try :
   I1i1IIii = b''
   O00ooOoooo = 0
   self . session . settimeout ( None )
   while True :
    if O00ooOoooo > 0 :
     if len ( I1i1IIii ) - 4 >= O00ooOoooo :
      if I1i1IIii [ 4 : 4 + O00ooOoooo ] == b'stop' :
       ctx . Join ( )
       self . session . close ( )
       os . _exit ( 2 )
      break
    elif len ( I1i1IIii ) >= 4 :
     O00ooOoooo , = struct . unpack ( '!I' , I1i1IIii [ : 4 ] )
     continue
    I1i1IIii += self . session . recv ( ( O00ooOoooo - ( len ( I1i1IIii ) - 4 ) ) if O00ooOoooo > 0 else 4 )
  except :
   pass
   if 8 - 8: I1I / ooo000
 def exit_handler ( self , signum , frame ) :
  signal . signal ( signal . SIGINT , signal . SIG_IGN )
  self . ctx . Join ( )
  self . session . shutdown ( socket . SHUT_RDWR )
  os . _exit ( 0 )
  if 48 - 48: i1i1i1111I * iI1iI11Ii111 % i1i1i1111I + i1i1i1111I . iI1iII1I1I1i / OooOoo
 def Run ( self ) :
  signal . signal ( signal . SIGINT , self . exit_handler )
  if self . session and platform . system ( ) == 'Windows' :
   OOo = threading . Thread ( target = self . waitStop , args = ( self . ctx , ) )
   OOo . setDaemon ( True )
   OOo . start ( )
  try :
   IiI = False
   iI1IIiI1IiI = len ( self . tpls )
   for ii in xrange ( 0 , iI1IIiI1IiI ) :
    iIIii1 = self . tpls [ ii ]
    II1IiiIIi = copy . copy ( self . gApis )
    for o0o00oO0OO0O in iIIii1 [ 1 ] :
     II1IiiIIi [ o0o00oO0OO0O [ 0 ] ] = o0o00oO0OO0O [ 1 ]
    iIIiIi1 = iIIii1 [ 0 ] + "\n\nif 'init' in locals() and callable(init):\n    init()\n"
    if ii == iI1IIiI1IiI - 1 :
     iIIiIi1 += "\nmain()\nif 'onexit' in globals():\n    onexit()"
    if not IiI and 'matplotlib' in iIIiIi1 :
     IiI = True
     try :
      __import__ ( 'matplotlib' ) . use ( 'Agg' )
     except :
      pass
    exec ( iIIiIi1 . replace ( '\r\n' , '\n' ) , II1IiiIIi )
  except ( EOFError , SystemExit ) :
   pass
  except :
   OOooO0oo , o0O0oooo0 , I1ii1IIiii = sys . exc_info ( )
   OooO0Oo = [ x for x in traceback . extract_tb ( I1ii1IIiii ) if x [ 0 ] == '<string>' ]
   if OooO0Oo :
    Oo00O00o0oO = [ 'Traceback (most recent call last):\n' ]
    Oo00O00o0oO = Oo00O00o0oO + traceback . format_list ( OooO0Oo )
   else :
    Oo00O00o0oO = [ ]
   Oo00O00o0oO = Oo00O00o0oO + traceback . format_exception_only ( OOooO0oo , o0O0oooo0 )
   self . ctx . g_LogError ( '' . join ( Oo00O00o0oO ) )
  self . ctx . Join ( )
  self . session . shutdown ( socket . SHUT_RDWR )
  if 70 - 70: IIiIIiIi11I1 / i1i1i1111I . Ii
class i1o0ooO0o ( ) :
 def send ( self , * args ) :
  pass
 def sendall ( self , * args ) :
  pass
 def close ( self , * args ) :
  pass
 def shutdown ( self , * args ) :
  pass
  if 42 - 42: Iii1i
def i1II1I1iIIIii1I1 ( symbol , unit = '1d' , start = None , end = None , count = 1000 ) :
 if hasattr ( unit , 'endswith' ) :
  if unit . endswith ( 'd' ) :
   unit = int ( unit [ : - 1 ] ) * 1440
  elif unit . endswith ( 'h' ) :
   unit = int ( unit [ : - 1 ] ) * 60
  elif unit . endswith ( 'm' ) :
   unit = int ( unit [ : - 1 ] )
 O000 = int ( time . time ( ) )
 if end is not None :
  end = end . replace ( '/' , '-' )
  O000 = int ( time . mktime ( datetime . datetime . strptime ( end , "%Y-%m-%d %H:%M:%S" if ' ' in end else "%Y-%m-%d" ) . timetuple ( ) ) )
 if start is not None :
  start = start . replace ( '/' , '-' )
  o0oOO00Ooo0o = int ( time . mktime ( datetime . datetime . strptime ( start , "%Y-%m-%d %H:%M:%S" if ' ' in start else "%Y-%m-%d" ) . timetuple ( ) ) )
  if end is None :
   O000 = o0oOO00Ooo0o + ( unit * 100 * ( count + 10 ) )
 else :
  if end is None :
   o0oOO00Ooo0o = 0
   O000 = 0
  else :
   o0oOO00Ooo0o = O000 - ( unit * 100 * ( count + 10 ) )
 o0O0 = { "symbol" : symbol , "resolution" : unit , "from" : o0oOO00Ooo0o , "to" : O000 , "size" : count }
 IiIi1Ii1111 = json . loads ( iIIiii1iI ( i1ii1 + "/chart/history?" + urlencode ( o0O0 ) ) )
 try :
  import pandas as pd
  from pandas . plotting import register_matplotlib_converters
  register_matplotlib_converters ( )
 except :
  return IiIi1Ii1111
 IIi1 = [ ]
 for IiiiiiIiI1 in IiIi1Ii1111 :
  IIi1 . append ( pd . Timestamp ( IiiiiiIiI1 [ 0 ] , unit = 's' , tz = 'Asia/Shanghai' ) )
  IiiiiiIiI1 . pop ( 0 )
 i1iiIIII = [ "open" , "high" , "low" , "close" , "volume" ]
 if len ( IiIi1Ii1111 ) > 0 and len ( IiIi1Ii1111 [ 0 ] ) == 6 :
  i1iiIIII . append ( "openInterest" )
 return pd . DataFrame ( IiIi1Ii1111 , index = IIi1 , columns = i1iiIIII )
 if 29 - 29: Oo % OooOoo - i1i1i1111I + IiIIii11Ii / I1Ii1I1 + i1i1i1111I
if __name__ == '__main__' :
 OO = os . getenv ( "BOTVS_TASK_UUID" )
 iiIIi1iiII1Ii = None
 if OO == 'dummy' :
  iiIIi1iiII1Ii = iIi [ 's' ]
 else :
  iiIIi1iiII1Ii = i1o0ooO0o ( )
 if iiIIi1iiII1Ii is not None :
  iIIIi1IiI ( __cfg__ , iiIIi1iiII1Ii ) . Run ( )
  if 53 - 53: IiIIii11Ii - ooo000 % IIiIIiIi11I1 . iI1iI11Ii111
  if 84 - 84: I1Ii1I1 / i1i1i1111I - oOo0O00 . i1iiIII111 . Oo + i1i1i1111I
