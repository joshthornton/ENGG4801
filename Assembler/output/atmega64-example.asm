
setup:
ldi TEMP,7			; TEMP = | 7 |
out DDRA,TEMP			; DDRA = TEMP
ldi TEMP,0			; TEMP = | 0 |
out TCCR1A,TEMP			; TCCR1A = TEMP
ldi TEMP,10			; TEMP = | 10 |
out TCCR1B,TEMP			; TCCR1B = TEMP
ldi TEMP,INTERRUPT_HIGH		; TEMP = | INTERRUPT_HIGH |
out OCR1AH,TEMP			; OCR1AH = TEMP
ldi TEMP,INTERRUPT_LOW		; TEMP = | INTERRUPT_LOW |
out OCR1AL,TEMP			; OCR1AL = TEMP
ldi TEMP,16			; TEMP = | 16 |
out TIMSK,TEMP			; TIMSK = TEMP
ldi TEMP,3			; TEMP = | 3 |
sts EICRA,TEMP			; mem [ EICRA ] = TEMP
ldi TEMP,1			; TEMP = | 1 |
out EIMSK,TEMP			; EIMSK = TEMP
bset I				; sreg [ I ] = | 1 |
ldi COUNTER,0			; COUNTER = | 0 |
ldi STATE,GREEN_STATE		; STATE = | GREEN_STATE |

busy:
rjmp busy			; goto busy

button:
sbrs STATE,GREEN_BIT		; if STATE [ GREEN_BIT ] == | 1 | skip
rjmp exit			; goto exit
tst COUNTER			; COUNTER <= | 0 |
brne exit			; if != goto exit
ldi STATE,YELLOW_STATE		; STATE = | YELLOW_STATE |
ldi COUNTER,3			; COUNTER = | 3 |
rjmp exit			; goto exit

timer:
sbrc STATE,GREEN_BIT		; if STATE [ GREEN_BIT ] == | 0 | skip
rjmp green			; goto green
sbrc STATE,YELLOW_BIT		; if STATE [ YELLOW_BIT ] == | 0 | skip
rjmp yellow			; goto yellow
sbrc STATE,RED_BIT		; if STATE [ RED_BIT ] == | 0 | skip
rjmp red			; goto red

yellow:
out OUTPUT,STATE		; OUTPUT = STATE
tst COUNTER			; COUNTER <= | 0 |
breq yellowNext			; if == goto yellowNext

yellowDec:
dec COUNTER			; COUNTER -= | 1 |
rjmp exit			; goto exit

yellowNext:
ldi STATE,RED_STATE		; STATE = | RED_STATE |
ldi COUNTER,10			; COUNTER = | 10 |
rjmp exit			; goto exit

red:
out OUTPUT,STATE		; OUTPUT = STATE
tst COUNTER			; COUNTER <= | 0 |
breq redNext			; if == goto redNext

redDec:
dec COUNTER			; COUNTER -= | 1 |
rjmp exit			; goto exit

redNext:
ldi STATE,GREEN_STATE		; STATE = | GREEN_STATE |
ldi COUNTER,10			; COUNTER = | 10 |
rjmp exit			; goto exit

green:
out OUTPUT,STATE		; OUTPUT = STATE
tst COUNTER			; COUNTER <= | 0 |
breq exit			; if == goto exit
dec COUNTER			; COUNTER -= | 1 |
rjmp exit			; goto exit

exit:
reti 				; reti
