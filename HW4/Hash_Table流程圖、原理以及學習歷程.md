### 流程圖 & Hash Function說明

![titile](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/Add.jpg)

將key進行MD5轉換後取出的餘數，將他們存到相對應的地方，但若是有大於等於2個的相同值的話，會發生碰撞，為了避免發生這樣的情況

使用Chaining去將每個node連接起來，使得每個地方都只有一筆資料，以方便在尋找的時候，發現找錯資料的錯誤

![title](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/Remove.jpg)

我用了之前寫Linked List的想法，設立一個Current將想要刪除的node放進current裡面，再把node.next接上去

再把current刪除，不等於時再將node = node.next執行下一次，最後回傳

![title](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/contain.jpg)

Contain的部分是將node.val = self.hashf(key)方式確認是否為同測值，回傳True，之後再將下一個node.next繼續執行相同的步驟，直到全部測完為止


### Hash Table 原理

雜湊透過Key : Value的方式找尋內部資料的資料結構，透過傳入key值經由hash function找到之後並回傳，

途中可能會發生碰撞，導致儲存的資料在同一個存放的位子，需要透過chaining解決碰撞的問題。

### Hash Table 學習歷程

在開始寫hash table之前我根據了老師的解說影片跟PPT先了解了一下原理，了解一下可以應用在日常生活的哪些地方，例如會員登入，認證身分時會用到解碼學的原理，以及Hahs Table去儲存查找資料，應用的層面很廣，在寫之前也有去回顧老師之前的上課內容，在class10那裏的解說，告訴我們寫程式犯錯誤是很正常的，需要一步一步慢慢地修改以及求證，改正我之前一次就寫太多的習慣，先自己寫過一次，add的部分有使用老師的邏輯，remove的部分是用之前寫linked lsit的寫法想的。

### 參考資料:

[Hash Table Intro](http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html)

[老師PPT](https://docs.google.com/presentation/d/e/2PACX-1vT1HO9Nl475k2bR0l1x8_Tr4V5Wzx0BEqp9bpmHckvj8kTeJehhYVlOJUDVPhLQm6kjGCJ_sLMSBUw5/pub?start=false&loop=false&delayms=3000&slide=id.p)

[老師的影片RBT](https://www.youtube.com/watch?v=qR35AEc84AI&feature=youtu.be)

[老師的影片Hash Table](https://www.youtube.com/watch?v=7C5f2ttq79Y&feature=youtu.be)


