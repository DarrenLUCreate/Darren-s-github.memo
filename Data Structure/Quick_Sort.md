# Quick Sort

Definition: 快速排序法的觀念是先找到一個中間值，把小於中間值得點放左邊，把大於中間值得點放在右邊，再重複將左右兩邊的list做同樣的動作，直到完成為止

![](https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwibpKC5z_bmAhUdxYsBHbAjCvcQjRx6BAgBEAQ&url=https%3A%2F%2Fwww.techiedelight.com%2Fquicksort%2F&psig=AOvVaw09aThh6yBRWEjvkunEKJ4Y&ust=1578662818764891)

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
