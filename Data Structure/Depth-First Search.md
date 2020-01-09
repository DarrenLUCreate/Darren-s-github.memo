# Depth-First Search

## Definition:
從圖形中的某一頂點開始拜訪，被拜訪過的頂點會被標記為已拜訪，在拜訪該點的鄰點中任一尚未拜訪過的點，並在已該點作為新的起點繼續下一次拜訪
並以STACK進行處理，堆疊內的元素的最頂端為最先拜訪的點，直到所有點都被拜訪完，為深度優先搜尋法

DFS()本質上是一種「遞迴(recursion)結構」，而遞迴結構其實是利用了系統的「堆疊(stack)」

## 步驟:
1.先拜訪起始點V

2.接著再選擇與頂點V相鄰的且尚未拜訪的頂點拜訪，再以該點做深度搜尋

3.若有一頂點相鄰的點都被拜訪過的話，就退回最近曾經拜訪過的點繼續作深度搜尋

4.當所有點都已經被拜訪過的時候，結束深度搜尋

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/DFS1.png)

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/DFS2.png)

## 參考資料:
[ChiuCC](https://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html)

[參考資料](http://simonsays-tw.com/web/DFS-BFS/DepthFirstSearch.html)

[GeeksforGeeks](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/)
