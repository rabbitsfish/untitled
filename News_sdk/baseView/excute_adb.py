# coding:utf-8
import subprocess

def excute_adb_shell(command):
    command = 'adb logcat|findstr News_'
    p = subprocess.Popen(command, shell=True, bufsize=1, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         encoding='utf-8')
    # for i in iter(p.stdout.readline, 'b'):
    #     print(i)
    #     # i
    while not p.poll():
        line = p.stdout.readline()
        if line:
            print(line)
        else:
            break
class ExcuteAdb:
    def __init__(self):
        pass

if __name__ == '__main__':
    excute_adb_shell('adb logcat|findstr News_')


