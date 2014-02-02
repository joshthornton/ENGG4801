nop 				; nop
adc r16,r17			; r16 += r17 + c
add r16,r17			; r16 += r17
adiw r25:r24,1			; r25:r24 += | 1 |
and r16,r17			; r16 &= r17
andi r16,240			; r16 &= | 240 |
com r16				; r16 ~= r16
cp r16,r17			; r16 == r17
cpc r16,r17			; r16 == r17 + c
cpi r16,240			; r16 == | 240 |
dec r16				; r16 -= | 1 |
eor r16,r17			; r16 ^= r17
fmul r16,r17			; r1:r0 = | r16 | . | r17 |
fmuls r16,r17			; r1:r0 = r16 . r17
fmulsu r16,r17			; r1:r0 = r16 . | r17 |
inc r16				; r16 += | 1 |
add r16,r16			; r16 += r16
lsr r16				; r16 >> | 1 |
mul r16,r17			; r1:r0 = | r16 | * | r17 |
muls r16,r17			; r1:r0 = r16 * r17
mulsu r16,r17			; r1:r0 = r16 * | r17 |
neg r16				; r16 ~= r16 + | 1 |
or r16,r17			; r16 |= r17
ori r16,240			; r16 |= | 240 |
sbc r16,r17			; r16 -= r17 - c
sbci r16,240			; r16 -= | 240 | - c
sbiw r25:r24,1			; r25:r24 -= | 1 |
sub r16,r17			; r16 -= r17
subi r16,240			; r16 -= | 240 |
asr r16				; r16 >>> | 1 |
bclr 1				; sreg [ 1 ] = | 0 |
bld r16,1			; r16 [ 1 ] = t
bset 1				; sreg [ 1 ] = | 1 |
bst r17,1			; sreg [ t ] = r17 [ 1 ]
cbi PORTA,1			; PORTA [ 1 ] = | 0 |
adc r16,r16			; r16 += r16 + c
ror r16				; r16 >> | 1 | + c
sbi PORTA,1			; PORTA [ 1 ] = | 1 |
swap r16			; swap ( r16 )

l0:
breq l0				; if == goto l0

l1:
brge l1				; if >= goto l1

l2:
brbs 4,l2			; if sreg [ 4 ] == | 1 | goto l2

l3:
brlo l3				; if | < | goto l3

l4:
brne l4				; if != goto l4

l5:
brbs 2,l5			; if sreg [ 2 ] == | 1 | goto l5

l6:
brpl l6				; if > | 0 | goto l6

l7:
brsh l7				; if | >= | goto l7

l8:
brne l8				; if != goto l8

l9:
breq l9				; if == goto l9
call l10			; l10 ( )
call l11			; l11 ( )

l10:
l11:
ret 				; ret
ldi r31,0			; r31 = | 0 |
ldi r30,52			; r30 = | 52 |
icall 				; * r31:r30 ( )
ldi r31,0			; r31 = | 0 |
ldi r30,59			; r30 = | 59 |
ijmp 				; goto * r31:r30
cpse r16,r17			; if r16 == r17 skip

l12:
jmp l12				; goto | l12 |

l13:
rjmp l13			; goto l13
sbic PINA,1			; if PINA [ 1 ] == | 0 | skip
sbis PINA,1			; if PINA [ 1 ] == | 1 | skip
sbrc r16,1			; if r16 [ 1 ] == | 0 | skip
sbrs r16,1			; if r16 [ 1 ] == | 1 | skip
in r16,PINA			; r16 = PINA
mov r16,r17			; r16 = r17
movw r25:r24,r31:r30		; r25:r24 = r31:r30
out DDRA,r17			; DDRA = r17
pop r16				; r16 = pop ( )
push r17			; push ( r17 )
sleep 				; sleep
wdr 				; wdr
ld r16,r27:26			; r16 = mem [ r27:26 ]
ld r16,r27:26+			; r16 = mem [ r27:26 ++ ]
ld r16,-r27:26			; r16 = mem [ -- r27:26 ]
ld r16,r29:r28			; r16 = mem [ r29:r28 ]
ld r16,r29:r28+			; r16 = mem [ r29:r28 ++ ]
ld r16,-r29:r28			; r16 = mem [ -- r29:r28 ]
ldd r16,r29:r28+1		; r16 = mem [ r29:r28 + 1 ]
ldd r16,r31:r30+0		; r16 = mem [ r31:r30 + 0 ]
ld r16,r31:r30+			; r16 = mem [ r31:r30 ++ ]
ld r16,-r31:r30			; r16 = mem [ -- r31:r30 ]
ldd r16,r31:r30+1		; r16 = mem [ r31:r30 + 1 ]
ldi r16,255			; r16 = | 255 |
lds r16,24			; r16 = mem [ 24 ]
lds r16,65534			; r16 = mem [ 65534 ]
lpm r0,r31:r30			; r0 = pmem [ r31:r30 ]
lpm r16,r31:r30			; r16 = pmem [ r31:r30 ]
lpm r16,r31:r30+		; r16 = pmem [ r31:r30 ++ ]
spm 				; pmem [ r31:r30 ++ ] = r1:r0
st r27:26,r16			; mem [ r27:26 ] = r16
st r27:26+,r16			; mem [ r27:26 ++ ] = r16
st -r27:26,r16			; mem [ -- r27:26 ] = r16
st r29:r28,r16			; mem [ r29:r28 ] = r16
st r29:r28+,r16			; mem [ r29:r28 ++ ] = r16
st -r29:r28,r16			; mem [ -- r29:r28 ] = r16
sts 127,r16			; mem [ 127 ] = r16
std r31:r30+0,r16		; mem [ r31:r30 + 0 ] = r16
st r31:r30+,r16			; mem [ r31:r30 ++ ] = r16
st -r31:r30,r16			; mem [ -- r31:r30 ] = r16
std r31:r30+63,r16		; mem [ r31:r30 + 63 ] = r16
sts 127,r16			; mem [ 127 ] = r16
sts 65534,r16			; mem [ 65534 ] = r16
