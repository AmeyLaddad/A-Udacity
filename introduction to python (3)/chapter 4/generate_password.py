import random

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

def generate_password():
    return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)

def generate_password1():
    return str().join(random.sample(word_list,3))
    
print (generate_password1())
