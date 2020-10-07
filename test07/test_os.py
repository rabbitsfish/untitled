import os
if not os.path.exists('b'):
    os.mkdir('b')
if not os.path.exists('b/test.txt'):
    file = open('b/test.txt', 'w')
    file.write("Hello World!")
    file.close()