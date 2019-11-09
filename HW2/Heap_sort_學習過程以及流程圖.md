學習的歷程: Heapsort我當初看了很久的影片，和一些網路上的大神的code模擬出來的

這是我一開始寫的code:

     def Heapsort(arr): 
       father = 0 
       left = 2father+1 
       right = 2father+2

       while father < len(arr):
           if arr[father] < arr[left]:
               arr[father],arr[left] = arr[left],arr[father]
               father+1
           elif arr[father] < arr[right]:
               arr[father],arr[right] = arr[right],arr[father]
               father+1
           else:
               father+=1
               continue
               
     Num = [12,30,56,68,10,7] Heapsort(Num) print(Num) [56, 7, 10, 68, 30, 12]

如上圖: 我發現到數值上的轉換有成功了，但是我的index卻沒有繼續走訪下去，持續只有heapsort一棵小的二元樹的期間很久，後來有去看到一些網路大神的code

大神code的url:https://www.geeksforgeeks.org/heap-sort/ 

heap的影片:https://www.youtube.com/watch?v=HqPJF2L5h9U 

發現我有漏做了一個地方就是沒有去尋找整個list裡的最大值

之後，寫完Heapify之後，又遇到了一個問題是要怎麼把它印出來的問題，我寫的一個while迴圈裡面包了一個for迴圈，再用python的語法append和pop印出來，但我發現我的sort出來的值是由大到小排列，若是我想要把她翻轉過來的話我可以用list取值方式的[::-1]來將整個迴圈反轉，於是出現了以上的結果

這次Heapsort的練習讓我思考很久，遠比寫MergeSort的時間還要長，首先我碰到的難點便是Heapify的步驟，我當初一直無法想像list是如何像一個二元樹一樣進行運作，後來有跟同學討論後，使用了index的互換寫成，光這個步驟就花了我許多時間，著實有挑戰性，讓我對演算法有近一步的認識
