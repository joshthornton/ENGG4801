from chla.Value import *
from chla.Label import *

class Operand:
	"""Abstract representation of a CHLA operand."""
	
	def __init__( self, name, r ):
		self._name = name
		self._range = r

	def __repr__( self ):
		return "Operand: {0} ({1})".format( self._name, self._range ) 
	
	def match( self, other ):
		
		"""Special method designed to match operands 
		to legal values as well as equate two operands."""

		if isinstance( other, Operand ):
			return self._name == other._name and self._range == other._range
		if isinstance( other, ( Value, Pair) ) and self._name != "l":
			return self._range.check( other ) 
		if isinstance( other, ( Label ) ) and self._name == "l":
			if other.value():
				return self._range.check( other )
			return True
		return False
	
	def __key( self ):
		return ( self._name, self._range )
	
	def __hash__( self ):
		return hash( self.__key() )
	
	def name( self ):
		return self._name
	
	def range( self ):
		return self._range
