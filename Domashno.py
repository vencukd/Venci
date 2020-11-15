'''
1. Модифицирайте програмта на изчисляване на комплиментарна ДНК, така че да чете входните данни
от файл и да записва резултата в друг файл.
'''

def complement_dna(dna):
    rep_1 = dna.replace("A", "t")
    rep_2 = rep_1.replace("T", "s")
    rep_3 = rep_2.replace("G", "c")
    rep_4 = rep_3.replace("C", "g")
    complementary_dna = rep_4.upper()
    return complementary_dna

dnk = open("dnk.txt")

for line in dnk:
    print(line)
    complement_dna(line)
dnk.close()

dnk_c = complement_dna(line)

comp_dnk = open("complementary_dnk.txt", "w")
comp_dnk.write(dnk_c)
print(dnk_c, end="")
comp_dnk.close()


'''
2. Модифицирайте програмта за определяне на най-често срещан символ, така че да взема данните от файл.
'''

string_f = open("string.txt", encoding="utf-8")
for i in string_f:
    my_string = i
string_f.close()

my_string = my_string.replace(" ", "")
if len(my_string) < 1:
    print("Invalid format")
    exit()
characters = {}

for ch in my_string:
    if characters.get(ch) is None:
        characters[ch] = 1
    else:
        characters[ch] = characters.get(ch) + 1

print(characters)

max_count = 0
for key, count in characters.items():
    if count > max_count:
        max_count = count
        top_char = key

print(f"Най-често стрещаният символ е {top_char} - {max_count} пъти")

'''
3. Напишете програма, която определя най-често получавания е-майл адрес от приложения файл.
'''

def prRed(skk): print("\033[91m {}\033[00m".format(skk))

list_line = []

f = open("mbox-short.txt", "r", encoding="utf-8")
for i in f:
    if f.readline(1) in "F":
        list_line.append(f.readline()[5:-1])
f.close()

list_line.remove("Changed")
# print(list_line)
max_count = 0

for mail in list_line:
    if list_line.count(mail) > max_count:
        max_count = list_line.count(mail)
        top_mail = mail

prRed(f"Най-често получавания е-майл адрес e: {top_mail} - {max_count} пъти.")