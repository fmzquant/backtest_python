# -*- coding: utf-8 -*-  
import warnings
warnings . filterwarnings ( "ignore" , category = DeprecationWarning )
import sys
import traceback
import math
import threading
import socket
import json
import copy
import os
import time
import io , base64
import struct
import platform
if 82 - 82: Iii1i
Ii = sys . version_info [ 0 ] >= 3
i11i1 = sys . version_info [ 0 ] <= 2
try :
 import md5
except :
 import hashlib as md5
 if 26 - 26: o0Ooo0OOO * IiI / OOo0O0oOo0O . ooo0oOoooOOO0 * Ii1I111 + i1iiIII111
 if 29 - 29: iI + o00Oo - OOoOoo000O00 * Oo0Oo - ii1I1iII1I1I . i1I1IiIIiIi1
oo0O000ooO = hasattr
def hasattr ( obj , method ) :
 try :
  return oo0O000ooO ( obj , method )
 except :
  return False
  if 98 - 98: IiiIIiii1 % iIi1ii1I1iI11
def o00o0OO00O ( raw ) :
 if i11i1 and isinstance ( raw , unicode ) :
  return raw . encode ( 'utf-8' )
 elif Ii and isinstance ( raw , bytes ) :
  return raw . decode ( 'utf-8' )
 return raw
 if 57 - 57: iiIi1 - ii % iiI * IIi1i111IiII . i1I
OO0o000o = threading . Lock ( )
IIiiii1IiIiII = globals ( )
IIiiii1IiIiII [ 'NaN' ] = None
IIiiii1IiIiII [ 'null' ] = None
IIiiii1IiIiII [ 'true' ] = True
IIiiii1IiIiII [ 'false' ] = False
i1ii11iii = 3000
if 22 - 22: iiIi1 - i1I1IiIIiIi1 / Ii1I111 . i1I1IiIIiIi1
if Ii :
 IIiiii1IiIiII [ 'xrange' ] = range
 if 1 - 1: iIi1ii1I1iI11 + IiiIIiii1 + iiI * iiIi1
if os . getenv ( "BOTVS_TMP_FILE" ) is not None :
 try :
  os . remove ( os . getenv ( "BOTVS_TMP_FILE" ) )
 except :
  pass
  if 20 - 20: i1iiIII111 + o0Ooo0OOO
class Iio0 :
 def __init__ ( self , name ) :
  self . __name = name
  sys . modules [ 'talib' ] = self
 def __getattr__ ( self , attr ) :
  raise Exception ( 'Please install %s module for python' % self . __name )
  if 11 - 11: i1I . IiI
class I1i ( RuntimeError ) :
 def __init__ ( self , message ) :
  self . message = message
  if 75 - 75: i1I . IiiIIiii1 . IIi1i111IiII * ii % Oo0Oo
o0OoOOo00OOO = False
try :
 i11ii1i1I = __import__ ( "talib" )
 import numpy
 o0OoOOo00OOO = True
except ImportError :
 i11ii1i1I = Iio0 ( 'talib' )
 if 17 - 17: iI . OOoOoo000O00 + Ii1I111
class O00o00O0ooO ( list ) :
 def __init__ ( self , data ) :
  super ( O00o00O0ooO , self ) . __init__ ( data )
  self . __data = data
 def __getattr__ ( self , attr ) :
  if attr . startswith ( '_' ) :
   raise AttributeError
  i1iII1i1Ii11I = [ ]
  for Oo in self . __data :
   i1iII1i1Ii11I . append ( Oo [ attr ] )
  if o0OoOOo00OOO :
   i1iII1i1Ii11I = numpy . array ( i1iII1i1Ii11I )
  setattr ( self , attr , i1iII1i1Ii11I )
  return i1iII1i1Ii11I
  if 82 - 82: o0Ooo0OOO + Oo0Oo . o00Oo / Ii1I111
class Oooo0o0oO0 :
 @ staticmethod
 def _skip ( arr , period ) :
  IiII = 0
  I1i1i = 0
  for I1i1i in xrange ( 0 , len ( arr ) ) :
   if arr [ I1i1i ] is not None :
    IiII += 1
   if IiII == period :
    break
  return I1i1i
  if 46 - 46: i1I - ooo0oOoooOOO0 * Ii1I111 / IiiIIiii1 / Iii1i
 @ staticmethod
 def _sum ( arr , num ) :
  I11iIi1i = 0.0
  for oooOOOooo in xrange ( 0 , num ) :
   if arr [ oooOOOooo ] is not None :
    I11iIi1i += arr [ oooOOOooo ]
  return I11iIi1i
  if 85 - 85: Oo0Oo - o00Oo
 @ staticmethod
 def _avg ( arr , num ) :
  if len ( arr ) == 0 :
   return 0
  I11iIi1i = 0.0
  I11I11I = 0
  for oooOOOooo in xrange ( 0 , min ( len ( arr ) , num ) ) :
   if arr [ oooOOOooo ] is not None :
    I11iIi1i += arr [ oooOOOooo ]
    I11I11I += 1
  if I11I11I == 0 :
   return 0
  return I11iIi1i / I11I11I
  if 4 - 4: o00Oo
 @ staticmethod
 def _zeros ( n ) :
  return [ 0.0 ] * n
  if 23 - 23: o0Ooo0OOO + i1I . ii1I1iII1I1I - Oo0Oo * IiiIIiii1
 @ staticmethod
 def _set ( arr , start , end , value ) :
  for oooOOOooo in xrange ( start , min ( len ( arr ) , end ) ) :
   arr [ oooOOOooo ] = value
   if 78 - 78: i1I1IiIIiIi1 . i1iiIII111 % o0Ooo0OOO + IiiIIiii1 * Iii1i
 @ staticmethod
 def _diff ( a , b ) :
  Ii1I1I1i = [ None ] * len ( b )
  for oooOOOooo in xrange ( 0 , len ( b ) ) :
   if a [ oooOOOooo ] is not None and b [ oooOOOooo ] is not None :
    Ii1I1I1i [ oooOOOooo ] = a [ oooOOOooo ] - b [ oooOOOooo ]
  return Ii1I1I1i
  if 93 - 93: OOoOoo000O00 % IiiIIiii1 * Oo0Oo
 @ staticmethod
 def _move_diff ( a ) :
  Ii1I1I1i = [ None ] * ( len ( a ) - 1 )
  for oooOOOooo in xrange ( 1 , len ( a ) ) :
   Ii1I1I1i [ oooOOOooo - 1 ] = a [ oooOOOooo ] - a [ oooOOOooo - 1 ]
  return Ii1I1I1i
  if 52 - 52: iiI + i1iiIII111 / i1I1IiIIiIi1 - Ii1I111 * IIi1i111IiII % OOoOoo000O00
 @ staticmethod
 def _cmp ( arr , start , end , cmpFunc ) :
  oOoO00 = arr [ start ]
  for oooOOOooo in xrange ( start , end ) :
   oOoO00 = cmpFunc ( arr [ oooOOOooo ] , oOoO00 )
  return oOoO00
  if 84 - 84: iIi1ii1I1iI11 - i1iiIII111 - ii
 @ staticmethod
 def _filt ( records , n , attr , iv , cmpFunc ) :
  if len ( records ) < 2 :
   return None
  oOoO00 = iv
  ooO0000Ooo0O = 0
  if n != 0 :
   ooO0000Ooo0O = len ( records ) - min ( len ( records ) - 1 , n ) - 1
  for oooOOOooo in xrange ( len ( records ) - 2 , ooO0000Ooo0O - 1 , - 1 ) :
   if records [ oooOOOooo ] is not None :
    if attr is not None :
     oOoO00 = cmpFunc ( oOoO00 , records [ oooOOOooo ] [ attr ] )
    else :
     oOoO00 = cmpFunc ( oOoO00 , records [ oooOOOooo ] )
  return oOoO00
  if 29 - 29: Iii1i / o0Ooo0OOO
 @ staticmethod
 def _ticks ( records ) :
  if len ( records ) == 0 :
   return [ ]
   if 32 - 32: IiI % IiiIIiii1 - IIi1i111IiII * i1iiIII111
  if isinstance ( records [ 0 ] , int ) or isinstance ( records [ 0 ] , float ) :
   return records
   if 92 - 92: iiIi1 - iI - Iii1i / IiiIIiii1 . Ii1I111 / ii
  oooOoO0000 = [ None ] * len ( records )
  for oooOOOooo in xrange ( 0 , len ( records ) ) :
   oooOoO0000 [ oooOOOooo ] = records [ oooOOOooo ] [ 'Close' ]
  return oooOoO0000
  if 41 - 41: ii % iiI - Ii1I111 - iiIi1
 @ staticmethod
 def _sma ( S , period ) :
  O0O0O = Oooo0o0oO0 . _zeros ( len ( S ) )
  I1i1i = Oooo0o0oO0 . _skip ( S , period )
  Oooo0o0oO0 . _set ( O0O0O , 0 , I1i1i , None )
  if I1i1i < len ( S ) :
   I11iIi1i = 0
   for oooOOOooo in xrange ( I1i1i , len ( S ) ) :
    if oooOOOooo == I1i1i :
     I11iIi1i = Oooo0o0oO0 . _sum ( S , oooOOOooo + 1 )
    else :
     I11iIi1i += S [ oooOOOooo ] - S [ oooOOOooo - period ]
    O0O0O [ oooOOOooo ] = I11iIi1i / period
  return O0O0O
  if 81 - 81: iIi1ii1I1iI11 + IiI
 @ staticmethod
 def _smma ( S , period ) :
  O0O0O = Oooo0o0oO0 . _zeros ( len ( S ) )
  I1i1i = Oooo0o0oO0 . _skip ( S , period )
  Oooo0o0oO0 . _set ( O0O0O , 0 , I1i1i , None )
  if I1i1i < len ( S ) :
   O0O0O [ I1i1i ] = Oooo0o0oO0 . _avg ( S , I1i1i + 1 )
   for oooOOOooo in xrange ( I1i1i + 1 , len ( S ) ) :
    O0O0O [ oooOOOooo ] = ( O0O0O [ oooOOOooo - 1 ] * ( period - 1 ) + S [ oooOOOooo ] ) / period
  return O0O0O
  if 92 - 92: o00Oo / Oo0Oo + iiI
 @ staticmethod
 def _ema ( S , period ) :
  O0O0O = Oooo0o0oO0 . _zeros ( len ( S ) )
  iiI1 = 2.0 / ( period + 1 )
  I1i1i = Oooo0o0oO0 . _skip ( S , period )
  Oooo0o0oO0 . _set ( O0O0O , 0 , I1i1i , None )
  if I1i1i < len ( S ) :
   O0O0O [ I1i1i ] = Oooo0o0oO0 . _avg ( S , I1i1i + 1 )
   for oooOOOooo in xrange ( I1i1i + 1 , len ( S ) ) :
    O0O0O [ oooOOOooo ] = ( ( S [ oooOOOooo ] - O0O0O [ oooOOOooo - 1 ] ) * iiI1 ) + O0O0O [ oooOOOooo - 1 ]
  return O0O0O
  if 20 - 20: IiI / IiiIIiii1 - iiI + IiiIIiii1 - i1iiIII111 . IiiIIiii1
