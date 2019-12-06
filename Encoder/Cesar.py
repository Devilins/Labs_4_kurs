import re


class Cesar(object):

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
        f.close()
        text.close()
        return txt

    def lett_counting(self, file):
        f = open(file, 'r+')
        encr_letter = []
        encr_code = []
        for line in f:
            for c in line:
                k = re.findall(r'[АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя]', c)
                if k != []:
                    if c in encr_letter:
                        ind = encr_letter.index(c)
                        encr_code[ind] += 1
                    else:
                        encr_letter.append(c)
                        encr_code.append(1)
        f.close()
        return encr_letter, encr_code

