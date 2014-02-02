class Value:
	"""Abstract representation of a numeric value, optionally with human readable name"""
	def __init__( self, name, value ):
		self._name = name
		self._value = value
	
	def asm( self ):
		return self._name if self._name != "" else str( self._value )
		#return str( self._value )
	
	def chla( self ):
		return self._name if self._name != "" else str( self._value )
	
	def __repr__( self ):
		return "Value: {0}".format( "{0}({1})".format(self._name,self._value) if self._name != "" else self._value )
	
	def __eq__( self, other ):
		if isinstance( other, Value ):
			return self._value == other._value
		return False
	
	def __key( self ):
		return ( self._value )
	
	def __hash__( self ):
		return hash( self.__key() )

class Pair:
	"""Abstract representation of a pair of numeric values, optionally with human readable name"""
	def __init__( self, firstValue, secondValue ):
		self._firstValue = firstValue
		self._secondValue = secondValue

	def __repr__( self ):
		return "Pair: {0}:{1}".format( self._firstValue, self._secondValue )
	
	def __eq__( self, other ):
		if isinstance( other, Pair ):
			return self._firstValue == other._firstValue and self._secondValue == other._secondValue 
		return False
	
	def __key( self ):
		return ( self._firstValue, self._secondValue )
	
	def __hash__( self ):
		return hash( self.__key() )
	
	def asm( self ):
		return "{0}:{1}".format( self._firstValue.asm(), self._secondValue.asm() )
	
	def chla( self ):
		return "{0}:{1}".format( self._firstValue.chla(), self._secondValue.chla() )
