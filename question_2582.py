    def passThePillow(self, n: int, time: int) -> int:
        count = 1;
        flag = True;
        for i in range(time):
            if flag :
                count += 1
            else: 
                count -= 1     
            if count==1 or count==n:
                flag = not flag
        return count
