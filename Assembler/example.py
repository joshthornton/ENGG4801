from chla.Disassembler import *
from chla.Assembler import *

try:
	Disassembler.disassemble( "test/atmega64.spec", "test/all.hex", "output/atmega64-all.hlasm", 2, "test/atmega64.def" )
	Disassembler.disassemble( "test/hcs08.spec", "test/all.s19", "output/hcs08-all.hlasm", 1, "test/hcs08.def" )

	Assembler.assemble( "test/atmega64.spec", "output/atmega64-all.hlasm", "output/atmega64-all.asm", 2, {} )
	Assembler.assemble( "test/hcs08.spec", "output/hcs08-all.hlasm", "output/hcs08-all.asm", 1, {} )
	
	Assembler.assemble( "test/hcs08.spec", "test/example.hlasm", "output/hcs08-example.asm", 1, {} )
	Assembler.assemble( "test/atmega64.spec", "test/example.hlasm", "output/atmega64-example.asm", 2, { "AVR" : 1 } )
except ValueError as e:
	print( e )
