num = [1,2,2,4]

class solution:
    def finderror(self,num):
        n = len(num) 
        nset = set(num) # set裡的元素不可重複
        missing = n * (n+1)/2-sum(nset) # 利用長度減去set中的總值
        dup = sum(num)-sum(nset) #全部的值減去set裡面的值
        return[missing,dup]
