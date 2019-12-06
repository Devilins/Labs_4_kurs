import Encoder.Cesar


class DecryptCesar(object):

    def decrypt(self, encText, decText):
        file = Encoder.Cesar
        let1, count1 = file.lett_counting(' ', encText)
        let2, count2 = file.lett_counting(' ', decText)
        #print(let1, count1)
        #print(let2, count2)

        f = open(encText, 'r+')
        text = open('Dec_Text.txt', 'w')
        res = ''
        txt = ''
        for line in f:
            for c in line:
                if c in let1:
                    ind = let1.index(c)
                    hm = count1[ind]
                    ind = count2.index(hm)
                    res += let2[ind]
                else:
                    res += c
            text.write(res)
            txt += res
            res = ''
        f.close()
        text.close()
        return txt