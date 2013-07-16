$l :,$l :,,,,,
"ADC $d , $r",$d += $r + C,0-31,0-31,,,000111rdddddrrrr
"ADD $d , $r",$d += $r,0-31,0-31,,,000011rdddddrrrr
"ADIW $d , $k",$d += $k,25:24-31:30,,0-63,,10010110kkddkkkk
"AND $d , $r",$d &= $r,0-31,0-31,,,001000rdddddrrrr
"ANDI $d , $k",$d &= $k,16-31,,0-255,,0111kkkkddddkkkk
COM $d,$d ~= $d,0-31,,,,1001010ddddd0000
"CP $d , $r",$d == $r,0-31,0-31,,,000101rdddddrrrr
"CPC $d , $r",$d == $r + C,0-31,0-31,,,000001rdddddrrrr
"CPI $d , $k",$d == $k,16-31,,0-255,,0011kkkkddddkkkk
DEC $d,$d -= 1,0-31,,,,1001010ddddd1010
"EOR $d , $r",$d ^= $r,0-31,0-31,,,001001rdddddrrrr
"FMUL $d , $r",R1:R0 = | $d | . | $r |,16-23,16-23,,,000000110ddd1rrr
"FMULS $d , $r",R1:R0 = $d . $r,16-23,16-23,,,000000111ddd0rrr
"FMULSU $d , $r",R1:R0 = $d . | $r |,16-23,16-23,,,000000111ddd1rrr
INC $d,$d += 1,0-31,,,,1001010ddddd0011
LSL $d,$d << 1,0-31,,,,000011rdddddrrrr
LSR $d,$d >> 1,0-31,,,,1001010ddddd0110
"MUL $d , $r",R1:R0 = | $d | * | $r |,0-31,0-31,,,100111rdddddrrrr
"MULS $d , $r",R1:R0 = $d * $r,16-31,16-31,,,00000010ddddrrrr
"MULSU $d , $r",R1:R0 = $d * | $r |,16-23,16-23,,,000000110ddd0rrr
NEG $d,$d ~= $d + 1,0-31,,,,1001010ddddd0001
"OR $d , $r",$d |= $r,0-31,0-31,,,001010rdddddrrrr
"ORI $d , $k",$d |= $k,16-31,,0-255,,0110kkkkddddkkkk
"SBC $d , $r",$d -= $r - C,0-31,0-31,,,000010rdddddrrrr
"SBCI $d , $k",$d -= $k - C,16-31,,0-255,,0100kkkkddddkkkk
"SBIW $d , $k",$d -= $k,25:24-31:30,,0-63,,10010111kkddkkkk
"SUB $d , $r",$d -= $r,0-31,0-31,,,000110rdddddrrrr
"SUBI $d , $k",$d -= $k,16-31,,0-255,,0101kkkkddddkkkk
ASR $d,$d >>> 1,0-31,,,,1001010ddddd0101
BCLR $b,SREG [ $b ] = $k,,,0,0-7,100101001kkk1000
"BLD $d , $b",$d [ $b ] = T,0-31,,,0-7,1111100ddddd0kkk
BSET $k,SREG [ $b ] = $k,,,1,0-7,100101000kkk1000
"BST $r , $b",SREG [ T ] = $r [ $b ],,0-31,,0-7,1111101ddddd0kkk
"CBI $d , $k",$d [ $b ] = $k,32-63,,0,0-7,10011000dddddkkk
ROL $d,$d << $k + C,0-31,,1,,000111rdddddrrrr
ROR $d,$d >> $k + C,0-31,,1,,1001010ddddd0111
"SBI $d , $k",$d [ $b ] = $k,32-63,,1,0-7,10011010dddddkkk
SWAP $d,SWAP ( $d ),0-31,,,,1001010ddddd0010
"BRBC $k , $l",if SREG [ $b ] == $k goto $l,,,0,0-7,111101lllllllkkk
"BRBS $k , $l",if SREG [ $b ] == $k goto $l,,,1,0-7,111100lllllllkkk
CALL $l,$l ( ),,,,,1001010kkkkk111kkkkkkkkkkkkkkkkk
"CPSE $d , $r",if $d == $r skip,0-31,0-31,,,000100rdddddrrrr
ICALL,* Z ( ),,,,,1001010100001001
IJMP,goto * Z,,,,,1001010000001001
JMP $l,goto $l,,,,,1001010kkkkk110kkkkkkkkkkkkkkkkk
RCALL $l,$l ( ),,,,,1101kkkkkkkkkkkk
RET,RET,,,,,1001010100001000
RETI,RETI,,,,,1001010100011000
RJMP $l,goto $l,,,,,1100llllllllllll
"SBIC $d , $b",if $d [ $b ] == $k skip,32-63,,0,0-7,10011001dddddkkk
"SBIS $d , $b",if $d [ $b ] == $k skip,32-63,,1,0-7,10011011dddddkkk
"SBRC $d , $b",if $d [ $b ] == $k skip,0-31,,0,0-7,1111110ddddd0kkk
"SBRS $d , $b",if $d [ $b ] == $k skip,0-31,,1,0-7,1111111ddddd0kkk
"IN $d , $r",$d = $r,0-31,32-95,,,10110rrdddddrrrr
"MOV $d , $r",$d = $r,0-31,0-31,,,001011rdddddrrrr
"MOVW $d , $r",$d = $r,1:0-31:30,1:0-31:30,,,00000001ddddrrrr
"OUT $d , $r",$d = $r,32-95,0-31,,,10111ddrrrrrdddd
POP $d,$d = POP ( ),0-31,,,,1001000ddddd1111
PUSH $r,PUSH ( $r ),,0-31,,,1001001ddddd1111
SLEEP,sleep,,,,,
WDR,wdr,,,,,
"ld $d , $r",$d = MEM [ $r ],0-31,27:26,,,1001000ddddd1100
"ld $d , $r +",$d = MEM [ $r ++ ],0-31,27:26,,,1001000ddddd1101
"ld $d , - $r",$d = MEM [ -- $r ],0-31,27:26,,,1001000ddddd1110
"ld $d , $r",$d = MEM [ $r ],0-31,29:28,,,1000000ddddd1000
"ld $d , $r +",$d = MEM [ $r ++ ],0-31,29:28,,,1001000ddddd1001
"ld $d , - $r",$d = MEM [ -- $r ],0-31,29:28,,,1001000ddddd1010
"ldd $d , $r + $k",$d = MEM [ $r + $k ],0-31,29:28,0-63,,10k0kk0ddddd1kkk
"ld $d , $r",$d = MEM [ $r ],0-31,31:30,,,1000000ddddd0000
"ld $d , $r +",$d = MEM [ $r ++ ],0-31,31:30,,,1001000ddddd0001
"ld $d , - $r",$d = MEM [ -- $r ],0-31,31:30,,,1001000ddddd0010
"ldd $d , $r + $k",$d = MEM [ $r + $k ],0-31,31:30,0-63,,10k0kk0ddddd0kkk
"ldi $d , $k",$d = $k,16-31,,0-255,,1110kkkkddddkkkk
"lds $d , $k",$d = MEM [ $k ],16-31,,0-127,,10100kkkddddkkkk
"lds $d , $k",$d = MEM [ $k ],0-31,,0-65535,,1001000ddddd0000kkkkkkkkkkkkkkkk
lpm,$d = PMEM [ $r ],0,31:30,,,1001010111001000
"lpm $d , $r",$d = PMEM [ $r ],0-31,31:30,,,1001000ddddd0100
"lpm $d , $r +",$d = PMEM [ $r ++ ],0-31,31:30,,,1001000ddddd0101
spm,PMEM [ $d ++ ] = $r,31:30,1:0,,,1001010111101000
"st $d , $r",MEM [ $d ] = $r,27:26,0-31,,,1001001rrrrr1100
"st $d + , $r",MEM [ $d ++ ] = $r,27:26,0-31,,,1001001rrrrr1101
"st - $d , $r",MEM [ -- $d ] = $r,27:26,0-31,,,1001001rrrrr1110
"st $d , $r",MEM [ $d ] = $r,29:28,0-31,,,1000001rrrrr1000
"st $d + , $r",MEM [ $d ++ ] = $r,29:28,0-31,,,1001001rrrrr1001
"st - $d , $r",MEM [ -- $d ] = $r,29:28,0-31,,,1001001rrrrr1010
"st $d + $k , $r",MEM [ $d + $k ] = $r,29:28,0-31,0-63,,10k0kk1rrrrr1kkk
"st $d , $r",MEM [ $d ] = $r,31:30,0-31,,,1000001rrrrr0000
"st $d + , $r",MEM [ $d ++ ] = $r,31:30,0-31,,,1001001rrrrr0001
"st - $d , $r",MEM [ -- $d ] = $r,31:30,0-31,,,1001001rrrrr0010
"st $d + $k , $r",MEM [ $d + $k ] = $r,31:30,0-31,0-63,,10k0kk1rrrrr0kkk
"sts $k , $r",MEM [ $k ] = $r,,16-31,0-127,,10101kkkddddkkkk
"sts $k , $r",MEM [ $k ] = $r,,0-31,0-65535,,1001001rrrrr0000kkkkkkkkkkkkkkkk