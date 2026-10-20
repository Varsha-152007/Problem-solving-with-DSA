# Problem: Additive Number
# Problem Link: https://leetcode.com/problems/additive-number/description/?envType=problem-list-v2&envId=string
# Date: 20th Oct 2026
# Time taken to solve: 1hr 15mins

#solution
<
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            for j in range(i + 1, n):
                a, b = num[:i], num[i:j]

                if (len(a) > 1 and a[0] == '0') or \
                   (len(b) > 1 and b[0] == '0'):
                    continue

                rest = num[j:]

                while rest:
                    c = str(int(a) + int(b))

                    if not rest.startswith(c):
                        break

                    rest = rest[len(c):]
                    a, b = b, c

                if not rest:
                    return True

        return False
>
