import random
def mix(word):
    nw = word[1:-1]
    nw.shuffle()
    return

data = []
in_file = open("txt.txt", "r", encoding='utf-8')
for line in in_file:
    data.append(line)
in_file.close()

out_data = []
for line in data:
    words = line.split()
    print(words)
    for i in range(0, len(words)):
        words[i] = mix(words[i])
    out_data.append(" ".join(words))

out_file = open("out_txt.txt", "w", encoding ="utf-8" )
for line in out_data:
    print(line, file = out_file)
out_file.close()
