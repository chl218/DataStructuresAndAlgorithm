class Solution:
    def isHappy(self, n: int) -> bool:

        num_set = set()

        while n not in num_set:

            num_set.add(n)

            happy = 0
            while n:
                r = n % 10
                happy += r*r
                n = n // 10

            if happy == 1:
                return True
            n = happy

        return False