import Encoder

file = Encoder.Cesar()
print(file.encrypt('Tolstoi.txt', 1))

text = Encoder.DecryptCesar()
text.decrypt('Enc_Text.txt', 'Tolstoi.txt')