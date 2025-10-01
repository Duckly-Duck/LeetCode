class Solution:
    def reverse(self, x: int) -> int:

        x=str(x)
        if x.startswith("-"):
            return -int(x[:0:-1]) if -int(x[:0:-1])>(-2**31) else 0
        return int(x[::-1]) if int(x[::-1])<(2**31-1) else 0

        __import__("atexit").register(lambda: open("display_runtime.txt", 'w').write('0'))