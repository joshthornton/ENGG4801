#ifndef _ENGG4801_SCANNER_H_
#define _ENGG4801_SCANNER_H_

#include <stdio.h>

#include "token.h"

typedef struct scanner {
	FILE *f;
	int line;					/* Line Number */
	int lineLookAhead;			/* Line Lookahead Number */
	int character;				/* Character Number */
	int characterLookAhead;		/* Character Lookahead Number */
	char next;					/* Next character */
} scanner;

int scanner_init( char *filename, scanner *s );
int scanner_get_next_token( scanner *s, token *t );
void scanner_exit( scanner *s );

#endif
