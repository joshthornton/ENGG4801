#ifndef _ENGG4801_TOKEN_H_
#define _ENGG4801_TOKEN_H_

#define T_EQU	 	"="
#define T_ADD_EQU 	"+="
#define T_AND_EQU	"&="
#define T_SUB_EQU	"-="
#define T_EQU_EQU	"=="
#define T_XOR_EQU	"^="
#define T_COL		":"
#define T_ABS		"|"
#define T_FMUL		"x"
#define T_RSHFT		">>"
#define T_LSHFT		"<<"
#define T_MUL		"*"
#define T_ADD		"+"
#define T_OR_EQU 	"|="
#define T_SUB		"-"
#define T_ARSHFT	">>>"
#define T_SREG		"SREG"
#define T_RSBRACE	"["
#define T_LSBRACE	"]"
#define T_RRBRACE	"(
#define T_LRBRACE	")"
#define T_SWAP		"SWAP"
#define T_IF		"IF"
#define T_GOTO		"GOTO"
#define T_FUNC		"()"
#define T_SKIP		"SKIP"
#define T_INDIRECT	"*"
#define T_RET		"RET"
#define T_RETI		"RETI"
#define T_MEM		"MEM"
#define T_RAM		"RAM"
#define T_PMEM		"PMEM"
#define T_POP		"POP"
#define T_PUSH		"PUSH"
#define T_SLEEP		"SLEEP"
#define T_WDR		"WDR"

enum Token
{
	t_equ,
	t_add_equ,
	t_and_equ,
	t_sub_equ,
	t_equ_equ,
	t_xor_equ,
	t_col,
	t_abs,
	t_fmul,
	t_rshft,
	t_lshft,
	t_mul,
	t_add,
	t_or_equ,
	t_sub,
	t_arshft,
	t_sreg,
	t_rsbrace,
	t_lsbrace,
	t_rrbrace,
	t_lrbrace,
	t_swap,
	t_if,
	t_goto,
	t_func,
	t_skip,
	t_indirect,
	t_ret,
	t_reti,
	t_mem,
	t_ram,
	t_pmem,
	t_pop,
	t_push,
	t_sleep,
	t_wrd,
	t_gp_reg,
	t_io_reg,
	t_reg_pair,
	t_constant,
	t_eof
};

typedef struct token {
	Token t;
	int l;		/* Line No. */
	int c;		/* Character No. */
	int val;	/* Register Address, Constant Value */
} token;

#endif
