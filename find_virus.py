import os

FILE = r'D:\homework\images'
LOG = r'D:\homework\images\file_log.TXT'


def clear(LOG):
    f = open(LOG, 'w')
    f.close()


def find_php(FILE):
    for root, dirs, files in os.walk(FILE):
        for name in files:
            if name.split('.')[-1] == 'php':
                f = open(LOG, 'a')
                f.write(f'{os.path.join(root, name)}\n')
                f.close()
    print_LOG(LOG)


def print_LOG(LOG):
    f = open(LOG, 'r')
    for line in f.readlines():
        print(line, end='')


clear(LOG)
find_php(FILE)
