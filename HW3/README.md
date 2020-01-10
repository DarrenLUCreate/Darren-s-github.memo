# Binary Search Tree

## Definition
1.若左子樹存在:其所有數均會比root小

2.若右子樹存在:其所有數均會比root大

3.其所有子樹皆符合二元搜尋樹

![title](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/tree.png)

##步驟
1.依據原始資料輸入順序來建立

2.第一個輸入的資料當作樹根

3.接下來輸入的數從樹根的節點資料開始比較

4.如果比樹根大放入右子樹，沒有右子樹，把新的資料當作右子樹

5.如果比樹根小放入左子樹，沒有左子樹，把新的資料當作左子樹

6.遞迴執行前二步驟直到位子確定為止

7.重複前四個步驟直到資料輸入完畢

## 具備的功能

### 新增:
我先確認樹裡有沒有值，如果沒有我就加入新值，如果有我就確認左右子節點是否為空值，並和我的樹根進行比大小，比樹根小就往左，比樹根大就往右

直到我可以把數值放入我的樹裡

### 搜尋:
若是在一開始就搜尋到我想要的數值時，便可以回傳了，但若不是，邊依照Binary Search Tree的規則搜尋下去

### 刪除:
Delete有分別3種情況，分別是沒有子節點，單一子節點，跟2個子節點，若是沒有子節點，我便可把該node指向None，若是我有1個子節點，便將該節點刪除後，將其子節點指向該父節點，若是我有2個子節點，便創造一個temp，將原本的節點的子節點放進temp，將原本的node指向其子節點，刪除後，再把原本temp裡的資料從新放回已刪除節點的位子

### 修改:
基本上就是先搜尋，在將固有值刪除，再插入新增的值

參考資料:

[article](http://alrightchiu.github.io/SecondRound/treeshu-introjian-jie.html)

[article](http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html)

[article](https://www.geeksforgeeks.org/binary-search-tree-data-structure/)

[article](https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/)

[article](https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/)
