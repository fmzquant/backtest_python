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
def oo0o0oO ( path , data ) :
 if 100 - 100: i11 - OooOoo * I1Ii1I1 / Ooo0Ooo / Iii1i
 I11iIi1i = '%s.%d.tmp' % ( path , os . getpid ( ) )
 with open ( I11iIi1i , 'wb' ) as oooOOOooo :
  oooOOOooo . write ( data )
 getattr ( os , 'replace' , os . rename ) ( I11iIi1i , path )
 if 85 - 85: i1iiIII111 - ooOOO
 if 9 - 9: I11iiIi11i1I + oOO - i1iiIII111
def ii1Iii ( ) :
 if 77 - 77: i1iiIII111 + i11 - Oo % ooo000
 return os . getenv ( "TASK_UUID" ) or os . getenv ( "BOTVS_TASK_UUID" )
 if 74 - 74: Ii + Ooo0Ooo
def iIi1I1I ( ) :
 II1III1I1i = tempfile . gettempdir ( ) + '/cache'
 if not os . path . exists ( II1III1I1i ) :
  try :
   os . mkdir ( II1III1I1i )
  except :
   pass
 return II1III1I1i
 if 25 - 25: ooo000 * I1Ii1I1 * iI1iI11Ii111 % oOo0O00
def oOoO00 ( e ) :
 if 84 - 84: iI1iII1I1I1i - I1I - I11iiIi11i1I
 if not hasattr ( e , '_body' ) :
  e . _body = e . read ( )
  if e . info ( ) . get ( 'Content-Encoding' ) == 'gzip' :
   try :
    e . _body = zlib . decompress ( e . _body , 16 + zlib . MAX_WBITS )
   except :
    pass
 return e . _body
 if 61 - 61: i1i1i1111I / I11iiIi11i1I + i11 * i1i1i1111I + oOo0O00 / i1
def ii ( url , body = None ) :
 try :
  IiII11i11II = urllib2 . Request ( url , data = body . encode ( 'utf-8' ) if body is not None else None )
  IiII11i11II . add_header ( 'Accept-Encoding' , 'gzip, deflate' )
  if body is not None :
   IiII11i11II . add_header ( 'Content-Type' , 'application/json' )
  o00o = urllib2 . urlopen ( IiII11i11II )
  Ii11I = o00o . read ( )
  if o00o . info ( ) . get ( 'Content-Encoding' ) == 'gzip' :
   Ii11I = zlib . decompress ( Ii11I , 16 + zlib . MAX_WBITS )
  return Ii11I
 except urllib2 . HTTPError as iIiO000O0Oo0 :
  Oo0O0O = dict ( iIiO000O0Oo0 . info ( ) )
  Ii1IiIII1 = oOoO00 ( iIiO000O0Oo0 )
  print ( "urllib2.HTTPError - Code: %s, URL: %s, Headers: %s, Body: %s" % ( iIiO000O0Oo0 . code , iIiO000O0Oo0 . url , Oo0O0O , Ii1IiIII1 ) )
  raise
  if 11 - 11: i1 / ooo000
class iII :
 @ staticmethod
 def _skip ( arr , period ) :
  OooOO00o = 0
  OO = 0
  for OO in xrange ( 0 , len ( arr ) ) :
   if arr [ OO ] is not None :
    OooOO00o += 1
   if OooOO00o == period :
    break
  return OO
  if 39 - 39: oOO - oOO * i1 % IIiIIiIi11I1
 @ staticmethod
 def _sum ( arr , num ) :
  IIiII11I = 0.0
  for I11i in xrange ( 0 , num ) :
   if arr [ I11i ] is not None :
    IIiII11I += arr [ I11i ]
  return IIiII11I
  if 51 - 51: Iii1i % Ooo0Ooo . iI1iII1I1I1i / Ii / ooOOO
 @ staticmethod
 def _avg ( arr , num ) :
  if len ( arr ) == 0 :
   return 0
  IIiII11I = 0.0
  OOOOO = 0
  for I11i in xrange ( 0 , min ( len ( arr ) , num ) ) :
   if arr [ I11i ] is not None :
    IIiII11I += arr [ I11i ]
    OOOOO += 1
  if OOOOO == 0 :
   return 0
  return IIiII11I / OOOOO
  if 36 - 36: i1i1i1111I + Iii1i - oOO * Ii
 @ staticmethod
 def _zeros ( n ) :
  return [ 0.0 ] * n
  if 45 - 45: i1i1i1111I * Ii
 @ staticmethod
 def _set ( arr , start , end , value ) :
  for I11i in xrange ( start , min ( len ( arr ) , end ) ) :
   arr [ I11i ] = value
   if 97 - 97: i1
 @ staticmethod
 def _diff ( a , b ) :
  iiiiI1i1iI1 = [ None ] * len ( b )
  for I11i in xrange ( 0 , len ( b ) ) :
   if a [ I11i ] is not None and b [ I11i ] is not None :
    iiiiI1i1iI1 [ I11i ] = a [ I11i ] - b [ I11i ]
  return iiiiI1i1iI1
  if 33 - 33: i11 / Oo % I1Ii1I1
 @ staticmethod
 def _move_diff ( a ) :
  iiiiI1i1iI1 = [ None ] * ( len ( a ) - 1 )
  for I11i in xrange ( 1 , len ( a ) ) :
   iiiiI1i1iI1 [ I11i - 1 ] = a [ I11i ] - a [ I11i - 1 ]
  return iiiiI1i1iI1
  if 40 - 40: iI1iI11Ii111
 @ staticmethod
 def _cmp ( arr , start , end , cmpFunc ) :
  I1II1ii111i = arr [ start ]
  for I11i in xrange ( start , end ) :
   I1II1ii111i = cmpFunc ( arr [ I11i ] , I1II1ii111i )
  return I1II1ii111i
  if 14 - 14: i11 + iI1iI11Ii111 . IiIIii11Ii . Ooo0Ooo % IiIIii11Ii * i1i1i1111I
 @ staticmethod
 def _filt ( records , n , attr , iv , cmpFunc ) :
  if len ( records ) < 2 :
   return None
  I1II1ii111i = iv
  oOoOO0O0 = 0
  if n != 0 :
   oOoOO0O0 = len ( records ) - min ( len ( records ) - 1 , n ) - 1
  for I11i in xrange ( len ( records ) - 2 , oOoOO0O0 - 1 , - 1 ) :
   if records [ I11i ] is not None :
    if attr is not None :
     I1II1ii111i = cmpFunc ( I1II1ii111i , records [ I11i ] [ attr ] )
    else :
     I1II1ii111i = cmpFunc ( I1II1ii111i , records [ I11i ] )
  return I1II1ii111i
  if 20 - 20: I11iiIi11i1I / ooOOO * oOO % IIiIIiIi11I1
 @ staticmethod
 def _ticks ( records ) :
  if len ( records ) == 0 :
   return [ ]
  if isinstance ( records [ 0 ] , int ) or isinstance ( records [ 0 ] , float ) :
   return records
   if 60 - 60: iI1iI11Ii111 * i1iiIII111 + i1i1i1111I / ooOOO
  o000OOoOO = [ None ] * len ( records )
  for I11i in xrange ( 0 , len ( records ) ) :
   o000OOoOO [ I11i ] = records [ I11i ] [ 'Close' ]
  return o000OOoOO
  if 24 - 24: IiIIii11Ii / i1iiIII111 + i11 + ooOOO
 @ staticmethod
 def _sma ( S , period ) :
  ii1 = iII . _zeros ( len ( S ) )
  OO = iII . _skip ( S , period )
  iII . _set ( ii1 , 0 , OO , None )
  if OO < len ( S ) :
   IIiII11I = 0
   for I11i in xrange ( OO , len ( S ) ) :
    if I11i == OO :
     IIiII11I = iII . _sum ( S , I11i + 1 )
    else :
     IIiII11I += S [ I11i ] - S [ I11i - period ]
    ii1 [ I11i ] = IIiII11I / period
  return ii1
  if 53 - 53: i1 % IIiIIiIi11I1 * IIiIIiIi11I1 * iI1iII1I1I1i
 @ staticmethod
 def _smma ( S , period ) :
  ii1 = iII . _zeros ( len ( S ) )
  OO = iII . _skip ( S , period )
  iII . _set ( ii1 , 0 , OO , None )
  if OO < len ( S ) :
   ii1 [ OO ] = iII . _avg ( S , OO + 1 )
   for I11i in xrange ( OO + 1 , len ( S ) ) :
    ii1 [ I11i ] = ( ii1 [ I11i - 1 ] * ( period - 1 ) + S [ I11i ] ) / period
  return ii1
  if 3 - 3: oOo0O00
 @ staticmethod
 def _ema ( S , period ) :
  ii1 = iII . _zeros ( len ( S ) )
  IiI11II11II11 = 2.0 / ( period + 1 )
  OO = iII . _skip ( S , period )
  iII . _set ( ii1 , 0 , OO , None )
  if OO < len ( S ) :
   ii1 [ OO ] = iII . _avg ( S , OO + 1 )
   for I11i in xrange ( OO + 1 , len ( S ) ) :
    ii1 [ I11i ] = ( ( S [ I11i ] - ii1 [ I11i - 1 ] ) * IiI11II11II11 ) + ii1 [ I11i - 1 ]
  return ii1
  if 43 - 43: iI1iII1I1I1i * oOo0O00 + ooOOO
