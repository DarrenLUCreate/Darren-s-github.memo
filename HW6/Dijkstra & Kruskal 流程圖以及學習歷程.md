## 流程圖圖解 & 學習歷程

Dijkstra_Shortest_path

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/SP.jpg)

關於這次的作業的部分，我覺得跟之前的Heap_Sort作業很像，比較不直觀，用圖解釋看起來理論很容易，但卻沒有想像中的簡單
首先第一個部分卡關的地方是觀念的釐清，Shortest_path的觀念是找出2個點的最短路徑，第二個卡關的地方是在餵入一個matrix時要怎麼讀取
一直在某個地方一直糾結不清，之前有嘗試過使用enumerate函數去使matrix可以有index可以去相互應對，只能說這個演算法還是需要之後繼續好好研究一下!

Minimum Spanning Tree

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/MST.jpg)

Kruskal演算法有跟同學討論一下，先去畫圖使自己理解背後的原意，再慢慢自己手工畫出整個的流程，第一步去sort出我餵進去的edge的權重，由小到大開始
第二步是選擇最小的邊，並增加下一次迭代的index，如果沒有造成cycle的話便繼續下去，直到我所有的點都已經被拜訪完。完成Kruskal演算法

## Dijkstra & Kruskal演算法原理

### Dijkstra原理:

Dijkstra使用了廣度優先搜尋，由一個點進行搜尋，找出對於其他點的最短路徑
第一次紀錄的時候，就會將相鄰的點紀錄，不能到達的點視為無限大
直到所有的點跟頂點的路徑為各自的最短路徑時，便可以求出最短路徑

### Kruskal原理:

Kruskal算法是藉由找出權重最小的邊開始連接，直到所有的邊都已經被連接
且沒有造成cycle的狀況下便可以形成最小生成樹
若是有cycle便不採用該edge，
點的視角：不斷連結兩棵 MSS 、合併兩棵 MSS ，得到最小生成樹（森林)
邊的視角：依序以權重最小、次小、 …… 的邊，嘗試連結各棵 MSS ，得到最小生成樹（森林）。

### 參考資料

[article](http://www.csie.ntnu.edu.tw/~u91029/SpanningTree.html)
[article](https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/)
[article](http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/kruskal.html)
[article](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)
