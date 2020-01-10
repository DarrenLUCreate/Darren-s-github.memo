# Red Black Tree

## Definition:
紅黑樹是一種二元樹的延伸，主要是要解決二元樹不平衡的問題，時間複雜度為O(nlogn)，剛剛講到了二元樹會不平衡的問題就在於，當新增的資料接近整理好的資料時，
他會退化成為linkedlist就是去他原本樹的優勢，時間複雜度變為O(n)，所以需鬥過紅黑樹去進行平衡。

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/RB.png)

## 特性:
1.RBT中的每一個node不是黑色就是紅色。

2.Root 一定是黑色

3.如果某個node是紅色，那麼其兩個child必定是黑色，不能有兩個紅色node，相連若某個node為黑色，其child之顏色沒有限制

4.站在任何一個node上，所有從該node走到其任意descendant leaf的path上之黑色node數必定相同。

5.每一個leaf node一定是黑色。


## Rotation:

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/RB2.png)

修正的方法便是將node(35)塗成紅色，node(34)塗成黑色，並且對node(35)進行Right Rotation(向右旋轉)，如此一來，RBT便能維持其基本特徵。
值得注意的是，在執行Rotation時，有時會順便調整RBT的height(樹高)，使得RBT維持在平衡(balanced)的狀態。

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/RB4.png)

在正確新增node(31)後，若要刪除node(20)，因為node(20)是黑色，若將其刪除則違反RBT之第五點特徵：從root走向任何一個leaf node(NIL)的任何一條path上之黑色node數皆相同，因此同樣需要進行修正。

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/RB5.png)

修正的方法則是將node(30)塗黑，node(34)塗紅，然後對node(34)進行Left Rotation(向左旋轉)，如此一來，RBT便能維持其基本特徵。

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/RB6.png)

經過以上說明，應該能體會到Rotation在修正Insert(新增資料)與Delete(刪除資料)時的威力，接著便來實地走訪Rotation實際上是哪些pointer在指來指去。

## 參考資料:
[ChiuCC](http://alrightchiu.github.io/SecondRound/red-black-tree-introjian-jie.html)

[ChiuCC](http://alrightchiu.github.io/SecondRound/red-black-tree-rotationxuan-zhuan.html)

[紅黑樹插入和刪除原理](https://www.itread01.com/content/1549532189.html)