class iiIi111iii1II :
 def __init__ ( self , logPtr = None ) :
  self . _logPtr = logPtr
  if 93 - 93: i11 % Oo + oOo0O00 / IiIIii11Ii / I1Ii1I1
 def _log ( self , name , * args ) :
  if self . _logPtr is not None :
   self . _logPtr ( name , Iio0 ( ',' . join ( map ( str , args ) ) ) )
   if 39 - 39: oOO
 @ staticmethod
 def Highest ( records , n , attr = None ) :
  return iII . _filt ( records , n , attr , 5e-324 , max )
  if 17 - 17: Ii . oOo0O00 % OooOoo
 @ staticmethod
 def Lowest ( records , n , attr = None ) :
  return iII . _filt ( records , n , attr , 1.7976931348623157e+308 , min )
  if 82 - 82: Iii1i . oOo0O00 % IIiIIiIi11I1 - iI1iII1I1I1i
 def MA ( self , records , period = 9 ) :
  self . _log ( 'MA' , period )
  if 44 - 44: ooOOO . IIiIIiIi11I1
  return iII . _sma ( iII . _ticks ( records ) , period )
  if 15 - 15: ooo000
 def SMA ( self , records , period = 9 ) :
  self . _log ( 'SMA' , period )
  if 63 - 63: iI1iI11Ii111
  return iII . _sma ( iII . _ticks ( records ) , period )
  if 81 - 81: OooOoo . iI1iI11Ii111 / i1i1i1111I + Oo / Ooo0Ooo % i11
 def EMA ( self , records , period = 9 ) :
  self . _log ( 'EMA' , period )
  if 77 - 77: I11iiIi11i1I / iI1iII1I1I1i - oOo0O00 - Ooo0Ooo % oOo0O00
  return iII . _ema ( iII . _ticks ( records ) , period )
  if 73 - 73: i11 . Oo * I1I / i1i1i1111I + I1Ii1I1
 def MACD ( self , records , fastEMA = 12 , slowEMA = 26 , signalEMA = 9 ) :
  self . _log ( 'MACD' , fastEMA , slowEMA , signalEMA )
  if 31 - 31: i1i1i1111I % I1Ii1I1
  o000OOoOO = iII . _ticks ( records )
  I11IIiiI1 = iII . _ema ( o000OOoOO , slowEMA )
  O0o = iII . _ema ( o000OOoOO , fastEMA )
  if 34 - 34: I1I % Oo - i1 % OooOoo * OooOoo + i1i1i1111I
  i111II = iII . _diff ( O0o , I11IIiiI1 )
  if 16 - 16: oOo0O00 * ooo000 * I11iiIi11i1I + oOO
  O0oOOooo000o0O = iII . _ema ( i111II , signalEMA )
  i11IIi1I1 = iII . _diff ( i111II , O0oOOooo000o0O )
  return [ i111II , O0oOOooo000o0O , i11IIi1I1 ]
  if 63 - 63: IIiIIiIi11I1
 def BOLL ( self , records , period = 20 , multiplier = 2 ) :
  self . _log ( 'BOLL' , period , multiplier )
  if 45 - 45: i1iiIII111 + Oo * i1iiIII111 / Ooo0Ooo
  OO0oOoOOOoO0 = iII . _ticks ( records )
  OO = period - 1
  while OO < len ( OO0oOoOOOoO0 ) and ( OO0oOoOOOoO0 [ OO ] is None ) :
   OO += 1
  Iii1I1I1 = iII . _zeros ( len ( OO0oOoOOOoO0 ) )
  oO0oO = iII . _zeros ( len ( OO0oOoOOOoO0 ) )
  Oo0 = iII . _zeros ( len ( OO0oOoOOOoO0 ) )
  iII . _set ( Iii1I1I1 , 0 , OO , None )
  iII . _set ( oO0oO , 0 , OO , None )
  iII . _set ( Oo0 , 0 , OO , None )
  OOOOO = 0.0
  for I11i in xrange ( OO , len ( OO0oOoOOOoO0 ) ) :
   if I11i == OO :
    for OooOO00o in xrange ( 0 , period ) :
     OOOOO += OO0oOoOOOoO0 [ OooOO00o ]
   else :
    OOOOO = OOOOO + OO0oOoOOOoO0 [ I11i ] - OO0oOoOOOoO0 [ I11i - period ]
   i1i1Ii = OOOOO / period
   iiiiI1i1iI1 = 0
   for OooOO00o in xrange ( I11i + 1 - period , I11i + 1 ) :
    iiiiI1i1iI1 += ( OO0oOoOOOoO0 [ OooOO00o ] - i1i1Ii ) * ( OO0oOoOOOoO0 [ OooOO00o ] - i1i1Ii )
   ii1iI1I11 = math . sqrt ( iiiiI1i1iI1 / period )
   OOoO0oOo0 = i1i1Ii + ( multiplier * ii1iI1I11 )
   iII1Ii = i1i1Ii - ( multiplier * ii1iI1I11 )
   Iii1I1I1 [ I11i ] = OOoO0oOo0
   oO0oO [ I11i ] = i1i1Ii
   Oo0 [ I11i ] = iII1Ii
  return [ Iii1I1I1 , oO0oO , Oo0 ]
  if 37 - 37: iI1iI11Ii111 + IIiIIiIi11I1 % iI1iII1I1I1i / IIiIIiIi11I1 % i1iiIII111 + oOO
 def KDJ ( self , records , n = 9 , k = 3 , d = 3 ) :
  self . _log ( 'KDJ' , n , k , d )
  if 98 - 98: iI1iII1I1I1i - I1I + i1 * ooo000 % i1
  o0O0OO0 = iII . _zeros ( len ( records ) )
  iII . _set ( o0O0OO0 , 0 , n - 1 , None )
  Iioo0Oo0oO0 = iII . _zeros ( len ( records ) )
  iII11I1iI = iII . _zeros ( len ( records ) )
  O0O0o0oo00Oo = iII . _zeros ( len ( records ) )
  if 96 - 96: Ooo0Ooo
  ii1IiiIiI = iII . _zeros ( len ( records ) )
  Ooo0O00o = iII . _zeros ( len ( records ) )
  for I11i in xrange ( 0 , len ( records ) ) :
   ii1IiiIiI [ I11i ] = records [ I11i ] [ 'High' ]
   Ooo0O00o [ I11i ] = records [ I11i ] [ 'Low' ]
   if 22 - 22: i11 . ooo000
  for I11i in xrange ( 0 , len ( records ) ) :
   if I11i >= ( n - 1 ) :
    IiiI1III1iI = records [ I11i ] [ 'Close' ]
    oOOOOOOoOOooO0O0 = iII . _cmp ( ii1IiiIiI , I11i - ( n - 1 ) , I11i + 1 , max )
    O0 = iII . _cmp ( Ooo0O00o , I11i - ( n - 1 ) , I11i + 1 , min )
    o0O0OO0 [ I11i ] = ( 100 * ( ( IiiI1III1iI - O0 ) / ( oOOOOOOoOOooO0O0 - O0 ) ) ) if oOOOOOOoOOooO0O0 != O0 else 100
    Iioo0Oo0oO0 [ I11i ] = float ( 1 * o0O0OO0 [ I11i ] + ( k - 1 ) * Iioo0Oo0oO0 [ I11i - 1 ] ) / k
    iII11I1iI [ I11i ] = float ( 1 * Iioo0Oo0oO0 [ I11i ] + ( d - 1 ) * iII11I1iI [ I11i - 1 ] ) / d
   else :
    Iioo0Oo0oO0 [ I11i ] = iII11I1iI [ I11i ] = 50.0
    o0O0OO0 [ I11i ] = 0.0
   O0O0o0oo00Oo [ I11i ] = 3 * Iioo0Oo0oO0 [ I11i ] - 2 * iII11I1iI [ I11i ]
   if 51 - 51: iI1iI11Ii111 . Ii * i11
  for I11i in xrange ( 0 , n - 1 ) :
   Iioo0Oo0oO0 [ I11i ] = iII11I1iI [ I11i ] = O0O0o0oo00Oo [ I11i ] = None
  return [ Iioo0Oo0oO0 , iII11I1iI , O0O0o0oo00Oo ]
  if 96 - 96: i1 + IiIIii11Ii % I1I / i11
 def RSI ( self , records , period = 14 ) :
  self . _log ( 'RSI' , period )
  if 33 - 33: OooOoo * Oo * Ii * iI1iII1I1I1i + iI1iI11Ii111 . IiIIii11Ii
  OOOOO = period
  iI1Iii = iII . _zeros ( len ( records ) )
  iII . _set ( iI1Iii , 0 , len ( iI1Iii ) , None )
  if len ( records ) < OOOOO :
   return iI1Iii
   if 17 - 17: I11iiIi11i1I + ooOOO % ooOOO / oOo0O00 - i1iiIII111
  o000OOoOO = iII . _ticks ( records )
  Iii = iII . _move_diff ( o000OOoOO )
  OOo = Iii [ : OOOOO ]
  OOoO0oOo0 = 0.0
  oO000O0O0 = 0.0
  for I11i in xrange ( 0 , len ( OOo ) ) :
   if OOo [ I11i ] >= 0 :
    OOoO0oOo0 += OOo [ I11i ]
   else :
    oO000O0O0 += OOo [ I11i ]
  OOoO0oOo0 /= OOOOO
  oO000O0O0 /= OOOOO
  oO000O0O0 = - oO000O0O0
  if oO000O0O0 != 0 :
   ooOo00O0o0o0 = OOoO0oOo0 / oO000O0O0
  else :
   ooOo00O0o0o0 = 0
  iI1Iii [ OOOOO ] = 100 - 100 / ( 1 + ooOo00O0o0o0 )
  OOooooOOooo0 = 0.0
  II1111I11 = 0.0
  IiI1IIi1IiII = 0.0
  for I11i in xrange ( OOOOO + 1 , len ( o000OOoOO ) ) :
   OOooooOOooo0 = Iii [ I11i - 1 ]
   if OOooooOOooo0 > 0 :
    II1111I11 = OOooooOOooo0
    IiI1IIi1IiII = 0.0
   else :
    II1111I11 = 0.0
    IiI1IIi1IiII = - OOooooOOooo0
   OOoO0oOo0 = ( OOoO0oOo0 * ( OOOOO - 1 ) + II1111I11 ) / OOOOO
   oO000O0O0 = ( oO000O0O0 * ( OOOOO - 1 ) + IiI1IIi1IiII ) / OOOOO
   ooOo00O0o0o0 = 0 if oO000O0O0 == 0 else ( OOoO0oOo0 / oO000O0O0 )
   iI1Iii [ I11i ] = 100 - 100 / ( 1 + ooOo00O0o0o0 )
  return iI1Iii
  if 31 - 31: IiIIii11Ii . IiIIii11Ii % Ii
 def OBV ( self , records ) :
  self . _log ( 'OBV' )
  if 51 - 51: Oo / i1i1i1111I - I1I
  if len ( records ) == 0 :
   return [ ]
   if 83 - 83: Iii1i % i1iiIII111 . OooOoo / I1I % oOO . I1I
  if 'Close' not in records [ 0 ] :
   raise "self.OBV argument must KLine"
   if 76 - 76: i1iiIII111 / OooOoo
  ii1 = iII . _zeros ( len ( records ) )
  for I11i in xrange ( 0 , len ( records ) ) :
   if I11i == 0 :
    ii1 [ I11i ] = records [ I11i ] [ 'Volume' ]
   elif records [ I11i ] [ 'Close' ] >= records [ I11i - 1 ] [ 'Close' ] :
    ii1 [ I11i ] = ii1 [ I11i - 1 ] + records [ I11i ] [ 'Volume' ]
   else :
    ii1 [ I11i ] = ii1 [ I11i - 1 ] - records [ I11i ] [ 'Volume' ]
  return ii1
  if 77 - 77: ooOOO
 def ATR ( self , records , period = 14 ) :
  self . _log ( 'ATR' , period )
  if 19 - 19: ooOOO % I1Ii1I1
  if len ( records ) == 0 :
   return [ ]
  if 'Close' not in records [ 0 ] :
   raise "self.ATR argument must KLine"
   if 15 - 15: OooOoo . IiIIii11Ii . iI1iI11Ii111 / Iii1i + ooOOO / Ii
  ii1 = iII . _zeros ( len ( records ) )
  Ii1iIII11i = 0.0
  OOOOO = 0.0
  for I11i in xrange ( 0 , len ( records ) ) :
   oo000OO0ooO = 0
   if I11i == 0 :
    oo000OO0ooO = records [ I11i ] [ 'High' ] - records [ I11i ] [ 'Low' ]
   else :
    oo000OO0ooO = max ( records [ I11i ] [ 'High' ] - records [ I11i ] [ 'Low' ] , abs ( records [ I11i ] [ 'High' ] - records [ I11i - 1 ] [ 'Close' ] ) , abs ( records [ I11i - 1 ] [ 'Close' ] - records [ I11i ] [ 'Low' ] ) )
   Ii1iIII11i += oo000OO0ooO
   if I11i < period :
    OOOOO = Ii1iIII11i / ( I11i + 1 )
   else :
    OOOOO = ( ( ( period - 1 ) * OOOOO ) + oo000OO0ooO ) / period
   ii1 [ I11i ] = OOOOO
  return ii1
  if 52 - 52: Oo * iI1iII1I1I1i - i1i1i1111I . i1iiIII111
 def Alligator ( self , records , jawLength = 13 , teethLength = 8 , lipsLength = 5 ) :
  self . _log ( 'Alligator' , jawLength , teethLength , lipsLength )
  if 78 - 78: OooOoo . ooOOO
  o000OOoOO = [ ]
  for I11i in xrange ( 0 , len ( records ) ) :
   o000OOoOO . append ( ( records [ I11i ] [ 'High' ] + records [ I11i ] [ 'Low' ] ) / 2 )
  return [
 [ None ] * 8 + iII . _smma ( o000OOoOO , jawLength ) ,
  [ None ] * 5 + iII . _smma ( o000OOoOO , teethLength ) ,
  [ None ] * 3 + iII . _smma ( o000OOoOO , lipsLength )
  ]
  if 80 - 80: oOO % i1iiIII111 * i11 - oOo0O00 % I11iiIi11i1I - i11
 def CMF ( self , records , period = 20 ) :
  self . _log ( 'CMF' , period )
  if 56 - 56: Oo
  IiIIIII1i = [ ]
  O0OOo0O = 0.0
  iiI = 0.0
  I1i1 = [ ]
  oO0O0oO0 = [ ]
  for I11i in xrange ( 0 , len ( records ) ) :
   iiiiI1i1iI1 = 0.0
   if records [ I11i ] [ 'High' ] != records [ I11i ] [ 'Low' ] :
    iiiiI1i1iI1 = ( 2 * records [ I11i ] [ 'Close' ] - records [ I11i ] [ 'Low' ] - records [ I11i ] [ 'High' ] ) / ( records [ I11i ] [ 'High' ] - records [ I11i ] [ 'Low' ] ) * records [ I11i ] [ 'Volume' ]
   I1i1 . append ( iiiiI1i1iI1 )
   oO0O0oO0 . append ( records [ I11i ] [ 'Volume' ] )
   O0OOo0O += iiiiI1i1iI1
   iiI += records [ I11i ] [ 'Volume' ]
   if I11i >= period :
    O0OOo0O -= I1i1 . pop ( 0 )
    iiI -= oO0O0oO0 . pop ( 0 )
   IiIIIII1i . append ( O0OOo0O / iiI )
  return IiIIIII1i
  if 40 - 40: iI1iI11Ii111 . I1I % OooOoo
  if 85 - 85: Oo / oOO + Oo + ooOOO
class I11111i111 :
 def __init__ ( self , name ) :
  self . __name = name
  sys . modules [ 'talib' ] = self
 def __getattr__ ( self , attr ) :
  if attr == '__file__' :
   return 'talib.py'
  raise Exception ( 'Please install %s module for python (%s)' % ( self . __name , attr ) )
  if 35 - 35: I1Ii1I1
class OOooo00 ( list ) :
 def __init__ ( self , data ) :
  super ( OOooo00 , self ) . __init__ ( data )
  self . __data = data
 def __getattr__ ( self , attr ) :
  if attr . startswith ( '_' ) :
   raise AttributeError
  IiIIIII1i = [ ]
  for o00oiIIIiII1 in self . __data :
   IiIIIII1i . append ( o00oiIIIiII1 [ attr ] )
  if oo :
   IiIIIII1i = numpy . array ( IiIIIII1i , dtype = 'float64' )
  setattr ( self , attr , IiIIIII1i )
  return IiIIIII1i
  if 21 - 21: i1i1i1111I . iI1iII1I1I1i + Ooo0Ooo * i11 - iI1iII1I1I1i
oo = False
try :
 import talib
 import numpy
 oo = True
