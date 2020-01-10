# Binary Tree
## Definition:
Tree廣義上來說對於node的child沒有數量上的限制，但對於如果有限制2個child便是Binary Tree，兩個pointer稱為left_child和right_child

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/BT.png)

## 特性:
1.
|二元樹|樹|
|:-:|:-|
|二元樹可以為空集合|樹不可為空集合|
|分支度0<=degree<=2|分支度degree>=0|
|左右子樹有次序之分|左右子樹沒有次序之分|

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/BT2.png)

2.假設二元樹有i個階度，最多的節點數目計算方法為2**i-1 , i>=1

3.假設高度為h的二元樹中計算最多節點的方法為(2**h)-1 , h>=1

4.總節點數為總邊數+1

## 搜尋方法:
主要分為3種前序追蹤，中序追蹤，後序追蹤

1.前序追蹤:Pre-order

先拜訪樹根，在拜訪左子樹，最後才拜訪右子樹，又稱為深度優先追蹤

2.中序追蹤:In-order

先拜訪左子樹，在拜訪樹根，最後拜訪右子樹

3.後序追蹤:Post-order

先拜訪左子樹，在拜訪右子樹，最後才拜訪樹根

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/BT.jpg)

Pre-Order:1,2,4,7,8,5,3,6,9,10

In-Order:7,4,8,2,5,1,3,9,6,10

Post-Order:7,8,4,5,2,9,10,6,3,1

## 參考資料:
[ChiuCC](http://alrightchiu.github.io/SecondRound/binary-tree-introjian-jie.html)

[ChiuCC](http://alrightchiu.github.io/SecondRound/binary-tree-traversalxun-fang.html)

[GeeksforGeeks](https://www.geeksforgeeks.org/binary-tree-data-structure/)

[二元樹走訪](https://ithelp.ithome.com.tw/articles/10205571)
