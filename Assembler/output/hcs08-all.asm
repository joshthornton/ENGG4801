ldhx #320			; h:x = | 320 |
txs 				; sp = h:x - | 1 |
cli 				; sreg [ i ] = | 0 |
adc #25				; a += | 25 | + c
adc 16				; a += 16 + c
adc 256				; a += 256 + c
adc 256,x			; a += mem [ 256 + x ] + c
adc 16,x			; a += mem [ 16 + x ] + c
adc ,x				; a += mem [ x ] + c
adc 256,sp			; a += mem [ 256 + sp ] + c
adc 16,sp			; a += mem [ 16 + sp ] + c
add #2				; a += | 2 |
add 16				; a += 16
add 256				; a += 256
add 256,x			; a += mem [ 256 + x ]
add 16,x			; a += mem [ 16 + x ]
add ,x				; a += mem [ x ]
add 256,sp			; a += mem [ 256 + sp ]
add 16,sp			; a += mem [ 16 + sp ]
ais #-1				; sp += | -1 |
aix #-1				; h:x += | -1 |
and #255			; a &= | 255 |
and 16				; a &= 16
and 16				; a &= 16
and 256				; a &= 256
and 256,x			; a &= mem [ 256 + x ]
and 16,x			; a &= mem [ 16 + x ]
and ,x				; a &= mem [ x ]
and 256,sp			; a &= mem [ 256 + sp ]
and 16,sp			; a &= mem [ 16 + sp ]
asr 16				; mem [ 16 ] >> 1
asra 				; a >> | 1 |
asrx 				; x >> | 1 |
asr 16,x			; mem [ 16 + x ] >> | 1 |
asr ,x				; mem [ x ] >> | 1 |
asr 16,sp			; mem [ 16 + sp ] >> | 1 |

l0:
bhs l0				; if | >= | goto l0
bclr 1,16			; mem [ 16 ] [ 1 ] = | 0 |

l1:
blo l1				; if | < | goto l1

l2:
beq l2				; if sreg [ Z ] == | 1 | goto l2

l3:
bge l3				; if >= goto l3

l4:
bgt l4				; if > goto l4

l5:
bhcc l5				; if sreg [ h ] == | 0 | goto l5

l6:
bhcs l6				; if sreg [ h ] == | 1 | goto l6

l7:
bhi l7				; if | > | goto l7

l8:
bhs l8				; if | >= | goto l8

l9:
bih l9				; if IRQ == | 1 | goto l9

l10:
bil l10				; if IRQ == | 0 | goto l10
bit #255			; a & | 255 |
bit 16				; a & 16
bit 256				; a & 256
bit 256,x			; a & mem [ 256 + x ]
bit 16,x			; a & mem [ 16 + x ]
bit ,x				; a & mem [ x ]
bit 256,sp			; a & mem [ 256 + sp ]
bit 16,sp			; a & mem [ 16 + sp ]

l11:
ble l11				; if <= goto l11

l12:
blo l12				; if | < | goto l12

l13:
bls l13				; if | <= | goto l13

l14:
blt l14				; if < goto l14

l15:
bmc l15				; if sreg [ i ] == | 0 | goto l15

l16:
bmi l16				; if sreg [ N ] == | 1 | goto l16

l17:
bms l17				; if sreg [ i ] == | 1 | goto l17

l18:
bne l18				; if sreg [ Z ] == | 0 | goto l18

l19:
bpl l19				; if sreg [ N ] == | 0 | goto l19

l20:
bra l20				; goto l20

l21:
brclr 1,16,l21			; if 16 [ 1 ] == | 0 | goto l21

l22:
brset 1,16,l22			; if 16 [ 1 ] == | 1 | goto l22
bset 1,16			; 16 [ 1 ] = | 1 |

l23:
bsr l23				; l23 ( )

l24:
cbeq 16,l24			; if a == 16 goto l24

l25:
cbeqa #255,l25			; if a == | 255 | goto l25

l26:
cbeqx #255,l26			; if x == | 255 | goto l26

l27:
cbeq 16,x+,l27			; if a == mem [ 16 + x ++ ] goto l27

l28:
cbeq 0,x+,l28			; if a == mem [ 0 + x ++ ] goto l28

