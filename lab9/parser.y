%{
#include <stdio.h>
#include <stdlib.h>

#define YYDEBUG 1

int yydebug = 0;
%}

%token TYPE
%token IF_KEY
%token ELSE_KEY
%token RUN_KEY
%token IN_KEY
%token OUT_KEY

%token IDENTIFIER
%token ICONSTANT
%token SCONSTANT

%left '+' '-' '*' '/'

%token PLUS
%token MINUS
%token DIV
%token MOD
%token MUL

%token EQUALS
%token BIGGER_THAN
%token SMALLER_THAN

%token ASSIGN
%token NOT_EQUALS
%token SMALLER_OR_EQUAL
%token GREATER_OR_EQUAL

%token RAISE_POW

%token OPEN_ROUND_BRACKET
%token CLOSED_ROUND_BRACKET
%token OPEN_RIGHT_BRACKET
%token CLOSED_RIGHT_BRACKET
%token OPEN_CURLY_BRACKET
%token CLOSED_CURLY_BRACKET

%token DOT
%token COLON
%token NEW_LINE

%start code

%%
code : program
program : instr | instr program;
instr : decl | logic_instr | NEW_LINE;
decl : var_decl | arr_decl;
var_decl : TYPE id;
arr_decl : TYPE id OPEN_RIGHT_BRACKET ICONSTANT CLOSED_RIGHT_BRACKET;

logic_instr : assign_stmt | in_stmt | out_stmt | if_stmt | else_stmt | while_stmt;

assign_stmt : id ASSIGN expression;
expression : term | OPEN_ROUND_BRACKET expression CLOSED_ROUND_BRACKET 
	| expression math_op expression;
math_op : PLUS | MINUS | DIV | MUL | RAISE_POW | MOD;
term: id | ICONSTANT | SCONSTANT;

in_stmt : IN_KEY OPEN_ROUND_BRACKET id CLOSED_ROUND_BRACKET;
out_stmt : OUT_KEY OPEN_ROUND_BRACKET id CLOSED_ROUND_BRACKET;
id : IDENTIFIER | IDENTIFIER OPEN_CURLY_BRACKET expression CLOSED_CURLY_BRACKET;

if_stmt : IF_KEY condition COLON NEW_LINE program DOT;
else_stmt: IF_KEY condition COLON NEW_LINE program ELSE_KEY COLON NEW_LINE program DOT;
condition : expression relation expression;
relation : SMALLER_THAN | BIGGER_THAN | EQUALS | NOT_EQUALS 
	| GREATER_OR_EQUAL | SMALLER_OR_EQUAL;

while_stmt : RUN_KEY condition COLON program DOT;

%%
yyerror(char *s)
{
	printf("%s\n",s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
	if(!yyparse()) fprintf(stderr, "\tO.K.\n"); 
}