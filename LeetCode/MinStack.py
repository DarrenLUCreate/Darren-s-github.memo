class MinStack:
    def __init__(self):
        self.data = [] #儲存所有的data
        self.mindata = [] #儲存每一次存取的最小元素
        
    def push(self,x):
        self.data.append(x)
        if len(self.data) == 0 or self.mindata[-1]: #確認我們是否需要上傳最小值，決定要不要排隊買雞排
            self.mindata.append(x) #回傳值，排隊買雞排
    
    def pop(self):
        if len(self.data) == 0: #如果self的長度是0，代表裡面沒有值，也就是沒有人買雞排
            return None
        else:
            if self.data[-1] == self.mindata[-1]: self.mindata.pop()
            return self.mindata.pop()
            
    def top(self):
        if len(self.data) == 0: return None
        else:                   return self.data[-1] #回傳最上面的值
        
    def getSize(self):
        if len(self.data) == 0: return None
        else:                   return len(self.data) #回傳stack中的資料長度
        
    def getMin(self):
        if len(self,data) == 0: return None
        else:                   return self.mindata[-1] # 回傳最小值
    
    
            
         
