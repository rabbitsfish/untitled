x, y = 10, 20
z = x + y
print(z) #30
globals()['x'] = -100  # globals()修改变量x的值为-100
z = x + y
print(z)

