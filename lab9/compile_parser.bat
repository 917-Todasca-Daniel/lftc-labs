flex scanner.lex
bison -dy parser.y
gcc lex.yy.c y.tab.c
a.exe < p1.txt
a.exe < p2.txt
a.exe < p3.txt
a.exe < p1err.txt