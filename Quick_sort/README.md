# Quick Sort

快速排序法的觀念是先找到一個中間值，把小於中間值得點放左邊，把大於中間值得點放在右邊，再重複將左右兩邊的list做同樣的動作，直到完成為止

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/Quicksort.png)

## 取中間值的方法:
 * 總是把第一個值當作中間點
 * 總是把最後一個點當作中間點
 * 隨機取點
 * 以中位數當作基準點
 
## 時間&空間複雜度:
  * Worst case: [ Big-O ]: O(n2)
  * Average Case: [Big-omega]: O(n*log n)
  * Best Case: [Big-theta]: O(n*log n)
  * Space Complexity : O(n*log n)
## 參考網站:
[ChiuCC](http://alrightchiu.github.io/SecondRound/comparison-sort-quick-sortkuai-su-pai-xu-fa.html)

[小殘程式光廊](https://emn178.pixnet.net/blog/post/88613503-%E5%BF%AB%E9%80%9F%E6%8E%92%E5%BA%8F%E6%B3%95(quick-sort))