l29:
cbeq 16,sp,l29			; if a == mem [ 16 + sp ] goto l29
clc 				; sreg [ c ] = | 0 |
cli 				; sreg [ i ] = | 0 |
clr 16				; 16 = | 0 |
lda #0				; a = | 0 |
ldx #0				; x = | 0 |
clrh 				; h = | 0 |
clr 16,x			; mem [ 16 + x ] = | 0 |
clr ,x				; mem [ x ] = | 0 |
clr PORTA,sp			; mem [ PORTA + sp ] = | 0 |
cmp #255			; a - | 255 |
cmp 16				; a - 16
cmp 256				; a - 256
cmp 256,x			; a - mem [ 256 + x ]
cmp 16,x			; a - mem [ 16 + x ]
cmp ,x				; a - mem [ x ]
cmp 256,sp			; a - mem [ 256 + sp ]
cmp 16,sp			; a - mem [ 16 + sp ]
com 16				; mem [ 16 ] ~= mem [ 16 ]
coma 				; a ~= a
comx 				; x ~= x
com 16,x			; mem [ 16 + x ] ~= mem [ 16 + x ]
com ,x				; mem [ x ] ~= mem [ x ]
com 16,sp			; mem [ 16 + sp ] ~= mem [ 16 + sp ]
cphx 256			; h:x - 256
cphx #65354			; h:x - | 65354 |
cphx 16				; h:x - 16
cphx 16,sp			; h:x - mem [ 16 + sp ]
cpx #255			; x - | 255 |
cpx 16				; x - 16
cpx 256				; x - 256
cpx 256,x			; x - mem [ 256 + x ]
cpx 16,x			; x - mem [ 16 + x ]
cpx ,x				; x - mem [ x ]
cpx 256,sp			; x - mem [ 256 + sp ]
cpx 16,sp			; x - mem [ 16 + sp ]

l30:
dbnz 16,l30			; if -- mem [ 16 ] != | 0 | goto l30

l31:
dbnza l31			; if -- a != | 0 | goto l31

l32:
dbnzx l32			; if -- x != | 0 | goto l32

l33:
dbnz 16,x,l33			; if -- mem [ 16 + x ] != | 0 | goto l33

l34:
l35:
dbnz ,x,l34			; if -- mem [ x ] != | 0 | goto l34
dbnz 16,sp,l35			; if -- mem [ 16 + sp ] != | 0 | goto l35
dec 16				; 16 -= | 1 |
deca 				; a -= | 1 |
decx 				; x -= | 1 |
dec 16,x			; mem [ 16 + x ] -= | 1 |
dec ,x				; mem [ x ] -= | 1 |
dec 16,sp			; mem [ 16 + sp ] -= | 1 |
div 				; a = mem [ h:a ] / mem [ x ]
eor #255			; a ^= | 255 |
eor 16				; a ^= 16
eor 256				; a ^= 256
eor 256,x			; a ^= mem [ 256 + x ]
eor 16,x			; a ^= mem [ 16 + x ]
eor ,x				; a ^= mem [ x ]
eor 256,sp			; a ^= mem [ 256 + sp ]
eor 16,sp			; a ^= mem [ 16 + sp ]
inc 16				; 16 += | 1 |
inca 				; a += | 1 |
incx 				; x += | 1 |
inc 16,x			; mem [ 16 + x ] += | 1 |
inc ,x				; mem [ x ] += | 1 |
inc 16,sp			; mem [ 16 + sp ] += | 1 |

l36:
l37:
jmp l36				; goto | l36 |
jmp l37,x			; goto | l37 + x |
jmp ,x				; goto | x |

