# Hash Table

## Definition:
雜湊透過Key : Value的方式找尋內部資料的資料結構，透過傳入key值經由hash function找到之後並回傳，

途中可能會發生碰撞，導致儲存的資料在同一個存放的位子，需要透過chaining解決碰撞的問題。

![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/HASH.png)

Key: 通常為使用端輸入的東西，例如字串之類的

Hash Function:透過轉換的算式，將輸入的key轉換成對應的index

Bucket:存放資料的地方

## What is Hash Function?

雜湊函式Hash Function是一種將輸入值映射到另一個值域的技術，Hash Function的底層有非常複雜的數學式，式子中蘊含了一些magic number，有興趣鑽研的可以再去尋找一些論文來研讀，這邊就不多作介紹，因此在這邊可以直接想像Hash Function就是一台轉換器，丟輸入進去就會產生一個輸出，而這種轉換有一個很重要的特性就是「單向」，也就是one-way function，輸入可以經由轉換得到輸出，但輸出卻不可得到輸入，具有不可逆的特性。

## What is Hash Table?

雜湊表Hash Table是一種儲存（Key,Value）的資料結構，通常一個Key就是對應一個Value，Value就是要儲存的資料，Key則可以想像成這筆資料的標籤，想要找到這筆資料就需要有這筆資料的Key去搜尋，比如有一些資料是許多車主的姓名和車子的廠牌：

##參考資料:
[Hash是甚麼](https://blockbar.io/blockchain/hash%E6%98%AF%E4%BB%80%E9%BA%BC-what-is-hash/)

[GeeksforGeeks](https://www.geeksforgeeks.org/hashing-data-structure/)

[IT邦幫忙](https://ithelp.ithome.com.tw/articles/10208884)

[Hash](http://www.tsnien.idv.tw/Security_WebBook/%E7%AC%AC%E5%9B%9B%E7%AB%A0%20%E9%9B%9C%E6%B9%8A%E8%88%87%E4%BA%82%E6%95%B8%E6%BC%94%E7%AE%97%E6%B3%95.html)