except ImportError :
 talib = I11111i111 ( 'talib' )
 if 54 - 54: I11iiIi11i1I / IiIIii11Ii . Ooo0Ooo
 if 15 - 15: iI1iI11Ii111 * I11iiIi11i1I - oOo0O00
class i1iiiIii ( dict ) :
 def __getattr__ ( self , name ) :
  if name in self :
   return self [ name ]
  else :
   raise AttributeError ( "no attribute '%s'" % name )
   if 98 - 98: i1iiIII111 + Iii1i . IIiIIiIi11I1
 def __setattr__ ( self , name , value ) :
  self [ name ] = value
  if 96 - 96: OooOoo / oOO - i1 * I11iiIi11i1I
 def __delattr__ ( self , name ) :
  if name in self :
   del self [ name ]
  else :
   raise AttributeError ( "no attribute '%s'" % name )
   if 72 - 72: i1i1i1111I + Ii - Iii1i - i1i1i1111I - iI1iI11Ii111 + Ooo0Ooo
def OoOoOo ( item ) :
 if isinstance ( item , float ) and ( math . isnan ( item ) or math . isinf ( item ) ) :
  if 80 - 80: IiIIii11Ii * Ooo0Ooo . i1 . Ooo0Ooo
  if 76 - 76: i1i1i1111I % oOo0O00 - i1iiIII111 * i1
  return str ( item )
 if isinstance ( item , ( dict , list , tuple ) ) :
  try :
   if 43 - 43: I11iiIi11i1I . Oo
   if 68 - 68: IiIIii11Ii / OooOoo + Oo / ooOOO / I1I
   iii1II11I111 = json . loads ( json . dumps ( item , default = str ) , parse_constant = lambda IiiI1III1iI : None )
   return json . dumps ( iii1II11I111 , separators = ( ',' , ':' ) , ensure_ascii = not I11II1Ii )
  except Exception :
   return str ( item )
 return item
 if 82 - 82: i1iiIII111 + iI1iII1I1I1i / IIiIIiIi11I1 . oOo0O00 - ooOOO
 if 76 - 76: IiIIii11Ii
def IIiiIIi1i ( args , status = False ) :
 O00oO00oO0O = [ ]
 for o00oiIIIiII1 in args :
  if hasattr ( o00oiIIIiII1 , 'savefig' ) and callable ( o00oiIIIiII1 . savefig ) :
   iiiiI1i1iI1 = io . BytesIO ( )
   o00oiIIIiII1 . savefig ( iiiiI1i1iI1 , format = "png" )
   O00oO00oO0O . append ( '`data:image/png;base64,%s`' % ( base64 . b64encode ( iiiiI1i1iI1 . getvalue ( ) ) . decode ( 'utf-8' ) ) )
  elif isinstance ( o00oiIIIiII1 , dict ) and o00oiIIIiII1 . get ( 'type' ) == 'table' and o00oiIIIiII1 . get ( 'cols' ) :
   O00oO00oO0O . append ( '`%s`' % json . dumps ( o00oiIIIiII1 ) )
  elif status and isinstance ( o00oiIIIiII1 , ( dict , list , tuple , float ) ) :
   if 65 - 65: iI1iII1I1I1i . Oo
   O00oO00oO0O . append ( str ( OoOoOo ( o00oiIIIiII1 ) ) )
  else :
   O00oO00oO0O . append ( str ( o00oiIIIiII1 ) )
 return Iio0 ( ' ' . join ( O00oO00oO0O ) )
 if 44 - 44: I11iiIi11i1I . I1Ii1I1 * i1 . iI1iII1I1I1i * I11iiIi11i1I - I11iiIi11i1I
def IIIII11 ( v ) :
 if isinstance ( v , bytes ) :
  if 7 - 7: i1iiIII111 * i1iiIII111 . oOO . ooo000 * ooOOO + i11
  return v . decode ( 'utf-8' , 'replace' )
 return v
 if 20 - 20: iI1iI11Ii111 . OooOoo * IiIIii11Ii
O00o = json . JSONEncoder ( separators = ( ',' , ':' ) , allow_nan = False ) . encode
OOo00000o00O = json . decoder . JSONDecoder ( object_hook = i1iiiIii ) . scan_once
if 66 - 66: IiIIii11Ii . I1Ii1I1 + I1I
class Ooooo ( object ) :
 def __init__ ( self , lib , ctx ) :
  if 38 - 38: I11iiIi11i1I
  if 99 - 99: I11iiIi11i1I * i1iiIII111 . OooOoo % ooo000 % OooOoo
  if 21 - 21: i11 * I1Ii1I1
  if 93 - 93: Ooo0Ooo . i1 + i11 - oOo0O00
  lib . api_call . argtypes = [ ctypes . c_void_p , ctypes . c_char_p , ctypes . c_char_p , ctypes . c_size_t ]
  lib . api_call . restype = ctypes . c_char_p
  self . call = lib . api_call
  self . ctx = ctx
  if 97 - 97: i1 - i1 % IIiIIiIi11I1 + IiIIii11Ii / iI1iI11Ii111 * iI1iII1I1I1i
 def __call__ ( self , name , * args ) :
  O00Ooo0o = O00o ( args ) . encode ( 'utf-8' )
  oOO0o00oOooO = self . call ( self . ctx , name , O00Ooo0o , len ( O00Ooo0o ) ) . decode ( 'utf-8' )
  IiiI1III1iI = oOO0o00oOooO [ 0 ]
  if IiiI1III1iI == 'r' :
   return OOo00000o00O ( oOO0o00oOooO , 1 ) [ 0 ]
  if IiiI1III1iI == 'x' :
   raise EOFError ( )
  raise Exception ( OOo00000o00O ( oOO0o00oOooO , 1 ) [ 0 ] )
  if 58 - 58: Ooo0Ooo / i1 . IiIIii11Ii - Ooo0Ooo . Ii
def OOoOo ( t ) :
 if t is not None and 'Info' not in t :
  t [ 'Info' ] = None
 return t
 if 4 - 4: i1iiIII111 . OooOoo / Ii
def Oo0OO0oooOoo0 ( v , keys ) :
 if v is None :
  if 94 - 94: Ooo0Ooo % oOo0O00 . oOo0O00 / Ii . i1
  return None
 return [ dic2obj ( [ ( k , d [ k ] ) for k in keys if k in d ] ) for d in v ]
 if 54 - 54: iI1iII1I1I1i % Oo . i11 - Iii1i % I11iiIi11i1I * iI1iI11Ii111
iIi1Ii = ( 'MarginLevel' , 'Amount' , 'FrozenAmount' , 'Price' , 'Profit' , 'Margin' , 'Type' , 'Symbol' , 'ContractType' )
if 74 - 74: i1i1i1111I / IiIIii11Ii % I11iiIi11i1I . oOO
def Ii1III1iI ( v ) :
 v = Oo0OO0oooOoo0 ( v , iIi1Ii )
 if v is not None :
  for I111i in v :
   if not I111i . get ( 'ContractType' ) :
    I111i . pop ( 'ContractType' , None )
 return v
 if 99 - 99: i1iiIII111 * Ii / oOO + I1Ii1I1 + iI1iII1I1I1i
def oo0O ( r ) :
 return int ( r ) if r is not None and r > 0 else None
 if 5 - 5: Ii / Ii / i1iiIII111
class OOOo0oOOo0 :
 routineId = 0
 def __init__ ( self , v ) :
  self . isWait = False
  self . v = v
  OOOo0oOOo0 . routineId += 1
  if 43 - 43: IiIIii11Ii . ooo000 - iI1iII1I1I1i
 def wait ( self , timeout = 0 ) :
  if self . isWait :
   return ( None , False )
  self . isWait = True
  return ( self . v , True )
  if 50 - 50: IIiIIiIi11I1 / IIiIIiIi11I1 * IiIIii11Ii
 def __repr__ ( self ) :
  return '<Go %d>' % OOOo0oOOo0 . routineId
  if 67 - 67: Ooo0Ooo . Ooo0Ooo . i11