l38:
l39:
l40:
jsr l38				; | l38 | ( )
jsr l39,x			; | l39 + x | ( )
jsr l40,x			; | l40 + x | ( )
jsr x				; | x | ( )
lda #255			; a = | 255 |
lda 16				; a = 16
lda 256				; a = 256
lda 256,x			; a = mem [ 256 + x ]
lda 16,x			; a = mem [ 16 + x ]
lda ,x				; a = mem [ x ]
lda 256,sp			; a = mem [ 256 + sp ]
lda 16,sp			; a = mem [ 16 + sp ]
ldhx #65535			; h:x = | 65535 |
ldhx 16				; h:x = 16
ldhx 256			; h:x = 256
ldhx ,x				; h:x = mem [ x ]
ldhx 256,x			; h:x = mem [ 256 + x ]
ldhx 16,x			; h:x = mem [ 16 + x ]
ldhx 16,sp			; h:x = mem [ 16 + sp ]
ldx #255			; x = | 255 |
ldx 16				; x = 16
ldx 256				; x = 256
ldx 256,x			; x = mem [ 256 + x ]
ldx 16,x			; x = mem [ 16 + x ]
ldx ,x				; x = mem [ x ]
ldx 256,sp			; x = mem [ 256 + sp ]
ldx 16,sp			; x = mem [ 16 + sp ]
lsl 16				; mem [ 16 ] << | 1 |
lsla 				; a << | 1 |
lslx 				; x << | 1 |
lsl 16,x			; mem [ 16 + x ] << | 1 |
lsl ,x				; mem [ x ] << | 1 |
lsl 16,sp			; mem [ 16 + sp ] << | 1 |
lsr 16				; 16 >>> | 1 |
lsra 				; a >>> | 1 |
lsrx 				; x >>> | 1 |
lsr 16,x			; mem [ 16 + x ] >>> | 1 |
lsr ,x				; mem [ x ] >>> | 1 |
lsr 16,sp			; mem [ 16 + sp ] >>> | 1 |
mov 16,17			; 17 = 16
mov ,x+,16			; mem [ x ++ ] = mem [ 16 ]
mov #255,16			; 16 = | 255 |
mov ,x+,16			; mem [ x ++ ] = mem [ 16 ]
mul 				; x:a = mem [ x ] * mem [ a ]
neg 16				; mem [ 16 ] ~= mem [ 16 ] + | 1 |
nega 				; a ~= a + | 1 |
negx 				; x ~= x + | 1 |
neg 16,x			; mem [ 16 + x ] ~= mem [ 16 + x ] + | 1 |
neg ,x				; mem [ x ] ~= mem [ x ] + | 1 |
neg 16,sp			; mem [ 16 + sp ] ~= mem [ 16 + sp ] + | 1 |
nop 				; nop
nsa 				; swap ( a )
ora #255			; a |= | 255 |
ora 255				; a |= 255
ora 256				; a |= 256
ora 256,x			; a |= mem [ 256 + x ]
ora 16,x			; a |= mem [ 16 + x ]
ora ,x				; a |= mem [ x ]
ora 256,sp			; a |= mem [ 256 + sp ]
ora 16,sp			; a |= mem [ 16 + sp ]
psha 				; push ( a )
pshh 				; push ( h )
pshx 				; push ( x )
pula 				; a = pop ( )
pulh 				; h = pop ( )
pulx 				; x = pop ( )
rol 16				; mem [ 16 ] << | 1 | + c
rola 				; a << | 1 | + c
rolx 				; x << | 1 | + c
rol PORTA,x			; mem [ PORTA + x ] << | 1 | + c
rol ,x				; mem [ x ] << | 1 | + c
rol 32,sp			; mem [ 32 + sp ] << | 1 | + c
bset 0,70			; 70 [ 0 ] = | 1 |
rorx 				; x >> | 1 | + c
ror 16,x			; mem [ 16 + x ] >> | 1 | + c
ror ,x				; mem [ x ] >> | 1 | + c
ror 16,sp			; mem [ 16 + sp ] >> | 1 | + c
rti 				; reti
rts 				; ret
sbc #255			; a -= | 255 | - c
sbc 16				; a -= 16 - c
sbc 256				; a -= 256 - c
sbc 256,x			; a -= mem [ 256 + x ] - c
sbc 16,x			; a -= mem [ 16 + x ] - c
sbc ,x				; a -= mem [ x ] - c
sbc 256,sp			; a -= mem [ 256 + sp ] - c
sbc 16,sp			; a -= mem [ 16 + sp ] - c
sec 				; sreg [ c ] = | 1 |
sei 				; sreg [ i ] = | 1 |
sta 16				; 16 = a
sta 256				; 256 = a
sta 16,x			; mem [ 16 + x ] = a
sta ,x				; mem [ x ] = a
sta 256,sp			; mem [ 256 + sp ] = a
sta 16,sp			; mem [ 16 + sp ] = a
sthx 255			; mem [ 255 ] = h:x
sthx 256			; mem [ 256 ] = h:x
sthx 16,sp			; mem [ 16 + sp ] = h:x
stx 16				; 16 = x
stx 256				; 256 = x
stx 256,x			; mem [ 256 + x ] = x
stx 16,x			; mem [ 16 + x ] = x
stx ,x				; mem [ x ] = x
stx 256,sp			; mem [ 256 + sp ] = x
stx 16,sp			; mem [ 16 + sp ] = x
sub #255			; a -= | 255 |
sub 16				; a -= 16
sub 256				; a -= 256
sub 16,x			; a -= mem [ 16 + x ]
sub ,x				; a -= mem [ x ]
sub 256,sp			; a -= mem [ 256 + sp ]
sub 16,sp			; a -= mem [ 16 + sp ]
tap 				; sreg = a
tax 				; x = a
tpa 				; a = sreg
tst 16				; 16 <= | 0 |
tsta 				; a <= | 0 |
tstx 				; x <= | 0 |
tst 16,x			; mem [ 16 + x ] <= | 0 |
tst ,x				; mem [ x ] <= | 0 |
tst 16,sp			; mem [ 16 + sp ] <= | 0 |
tsx 				; h:x = sp + | 1 |
txa 				; a = x
txs 				; sp = h:x - | 1 |
sub 0,x				; a -= mem [ 0 + x ]
