from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        c = Counter()
        for i, s in enumerate(strs):
            d[frozenset((Counter(s).items()))].append(i)
        res = []
        for v in d.values():
            ss = [strs[vi] for vi in v]
            res.append(ss)
        return res