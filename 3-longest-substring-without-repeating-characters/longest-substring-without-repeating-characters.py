class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # close enough but not correct

        # a=set()
        # l=[]
        # for i in s:   
        #     if i not in a:
        #         a.add(i)
        #     else:
        #         l.append(len(a))
        #         a.clear()
        #         a.add(i)
     
        # l.append(len(a))
        # return max(l) 


        # SLIDING WINDOW TYPE

        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len