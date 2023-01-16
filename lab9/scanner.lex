%{
#include <stdio.h>
#include <string.h>
#include "y.tab.h"
int lines = 0;
%}

%option noyywrap
%x CMNT

DIGIT [0-9]
NON_ZERO_DIGIT [1-9]
LETTER [a-zA-Z_]
INT_CONSTANT [-]?{NON_ZERO_DIGIT}{DIGIT}*|0
STRING_CONSTANT \"({LETTER}|{DIGIT})*\"
IDENTIFIER {LETTER}({LETTER}|{DIGIT})*
BAD_IDENTIFIER ({DIGIT})+({LETTER})+({LETTER}|{DIGIT})*

%%
"#" {BEGIN CMNT;} 
<CMNT>. {;}
<CMNT>\n {++lines; BEGIN INITIAL;}
\n {
    printf("new line\n");
++lines;
return NEW_LINE;
}

"run" { printf("%s - reserved word\n", yytext); return RUN_KEY; }
"out" { printf("%s - reserved word\n", yytext); return OUT_KEY; }
"in" { printf("%s - reserved word\n", yytext); return IN_KEY; }
"if" { printf("%s - reserved word\n", yytext); return IF_KEY; }
"el" { printf("%s - reserved word\n", yytext); return ELSE_KEY; }
"i" { printf("%s - reserved word\n", yytext); return TYPE; }
"s" { printf("%s - reserved word\n", yytext); return TYPE; }

{IDENTIFIER} {printf("%s - identifier\n", yytext); return IDENTIFIER; }
{BAD_IDENTIFIER} {printf("Error at token %s at line %d\n", yytext, lines); return -1;}

{INT_CONSTANT} {printf("%s - int constant\n", yytext); return ICONSTANT; }
{STRING_CONSTANT} {printf("%s - str constant\n", yytext); return SCONSTANT; }

"+" { printf("%s - operator\n", yytext); return PLUS; }
"-" { printf("%s - operator\n", yytext); return MINUS; }
"*" { printf("%s - operator\n", yytext); return MUL; }
"/" { printf("%s - operator\n", yytext); return DIV; }
"**" { printf("%s - operator\n", yytext); return RAISE_POW; }
"%" { printf("%s - operator\n", yytext); return MOD; }
"=" { printf("%s - operator\n", yytext); return ASSIGN; }
">" { printf("%s - operator\n", yytext); return BIGGER_THAN; }
">=" { printf("%s - operator\n", yytext); return GREATER_OR_EQUAL; }
"<" { printf("%s - operator\n", yytext); return SMALLER_THAN; }
"<=" { printf("%s - operator\n", yytext); return SMALLER_OR_EQUAL; }
"==" { printf("%s - operator\n", yytext); return EQUALS; }
"!=" { printf("%s - operator\n", yytext); return NOT_EQUALS; }

"(" { printf("%s - separator\n", yytext); return OPEN_ROUND_BRACKET; }
")" { printf("%s - separator\n", yytext); return CLOSED_ROUND_BRACKET; }
"[" { printf("%s - separator\n", yytext); return OPEN_RIGHT_BRACKET; }
"]" { printf("%s - separator\n", yytext); return CLOSED_RIGHT_BRACKET; }
"{" { printf("%s - separator\n", yytext); return OPEN_CURLY_BRACKET; }
"}" { printf("%s - separator\n", yytext); return CLOSED_CURLY_BRACKET; }
":" { printf("%s - separator\n", yytext); return COLON; }
"\." { printf("%s - separator dot\n", yytext); return DOT; }

[ \t]+ { printf("tab\n");}

[\n]+ {++lines; return NEW_LINE;}

. {printf("Error at token %s at line %d\n", yytext, lines); return -1;}

%%