import inspect

class Instruction:
	def __init__( self, name ):
		self._name = name
	
	def __str__( self ):
		return self._name
	
	def __repr__( self ):
		return "Instruction: {0}".format( self._name )
	
	def __eq__( self, other ):
		if isinstance( other, Instruction ):
			return self._name == other._name
		return False
	
	def __key( self ):
		return ( self._name )
	
	def __hash__( self ):
		return hash( self.__key() )
	
	def asm( self ):
		return self._name

class Instructions:
	ADC		=	Instruction( "adc" )
	ADD		=	Instruction( "add" )
	ADIW	=	Instruction( "adiw" )
	AND		=	Instruction( "and" )
	ANDI	=	Instruction( "andi" )
	COM		=	Instruction( "com" )
	CP		=	Instruction( "cp" )
	CPC		=	Instruction( "cpc" )
	CPI		=	Instruction( "cpi" )
	DEC		=	Instruction( "dec" )
	EOR		=	Instruction( "eor" )
	FMUL	=	Instruction( "fmul" )
	FMULS	=	Instruction( "fmuls" )
	FMULSU	=	Instruction( "fmulsu" )
	INC		=	Instruction( "inc" )
	LSL		=	Instruction( "lsl" )
	LSR		=	Instruction( "lsr" )
	MUL		=	Instruction( "mul" )
	MULS	=	Instruction( "muls" )
	MULSU	=	Instruction( "mulsu" )
	NEG		=	Instruction( "neg" )
	OR		=	Instruction( "or" )
	ORI		=	Instruction( "ori" )
	SBC		=	Instruction( "sbc" )
	SBCI	=	Instruction( "sbci" )
	SBIW	=	Instruction( "sbiw" )
	SUB		=	Instruction( "sub" )
	SUBI	=	Instruction( "subi" )
	ASR		=	Instruction( "asr" )
	BCLR	=	Instruction( "bclr" )
	BLD		=	Instruction( "bld" )
	BSET	=	Instruction( "bset" )
	BST		=	Instruction( "bst" )
	CBI		=	Instruction( "cbi" )
	ROL		=	Instruction( "rol" )
	ROR		=	Instruction( "ror" )
	SBI		=	Instruction( "sbi" )
	SWAP	=	Instruction( "swap" )
	BRBC	=	Instruction( "brbc" )
	BRBS	=	Instruction( "brbs" )
	CALL	=	Instruction( "call" )
	CPSE	=	Instruction( "cpse" )
	ICALL	=	Instruction( "icall" )
	IJMP	=	Instruction( "ijmp" )
	JMP		=	Instruction( "jmp" )
	RCALL	=	Instruction( "rcall" )
	RET		=	Instruction( "ret" )
	RETI	=	Instruction( "reti" )
	RJMP	=	Instruction( "rjmp" )
	SBIC	=	Instruction( "sbic" )
	SBIS	=	Instruction( "sbis" )
	SBRC	=	Instruction( "sbrc" )
	SBRS	=	Instruction( "sbrs" )
	IN		=	Instruction( "in" )
	MOV		=	Instruction( "mov" )
	MOVW	=	Instruction( "movw" )
	OUT		=	Instruction( "out" )
	POP		=	Instruction( "pop" )
	PUSH	=	Instruction( "push" )
	SLEEP	=	Instruction( "sleep" )
	WDR		=	Instruction( "wdr" )
	LD		=	Instruction( "ld" )
	LDD		=	Instruction( "ldd" )
	LDI		=	Instruction( "ldi" )
	LDS		=	Instruction( "lds" )
	LPM		=	Instruction( "lpm" )
	SPM		=	Instruction( "spm" )
	ST		=	Instruction( "st" )
	STS		=	Instruction( "sts" )


	def __iter__(self):
		return ( v for k, v in inspect.getmembers( self ) if not k.startswith( '__' ) )
