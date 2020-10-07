# from Cryptodome.Cipher import AES
# from binascii import b2a_hex, a2b_hex
#
#
# # 如果text不足16位的倍数就用空格补足为16位
# def add_to_16(text):
#     if len(text.encode('utf-8')) % 16:
#         add = 16 - (len(text.encode('utf-8')) % 16)
#     else:
#         add = 0
#     text = text + ('\0' * add)
#     return text.encode('utf-8')
#
#
# # 加密函数
# def encrypt(key, iv, text):
#     key = key.encode('utf-8')
#     mode = AES.MODE_CBC
#     # iv = b'qqqqqqqqqqqqqqqq'
#     text = add_to_16(text)
#     cryptos = AES.new(key, mode, iv)
#     cipher_text = cryptos.encrypt(text)
#     # 因为AES加密后的字符串不一定是ascii字符集的，输出保存可能存在问题，所以这里转为16进制字符串
#     return b2a_hex(cipher_text)
#
#
# # 解密后，去掉补足的空格用strip() 去掉
# def decrypt(key, iv, text):
#     key = key.encode('utf-8')
#     #key = 'b1ac9861485a652b'.encode('utf-8')
#     # iv = '1269571569321210'
#     # iv = b'1234123412341234'
#     mode = AES.MODE_CBC
#     cryptos = AES.new(key, mode, iv)
#     plain_text = cryptos.decrypt(a2b_hex(text))
#     return bytes.decode(plain_text).rstrip('\0')
#
#
# if __name__ == '__main__':
#     content = 'testtesttesttesttesttesttesttest'
#     iv = b'1269571569321210'
#     key = 'b1ac9861485a652b'
#     e = encrypt(key, iv, content)  # 加密
#     d = decrypt(key, iv, e)  # 解密
#     print('content:', content)
#     print("加密:", e)
#     print("解密:", d)

import xlrd
wb = xlrd.open_workbook('11.xlsx')
sheet1 = wb.sheet_by_index(0)
sumA = 0.0;
sumB = 0.0;

for i in range(37):
    if i == 0:
        continue
    if i % 2 == 0:
        sumB = sumB + sheet1.cell(i, 1).value
        continue
    if i % 2 != 0:
        sumA = sumA + sheet1.cell(i, 1).value
        continue

print(sumA)
print(sumB)
aaa = sumA / 18
bbb = sumB / 18
A1 = aaa * 3.2893296 + bbb * 5.4725318 - 11.5307833
B1 = aaa * 7.2371075 + bbb * 8.1776448 - 32.3553266
C1 = aaa * 3.9246754 + bbb * 9.7102446 - 28.4573220
D1 = aaa * 7.3654621 + bbb * 4.9392039 - 22.22810880
print('安全型：' + str(A1))
print('恐惧型: ' + str(B1))
print('专注型: ' + str(C1))
print('冷漠型: ' + str(D1))