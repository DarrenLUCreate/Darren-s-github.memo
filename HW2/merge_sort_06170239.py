class Solution(object):
    def merge(self,array):
    
        if len(array)>1:
            mid=len(array)//2 #設定切分點為list的中間
            left=self.merge(array[:mid])#左邊的list是從頭到中間
            right=self.merge(array[mid:])#右邊的list是從中間到最後
        else:
            return array #當list長度小於1時回傳list
        
        left_idx=0 #設定左邊INDEX初始值為0
        right_idx=0#測定右邊INDEX初始值為0
        result=[] #新的存放數值的list
    
        while left_idx<len(left) and right_idx<len(right):#當左右的INDEX都小於該對應的list長度後
            if left[left_idx]<right[right_idx]: #比較兩邊的大小
                result.append(left[left_idx]) #比較小的放入result裡
                left_idx+=1 #左邊的INDEX往後推進1
            else:
                result.append(right[right_idx])
                right_idx+=1
            
        while left_idx<len(left): #當只有左邊有剩下的值時，將剩餘的數值加入
            result.append(left[left_idx])
            left_idx+=1
        
        while right_idx<len(right):
            result.append(right[right_idx])
            right_idx+=1
        
        return result #回傳result
'''
arr=[-6,2,7,8,0,0]
rarr=[-6,0,0,2,7,8]
'''