class IiiI1II :
 def __init__ ( self , api , idx , opt , cfg ) :
  self . api = api
  self . idx = idx
  self . opt = opt
  self . cfg = cfg
  self . name = cfg [ "Id" ]
  self . label = cfg [ "Label" ]
  self . currency = '%s_%s' % ( cfg [ "BaseCurrency" ] , cfg [ "QuoteCurrency" ] )
  self . baseCurrency = cfg [ "BaseCurrency" ]
  self . quoteCurrency = cfg [ "QuoteCurrency" ]
  self . maxBarLen = cfg . get ( 'MaxBarLen' , 1000 )
  self . period = opt [ 'Period' ]
  self . ct = ''
  self . records_cache = { }
  if 58 - 58: Ooo0Ooo * iI1iII1I1I1i / iI1iII1I1I1i + IiIIii11Ii . i11
 def Go ( self , method , * args ) :
  return OOOo0oOOo0 ( getattr ( self , method ) ( * args ) )
  if 56 - 56: Ii * ooo000 . IiIIii11Ii
 def GetName ( self ) :
  return self . name
  if 66 - 66: I1Ii1I1 * OooOoo . iI1iII1I1I1i % OooOoo . i1 . IiIIii11Ii
 def GetLabel ( self ) :
  return self . label
  if 47 - 47: Ii % OooOoo % iI1iII1I1I1i * IiIIii11Ii
 def GetCurrency ( self ) :
  return self . currency
  if 48 - 48: iI1iI11Ii111 . I11iiIi11i1I / ooo000 + i1iiIII111
 def GetBaseCurrency ( self ) :
  return self . baseCurrency
  if 84 - 84: Oo / I1Ii1I1 . IIiIIiIi11I1
 def GetQuoteCurrency ( self ) :
  return self . quoteCurrency
  if 67 - 67: Oo % ooOOO + iI1iII1I1I1i * I1I
 def GetUSDCNY ( self ) :
  return self . api ( b'Exchange_GetUSDCNY' , self . idx )
  if 79 - 79: IIiIIiIi11I1 * Oo / OooOoo
 def SetMaxBarLen ( self , n ) :
  self . maxBarLen = n
  if 10 - 10: iI1iII1I1I1i / i1iiIII111 . IiIIii11Ii * i1i1i1111I
 def SetPrecision ( self , a , b ) :
  self . api ( b'Exchange_SetPrecision' , self . idx , a , b )
  if 71 - 71: oOo0O00 + I1Ii1I1 / I11iiIi11i1I + Oo / I1I
 def GetRate ( self ) :
  return self . api ( b'Exchange_GetRate' , self . idx )
  if 18 - 18: Iii1i - IiIIii11Ii
 def SetProxy ( self , s ) :
  pass
  if 71 - 71: iI1iII1I1I1i + OooOoo % i1i1i1111I % oOo0O00 . ooo000
 def SetTimeout ( self , ms ) :
  pass
  if 92 - 92: I11iiIi11i1I - Ooo0Ooo - i1i1i1111I % i1iiIII111 / i1i1i1111I * iI1iII1I1I1i
 def SetBase ( self , s ) :
  return self . api ( b'Exchange_SetBase' , self . idx , s )
  if 60 - 60: IiIIii11Ii % oOO / iI1iI11Ii111 * OooOoo / I11iiIi11i1I - Ii
 def GetBase ( self ) :
  return self . api ( b'Exchange_GetBase' , self . idx )
  if 16 - 16: oOo0O00 / I1Ii1I1 / i1 + I11iiIi11i1I + oOo0O00
 def SetCurrency ( self , s ) :
  O00oO00oO0O = s . split ( '_' )
  if len ( O00oO00oO0O ) == 2 :
   self . currency = s
   self . quoteCurrency = O00oO00oO0O [ 1 ]
   return self . api ( b'Exchange_SetCurrency' , self . idx , s )
   if 11 - 11: oOO / OooOoo + oOo0O00
 def SetRate ( self , rate = 1.0 ) :
  return self . api ( b'Exchange_SetRate' , self . idx , rate )
  if 79 - 79: I11iiIi11i1I . I1Ii1I1 * iI1iI11Ii111 % I1Ii1I1 / i11
 def GetTrades ( self , symbol = '' ) :
  return Oo0OO0oooOoo0 ( self . api ( b'Exchange_GetTrades' , self . idx , symbol ) , ( 'Id' , 'Time' , 'Price' , 'Amount' , 'Type' ) )
  if 93 - 93: iI1iI11Ii111 + Iii1i . Ii . iI1iI11Ii111 * ooOOO
 def SetData ( self , name , data ) :
  if not isinstance ( data , ii1Ii ) :
   data = json . dumps ( data )
  return int ( self . api ( b'Exchange_SetData' , self . idx , name , data ) )
  if 84 - 84: Ooo0Ooo % i11
 def GetData ( self , name , timeout = 60000 , offset = 0 ) :
  oOO0o00oOooO = self . api ( b'Exchange_GetData' , self . idx , name , int ( timeout ) , int ( offset ) )
  if oOO0o00oOooO is None :
   return None
  return i1iiiIii ( { 'Time' : int ( oOO0o00oOooO [ 'Time' ] ) , 'Data' : json . loads ( oOO0o00oOooO [ 'Data' ] ) if oOO0o00oOooO [ 'Data' ] else None } )
  if 82 - 82: IIiIIiIi11I1
 def GetTickers ( self ) :
  I1II1ii111i = self . api ( b'Exchange_GetTickers' , self . idx )
  if I1II1ii111i is not None :
   for Oo0OOOo0o in I1II1ii111i :
    OOoOo ( Oo0OOOo0o )
  return I1II1ii111i
  if 21 - 21: IIiIIiIi11I1 - I1I - i11 + OooOoo
 def GetMarkets ( self ) :
  return json . loads ( self . api ( b'Exchange_GetMarkets' , self . idx ) )
  if 41 - 41: IiIIii11Ii + OooOoo - I11iiIi11i1I + Oo % i1 + iI1iII1I1I1i
 def GetTicker ( self , symbol = '' ) :
  return OOoOo ( self . api ( b'Exchange_GetTicker' , self . idx , symbol ) )
  if 16 - 16: i1 - Oo / Ii
 def GetFundings ( self , symbol = '' ) :
  return self . api ( b'Exchange_GetFundings' , self . idx , symbol )
  if 38 - 38: Ooo0Ooo % I1Ii1I1 / iI1iI11Ii111 + i1iiIII111
 def IO ( self , k , v = 0 , * more ) :
  if k == 'currency' :
   return self . SetCurrency ( v )
  if k in ( 'isMarketOpen' , 'ismarketopen' ) :
   if 25 - 25: I11iiIi11i1I - iI1iII1I1I1i
   OooO0Ooo0 = ( v , ) + more if ( more or v != 0 ) else ( )
   return i1iiiIii ( self . api ( b'Exchange_IO' , self . idx , k , * OooO0Ooo0 ) )
  return self . api ( b'Exchange_IO' , self . idx , k , int ( v ) )
  if 46 - 46: Ii
 def GetDepth ( self , symbol = '' ) :
  iiiiI1i1iI1 = self . api ( b'Exchange_GetDepth' , self . idx , symbol )
  if iiiiI1i1iI1 is None :
   return None
  O00OO0ooOoO , OOOOO = iiiiI1i1iI1 [ 'Orders' ] , iiiiI1i1iI1 [ 'AsksLen' ]
  return i1iiiIii ( { 'Asks' : O00OO0ooOoO [ : OOOOO ] , 'Bids' : O00OO0ooOoO [ OOOOO : OOOOO + iiiiI1i1iI1 [ 'BidsLen' ] ] } )
  if 94 - 94: IiIIii11Ii - ooo000 . Ii
 def GetRecords ( self , symbol = '' , period = - 1 , limit = 0 ) :
  if isinstance ( symbol , int ) :
   limit = period
   period = symbol
   symbol = ''
  if period == - 1 :
   period = int ( self . period / 1000 )
  IIiI1I1I11 = self . api ( b'Exchange_GetRecords' , self . idx , symbol , int ( period ) )
  if IIiI1I1I11 is None :
   return None
  OooOO00o = '%s/%s/%s/%d' % ( self . currency , symbol , self . ct , period )
  IiiI1III1iI = self . records_cache . get ( OooOO00o , None )
  if IiiI1III1iI is None or len ( IiiI1III1iI ) == 0 :
   if len ( IIiI1I1I11 ) > self . maxBarLen :
    IIiI1I1I11 = IIiI1I1I11 [ len ( IIiI1I1I11 ) - self . maxBarLen : ]
   self . records_cache [ OooOO00o ] = IIiI1I1I11
  else :
   iIIOo00 = 0 if len ( IiiI1III1iI ) == 0 else IiiI1III1iI [ - 1 ] [ 'Time' ]
   for ooI1Ii11iI1 in IIiI1I1I11 :
    Oo0OOOo0o = ooI1Ii11iI1 [ 'Time' ]
    if Oo0OOOo0o == iIIOo00 :
     IiiI1III1iI [ - 1 ] = ooI1Ii11iI1
    elif Oo0OOOo0o > iIIOo00 :
     IiiI1III1iI . append ( ooI1Ii11iI1 )
     if len ( IiiI1III1iI ) > self . maxBarLen :
      IiiI1III1iI . pop ( 0 )
     iIIOo00 = Oo0OOOo0o
  oOO0o00oOooO = OOooo00 ( self . records_cache [ OooOO00o ] )
  if limit > 0 :
   oOO0o00oOooO = OOooo00 ( oOO0o00oOooO [ - limit : ] )
  return oOO0o00oOooO
  if 41 - 41: i11 - oOo0O00
 def GetAssets ( self ) :
  return Oo0OO0oooOoo0 ( self . api ( b'Exchange_GetAssets' , self . idx ) , ( 'Currency' , 'Amount' , 'FrozenAmount' ) )
  if 76 - 76: I11iiIi11i1I % IIiIIiIi11I1 % iI1iI11Ii111
 def GetAccount ( self ) :
  return self . api ( b'Exchange_GetAccount' , self . idx )
  if 39 - 39: IiIIii11Ii . Oo + iI1iI11Ii111 - oOo0O00
 def Buy ( self , price , amount = None , * extra ) :
  return oo0O ( self . api ( b'Exchange_Buy' , self . idx , price , amount , IIIII11 ( IIiiIIi1i ( extra ) ) ) )
  if 93 - 93: Iii1i * IIiIIiIi11I1 % iI1iI11Ii111 + i1 % Ii * iI1iI11Ii111
 def Sell ( self , price , amount = None , * extra ) :
  return oo0O ( self . api ( b'Exchange_Sell' , self . idx , price , amount , IIIII11 ( IIiiIIi1i ( extra ) ) ) )
  if 62 - 62: i11 % ooo000
 def CreateOrder ( self , symbol , side , price , amount = None , * extra ) :
  return oo0O ( self . api ( b'Exchange_CreateOrder' , self . idx , symbol , side , price , amount , IIIII11 ( IIiiIIi1i ( extra ) ) ) )
  if 19 - 19: Ii / Oo % Iii1i / i1iiIII111 - OooOoo - Ooo0Ooo
 def ModifyOrder ( self , orderId , side , price , amount = None , * extra ) :
  return oo0O ( self . api ( b'Exchange_ModifyOrder' , self . idx , orderId , side , price , amount , IIIII11 ( IIiiIIi1i ( extra ) ) ) )
  if 89 - 89: I11iiIi11i1I - i11
 def GetOrders ( self , symbol = '' ) :
  return self . api ( b'Exchange_GetOrders' , self . idx , symbol , False )
  if 61 - 61: Ii * OooOoo * I1I % i1iiIII111 % IIiIIiIi11I1 * I11iiIi11i1I
 def GetHistoryOrders ( self , symbol = '' , since = 0 , limit = 0 ) :
  if isinstance ( symbol , int ) :
   limit = since
   since = symbol
   symbol = ''
  return self . api ( b'Exchange_GetHistoryOrders' , self . idx , symbol , False , since , limit )
  if 49 - 49: iI1iII1I1I1i / i1iiIII111 % oOO
 def GetOrder ( self , orderId ) :
  return self . api ( b'Exchange_GetOrder' , self . idx , orderId , False )
  if 46 - 46: ooOOO * IIiIIiIi11I1 % i1 / oOO + i1 + oOo0O00
 def CancelOrder ( self , orderId , * extra ) :
  return self . api ( b'Exchange_CancelOrder' , self . idx , orderId , False , IIIII11 ( IIiiIIi1i ( extra ) ) ) is True
  if 99 - 99: I1I * IIiIIiIi11I1 * i1iiIII111
  if 62 - 62: ooOOO % Oo + iI1iI11Ii111
 def CreateConditionOrder ( self , symbol , side , amount , condition , * extra ) :
  return oo0O ( self . api ( b'Exchange_CreateConditionOrder' , self . idx , symbol , side , amount , json . dumps ( condition ) , IIIII11 ( IIiiIIi1i ( extra ) ) ) )
  if 87 - 87: ooo000 - OooOoo + Ii + i1i1i1111I + IiIIii11Ii
 def ModifyConditionOrder ( self , orderId , side , amount , condition , * extra ) :
  return oo0O ( self . api ( b'Exchange_ModifyConditionOrder' , self . idx , orderId , side , amount , json . dumps ( condition ) , IIIII11 ( IIiiIIi1i ( extra ) ) ) )
  if 57 - 57: IIiIIiIi11I1 + I1I / ooOOO % ooOOO % Oo / i11
 def GetConditionOrders ( self , symbol = '' ) :
  return self . api ( b'Exchange_GetOrders' , self . idx , symbol , True )
  if 95 - 95: i1 / I11iiIi11i1I . i1 / Oo . Ooo0Ooo
 def GetHistoryConditionOrders ( self , symbol = '' , since = 0 , limit = 0 ) :
  if isinstance ( symbol , int ) :
   limit = since
   since = symbol
   symbol = ''
  return self . api ( b'Exchange_GetHistoryOrders' , self . idx , symbol , True , since , limit )
  if 43 - 43: Oo - OooOoo * oOO . Ooo0Ooo / IIiIIiIi11I1 * IIiIIiIi11I1
 def GetConditionOrder ( self , orderId ) :
  return self . api ( b'Exchange_GetOrder' , self . idx , orderId , True )
  if 84 - 84: i1iiIII111 + oOo0O00
 def CancelConditionOrder ( self , orderId , * extra ) :
  return self . api ( b'Exchange_CancelOrder' , self . idx , orderId , True , IIIII11 ( IIiiIIi1i ( extra ) ) ) is True
  if 83 - 83: i1i1i1111I
 def Log ( self , orderType , price , amount = 0 , * extra ) :
  IiIIIII1i = self . api ( b'Exchange_Log' , self . idx , orderType , price , amount , IIIII11 ( IIiiIIi1i ( extra ) ) )
  if orderType == 2 :
   return bool ( IiIIIII1i )
  if IiIIIII1i > 0 :
   return int ( IiIIIII1i )
   if 84 - 84: oOO / Ii * Ooo0Ooo / Ii / ooo000
 def GetContractType ( self ) :
  return self . ct
  if 64 - 64: oOo0O00 * Ii
 def GetPeriod ( self ) :
  return int ( self . period / 1000 )
  if 2 - 2: i11 % i1iiIII111 . oOo0O00
 def SetContractType ( self , symbol ) :
  oOO0o00oOooO = self . api ( b'Exchange_SetContractType' , self . idx , symbol )
  if oOO0o00oOooO is None :
   return None
  self . ct = symbol
  return json . loads ( oOO0o00oOooO ) if oOO0o00oOooO else True
  if 59 - 59: I11iiIi11i1I % OooOoo - iI1iII1I1I1i % I1I + i1iiIII111 . I1Ii1I1
 def SetMarginLevel ( self , symbol , level = None ) :
  if isinstance ( symbol , int ) or isinstance ( symbol , float ) :
   level , symbol = symbol , level
  if not symbol :
   symbol = ''
  return self . api ( b'Exchange_SetMarginLevel' , self . idx , symbol , level )
  if 94 - 94: ooOOO * I1Ii1I1 * i1iiIII111 . oOo0O00
 def SetDirection ( self , direction ) :
  return self . api ( b'Exchange_SetDirection' , self . idx , direction )
  if 73 - 73: I1Ii1I1 / ooo000 % I11iiIi11i1I - i1i1i1111I + Oo - I1Ii1I1
 def GetPositions ( self , symbol = '' ) :
  return Ii1III1iI ( self . api ( b'Exchange_GetPositions' , self . idx , symbol ) )
  if 18 - 18: i1 + ooOOO . i1 - iI1iII1I1I1i
 def GetPosition ( self ) :
  return self . GetPositions ( )
  if 97 - 97: oOo0O00 + iI1iI11Ii111 % Iii1i
class Ooo0oOOoO000O ( object ) :
 def __init__ ( self , api , js ) :
  self . api = api
  self . api ( b'Chart_New' , json . dumps ( js ) )
  if 89 - 89: oOo0O00
 def update ( self , js ) :
  self . api ( b'Chart_New' , json . dumps ( js ) )
  if 48 - 48: i1 / IIiIIiIi11I1 / iI1iII1I1I1i / i11 * IiIIii11Ii
 def add ( self , seriesIdx , d , replaceId = None ) :
  O0oo00o0O0 = [ seriesIdx , d ]
  if replaceId is not None :
   O0oo00o0O0 . append ( replaceId )
  self . api ( b'Chart_Add' , json . dumps ( O0oo00o0O0 ) )
  if 91 - 91: iI1iI11Ii111 . Ii . oOO
 def reset ( self , keep = 0 ) :
  self . api ( b'Chart_Reset' , keep )
  if 65 - 65: oOO % OooOoo