class oOOoOOOO000 :
 @ staticmethod
 def Highest ( records , n , attr = None ) :
  return Oooo0o0oO0 . _filt ( records , n , attr , 5e-324 , max )
  if 70 - 70: iiIi1 / o00Oo / iiIi1 - i1I1IiIIiIi1 . Oo0Oo
 @ staticmethod
 def Lowest ( records , n , attr = None ) :
  return Oooo0o0oO0 . _filt ( records , n , attr , 1.7976931348623157e+308 , min )
  if 86 - 86: Ii1I111 - ooo0oOoooOOO0 - iiI % i1I1IiIIiIi1 . IIi1i111IiII % Iii1i
 @ staticmethod
 def MA ( records , period = 9 ) :
  return Oooo0o0oO0 . _sma ( Oooo0o0oO0 . _ticks ( records ) , period )
  if 11 - 11: ooo0oOoooOOO0 - Ii1I111 - o00Oo . Oo0Oo - iIi1ii1I1iI11 / Oo0Oo
 @ staticmethod
 def SMA ( records , period = 9 ) :
  return Oooo0o0oO0 . _sma ( Oooo0o0oO0 . _ticks ( records ) , period )
  if 44 - 44: IiiIIiii1 + IiI + Iii1i - iiI
 @ staticmethod
 def EMA ( records , period = 9 ) :
  return Oooo0o0oO0 . _ema ( Oooo0o0oO0 . _ticks ( records ) , period )
  if 7 - 7: IiI / o0Ooo0OOO * Iii1i
 @ staticmethod
 def MACD ( records , fastEMA = 12 , slowEMA = 26 , signalEMA = 9 ) :
  oooOoO0000 = Oooo0o0oO0 . _ticks ( records )
  i1 = Oooo0o0oO0 . _ema ( oooOoO0000 , slowEMA )
  iI1i = Oooo0o0oO0 . _ema ( oooOoO0000 , fastEMA )
  if 73 - 73: o00Oo - ii1I1iII1I1I
  iIi1 = Oooo0o0oO0 . _diff ( iI1i , i1 )
  if 4 - 4: i1I1IiIIiIi1 % i1iiIII111 - IiI
  iI11i1iI1I1Ii = Oooo0o0oO0 . _ema ( iIi1 , signalEMA )
  oOoOO0O0 = Oooo0o0oO0 . _diff ( iIi1 , iI11i1iI1I1Ii )
  return [ iIi1 , iI11i1iI1I1Ii , oOoOO0O0 ]
  if 20 - 20: ii / o00Oo * iiI % iiIi1
 @ staticmethod
 def BOLL ( records , period = 20 , multiplier = 2 ) :
  O0OOooOOoO000 = Oooo0o0oO0 . _ticks ( records )
  I1i1i = period - 1
  while I1i1i < len ( O0OOooOOoO000 ) and ( O0OOooOOoO000 [ I1i1i ] is None ) :
   I1i1i += 1
  OO = Oooo0o0oO0 . _zeros ( len ( O0OOooOOoO000 ) )
  ooOOOO00O = Oooo0o0oO0 . _zeros ( len ( O0OOooOOoO000 ) )
  ii1 = Oooo0o0oO0 . _zeros ( len ( O0OOooOOoO000 ) )
  Oooo0o0oO0 . _set ( OO , 0 , I1i1i , None )
  Oooo0o0oO0 . _set ( ooOOOO00O , 0 , I1i1i , None )
  Oooo0o0oO0 . _set ( ii1 , 0 , I1i1i , None )
  I11I11I = 0.0
  for oooOOOooo in xrange ( I1i1i , len ( O0OOooOOoO000 ) ) :
   if oooOOOooo == I1i1i :
    for IiII in xrange ( 0 , period ) :
     I11I11I += O0OOooOOoO000 [ IiII ]
   else :
    I11I11I = I11I11I + O0OOooOOoO000 [ oooOOOooo ] - O0OOooOOoO000 [ oooOOOooo - period ]
   Oo0O00OOoo = I11I11I / period
   Ii1I1I1i = 0
   for IiII in xrange ( oooOOOooo + 1 - period , oooOOOooo + 1 ) :
    Ii1I1I1i += ( O0OOooOOoO000 [ IiII ] - Oo0O00OOoo ) * ( O0OOooOOoO000 [ IiII ] - Oo0O00OOoo )
   o0oO00OO = math . sqrt ( Ii1I1I1i / period )
   O0OO0OOOOoo0o = Oo0O00OOoo + ( multiplier * o0oO00OO )
   o00ooo0OO0000 = Oo0O00OOoo - ( multiplier * o0oO00OO )
   OO [ oooOOOooo ] = O0OO0OOOOoo0o
   ooOOOO00O [ oooOOOooo ] = Oo0O00OOoo
   ii1 [ oooOOOooo ] = o00ooo0OO0000
  return [ OO , ooOOOO00O , ii1 ]
  if 37 - 37: i1iiIII111
 @ staticmethod
 def KDJ ( records , n = 9 , k = 3 , d = 3 ) :
  ooOo00o = Oooo0o0oO0 . _zeros ( len ( records ) )
  Oooo0o0oO0 . _set ( ooOo00o , 0 , n - 1 , None )
  o0 = Oooo0o0oO0 . _zeros ( len ( records ) )
  oOoo0OOOOOoo = Oooo0o0oO0 . _zeros ( len ( records ) )
  OoO = Oooo0o0oO0 . _zeros ( len ( records ) )
  if 63 - 63: IIi1i111IiII
  i1Ii = Oooo0o0oO0 . _zeros ( len ( records ) )
  iI111i1III = Oooo0o0oO0 . _zeros ( len ( records ) )
  for oooOOOooo in xrange ( 0 , len ( records ) ) :
   i1Ii [ oooOOOooo ] = records [ oooOOOooo ] [ 'High' ]
   iI111i1III [ oooOOOooo ] = records [ oooOOOooo ] [ 'Low' ]
   if 39 - 39: OOoOoo000O00 - i1I % i1I . OOo0O0oOo0O * i1iiIII111
  for oooOOOooo in xrange ( 0 , len ( records ) ) :
   if oooOOOooo >= ( n - 1 ) :
    Iiiii1iiiII1 = records [ oooOOOooo ] [ 'Close' ]
    OoOOo0oO000oOo0 = Oooo0o0oO0 . _cmp ( i1Ii , oooOOOooo - ( n - 1 ) , oooOOOooo + 1 , max )
    iiiiiI = Oooo0o0oO0 . _cmp ( iI111i1III , oooOOOooo - ( n - 1 ) , oooOOOooo + 1 , min )
    ooOo00o [ oooOOOooo ] = ( 100 * ( ( Iiiii1iiiII1 - iiiiiI ) / ( OoOOo0oO000oOo0 - iiiiiI ) ) ) if OoOOo0oO000oOo0 != iiiiiI else 100
    o0 [ oooOOOooo ] = float ( 1 * ooOo00o [ oooOOOooo ] + ( k - 1 ) * o0 [ oooOOOooo - 1 ] ) / k
    oOoo0OOOOOoo [ oooOOOooo ] = float ( 1 * o0 [ oooOOOooo ] + ( d - 1 ) * oOoo0OOOOOoo [ oooOOOooo - 1 ] ) / d
   else :
    o0 [ oooOOOooo ] = oOoo0OOOOOoo [ oooOOOooo ] = 50.0
    ooOo00o [ oooOOOooo ] = 0.0
   OoO [ oooOOOooo ] = 3 * o0 [ oooOOOooo ] - 2 * oOoo0OOOOOoo [ oooOOOooo ]
   if 77 - 77: OOoOoo000O00 % OOo0O0oOo0O - OOoOoo000O00 - i1I1IiIIiIi1 * ii + iiI
  for oooOOOooo in xrange ( 0 , n - 1 ) :
   o0 [ oooOOOooo ] = oOoo0OOOOOoo [ oooOOOooo ] = OoO [ oooOOOooo ] = None
  return [ o0 , oOoo0OOOOOoo , OoO ]
  if 64 - 64: i1I . IiiIIiii1 . Oo0Oo * i1I
 @ staticmethod
 def RSI ( records , period = 14 ) :
  I11I11I = period
  oo0 = Oooo0o0oO0 . _zeros ( len ( records ) )
  Oooo0o0oO0 . _set ( oo0 , 0 , len ( oo0 ) , None )
  if len ( records ) < I11I11I :
   return oo0
   if 74 - 74: o00Oo . o0Ooo0OOO % iiIi1 / iIi1ii1I1iI11 % o00Oo
  oooOoO0000 = Oooo0o0oO0 . _ticks ( records )
  IIiIIIII1iiI = Oooo0o0oO0 . _move_diff ( oooOoO0000 )
  O0O0oO = IIiIIIII1iiI [ : I11I11I ]
  O0OO0OOOOoo0o = 0.0
  IIiI1i = 0.0
  for oooOOOooo in xrange ( 0 , len ( O0O0oO ) ) :
   if O0O0oO [ oooOOOooo ] >= 0 :
    O0OO0OOOOoo0o += O0O0oO [ oooOOOooo ]
   else :
    IIiI1i += O0O0oO [ oooOOOooo ]
  O0OO0OOOOoo0o /= I11I11I
  IIiI1i /= I11I11I
  IIiI1i = - IIiI1i
  if IIiI1i != 0 :
   OoOOooO0oOO0Oo = O0OO0OOOOoo0o / IIiI1i
  else :
   OoOOooO0oOO0Oo = 0
  oo0 [ I11I11I ] = 100 - 100 / ( 1 + OoOOooO0oOO0Oo )
  iiI1i1IiiiIi1 = 0.0
  II11IIIIiI1iI = 0.0
  iII = 0.0
  for oooOOOooo in xrange ( I11I11I + 1 , len ( oooOoO0000 ) ) :
   iiI1i1IiiiIi1 = IIiIIIII1iiI [ oooOOOooo - 1 ]
   if iiI1i1IiiiIi1 > 0 :
    II11IIIIiI1iI = iiI1i1IiiiIi1
    iII = 0.0
   else :
    II11IIIIiI1iI = 0.0
    iII = - iiI1i1IiiiIi1
   O0OO0OOOOoo0o = ( O0OO0OOOOoo0o * ( I11I11I - 1 ) + II11IIIIiI1iI ) / I11I11I
   IIiI1i = ( IIiI1i * ( I11I11I - 1 ) + iII ) / I11I11I
   OoOOooO0oOO0Oo = 0 if IIiI1i == 0 else ( O0OO0OOOOoo0o / IIiI1i )
   oo0 [ oooOOOooo ] = 100 - 100 / ( 1 + OoOOooO0oOO0Oo )
  return oo0
 @ staticmethod
 def OBV ( records ) :
  if len ( records ) == 0 :
   return [ ]
   if 44 - 44: Iii1i + OOoOoo000O00 + IIi1i111IiII % iiIi1 * ooo0oOoooOOO0
  if 'Close' not in records [ 0 ] :
   raise "TA.OBV argument must KLine"
   if 58 - 58: ii1I1iII1I1I - iiI + i1I1IiIIiIi1 % Oo0Oo - i1iiIII111
  O0O0O = Oooo0o0oO0 . _zeros ( len ( records ) )
  for oooOOOooo in xrange ( 0 , len ( records ) ) :
   if oooOOOooo == 0 :
    O0O0O [ oooOOOooo ] = records [ oooOOOooo ] [ 'Volume' ]
   elif records [ oooOOOooo ] [ 'Close' ] >= records [ oooOOOooo - 1 ] [ 'Close' ] :
    O0O0O [ oooOOOooo ] = O0O0O [ oooOOOooo - 1 ] + records [ oooOOOooo ] [ 'Volume' ]
   else :
    O0O0O [ oooOOOooo ] = O0O0O [ oooOOOooo - 1 ] - records [ oooOOOooo ] [ 'Volume' ]
  return O0O0O
  if 90 - 90: i1I1IiIIiIi1 % iI
 @ staticmethod
 def ATR ( records , period = 14 ) :
  if len ( records ) == 0 :
   return [ ]
  if 'Close' not in records [ 0 ] :
   raise "TA.ATR argument must KLine"
   if 100 - 100: Oo0Oo . iiIi1 * i1I1IiIIiIi1 * i1I1IiIIiIi1
  O0O0O = Oooo0o0oO0 . _zeros ( len ( records ) )
  Iioo0Oo0oO0 = 0.0
  I11I11I = 0.0
  for oooOOOooo in xrange ( 0 , len ( records ) ) :
   iII11I1iI = 0
   if oooOOOooo == 0 :
    iII11I1iI = records [ oooOOOooo ] [ 'High' ] - records [ oooOOOooo ] [ 'Low' ]
   else :
    iII11I1iI = max ( records [ oooOOOooo ] [ 'High' ] - records [ oooOOOooo ] [ 'Low' ] , abs ( records [ oooOOOooo ] [ 'High' ] - records [ oooOOOooo - 1 ] [ 'Close' ] ) , abs ( records [ oooOOOooo - 1 ] [ 'Close' ] - records [ oooOOOooo ] [ 'Low' ] ) )
   Iioo0Oo0oO0 += iII11I1iI
   if oooOOOooo < period :
    I11I11I = Iioo0Oo0oO0 / ( oooOOOooo + 1 )
   else :
    I11I11I = ( ( ( period - 1 ) * I11I11I ) + iII11I1iI ) / period
   O0O0O [ oooOOOooo ] = I11I11I
  return O0O0O
  if 87 - 87: Oo0Oo - iiIi1 * o0Ooo0OOO % IiI % iI
 @ staticmethod
 def Alligator ( records , jawLength = 13 , teethLength = 8 , lipsLength = 5 ) :
  oooOoO0000 = [ ]
  for oooOOOooo in xrange ( 0 , len ( records ) ) :
   oooOoO0000 . append ( ( records [ oooOOOooo ] [ 'High' ] + records [ oooOOOooo ] [ 'Low' ] ) / 2 )
  return [
 [ None ] * 8 + Oooo0o0oO0 . _smma ( oooOoO0000 , jawLength ) ,
  [ None ] * 5 + Oooo0o0oO0 . _smma ( oooOoO0000 , teethLength ) ,
  [ None ] * 3 + Oooo0o0oO0 . _smma ( oooOoO0000 , lipsLength )
  ]
  if 81 - 81: iI + IiI * OOo0O0oOo0O - OOo0O0oOo0O * Ii1I111 - OOoOoo000O00
 @ staticmethod
 def CMF ( records , periods = 20 ) :
  i1iII1i1Ii11I = [ ]
  iiIIIIi = 0.0
  I1iiii1I11i = 0.0
  oO0OO = [ ]
  oO00ooOO0 = [ ]
  for oooOOOooo in xrange ( 0 , len ( records ) ) :
   Ii1I1I1i = 0.0
   if records [ oooOOOooo ] [ 'High' ] != records [ oooOOOooo ] [ 'Low' ] :
    Ii1I1I1i = ( 2 * records [ oooOOOooo ] [ 'Close' ] - records [ oooOOOooo ] [ 'Low' ] - records [ oooOOOooo ] [ 'High' ] ) / ( records [ oooOOOooo ] [ 'High' ] - records [ oooOOOooo ] [ 'Low' ] ) * records [ oooOOOooo ] [ 'Volume' ]
   oO0OO . append ( Ii1I1I1i )
   oO00ooOO0 . append ( records [ oooOOOooo ] [ 'Volume' ] )
   iiIIIIi += Ii1I1I1i
   I1iiii1I11i += records [ oooOOOooo ] [ 'Volume' ]
   if oooOOOooo >= periods :
    iiIIIIi -= oO0OO . pop ( 0 )
    I1iiii1I11i -= oO00ooOO0 . pop ( 0 )
   i1iII1i1Ii11I . append ( iiIIIIi / I1iiii1I11i )
  return i1iII1i1Ii11I
  if 39 - 39: o00Oo - OOoOoo000O00 - i1I1IiIIiIi1 / OOo0O0oOo0O - i1I1IiIIiIi1 / IIi1i111IiII
  if 46 - 46: OOoOoo000O00 + i1I1IiIIiIi1 . Iii1i + o0Ooo0OOO % i1I
