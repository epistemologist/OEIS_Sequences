# A103132

## Calculate Pi in Base 26
Download first 10 billion digtis of pi from [here](https://jackgiffin.com/main/pi_10_billion/)
 
 ```bash
 $ time python3 base_convert.py
[+] Calculating P, 10000000000 digits
[+] Calculating Q
[+] Calculating 7067270923 base 26 digits...
100%|████████████████████████████████████████████████████████████████████████████| 22/22 [6:11:28<00:00, 1013.13s/it]

real    451m20.678s
user    408m1.438s
sys     41m33.453s
 ```
We only get ~6.9 * 10^9 base 26 digits of pi as we chop off the tail - we next look for words from the [SOWPODS Scrabble tournament wordlist ](https://raw.githubusercontent.com/jmlewis/valett/master/scrabble/sowpods.txt) of length 10 as well as a wordlist scrapped together from 
 - [here](https://www.keithv.com/software/wlist/).
 - titles of English Wiktionary articles
 - other wordlists I found online
 
## Possible Candidates for a(10)
(NOTE: The following numbers are given with 0 indexing (so "reformist" would have index 5204507 instead of 5204508 as given in OEIS) 
 - 74246467: CASTIGANTS (ones who are castigated / punished)
 - 1284753671: AFRICANESS (the state or quality of being African)
 - 2226422795: NONDENSITY (the state or quality of lacking density)
 - 2614458903: ELEVENSIES (A short mid-morning break taken around eleven o'clock for a drink or light snack.)
 - 3309828522: STRINGHOLE (A hole for a string)
 - 3316593903: SARAWAKIAN (Of or relating to Sarawak, a state in Eastern Malaysia)
 - 4817777122: AMISHWOMAN (Amish woman - can be one word [according to Wiktionary](https://en.wiktionary.org/wiki/Amishwoman))
 - 5281452216: CRUMPLEDUP (technically two words)
 - 5405488859: FLOTATIONS* (only candidates in the Scrabble dictionary)
 - 5553276652: MISCREENTS (misspelling of miscreants) 
 
As this is a vague enough sequence, any of these candidates could work for the next term.