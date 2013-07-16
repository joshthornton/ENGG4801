from Operand import *

class StatementTemplate:
	
	def __init__( self, asm, hlasm, opcode, operandPositions ): 
		self._asm = asm
		self._hlasm = hlasm
		self._opcode = opcode
		self._operandPositions = operandPositions
	
	def __repr__( self ):
		return " ".join( [ str(i) for i in self._hlasm ] )
	
	def statement( self, hlasm ):
		operands = {}
		for p in self._operandPositions:
			operands[ p ] = hlasm[ self._operandPositions[ p ] ]
		return Statement( self._asm, self._hlasm, self._opcode, operands ) 

class Statement:
	
	def __init__( self, asm, hlasm, opcode, operands ): 
		self._asm = asm
		self._hlasm = hlasm
		self._opcode = opcode
		self._operands = operands
	
	def __repr__( self ):
		return " ".join( [ str(i) for i in self._hlasm ] )

	def asm( self ):
		
		s = []

		for token in self._asm:
			if isinstance( token, Operand ):
				s.append( self._operands[ token.name() ].asm() )
			else:
				s.append( token.asm() )

		return "{0} {1}".format( s[0], "".join( s[1:] ) )
