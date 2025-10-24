class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        candidate = n + 1
        while True:
            digit_count = [0] * 10
            temp = candidate
            
            while temp > 0:
                digit = temp % 10
                digit_count[digit] += 1
                temp //= 10
            
            is_balanced = all(
                count == 0 or digit == count
                for digit, count in enumerate(digit_count)
            )
            
            if is_balanced:
                return candidate
            
            candidate += 1