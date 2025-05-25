from itertools import count
from math import log
from typing import *
from string import ascii_uppercase, ascii_lowercase, digits

from tqdm import tqdm
import gmpy2
from gmpy2 import mpz

def base_convert( 
	x: Tuple[mpz, mpz], 
	base_out: mpz, 
	chunk_size: mpz,
	num_digits: int,
	mapping: Optional[Dict]
) -> List[int]:
	"""
	Takes in x as a tuple of ints - representing it as a rational
	"""
	if mapping is None: mapping = dict()
	base_chunk = base_out ** chunk_size 
	out = ""
	p, q = x
	for _ in tqdm(count(1), total = num_digits//chunk_size):
		p *= base_chunk
		next_digit = p // q
		# next digit in base base_chunk
		# break up into smaller base
		out += next_digit.digits(base_out).zfill(chunk_size).translate(mapping)
		p -= (next_digit * q)
		if len(out) > num_digits: break
	return out

PI_FRAC = open("pi_frac.txt", "r").read() # This file should start 14159... to as many digits that are needed
NUM_DEC_DIGITS = len(PI_FRAC.strip())
print(f"[+] Calculating P, {NUM_DEC_DIGITS} digits")
P = mpz(PI_FRAC)
print("[+] Calculating Q")
Q = mpz(10) ** NUM_DEC_DIGITS

NUM_BASE26_DIGITS = int( NUM_DEC_DIGITS * log(10)/log(26) )
print(f"[+] Calculating {NUM_BASE26_DIGITS} base 26 digits...")

output=open("pi_base26.txt", "w")
output.write(
	base_convert(
		x = (P,Q),
		base_out = 26,
		chunk_size = 3*10**8,
		num_digits = int(0.95 * NUM_BASE26_DIGITS),
		mapping = dict(zip([ord(i) for i in  ( digits + ascii_lowercase )[:26] ], ascii_uppercase))
	)
)
output.close()

