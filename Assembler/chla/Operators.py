import inspect

class Operator:
	"""Abstract representation of CHLA operator."""

	def __init__( self, name ):
		self._name = name

	def __str__( self ):
		return self._name

	def __repr__( self ):
		return "Operator: {0}".format( self._name )
	
	def match( self, other ):
		if isinstance( other, Operator ):
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

class Operators:
	PLUS_EQ			=	Operator( "+=" )
	PLUS_PLUS		=	Operator( "++" )
	PLUS			=	Operator( "+" )
	AND_EQ          =	Operator( "&=" )
	NOT_EQ          =	Operator( "!=" )
	NOT             =	Operator( "~=" )
	EQ_EQ			=	Operator( "==" )
	SUB_EQ			=	Operator( "-=" )
	SUB_SUB			=	Operator( "--" )
	SUB             =	Operator( "-" )
	EOR             =	Operator( "^=" )
	EQ              =	Operator( "=" )
	FMUL			=	Operator( "." )
	MUL             =	Operator( "*" )
	ABS             =	Operator( "|" )
	LSL             =	Operator( "<<" )
	ASR             =	Operator( ">>>" )
	LSR             =	Operator( ">>" )
	OR              =	Operator( "|=" )
	OPEN_BRACE		=	Operator( "[" )
	OPEN_BRACKET    =	Operator( "(" )
	CLOSE_BRACE		=	Operator( "]" )
	CLOSE_BRACKET   =	Operator( ")" )
	PAIR			=	Operator( ":" )
	COMMA			= 	Operator( "," )
	HASH			= 	Operator( "#" )
	GEQ				= 	Operator( ">=" )
	LEQ				=	Operator( "<=" )
	LT				=	Operator( "<" )
	GT				=	Operator( ">" )
	AND				=	Operator( "&" )
	DIV				=	Operator( "/" )

	def __iter__(self):
		return ( v for k, v in inspect.getmembers( self ) if not k.startswith( '__' ) )
