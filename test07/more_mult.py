import multiprocessing
import time
import os
base = 'C:\\Users\\dongff\\Desktop\\新建文件夹'
target_base = 'C:\\Users\\dongff\\Desktop\\新建文件夹1'

def get_path(base_path, target_base):
    list_path = os.listdir(base_path)
    for j in list_path:
        is_file = os.path.isfile(base_path + '\\' + j)
        if is_file:
            print(base_path + '\\' + j)
            if not os.path.exists(target_base + '\\' + j):
                os.mkdir(target_base + '\\' + j)
            with open(base_path + '\\' + j, 'rb') as file1:
                with open(target_base + '\\' + j, 'wb') as file2:
                    file2.write(file1.read())
        else:
            get_path(base_path + '\\' + j, target_base + '\\' + j)


get_path(base, target_base)

if __name__ == '__main__':
    pass