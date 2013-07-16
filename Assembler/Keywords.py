import inspect

class Keyword:
	
	def __init__( self, name ):
		self._name = name
	
	def __str__( self ):
		return self._name
	
	def __repr__( self ):
		return "Keyword: {0}".format( self._name )
	
	def __eq__( self, other ):
		if isinstance( other, Keyword ):
			return self._name == other._name
		return False
	
	def __key( self ):
		return ( self._name )
	
	def __hash__( self ):
		return hash( self.__key() )
		
	def asm( self ):
		return self._name

class Keywords:
	R0R1		=	Keyword( "r1:r0" )
	SREG		=	Keyword( "sreg" )
	TRANSFER	=	Keyword( "t" )
	SWAP		=	Keyword( "swap" )
	IF			=	Keyword( "if" )
	GOTO		=	Keyword( "goto" )
	SKIP		=	Keyword( "skip" )
	RET			=	Keyword( "ret" )
	RETI		=	Keyword( "reti" )
	POP			=	Keyword( "pop" )
	PUSH		=	Keyword( "push" )
	MEM			=	Keyword( "mem" )
	PMEM		=	Keyword( "pmem" )
	CARRY		=	Keyword( "c" )
	X			=	Keyword( "x" )
	Y			=	Keyword( "y" )
	Z			=	Keyword( "z" )
	END			=	Keyword( "end" )
	
	def __iter__(self):
		return ( v for k, v in inspect.getmembers( self ) if not k.startswith( '__' ) )
