from chla.Generator import *
from chla.Tokeniser import *

class Assembler:

	def assemble( spec, source, out, bytesInWord, definitions ):
		"""assemble( spec, source, out, bytesInWord, definitions ): takes a specification document and source file as arguments and assembles the program into the output file"""
		
		# initialise tokeniser
		t = Tokeniser( source, definitions )
		
		# initialise parse tree
		tree = Generator.generate_tree( spec, t )
		
		# read in program
		_,program = t.tokenise()

		# first pass - calculate labels
		statements = {} 
		byteLabels = {}
		nameLabels = {}
		wordCounter = 0
		for byte in sorted( program.keys() ):
			
			# get statement
			chla = program[ byte ]
			
			# match statement to assembly instruction
			template = Assembler.match( tree, chla )

			if template:
				
				# fill in operands with values
				statements[ wordCounter ] = template.statement_from_chla( chla )
				
				# increment byte counter
				wordCounter += int( len( template.opcode() ) / ( 8 * bytesInWord ) )

			# not a statement, check if label
			elif isinstance( chla[0], Label ) and chla[1] == Operators.PAIR:

				# get all labels at that byte address
				labels = byteLabels.get( wordCounter, list() )
				labels.append( chla )

				# save address
				byteLabels[ wordCounter ] = labels 
				nameLabels[ chla[0].name() ] = wordCounter

			# no match
			else:
				raise ValueError( "ERROR byte offset {0}: Could not match '{1}'".format( byte, " ".join( [ repr( t ) for t in chla ] ) ) )

		# second pass - fill in label addresses
		
		# we stop if we reach this address
		maxByte = sorted( list( set ( list( statements.keys() ) + list( byteLabels.keys() ) ) ) )[-1]
		b = 0
		while b <= maxByte:
			
			# get next statement
			if statements.get( b ):
				s = statements[b]
			else:
				b += 1
				continue

			# get the range and value for the label operand
			labelRange,label = s.operand( 'l' )
			if label:
				
				# absolute address
				if s.instruction() == Instructions.JMP or s.instruction() == Instructions.CALL or s.instruction() == Instructions.JSR:
					addressValue = nameLabels[ label.name() ]

				# relative address
				else:
					addressValue = nameLabels[ label.name() ] - ( b + 1 )

				# update the label's value to the new address
				label.update_value( addressValue )
				
				# new value maybe outside range
				if not labelRange.check( label ):

					# try upgrade 0-255 jump to 0-65535 jump if possible 
					# this could not be done earlier as jump address was not known
					template = Assembler.match( tree, s.chla() )
					if template:
						
						# fill in operands with values
						statements[b] = template.statement_from_chla( s.chla() )
						
						# re-check range
						labelRange,label = statements[b].operand( 'l' )
						if labelRange.check( label ):

							# must relocate all bytes after this point
							mb = sorted( list( set ( list( statements.keys() ) + list( byteLabels.keys() ) ) ) )[-1]
							maxByte = mb + 1
							while mb > b:
								
								if byteLabels.get( mb ):
									byteLabels[ mb + 1 ] = byteLabels[ mb ]
									del byteLabels[ mb ]
							
								if statements.get( mb ):
									statements[ mb + 1 ] = statements[ mb ]
									del statements[ mb ]

								mb -= 1

							b += 1
							continue
					raise ValueError( "Byte Offset {0} Label '{1}' with value {2} out of range {3} in line {4}".format( b, l.name(), value, repr( r ), repr( s ) ) )
						
			# increment byte counter
			b += 1
		
		# output the assembly
		f = open( out, "w" )
		
		keys = sorted( list( set ( list( statements.keys() ) + list( byteLabels.keys() ) ) ) )
		for byteNo in keys:
			
			# Write label
			if byteLabels.get( byteNo ):
				f.write( "\n" )
				
				# write each label at this address
				for label in byteLabels.get( byteNo ):
					for token in label:
						f.write( token.asm() )
					f.write( "\n" )

			# Write each statement at this address
			if statements.get( byteNo ):
				# Write ASM
				asm = statements[ byteNo ].asm_string()

				# Write chla comment
				#chla = ""
				chla = ( ( 4 - int( len( asm ) / 8 ) ) * "\t" ) + "; " + statements[ byteNo ].chla_string()

				# Write line
				f.write( asm + chla + "\n" )

		# close file
		f.close()
	
	def match( node, chla ):
		"""recursively matches chla against the parse tree"""

		if len( chla ) == 0:
			# no more tokens to match
			# Return the leaf node if it exists
			return node.get( Keywords.LEAF ) 

		for n in node:
			# try all branches at current node
			if n.match( chla[0] ):
				# next token matches
				# continue down branch
				r = Assembler.match( node[n], chla[1:] )
				if r:
					# successfully matched statement at leaf 
					return r
		
		return None
