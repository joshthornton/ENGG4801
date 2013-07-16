from Keywords import *
from Operators import *
from Value import *
from Label import *
import re

class Tokeniser:
	
	def __init__( self, definitions ):
		self.definitions = {}
		self.load_definitions( definitions )
	
	def load_definitions( self, definitions ):
		
		# open file
		f = open( definitions )

		# extract each definition
		for line in f:
			parts = line.rstrip().split( "=" )
			name = parts[0]
			value = self.definitions.get( parts[1], parts[1] )
			try:
				self.definitions[name] = int( value, 0 )
			except Exception as e:
				print( "Could not parse '{0}' as integer".format( value ) )
				exit()

		# close file
		f.close()		
	
	def tokenise( self, source  ):

		# open file
		f = open( source )

		lines = {}
		labels = {}

		# go through each line
		for lineno,line in enumerate( f ):
			
			tokens = []
			parts = re.findall( "(([a-zA-Z0-9]+)(:)$)|([a-zA-Z0-9]+:[a-zA-Z0-9]+)|([a-zA-Z0-9]+)|([\+=&~\-\^\.\|<>\[\]\(\)\*:]+)", line ) 

			for t in parts:	

				if t[1] != "":
					if labels.get( t[1] ):
						print( "Duplicate label '{0}' encountered on line {1}, previously seen on line {2}".format( t[1], lineno, labels.get( t[1] ) ) )
						exit()
					else:
						labels[ t[1] ] = lineno
						tokens.append( Label( t[1] ) )

				token = t[2] if t[2] != "" else t[3] if t[3] != "" else t[4] if t[4] != "" else t[5]

				try:
					tokens.append( self.parse_token( token ) )
				except ValueError as e:
					print( "Could not parse token '{0}' on line {1}".format( token, lineno ) )
					exit()

			if len( tokens ) > 0:
				lines[lineno] = tokens

		f.close()
		
		return labels,lines

	def parse_token( self, token ):

		# definition
		if token in self.definitions.keys():
			return Value( token, self.definitions[ token ] )

		# keyword
		for k in Keywords():
			if token.lower() == str( k ):
				return k

		# operator
		if re.match( "[\+=&~\-\^\.\|<>\[\]\(\)\*]+", token ):
			for op in Operators():
				if token == str( op ):
					return op
			raise ValueError()

		# pair
		if re.match( "([a-zA-Z0-9]+:([a-zA-Z0-9]+))", token ):
			tokens = token.split(":")
			first = self.parse_token( tokens[0] )
			second = self.parse_token( tokens[1] )
			if not isinstance( first, Value ):
				raise ValueError( "Pair must contain two values. {0} is not a value".format( str( first ) ) )
			if not isinstance( second, Value ):
				raise ValueError( "Pair must contain two values. {0} is not a value".format( str( second ) ) )
			return Pair( first, second )

		# value
		if re.match( "(0x[0-9A-Fa-f]+)|([0-9]+)", token ):
			return Value( "", int( token, 0 ) )

		# assume label
		return Label( token )