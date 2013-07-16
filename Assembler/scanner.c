#include <stdio.h>

#include "scanner.h"
#include "misc.h"

int scanner_init( const char *filename, scanner *s )
{
	s->f = fopen( filename, "r" );
	s->line = 0;
	s->lineLookAhead = 0;
	s->character = 0;
	s->characterLookAhead = 0;
	s->next = fgetc( s->f );

	if ( s->f )
		return SUCESS;
	return FILE_ERR;
}

void get_char( scanner *s, char *c, char *n )
{
	*c = s->next;										/* copy next to current */ 
	s->character = s->characterLookAhead;				/* Set character counter */ 
	s->line = s->lineLookAhead;							/* Set line counter */
	*n = s->next = fgetc( s->f );						/* read in char to next */
	s->characterLookAhead++;							/* increment read counter */
	if ( s->next == '\n' )
	{
		s->lineLookAhead++;
		s->characterLookAhead = 0;
	}
}

int is_char( char c )
{
	return ( c >= 'A' && c <= 'Z' ) || ( c >= 'a' && c <= 'z' );
}

int is_num( char c )
{
	return ( c >= '0' && c <= '9' );
}

int scanner_get_next_token( scanner *s, token *t )
{
	char c, nc;

	do {

		/* Read Character from File */
		get_char( s, &c, &nc );
		t->c = s->character;
		t->l = s->line;

		/* Reached end of file */
		if ( c == EOF )
		{
			t->t = t_eof;
		}

		/* If c is [a-zA-Z] read identifier or keyword */
		if ( is_char( c ) )
		{
			return get_identifier_token( c, s, t );
		}

		/* If c is /(0x[0-9a-fA-F]+)|(0b[0-1]+)|(0o[0-7]+)|([0-9]+)/ then read constant */
		if ( is_num( c ) )
		{
			return get_constant_token( c, s, t );
		}

		switch( c )
		{

			/* skip white space */
			case ' ':
			case '\t':
			case '\f':
			case '\n':
			case '\r':
				break;
			
			case T_EQU[0]:
				if ( nc == T_EQU_EQU[1] )
				{
					t->t = t_equ_equ;
					get_char( s, &c, &nc ); /* Consume extra character */
					return SUCCESS;
				}
				t->t = t_equ;
				return SUCCESS;

			case T_ADD[0]:
				if ( nc == T_ADD_EQU[1] )
				{
					t->t = t_add_equ;
					get_char( s, &c, &nc ); /* Consume extra character */
					return SUCCESS;
				}
				t->t = t_add;
				return SUCCESS;;

			case T_AND_EQU[0]:
				if ( nc == T_AND_EQU[1] )
				{
					t->t = t_and_equ;
					get_char( s, &c, &nc ); /* Consume extra character */
					return SUCCESS;
				}
				return TOKEN_ERR;

			case T_SUB[0]:
				if ( nc == T_SUB_EQU[1] )
				{
					t->t = t_sub_equ;
					get_char( s, &c, &nc ); /* Consume extra character */
					return SUCCESS;
				}
				t->t = t_sub;
				return SUCCESS;

			default:
				return TOKEN_ERR; 
		}
	} while ( 1 );
}
void scanner_exit( scanner *s );
