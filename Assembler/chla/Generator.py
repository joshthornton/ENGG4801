from chla.Keywords import *
from chla.Range import *
from chla.Operators import *
from chla.Value import *
from chla.Label import *
from chla.Operand import *
from chla.Instructions import *
from chla.Tokeniser import *
from chla.Statement import *
from chla.Constant import *
import re
import csv 

class Generator:
		
	def generate( spec, tokeniser, callback ):
		"""Parse the specification document and call the callback with each statement parsed as the argument"""
 
		# open file as csv
		f= open( spec )
		reader = csv.reader( f, delimiter = "," )
		error = False
		
		for lineno,parts in enumerate( reader ):
			
			try:
				# clear on each loop begin
				d = None
				r = None
				k = None
				b = None
				l = None
				asm = []
				chla = []
				s = None
				opcode = None
				
				# parse ranges
				d = Generator.parse_range( parts[2] )
				r = Generator.parse_range( parts[3] )
				k = Generator.parse_range( parts[4] )
				b = Generator.parse_range( parts[5] )
				l = Generator.parse_range( parts[6] )
				operands = { 'd' : d, 'r' : d, 'k' : k, 'b' : b, 'l' : l }
				
				# operand positions: describes the index of each operand in the list of chla tokens
				operandPositions = {}
				
				# parse asm
				for token in parts[0].split( " " ):
					if token != "":
						asm.append( Generator.parse_asm( token, d, r, k, b, l ) )
	
				# parse opcode
				opcode = parts[7]
	
				# parse chla
				for token in parts[1].split( " " ):
					if token != "":
						t = Generator.parse_chla( token, tokeniser, d, r, k, b, l )
						
						# if an operand is found, record its position/index
						if isinstance( t, Operand ):
							operandPositions[ t.name() ] = len( chla )
						chla.append( t )
				
				# create template
				# statement templates are filled in when the values are added
				s = StatementTemplate( asm, chla, opcode, operandPositions, operands )

				# callback
				callback( s )

			except ValueError as e:
				print( "ERROR line {0}: {1} {2}".format( lineno, " ".join( parts ), str(e) ) )
				print( "\t", operands, s )
				print( "\t", e )
				error = True
		if error:
			exit()
	
	def generate_statements( spec, tokeniser ):
		"""Generates an opcode indexed list of statements for disassembler"""
		
		statements = {}
		def regex_statements( statement ):
			opcode = statement.opcode()
			regex = re.sub( "[drklb]", "[01]", opcode )
			statements[ regex ] = statement

		Generator.generate( spec, tokeniser, regex_statements )

		return statements
	
	def generate_tree( spec, tokeniser ):
		"""Generates a parse tree for assembler"""
		tree = {}
		def add_to_tree( statement ):
			node = tree
			for token in statement.chla():
				if token not in node:
					node[token] = {}
				node = node[token]
			if node.get( Keywords.LEAF ):
				raise ValueError( "two statements parse to same value:\n1.\t{0}\n2.\t{1}".format( node.get( Keywords.LEAF ).chla(), statement.chla() ) )
			node[ Keywords.LEAF ] = statement 

		Generator.generate( spec, tokeniser, add_to_tree )
		
		return tree
	
	def parse_chla( token, tokeniser, d, r, k, b, l ):
		"""Recognises CHLA syntax. If not an operand, defers to tokeniser to recognise tokens"""
		
		# operand
		operand = Generator.parse_operand( token, d, r, k, b, l )
		if operand:
			return operand

		return tokeniser.parse_token( token )

	def parse_range( r ):
		"""Parses the legal ranges provided in the specification document"""
		
		if r == "":
			return None

		# pair range
		matches = re.match( "([0-9]+):([0-9]+)\-([0-9]+):([0-9]+)", r )
		if matches:
			return PairRange( ( int( matches.group( 1 ) ), int( matches.group( 3 ) ) ), ( int( matches.group( 2 ) ), int( matches.group( 4 ) ) ) )

		# single pair
		matches = re.match( "([0-9]+):([0-9]+)", r )
		if matches:
			return PairRange( ( int( matches.group( 1 ) ), int( matches.group( 1 ) ) ), ( int( matches.group( 2 ) ), int( matches.group( 2 ) ) ) )

		# normal range
		matches = re.match( "(-?[0-9]+)-([0-9]+)", r )
		if matches:
			return Range( int( matches.group( 1 ) ), int( matches.group( 2 ) ) )
		
		# normal single
		matches = re.match( "(-?[0-9]+)", r )
		if matches:
			return Range( int( matches.group( 1 ) ), int( matches.group( 1 ) ) )

		return None

	def parse_asm( token, d, r, k, b, l ):
		"""Recognises and parses assembly found in the specification document"""
		
		# operand
		operand = Generator.parse_operand( token, d, r, k, b, l )
		if operand:
			return operand

		#instruction
		for instruction in Instructions():
			if token.lower() == str( instruction ):
				return instruction

		# operator
		for op in Operators():
			if token == str( op ):
				return op

        # keyword
		for kw in Keywords():
			if token.lower() == str( kw ):
				return kw

		# assume constant
		return Constant( token )
	
	def parse_operand( token, d, r, k, b, l ):
		"""Checks if token is operand and if it is ensures that a range for that operand has been found"""
		# operand
		if token == "$d":
			if d == None:
				raise ValueError( "$d operand found but range is None" )
			return Operand( "d", d )
		if token == "$r":
			if r == None:
				raise ValueError( "$r operand found but range is None" )
			return Operand( "r", r )
		if token == "$k":
			if k == None:
				raise ValueError( "$k operand found but range is None" )
			return Operand( "k", k )
		if token == "$b":
			if b == None:
				raise ValueError( "$b operand found but range is None" )
			return Operand( "b", b )
		if token == "$l":
			return Operand( "l", l )

		return None
