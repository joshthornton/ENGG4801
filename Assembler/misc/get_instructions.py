import csv 

f= open( "test/hcs08.spec" )
reader = csv.reader( f, delimiter = "," )

d = {}

for lineno,parts in enumerate( reader ):
    instr = parts[0].split( " " )[0]

    if ( d.get( instr ) == None ):
        d[instr] = 0

f= open( "test/atmega64.spec" )
reader = csv.reader( f, delimiter = "," )

for lineno,parts in enumerate( reader ):
    instr = parts[0].split( " " )[0]

    if ( d.get( instr ) == None ):
        d[instr] = 0

for instr in sorted( d.keys() ):
    print( "\t{0}\t\t=\tInstruction( \"{1}\" )".format( instr.upper(), instr.lower() ) )
