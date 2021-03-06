# 我的學習筆記

## Welcome To My Learning Note

### LinkedList 

LinkedList是由一連串的節點(Node)所組成的，每個節點指向下一個節點，最後一個節點指向None

每個節點就像是一種分離式收納箱的概念，應該都需要有兩種屬性值，分別是本身帶有資料的格子，另一個是指向下一個節點的Pointer

LinkedList:![alt text](https://github.com/DarrenLUCreate/DarreNC/blob/master/LinkList.png)

上面圖解的作者網址:https://medium.com/@tobby168/%E7%94%A8python%E5%AF%A6%E4%BD%9Clinked-list-524441133d4d

    class LinkList:

      def __init__(self,data):
  
        self.data = data
    
        self.next = None
    
        return
    
### 為甚麼要有LinkedList?

LinkedList & Array 

在儲存方面

* LinkedList不用連續區間的記憶體就可以存取資料
* Array則需要一連串的區間去存取資料

LinkedList的優缺點:

* 存取方面比較可以動態存取，只需要改變Pointer即可加入或刪除，且共用容易
* 缺點是需要額外的空間去儲存pointer，執行速度比array慢，因為要從頭讀取，不能direct access

Memory Access:![alt text](https://github.com/DarrenLUCreate/DarreNC/blob/master/access.jpeg)

上面圖解的原作者:https://medium.com/basecs/whats-a-linked-list-anyway-part-1-d8b7e6508b9d



