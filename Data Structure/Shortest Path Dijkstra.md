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
