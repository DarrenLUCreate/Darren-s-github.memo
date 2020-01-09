# Merge Sort 

## Definition:

合併排序法適用於內部排序和外部排序，也是一種典型的分而治之的方法，將N筆資料依照鍵值順序排序的方法

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/Merge_sort.png)

## 步驟:
1.將一個list重複劃分成好幾個小list直到每個小list裡面都只剩下一個元素

2.將相鄰的兩個小list互相比較，並取較小值則為以排序值，以排序值可以用新list 存或是用 index 的方式將其隔開。

3.直到所有小list合成一個完整的list

## 分而治之(Divide & Conquer)
Divide :把數列「對半拆解」成兩個小數列，依此類推，直到每個數列剩下一個元素。

Conquer:按照「由小到大」的順序，「合併」小數列，依此類推比較大小後，合併成數列

## 參考資料:
[ChiuCC](https://alrightchiu.github.io/SecondRound/comparison-sort-merge-sorthe-bing-pai-xu-fa.html)

[初學者學演算法｜排序法進階：合併排序法](https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E6%8E%92%E5%BA%8F%E6%B3%95%E9%80%B2%E9%9A%8E-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95-6252651c6f7e)