O0Oo0 = { }
I111i1i11iII = { }
IiiII1Iiii1I1 = { }
oOO0Oo = 500
if 60 - 60: ooo0oOoooOOO0
def IIiIiI1iII ( method , firstArg , ret ) :
 global IiiII1Iiii1I1
 if method not in [
 'Exchange_GetName' ,
 'Exchange_GetLabel' ,
 'Exchange_GetCurrency' ,
 'Exchange_GetMarkets' ,
 'Exchange_GetMinPrice' ,
 'Exchange_GetMinStock' ,
 ] :
  return
 IiII = '%s_%s' % ( method , firstArg )
 if IiII not in IiiII1Iiii1I1 :
  IiiII1Iiii1I1 [ IiII ] = ret
  if 87 - 87: o00Oo * i1I1IiIIiIi1 % ii1I1iII1I1I * iI . Iii1i - i1I
def oo0O0O0Ooooo ( r , eIndex , platformId , symbol , customPeriod ) :
 IiII = '%d_%s_%d' % ( eIndex , symbol , customPeriod )
 Ooo = O0Oo0 . get ( IiII , None )
 if 69 - 69: iIi1ii1I1iI11 - ii1I1iII1I1I
 global oOO0Oo
 o0oO0OOo = len ( r )
 if o0oO0OOo > oOO0Oo :
  oOO0Oo = o0oO0OOo
  if 89 - 89: iIi1ii1I1iI11 / iI - ii1I1iII1I1I
 if Ooo is not None and len ( Ooo ) > 0 :
  for Oo in r :
   if Oo [ 'Time' ] == Ooo [ - 1 ] [ 'Time' ] :
    Ooo [ - 1 ] = Oo
   elif Oo [ 'Time' ] > Ooo [ - 1 ] [ 'Time' ] :
    Ooo . append ( Oo )
    if len ( Ooo ) > oOO0Oo :
     Ooo . pop ( 0 )
  r = Ooo
  if 13 - 13: iiI + ii1I1iII1I1I * i1I1IiIIiIi1 . i1iiIII111 + iIi1ii1I1iI11 . IiI
 O0Oo0 [ IiII ] = r
 return O00o00O0ooO ( r )
 if 85 - 85: i1I * Iii1i
