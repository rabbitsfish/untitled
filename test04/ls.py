import os
import time
import sys

def ls_copy(ls_li):
    if ls_li.__len__() > 1:
        ls_list = []
        if ls_li.__len__() == 2:
            print(ls_li)
            ls_com = ls_li[1]
            if ls_com.startswith('-'):
                ls_list = os.listdir(os.path.abspath(os.path.dirname(__file__)))
                if 'a' not in ls_com:
                    ls_list_copy = []
                    for i in ls_list:
                        if not i.startswith('.'):
                            ls_list_copy.append(i)
                    ls_list = ls_list_copy
                ls_dict_list = []
                if 'l' in ls_com:
                    for i in ls_list:
                        ls_stat = os.stat(os.path.abspath(i))
                        ls_dict = {}
                        ls_dict['ls_size'] = ls_stat.st_size
                        ls_dict['ls_mtime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ls_stat.st_mtime))
                        ls_dict['ls_ctime'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(ls_stat.st_ctime))
                        ls_dict['ls_name'] = i
                        ls_dict_list.append(ls_dict)
                    ls_list = ls_dict_list
                else:
                    ls_dict = {}
                    ls_dict['ls_name'] = i
                    ls_dict_list.append(ls_dict)
                if 'r' in ls_com:
                    ls_dict_list.sort(key=lambda ele:ele['ls_ctime'])
            else:
                print('command is must startswith -')

if __name__ == '__main__':
    print('sys.argv:', sys.argv)
    ls_copy(sys.argv)