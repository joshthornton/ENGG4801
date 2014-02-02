from chla.Keywords import *
from chla.Operators import *
from chla.Value import *
from chla.Label import *
import re

class Tokeniser:
	"""Reads in source file and scans/tokenises the input"""
	
	def __init__( self, source, definitions ):
		self.definitions = definitions
		self.lines = self.preprocess( source )
	
	def name_from_value( self, value ):
		"""Reconcile a value to a name from definitions file for greater readability"""
		for ( n, v ) in self.definitions.items():
			if value == v:
				return n
		return ""
	
	def preprocess( self, source ):
		"""Reads in pre-processor directives and evaulates them"""

		# open file
		files = []
		files.append( open( source ) )

		# Output
		lines = []
		
		# depth and value of conditional directives
		skip = [ False ]
		
		# whilst there are still files to preprocess
		while len( files ) > 0:
			
			while True:
				
				# get line from current file
				line = files[-1].readline()
				
				if line != "":
					
					# pre-processor directive
					if line.startswith( "#" ):

						# Include
						match = re.match( '#include\s+"(.*)"\s*$', line )
						if match:
							if not skip[ -1 ]:
								files.append( open( match.group( 1 ) ) )
							continue

						# Definition
						match = re.match( '#define\s+(\S+)\s+(\S+)\s*$', line )
						if match:
							if not skip[ -1 ]:
								
								# Check if recursive definition
								value = self.definitions.get( match.group( 2 ), match.group( 2 ) )
								
								# if determined to be an int, stop processing
								if isinstance( value, int ):
									self.definitions[ match.group( 1 ) ] = value
								
								# attempt to evaluate complex expression
								else:
									try:
										self.definitions[ match.group( 1 ) ] = eval( value, self.definitions )
									except Exception as e:
										
										# could not parse as expression, assume constant
										self.definitions[ match.group( 1 ) ] = value
						
							continue

						# if defined 
						match = re.match( '#ifdef\s+(\S+)\s*$', line )
						if match:
							if not skip[ -1 ]:
								if match.group( 1 ) in self.definitions:
									skip.append( False )
								else:
									skip.append( True )
							continue

						# if not defined 
						match = re.match( '#ifndef\s+(\S+)\s*$', line )
						if match:
							if not skip[ -1 ]:
								if match.group( 1 ) in self.definitions:
									skip.append( True )
								else:
									skip.append( False )
							continue

						# end if
						match = re.match( '#endif\s*$', line )
						if match:
							if len( skip ) <= 1:
								raise ValueError( "Unexpected #endif" )
							else:
								skip.pop( -1 )
							continue

						# else
						match = re.match( '#else\s*$', line )
						if match:
							skip[ -1 ] = not skip[ -1 ]	
							continue

						raise ValueError( "Unrecognised preprocessor directive: {0}".format( line ) )
							
					elif not skip[ -1 ]:
						lines.append( line )
				
				else:
					f = files.pop()
					f.close()
					break

		return lines

	def tokenise( self ):

		lines = {}
		labels = {}

		# go through each line
		for lineno,line in enumerate( self.lines ):
			
			tokens = []
			
			# tokenise as:
			# label,
			# pair,
			# number, or
			# operator
			parts = re.findall( "(([a-zA-Z0-9]+)(:)$)|([a-zA-Z0-9_]+:[a-zA-Z0-9_]+)|(-?(?!=)[a-zA-Z0-9_]+)|([\+!=&~\-\^\.\|<>\[\]\*:/]+|\(|\))", line ) 

			for t in parts:

				# if label
				if t[1] != "":
					
					# check not duplicate
					if labels.get( t[1] ):
						raise ValueError( "Duplicate label '{0}' encountered on line {1}, previously seen on line {2}".format( t[1], lineno, labels.get( t[1] ) ) )
					
					# save label
					else:
						labels[ t[1] ] = lineno
						tokens.append( Label( t[1], None ) )
			
				# get correct match
				token = t[2] if t[2] != "" else t[3] if t[3] != "" else t[4] if t[4] != "" else t[5]

				# attempt to parse and save
				try:
					tokens.append( self.parse_token( token ) )
				except ValueError as e:
					print( "Could not parse token '{0}' on line {1}".format( token, lineno ) )
					exit()

			if len( tokens ) > 0:
				lines[lineno] = tokens
		
		return labels,lines


	def parse_token( self, token ):
		

		# definition
		if token in self.definitions.keys():
			if isinstance( self.definitions[ token ], int ):
				return Value( token, self.definitions[ token ] )
			else:
				token = self.definitions[ token ]

		# keyword
		for k in Keywords():
			if token.lower() == str( k ):
				return k

		# value
		if re.match( "(0x[0-9A-Fa-f]+)|(-?[0-9]+)", token ):
			return Value( "", int( token, 0 ) )
		
		# operator
		if re.match( "[\+!=&~\-\^\.\|<>\[\]\(\)\*:/]+", token ):
			for op in Operators():
				if token == str( op ):
					return op
			raise ValueError( "Operator not recognised: " + token )

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

		# assume label
		return Label( token, None )
