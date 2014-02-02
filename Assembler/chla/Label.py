class Label:
	"""Abstract representation of a CHLA/Assembly Label"""
	
	def __init__( self, name, value ):
		self._name = name
		self._value = value
	
	def __str__( self ):
		return self._name

	def __repr__( self ):
		return "Label: {0}{1}".format( self._name, "({0})".format( self._value ) if self._value else ""  )
	
	def match( self, other ):
		if isinstance( other, Label ):
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
	
	def name( self ):
		return self._name
	
	def value( self ):
		return self._value
	
	def update_value( self, value ):
		self._value = value
