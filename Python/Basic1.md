# Python Basic memo

### 運算子

i = 10

* " //= " :相除之後得到商數在指定給原變數

Ex: i//=5 => 2

* " **= " :指數運算後再給原變數

EX: i **=3 => 1000

### List

append():增加list裡的元素，但是從尾端加入

insert():在list中插入元素，語法是"listname.insert(index,element)"

remove():指定list中的一個元素刪除，語法是"listname.remove(element)"

pop(): 從list中取出元素並刪除，語法是"listname.pop([index])"

sort(): list由小排到大，語法是"listname.sort()"

reverse(): 反轉序列，語法是"listname.reverse()"

sorted(): 不改變原來list的內容，所進行的排序，語法是"listname = sorted(原本的串列,reverse=True or False)"

### dictionary

**字典名稱 = {key:value:,key:value:}**

### functions

常用的函數整理:
* abs(x) 取得x的絕對值
* chr(x) 取得整數x的字元
* float(x) 浮點數
* hex(x) 將x轉換成十六進位數字
* int(x) 將x換成整數
* len(x) 取得元素個數
* max(x) 最大值
* min(x) 最小值
* str(x) 將x轉換成字串
* sum(list) 計算元素總和
* join: 將串列中的元素組成一個字串，語法是"connection list.join(list)"
* split: 將一個字串已指定方式進行分割，語法是"list.split([split list])"
* find : 找尋字串在字串中的位置，語法是"字串.find(搜尋字串)"
* replace: 字串.replace(被取代的字串,取代的字串)
