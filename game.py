# What prints is what the "AI" makes.

def play(choose):
    if choose == 'rock':
        print 'paper'
    elif choose == 'paper':
        print 'scissors'
    elif choose == 'scissors':
        print 'rock'
    else:
        print 'nil'

def run(prompt='> '):
    while True:
        play(raw_input(prompt))

if __name__ == '__main__':
    print 'Now you may start play.'
    run()