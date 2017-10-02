# 01
stressed = "stressed"

# 02
patato = "パタトクカシーー"
get_string = patato[1] + patato[3] + patato[5] + patato[7]

# 03
patoka = "パトカー"
takushi = "タクシー"
patato = ""

for p, t in zip(patoka, takushi):
    patato += p
    patato += t

# 04 
alphabets = [chr(i) for i in range(97, 97+26)]
pistring = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics"
string_count_ary = []
for word in pistring.split(" "):
    count_ary = [0]*len(alphabets)
    for char in word: 
        low_char = char.lower()
        for i, alphabet in enumerate(alphabets):
            if alphabet == low_char:
                count_ary[i] += 1
    string_count_ary.append(count_ary)

# 05
gensostring = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
one_char_index = [0, 4, 5, 6, 7, 8, 14, 15, 18]
genshi_map = {}
for i, gen in enumerate(gensostring.split(" ")):
    if i in one_char_index:
        key = gen[0]
    else:
        key = gen[:2]
    genshi_map[key] = i+1
 
# 06
def get_bigram(string):
    str_ary = string.split(" ")
    return zip(str_ary, str_ary[1:])

string = "I am an NLPer"
bigram = get_bigram(string)
print(list(bigram))

