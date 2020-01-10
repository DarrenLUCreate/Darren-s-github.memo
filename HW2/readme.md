# Heap Sort

Heap Sort主要以Binary Array的方式實現，增加節點時必須以最左邊的地方加入

Python的index從0開始由上而下由左至右的話，並以i來代表節點的位子
* 父節點:(i-1)/2
* 左子節點:(2* i)+1
* 右子節點:(2* i)+2

若以index[i]為二元樹裡的root的話，分為兩種二元樹
* if value[i] < value[2i+1],value[2i+2]，這個二元樹為Min Heap
* if value[i] > value[2i+1],value[2i+2]，這個二元樹為Max Heap

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/Heap-Property.png)

### 時間複雜度

Heap Sort的時間複雜度，以n來代表資料
* Best Case : nlogn
* Average Case: nlogn
* Worst Case: nlogn

# Merge Sort
合併排序法適用於內部排序和外部排序，也是一種典型的分而治之的方法，將N筆資料依照鍵值順序排序的方法

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/Merge_sort.png)

## 步驟:
1.將一個list重複劃分成好幾個小list直到每個小list裡面都只剩下一個元素

2.將相鄰的兩個小list互相比較，並取較小值則為以排序值，以排序值可以用新list 存或是用 index 的方式將其隔開。

3.直到所有小list合成一個完整的list
