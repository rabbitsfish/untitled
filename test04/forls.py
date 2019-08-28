
import os
import sys
from pathlib import Path
# print(__file__)
# print((os.path.dirname(__file__)))
filename = 'E:'
li = os.listdir(os.path.abspath(filename))
sum_li = []
# for i in li:
#     print(i)
#     print(os.path.abspath(i))
#     print(os.stat('%s\%s' % (filename, i)))
def get_son_list(par_dir, filename):
    if Path('%s/%s' % (par_dir, filename)).is_dir():
        base_path = os.path.abspath('%s/%s' % (par_dir, filename))
        son_li = os.listdir(base_path)
        for son in son_li:
            get_son_list(os.path.abspath('%s/%s' % (par_dir, filename)), son)
    else:
        sum_li.append(os.path.abspath('%s/%s' % (par_dir, filename)))

if __name__ == '__main__':
    for i in li:
        get_son_list(os.path.abspath(filename), i)
    for file_name in sum_li:
        print(file_name)
    print(sum_li.__len__())