class Ii1ii :
 def __init__ ( self , p , index , platformId , currency , period ) :
  self . p = p
  self . currency = currency
  self . platformId = platformId
  self . period = period
  self . index = index
  self . maxKLen = 500
  self . ct = ''
  I111i1i11iII [ index ] = currency + '_'
  if 98 - 98: IIi1i111IiII / iI / ooo0oOoooOOO0 + Iii1i % o00Oo
 def GetPeriod ( self ) :
  return self . period
  if 19 - 19: o00Oo % Ii1I111
 def SetContractType ( self , * args ) :
  for iiIi in args :
   if not iiIi . startswith ( '-' ) :
    self . ct = iiIi
    break
  I111i1i11iII [ self . index ] = self . currency + '_' + self . ct
  return self . p . invoke ( * tuple ( [ 'Exchange_SetContractType' , self . index ] + list ( args ) ) )
  if 76 - 76: Ii1I111 . o0Ooo0OOO + ooo0oOoooOOO0
 def IO ( self , * args ) :
  global IiiII1Iiii1I1
  if len ( args ) == 2 and args [ 0 ] == 'currency' :
   self . currency = str ( args [ 1 ] )
   I111i1i11iII [ self . index ] = str ( args [ 1 ] ) + '_' + self . ct
   for IiII in IiiII1Iiii1I1 :
    if 'Currency' in IiII :
     IiiII1Iiii1I1 [ IiII ] = None
  return self . p . invoke ( * tuple ( [ 'Exchange_IO' , self . index ] + list ( args ) ) )
  if 95 - 95: OOo0O0oOo0O % IiI * iIi1ii1I1iI11 - ii1I1iII1I1I
 def SetCurrency ( self , s ) :
  return self . IO ( "currency" , s )
  if 66 - 66: iIi1ii1I1iI11 . iI % o0Ooo0OOO % ii * OOoOoo000O00
 def SetBase ( self , s ) :
  return self . IO ( "base" , s )
  if 59 - 59: o0Ooo0OOO . i1I1IiIIiIi1 - OOo0O0oOo0O - iIi1ii1I1iI11 - IiI . Oo0Oo
 def Log ( self , logType , price , amount = 0 , * extra ) :
  iI11 = [ str ( item ) for item in extra ]
  return self . p . invoke ( 'Exchange_Log' , self . index , logType , price , amount , ' ' . join ( iI11 ) )
  if 75 - 75: Oo0Oo * i1I - OOoOoo000O00 % ii - i1I
 def SetMaxBarLen ( self , n ) :
  global oOO0Oo
  oOO0Oo = n
  self . p . invoke ( 'Exchange_SetMaxBarLen' , self . index , n )
  if 56 - 56: OOo0O0oOo0O
 def GetRecords ( self , period = - 1 ) :
  if period == - 1 :
   period = self . period
  IiIIIII1i = I111i1i11iII . get ( self . index , '' )
  O0OOo0O = self . p . invoke ( 'Exchange_GetRecords' , self . index , period )
  if O0OOo0O is None :
   return O0OOo0O
  return oo0O0O0Ooooo ( O0OOo0O , self . index , self . platformId , IiIIIII1i , period )
  if 9 - 9: IiI
  if 12 - 12: ii1I1iII1I1I . iiI / IIi1i111IiII . iiI
 def __getattr__ ( self , name ) :
  if name == 'Go' :
   return lambda * oO0O0oO0 : self . p . invoke ( 'GoAsync_Exchange_' + oO0O0oO0 [ 0 ] , self . index , * oO0O0oO0 [ 1 : ] )
  elif '_' not in name :
   return lambda * oO0O0oO0 : self . p . invoke ( 'Exchange_' + name , self . index , * oO0O0oO0 )
   if 40 - 40: IIi1i111IiII . i1iiIII111 % ooo0oOoooOOO0
 def __repr__ ( self ) :
  return '<Exchange>'
  if 85 - 85: OOo0O0oOo0O / iiI + OOo0O0oOo0O + o00Oo
class I11111i111 ( dict ) :
 def __getattr__ ( self , name ) :
  if name in self :
   return self [ name ]
  else :
   raise AttributeError ( "no attribute '%s'" % name )
   if 35 - 35: Ii1I111
 def __setattr__ ( self , name , value ) :
  self [ name ] = value
  if 35 - 35: Oo0Oo + Iii1i + ooo0oOoooOOO0 / i1I1IiIIiIi1 % ooo0oOoooOOO0 . Iii1i
 def __delattr__ ( self , name ) :
  if name in self :
   del self [ name ]
  else :
   raise AttributeError ( "no attribute '%s'" % name )
   if 12 - 12: i1iiIII111 % IiiIIiii1 - Oo0Oo - ii1I1iII1I1I / Oo0Oo + IIi1i111IiII
class ii1i :
 def __init__ ( self , p , config ) :
  self . p = p
  self . p . invoke ( 'Chart_New' , json . dumps ( config ) )
  if 87 - 87: o00Oo
 def add ( self , * arg ) :
  self . p . invoke ( 'Chart_Add' , json . dumps ( list ( arg ) ) )
  if 57 - 57: iiIi1 - iIi1ii1I1iI11 % o00Oo - ii / ii1I1iII1I1I . IiiIIiii1
 def update ( self , config ) :
  self . p . invoke ( 'Chart_New' , json . dumps ( config ) )
  if 15 - 15: IIi1i111IiII * ii - OOoOoo000O00
 def reset ( self , reverse = 0 ) :
  self . p . invoke ( 'Chart_Reset' , reverse )
  if 6 - 6: i1I - o0Ooo0OOO
 def __repr__ ( self ) :
  return '<Chart>'
  if 1 - 1: i1iiIII111 + ooo0oOoooOOO0
