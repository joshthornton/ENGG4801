from chla.Operand import *

class StatementTemplate:
	"""Abstract representation of a single line of assembly. Maintains the assembly, CHLA, operands and the position of the operands for the statement."""
	def __init__( self, asm, chla, opcode, operandPositions, operands ): 
		self._asm = asm
		self._chla = chla
		self._opcode = opcode
		self._operandPositions = operandPositions
		self._operands = operands
	
	def __repr__( self ):
		return " ".join( [ repr(i) for i in self._chla ] )
	
	def statement_from_chla( self, chla ):
		values = {}
		for p in self._operandPositions:
			values[ p ] = chla[ self._operandPositions[ p ] ]
		return Statement( self._asm, self._chla, self._opcode, self._operands, values ) 
	
	def statement_from_opcode( self, values ):
		return Statement( self._asm, self._chla, self._opcode, self._operands, values )
	
	def chla( self ):
		return self._chla
	
	def asm( self ):
		return self._asm
	
	def opcode( self ):
		return self._opcode
	
	def operand( self, operand ):
		return self._operands.get( operand )

class Statement:
	"""Abstract representation of a single line of assembly. Maintains the assembly, CHLA, operands and the value of the operands for the statement."""
	
	def __init__( self, asm, chla, opcode, operands, values ): 
		self._asm = asm
		self._chla = chla
		self._opcode = opcode
		self._operands = operands
		self._values = values
	
	def __repr__( self ):
		return " ".join( [ repr(i) for i in self._chla ] )

	def asm( self ):
		s = []

		for token in self._asm:
			if isinstance( token, Operand ):
				s.append( self._values[ token.name() ] )
			else:
				s.append( token )

		return s
	
	def chla( self ):
		s = []

		for token in self._chla:
			if isinstance( token, Operand ):
				s.append( self._values[ token.name() ] )
			else:
				s.append( token )
		
		return s 
		
	def asm_string( self ):
		s = []

		for token in self._asm:
			if isinstance( token, Operand ):
				s.append( self._values[ token.name() ].asm() )
			else:
				s.append( token.asm() )

		return "{0} {1}".format( s[0], "".join( s[1:] ) )
	
	def chla_string( self ):
		
		s = []

		for token in self._chla:
			if isinstance( token, Operand ):
				s.append( self._values[ token.name() ].chla() )
			else:
				s.append( token.chla() )

		return " ".join( s )
	
	def operand( self, operand ):
		return ( self._operands.get( operand ), self._values.get( operand ) )
	
	def instruction( self ):
		return self._asm[0]
