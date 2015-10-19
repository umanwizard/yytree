Pass the `-t` field when invoking `yacc`.

Then...

	YYDEBUG=1 myParser < myInput | python yytree.py
