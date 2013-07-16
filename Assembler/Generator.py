from Keywords import *
from Range import *
from Operators import *
from Value import *
from Label import *
from Operand import *
from Instructions import *
from Tokeniser import *
from Statement import *
import re
import csv 

class Generator:
		
	def generate( spec, tokeniser ):
 
		# open file
		f= open( spec )
		reader = csv.reader( f, delimiter = "," )

		tree = {}

		for lineno,parts in enumerate( reader ):

			try:
				# parse ranges
				d = Generator.parse_range( parts[2] )
				r = Generator.parse_range( parts[3] )
				k = Generator.parse_range( parts[4] )
				b = Generator.parse_range( parts[5] )

				# variable positions
				operandPositions = {}
				
				# parse asm
				asm = []
				for token in parts[0].split( " " ):
					if token != "":
						asm.append( Generator.parse_asm( token, d, r, k, b ) )
	
				# parse opcode
				opcode = parts[6]
	
				# parse hlasm
				hlasm = []
				for token in parts[1].split( " " ):
					if token != "":
						t = Generator.parse_hlasm( token, tokeniser, d, r, k, b )
						if isinstance( t, Operand ):
							operandPositions[ t.name() ] = len( hlasm )
						hlasm.append( t )
	
				# add to tree
				node = tree
				for token in hlasm:
					if token not in node:
						node[token] = {}
					node = node[token]
	
				node[ Keywords.END ] = StatementTemplate( asm, hlasm, opcode, operandPositions )
			except ValueError as e:
				print( "ERROR line {0}: {1}".format( lineno, " ".join( parts ) ) )
				print( e )
				exit()	

		return tree

	def parse_hlasm( token, tokeniser, d, r, k, b ):
		# operand
		operand = Generator.parse_operand( token, d, r, k, b )
		if operand:
			return operand

		return tokeniser.parse_token( token )

	def parse_range( r ):
		
		if r == "":
			return None

		# pair range
		matches = re.match( "([0-9]+):([0-9]+)\-([0-9]+):([0-9]+)", r )
		if matches:
			return PairRange( ( int( matches.group( 1 ) ), int( matches.group( 3 ) ) ), ( int( matches.group( 2 ) ), int( matches.group( 4 ) ) ) )

		# single pair
		matches = re.match( "([0-9]+):([0-9]+)", r )
		if matches:
			return PairRange( ( int( matches.group( 1 ) ), int( matches.group( 2 ) ) ), ( int( matches.group( 1 ) ), int( matches.group( 2 ) ) ) )

		# normal range
		matches = re.match( "([0-9]+)-([0-9]+)", r )
		if matches:
			return Range( int( matches.group( 1 ) ), int( matches.group( 2 ) ) )
		
		# normal single
		matches = re.match( "([0-9]+)", r )
		if matches:
			return Range( int( matches.group( 1 ) ), int( matches.group( 1 ) ) )

	def parse_asm( token, d, r, k, b ):
		
		# operand
		operand = Generator.parse_operand( token, d, r, k, b )
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

		raise ValueError( token )
	
	def parse_operand( token, d, r, k, b ):
		
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
			return Operand( "l", None )

		return None