class IIi1i11Ii1 ( ) :
 def __init__ ( self , api , options = { } ) :
  options [ "__isCandle" ] = True
  self . chart = Ooo0oOOoO000O ( api , options )
  self . bar = None
  self . overlay = options . get ( "overlay" , False )
  self . preTime = 0
  self . runtime = { "plots" : [ ] , "signals" : [ ] , "titles" : { } , "count" : 0 }
  if 58 - 58: iI1iII1I1I1i
 def trim ( self , obj ) :
  I1i1I1I1i = { }
  for OooOO00o in obj :
   if obj [ OooOO00o ] is not None :
    I1i1I1I1i [ OooOO00o ] = obj [ OooOO00o ]
  return I1i1I1I1i
  if 51 - 51: I1I . i1i1i1111I % Ii
 def newPlot ( self , obj ) :
  Oo0ooOoOOoo00 = self . trim ( obj )
  if "overlay" not in Oo0ooOoOOoo00 :
   Oo0ooOoOOoo00 [ "overlay" ] = self . overlay
  if Oo0ooOoOOoo00 [ "type" ] != 'shape' and Oo0ooOoOOoo00 [ "type" ] != 'bgcolor' and Oo0ooOoOOoo00 [ "type" ] != 'barcolor' :
   if "title" not in Oo0ooOoOOoo00 or len ( Oo0ooOoOOoo00 [ "title" ] ) == 0 or Oo0ooOoOOoo00 [ "title" ] in self . runtime [ "titles" ] :
    Oo0ooOoOOoo00 [ "title" ] = '<' + Oo0ooOoOOoo00 . get ( "title" , "plot" ) + '_' + str ( self . runtime [ "count" ] ) + '>'
   self . runtime [ "count" ] += 1
   if "title" in Oo0ooOoOOoo00 :
    self . runtime [ "titles" ] [ Oo0ooOoOOoo00 [ "title" ] ] = True
  return Oo0ooOoOOoo00
  if 83 - 83: ooo000 + ooo000 - i1i1i1111I - oOO
  if 18 - 18: Oo + oOO / I11iiIi11i1I - i1 / Iii1i . oOo0O00
 def begin ( self , bar ) :
  self . bar = bar
  if 60 - 60: oOO * oOO - i1 - iI1iII1I1I1i / OooOoo + ooOOO
 def reset ( self , remain = 0 ) :
  self . chart . reset ( remain )
  self . preTime = 0
  if 25 - 25: Ii . Ooo0Ooo * Iii1i % I1I / Oo . i11
 def close ( self , bar = None ) :
  if bar :
   self . bar = bar
   if 5 - 5: Ii % Ii / iI1iII1I1I1i - i1
  if self . bar [ "Time" ] < self . preTime :
   return
   if 70 - 70: OooOoo . I11iiIi11i1I
  Ii11I = {
 "timestamp" : self . bar [ "Time" ] ,
 "open" : self . bar [ "Open" ] ,
 "high" : self . bar [ "High" ] ,
 "low" : self . bar [ "Low" ] ,
 "close" : self . bar [ "Close" ] ,
 "volume" : self . bar . get ( "Volume" , 0 ) ,
 }
  if 38 - 38: iI1iI11Ii111 * i1iiIII111
  for OooOO00o in [ "plots" , "signals" ] :
   if len ( self . runtime [ OooOO00o ] ) > 0 :
    if "runtime" not in Ii11I :
     Ii11I [ "runtime" ] = { }
    Ii11I [ "runtime" ] [ OooOO00o ] = self . runtime [ OooOO00o ]
    if 74 - 74: i1iiIII111 * oOo0O00 / I11iiIi11i1I / Ooo0Ooo / oOo0O00
  if self . preTime == self . bar [ "Time" ] :
   self . chart . add ( 0 , Ii11I , - 1 )
  else :
   self . chart . add ( 0 , Ii11I )
   if 36 - 36: oOO
  self . preTime = self . bar [ "Time" ]
  self . runtime [ "plots" ] = [ ]
  self . runtime [ "signals" ] = [ ]
  self . runtime [ "titles" ] = { }
  self . runtime [ "count" ] = 0
  if 76 - 76: Ooo0Ooo / IIiIIiIi11I1 % IiIIii11Ii . ooo000 * i1iiIII111 % Ooo0Ooo
 def plot ( self , series = None , title = None , color = None , linewidth = 1 , style = "line" , trackprice = None , histbase = 0 , offset = 0 , join = False , editable = False , show_last = None , display = "all" , overlay = None ) :
  if series is None or self . bar [ "Time" ] < self . preTime :
   return
   if 53 - 53: ooo000 + I1Ii1I1
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
  if 97 - 97: i1 - oOo0O00 / OooOoo * Ii - oOO
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
  if 53 - 53: I11iiIi11i1I % ooo000 / ooOOO / I1I
 def plotarrow ( self , series , title = None , colorup = "#00ff00" ,
 colordown = "#ff0000" ,
 offset = 0 ,
 minheight = 5 ,
 maxheight = 100 ,
 editable = False , show_last = None , display = "all" , overlay = None ) :
  if display != "all" or self . bar [ "Time" ] < self . preTime :
   return
   if 43 - 43: iI1iII1I1I1i . i1i1i1111I + I1I % ooOOO . i11 - i11
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
  if 6 - 6: I1I
 def hline ( self , price , title = None , color = None , linestyle = "dashed" , linewidth = None , editable = False , display = "all" , overlay = None ) :
  if display != "all" or self . bar [ "Time" ] < self . preTime :
   return
   if 98 - 98: oOO * IIiIIiIi11I1 / i1iiIII111 / Iii1i + I1I
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
  if 25 - 25: IIiIIiIi11I1 . i11 / I1I * i1 - i1iiIII111 % oOo0O00
  if 49 - 49: IiIIii11Ii % ooOOO + I11iiIi11i1I + IIiIIiIi11I1
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
  if 60 - 60: IIiIIiIi11I1
  if 98 - 98: IiIIii11Ii / Ooo0Ooo + Ii
 def plotchar ( self , series , title = None , char = None , location = "abovebar" , color = None , offset = None , text = None , textcolor = None , editable = None , size = "auto" , show_last = None , display = "all" , overlay = None ) :
  if ( location != "absolute" and series is None ) or ( location == "absolute" and series is None ) or char is None or self . bar [ "Time" ] < self . preTime :
   return
   if 73 - 73: OooOoo * Iii1i
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
  if 34 - 34: iI1iI11Ii111 % Ooo0Ooo * OooOoo + i1iiIII111 / i1
  if 49 - 49: IIiIIiIi11I1 / i1iiIII111 % IIiIIiIi11I1 + IIiIIiIi11I1 * iI1iII1I1I1i
  if 22 - 22: I1Ii1I1 + oOO / I1Ii1I1 - Ii % Ii % i1i1i1111I
 def plotshape ( self , series , title = None , style = None , location = "abovebar" , color = None , offset = None , text = None , textcolor = None , editable = None , size = "auto" , show_last = None , display = "all" , overlay = None ) :
  if ( location != "absolute" and series is None ) or ( location == "absolute" and series is None ) or self . bar [ "Time" ] < self . preTime :
   return
   if 86 - 86: Iii1i
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
  if 53 - 53: i1 * i1i1i1111I
 def plotcandle ( self , open , high , low , close , title = None , color = None , wickcolor = None , editable = None , show_last = None , bordercolor = None , display = "all" , overlay = None ) :
  if display != "all" or self . bar [ "Time" ] < self . preTime :
   return
   if 91 - 91: I1I . I11iiIi11i1I
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
  if 59 - 59: i11 . i11 * IIiIIiIi11I1
 def fill ( self , plot1 , plot2 , color = None , title = None , editable = None , show_last = None , fillgaps = None , display = "all" ) :
  if self . bar [ "Time" ] < self . preTime :
   return
  if plot1 >= 0 and plot2 >= 0 and plot1 < len ( self . runtime [ "plots" ] ) and plot2 < len ( self . runtime [ "plots" ] ) and display == "all" :
   I1i1I1I1i = self . runtime [ "plots" ] [ plot1 ]
   if "fill" not in I1i1I1I1i :
    I1i1I1I1i [ "fill" ] = [ ]
   I1i1I1I1i [ "fill" ] . append ( self . trim ( {
 "value" : self . runtime [ "plots" ] [ plot2 ] [ "series" ] ,
 "color" : color ,
 "showLast" : show_last
 } ) )
   if 85 - 85: Iii1i . oOO % Iii1i - Iii1i
 def signal ( self , direction , price , qty , id = None ) :
  if self . bar [ "Time" ] < self . preTime :
   return
  O0oo0 = {
 "id" : id or direction ,
 "avgPrice" : price ,
 "qty" : qty
 }
  if direction == "buy" or direction == "long" :
   O0oo0 [ "direction" ] = "long"
  elif direction == "sell" or direction == "short" :
   O0oo0 [ "direction" ] = "short"
  elif direction == "closesell" or direction == "closeshort" :
   O0oo0 [ "direction" ] = "close"
   O0oo0 [ "closeDirection" ] = "short"
  elif direction == "closebuy" or direction == "closelong" :
   O0oo0 [ "direction" ] = "close"
   O0oo0 [ "closeDirection" ] = "long"
   if 20 - 20: i11 / I11iiIi11i1I
  if O0oo0 [ "direction" ] or O0oo0 [ "closeDirection" ] :
   self . runtime [ "signals" ] . append ( O0oo0 )
   if 33 - 33: ooo000 + IiIIii11Ii . ooo000
def ooO0o00ooOOO0 ( s , default ) :
 oo0ooOO0O0o0 = default
 if len ( s ) < 2 :
  return oo0ooOO0O0o0
 I11iIi1i = int ( s [ : - 1 ] )
 IiiI1III1iI = s [ - 1 ]
 if IiiI1III1iI == 'd' :
  oo0ooOO0O0o0 = I11iIi1i * 60000 * 60 * 24
 elif IiiI1III1iI == 'm' :
  oo0ooOO0O0o0 = I11iIi1i * 60000
 elif IiiI1III1iI == 'm' :
  oo0ooOO0O0o0 = I11iIi1i * 60000
 return oo0ooOO0O0o0
 if 6 - 6: iI1iI11Ii111 / IIiIIiIi11I1
def o0O ( s ) :
 iii1i1I = s
 I1i1O0o00o00 = { }
 for oOo in iii1i1I . split ( '\n' ) :
  oOo = oOo . strip ( )
  if ':' not in oOo :
   continue
  O00oO00oO0O = oOo . split ( ':' , 1 )
  if len ( O00oO00oO0O ) == 2 :
   OooOO00o = O00oO00oO0O [ 0 ] . strip ( )
   I1II1ii111i = O00oO00oO0O [ 1 ] . strip ( )
   I1i1O0o00o00 [ OooOO00o ] = I1II1ii111i
 I11IIi1IIIi = I1i1O0o00o00 . get ( 'pnl' , 'true' )
 Oo000Oo0 = I1i1O0o00o00 . get ( 'dataServer' , i1ii1 )
 oo0ooOO0O0o0 = ooO0o00ooOOO0 ( I1i1O0o00o00 . get ( 'period' , '1h' ) , 60000 * 60 )
 oooOoO00o0OOO = ooO0o00ooOOO0 ( I1i1O0o00o00 . get ( 'basePeriod' , '' ) , 0 )
 if 14 - 14: Iii1i
 OOooooO = [ ]
 for iIiO000O0Oo0 in json . loads ( I1i1O0o00o00 . get ( 'exchanges' , '[]' ) ) :
  O00oO00oO0O = iIiO000O0Oo0 [ 'currency' ] . upper ( ) . split ( '_' )
  if len ( O00oO00oO0O ) == 1 :
   O00oO00oO0O . append ( 'CNY' if 'CTP' in iIiO000O0Oo0 [ 'eid' ] else 'USD' )
  if oooOoO00o0OOO == 0 :
   oooOoO00o0OOO = 60000 * 60
   if oo0ooOO0O0o0 == 86400000 :
    oooOoO00o0OOO = 60000 * 60
   elif oo0ooOO0O0o0 == 3600000 :
    oooOoO00o0OOO = 60000 * 30
   elif oo0ooOO0O0o0 == 1800000 :
    oooOoO00o0OOO = 60000 * 15
   elif oo0ooOO0O0o0 == 900000 :
    oooOoO00o0OOO = 60000 * 5
   elif oo0ooOO0O0o0 == 300000 :
    oooOoO00o0OOO = 60000
  Ooo = {
 'Huobi' : [ 150 , 200 ] ,
 'OKX' : [ 150 , 200 ] ,
 'Binance' : [ 150 , 200 ] ,
 'Futures_BitMEX' : [ 8 , 10 ] ,
 'Futures_OKX' : [ 30 , 30 ] ,
 'Futures_HuobiDM' : [ 30 , 30 ] ,
 'Futures_CTP' : [ 25 , 25 ] ,
 'Futures_XTP' : [ 30 , 130 ] ,
 }
  if iIiO000O0Oo0 [ 'eid' ] == "Futures_CTP" :
   Oo000Oo0 = "http://q.youquant.com"
   if 46 - 46: i11 . i1iiIII111 % Iii1i - Ooo0Ooo + ooo000
  i1i1IiiIIII = iIiO000O0Oo0 . get ( 'fee' )
  if i1i1IiiIIII is None :
   i1i1IiiIIII = Ooo . get ( iIiO000O0Oo0 [ 'eid' ] , [ 2000 , 2000 ] )
  else :
   i1i1IiiIIII = [ int ( i1i1IiiIIII [ 0 ] * 10000 ) , int ( i1i1IiiIIII [ 1 ] * 10000 ) ]
   if 19 - 19: I1Ii1I1
  OOOoOOo0 = {
 "Balance" : iIiO000O0Oo0 . get ( 'balance' , 10000.0 ) ,
 "Stocks" : iIiO000O0Oo0 . get ( 'stocks' , 3.0 ) ,
 "BaseCurrency" : O00oO00oO0O [ 0 ] ,
 "QuoteCurrency" : O00oO00oO0O [ 1 ] ,
 "BasePeriod" : oooOoO00o0OOO ,
 "FeeDenominator" : 6 ,
 "FeeMaker" : i1i1IiiIIII [ 0 ] ,
 "FeeTaker" : i1i1IiiIIII [ 1 ] ,
 "FeeMin" : iIiO000O0Oo0 . get ( 'feeMin' , 0 ) ,
 "Id" : iIiO000O0Oo0 [ 'eid' ] ,
 "Label" : iIiO000O0Oo0 [ 'eid' ]
 }
  OOooooO . append ( OOOoOOo0 )
  if 81 - 81: i11 % iI1iII1I1I1i / OooOoo . oOo0O00
 I1IIIII = {
 "DataServer" : Oo000Oo0 ,
 "MaxChartLogs" : 800 ,
 "MaxProfitLogs" : 800 ,
 "MaxRuntimeLogs" : 800 ,
 "NetDelay" : 200 ,
 "Period" : oo0ooOO0O0o0 ,
 "RetFlags" : iiI1111IIi1 | OoO | iIIiiIi1Ii1I | ii1IiIiiII | iii11i | I1I111i11I ,
 "TimeBegin" : int ( time . mktime ( datetime . datetime . strptime ( I1i1O0o00o00 . get ( 'start' , '2019-02-01 00:00:00' ) , "%Y-%m-%d %H:%M:%S" ) . timetuple ( ) ) ) ,
 "TimeEnd" : int ( time . mktime ( datetime . datetime . strptime ( I1i1O0o00o00 . get ( 'end' , '2019-02-10 00:00:00' ) , "%Y-%m-%d %H:%M:%S" ) . timetuple ( ) ) ) ,
 "UpdatePeriod" : 5000
 }
 I11iIIi = 86400
 O000O0 = I1IIIII [ 'TimeEnd' ] - I1IIIII [ 'TimeBegin' ]
 if O000O0 / 3600 <= 2 :
  I11iIIi = 60
 elif O000O0 / 86400 <= 2 :
  I11iIIi = 300
 elif O000O0 / 86400 < 30 :
  I11iIIi = 3600
 I1IIIII [ 'SnapshotPeriod' ] = I11iIIi * 1000
 if I11IIi1IIIi == 'true' :
  I1IIIII [ 'RetFlags' ] |= oo0
 return { 'Exchanges' : OOooooO , 'Options' : I1IIIII }
 if 32 - 32: ooOOO - IiIIii11Ii - Oo
