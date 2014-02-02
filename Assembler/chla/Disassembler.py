from chla.Generator import *
from chla.Tokeniser import *
from chla.Binary import *
import re

class Disassembler:

	def disassemble( spec, source, out, bytesInWord, definitionsFile ):
		
		# initialise tokeniser / scanner
		tokeniser = Tokeniser( definitionsFile, {} )
		definitions = tokeniser.definitions
		
		# generate list of all possible instructions
		generatedStatements = Generator.generate_statements( spec, tokeniser )
		
		# read in sourceBinary file
		sourceBinary = Binary.parse_hex( source ) if source.endswith( ".hex" ) else Binary.parse_srec( source )

		# local variables
		labelCounter = 0
		statements = {}
		labels = {}
		found = True
		wordAddress = 0
		wordBytes = 0
		word = []
		address = sorted( sourceBinary.keys() )
		i = 0

		while True:

			# SREC format may need null byte appended for valid instruction
			if i == len( address ):
				if not found:
					address.append( byteAddress + 1 )
					sourceBinary[ byteAddress + 1 ] = "00000000"
				else:
					break

			# get next byte
			byteAddress = address[i]
			i += 1

			# instruction words vary in size so:
			# look for larger word instruction if didn't match smaller word
			if not found:
				# maximum word size
				if wordBytes >= 4:
					raise ValueError( "Unrecognised opcode: {0}".format( opcode ) )
				# increase size
				word.append( sourceBinary[byteAddress] )
				wordBytes += 1
		
			# if last word did match, start new word
			else:
				word = [ sourceBinary[ byteAddress] ]
				found = False
				wordBytes = 1
				wordAddress = byteAddress
			
			# some architectures only support specific word sizes
			# only match word size instructions
			if wordBytes % bytesInWord != 0:
				continue

			# convert word to opcode
			# words are big endian
			# instructions are little endian 
			# e.g. ATMega64 32-bit instruction is bytes [ 1, 0, 3, 2 ]
			opcode = ""
			for w in range( 0, wordBytes, bytesInWord ):
				for b in range( 0, bytesInWord ):
					opcode += word[ w + bytesInWord - b - 1 ]

			# attempt to match against statements
			for regex in generatedStatements.keys():
				
				# attempt to match
				if regex != "" and re.match( regex, opcode ):
					
					# get matching statement
					statement = generatedStatements[ regex ]
					
					# parse operands in statement
					label,statement = Disassembler.parse_opcode( opcode, statement, tokeniser, wordAddress, labelCounter, bytesInWord )
					
					# save as address indexed statement
					statements[ wordAddress ] = statement
					
					# if a branch/jump make new label
					if label:
						labelList = labels.get( label[1], list() )
						labelList.append( label[0] )
						labels[ label[1] ] = labelList
						labelCounter += 1
					found = True
					break

		if not found:
			raise ValueError( "Unrecognised opcode: {0}".format( opcode ) )

		# output chla
		f = open( out, "w" )

		# reintroduce definitions file for human readable naming
		if definitionsFile:
			f.write( '#include "{0}"\n'.format( definitionsFile ) )

		# write each statement/label at address
		for byte in sorted( list( set ( list( statements.keys() ) + list( labels.keys() ) ) ) ):
			if labels.get( byte ):
				for l in labels[ byte ]:
					f.write( l + ":" + "\n" )
			if statements.get( byte ):
				f.write( statements[ byte ].chla_string() + "\n" )

		f.close()

	def parse_opcode( line, s, t, byteAddress, labelCounter, bytesInWord ):
		""" extracts value of operands from generatedStatements """
		
		operands = {}
		label = None
		
		# read the CHLA from the specification document to see what operands it expects
		for token in s.chla():
			
			# if an operand is found
			if isinstance( token, Operand ):
			
				# Label
				if token.name() == 'l': 
				
					# unfortunately, the specification document does not describe the sourceBinary representation specific to each instruction
					# As the representation changes depending on the jump/branch they have been special cased below
				
					# extract as raw unsigned number
					num = Disassembler.extract_value( token.name(), s.opcode(), line )
					
					# rjmp - 12 bit excess 2048
					if s.asm()[0] == Instructions.RJMP:
						excess = (num - 4095) if num > 2048 else ( num + 1 )
						val = excess * bytesInWord + byteAddress

					# jmp - unsigned absolute jump
					elif s.asm()[0] == Instructions.JMP:
						val = num * bytesInWord 
					
					# brbc, brbs - 7 bit two's complement
					elif s.asm()[0] == Instructions.BRBC or s.asm()[0] == Instructions.BRBS:
						val = ( num - 128 if num > 63 else num ) + byteAddress + 1

					# breq, brge, brlt, brlo, brne, brmi, brpl, brsh- 7 bit two's complement
					elif s.asm()[0] == Instructions.BREQ or s.asm()[0] == Instructions.BRGE or s.asm()[0] == Instructions.BRLT or s.asm()[0] == Instructions.BRLO or s.asm()[0] == Instructions.BRNE or s.asm()[0] == Instructions.BRMI or s.asm()[0] == Instructions.BRPL or s.asm()[0] == Instructions.BRSH:
						val = ( num - 128 if num > 63 else num ) + byteAddress + 1

					# bra
					elif s.asm()[0] == Instructions.BRA:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# dbnz
					elif s.asm()[0] == Instructions.DBNZA or s.asm()[0] == Instructions.DBNZX or s.asm()[0] == Instructions.DBNZ:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# BSR 
					elif s.asm()[0] == Instructions.BSR:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# CBEQ 
					elif s.asm()[0] == Instructions.CBEQ:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# CBEQX 
					elif s.asm()[0] == Instructions.CBEQX:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# CBEQA
					elif s.asm()[0] == Instructions.CBEQA:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# bne 
					elif s.asm()[0] == Instructions.BNE:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# cbeqx 
					elif s.asm()[0] == Instructions.CBEQX:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# brset 
					elif s.asm()[0] == Instructions.BRSET:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# dbnx 
					elif s.asm()[0] == Instructions.DBNX:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# bhs 
					elif s.asm()[0] == Instructions.BHS:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# blo
					elif s.asm()[0] == Instructions.BLO:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# beq 
					elif s.asm()[0] == Instructions.BEQ:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# bge 
					elif s.asm()[0] == Instructions.BGE:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# bgt 
					elif s.asm()[0] == Instructions.BGT:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# bhcc 
					elif s.asm()[0] == Instructions.BHCC:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# bhcs 
					elif s.asm()[0] == Instructions.BHCS:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# bhi 
					elif s.asm()[0] == Instructions.BHI:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# bih
					elif s.asm()[0] == Instructions.BIH:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# bil
					elif s.asm()[0] == Instructions.BIL:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# ble 
					elif s.asm()[0] == Instructions.BLE:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# bls 
					elif s.asm()[0] == Instructions.BLS:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# blt 
					elif s.asm()[0] == Instructions.BLT:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# bmc 
					elif s.asm()[0] == Instructions.BMC:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# bmi 
					elif s.asm()[0] == Instructions.BMI:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# bms 
					elif s.asm()[0] == Instructions.BMS:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# bne 
					elif s.asm()[0] == Instructions.BNE:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# bpl 
					elif s.asm()[0] == Instructions.BPL:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# brclr 
					elif s.asm()[0] == Instructions.BRCLR:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# brset
					elif s.asm()[0] == Instructions.BRSET:
						val = ( ( num - 256 ) if num > 127 else num ) + byteAddress + 2

					# call 
					elif s.asm()[0] == Instructions.CALL:
						val = num * 2 
					
					# jsr 
					elif s.asm()[0] == Instructions.JSR:
						val = num 
					
					# rcall 
					elif s.asm()[0] == Instructions.RCALL:
						val = ( ( (num - 4095) if num > 2048 else ( num + 1 ) ) * 2 ) + byteAddress 

					else:
						raise ValueError( "Unrecognised branch: {0}".format( s.asm()[0] ) )

					# make up sequential label for jump/branch
					name = "l" + str( labelCounter )
					
					# save 'l' operand
					operands[ token.name() ] = Label( name, val )
					
					# return label independently
					label = ( name, val )
				
				
				# Single Value
				elif isinstance( token.range(), Range ):
					
					# some operands represent constants
					# if allowed range is low == high, set value = low = high
					if token.range().low() == token.range().high():
						num = token.range().low()
						val = num
					
					# extract value and adjust for offset
					else:
						num = Disassembler.extract_value( token.name(), s.opcode(), line )
						val = num + token.range().low()
					
					# attempt to reconcile variable names from definitions file for greater readability
					if token.name() in [ 'd', 'r' ]:
						name = t.name_from_value( val )
					else:
						name = ""
					
					# save operand
					operands[ token.name() ] = Value( name, val )

				# Pair Value
				elif isinstance( token.range(), PairRange ):
					
					# some operands represent constants
					# if constant range, set value to constant
					if token.range().first().low() == token.range().first().high() and token.range().second().low() == token.range().second().high():
						first = token.range().first().low()
						second = token.range().second().low()
						fName = t.name_from_value( first )
						sName = t.name_from_value( second )
					
					# extract value and adjust for offset
					else:
						num = Disassembler.extract_value( token.name(), s.opcode(), line ) 
						first = num * 2 + token.range().first().low()
						second = num * 2 + token.range().second().low()
						fName = t.name_from_value( first )
						sName = t.name_from_value( second )
					
					# save operand
					operands[ token.name() ] = Pair( Value( fName, first ), Value( sName, second ) )


		return ( label, s.statement_from_opcode( operands ) )


	def extract_value( char, opcode, line ):
		"""Recursively extract operand from opcode that match 'char'"""
		
		val = ""
		opcode = list( opcode )

		try:
			while True:
				pos = opcode.index( char )
				val += line[pos]
				opcode[pos] = "X"
		except ValueError:
			pass

		if val == "":
			raise ValueError( "invalid value char '{0}' in {1} on line {2}".format( char, opcode, line ) )

		return int( val, 2 )

