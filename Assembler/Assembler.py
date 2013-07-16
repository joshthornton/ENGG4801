from Generator import *
from Tokeniser import *

class Assembler:

	def assemble( spec, definition, source, out ):
		
		t = Tokeniser( definition )
		tree = Generator.generate( spec, t ) 
		labels,program = t.tokenise( source ) 
		
		statements = []
		for lineno,statement in program.items():
			template = Assembler.match( tree, statement )
			if template:
				statements.append( template.statement( statement ) )
			else:
				raise ValueError( "ERROR line {0}: Could not match '{1}'".format( lineno, " ".join( [ str( t ) for t in statement ] ) ) )
		
		f = open( out, "w" )
		for s in statements:
			f.write( s.asm() + "\n" )
		f.close()
	
	def match( node, hlasm ):

		if len( hlasm ) == 0:
			return node.get( Keywords.END ) 

		for n in node:
			if n == hlasm[0]:
				r = Assembler.match( node[n], hlasm[1:] )
				if r:
					return r

		return None
