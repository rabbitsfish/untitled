import sys
import os
base_tools_path = os.path.abspath('C:\\Users\\dongff\\PycharmProjects\\untitled\\test03\\base_tools')
curPath = os.path.abspath(os.path.dirname(base_tools_path))
sys.path.append(curPath)
print(sys.path)
# from test03 import base_tools
def get_imeis():
    base_imei='00860021165104'
    imei_list = []
    for i in range(10):
        imei = base_imei + str(i)
        imei_list.append(base_tools.encryption_s(imei))
    return imei_list



# if __name__ == '__main__':
#     print(111)