# Welcome To My Learning Note

### Set(集合)

Python 的 Sets 是一種無順序的元素集合，每個元素是唯一且不可重複的，可以進行更新，新增，刪除，也可進行數學上的交集，聯集，差集上的運算

Python 的集合是用{}刮起來，每個元素是用逗號進行區隔

### 走訪集合

集合沒有順序，沒有辦法建立順序進行走訪

### 集合的運算

```python=
a = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}

a&b # 交集:{4,5,6} # 亦可用intersection的方法

a|b # 聯集:{1,2,3,4,5,6,7,8,9} # 亦可用union的方法

a-b # 差集:{1,2,3} # 亦可用 difference()的方法

a^b # 對稱差集:{1,2,3,7,8,9} # 亦可用symmetric_difference()的方法

```

## 其他符號
|python 符號|意思|
|:-:|:-|
|---|差集|
|&|交集|
|I|聯集|
|!=|不等於|
|==|等於|
|in|屬於|
|not in|不屬於|

 資料來源:
 
[Python網路資料爬蟲與資料視覺化應用實務(作者:陳允傑，出版社:旗標出版社)](https://www.books.com.tw/products/0010809154)

[Leetcode 題目練習，我的解答](https://github.com/DarrenLUCreate/Darren-s-github.memo/blob/master/LeetCode/Set_Mismatch.py)
