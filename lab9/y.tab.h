
/* A Bison parser, made by GNU Bison 2.4.1.  */

/* Skeleton interface for Bison's Yacc-like parsers in C
   
      Copyright (C) 1984, 1989, 1990, 2000, 2001, 2002, 2003, 2004, 2005, 2006
   Free Software Foundation, Inc.
   
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   
   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   
   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.
   
   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */


/* Tokens.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
   /* Put the tokens into the symbol table, so that GDB and other debuggers
      know about them.  */
   enum yytokentype {
     TYPE = 258,
     IF_KEY = 259,
     ELSE_KEY = 260,
     RUN_KEY = 261,
     IN_KEY = 262,
     OUT_KEY = 263,
     IDENTIFIER = 264,
     ICONSTANT = 265,
     SCONSTANT = 266,
     PLUS = 267,
     MINUS = 268,
     DIV = 269,
     MOD = 270,
     MUL = 271,
     EQUALS = 272,
     BIGGER_THAN = 273,
     SMALLER_THAN = 274,
     ASSIGN = 275,
     NOT_EQUALS = 276,
     SMALLER_OR_EQUAL = 277,
     GREATER_OR_EQUAL = 278,
     RAISE_POW = 279,
     OPEN_ROUND_BRACKET = 280,
     CLOSED_ROUND_BRACKET = 281,
     OPEN_RIGHT_BRACKET = 282,
     CLOSED_RIGHT_BRACKET = 283,
     OPEN_CURLY_BRACKET = 284,
     CLOSED_CURLY_BRACKET = 285,
     DOT = 286,
     COLON = 287,
     NEW_LINE = 288
   };
#endif
/* Tokens.  */
#define TYPE 258
#define IF_KEY 259
#define ELSE_KEY 260
#define RUN_KEY 261
#define IN_KEY 262
#define OUT_KEY 263
#define IDENTIFIER 264
#define ICONSTANT 265
#define SCONSTANT 266
#define PLUS 267
#define MINUS 268
#define DIV 269
#define MOD 270
#define MUL 271
#define EQUALS 272
#define BIGGER_THAN 273
#define SMALLER_THAN 274
#define ASSIGN 275
#define NOT_EQUALS 276
#define SMALLER_OR_EQUAL 277
#define GREATER_OR_EQUAL 278
#define RAISE_POW 279
#define OPEN_ROUND_BRACKET 280
#define CLOSED_ROUND_BRACKET 281
#define OPEN_RIGHT_BRACKET 282
#define CLOSED_RIGHT_BRACKET 283
#define OPEN_CURLY_BRACKET 284
#define CLOSED_CURLY_BRACKET 285
#define DOT 286
#define COLON 287
#define NEW_LINE 288




#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED
typedef int YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define yystype YYSTYPE /* obsolescent; will be withdrawn */
# define YYSTYPE_IS_DECLARED 1
#endif

extern YYSTYPE yylval;