class i1i1I1iII1iI ( ) :
 pass
 if 87 - 87: oOo0O00 / ooOOO / OooOoo * Ooo0Ooo
class o0O0O000O ( object ) :
 def __init__ ( self , task = None , autoRun = False , gApis = None , progressCallback = None ) :
  self . _joinResult = None
  self . gs = threading . Lock ( )
  if gApis is None :
   if __name__ == "__main__" :
    gApis = globals ( )
   else :
    gApis = dict ( inspect . getmembers ( inspect . stack ( ) [ 1 ] [ 0 ] ) ) [ "f_globals" ]
    if 70 - 70: IiIIii11Ii
  if task is None :
   task = o0O ( gApis [ '__doc__' ] )
  elif hasattr ( task , 'upper' ) :
   task = o0O ( task )
   if 90 - 90: i1i1i1111I % i1 . IiIIii11Ii * i11 / Ii
  if progressCallback is not None :
   self . progressCallback = progressCallback
   if 73 - 73: ooo000 * Ooo0Ooo + Iii1i . ooOOO . I11iiIi11i1I / I11iiIi11i1I
  self . httpGetPtr = ctypes . CFUNCTYPE ( ctypes . c_int , ctypes . c_char_p , ctypes . POINTER ( ctypes . c_char_p ) , ctypes . POINTER ( ctypes . c_int ) , ctypes . POINTER ( ctypes . c_int ) ) ( self . httpGetCallback )
  self . progessCallbackPtr = ctypes . CFUNCTYPE ( None , ctypes . c_char_p ) ( self . progressCallback )
  III1111 = platform . system ( )
  II = platform . architecture ( ) [ 0 ]
  if 14 - 14: i1i1i1111I - OooOoo . IiIIii11Ii
  Oo0OOOoO0 = platform . machine ( ) . lower ( )
  if platform . processor ( ) == "arm" or Oo0OOOoO0 . startswith ( "arm" ) or Oo0OOOoO0 . startswith ( "aarch" ) :
   II = 'arm64' if II == '64bit' else 'arm'
  self . os = '%s/%s' % ( III1111 . lower ( ) , II )
  OOoi1i1i1i = 'backtest_py_%s_%s.so' % ( III1111 . lower ( ) , II )
  i1IIiI1 = 'md5.json'
  i1IIi11iI1II = os . path . join ( "./depends" , OOoi1i1i1i )
  if not os . path . exists ( i1IIi11iI1II ) :
   iI1i1 = { }
   II1III1I1i = iIi1I1I ( )
   iIiIiI1 = os . path . join ( II1III1I1i , i1IIiI1 )
   if os . path . exists ( iIiIiI1 ) :
    OO0O0oOOO0o = open ( iIiIiI1 , 'rb' ) . read ( )
    if ii1Iii ( ) is None or "0fbd04c90e587d6334aacbc4500752d3" in str ( OO0O0oOOO0o ) :
     iI1i1 = Iii11iiiiI ( OO0O0oOOO0o )
   i1IIi11iI1II = os . path . join ( II1III1I1i , OOoi1i1i1i )
   ooOooOooO0o0 = False
   if not os . path . exists ( i1IIi11iI1II ) :
    ooOooOooO0o0 = True
   else :
    Oo0OOoO0000 = md5 . md5 ( open ( i1IIi11iI1II , 'rb' ) . read ( ) ) . hexdigest ( )
    if Oo0OOoO0000 != iI1i1 . get ( OOoi1i1i1i , None ) :
     ooOooOooO0o0 = True
     iIiiII1iI = os . path . join ( II1III1I1i , Oo0OOoO0000 )
     try :
      os . rename ( i1IIi11iI1II , iIiiII1iI )
      os . remove ( iIiiII1iI )
     except :
      pass
   if ooOooOooO0o0 :
    oo0o0oO ( i1IIi11iI1II , ii ( task [ "Options" ] [ "DataServer" ] + "/dist/depends/" + OOoi1i1i1i ) )
    oo0o0oO ( iIiIiI1 , ii ( task [ "Options" ] [ "DataServer" ] + "/dist/depends/" + i1IIiI1 ) )
  else :
   print ( "load from debug mode" , i1IIi11iI1II )
  IiI1 = ctypes . CDLL ( os . path . abspath ( i1IIi11iI1II ) )
  IiI1 . api_backtest . restype = ctypes . c_void_p
  OOO0OOoo0ooO = ctypes . c_void_p ( IiI1 . api_backtest ( Iio0 ( json . dumps ( task ) ) , self . httpGetPtr , self . progessCallbackPtr , None ) )
  if not OOO0OOoo0ooO :
   raise 'Initialize backtest engine error'
  self . ctx = OOO0OOoo0ooO
  self . lib = IiI1
  self . api = Ooooo ( IiI1 , OOO0OOoo0ooO )
  self . cache = { }
  self . kvdb = { }
  self . cRetryDelay = 3000
  if 5 - 5: oOO / I1Ii1I1 + iI1iII1I1I1i
  OOooooO = [ ]
  I11i = 0
  for ooI1Ii11iI1 in task [ "Exchanges" ] :
   OOooooO . append ( IiiI1II ( self . api , I11i , task [ "Options" ] , ooI1Ii11iI1 ) )
   I11i += 1
   if 73 - 73: oOO - Oo % Oo % oOO + oOO + Ii
  for OooOO00o in dir ( self ) :
   if OooOO00o . startswith ( 'g_' ) :
    gApis [ OooOO00o [ 2 : ] ] = getattr ( self , OooOO00o )
    if 98 - 98: oOO - Ooo0Ooo / i1 . Ii + ooOOO - IiIIii11Ii
  self . realTime = time . time
  time . time = self . g_PyTime
  gApis [ '__name__' ] = '__main__'
  gApis [ "TA" ] = iiIi111iii1II ( self . _logTA )
  gApis [ 'exchanges' ] = OOooooO
  gApis [ 'exchange' ] = OOooooO [ 0 ]
  gApis [ 'ext' ] = i1i1I1iII1iI ( )
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
  if 12 - 12: i1 . iI1iI11Ii111 / IiIIii11Ii * i11
  gApis [ "ORDER_CONDITION_TYPE_OCO" ] = 0
  gApis [ "ORDER_CONDITION_TYPE_TP" ] = 1
  gApis [ "ORDER_CONDITION_TYPE_SL" ] = 2
  gApis [ "ORDER_CONDITION_TYPE_GENERIC" ] = 3
  if 81 - 81: i11 / I1I / Ii / iI1iI11Ii111
  gApis [ "PD_LONG" ] = 0
  gApis [ "PD_SHORT" ] = 1
  gApis [ "PD_LONG_YD" ] = 2
  gApis [ "PD_SHORT_YD" ] = 3
  if 45 - 45: i11 + I1Ii1I1 % oOo0O00 + iI1iI11Ii111 + ooOOO
  gApis [ "LOG_TYPE_BUY" ] = 0
  gApis [ "LOG_TYPE_SELL" ] = 1
  gApis [ "LOG_TYPE_CANCEL" ] = 2
  gApis [ "LOG_TYPE_ERROR" ] = 3
  gApis [ "LOG_TYPE_PROFIT" ] = 4
  gApis [ "LOG_TYPE_LOG" ] = 5
  gApis [ "LOG_TYPE_RESTART" ] = 6
  if 66 - 66: OooOoo . Ii - OooOoo + OooOoo * OooOoo / i1iiIII111
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
  if 32 - 32: IIiIIiIi11I1 - iI1iI11Ii111 / ooOOO * Ooo0Ooo * iI1iII1I1I1i - i1i1i1111I
  if autoRun :
   try :
    gApis [ 'main' ] ( )
   except EOFError :
    pass
   self . Join ( )
   if 82 - 82: ooo000
 def httpGetCallback ( self , path , ptr_buf , ptr_size , ptr_need_free ) :
  if 66 - 66: IiIIii11Ii + IIiIIiIi11I1 - iI1iI11Ii111 + i1i1i1111I . iI1iII1I1I1i * IiIIii11Ii
  IIiII = path . decode ( 'utf8' )
  O00o0OO = None
  if '\n' in IIiII :
   IIiII , O00o0OO = IIiII . split ( '\n' , 1 )
  i1I = None if O00o0OO is not None else iIi1I1I ( ) + '/http_' + md5 . md5 ( path ) . hexdigest ( )
  Ii11I = None
  try :
   if i1I and os . path . exists ( i1I ) :
    Ii11I = open ( i1I , 'rb' ) . read ( )
   else :
    Ii11I = ii ( IIiII , O00o0OO )
    if i1I and len ( Ii11I ) > 0 :
     oo0o0oO ( i1I , Ii11I )
  except urllib2 . HTTPError as iIiO000O0Oo0 :
   if 3 - 3: I1Ii1I1
   if iIiO000O0Oo0 . code not in ( 502 , 503 , 504 ) :
    Ii11I = oOoO00 ( iIiO000O0Oo0 )
   else :
    Ii11I = None
    OOiIiIi1IIiI11 = 'HTTP %d' % iIiO000O0Oo0 . code
  except Exception as iIiO000O0Oo0 :
   Ii11I = None
   OOiIiIi1IIiI11 = str ( iIiO000O0Oo0 )
  if Ii11I is None :
   if 22 - 22: ooo000
   o0o0oooO = ctypes . create_string_buffer ( OOiIiIi1IIiI11 . encode ( 'utf-8' , 'replace' ) )
   ptr_size . contents . value = len ( o0o0oooO . value )
   ptr_need_free . contents . value = 0
   ptr_buf . contents . value = ctypes . addressof ( o0o0oooO )
   self . cache = { 0 : o0o0oooO }
   return 1
  ptr_size . contents . value = len ( Ii11I )
  ptr_need_free . contents . value = 0
  ii11Iii1IiI = ctypes . create_string_buffer ( Ii11I )
  ptr_buf . contents . value = ctypes . addressof ( ii11Iii1IiI )
  if 89 - 89: i1i1i1111I - i1
  self . cache = { 0 : ii11Iii1IiI }
  return 0
  if 50 - 50: Oo
 def progressCallback ( self , st ) :
  pass
  if 14 - 14: oOo0O00 + ooo000 / OooOoo
 def _logTA ( self , name , args ) :
  self . api ( b'LogTA' , IIIII11 ( name ) , IIIII11 ( args ) )
  if 83 - 83: i1i1i1111I / iI1iI11Ii111 % i11 . I1Ii1I1 * IiIIii11Ii - I1I
 def g_Unix ( self ) :
  return self . api ( b'Unix' )
  if 81 - 81: Ooo0Ooo / iI1iII1I1I1i % i1i1i1111I / OooOoo . iI1iI11Ii111 . ooo000
 def g_UnixNano ( self ) :
  return self . api ( b'UnixNano' )
  if 45 - 45: OooOoo + ooOOO / i1i1i1111I * i1
 def g_PyTime ( self ) :
  return float ( self . g_UnixNano ( ) ) / 1e9
  if 71 - 71: i11 % Iii1i + oOo0O00 * I11iiIi11i1I / i11
 def g_Sleep ( self , n ) :
  self . api ( b'Sleep' , n )
  if 66 - 66: ooo000 * oOo0O00
 def g_EnableLog ( self , flag = True ) :
  self . api ( b'EnableLog' , bool ( flag ) )
  if 83 - 83: i1
 def g_Log ( self , * extra ) :
  self . api ( b'Log' , IIIII11 ( IIiiIIi1i ( extra ) ) )
  if 64 - 64: i1 . i11 - I11iiIi11i1I . Iii1i
 def g_LogReset ( self , keep = 0 ) :
  self . api ( b'LogReset' , keep )
  if 47 - 47: ooo000 / Ooo0Ooo % IiIIii11Ii
 def g_LogVacuum ( self ) :
  pass
  if 70 - 70: IIiIIiIi11I1 / Iii1i . i1i1i1111I % ooOOO . Ii / Ii
 def g_LogStatus ( self , * extra ) :
  self . api ( b'LogStatus' , IIIII11 ( IIiiIIi1i ( extra , status = True ) ) )
  if 51 - 51: I11iiIi11i1I + Ooo0Ooo - ooo000 * oOO . oOO
 def g_LogProfit ( self , profit , * extra ) :
  self . api ( b'LogProfit' , profit , IIIII11 ( IIiiIIi1i ( extra ) ) )
  if 79 - 79: i1i1i1111I + oOo0O00
 def g_LogProfitReset ( self , keep = 0 ) :
  self . api ( b'LogProfitReset' , keep )
  if 11 - 11: OooOoo / i1iiIII111 % iI1iI11Ii111 - i1i1i1111I * oOo0O00
 def g_LogError ( self , * extra ) :
  self . api ( b'LogError' , IIIII11 ( IIiiIIi1i ( extra ) ) )
  if 90 - 90: i1 * i1 . Ooo0Ooo . Oo
 def g_Panic ( self , * extra ) :
  self . api ( b'LogError' , IIIII11 ( IIiiIIi1i ( extra ) ) )
  raise EOFError ( )
  if 59 - 59: Ii % I1Ii1I1 + Iii1i . OooOoo * Iii1i
 def g_GetLastError ( self ) :
  return ''
  if 21 - 21: I11iiIi11i1I + ooOOO % IiIIii11Ii / OooOoo
 def g_MD5 ( self , s ) :
  return md5 . md5 ( Iio0 ( s ) ) . hexdigest ( )
  if 96 - 96: Oo * i1iiIII111 . Ooo0Ooo
 def g_HttpQuery ( self , url , options = None ) :
  if 35 - 35: ooOOO . iI1iI11Ii111 * i1i1i1111I * iI1iII1I1I1i - I11iiIi11i1I
  if 47 - 47: IIiIIiIi11I1
  if isinstance ( options , str ) and options :
   options = { 'method' : 'POST' , 'body' : options }
  IiIIIII1i = self . api ( b'HttpQuery' , url , json . dumps ( options ) if isinstance ( options , dict ) else '' )
  if isinstance ( options , dict ) and options . get ( 'debug' ) :
   O0oo00o0O0 = json . loads ( IiIIIII1i )
   O00o0OO = O0oo00o0O0 . get ( 'body' )
   IiIIIII1i = i1iiiIii ( { 'StatusCode' : O0oo00o0O0 . get ( 'status' ) , 'Length' : len ( O00o0OO ) if O00o0OO else 0 , 'Body' : O00o0OO ,
 'Header' : { k : [ v ] for k , v in ( O0oo00o0O0 . get ( 'headers' ) or { } ) . items ( ) } } )
  return IiIIIII1i
  if 73 - 73: I1Ii1I1 + ooOOO
 def g_HttpQuery_Go ( self , * args ) :
  return OOOo0oOOo0 ( self . g_HttpQuery ( * args ) )
  if 99 - 99: iI1iI11Ii111
 def g_JSONParse ( self , s ) :
  return json . loads ( s )
  if 87 - 87: i1 . I11iiIi11i1I * Ii . i1 . IIiIIiIi11I1 . IiIIii11Ii
 def g_UUID ( self ) :
  return uuid . uuid4 ( ) . hex . upper ( )
  if 50 - 50: Ii / oOO
 def g_StrDecode ( self , s , c = 'gbk' ) :
  self . g_LogError ( "sandbox not support StrDecode" )
  if 92 - 92: Ooo0Ooo * i1iiIII111 / Ooo0Ooo / i1iiIII111 * i1i1i1111I + iI1iI11Ii111
 def g_EnableLogLocal ( self , b ) :
  pass
  if 48 - 48: I11iiIi11i1I
 def g_Dial ( self , * args ) :
  self . g_LogError ( "sandbox not support Dial" )
  if 87 - 87: I1Ii1I1
 def g_DBExec ( self , * args ) :
  self . g_LogError ( "sandbox not support DBExec" )
  if 29 - 29: ooo000 . iI1iII1I1I1i . oOo0O00 + i1i1i1111I + oOO
 def g_Encode ( self , * args ) :
  self . g_LogError ( "sandbox not support Encode" )
  if 59 - 59: IiIIii11Ii
 def g_EventLoop ( self , * args ) :
  self . g_LogError ( "sandbox not support EventLoop" )
  if 26 - 26: oOo0O00 % i11 * i1
 def g_Mail ( self , smtpServer = '' , smtpUsername = '' , smtpPassword = '' , mailTo = '' , title = '' , body = '' ) :
  if 60 - 60: IIiIIiIi11I1 % oOO / i1
  return self . api ( b'Mail' , smtpServer , smtpUsername , smtpPassword , mailTo , title , body )
  if 20 - 20: Ooo0Ooo
 def g_Mail_Go ( self , * args ) :
  return OOOo0oOOo0 ( self . g_Mail ( * args ) )
  if 4 - 4: IiIIii11Ii % Iii1i
 def g_GetCommand ( self ) :
  if 43 - 43: ooo000
  return None
  if 95 - 95: Oo + I11iiIi11i1I / Ooo0Ooo / Ii - ooOOO / i1i1i1111I
 def g_GetMeta ( self ) :
  return None
  if 6 - 6: Ooo0Ooo % IiIIii11Ii
 def g_SetErrorFilter ( self , s ) :
  pass
  if 59 - 59: iI1iI11Ii111 . I11iiIi11i1I . ooo000 / iI1iI11Ii111 . Ii % Ooo0Ooo
 def g_SetChannelData ( self , s ) :
  pass
  if 85 - 85: oOo0O00 / ooOOO
 def g_GetChannelData ( self , s = '' ) :
  return ''
  if 41 - 41: i1iiIII111 * iI1iII1I1I1i + i1 + i1i1i1111I
 def g_GetOS ( self ) :
  return self . os
  if 26 - 26: Oo % OooOoo
 def g_Version ( self , detail = False ) :
  return self . api ( b'Version' , bool ( detail ) )
  if 14 - 14: iI1iII1I1I1i - i1iiIII111
 def g_IsVirtual ( self ) :
  return True
  if 53 - 53: oOO
 def g_Chart ( self , js ) :
  return Ooo0oOOoO000O ( self . api , js )
  if 46 - 46: oOo0O00 - iI1iII1I1I1i
 def g_KLineChart ( self , js = { } ) :
  return IIi1i11Ii1 ( self . api , js )
  if 34 - 34: i1i1i1111I
 def g_GetPid ( self ) :
  return os . getpid ( )
  if 21 - 21: i11 + I1I . OooOoo + i1 . ooo000 + I11iiIi11i1I
 def g__Cross ( self , arr1 , arr2 ) :
  if len ( arr1 ) != len ( arr2 ) :
   raise Exception ( "cross array length not equal" )
  OOOOO = 0
  for I11i in range ( len ( arr1 ) - 1 , - 1 , - 1 ) :
   if arr1 [ I11i ] is None or arr2 [ I11i ] is None :
    break
   if arr1 [ I11i ] < arr2 [ I11i ] :
    if OOOOO > 0 :
     break
    OOOOO -= 1
   elif arr1 [ I11i ] > arr2 [ I11i ] :
    if OOOOO < 0 :
     break
    OOOOO += 1
   else :
    break
  return OOOOO
  if 7 - 7: ooOOO + Iii1i / iI1iII1I1I1i - oOO % Oo / iI1iII1I1I1i
 def g__G ( self , k = '__wtf__' , v = '__wtf__' ) :
  if k == '__wtf__' :
   return 1
  elif k is None :
   self . kvdb = { }
  else :
   k = k . lower ( )
   if v is None :
    self . kvdb . pop ( k , None )
   elif v == '__wtf__' :
    return self . kvdb . get ( k , None )
   elif v is not None :
    self . kvdb [ k ] = v
    if 14 - 14: Iii1i . Ii
 def g__CDelay ( self , d ) :
  if d > 0 :
   self . cRetryDelay = d
   if 100 - 100: I1I / ooo000
 def g__C ( self , pfn , * arg ) :
  while True :
   IiIIIII1i = pfn ( * arg )
   if IiIIIII1i == False or IiIIIII1i is None :
    self . g_Sleep ( self . cRetryDelay )
   else :
    return IiIIIII1i
 def g__D ( self , date = None , fmt = None ) :
  if date is None :
   date = self . g_Unix ( )
  if fmt is None :
   fmt = '%Y-%m-%d %H:%M:%S'
  return time . strftime ( fmt , time . localtime ( date ) )
  if 48 - 48: i1i1i1111I * iI1iI11Ii111 % i1i1i1111I + i1i1i1111I . iI1iII1I1I1i / OooOoo
 def g__T ( self , a , b = None ) :
  oOO0o00oOooO = str ( a )
  if b is not None :
   oOO0o00oOooO = str ( a ) + '|' + str ( b )
  return '[trans]' + oOO0o00oOooO + '[/trans]'
  if 12 - 12: Ii . Ii - I1Ii1I1
 def g__N ( self , n , precision = 4 ) :
  if precision < 0 :
   OoO0OoOoo = 10 ** - precision
   return n - ( n % OoO0OoOoo )
  else :
   Ooo000o0O = 1 / ( 10 ** ( max ( 10 , precision + 5 ) ) )
   return int ( ( n + Ooo000o0O ) * ( 10 ** precision ) ) / ( 10 ** precision )
   if 64 - 64: IIiIIiIi11I1 % i1i1i1111I . ooo000 + OooOoo
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
   if 54 - 54: I11iiIi11i1I * i1
   if 81 - 81: ooo000 . IiIIii11Ii * oOO - IiIIii11Ii - iI1iI11Ii111
  def OooO0o ( self ) :
   try :
    Ii11I = json . loads ( self . Join ( ) . decode ( 'utf-8' ) )
   except :
    return
   I1i1O0o00o00 = { }
   I1i1O0o00o00 [ 'timeStamp' ] = [ ]
   I1i1O0o00o00 [ 'assets' ] = [ ]
   I1i1O0o00o00 [ 'surplus' ] = [ ]
   I1i1O0o00o00 [ 'loss' ] = [ ]
   I1i1O0o00o00 [ 'moneyUse' ] = [ ]
   I1i1O0o00o00 [ 'unit' ] = ''
   IIooo0 = 0
   for I11i in Ii11I [ 'Snapshots' ] :
    if not I11i [ 1 ] :
     continue
    I1ii1IIiii = 0
    Oo00O00o0oO = 0
    for oOoOO0O0 in range ( 0 , len ( I11i [ 1 ] ) ) :
     o00oiIIIiII1 = I11i [ 1 ] [ oOoOO0O0 ]
     ooooo0oo0 = Ii11I [ 'Task' ] [ 'Exchanges' ] [ oOoOO0O0 ]
     o0ooO0o = o00oiIIIiII1 [ 'Symbols' ]
     if o0ooO0o :
      ooiIiI11I1iI = 0
      Oo0O = 0
      O000 = 0
      o0oOO00Ooo0o = 0
      for o0O0 in o0ooO0o :
       if 'Long' in o0ooO0o [ o0O0 ] :
        iiI1iiIIi = o0ooO0o [ o0O0 ] [ 'Long' ]
        ooiIiI11I1iI += iiI1iiIIi [ 'Margin' ]
        Oo0O += iiI1iiIIi [ 'Profit' ]
       if 'Short' in o0ooO0o [ o0O0 ] :
        IiIii1iII = o0ooO0o [ o0O0 ] [ 'Short' ]
        ooiIiI11I1iI += IiIii1iII [ 'Margin' ]
        Oo0O += IiIii1iII [ 'Profit' ]
       if 'Stocks' in o0ooO0o [ o0O0 ] :
        O000 += ( o0ooO0o [ o0O0 ] [ 'Stocks' ] + o0ooO0o [ o0O0 ] [ 'FrozenStocks' ] ) * o0ooO0o [ o0O0 ] [ 'Last' ]
        o0oOO00Ooo0o += ( o0ooO0o [ o0O0 ] [ 'Stocks' ] + o0ooO0o [ o0O0 ] [ 'FrozenStocks' ] - ooooo0oo0 [ 'Stocks' ] ) * o0ooO0o [ o0O0 ] [ 'Last' ]
        if 14 - 14: Ii . iI1iII1I1I1i - Ooo0Ooo * Ooo0Ooo / ooo000 - IiIIii11Ii
      for o000ooOoo in o00oiIIIiII1 [ 'Assets' ] :
       if o00oiIIIiII1 [ 'QuoteCurrency' ] == 'CNY' :
        I1ii1IIiii += o000ooOoo [ 'Amount' ] + o000ooOoo [ 'FrozenAmount' ] + Oo0O + ooiIiI11I1iI
        I1i1O0o00o00 [ 'unit' ] = '(CNY)'
       elif 'Futures_' in o00oiIIIiII1 [ 'Id' ] :
        if o00oiIIIiII1 [ 'QuoteCurrency' ] == 'USDT' :
         I1ii1IIiii += o000ooOoo [ 'Amount' ] + o000ooOoo [ 'FrozenAmount' ] + Oo0O + ooiIiI11I1iI
         I1i1O0o00o00 [ 'unit' ] = '(USDT)'
        else :
         I1ii1IIiii += o000ooOoo [ 'Amount' ] + o000ooOoo [ 'FrozenAmount' ] + Oo0O + ooiIiI11I1iI
         I1i1O0o00o00 [ 'unit' ] = '(%s)' % ( o00oiIIIiII1 [ "BaseCurrency" ] , )
       else :
        I1ii1IIiii += o000ooOoo [ 'Amount' ] + o000ooOoo [ 'FrozenAmount' ] + O000
        ooiIiI11I1iI = abs ( o0oOO00Ooo0o )
        I1i1O0o00o00 [ 'unit' ] = '(USD)'
       Oo00O00o0oO += ooiIiI11I1iI / I1ii1IIiii if I1ii1IIiii != 0 else 0
    I1i1O0o00o00 [ 'timeStamp' ] . append ( datetime . datetime . fromtimestamp ( I11i [ 0 ] / 1000 ) . date ( ) )
    I1i1O0o00o00 [ 'assets' ] . append ( I1ii1IIiii )
    I1i1O0o00o00 [ 'moneyUse' ] . append ( Oo00O00o0oO )
    if IIooo0 != 0 :
     oOooOoO = I1ii1IIiii - IIooo0
     if oOooOoO > 0 :
      I1i1O0o00o00 [ 'surplus' ] . append ( oOooOoO )
      I1i1O0o00o00 [ 'loss' ] . append ( 0 )
     elif oOooOoO < 0 :
      I1i1O0o00o00 [ 'surplus' ] . append ( 0 )
      I1i1O0o00o00 [ 'loss' ] . append ( oOooOoO )
     else :
      I1i1O0o00o00 [ 'surplus' ] . append ( 0 )
      I1i1O0o00o00 [ 'loss' ] . append ( 0 )
    else :
     I1i1O0o00o00 [ 'surplus' ] . append ( 0 )
     I1i1O0o00o00 [ 'loss' ] . append ( 0 )
    IIooo0 = I1ii1IIiii
   return I1i1O0o00o00
   if 21 - 21: oOO . i1iiIII111 . i11 % Iii1i - I1Ii1I1 - i11
   if 56 - 56: Oo . i1iiIII111
  plt . rcParams [ 'axes.unicode_minus' ] = False
  if 27 - 27: oOO - oOO
  if 34 - 34: oOo0O00 + Oo / ooo000 . oOO % OooOoo - Ii
  Ii11I = OooO0o ( self )
  if Ii11I :
   ooO000Oo = Ii11I [ 'timeStamp' ]
   I1ii1IIiii = Ii11I [ 'assets' ]
   ii1IioOOO0O = Ii11I [ 'surplus' ]
   IIII = Ii11I [ 'loss' ]
   Oo00O00o0oO = Ii11I [ 'moneyUse' ]
   IIOoO0oo = Ii11I [ 'unit' ]
   if 97 - 97: Oo * IiIIii11Ii . Ooo0Ooo % i1 % Ii % ooo000
   plt . figure ( figsize = ( 14 , 8 ) )
   plt . subplots_adjust ( left = 0.090 , right = 0.930 )
   plt . subplots_adjust ( hspace = 0 , wspace = 0 )
   OoOOoO0o000 = plt . subplot ( 311 )
   plt . title ( u'Backtest' , fontsize = 18 )
   plt . grid ( linestyle = '--' , color = '#D9D9D9' )
   plt . plot ( ooO000Oo , I1ii1IIiii , color = '#3A859E' , label = u'Equity %s %f' % ( IIOoO0oo , I1ii1IIiii [ - 1 ] ) )
   plt . fill_between ( ooO000Oo , min ( I1ii1IIiii ) , I1ii1IIiii , color = '#D0DBE8' , alpha = .5 )
   plt . legend ( loc = 'upper left' )
   OoOOoO0o000 = plt . subplot ( 312 )
   plt . grid ( linestyle = '--' , color = '#D9D9D9' )
   plt . bar ( ooO000Oo , ii1IioOOO0O , color = 'r' )
   plt . bar ( ooO000Oo , IIII , color = 'g' )
   plt . legend ( loc = 'upper left' , labels = [ u'Win' + IIOoO0oo , u'Loss' + IIOoO0oo ] )
   if 74 - 74: OooOoo % iI1iII1I1I1i . I1Ii1I1 / I1I / Ii / Ooo0Ooo
   OoOOoO0o000 = plt . subplot ( 313 )
   plt . grid ( linestyle = '--' , color = '#D9D9D9' )
   plt . plot ( ooO000Oo , Oo00O00o0oO , color = '#EBB000' , label = 'Utilization' )
   OoOOoO0o000 . yaxis . set_major_formatter ( ticker . PercentFormatter ( xmax = 1 , decimals = 1 ) )
   plt . fill_between ( ooO000Oo , 0 , Oo00O00o0oO , color = '#FFFBEB' , alpha = .5 )
   plt . legend ( loc = 'upper left' )
   if 11 - 11: I1I - OooOoo * ooOOO % i1i1i1111I + ooo000 . oOO
   plt . show ( )
  else :
   print ( 'No data' )
   if 51 - 51: ooOOO + iI1iII1I1I1i % i11 . I11iiIi11i1I % Ooo0Ooo
 def Join ( self , report = False ) :
  self . gs . acquire ( )
  if self . _joinResult is None :
   self . lib . api_Join . restype = ctypes . c_char_p
   oOO0o00oOooO = self . lib . api_Join ( self . ctx )
   self . lib . api_Release ( self . ctx )
   self . _joinResult = oOO0o00oOooO
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
  IiIIIII1i = json . loads ( self . _joinResult )
  I11IIi1IIIi = [ ]
  Ii11 = [ ]
  iiI1IIII1I1 = ''
  for ooI1Ii11iI1 in IiIIIII1i [ 'Snapshots' ] :
   ooooo0oo0 = ooI1Ii11iI1 [ 1 ] [ 0 ]
   if not iiI1IIII1I1 :
    iiI1IIII1I1 = '(%s)' % ( ooooo0oo0 [ 'MarginCurrency' ] , )
   I11IIi1IIIi . append ( [ ooooo0oo0 [ 'PnL' ] , ooooo0oo0 [ 'Utilization' ] * 100 ] )
   Ii11 . append ( pd . Timestamp ( ooI1Ii11iI1 [ 0 ] , unit = 'ms' , tz = 'Asia/Shanghai' ) )
  oOOo = [ "PnL" + iiI1IIII1I1 , "Utilization(%)" ]
  return pd . DataFrame ( I11IIi1IIIi , index = Ii11 , columns = oOOo )
  if 80 - 80: ooo000 * ooo000 . i1 + IIiIIiIi11I1 . ooOOO
