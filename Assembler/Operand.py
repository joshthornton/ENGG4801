from Value import *
from Label import *

class Operand:
	def __init__( self, name, r ):
		self._name = name
		self._range = r

	def __repr__( self ):
		return "Operand: {0} ({1})".format( self._name, self._range ) 
	
	def __eq__( self, other ):
		if isinstance( other, Operand ):
			return self._name == other._name and self._range == other._range
		if isinstance( other, ( Value, Pair) ) and self._name != "l":
			return self._range.check( other ) 
		if isinstance( other, ( Label ) ) and self._name == "l":
			return True
		return False
	
	def __key( self ):
		return ( self._name, self._range )
	
	def __hash__( self ):
		return hash( self.__key() )
	
	def name( self ):
		return self._name
