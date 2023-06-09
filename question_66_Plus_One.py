class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str1 = ""
        for i in digits:
            str1 += f"{i}"
        
        summ = str(int(str1) + 1)
        return [int(n) for n in summ]