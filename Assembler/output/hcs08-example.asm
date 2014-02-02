
setup:
ldx #7				; x = | 7 |
stx DDRA			; DDRA = x
ldx #23				; x = | 23 |
stx SRTISC			; SRTISC = x
ldx #18				; x = | 18 |
stx IRQSC			; IRQSC = x
lda #0				; a = | 0 |
mov #GREEN_STATE,STATE		; STATE = | GREEN_STATE |

busy:
bra busy			; goto busy

button:
brset GREEN_BIT,STATE,1		; if STATE [ GREEN_BIT ] == | 1 | skip
bra exit			; goto exit
tsta 				; a <= | 0 |
bne exit			; if != goto exit
mov #YELLOW_STATE,STATE		; STATE = | YELLOW_STATE |
lda #3				; a = | 3 |
bset 2,IRQSC			; IRQSC [ 2 ] = | 1 |
bra exit			; goto exit

timer:
brclr GREEN_BIT,STATE,1		; if STATE [ GREEN_BIT ] == | 0 | skip
bra green			; goto green
brclr YELLOW_BIT,STATE,1	; if STATE [ YELLOW_BIT ] == | 0 | skip
bra yellow			; goto yellow
brclr RED_BIT,STATE,1		; if STATE [ RED_BIT ] == | 0 | skip
bra red				; goto red

yellow:
mov STATE,OUTPUT		; OUTPUT = STATE
tsta 				; a <= | 0 |
beq yellowNext			; if == goto yellowNext

yellowDec:
deca 				; a -= | 1 |
bra exit			; goto exit

yellowNext:
mov #RED_STATE,STATE		; STATE = | RED_STATE |
lda #10				; a = | 10 |
bra exit			; goto exit

red:
mov STATE,OUTPUT		; OUTPUT = STATE
tsta 				; a <= | 0 |
beq redNext			; if == goto redNext

redDec:
deca 				; a -= | 1 |
bra exit			; goto exit

redNext:
mov #GREEN_STATE,STATE		; STATE = | GREEN_STATE |
lda #10				; a = | 10 |
bra exit			; goto exit

green:
mov STATE,OUTPUT		; OUTPUT = STATE
tsta 				; a <= | 0 |
beq exit			; if == goto exit
deca 				; a -= | 1 |
bra exit			; goto exit

exit:
rti 				; reti
