# Minimum Spanning Tree-Kruskal

## Definition:
Kruskal演算法是一種用來尋找最小生成樹的演算法，由Joseph Kruskal在1956年發表。用來解決同樣問題的還有前面Prim演算法和Boruvka演算法等。和Boruvka演算法不同的地方是，Kruskal演算法在圖中存在相同權值的邊時也有效。

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/MST.png)

## 步驟:
1.輸入：一個加權連通圖G (V, E)，其中頂點集合為V，邊集合為E；一系列非負邊權重值 w(u, v)。

2.初始化：新建圖G’，G’中擁有原圖中相同的全部e個頂點，但沒有邊。

3.將原圖Graph中所有e個邊按權值從小到大排序

4.迴圈：從權值最小的邊開始遍歷每條邊 直至圖Graph中所有的節點都在同一個連通分量中

## 時間複雜度:
O(|E|log|V|)

## 參考資料:
[MST](https://www.itread01.com/content/1550409678.html)

[ChiuCC](http://alrightchiu.github.io/SecondRound/minimum-spanning-treekruskals-algorithm.html)

[MST](http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/kruskal.html)