class OooO0Oo :
 def __init__ ( self , p , options = { } ) :
  options [ "__isCandle" ] = True
  self . chart = ii1i ( p , options )
  self . bar = None
  self . overlay = options . get ( "overlay" , False )
  self . preTime = 0
  self . runtime = { "plots" : [ ] , "signals" : [ ] , "titles" : { } , "count" : 0 }
  if 17 - 17: iI % iiI % ii1I1iII1I1I * IiI
 def trim ( self , obj ) :
  ooOoO0O0 = { }
  for IiII in obj :
   if obj [ IiII ] is not None :
    ooOoO0O0 [ IiII ] = obj [ IiII ]
  return ooOoO0O0
  if 52 - 52: IiiIIiii1 * OOo0O0oOo0O + Iii1i - Ii1I111 + iIi1ii1I1iI11 % ii1I1iII1I1I
 def newPlot ( self , obj ) :
  IiIoO0OoOoo = self . trim ( obj )
  if "overlay" not in IiIoO0OoOoo :
   IiIoO0OoOoo [ "overlay" ] = self . overlay
  if IiIoO0OoOoo [ "type" ] != 'shape' and IiIoO0OoOoo [ "type" ] != 'bgcolor' and IiIoO0OoOoo [ "type" ] != 'barcolor' :
   if "title" not in IiIoO0OoOoo or len ( IiIoO0OoOoo [ "title" ] ) == 0 or IiIoO0OoOoo [ "title" ] in self . runtime [ "titles" ] :
    IiIoO0OoOoo [ "title" ] = '<' + IiIoO0OoOoo . get ( "title" , "plot" ) + '_' + str ( self . runtime [ "count" ] ) + '>'
   self . runtime [ "count" ] += 1
   if "title" in IiIoO0OoOoo :
    self . runtime [ "titles" ] [ IiIoO0OoOoo [ "title" ] ] = True
  return IiIoO0OoOoo
  if 66 - 66: ii . i1iiIII111 % ii1I1iII1I1I + ooo0oOoooOOO0 * OOo0O0oOo0O / ooo0oOoooOOO0
  if 33 - 33: i1I / ooo0oOoooOOO0
 def begin ( self , bar ) :
  self . bar = bar
  if 98 - 98: Ii1I111 . iiIi1 * IIi1i111IiII - iIi1ii1I1iI11 % IIi1i111IiII * i1I
 def reset ( self , remain = 0 ) :
  self . chart . reset ( remain )
  self . preTime = 0
  if 42 - 42: ooo0oOoooOOO0 + IiI - iIi1ii1I1iI11 - OOoOoo000O00 * IIi1i111IiII + o0Ooo0OOO
 def close ( self ) :
  if self . bar [ "Time" ] < self . preTime :
   return
   if 46 - 46: OOoOoo000O00 . iIi1ii1I1iI11 - o0Ooo0OOO . OOoOoo000O00 + IiI
  I111iI11i = {
 "timestamp" : self . bar [ "Time" ] ,
 "open" : self . bar [ "Open" ] ,
 "high" : self . bar [ "High" ] ,
 "low" : self . bar [ "Low" ] ,
 "close" : self . bar [ "Close" ] ,
 "volume" : self . bar . get ( "Volume" , 0 ) ,
 }
  if 42 - 42: ii - o0Ooo0OOO / OOo0O0oOo0O - IiI + ii
  for IiII in [ "plots" , "signals" ] :
   if len ( self . runtime [ IiII ] ) > 0 :
    if "runtime" not in I111iI11i :
     I111iI11i [ "runtime" ] = { }
    I111iI11i [ "runtime" ] [ IiII ] = self . runtime [ IiII ]
    if 83 - 83: iI . iIi1ii1I1iI11
  if self . preTime == self . bar [ "Time" ] :
   self . chart . add ( 0 , I111iI11i , - 1 )
  else :
   self . chart . add ( 0 , I111iI11i )
   if 57 - 57: i1I % ii1I1iII1I1I / OOoOoo000O00 + IiiIIiii1 - Oo0Oo
  self . preTime = self . bar [ "Time" ]
  self . runtime [ "plots" ] = [ ]
  self . runtime [ "signals" ] = [ ]
  self . runtime [ "titles" ] = { }
  self . runtime [ "count" ] = 0
  if 87 - 87: Oo0Oo . Oo0Oo . iiI . i1I1IiIIiIi1 * OOoOoo000O00
 def plot ( self , series = None , title = None , color = None , linewidth = 1 , style = "line" , trackprice = None , histbase = 0 , offset = 0 , join = False , editable = False , show_last = None , display = "all" , overlay = None ) :
  if series is None or self . bar [ "Time" ] < self . preTime :
   return
   if 33 - 33: i1I * Oo0Oo / IIi1i111IiII . ooo0oOoooOOO0 * OOoOoo000O00 + i1I1IiIIiIi1
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
  if 17 - 17: IiI * iiI + Oo0Oo - ii / IiI
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
  if 83 - 83: ii - Iii1i + OOoOoo000O00 + i1iiIII111 / iiIi1 + i1iiIII111
 def plotarrow ( self , series , title = None , colorup = "#00ff00" ,
 colordown = "#ff0000" ,
 offset = 0 ,
 minheight = 5 ,
 maxheight = 100 ,
 editable = False , show_last = None , display = "all" , overlay = None ) :
  if display != "all" or self . bar [ "Time" ] < self . preTime :
   return
   if 29 - 29: IiI / OOoOoo000O00
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
  if 13 - 13: ii % Oo0Oo . ooo0oOoooOOO0 % i1I1IiIIiIi1 % ooo0oOoooOOO0
 def hline ( self , price , title = None , color = None , linestyle = "dashed" , linewidth = None , editable = False , display = "all" , overlay = None ) :
  if display != "all" or self . bar [ "Time" ] < self . preTime :
   return
   if 21 - 21: i1I * Ii1I111
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
  if 93 - 93: IiiIIiii1 . iI + i1I - OOoOoo000O00
  if 97 - 97: iI - iI % iiIi1 + ii1I1iII1I1I / IIi1i111IiII * iIi1ii1I1iI11
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
  if 60 - 60: ii - IiiIIiii1 % Ii1I111
  if 26 - 26: o00Oo / iiIi1 . iiI + ii . OOo0O0oOo0O
 def plotchar ( self , series , title = None , char = None , location = "abovebar" , color = None , offset = None , text = None , textcolor = None , editable = None , size = "auto" , show_last = None , display = "all" , overlay = None ) :
  if ( location != "absolute" and series is None ) or ( location == "absolute" and series is None ) or char is None or self . bar [ "Time" ] < self . preTime :
   return
   if 37 - 37: Ii1I111
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
  if 35 - 35: ooo0oOoooOOO0 % IiI - iIi1ii1I1iI11 / ii1I1iII1I1I
  if 4 - 4: i1I1IiIIiIi1 . ii1I1iII1I1I % i1I1IiIIiIi1 / IiI
  if 48 - 48: Oo0Oo . OOo0O0oOo0O
 def plotshape ( self , series , title = None , style = None , location = "abovebar" , color = None , offset = None , text = None , textcolor = None , editable = None , size = "auto" , show_last = None , display = "all" , overlay = None ) :
  if ( location != "absolute" and series is None ) or ( location == "absolute" and series is None ) or self . bar [ "Time" ] < self . preTime :
   return
   if 92 - 92: ooo0oOoooOOO0 + o0Ooo0OOO / iiIi1 + ooo0oOoooOOO0 * iiIi1 * iIi1ii1I1iI11
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
  if 79 - 79: IiI
 def plotcandle ( self , open , high , low , close , title = None , color = None , wickcolor = None , editable = None , show_last = None , bordercolor = None , display = "all" , overlay = None ) :
  if display != "all" or self . bar [ "Time" ] < self . preTime :
   return
   if 3 - 3: ooo0oOoooOOO0 / i1I % ii
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
  if 55 - 55: OOoOoo000O00
 def fill ( self , plot1 , plot2 , color = None , title = None , editable = None , show_last = None , fillgaps = None , display = "all" ) :
  if self . bar [ "Time" ] < self . preTime :
   return
  if plot1 >= 0 and plot2 >= 0 and plot1 < len ( self . runtime [ "plots" ] ) and plot2 < len ( self . runtime [ "plots" ] ) and display == "all" :
   ooOoO0O0 = self . runtime [ "plots" ] [ plot1 ]
   if "fill" not in ooOoO0O0 :
    ooOoO0O0 [ "fill" ] = [ ]
   ooOoO0O0 [ "fill" ] . append ( self . trim ( {
 "value" : self . runtime [ "plots" ] [ plot2 ] [ "series" ] ,
 "color" : color ,
 "showLast" : show_last
 } ) )
   if 31 - 31: o0Ooo0OOO . IiiIIiii1 / i1I
 def signal ( self , direction , price , qty , id = None ) :
  if self . bar [ "Time" ] < self . preTime :
   return
  oO0 = {
 "id" : id or direction ,
 "avgPrice" : price ,
 "qty" : qty
 }
  if direction == "buy" or direction == "long" :
   oO0 [ "direction" ] = "long"
  elif direction == "sell" or direction == "short" :
   oO0 [ "direction" ] = "short"
  elif direction == "closesell" or direction == "closeshort" :
   oO0 [ "direction" ] = "close"
   oO0 [ "closeDirection" ] = "short"
  elif direction == "closebuy" or direction == "closelong" :
   oO0 [ "direction" ] = "close"
   oO0 [ "closeDirection" ] = "long"
   if 69 - 69: ii
  if oO0 [ "direction" ] or oO0 [ "closeDirection" ] :
   self . runtime [ "signals" ] . append ( oO0 )
   if 74 - 74: ooo0oOoooOOO0 * OOoOoo000O00
