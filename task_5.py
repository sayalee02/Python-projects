#Task5: File Manipulation

f = open("Level 2/task5.txt")
file = f.read()
f.close()
print(file)

word_count = {}
for line in file.splitlines():                # splits each line in the file
    for word in line.strip().lower().split(): #splits the word in each line
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

for word, count in word_count.items():
    print(f"{word}: {count}")
















    #
""""
f = open("Level 2/task5.txt")
list=[]
file=f.read()
f.close()
print(file)

for line in file.splitlines():
    for word in line.split():
        list.append(word)
print(list)
list.sort()
print(list)
for word in list:
    print(word, end=" ")
    occ= file.count(word)
    print(occ)


text = open("Level 2/task5.txt", "r")
d = dict()
for line in text:
	line = line.strip()
	line = line.lower()
	words = line.split(" ")
	for word in words:
		if word in d:
			d[word] = d[word] + 1
		else:
			d[word] = 1
for key in list(d.keys()):
	print(key, ":", d[key])
"""	
