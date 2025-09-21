class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        l=list(str(num))

        for i,j in enumerate(l):
            if j=='6':
                l[i]='9'
                break
        return int(''.join(l))