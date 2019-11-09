class Solution(object):
    def Heapify(array,i):   
        Largest=i
        left=2*i+1
        right=2*i+2
        
        if left<len(array) and array[left]>array[i]: #二元樹裡左邊的節點大於父節點，最大值指向左邊節點的值
            Largest=left
            
        if right<len(array) and array[right]>array[i]:#同理，二元樹中右邊的節點若大於父節點的話，最大值指向右邊節點的值
            Largest=right
            
        if Largest!=i:
            array[i],array[Largest]=array[Largest],array[i] # 若是比到最後父節點不是最大值，繼續向下尋找最大值
            Heapify(array,Largest)
    def heapsort(arr):
        result=[]
        Max_len=len(arr)//2-1 # i 的最大值為整個list的長度減去1
        
        while len(arr)>0:
            for i in range(Max_len,-1,-1): #for迴圈(i的起始值最大，往前走訪，到i=0)
                Heapify(arr,i)
            sol.append(arr.pop(0)) #把比出來的最大值pop出來加到result裡
        real = result[::-1] #反轉整個list
                     
        return real
