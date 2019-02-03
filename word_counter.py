word = input().lower()
words = []
o_f = open("voina i mir","r", encoding="utf-8")
count=0
for line in o_f:
    line = line.strip().lower()
    word_list = line.split()
    for new_word in word_list:
        if new_word[:len(word)] == word:
            count+=1
            if new_word not in words:
                words.append(new_word)
            if new_word == "ь.":
                print (line)
for w in words:
    print (w)
print ("kolichestvo slov {}".format(count))
