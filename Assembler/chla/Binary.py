import re

class Binary:

	def parse_hex( hex ):
		""" parse_hex( hexfile ) -> address indexed opcodes"""

		# open file
		h = open( hex )
		# output
		output = {}

		# hex file default base address is 0
		base = 0
		
		for i,line in enumerate(h):
		
		# check valid hex format
			match = re.match( "^:([0-9a-fA-f]{2})([0-9a-fA-f]{4})([0-9a-fA-f]{2})([0-9a-fA-f]*)([0-9a-fA-f]{2})$", line )

			if match:
				
				# number of bytes
				count = int( match.group( 1 ), 16 )
				
				# starting address
				address = int( match.group( 2 ), 16 )
				
				# data or otherwise
				type = int( match.group( 3 ), 16 )
				
				# actual data
				data = match.group( 4 )
				
				# checksum
				checksum = int( match.group( 5 ), 16 )
			
				# address data
				if type == 2:
					base = 16 * int( data, 16 )
				
				# program data
				elif type == 0:
					# split into bytes
					for i in range( 0, len(data), 2 ):
						output[ int(base + address + (i/2)) ] = (bin( int( data[i:i+2], 16 ) )[2:]).zfill(8) # strip 0b from fron of binary, pad to 8 bits
				
				# EOF
				elif type == 1:
					break
						
				# unrecognised
				else:
					raise ValueError( "Invalid record type " + str( type ) + " on line " + str(i) )
			else:
				raise ValueError( "invalid line " + str(i) + ": " + line )
		
		return output
	
	def parse_srec( srec ):
		""" parse_srec( srecfile ) -> address index opcodes """
		
		# open file
		h = open( srec )
		# output
		output = {}

		for i,line in enumerate(h):
			
			# match block header
			match = re.match( "^S0([0-9a-fA-f]{2})([0-9a-fA-f]{4})([0-9a-fA-f]*)([0-9a-fA-f]{2})$", line )
			if match:
				continue

			# match data sequence 1
			match = re.match( "^S1([0-9a-fA-f]{2})([0-9a-fA-f]{4})([0-9a-fA-f]*)([0-9a-fA-f]{2})$", line )
			if match:
				count = int( match.group( 1 ), 16 )
				address = int( match.group( 2 ), 16 )
				data = match.group( 3 )
				checksum = int( match.group( 4 ), 16 )
				# split into bytes
				for i in range( 0, len(data), 2 ):
					# strip 0b from fron of binary, pad to 8 bits
					output[ int(address + (i/2)) ] = (bin( int( data[i:i+2], 16 ) )[2:]).zfill(8)
				continue

			# match data sequence 2
			match = re.match( "^S1([0-9a-fA-f]{2})([0-9a-fA-f]{6})([0-9a-fA-f]*)([0-9a-fA-f]{2})$", line )
			if match:
				count = int( match.group( 1 ), 16 )
				address = int( match.group( 2 ), 16 )
				data = match.group( 3 )
				checksum = int( match.group( 4 ), 16 )
				# split into bytes
				for i in range( 0, len(data), 2 ):
					# strip 0b from fron of binary, pad to 8 bits
					output[ int(address + (i/2)) ] = (bin( int( data[i:i+2], 16 ) )[2:]).zfill(8)
				continue
			
			# match data sequence 3
			match = re.match( "^S1([0-9a-fA-f]{2})([0-9a-fA-f]{8})([0-9a-fA-f]*)([0-9a-fA-f]{2})$", line )
			if match:
				count = int( match.group( 1 ), 16 )
				address = int( match.group( 2 ), 16 )
				data = match.group( 3 )
				checksum = int( match.group( 4 ), 16 )
				# split into bytes
				for i in range( 0, len(data), 2 ):
					# strip 0b from fron of binary, pad to 8 bits
					output[ int(address + (i/2)) ] = (bin( int( data[i:i+2], 16 ) )[2:]).zfill(8)
				continue

			# match count, or end block
			match = re.match( "^S([5-9])([0-9a-fA-f]{2})([0-9a-fA-f]{4})([0-9a-fA-f]*)([0-9a-fA-f]{2})$", line )

			if match:
				break
			
			raise ValueError( "invalid line " + str(i) + ": " + line )
		return output
