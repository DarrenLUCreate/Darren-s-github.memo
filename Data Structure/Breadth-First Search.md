# Breadth-First Search
## Definition:
從圖形中的某一頂點開始拜訪，被拜訪過的頂點會被標記為已拜訪，在拜訪該點的鄰點中任一尚未拜訪過的點，並在已該點作為新的起點繼續下一次拜訪 並以QUEUE以及Recursive，當拜訪的點的相鄰所有點都已經拜訪完了，
便會返回搜尋尚未拜訪的點，直到所有點都拜訪完，為廣度優先搜尋法

## 步驟:
1.準備一個儲存列Queue

2.Enqueue頂點V到Queue裡面

3.如果Queue不為空，執行下列步驟，否則進行下一步
  * 從Queue裡面dequeue頂點W
  *並標示頂點W為已拜訪過
  *將所有與頂點W相鄰的點Enqueue到Queue裡面
  
4.回到步驟3，直到所有點都拜訪完畢

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/BFS1.png)

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/BFS2.png)

## 參考資料

[ChiuCC](https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html)

[參考資料](http://simonsays-tw.com/web/DFS-BFS/BreadthFirstSearch.html)

[GeeksForGeeks](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)
