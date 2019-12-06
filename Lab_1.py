import Encoder

file = Encoder.Cesar()
print(file.encrypt('Tolstoi.txt', 3))

text = Encoder.DecryptCesar()
print(text.decrypt('Enc_Text.txt', 'Tolstoi.txt'))