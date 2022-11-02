#  write your code here 
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--file')

parser.add_argument('--cipher')

args = parser.parse_args()

filename = args.file

displacement = int(args.cipher)

opened_file = open(filename)
encoded_text = opened_file.read()  # read the file into a string
opened_file.close()  # always close the files you've opened


def decode_caesar_cipher(s, n):
    alpha = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',.?!"
    s = s.strip()
    text = ''
    for c in s:
        text += alpha[(alpha.index(c) + n) % len(alpha)]
    print('Decoded text: "' + text + '"')


decode_caesar_cipher(encoded_text, displacement)
