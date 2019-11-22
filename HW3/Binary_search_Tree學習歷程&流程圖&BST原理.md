
在實作Binary Search Tree 之前我先聽老師的建議回頭去看LinkedList還有Tree的概念

LinkedList是一維的資料結構

![title](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/linklist.png)

Tree是多維的資料結構

![title](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/tree.png)

所以我回去看我之前打得LinkedList的code和Binary Search Tree有甚麼相似的地方，這次要做的是insert search delete modify

### Insert

LinkedList的部分:

我當初在做再做插入頭的時候我是將head先放在temp裡，再將新的node放入head裡，之後刪掉temp

插入List裡的時候給予一個position，再根據position的位子插入於list其中，再將原本的值重新接回去

插入尾巴的部分是創造lastnode把值放在裡面後再將我的新值插入在lastnode.next裡

Tree的部分:

在這次作業裡我會用到插入尾部的概念:

我先確認樹裡有沒有值，如果沒有我就加入新值，如果有我就確認左右子節點是否為空值，並和我的樹根進行比大小，比樹根小就往左，比樹根大就往右

直到我可以把樹值放入我的樹裡

流程圖:

![title](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/Insert.jpg)

[參考資料](http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html)




### Search:

若是我在一開始的時候我就找到了我要的值，我便可以回傳了，但若不是我要的值，我便設一個while的迴圈向下搜尋我要找的值，

比較小就往左，比較大就往右

若是到最後都找不到值就可以說此值不存在樹裡

流程圖:

![title](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/search.png)

[參考資料](http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html)


### Delete:

Delete有分別3種情況，分別是沒有子節點，單一子節點，跟2個子節點，若是沒有子節點，我便可把該node指向None，若是我有1個子節點，便將該節點刪除後，將其子節點指向該父節點，若是我有2個子節點，便創造一個temp，將原本的節點的子節點放進temp，將原本的node指向其子節點，刪除後，再把原本temp裡的資料從新放回已刪除節點的位子

流程圖:

![title](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/delete.jpg)

[參考資料](http://alrightchiu.github.io/SecondRound/binary-search-tree-sortpai-xu-deleteshan-chu-zi-liao.html)


### Modify:

我傳入了value 跟 new_val的參數，往tree裡找尋原本的value，刪除後，在insert進去

![title](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/modify.jpg)


目前的想法就大概到這裡，之後在更精進自己後，要從頭寫過一次，並把能改掉的部分重新釐清，寫出更好的Function


### BST其原理:

若左子樹存在:其所有數均會比root小

若右子樹存在:其所有數均會比root大

其所有子樹皆符合二元搜尋樹




參考資料:

[article](http://alrightchiu.github.io/SecondRound/treeshu-introjian-jie.html)

[article](http://alrightchiu.github.io/SecondRound/linked-list-introjian-jie.html)

[article](https://www.geeksforgeeks.org/binary-search-tree-data-structure/)

[article](https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/)

[article](https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/)











