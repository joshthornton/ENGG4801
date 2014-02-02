ADC # $k,A += | $k | + C,,,0-255,,,10101001kkkkkkkk
ADC $r,A += MEM [ $r ] + C,,0-255,,,,10111001rrrrrrrr
ADC $r,A += $r + C,,0-255,,,,10111001rrrrrrrr
ADC $r,A += MEM [ $r ] + C,,0-65535,,,,11001001rrrrrrrrrrrrrrrr
ADC $r,A += $r + C,,0-65535,,,,11001001rrrrrrrrrrrrrrrr
"ADC $r , X",A += MEM [ $r + X ] + C,,0-65535,,,,11011001rrrrrrrrrrrrrrrr
"ADC $r , X",A += MEM [ $r + X ] + C,,0-255,,,,11101001rrrrrrrr
"ADC , X",A += MEM [ X ] + C,,,,,,11111001
"ADC $r , SP",A += MEM [ $r + SP ] + C,,0-65535,,,,1001111011011001rrrrrrrrrrrrrrrr
"ADC $r , SP",A += MEM [ $r + SP ] + C,,0-255,,,,1001111011101001rrrrrrrr
ADD # $k,A += | $k |,,,0-255,,,10101011kkkkkkkk
ADD $r,A += MEM [ $r ],,0-255,,,,10111011rrrrrrrr
ADD $r,A += $r,,0-255,,,,10111011rrrrrrrr
ADD $r,A += MEM [ $r ],,0-65535,,,,11001011rrrrrrrrrrrrrrrr
ADD $r,A += $r,,0-65535,,,,11001011rrrrrrrrrrrrrrrr
"ADD $r , X",A += MEM [ $r + X ],,0-65535,,,,11011011rrrrrrrrrrrrrrrr
"ADD $r , X",A += MEM [ $r + X ],,0-255,,,,11101011rrrrrrrr
"ADD , X",A += MEM [ X ],,,,,,11111011
"ADD $r , SP",A += MEM [ $r + SP ],,0-65535,,,,1001111011011011rrrrrrrrrrrrrrrr
"ADD $r , SP",A += MEM [ $r + SP ],,0-255,,,,1001111011101011rrrrrrrr
AIS # $k,SP += | $k |,,,-128-127,,,10100111kkkkkkkk
AIX # $k,H:X += | $k |,,,-128-127,,,10101111kkkkkkkk
AND # $k,A &= | $k |,,,0-255,,,10100100kkkkkkkk
AND $r,A &= MEM [ $r ],,0-255,,,,10110100rrrrrrrr
AND $r,A &= $r,,0-255,,,,10110100rrrrrrrr
AND $r,A &= MEM [ $r ],,0-65535,,,,11000100rrrrrrrrrrrrrrrr
AND $r,A &= $r,,0-65535,,,,11000100rrrrrrrrrrrrrrrr
"AND $r , X",A &= MEM [ $r + X ],,0-65535,,,,11010100rrrrrrrrrrrrrrrr
"AND $r , X",A &= MEM [ $r + X ],,0-255,,,,11100100rrrrrrrr
"AND , X",A &= MEM [ X ],,,,,,11110100
"AND $r , SP",A &= MEM [ $r + SP ],,0-65535,,,,1001111011010100rrrrrrrrrrrrrrrr
"AND $r , SP",A &= MEM [ $r + SP ],,0-255,,,,1001111011100100rrrrrrrr
ASR $r,MEM [ $r ] >> $k,,0-255,1,,,00110111rrrrrrrr
ASRA,A >> | $k |,,,1,,,01000111
ASRX,X >> | $k |,,,1,,,01010111
"ASR $r , X",MEM [ $r + X ] >> | $k |,,0-255,1,,,01100111rrrrrrrr
"ASR , X",MEM [ X ] >> | $k |,,,1,,,01110111
"ASR $r , SP",MEM [ $r + SP ] >> | $k |,,0-255,1,,,1001111001100111rrrrrrrr
BCC $l,if SREG [ C ] == | $k | goto $l,,,0,,-128-127,00100100llllllll
"BCLR $b , $r",MEM [ $r ] [ $b ] = | $k |,,0-255,0,0-7,,0001bbb1rrrrrrrr
BCS $l,if SREG [ C ] == | $k | goto $l,,,1,,-128-127,00100101llllllll
BEQ $l,if == goto $l,,,1,,-128-127,00100111llllllll
BEQ $l,if SREG [ Z ] == | $k | goto $l,,,1,,-128-127,00100111llllllll
BGE $l,if >= goto $l,,,,,-128-127,10010000llllllll
BGT $l,if > goto $l,,,,,-128-127,10010010llllllll
BHCC $l,if SREG [ H ] == | $k | goto $l,,,0,,-128-127,00101000llllllll
BHCS $l,if SREG [ H ] == | $k | goto $l,,,1,,-128-127,00101001llllllll
BHI $l,if | > | goto $l,,,,,-128-127,00100010llllllll
BHS $l,if | >= | goto $l,,,,,-128-127,00100100llllllll
BIH $l,if IRQ == | $k | goto $l,,,1,,-128-127,00101111llllllll
BIL $l,if IRQ == | $k | goto $l,,,0,,-128-127,00101110llllllll
BIT # $k,A & | $k |,,,0-255,,,10100101kkkkkkkk
BIT $r,A & MEM [ $r ],,0-255,,,,10110101rrrrrrrr
BIT $r,A & $r,,0-255,,,,10110101rrrrrrrr
BIT $r,A & MEM [ $r ],,0-65535,,,,11000101rrrrrrrrrrrrrrrr
BIT $r,A & $r,,0-65535,,,,11000101rrrrrrrrrrrrrrrr
"BIT $r , X",A & MEM [ $r + X ],,0-65535,,,,11010101rrrrrrrrrrrrrrrr
"BIT $r , X",A & MEM [ $r + X ],,0-255,,,,11100101rrrrrrrr
"BIT , X",A & MEM [ X ],,,,,,11110101
"BIT $r , SP",A & MEM [ $r + SP ],,0-65535,,,,1001111011010101rrrrrrrrrrrrrrrr
"BIT $r , SP",A & MEM [ $r + SP ],,0-255,,,,1001111011100101rrrrrrrr
BLE $l,if <= goto $l,,,,,-128-127,10010011llllllll
BLO $l,if | < | goto $l,,,,,-128-127,00100101llllllll
BLS $l,if | <= | goto $l,,,,,-128-127,00100011llllllll
BLT $l,if < goto $l,,,,,-128-127,10010001llllllll
BMC $l,if SREG [ I ] == | $k | goto $l,,,0,,-128-127,00101100llllllll
BMI $l,if SREG [ N ] == | $k | goto $l,,,1,,-128-127,00101011llllllll
BMS $l,if SREG [ I ] == | $k | goto $l,,,1,,-128-127,00101101llllllll
BNE $l,if != goto $l,,,,,-128-127,00100110llllllll
BNE $l,if SREG [ Z ] == | $k | goto $l,,,0,,-128-127,00100110llllllll
BPL $l,if SREG [ N ] == | $k | goto $l,,,0,,-128-127,00101010llllllll
BRA $l,goto $l,,,,,-128-127,00100000llllllll
"BRCLR $b , $r , $l",if MEM [ $r ] [ $b ] == | $k | goto $l,,0-255,0,0-7,-128-127,0000bbb1rrrrrrrrllllllll
"BRCLR $b , $r , $l",if $r [ $b ] == | $k | goto $l,,0-255,0,0-7,-128-127,0000bbb1rrrrrrrrllllllll
"BRCLR $b , $r , 1",if $r [ $b ] == | $k | skip,,0-255,0,0-7,,0000bbb1rrrrrrrr00000001
"BRSET $b , $r , $l",if MEM [ $r ] [ $b ] == | $k | goto $l,,0-255,1,0-7,-128-127,0000bbb0rrrrrrrrllllllll
"BRSET $b , $r , $l",if $r [ $b ] == | $k | goto $l,,0-255,1,0-7,-128-127,0000bbb0rrrrrrrrllllllll
"BRSET $b , $r , 1",if $r [ $b ] == | $k | skip,,0-255,1,0-7,,0000bbb0rrrrrrrr00000001
"BSET $b , $r",MEM [ $r ] [ $b ] = | $k |,,0-255,1,0-7,,0001bbb0rrrrrrrr
"BSET $b , $r",$r [ $b ] = | $k |,,0-255,1,0-7,,0001bbb0rrrrrrrr
BSR $l,$l ( ),,,,,-128-127,10101101llllllll
"CBEQ $r , $l",if A == MEM [ $r ] goto $l,,0-255,,,-128-127,00110001rrrrrrrrllllllll
"CBEQ $r , $l",if A == $r goto $l,,0-255,,,-128-127,00110001rrrrrrrrllllllll
"CBEQA # $k , $l",if A == | $k | goto $l,,,0-255,,-128-127,01000001kkkkkkkkllllllll
"CBEQX # $k , $l",if X == | $k | goto $l,,,0-255,,-128-127,01010001kkkkkkkkllllllll
"CBEQ $r , X + , $l",if A == MEM [ $r + X ++ ] goto $l,,0-255,,,-128-127,01100001rrrrrrrrllllllll
"CBEQ , X + , $l",if A == MEM [ X ++ ] goto $l,,,,,-128-127,01110001rrrrrrrrllllllll
"CBEQ $r , SP , $l",if A == MEM [ $r + SP ] goto $l,,0-255,,,-128-127,1001111001100001rrrrrrrrllllllll
CLC,SREG [ C ] = | $k |,,,0,,,10011000
CLI,SREG [ I ] = | $k |,,,0,,,10011010
CLR $r,MEM [ $r ] = | $k |,,0-255,0,,,00111111rrrrrrrr
CLR $r,$r = | $k |,,0-255,0,,,00111111rrrrrrrr
CLRA,A = | $k |,,,0,,,01001111
CLRX,X = | $k |,,,0,,,01011111
CLRH,H = | $k |,,,0,,,10001100
"CLR $r , X",MEM [ $r + X ] = | $k |,,0-255,0,,,01101111rrrrrrrr
"CLR , X",MEM [ X ] = | $k |,,,0,,,01111111
"CLR $r , SP",MEM [ $r + SP ] = | $k |,,0-255,0,,,1001111001101111rrrrrrr
CMP # $k,A - | $k |,,,0-255,,,10100001kkkkkkkk
CMP $r,A - MEM [ $r ],,0-255,,,,10110001rrrrrrrr
CMP $r,A - $r,,0-255,,,,10110001rrrrrrrr
CMP $r,A - MEM [ $r ],,0-65535,,,,11000001rrrrrrrrrrrrrrrr
CMP $r,A - $r,,0-65535,,,,11000001rrrrrrrrrrrrrrrr
"CMP $r , X",A - MEM [ $r + X ],,0-65535,,,,11010001rrrrrrrrrrrrrrrr
"CMP $r , X",A - MEM [ $r + X ],,0-255,,,,11100001rrrrrrrr
"CMP , X",A - MEM [ X ],,,,,,11110001
"CMP $r , SP",A - MEM [ $r + SP ],,0-65535,,,,1001111011010001rrrrrrrrrrrrrrrr
"CMP $r , SP",A - MEM [ $r + SP ],,0-255,,,,1001111011100001rrrrrrrr
COM $r,MEM [ $r ] ~= MEM [ $r ],,0-255,,,,00110011rrrrrrrr
COMA,A ~= A,,,,,,01000011
COMX,X ~= X,,,,,,01010011
"COM $r , X",MEM [ $r + X ] ~= MEM [ $r + X ],,0-255,,,,01100011rrrrrrrr
"COM , X",MEM [ X ] ~= MEM [ X ],,,,,,01110011
"COM $r , SP",MEM [ $r + SP ] ~= MEM [ $r + SP ],,0-255,,,,1001111001100011rrrrrrrr
CPHX $r,H:X - MEM [ $r ],,0-65535,,,,00111110rrrrrrrrrrrrrrrr
CPHX $r,H:X - $r,,0-65535,,,,00111110rrrrrrrrrrrrrrrr
CPHX # $k,H:X - | $k |,,,0-65535,,,01100101kkkkkkkkkkkkkkkk
CPHX $r,H:X - MEM [ $r ],,0-255,,,,01110101rrrrrrrr
CPHX $r,H:X - $r,,0-255,,,,01110101rrrrrrrr
"CPHX $r , SP",H:X - MEM [ $r + SP ],,0-255,,,,1001111011110011rrrrrrrr
CPX # $k,X - | $k |,,,0-255,,,10100011kkkkkkkk
CPX $r,X - MEM [ $r ],,0-255,,,,10110011rrrrrrrr
CPX $r,X - $r,,0-255,,,,10110011rrrrrrrr
CPX $r,X - MEM [ $r ],,0-65535,,,,11000011rrrrrrrrrrrrrrrr
CPX $r,X - $r,,0-65535,,,,11000011rrrrrrrrrrrrrrrr
"CPX $r , X",X - MEM [ $r + X ],,0-65535,,,,11010011rrrrrrrrrrrrrrrr
"CPX $r , X",X - MEM [ $r + X ],,0-255,,,,11100011rrrrrrrr
"CPX , X",X - MEM [ X ],,,,,,11110011
"CPX $r , SP",X - MEM [ $r + SP ],,0-65535,,,,1001111011010011rrrrrrrrrrrrrrrr
"CPX $r , SP",X - MEM [ $r + SP ],,0-255,,,,1001111011100011rrrrrrrr
"DBNZ $r , $l",if -- MEM [ $r ] != | $k | goto $l,,0-255,0,,-128-127,00111011rrrrrrrrllllllll
DBNZA $l,if -- A != | $k | goto $l,,,0,,-128-127,01001011llllllll
DBNZX $l,if -- X != | $k | goto $l,,,0,,-128-127,01011011llllllll
"DBNZ $r , X , $l",if -- MEM [ $r + X ] != | $k | goto $l,,0-255,0,,-128-127,01101011rrrrrrrrllllllll
"DBNZ , X , $l",if -- MEM [ X ] != | $k | goto $l,,,0,,-128-127,01111011llllllll
"DBNZ $r , SP , $l",if -- MEM [ $r + SP ] != | $k | goto $l,,0-255,0,,-128-127,1001111001101011rrrrrrrrllllllll
DEC $r,MEM [ $r ] -= | $k |,,0-255,1,,,00111010rrrrrrrr
DEC $r,$r -= | $k |,,0-255,1,,,00111010rrrrrrrr
DECA,A -= | $k |,,,1,,,01001010
DECX,X -= | $k |,,,1,,,01011010
"DEC $r , X",MEM [ $r + X ] -= | $k |,,0-255,1,,,01101010rrrrrrrr
"DEC , X",MEM [ X ] -= | $k |,,,1,,,01111010
"DEC $r , SP",MEM [ $r + SP ] -= | $k |,,0-255,1,,,1001111001101010rrrrrrrr
DIV,A = MEM [ H:A ] / MEM [ X ],,,,,,01010010
EOR # $k,A ^= | $k |,,,0-255,,,10101000kkkkkkkk
EOR $r,A ^= MEM [ $r ],,0-255,,,,10111000rrrrrrrr
EOR $r,A ^= MEM [ $r ],,0-65535,,,,11001000rrrrrrrrrrrrrrrr
EOR $r,A ^= $r,,0-255,,,,10111000rrrrrrrr
EOR $r,A ^= $r,,0-65535,,,,11001000rrrrrrrrrrrrrrrr
"EOR $r , X",A ^= MEM [ $r + X ],,0-65535,,,,11011000rrrrrrrrrrrrrrrr
"EOR $r , X",A ^= MEM [ $r + X ],,0-255,,,,11101000rrrrrrrr
"EOR , X",A ^= MEM [ X ],,,,,,11111000
"EOR $r , SP",A ^= MEM [ $r + SP ],,0-65535,,,,1001111011011000rrrrrrrrrrrrrrrr
"EOR $r , SP",A ^= MEM [ $r + SP ],,0-255,,,,1001111011101000rrrrrrrr
INC $r,MEM [ $r ] += | $k |,,0-255,1,,,00111100rrrrrrrr
INC $r,$r += | $k |,,0-255,1,,,00111100rrrrrrrr
INCA,A += | $k |,,,1,,,01001100
INCX,X += | $k |,,,1,,,01011100
"INC $r , X",MEM [ $r + X ] += | $k |,,0-255,1,,,01101100rrrrrrrr
"INC , X",MEM [ X ] += | $k |,,,1,,,01111100
"INC $r , SP",MEM [ $r + SP ] += | $k |,,0-255,1,,,1001111001101100rrrrrrrr
JMP $l,goto | $l |,,,,,0-255,10111100llllllll
JMP $l,goto | $l |,,,,,0-65535,11001100llllllllllllllll
"JMP $l , X",goto | $l + X |,,,,,0-65535,11011100llllllllllllllll
"JMP $l , X",goto | $l + X |,,,,,0-255,11101100llllllll
"JMP , X",goto | X |,,,,,,11111100
JSR $l,| $l | ( ),,,,,0-255,10111101llllllll
JSR $l,| $l | ( ),,,,,0-65535,11001101llllllllllllllll
"JSR $l , X",| $l + X | ( ),,,,,0-65535,11011101llllllllllllllll
"JSR $l , X",| $l + X | ( ),,,,,0-255,11101101llllllll
JSR X,| X | ( ),,,,,,11111101
LDA # $k,A = | $k |,,,0-255,,,10100110kkkkkkkk
LDA $r,A = MEM [ $r ],,0-255,,,,10110110rrrrrrrr
LDA $r,A = $r,,0-255,,,,10110110rrrrrrrr
LDA $r,A = MEM [ $r ],,0-65535,,,,11000110rrrrrrrrrrrrrrrr
LDA $r,A = $r,,0-65535,,,,11000110rrrrrrrrrrrrrrrr
"LDA $r , X",A = MEM [ $r + X ],,0-65535,,,,11010110rrrrrrrrrrrrrrrr
"LDA $r , X",A = MEM [ $r + X ],,0-255,,,,11100110rrrrrrrr
"LDA , X",A = MEM [ X ],,,,,,11110110
"LDA $r , SP",A = MEM [ $r + SP ],,0-65535,,,,1001111011010110rrrrrrrrrrrrrrrr
"LDA $r , SP",A = MEM [ $r + SP ],,0-255,,,,1001111011100110rrrrrrrr
LDHX # $k,H:X = | $k |,,,0-65535,,,01000101kkkkkkkkkkkkkkkk
LDHX $r,H:X = MEM [ $r ],,0-255,,,,01010101rrrrrrrr
LDHX $r,H:X = MEM [ $r ],,0-65535,,,,00110010rrrrrrrrrrrrrrrr
LDHX $r,H:X = $r,,0-255,,,,01010101rrrrrrrr
LDHX $r,H:X = $r,,0-65535,,,,00110010rrrrrrrrrrrrrrrr
"LDHX , X",H:X = MEM [ X ],,,,,,1001111010101110
"LDHX $r , X",H:X = MEM [ $r + X ],,0-65535,,,,1001111010111110rrrrrrrrrrrrrrrr
"LDHX $r , X",H:X = MEM [ $r + X ],,0-255,,,,1001111011001110rrrrrrrr
"LDHX $r , SP",H:X = MEM [ $r + SP ],,0-255,,,,1001111011111110rrrrrrrr
LDX # $k,X = | $k |,,,0-255,,,10101110kkkkkkkk
LDX $r,X = MEM [ $r ],,0-255,,,,10111110rrrrrrrr
LDX $r,X = MEM [ $r ],,0-65535,,,,11001110rrrrrrrrrrrrrrrr
LDX $r,X = $r,,0-255,,,,10111110rrrrrrrr
LDX $r,X = $r,,0-65535,,,,11001110rrrrrrrrrrrrrrrr
"LDX $r , X",X = MEM [ $r + X ],,0-65535,,,,11011110rrrrrrrrrrrrrrrr
"LDX $r , X",X = MEM [ $r + X ],,0-255,,,,11101110rrrrrrrr
"LDX , X",X = MEM [ X ],,,,,,11111110
"LDX $r , SP",X = MEM [ $r + SP ],,0-65535,,,,1001111011011110rrrrrrrrrrrrrrrr
"LDX $r , SP",X = MEM [ $r + SP ],,0-255,,,,1001111011101110rrrrrrrr
LSL $r,MEM [ $r ] << | $k |,,0-255,1,,,00111000rrrrrrrr
LSLA,A << | $k |,,,1,,,01001000
LSLX,X << | $k |,,,1,,,01011000
"LSL $r , X",MEM [ $r + X ] << | $k |,,0-255,1,,,01101000rrrrrrrr
"LSL , X",MEM [ X ] << | $k |,,,1,,,01111000
"LSL $r , SP",MEM [ $r + SP ] << | $k |,,0-255,1,,,1001111001101000rrrrrrrr
LSR $r,MEM [ $r ] >>> | $k |,,0-255,1,,,00110100rrrrrrrr
LSR $r,$r >>> | $k |,,0-255,1,,,00110100rrrrrrrr
LSRA,A >>> | $k |,,,1,,,01000100
LSRX,X >>> | $k |,,,1,,,01010100
"LSR $r , X",MEM [ $r + X ] >>> | $k |,,0-255,1,,,01100100rrrrrrrr
"LSR , X",MEM [ X ] >>> | $k |,,,1,,,01110100
"LSR $r , SP",MEM [ $r + SP ] >>> | $k |,,0-255,1,,,1001111001100100rrrrrrrr
"MOV $r , $d",MEM [ $d ] = MEM [ $r ],0-255,0-255,,,,01001110rrrrrrrrdddddddd
"MOV $r , $d",$d = $r,0-255,0-255,,,,01001110rrrrrrrrdddddddd
"MOV $r , X +",MEM [ X++ ] = MEM [ $r ],,0-255,,,,01011110rrrrrrrr
"MOV # $k , $d",MEM [ $d ] = | $k |,0-255,,0-255,,,01101110kkkkkkkkdddddddd
"MOV # $k , $d",$d = | $k |,0-255,,0-255,,,01101110kkkkkkkkdddddddd
"MOV , X + , $r",MEM [ X ++ ] = MEM [ $r ],,0-255,,,,01111110rrrrrrrr
MUL,X:A = MEM [ X ] * MEM [ A ],,,,,,01000010
NEG $r,MEM [ $r ] ~= MEM [ $r ] + | $k |,,0-255,1,,,00110000rrrrrrrr
NEGA,A ~= A + | $k |,,,1,,,01000000
NEGX,X ~= X + | $k |,,,1,,,01010000
"NEG $r , X",MEM [ $r + X ] ~= MEM [ $r + X ] + | $k |,,0-255,1,,,01100000rrrrrrrr
"NEG , X",MEM [ X ] ~= MEM [ X ] + | $k |,,,1,,,01110000
"NEG $r , SP",MEM [ $r + SP ] ~= MEM [ $r + SP ] + | $k |,,0-255,1,,,1001111001100000rrrrrrrr
NOP,NOP,,,,,,10011101
NSA,SWAP ( A ),,,,,,01100010
ORA # $k,A |= | $k |,,,0-255,,,10101010kkkkkkkk
ORA $r,A |= MEM [ $r ],,0-255,,,,10111010rrrrrrrr
ORA $r,A |= MEM [ $r ],,0-65535,,,,11001010rrrrrrrrrrrrrrrr
ORA $r,A |= $r,,0-255,,,,10111010rrrrrrrr
ORA $r,A |= $r,,0-65535,,,,11001010rrrrrrrrrrrrrrrr
"ORA $r , X",A |= MEM [ $r + X ],,0-65535,,,,11011010rrrrrrrrrrrrrrrr
"ORA $r , X",A |= MEM [ $r + X ],,0-255,,,,11101010rrrrrrrr
"ORA , X",A |= MEM [ X ],,,,,,11111010
"ORA $r , SP",A |= MEM [ $r + SP ],,0-65535,,,,1001111011011010rrrrrrrrrrrrrrrr
"ORA $r , SP",A |= MEM [ $r + SP ],,0-255,,,,1001111011101010rrrrrrrr
PSHA,PUSH ( A ),,,,,,10000111
PSHH,PUSH ( H ),,,,,,10001011
PSHX,PUSH ( X ),,,,,,10001001
PULA,A = POP ( ),,,,,,10000110
PULH,H = POP ( ),,,,,,10001010
PULX,X = POP ( ),,,,,,10001000
ROL $r,MEM [ $r ] << | $k  | + C,,0-255,1,,,00111001rrrrrrrr
ROLA,A << | $k | + C,,,1,,,01001001
ROLX,X << | $k | + C,,,1,,,01011001
"ROL $r , X",MEM [ $r + X ] << | $k | + C,,0-255,1,,,01101001rrrrrrr
"ROL , X",MEM [ X ] << | $k | + C,,,1,,,01111001
"ROL $r , SP",MEM [ $r + SP ] << | $k | + C,,0-255,1,,,1001111001101001rrrrrrrrr
ROR $r,MEM [ $r ] >> | $k | + C,,0-255,1,,,00110110rrrrrrrr
RORA,A >> | $k | + C,,,1,,,01000110
RORX,X >> | $k | + C,,,1,,,01010110
"ROR $r , X",MEM [ $r + X ] >> | $k | + C,,0-255,1,,,01100110rrrrrrrr
"ROR , X",MEM [ X ] >> | $k | + C,,,1,,,01110110
"ROR $r , SP",MEM [ $r + SP ] >> | $k | + C,,0-255,1,,,1001111001100110rrrrrrrr
RTI,reti,,,,,,10000000
RTS,ret,,,,,,10000001
SBC # $k,A -= | $k | - C,,,0-255,,,10100010kkkkkkkk
SBC $r,A -= MEM [ $r ] - C,,0-255,,,,10110010rrrrrrrr
SBC $r,A -= MEM [ $r ] - C,,0-65535,,,,11000010rrrrrrrrrrrrrrrr
SBC $r,A -= $r - C,,0-255,,,,10110010rrrrrrrr
SBC $r,A -= $r - C,,0-65535,,,,11000010rrrrrrrrrrrrrrrr
"SBC $r , X",A -= MEM [ $r + X ] - C,,0-65535,,,,11010010rrrrrrrrrrrrrrrr
"SBC $r , X",A -= MEM [ $r + X ] - C,,0-255,,,,11100010rrrrrrrr
"SBC , X",A -= MEM [ X ] - C,,,,,,11110010
"SBC $r , SP",A -= MEM [ $r + SP ] - C,,0-65535,,,,1001111011010010rrrrrrrrrrrrrrrr
"SBC $r , SP",A -= MEM [ $r + SP ] - C,,0-255,,,,1001111011100010rrrrrrrr
SEC,SREG [ C ] = | $k |,,,1,,,10011001
SEI,SREG [ I ] = | $k |,,,1,,,10011011
STA $r,MEM [ $r ] = A,,0-255,,,,10110111rrrrrrrr
STA $r,MEM [ $r ] = A,,0-65535,,,,11000111rrrrrrrrrrrrrrrr
STA $r,$r = A,,0-255,,,,10110111rrrrrrrr
STA $r,$r = A,,0-65535,,,,11000111rrrrrrrrrrrrrrrr
"STA $r , X",MEM [ $r + X ] = A,,0-255,,,,11100111rrrrrrrr
"STA , X",MEM [ X ] = A,,,,,,11110111
"STA $r , SP",MEM [ $r + SP ] = A,,0-65535,,,,1001111011010111rrrrrrrrrrrrrrrr
"STA $r , SP",MEM [ $r + SP ] = A,,0-255,,,,1001111011100111rrrrrrrr
STHX $r,MEM [ $r ] = H:X,,0-255,,,,00110101rrrrrrrr
STHX $r,MEM [ $r ] = H:X,,0-65535,,,,10010110rrrrrrrrrrrrrrrr
"STHX $r , SP",MEM [ $r + SP ] = H:X,,0-255,,,,1001111011111111rrrrrrrr
STX $r,MEM [ $r ] = X,,0-255,,,,10111111rrrrrrrr
STX $r,MEM [ $r ] = X,,0-65535,,,,11001111rrrrrrrrrrrrrrrr
STX $r,$r = X,,0-255,,,,10111111rrrrrrrr
STX $r,$r = X,,0-65535,,,,11001111rrrrrrrrrrrrrrrr
"STX $r , X",MEM [ $r + X ] = X,,0-65535,,,,11011111rrrrrrrrrrrrrrrr
"STX $r , X",MEM [ $r + X ] = X,,0-255,,,,11101111rrrrrrrr
"STX , X",MEM [ X ] = X,,,,,,11111111
"STX $r , SP",MEM [ $r + SP ] = X,,0-65535,,,,1001111011011111rrrrrrrrrrrrrrrr
"STX $r , SP",MEM [ $r + SP ] = X,,0-255,,,,1001111011101111rrrrrrrr
SUB # $k,A -= | $k |,,,0-255,,,10100000kkkkkkkk
SUB $r,A -= MEM [ $r ],,0-255,,,,10110000rrrrrrrr
SUB $r,A -= MEM [ $r ],,0-65535,,,,11000000rrrrrrrrrrrrrrrr
SUB $r,A -= $r,,0-255,,,,10110000rrrrrrrr
SUB $r,A -= $r,,0-65535,,,,11000000rrrrrrrrrrrrrrrr
"SUB $r , X",A -= MEM [ $r + X ],,0-255,,,,11100000rrrrrrrr
"SUB , X",A -= MEM [ X ],,,,,,11110000
"SUB $r , SP",A -= MEM [ $r + SP ],,0-65535,,,,1001111011010000rrrrrrrrrrrrrrrr
"SUB $r , SP",A -= MEM [ $r + SP ],,0-255,,,,1001111011100000rrrrrrrr
TAP,SREG = A,,,,,,10000100
TAX,X = A,,,,,,10010111
TPA,A = SREG,,,,,,10000101
TST $r,MEM [ $r ] <= | $k |,,0-255,0,,,00111101rrrrrrrr
TST $r,$r <= | $k |,,0-255,0,,,00111101rrrrrrrr
TSTA,A <= | $k |,,,0,,,01001101
TSTX,X <= | $k |,,,0,,,01011101
"TST $r , X",MEM [ $r + X ] <= | $k |,,0-255,0,,,01101101rrrrrrrr
"TST , X",MEM [ X ] <= | $k |,,,0,,,01111101
"TST $r , SP",MEM [ $r + SP ] <= | $k |,,0-255,0,,,1001111001101101rrrrrrrr
TSX,H:X = SP + | $k |,,,1,,,10010101
TXA,A = X,,,,,,10011111
TXS,SP = H:X - | $k |,,,1,,,10010100