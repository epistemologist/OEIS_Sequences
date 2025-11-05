from itertools import combinations
from fractions import Fraction as F
from tqdm import tqdm

def gen_bad_sets(N):
	out = []
	for b,c in combinations(range(1, N+1), 2):
		tmp = F(1,b) + F(1,c)
		if tmp.numerator == 1:
			a = tmp.denominator
			if a != b and a != c: out.append({a,b,c})
	return out


def A390395(N):
    bad_sets = gen_bad_sets(N)
    # print('bad sets: ', bad_sets)
    for k in reversed(range(N)):
        for S in combinations(range(1, N+1), k):
            S = set(S)
            if all([not B.issubset(S) for B in bad_sets]):
                return S


