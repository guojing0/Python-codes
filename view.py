import sys

file_name = open(sys.argv[1])

def process(info):
    print info

def run():
    for f in file_name:
	process(f)

if __name__ == '__main__': run()

file_name.close()
