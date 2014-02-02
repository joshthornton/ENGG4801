import inspect

class Instruction:
	"""Abstract representation of an assembly instruction"""
	
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
	ADIW		=	Instruction( "adiw" )
	AIS		=	Instruction( "ais" )
	AIX		=	Instruction( "aix" )
	AND		=	Instruction( "and" )
	ANDI		=	Instruction( "andi" )
	ASR		=	Instruction( "asr" )
	ASRA		=	Instruction( "asra" )
	ASRX		=	Instruction( "asrx" )
	BCC		=	Instruction( "bcc" )
	BCLR		=	Instruction( "bclr" )
	BCS		=	Instruction( "bcs" )
	BEQ		=	Instruction( "beq" )
	BGE		=	Instruction( "bge" )
	BGT		=	Instruction( "bgt" )
	BHCC		=	Instruction( "bhcc" )
	BHCS		=	Instruction( "bhcs" )
	BHI		=	Instruction( "bhi" )
	BHS		=	Instruction( "bhs" )
	BIH		=	Instruction( "bih" )
	BIL		=	Instruction( "bil" )
	BIT		=	Instruction( "bit" )
	BLD		=	Instruction( "bld" )
	BLE		=	Instruction( "ble" )
	BLO		=	Instruction( "blo" )
	BLS		=	Instruction( "bls" )
	BLT		=	Instruction( "blt" )
	BMC		=	Instruction( "bmc" )
	BMI		=	Instruction( "bmi" )
	BMS		=	Instruction( "bms" )
	BNE		=	Instruction( "bne" )
	BPL		=	Instruction( "bpl" )
	BRA		=	Instruction( "bra" )
	BRBC		=	Instruction( "brbc" )
	BRBS		=	Instruction( "brbs" )
	BRCLR		=	Instruction( "brclr" )
	BREQ		=	Instruction( "breq" )
	BRGE		=	Instruction( "brge" )
	BRLO		=	Instruction( "brlo" )
	BRLT		=	Instruction( "brlt" )
	BRMI		=	Instruction( "brmi" )
	BRNE		=	Instruction( "brne" )
	BRPL		=	Instruction( "brpl" )
	BRSET		=	Instruction( "brset" )
	BRSH		=	Instruction( "brsh" )
	BSET		=	Instruction( "bset" )
	BSR		=	Instruction( "bsr" )
	BST		=	Instruction( "bst" )
	CALL		=	Instruction( "call" )
	CBEQ		=	Instruction( "cbeq" )
	CBEQA		=	Instruction( "cbeqa" )
	CBEQX		=	Instruction( "cbeqx" )
	CBI		=	Instruction( "cbi" )
	CLC		=	Instruction( "clc" )
	CLI		=	Instruction( "cli" )
	CLR		=	Instruction( "clr" )
	CLRA		=	Instruction( "clra" )
	CLRH		=	Instruction( "clrh" )
	CLRX		=	Instruction( "clrx" )
	CMP		=	Instruction( "cmp" )
	COM		=	Instruction( "com" )
	COMA		=	Instruction( "coma" )
	COMX		=	Instruction( "comx" )
	CP		=	Instruction( "cp" )
	CPC		=	Instruction( "cpc" )
	CPHX		=	Instruction( "cphx" )
	CPI		=	Instruction( "cpi" )
	CPSE		=	Instruction( "cpse" )
	CPX		=	Instruction( "cpx" )
	DBNX		=	Instruction( "dbnx" )
	DBNZ		=	Instruction( "dbnz" )
	DBNZA		=	Instruction( "dbnza" )
	DBNZX		=	Instruction( "dbnzx" )
	DEC		=	Instruction( "dec" )
	DECA		=	Instruction( "deca" )
	DECX		=	Instruction( "decx" )
	DIV		=	Instruction( "div" )
	EOR		=	Instruction( "eor" )
	FMUL		=	Instruction( "fmul" )
	FMULS		=	Instruction( "fmuls" )
	FMULSU		=	Instruction( "fmulsu" )
	ICALL		=	Instruction( "icall" )
	IJMP		=	Instruction( "ijmp" )
	IN		=	Instruction( "in" )
	INC		=	Instruction( "inc" )
	INCA		=	Instruction( "inca" )
	INCX		=	Instruction( "incx" )
	JMP		=	Instruction( "jmp" )
	JSR		=	Instruction( "jsr" )
	LDA		=	Instruction( "lda" )
	LDHX		=	Instruction( "ldhx" )
	LDX		=	Instruction( "ldx" )
	LSL		=	Instruction( "lsl" )
	LSLA		=	Instruction( "lsla" )
	LSLX		=	Instruction( "lslx" )
	LSR		=	Instruction( "lsr" )
	LSRA		=	Instruction( "lsra" )
	LSRX		=	Instruction( "lsrx" )
	MOV		=	Instruction( "mov" )
	MOVW		=	Instruction( "movw" )
	MUL		=	Instruction( "mul" )
	MULS		=	Instruction( "muls" )
	MULSU		=	Instruction( "mulsu" )
	NEG		=	Instruction( "neg" )
	NEGA		=	Instruction( "nega" )
	NEGX		=	Instruction( "negx" )
	NOP		=	Instruction( "nop" )
	NSA		=	Instruction( "nsa" )
	OR		=	Instruction( "or" )
	ORA		=	Instruction( "ora" )
	ORI		=	Instruction( "ori" )
	OUT		=	Instruction( "out" )
	POP		=	Instruction( "pop" )
	PSHA		=	Instruction( "psha" )
	PSHH		=	Instruction( "pshh" )
	PSHX		=	Instruction( "pshx" )
	PULA		=	Instruction( "pula" )
	PULH		=	Instruction( "pulh" )
	PULX		=	Instruction( "pulx" )
	PUSH		=	Instruction( "push" )
	RCALL		=	Instruction( "rcall" )
	RET		=	Instruction( "ret" )
	RETI		=	Instruction( "reti" )
	RJMP		=	Instruction( "rjmp" )
	ROL		=	Instruction( "rol" )
	ROLA		=	Instruction( "rola" )
	ROLX		=	Instruction( "rolx" )
	ROR		=	Instruction( "ror" )
	RORA		=	Instruction( "rora" )
	RORX		=	Instruction( "rorx" )
	RTI		=	Instruction( "rti" )
	RTS		=	Instruction( "rts" )
	SBC		=	Instruction( "sbc" )
	SBCI		=	Instruction( "sbci" )
	SBI		=	Instruction( "sbi" )
	SBIC		=	Instruction( "sbic" )
	SBIS		=	Instruction( "sbis" )
	SBIW		=	Instruction( "sbiw" )
	SBRC		=	Instruction( "sbrc" )
	SBRS		=	Instruction( "sbrs" )
	SEC		=	Instruction( "sec" )
	SEI		=	Instruction( "sei" )
	SLEEP		=	Instruction( "sleep" )
	STA		=	Instruction( "sta" )
	STHX		=	Instruction( "sthx" )
	STX		=	Instruction( "stx" )
	SUB		=	Instruction( "sub" )
	SUBI		=	Instruction( "subi" )
	SWAP		=	Instruction( "swap" )
	TAP		=	Instruction( "tap" )
	TAX		=	Instruction( "tax" )
	TPA		=	Instruction( "tpa" )
	TST		=	Instruction( "tst" )
	TSTA		=	Instruction( "tsta" )
	TSTX		=	Instruction( "tstx" )
	TSX		=	Instruction( "tsx" )
	TXA		=	Instruction( "txa" )
	TXS		=	Instruction( "txs" )
	WDR		=	Instruction( "wdr" )
	LD		=	Instruction( "ld" )
	LDD		=	Instruction( "ldd" )
	LDI		=	Instruction( "ldi" )
	LDS		=	Instruction( "lds" )
	LPM		=	Instruction( "lpm" )
	SPM		=	Instruction( "spm" )
	ST		=	Instruction( "st" )
	STD		=	Instruction( "std" )
	STS		=	Instruction( "sts" )

	def __iter__(self):
		return ( v for k, v in inspect.getmembers( self ) if not k.startswith( '__' ) )