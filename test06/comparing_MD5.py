import tkinter as tk
from tkinter import filedialog
import hashlib
import os
import requests
import threading

def upload_file1():
    global file1
    # entry1.select_clear()
    entry1.delete(0, 'end')
    selectFile = tk.filedialog.askopenfilename() # askopenfilename 1次上传1个；askopenfilenames1次上传多个
    # print('file1:', file1)
    entry1.insert(0, selectFile)

# def upload_file2():
#     global file2
    # entry2.delete(0, 'end')
    # file2 = entry2.get()
    #selectFile = tk.filedialog.askopenfilename()  # askopenfilename 1次上传1个；askopenfilenames1次上传多个
    # file2 = selectFile
    # print('file2:', file2)
    # entry2.insert(0, selectFile)

def compare_MD5():
    file1 = entry1.get()
    file2 = entry2.get()
    if file1 == '' or file2 == '':
        te = tk.Label(frm3, text='两处的文件都需要上传', bg='red', fg='white', font=('Arial', 12), width=30, height=2)
        te.grid(row=1, column=0)
        return
    file1 = file1.strip()
    file2 = file2.strip()
    if not os.path.exists(file1):
        te = tk.Label(frm3, text='路径不存在', bg='red', fg='white', font=('Arial', 12), width=30, height=2)
        te.grid(row=1, column=0)
        return
    if not os.path.isfile(file1):
        te = tk.Label(frm3, text='非文件', bg='red', fg='white', font=('Arial', 12), width=30, height=2)
        te.grid(row=1, column=0)
        return
    if not file2.startswith('http') and not file2.startswith('https'):
        te = tk.Label(frm3, text='下载链接需要以http或者https开头', bg='red', fg='white', font=('Arial', 12), width=30, height=2)
        te.grid(row=1, column=0)
        return
    with open(file1, 'rb') as apk1:
        da = apk1.read()
    apk1_MD5 = hashlib.md5(da).hexdigest()
    # print('apk1_MD5:', apk1_MD5)
    te = tk.Label(frm3, text='下载中，请稍后', bg='blue', fg='white', font=('Arial', 12), width=30, height=2)
    te.grid(row=1, column=0)
    try:
        r = requests.get(file2)
    except requests.exceptions.ConnectionError as e:
        # print('~~~~~~~~~', e.args)
        te = tk.Label(frm3, text='连接超时或者有其他问题', bg='red', fg='white', font=('Arial', 12), width=30, height=2)
        te.grid(row=1, column=0)
        return
    except (requests.exceptions.InvalidURL, requests.exceptions.MissingSchema) as e:
        te = tk.Label(frm3, text='路径非法', bg='red', fg='white', font=('Arial', 12), width=30, height=2)
        te.grid(row=1, column=0)
        return
    # print('status:', r.status_code)
    if r.status_code == 404:
        te = tk.Label(frm3, text='下载链接不存在', bg='red', fg='white', font=('Arial', 12), width=30, height=2)
        te.grid(row=1, column=0)
        return
    if os.path.exists('1.apk'):
        os.remove('1.apk')
    with open('1.apk', 'wb') as apk2:
        apk2.write(r.content)
    apk2_MD5 = hashlib.md5(r.content).hexdigest()
    # print('apk2_MD5:', apk2_MD5)

    if apk1_MD5 == apk2_MD5:
        te = tk.Label(frm3, text='MD5值相同', bg='green', fg='white', font=('Arial', 12), width=30, height=2)
        te.grid(row=1, column=0)
    else:
        te = tk.Label(frm3, text='MD5值不同', bg='red', fg='white', font=('Arial', 12), width=30, height=2)
        te.grid(row=1, column=0)

def compare_MD5_thread():
    t = threading.Thread(target=compare_MD5)
    t.setDaemon(True)
    t.start()

window = tk.Tk()
window.geometry('500x400')
window.title('比较两个文件的MD5值')
# l = tk.Label(window, text='你好！this is Tkinter', bg='green', font=('Arial', 12), width=30, height=2)
# l.pack()
frm1 = tk.Frame(window)
frm1.grid(padx='20', pady='10')
btn1 = tk.Button(frm1, text='上传文件1', command=upload_file1)
btn1.grid(row=0, column=0, ipadx='3', ipady='3', padx='10', pady='20')
entry1 = tk.Entry(frm1, width='40')
entry1.grid(row=0, column=1)

frm2 = tk.Frame(window)
frm2.grid(padx='20', pady='10')
lb2 = tk.Label(frm2, text='下载链接:')
lb2.grid(row=0, column=0, ipadx='3', ipady='3', padx='10', pady='20')
entry2 = tk.Entry(frm2, width='40')
entry2.grid(row=0, column=1)

frm3 = tk.Frame(window)
frm3.grid(padx='20', pady='10')
btn = tk.Button(frm3, text='比较两个文件的MD5值', command=compare_MD5_thread)
btn.grid(row=0, column=0, ipadx='3', ipady='3', padx='10', pady='20')

window.mainloop()

