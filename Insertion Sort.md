# 我的學習筆記

# Welcome To My Learning Note

## Insertion Sort & Sorting

### Insertion Sort (插入排序法)

將數字分為已排序何謂排序的兩堆數字，從未排序的從未排序的數值插入到已排序的數字裡

插入時由右而左進行比較，直到遇到一個比自己小的值，自己放在右邊，遇到比自己大的，自己放左邊

Insertion Sort: 

![alt text](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/Insertion%20Sort.png)

參考資料:
* article: [Insertion Sort](https://www.google.com/url?sa=i&source=images&cd=&ved=2ahUKEwio-JLG_oPlAhVzNKYKHawsDX4QjRx6BAgBEAQ&url=https%3A%2F%2Femn178.pixnet.net%2Fblog%2Fpost%2F93791164&psig=AOvVaw1hjrzhngFW1CYybiMuD_wG&ust=1570326048101156)

## Time Complexity & Space Complexity

時間複雜度是指完全的執行程式所需要的計算機時間
* O(1):陣列讀取
* O(n):簡易讀取
* O(logn):二分搜尋
* O(nlogn):合併排序
* O(n平方):選擇排序
* O(2^n):費波納契數列

空間複雜度是指評估演算法內佔用內存大小

a = "python" 空間複雜度為1

a = [1,2,3,4,5] 空間複雜度為5

a = [[[1,2],[1,2]],[[1,2],[1,2]],[[1,2],[1,2]]] 空間複雜度為3乘以2乘以2

Time Complexity:

![alt text](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/time%20complexity.png)

參考資料:

[Time Complexity](https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E5%BE%9E%E6%99%82%E9%96%93%E8%A4%87%E9%9B%9C%E5%BA%A6%E8%AA%8D%E8%AD%98%E5%B8%B8%E8%A6%8B%E6%BC%94%E7%AE%97%E6%B3%95-%E4%B8%80-b46fece65ba5)

[Time Complexity & Space Complexity](https://www.twblogs.net/a/5b87fdd32b71775d1cd9eb70)

[Time Complexity's pic & text](https://dev.to/victoria/a-coffee-break-introduction-to-time-complexity-of-algorithms-160m)
