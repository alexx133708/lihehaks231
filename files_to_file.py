import os

DIR = r'D:\homework\lesson3'


def find(DIR):
    all_content = ''
    for root, dirs, files in os.walk(DIR):
        for name in files:
            f = open(os.path.join(root, name), 'r', encoding='utf-8')
            all_content += f.read() + ' '
    with open(os.path.join('D:\homework\lesson3','all_content.txt'), 'w') as f1:
        f1.write(all_content)



find(DIR)

