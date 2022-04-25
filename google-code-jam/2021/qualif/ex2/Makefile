debug:
	cat input.txt | ./solve.py 2>&1 | batcat

test:
	cat input-1.txt | ./solve.py | diff -s - expected-1.txt
	cat input-2.txt | ./solve.py | diff -s - expected-2.txt

.PHONY: debug test

