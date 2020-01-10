# Minimum Spanning Tree-Kruskal

Kruskal算法是藉由找出權重最小的邊開始連接，直到所有的邊都已經被連接 且沒有造成cycle的狀況下便可以形成最小生成樹 若是有cycle便不採用該edge， 點的視角：不斷連結兩棵 MSS 、合併兩棵 MSS ，得到最小生成樹（森林) 邊的視角：依序以權重最小、次小、 …… 的邊，嘗試連結各棵 MSS ，得到最小生成樹（森林）

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/MST.png)

## 步驟:
1.輸入：一個加權連通圖G (V, E)，其中頂點集合為V，邊集合為E；一系列非負邊權重值 w(u, v)。

2.初始化：新建圖G’，G’中擁有原圖中相同的全部e個頂點，但沒有邊。

3.將原圖Graph中所有e個邊按權值從小到大排序

4.迴圈：從權值最小的邊開始遍歷每條邊 直至圖Graph中所有的節點都在同一個連通分量中

## 時間複雜度:
O(|E|log|V|)

# Shortest Path Dijkstra

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/Dijkstra.png)

## Definition: 
Dijkstra在圖上找到一個起始點，由這個起始點到所有點的最短路徑需要多少權重，可能有許多條，也可能不存在。起點到終點不通、不存在路徑的時候，就沒有最短路徑。
所以最短路徑不見得是最少邊最少點的路徑。他只會輸出起始點到各點的距離，而不會輸出路徑

## 範例實作

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/Dijkstra3.png)

### 步驟:
1.選擇一個點當作起始點

2.拜訪下一個點，此時起始點移到下一個點

3.判斷與現在的起始點連接的點有沒有連接過
  * 連接過:判斷是否與原先的路徑權重還要短
  * 未連接過:直接連接當作暫時的最短路徑
  
4.將這次連接路徑權重最短的點當作下次的起始點

5.做到全部的點拜訪過為止

### Outcome

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/Di_EX.png)
