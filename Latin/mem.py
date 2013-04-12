# It is a program for me to memorize Latin words.
# And for learning how to code as well.

text = open('words.txt').readlines()

def find(word):
    for line in text:
	if word in line:
	    print line

def run(prompt='Word> '):
    while True:
	val = find(raw_input(prompt))
	if val is not None: print val

if __name__ == '__main__':
    print "Guo Jing code the program, it's Ver 1.0. But it actually works."
    run()
