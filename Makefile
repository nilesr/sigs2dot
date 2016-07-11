all:
	gpg --list-sigs > sigs
	python3 sigs2dot.py sigs > out.dot
	neato out.dot -Tsvg > out.svg
	convert out.svg out.png
	xdg-open out.png
clean:
	rm sigs out.dot out.svg out.png||:
