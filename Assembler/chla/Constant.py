class Constant:
	"""Abstract Representation of assembly character constant"""
	def __init__( self, name ):
		self._name = name

	def __str__( self ):
		return self._name

	def __repr__( self ):
		return "Constant: {0}".format( self._name )
	
	def __eq__( self, other ):
		if isinstance( other, Constant ):
			return self._name == other._name
		return False
	
	def __key( self ):
		return ( self._name )
	
	def __hash__( self ):
		return hash( self.__key() )

	def asm( self ):
		return self._name

	def chla( self ):
		return self._name
