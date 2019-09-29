# 我的學習筆記
## Welcome To My learning Note 
這裡記錄我的資料科學以及演算法的生活筆記

### STACK & QUEUE
STACK的概念有點像堆疊書本最先放上去的是最後才被取出，最後放上去的是最先被取出，任何遞迴都可以用Stack進行改寫

First In Last Out & Last In First Out

假如說今天有個DataSet是ABC，我放入的順序是ABC，我取出來的時候是CBA

Stack:![alt text](https://github.com/DarrenLUCreate/DarreNC/blob/master/Stack.png)

Stack所必須要具備的5項功能:
* Push : 把資料丟進去的動作，第一個是head，最後一個是Tail
* Pop : 把最上面的，也就是從尾巴開始將資料移除
* Top : 查看並確認Tail的資料是哪個資料
* IsEmpty : 確認Stack中是否有資料
* getSize : 回傳Stack中有多少的資料

Queue有點像是排隊買雞排，先買到的時候就可以很囂張地跟後面的人說"嗯~真香~"，網站伺服器，CPU都有用到Queue

First In First Out & Last In Last Out

假如今天我有一個DataSet是ABC，我放入的順序是ABC，我取出來的順序也是ABC

Queue必備的功能:
* Push : 從資料的Tail放入新的資料 ，也就是新的人來買雞排
* Pop : 將Front所指向的資料移除，從Queue裡刪除資料為dequeue，也就是拿到雞排後走掉的人
* getFront : 回傳Front所指向的資料，
* getBack : 回傳Back所指向的資料
* IsEmpty : 回傳Queue裡是否有資料
* getSize : 確認Queue裡的資料個數

Queue:![alt text](https://github.com/DarrenLUCreate/DarreNC/blob/master/geek-queue-1.png)

相關資料:

Python Stack&Queue[![Video]](https://youtu.be/In-1i27Fp0w)







