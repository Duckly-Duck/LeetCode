class Solution:
    def reverse(self, x: int) -> int:
        # a=list(str(x))
        # if not a[0].isdigit():
        #     s=a[0]

        # a=a[:0:-1].join("")

        # return 


        x=str(x)
        if x.startswith("-"):
            return -int(x[:0:-1]) if -int(x[:0:-1])>(-2**31) else 0
        return int(x[::-1]) if int(x[::-1])<(2**31-1) else 0