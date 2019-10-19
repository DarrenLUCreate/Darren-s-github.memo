# Heap Sort (堆積排序法)

### Heap Data Structure

Heap Sort主要以Binary Array的方式實現，增加節點時必須以最左邊的地方加入

Python的index從0開始由上而下由左至右的話，並以i來代表節點的位子
* 父節點:(i-1)/2
* 左子節點:(2* i)+1
* 右子節點:(2* i)+2

若以index[i]為二元樹裡的root的話，分為兩種二元樹
* if value[i] < value[2i+1],value[2i+2]，這個二元樹為Min Heap
* if value[i] > value[2i+1],value[2i+2]，這個二元樹為Max Heap

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/heap_sort2.png)

### 時間複雜度

Heap Sort的時間複雜度，以n來代表資料
* Best Case : nlogn
* Average Case: nlogn
* Worst Case: nlogn

### 目前對於Heap Sort 程式碼的想法

我需要一個設定一個array來存放數值，以及n，i兩個變數，n為value，i為index

另外左右節點的變數設定為left=2i+1 , right=2i+2

我需要一個push函數將數值放進array，將第一個Node跟最後一個Node進行比較(Swap)，比較完的數就當他不存在了，交由pop函數將他append到新的list中放著

重複進行每個節點跟第一個節點進行比較，完成排序。

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/Heap.png)






