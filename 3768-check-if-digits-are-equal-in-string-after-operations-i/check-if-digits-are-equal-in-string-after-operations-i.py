class Solution:
    def hasSameDigits(self, s: str) -> bool:
        l=[int(i) for i in s]
        while len(l)>2:
            l = [(l[i] + l[i + 1]) % 10 for i in range(len(l) - 1)]

        return l[0]==l[1]
            