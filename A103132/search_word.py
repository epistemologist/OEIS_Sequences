import re
from tqdm import tqdm

pi_digits = open("pi_base26.txt","r").read()
wordlist = set([ re.sub("[^A-Z]+","", w.upper() ) for w in open("./wordlist/wordlist_all.txt","r").read().splitlines() ])

LEN = 10
wordlist = { w for w in wordlist if len(w) == LEN }

f=open("matches.txt", "w")
for i in tqdm(range(len(pi_digits)-LEN)):
	curr_word = pi_digits[i:i+LEN]
	if curr_word in wordlist:
		print(i, curr_word, ",", pi_digits[i:i+LEN+1])
		f.write(f"{i}: {curr_word}, {pi_digits[i:i+LEN+1]}\n")

f.close()
