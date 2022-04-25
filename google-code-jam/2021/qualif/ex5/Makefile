debug:
	cat input.txt | ./solve.py 2>&1 | batcat

test:
	cat input.txt | ./solve.py | diff -s - expected.txt

.PHONY: debug test

