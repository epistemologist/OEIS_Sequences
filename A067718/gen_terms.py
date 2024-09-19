import requests,json,sys
from math import prod
from tqdm import tqdm

sys.set_int_max_str_digits(10**6)

FACTOR_DB_URL = "https://factordb.com/api"

def get_factors(n):
	data = json.loads( requests.get(FACTOR_DB_URL, params={"query": str(n)}).text )
	if data["status"] not in ["FF", "P"]:
		return None
	return [(int(p), e) for p,e in data["factors"] ]

for k in tqdm( range(1050, 2000) ):
	factors = get_factors(2**k+1)
	if factors is None: print(f"{k} ?")
	else:
		sigma = prod([ (pow(p,e+1)-1)//(p-1) for p,e in factors])
		if sigma % k == 0:
			print(f"{k} y")

