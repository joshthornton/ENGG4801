import inspect
from Keywords import *
from Operators import *
from Value import *
from Label import *
from Operand import *

class Statement:
	
	def __init__( self, asm, hlasm, opcode ):
		self._asm = asm
		self._hlasm = hlasm
		self._opcode = opcode
	
	def __str__( self ):
		return " ".join( self._hlasm ) 
	
	def __repr__( self ):
		return " ".join( self._hlasm ) 

class Atmega64:
	
	ADC = Statement( [ Instructions.ADC , Operands.D, Operators.COMMA, Operands.R, Operators.PLUS, Keywords.CARRY ]
	ADD = Statement( [ Instructions.ADC , Operands.D, Operators.COMMA, Operands.R, Operators.PLUS, Keywords.CARRY ]

	def __iter__(self):
		return ( v for k, v in inspect.getmembers( self ) if not k.startswith( '__' ) )
