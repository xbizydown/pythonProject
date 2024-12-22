from pprint import pprint
#
# text = input()
# ascii_values = [ord(i) for i in text]
# print(ascii_values)
#
# text = input()
# hex_values = text.encode().hex()
# print(hex_values)
#
# text = input()
# hex_string = ''.join(format(i, '02x') for i in bytes(text, 'utf-8'))
# ascii_characters = [chr(int(i, 16)) for i in hex_string]
# print(ascii_characters)

name_of_file = 'text.txt'
file_contents = """[Intro: Gangsta Boo & Kingpin Skinny Pimp]
An angel on the left, the Devil on the right
My head was in the middle
The sky was day and night
An angel on the left, the Devil on the right
My head was in the middle
The sky was day and night
An angel on the left, the Devil on the right
My head was in the middle

[Verse 1: LiL' Maniyak]

[Chorus: Gangsta Boo]
An angel on the left, the Devil on the right
An angel on the left, the Devil on the right
An angel on the left, the Devil on the right
An angel on the left, the Devil on the right

[Verse 2: LiL' Maniyak]

[Outro: Gangsta Boo & Kingpin Skinny Pimp]
An angel on the left, the Devil on the right
My head was in the middle
The sky was day and night
An angel on the left, the Devil on the right"""

with open(name_of_file, 'w') as file:
    file.write(file_contents)

print("Saved!")