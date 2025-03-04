class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def get_digit_sum(n):
            tmp = 0
            while n:
                tmp = tmp * 10 + n % 10
                n //= 10
            return tmp
        
        while n:
            sum_digits = get_digit_sum(n)
            if sum_digits % 3 == 2:
                return False
            elif sum_digits % 3 == 1:
                n = (n - 1) // 3
            else:
                n //= 3
            
        return True