class oOo0Oo00o0O :
 def __init__ ( self , p , addr , fd ) :
  self . p = p
  self . addr = addr
  self . fd = fd
  if 9 - 9: ii % iiI % i1I1IiIIiIi1 . o0Ooo0OOO - i1I1IiIIiIi1
 def read ( self , timeout = 0 ) :
  return self . p . invoke ( 'TSocket_Read' , self . fd , timeout )
  if 48 - 48: Iii1i * IiI + ii1I1iII1I1I
 def write ( self , buf , timeout = 0 ) :
  return self . p . invoke ( 'TSocket_Write' , self . fd , buf , timeout )
  if 31 - 31: OOo0O0oOo0O * Oo0Oo % o0Ooo0OOO / iiI + Ii1I111 + iIi1ii1I1iI11
 def close ( self ) :
  return self . p . invoke ( 'TSocket_Close' , self . fd )
  if 90 - 90: Ii1I111 * IiI / iIi1ii1I1iI11 * o0Ooo0OOO
 def __repr__ ( self ) :
  return '<Dial %s fd:%d>' % ( self . addr , self . fd )
  if 38 - 38: i1iiIII111 . o0Ooo0OOO
class OO0OOo0oOO :
 def __init__ ( self , p , eIndex , platformId , symbol , period , routineId ) :
  self . p = p
  self . eIndex = eIndex
  self . symbol = symbol
  self . period = period
  self . platformId = platformId
  self . routineId = routineId
  if 100 - 100: Oo0Oo
 def wait ( self , timeout = None ) :
  if timeout is None :
   timeout = 0 if self . p . invoke ( 'Test' , 'thread' ) else - 1
  O0OOo0O , oOO0OOO = self . p . invoke ( 'GoWait' , self . routineId , timeout )
  if oOO0OOO and ( O0OOo0O is not None ) and self . symbol != '' :
   O0OOo0O = oo0O0O0Ooooo ( O0OOo0O , self . eIndex , self . platformId , self . symbol , self . period )
  return O0OOo0O , oOO0OOO
  if 24 - 24: iiIi1 * ii + IiI + IiiIIiii1
 def __repr__ ( self ) :
  return '<Go %d>' % self . routineId
  if 11 - 11: Ii1I111 % OOoOoo000O00 % OOo0O0oOo0O + IiI
class OO00Oo ( json . JSONEncoder ) :
 def default ( self , obj ) :
  return str ( obj )
  if 89 - 89: iIi1ii1I1iI11 + ii1I1iII1I1I . IiiIIiii1 % o00Oo
