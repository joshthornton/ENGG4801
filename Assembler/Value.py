class Value:
	def __init__( self, name, value ):
		self._name = name
		self._value = value
	
	def asm( self ):
		return self._name if self._name != "" else str( self._value )
	
	def __repr__( self ):
		return "Value: {0}".format( self._name if self._name != "" else self._value )
	
	def __eq__( self, other ):
		if isinstance( other, Value ):
			return self._value == other._value
		return False
	
	def __key( self ):
		return ( self._value )
	
	def __hash__( self ):
		return hash( self.__key() )

class Pair:
	
	def __init__( self, first, second ):
		self._first = first
		self._second = second

	def __repr__( self ):
		return "Pair: {0}:{1}".format( self._first, self._second )
	
	def __eq__( self, other ):
		if isinstance( other, Pair ):
			return self._first == other._first and self._second == other._second 
		return False
	
	def __key( self ):
		return ( self._first, self._second )
	
	def __hash__( self ):
		return hash( self.__key() )
	
	def asm( self ):
		return "{0}:{1}".format( self._first.asm(), self._second.asm() )
