from Value import *

class Range:
	def __init__( self, low, high ):
		self._low = low
		self._high = high
	
	def __repr__( self ):
		return "Range: {0}-{1}".format( self._low, self._high )
	
	def __eq__( self, other ):
		if isinstance( other, Range ):
			return self._low == other._low and self._high == other._high
		return False
	
	def __key( self ):
		return ( self._low, self._high )
	
	def __hash__( self ):
		return hash( self.__key() )
	
	def check( self, v ):
		if isinstance( v, Value ):
			return v._value >= self._low and v._value <= self._high
		return False

class PairRange:
	def __init__( self, first, second ):
		self._first = Range( first[0], first[1] )
		self._second = Range( second[0], second[1] )
	
	def __repr__( self ):
		return "PairRange: {0}:{1}".format( self._first, self._second )
	
	def __eq__( self, other ):
		if isinstance( other, PairRange ):
			return self._first == other._first and self._second == other._second
		return False
	
	def __key( self ):
		return ( self._first, self._second )
	
	def __hash__( self ):
		return hash( self.__key() )
	
	def check( self, v ):
		if isinstance( v, Pair ):
			if v._first._value != v._second._value + 1:
				return False
			return self._first.check( v._first ) and self._second.check( v._second )
		return False