i1II111iii11 = False
class ooo0 :
 def __init__ ( self , addr , pwd ) :
  self . __addr = addr
  self . __pwd = pwd
  self . __seq = 0
  self . __sock = None
  self . __isConnect = False
  self . __nonce = 0
  if ':' in self . __addr :
   iI11 = addr . split ( ':' )
   self . __addr = ( iI11 [ 0 ] , int ( iI11 [ 1 ] ) )
   self . proto = socket . AF_INET
  else :
   self . __addr = addr
   self . proto = socket . AF_UNIX
  O0o0o0OO = 0
  O0o = [ ]
  while True :
   try :
    i1iII1i1Ii11I = self . invoke ( 'Exchange_Len' )
    if isinstance ( i1iII1i1Ii11I , ( int , float ) ) :
     O0o0o0OO = i1iII1i1Ii11I
     for oooOOOooo in xrange ( 0 , O0o0o0OO ) :
      O0o . append ( [ oooOOOooo + 1 , - 1 , '' , - 1 ] )
    else :
     O0o0o0OO = len ( i1iII1i1Ii11I )
     O0o = i1iII1i1Ii11I
    break
   except :
    time . sleep ( 1 )
  self . exchanges = [ ]
  self . exchange = None
  for oooOOOooo in xrange ( 0 , O0o0o0OO ) :
   if len ( O0o [ oooOOOooo ] ) == 3 :
    O0o [ oooOOOooo ] . insert ( 0 , oooOOOooo + 1 )
   O0Oooo0 = Ii1ii ( self , O0o [ oooOOOooo ] [ 0 ] , O0o [ oooOOOooo ] [ 1 ] , O0o [ oooOOOooo ] [ 2 ] , O0o [ oooOOOooo ] [ 3 ] )
   self . exchanges . append ( O0Oooo0 )
   if oooOOOooo == 0 :
    self . exchange = O0Oooo0
    if 24 - 24: i1I1IiIIiIi1 % OOo0O0oOo0O % o00Oo + iIi1ii1I1iI11
  if platform . system ( ) == 'Windows' :
   IIiiiiIi1Ii1I = threading . Thread ( target = self . wait )
   IIiiiiIi1Ii1I . setDaemon ( True )
   IIiiiiIi1Ii1I . start ( )
   if 86 - 86: IiI * iiI % OOoOoo000O00
 def reset ( self ) :
  global OO0o000o
  OO0o000o = threading . Lock ( )
  self . __isConnect = False
  if 39 - 39: Ii1I111 * ii1I1iII1I1I
 def wait ( self ) :
  global i1II111iii11
  I11iIi1i = socket . socket ( self . proto , socket . SOCK_STREAM )
  try :
   I111iI11i = struct . pack ( "<QBBI" , 2 , 100 , 1 , 0 )
   I11iIi1i . connect ( self . __addr )
   I11iIi1i . send ( I111iI11i )
   I11iIi1i . settimeout ( None )
   I11iIi1i . recv ( 5 )
   i1II111iii11 = True
  except :
   pass
  I11iIi1i . close ( )
  if 66 - 66: i1iiIII111 . ooo0oOoooOOO0
 def invoke ( self , method , * arg ) :
  global i1II111iii11 , IiiII1Iiii1I1
  if i1II111iii11 :
   i1II111iii11 = False
   raise I1i ( "stop" )
  if method != "_G" and not method [ 0 ] . isupper ( ) :
   raise Exception ( "invalid method" )
  if len ( arg ) > 0 :
   oOoO00 = IiiII1Iiii1I1 . get ( '%s_%s' % ( method , arg [ 0 ] ) , None )
   if oOoO00 :
    return oOoO00
    if 31 - 31: ii1I1iII1I1I . IIi1i111IiII % iIi1ii1I1iI11 + iiI
  if method == "Dial" :
   method = "TSocket_New"
   if len ( arg ) == 0 :
    arg = ( 30 , )
  if ( method == "Exchange_Buy" or method == "Exchange_Sell" ) and len ( arg ) == 2 :
   arg = ( arg [ 0 ] , - 1 , arg [ 1 ] )
  if method == "Exchange_GetData" :
   if len ( arg ) == 2 :
    arg = ( arg [ 0 ] , arg [ 1 ] , 60000 , 0 )
   elif len ( arg ) == 3 :
    arg = ( arg [ 0 ] , arg [ 1 ] , arg [ 2 ] , 0 )
  if Ii and ( method == "Exchange_CancelOrder" or method == "Exchange_GetOrder" ) and len ( arg ) > 1 and isinstance ( arg [ 1 ] , bytes ) :
   iIIO0ooO0oO = list ( arg )
   iIIO0ooO0oO [ 1 ] = str ( iIIO0ooO0oO [ 1 ] , 'utf-8' )
   arg = tuple ( iIIO0ooO0oO )
  OO0o000o . acquire ( )
  self . __seq += 1
  O000 = int ( time . time ( ) * 1000000 )
  if O000 <= self . __nonce :
   O000 = self . __nonce + 1
  self . __nonce = O000
  i1ii1iIi = list ( arg )
  for oooOOOooo in xrange ( 0 , len ( i1ii1iIi ) ) :
   if hasattr ( i1ii1iIi [ oooOOOooo ] , 'savefig' ) and callable ( i1ii1iIi [ oooOOOooo ] . savefig ) :
    try :
     Ii1I1I1i = io . BytesIO ( )
     i1ii1iIi [ oooOOOooo ] . savefig ( Ii1I1I1i , format = "png" )
     i1ii1iIi [ oooOOOooo ] = '`data:image/png;base64,%s`' % ( base64 . b64encode ( Ii1I1I1i . getvalue ( ) ) . decode ( 'utf-8' ) )
    except :
     i1ii1iIi [ oooOOOooo ] = '`%s`' % json . dumps ( i1ii1iIi [ oooOOOooo ] )
   elif isinstance ( i1ii1iIi [ oooOOOooo ] , dict ) and i1ii1iIi [ oooOOOooo ] . get ( 'type' ) == 'table' and i1ii1iIi [ oooOOOooo ] . get ( 'cols' ) :
    i1ii1iIi [ oooOOOooo ] = '`%s`' % json . dumps ( i1ii1iIi [ oooOOOooo ] )
    if 21 - 21: iI * ii + OOoOoo000O00
  O0OOo0O = { 'Method' : method , 'Args' : i1ii1iIi , 'Nonce' : O000 , 'Sign' : md5 . md5 ( ( method + '|' + str ( O000 ) + '|' + self . __pwd ) . encode ( 'utf-8' ) ) . hexdigest ( ) }
  I11Ii = json . dumps ( O0OOo0O , cls = OO00Oo ) . encode ( 'utf-8' )
  I111iI11i = struct . pack ( "<QBBI%ds" % len ( I11Ii ) , self . __seq , 100 , 0 , len ( I11Ii ) , I11Ii )
  if not self . __isConnect :
   self . __sock = socket . socket ( self . proto , socket . SOCK_STREAM )
   self . __sock . connect ( self . __addr )
   self . __sock . settimeout ( None )
   self . __isConnect = True
  try :
   self . __sock . send ( I111iI11i )
  except socket . error as O0Oooo0 :
   self . __isConnect = False
   self . __sock . shutdown ( socket . SHUT_RDWR )
   self . __sock . close ( )
   OO0o000o . release ( )
   raise O0Oooo0
  o0o00oo000 = 13
  oo = - 1
  Ii1I11iI11I1 = 101
  O0OOO = o0o00oo000
  iIII = bytes ( )
  while True :
   try :
    iIII += self . __sock . recv ( O0OOO - len ( iIII ) )
   except socket . error as O0Oooo0 :
    self . __isConnect = False
    self . __sock . shutdown ( socket . SHUT_RDWR )
    self . __sock . close ( )
    OO0o000o . release ( )
    raise O0Oooo0
   if len ( iIII ) >= O0OOO :
    if oo < 0 :
     o0oO0O0 , Ii1I11iI11I1 , oo = struct . unpack ( '<QBI' , iIII [ : o0o00oo000 ] )
     O0OOO += oo
    else :
     break
  OO0o000o . release ( )
  if Ii1I11iI11I1 == 101 :
   try :
    oO0O0oO0 = str ( iIII [ o0o00oo000 : ] . decode ( 'utf-8' ) )
   except :
    oO0O0oO0 = str ( iIII [ o0o00oo000 : ] )
   O0OOo0O = json . loads ( oO0O0oO0 , object_hook = I11111i111 )
   if len ( O0OOo0O ) == 1 :
    if method . startswith ( 'Exchange_Get' ) and len ( arg ) > 0 and O0OOo0O [ 0 ] is not None :
     O0OOo0O [ 0 ] = o00o0OO00O ( O0OOo0O [ 0 ] )
     IIiIiI1iII ( method , arg [ 0 ] , O0OOo0O [ 0 ] )
     return O0OOo0O [ 0 ]
    if method == 'TSocket_New' and O0OOo0O [ 0 ] is not None :
     return oOo0Oo00o0O ( self , arg [ 0 ] , int ( O0OOo0O [ 0 ] ) )
    elif method . startswith ( 'GoAsync_' ) and O0OOo0O [ 0 ] is not None :
     OO00 = - 1
     IIiII = - 1
     IiIIIII1i = ''
     iiIOoO00 = 0
     if len ( arg ) > 0 :
      iiIOoO00 = arg [ 0 ]
     if method == 'GoAsync_Exchange_GetRecords' and len ( arg ) > 0 :
      if len ( arg ) == 2 :
       OO00 = arg [ 1 ]
      if OO00 == - 1 :
       OO00 = self . exchanges [ iiIOoO00 - 1 ] . period
      IIiII = self . exchanges [ iiIOoO00 - 1 ] . platformId
      IiIIIII1i = I111i1i11iII . get ( iiIOoO00 , '' )
     return OO0OOo0oOO ( self , iiIOoO00 , IIiII , IiIIIII1i , OO00 , int ( O0OOo0O [ 0 ] ) )
    elif method . find ( 'TSocket' ) == - 1 :
     return o00o0OO00O ( O0OOo0O [ 0 ] )
    return O0OOo0O [ 0 ]
   return tuple ( O0OOo0O )
  if Ii1I11iI11I1 == 102 :
   raise Exception ( iIII [ o0o00oo000 : ] )
   if 41 - 41: iiIi1 / ii
 def __getattr__ ( self , name ) :
  return lambda * oO0O0oO0 : self . invoke ( name , * oO0O0oO0 )
  if 60 - 60: iiIi1 + IiI . ii - iIi1ii1I1iI11
 def __getitem__ ( self , name ) :
  return lambda * oO0O0oO0 : self . invoke ( name , * oO0O0oO0 )
  if 31 - 31: ii1I1iII1I1I % o0Ooo0OOO
 def close ( self ) :
  if self . __sock :
   self . __sock . shutdown ( socket . SHUT_RDWR )
   self . __sock . close ( )
   if 7 - 7: i1I - iiIi1 * OOoOoo000O00
 def GetMeta ( self ) :
  return self . invoke ( 'Env' , 'meta' )
  if 69 - 69: OOo0O0oOo0O
 def Chart ( self , config ) :
  return ii1i ( self , config )
  if 56 - 56: ii1I1iII1I1I + i1I1IiIIiIi1
 def KLineChart ( self , config = { } ) :
  return OooO0Oo ( self , config )
  if 47 - 47: i1I1IiIIiIi1
def i1IiI1I ( a , b = None ) :
 O0OOo0O = str ( a )
 if b is not None :
  O0OOo0O = str ( a ) + '|' + str ( b )
 return '[trans]' + O0OOo0O + '[/trans]'
 if 98 - 98: i1I + i1I * ooo0oOoooOOO0 . i1I1IiIIiIi1 . ii1I1iII1I1I
def Oo00 ( date = None , fmt = None ) :
 if date is None :
  date = time . time ( )
 if fmt is None :
  fmt = '%Y-%m-%d %H:%M:%S'
 return time . strftime ( fmt , time . localtime ( date ) )
 if 52 - 52: o0Ooo0OOO . ooo0oOoooOOO0 . Oo0Oo * ii - iIi1ii1I1iI11
def i1IiI11 ( arr1 , arr2 ) :
 if len ( arr1 ) != len ( arr2 ) :
  raise Exception ( "cross array length not equal" )
 I11I11I = 0
 for oooOOOooo in range ( len ( arr1 ) - 1 , - 1 , - 1 ) :
  if arr1 [ oooOOOooo ] is None or arr2 [ oooOOOooo ] is None :
   break
  if arr1 [ oooOOOooo ] < arr2 [ oooOOOooo ] :
   if I11I11I > 0 :
    break
   I11I11I -= 1
  elif arr1 [ oooOOOooo ] > arr2 [ oooOOOooo ] :
   if I11I11I < 0 :
    break
   I11I11I += 1
  else :
   break
 return I11I11I
 if 39 - 39: ii + iiI % IIi1i111IiII - iiIi1 + Iii1i
def OoO0O000o0OO ( num , precision = 4 ) :
 oO0O0oO0 = math . pow ( 10 , precision )
 return math . floor ( num * oO0O0oO0 ) / oO0O0oO0
 if 84 - 84: iI % o0Ooo0OOO * iiIi1 % ii / i1I
def ooo00oooOOOo ( ns ) :
 global i1II111iii11
 I11I11I = float ( ns ) / 1000
 while True :
  if i1II111iii11 :
   i1II111iii11 = False
   raise I1i ( "stop" )
  Iioo0Oo0oO0 = min ( I11I11I , 0.2 )
  if Iioo0Oo0oO0 <= 0 :
   break
  time . sleep ( Iioo0Oo0oO0 )
  I11I11I -= Iioo0Oo0oO0
  if 53 - 53: IiiIIiii1 / i1I % o0Ooo0OOO - ooo0oOoooOOO0 * i1iiIII111 % iiI
