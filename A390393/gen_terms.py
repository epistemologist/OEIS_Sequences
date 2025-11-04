from collections import deque, namedtuple
from itertools import combinations, count
from fractions import Fraction as F
from tqdm import tqdm

def gen_bad_sets(N):
    # Use BFS to generate all S \subseteq [N] s.t. \sum_{n \in S} 1/n = 1
    # print(f"[+] Calculating bad sets for N={N}...")
    SearchNode = namedtuple("SearchNode", ["S", "sum", "max_n"])
    queue = deque([
        SearchNode(S = (), sum = 0, max_n = 0)
    ])
    out = set()
    for _ in tqdm(count(1)):
        if len(queue) == 0:
            break
        cur = queue.popleft()
        if cur.sum == 1:
            out.add(cur); continue
        if cur.sum > 1 or cur.max_n >= N:
            continue
        n = cur.max_n
        queue.extend([
            SearchNode(
                S = cur.S,
                sum = cur.sum,
                max_n = n+1
        ),
            SearchNode(
                S = tuple( set(cur.S) | {n+1}),
                sum = cur.sum + F(1, n+1),
                max_n = n+1
            )
        ])
    return [set(i.S) for i in out]

# Brute force to sanity test the above function
def powerset_iterator(S):
	for k in range(len(S)+1):
		for subset in combinations(S, k):
			yield set(subset)

def gen_bad_sets_brute(N):
	return [ S 
		for S in powerset_iterator(range(1, N+1))
		if sum(F(1, i) for i in S) == 1
	]

	
def sanity_test():
	for i in range(1, 15):
		# Check if gen_bad_sets and gen_bad_sets_brute contain the same sets for all i
		assert set(map(tuple, gen_bad_sets(i))) == set(map(tuple, gen_bad_sets_brute(i)))
	return True

def A390393(N):
    bad_sets = gen_bad_sets(N)
    # print('bad sets: ', bad_sets)
    for k in reversed(range(N)):
        for S in combinations(range(1, N+1), k):
            S = set(S)
            if all([not B.issubset(S) for B in bad_sets]):
                return S

sanity_test()
out = []
for i in range(1, 15):
    tmp = A390393(i)
    print(i, len(tmp), tmp)
    out.append((i, len(tmp), tmp))
