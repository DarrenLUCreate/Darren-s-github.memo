## BFS流程圖

![title](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/BFS.png)

## DFS流程圖

![title](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/DFS.png)

## 學習歷程

這次Follow了老師的影片以及之前跟學長姐的經驗，告訴我程式這種東西真的沒有捷徑，只能一步一步去慢慢體會，只有經過好幾次溺水之後
才會懂得甚麼是邁進一步的感覺，這次先去理解它的原理，不先去打CODE，先去把原理看懂，然後蓋起來，試著自己寫一遍，然後再把自己寫的Pseudo Code看一次
然後再把自己寫的邏輯給別人看，因為當下看的時候，可能對自己的程式覺得很完整，但給別人看過之後，往往別人會看出我的邏輯本身的錯誤，
從這之中也可以看到別人的觀點以及邏輯的出發點，跟別人討論的過程很美好，也可以讓自己的邏輯更完整一點。

## BFS原理&DFS原理之比較

BFS:從圖形中的某一頂點開始拜訪，被拜訪過的頂點會被標記為已拜訪，在拜訪該點的鄰點中任一尚未拜訪過的點，並在已該點作為新的起點繼續下一次拜訪
並以QUEUE以及Recursive，當拜訪的點的相鄰所有點都已經拜訪完了，便會返回搜尋尚未拜訪的點，直到所有點都拜訪完，為廣度優先搜尋法

QUEUE:First in First Out

DFS:從圖形中的某一頂點開始拜訪，被拜訪過的頂點會被標記為已拜訪，在拜訪該點的鄰點中任一尚未拜訪過的點，並在已該點作為新的起點繼續下一次拜訪
並以STACK進行處理，堆疊內的元素的最頂端為最先拜訪的點，直到所有點都被拜訪完，為深度優先搜尋法

STACK:First in Last Out

## 參考資料:

[BFS](http://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html)

[BFS](http://simonsays-tw.com/web/DFS-BFS/BreadthFirstSearch.html)

[DFS](http://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html)

[BFS&DFS](https://kopu.chat/2017/09/22/%E5%AF%A6%E4%BD%9Cgraph%E8%88%87dfs%E3%80%81bfs%E8%B5%B0%E8%A8%AA/)

[Graph](http://www.csie.ntnu.edu.tw/~u91029/Graph.html)