def OOOoO0O0O0 ( ) :
 return False
 if 99 - 99: o00Oo * iiIi1 % iI / iiI + iI + OOoOoo000O00
def o0OOOO00OOo00 ( d ) :
 global i1ii11iii
 if d > 0 :
  i1ii11iii = d
  if 70 - 70: ii1I1iII1I1I - OOoOoo000O00 / OOoOoo000O00 . IiI
def OO0Ooo0O00Oo ( pfn , * arg ) :
 while True :
  i1iII1i1Ii11I = pfn ( * arg )
  if i1iII1i1Ii11I == False or i1iII1i1Ii11I is None :
   ooo00oooOOOo ( i1ii11iii )
  else :
   return i1iII1i1Ii11I
   if 14 - 14: IIi1i111IiII * iI / ii . iI / o0Ooo0OOO
class I1Ii1ii :
 pass
 if 71 - 71: iiIi1 - iiIi1
II1ii11 = '''
import os, sys, signal, json, threading
alreadyExit = False
onExitSuccess = False
def wrap_onexit():
    onexit()
    onExitSuccess = True

def exit_handler(signum, frame):
    global alreadyExit
    if alreadyExit:
        return
    alreadyExit = True
    _resetRpc()
    signal.signal(signal.SIGINT, signal.SIG_IGN)
    exitCode = 0
    if 'onexit' in globals():
        t = threading.Thread(target=wrap_onexit)
        t.setDaemon(True)
        t.start()
        t.join(timeout=300)
        if not onExitSuccess:
            exitCode = 1
            sys.stderr.write("onexit timeout")
    os._exit(exitCode)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, exit_handler)
    try:
        if 'init' in globals():
            init()
        if 'main' in globals():
            ret = main()
            if ret is not None:
                SetResult(json.dumps(ret))
    except StopError:
        pass
    exit_handler(None, None)
'''
if 30 - 30: o0Ooo0OOO * IiiIIiii1 / o0Ooo0OOO / iiIi1 - Ii1I111
def __init_ctx__ ( srcCode , tpls ) :
 iI11 = globals ( ) [ '__RPC_ENV__' ] . split ( ',' )
 oO = ooo0 ( iI11 [ 0 ] , iI11 [ 1 ] )
 oOoO00 = { }
 oOoO00 [ 'null' ] = None
 oOoO00 [ 'true' ] = True
 oOoO00 [ 'false' ] = False
 oOoO00 [ 'PERIOD_M1' ] = 60 * 1
 oOoO00 [ 'PERIOD_M3' ] = 60 * 3
 oOoO00 [ 'PERIOD_M5' ] = 60 * 5
 oOoO00 [ 'PERIOD_M15' ] = 60 * 15
 oOoO00 [ 'PERIOD_M30' ] = 60 * 30
 oOoO00 [ 'PERIOD_H1' ] = 60 * 60
 oOoO00 [ 'PERIOD_H2' ] = 60 * 60 * 2
 oOoO00 [ 'PERIOD_H4' ] = 60 * 60 * 4
 oOoO00 [ 'PERIOD_H6' ] = 60 * 60 * 6
 oOoO00 [ 'PERIOD_H12' ] = 60 * 60 * 12
 oOoO00 [ 'PERIOD_D1' ] = 60 * 60 * 24
 oOoO00 [ 'PERIOD_D3' ] = 60 * 60 * 24 * 3
 oOoO00 [ 'PERIOD_W1' ] = 60 * 60 * 24 * 7
 oOoO00 [ 'ORDER_STATE_PENDING' ] = 0
 oOoO00 [ 'ORDER_STATE_CLOSED' ] = 1
 oOoO00 [ 'ORDER_STATE_CANCELED' ] = 2
 oOoO00 [ 'ORDER_STATE_UNKNOWN' ] = 3
 oOoO00 [ 'ORDER_TYPE_BUY' ] = 0
 oOoO00 [ 'ORDER_TYPE_SELL' ] = 1
 oOoO00 [ "ORDER_OFFSET_OPEN" ] = 0
 oOoO00 [ "ORDER_OFFSET_CLOSE" ] = 1
 oOoO00 [ 'LOG_TYPE_BUY' ] = 0
 oOoO00 [ 'LOG_TYPE_SELL' ] = 1
 oOoO00 [ 'LOG_TYPE_CANCEL' ] = 2
 oOoO00 [ 'PD_LONG' ] = 0
 oOoO00 [ 'PD_SHORT' ] = 1
 oOoO00 [ 'PD_LONG_YD' ] = 2
 oOoO00 [ 'PD_SHORT_YD' ] = 3
 oOoO00 [ 'exchange' ] = oO . exchange
 oOoO00 [ 'exchanges' ] = oO . exchanges
 oOoO00 [ 'TA' ] = oOOoOOOO000
 oOoO00 [ 'talib' ] = i11ii1i1I
 oOoO00 [ 'Chart' ] = oO . Chart
 oOoO00 [ 'KLineChart' ] = oO . KLineChart
 oOoO00 [ 'GetMeta' ] = oO . GetMeta
 oOoO00 [ '_N' ] = OoO0O000o0OO
 oOoO00 [ '_Cross' ] = i1IiI11
 oOoO00 [ '_D' ] = Oo00
 oOoO00 [ '_C' ] = OO0Ooo0O00Oo
 oOoO00 [ '_CDelay' ] = o0OOOO00OOo00
 oOoO00 [ 'Sleep' ] = ooo00oooOOOo
 oOoO00 [ 'IsVirtual' ] = OOOoO0O0O0
 oOoO00 [ '__name__' ] = '__main__'
 oOoO00 [ 'ext' ] = I1Ii1ii ( )
 oOoO00 [ 'StopError' ] = I1i
 oOoO00 [ '_resetRpc' ] = oO . reset
 if 73 - 73: Oo0Oo . iIi1ii1I1iI11 + iiI * iiIi1 % ooo0oOoooOOO0
 for IiII in [ 'Version' , 'JSONParse' , 'Log' , 'DBExec' , 'LogProfit' , 'LogProfitReset' , 'LogReset' , 'LogVacuum' , 'LogStatus' , 'EnableLog' , 'Mail' , 'SetErrorFilter' , 'MD5' , 'HMAC' , 'Encode' , 'Hash' , 'StrDecode' , 'Unix' , 'UnixNano' , 'GetOS' , 'UUID' , 'EventLoop' , 'GetPid' , 'GetLastError' , 'Env' , '_G' , 'GetCommand' , 'Dial' , 'SetResult' ] :
  oOoO00 [ IiII ] = oO [ IiII ]
  if 65 - 65: i1iiIII111 + Oo0Oo . iIi1ii1I1iI11 / o00Oo
 try :
  iII11ii11II1I = __tpls
  ooO0000Ooo0O = 0
  for IiiiIIiiIIiI in iII11ii11II1I :
   O000oO = tpls [ ooO0000Ooo0O ]
   o0IiI111 = copy . copy ( oOoO00 )
   for I11I11I in IiiiIIiiIIiI :
    o0IiI111 [ I11I11I ] = IiiiIIiiIIiI [ I11I11I ]
   exec ( O000oO . replace ( '\r\n' , '\n' ) + "\n\nif 'init' in locals() and callable(init):\n    init()\n" , o0IiI111 )
   ooO0000Ooo0O += 1
   if 99 - 99: OOo0O0oOo0O * OOoOoo000O00 * ii1I1iII1I1I
  iIIO0ooO0oO = __jsargs
  for IiII in iIIO0ooO0oO :
   oOoO00 [ IiII ] = iIIO0ooO0oO [ IiII ]
  exec ( srcCode . replace ( '\r\n' , '\n' ) + "\n\n" + II1ii11 , oOoO00 )
 except :
  iIiI , O0O00oo00o0O0 , ooo00o00ooO = sys . exc_info ( )
  iI11 = [ x for x in traceback . extract_tb ( ooo00o00ooO ) if x [ 0 ] == '<string>' ]
  if iI11 :
   oo00Oo0OoOo0 = [ 'Traceback (most recent call last):\n' ]
   oo00Oo0OoOo0 = oo00Oo0OoOo0 + traceback . format_list ( iI11 )
  else :
   oo00Oo0OoOo0 = [ ]
  oo00Oo0OoOo0 = oo00Oo0OoOo0 + traceback . format_exception_only ( iIiI , O0O00oo00o0O0 )
  sys . stderr . write ( '' . join ( oo00Oo0OoOo0 ) )
  exit ( 1 )
  if 54 - 54: o0Ooo0OOO % iIi1ii1I1iI11 % OOoOoo000O00 * Iii1i
  if 51 - 51: i1iiIII111 . IiI % o0Ooo0OOO
__init_ctx__ ( __Code__ , __Templates__ )
if 55 - 55: IiI * o0Ooo0OOO % IiI
