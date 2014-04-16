# It's a program to save some functions I use.

__all__ = [
    'warner', 'timer','word_count',
    'view', 'greeting','clear',
    'word_find','length','get_email_name'
]

import time, random

def warner(thing):
    """You can input seconds to warn you to do something."""
    sec = raw_input("How many seconds you want?")
    print thing
    time.sleep(float(sec))
    print "\a\a\a\a\a"
    
def timer(func, *arg):
    """Time the function it takes."""
    start = time.clock()
    return func(*arg), time.clock() - start
    
def word_count(filename):
    try:
        text = open(filename).readlines()
        string = ' '.join(text)
        words = string.split()
        print 'It consists of %s characters and %s words.' % (len(string),  len(words))
    except IOError:
        print 'It does not exist.'

def view(filename):
    def process(info):
        print info
    for line in open(filename):
	process(line)

def greeting():
    """Return a sentence to encourage and greet."""
    words = ['Live long and prosper!',
             'Hacking spirit will be with you.',
	     'Funny love is with me as always.',
	     'May the sourse be with you!',
	     'It is the start of a nice program.']
    return random.choice(words)

def clear(lst):
    """Clean a list if it's not null."""
    if lst == []:
	print 'It is null.'
    else:
        del lst[:]

def word_find(word, filename):
    text = open(filename).readlines()
    for line in text:
	if word in line:
	    print line

def get_email_name(email):
    name = email.split('@')[0]
    print name

#It's a function to "develop" myself,it's lispy.
car  = lambda x: x[0]
cdr  = lambda x: x[1:]
null = lambda x: x == []

def length(lst, num=0):
    if null(lst):
	return num
    else:
	num += 1
	return length(cdr(lst), num)
