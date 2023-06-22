class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1,n):
            back = n - i
            check1 = True
            check2 = True
            for j in str(back):
                if j == '0':
                    check1 = False
                    break
            for j in str(i):
                if j == '0':
                    check2 = False
                    break
            if check1 and check2:
                return [i,back]