class oOOOO00 ( ) :
 def __init__ ( self , task , session ) :
  self . session = session
  self . task = task
  self . gApis = { }
  self . tpls = task [ 'Code' ]
  del task [ 'Code' ]
  self . ctx = o0O0O000O ( task = self . task , gApis = self . gApis , progressCallback = self . progressCallback )
  if 13 - 13: oOo0O00 / iI1iII1I1I1i
 def progressCallback ( self , st ) :
  if self . session is None :
   return
  self . session . sendall ( struct . pack ( '!II' , Iii11iiiiI ( st ) [ 'TaskStatus' ] , len ( st ) ) + st )
  if 100 - 100: Ooo0Ooo + i1i1i1111I % I1I
 def waitStop ( self , ctx ) :
  if self . session is None :
   return
  try :
   o0o0oooO = b''
   o0O0Oo0o = 0
   self . session . settimeout ( None )
   while True :
    if o0O0Oo0o > 0 :
     if len ( o0o0oooO ) - 4 >= o0O0Oo0o :
      if o0o0oooO [ 4 : 4 + o0O0Oo0o ] == b'stop' :
       ctx . Join ( )
       self . session . close ( )
       os . _exit ( 2 )
      break
    elif len ( o0o0oooO ) >= 4 :
     o0O0Oo0o , = struct . unpack ( '!I' , o0o0oooO [ : 4 ] )
     continue
    o0o0oooO += self . session . recv ( ( o0O0Oo0o - ( len ( o0o0oooO ) - 4 ) ) if o0O0Oo0o > 0 else 4 )
  except :
   pass
   if 9 - 9: I11iiIi11i1I * OooOoo - I11iiIi11i1I
 def exit_handler ( self , signum , frame ) :
  signal . signal ( signal . SIGINT , signal . SIG_IGN )
  self . ctx . Join ( )
  self . session . shutdown ( socket . SHUT_RDWR )
  os . _exit ( 0 )
  if 73 - 73: I1Ii1I1
 def Run ( self ) :
  signal . signal ( signal . SIGINT , self . exit_handler )
  if self . session and platform . system ( ) == 'Windows' :
   Oo0OOOo0o = threading . Thread ( target = self . waitStop , args = ( self . ctx , ) )
   Oo0OOOo0o . setDaemon ( True )
   Oo0OOOo0o . start ( )
  try :
   iiII = False
   II1I1i1 = len ( self . tpls )
   for I11i in xrange ( 0 , II1I1i1 ) :
    iI1IiI1 = self . tpls [ I11i ]
    OO00 = copy . copy ( self . gApis )
    for IIiii1i1iI1I1 in iI1IiI1 [ 1 ] :
     OO00 [ IIiii1i1iI1I1 [ 0 ] ] = IIiii1i1iI1I1 [ 1 ]
    o0O0 = iI1IiI1 [ 0 ] + "\n\nif 'init' in locals() and callable(init):\n    init()\n"
    if I11i == II1I1i1 - 1 :
     o0O0 += "\nmain()\nif 'onexit' in globals():\n    onexit()"
    if not iiII and 'matplotlib' in o0O0 :
     iiII = True
     try :
      __import__ ( 'matplotlib' ) . use ( 'Agg' )
     except :
      pass
    exec ( o0O0 . replace ( '\r\n' , '\n' ) , OO00 )
  except ( EOFError , SystemExit ) :
   pass
  except :
   ii1i1iiI1 , OOOOOoOO , o0 = sys . exc_info ( )
   O00oO00oO0O = [ x for x in traceback . extract_tb ( o0 ) if x [ 0 ] == '<string>' ]
   if O00oO00oO0O :
    O0oOoO = [ 'Traceback (most recent call last):\n' ]
    O0oOoO = O0oOoO + traceback . format_list ( O00oO00oO0O )
   else :
    O0oOoO = [ ]
   O0oOoO = O0oOoO + traceback . format_exception_only ( ii1i1iiI1 , OOOOOoOO )
   self . ctx . g_LogError ( '' . join ( O0oOoO ) )
  self . ctx . Join ( )
  self . session . shutdown ( socket . SHUT_RDWR )
  if 36 - 36: ooOOO + oOo0O00 + OooOoo / i1 % i11 . ooo000
class oo0OOOOOO0o00 ( ) :
 def send ( self , * args ) :
  pass
 def sendall ( self , * args ) :
  pass
 def close ( self , * args ) :
  pass
 def shutdown ( self , * args ) :
  pass
  if 74 - 74: i1 + oOO
if __name__ == '__main__' :
 OOo00oOoOo = ii1Iii ( )
 oO0ooOo0OOOO = None
 if OOo00oOoOo == 'dummy' :
  oO0ooOo0OOOO = iIi [ 's' ]
 else :
  oO0ooOo0OOOO = oo0OOOOOO0o00 ( )
 if oO0ooOo0OOOO is not None :
  oOOOO00 ( __cfg__ , oO0ooOo0OOOO ) . Run ( )
  if 34 - 34: iI1iII1I1I1i + IIiIIiIi11I1 . iI1iI11Ii111 . i11 % i1i1i1111I
  if 61 - 61: Oo % ooo000
