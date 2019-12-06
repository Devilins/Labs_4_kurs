import re


class Cesar(object):
    attr1 = " "

    def encrypt(self, file, key):
        f = open(file, 'r+')
        text = open('Enc_Text.txt', 'w')
        alpha = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        res = ''
        txt = ''
        for line in f:
            for c in line:
                k = re.findall(r'[АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя]', c)
                if k != []:
                    res += alpha[(alpha.index(c) + key) % len(alpha)]
                else:
                    res += c
            text.write(res)
            txt += res
            res = ''
        return txt