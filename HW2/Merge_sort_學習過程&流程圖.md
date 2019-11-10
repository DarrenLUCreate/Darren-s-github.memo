Merge_sort在這次作業中花了我比較少的時間，但還是經歷了許多的錯誤

我是看這位大神的文章學習的:https://medium.com/appworks-school/%E5%88%9D%E5%AD%B8%E8%80%85%E5%AD%B8%E6%BC%94%E7%AE%97%E6%B3%95-%E6%8E%92%E5%BA%8F%E6%B3%95%E9%80%B2%E9%9A%8E-%E5%90%88%E4%BD%B5%E6%8E%92%E5%BA%8F%E6%B3%95-6252651c6f7e

起初我打算用以下的方式:

     class Merge_sort:
        def merge_sort(arr):
            arr = []
            if len(arr)>1:
                mid = len(arr)//2
                left = arr[:mid]
                right = arr[mid:]
            else:
                return arr
        def division(right_index,left_index,all_index):

            right_index = 0
            left_index = 0
            all_index = 0

           while right_index < right and left_index < left:
                if left[left_index] <= right[right_index]:
                    arr[all_index] = left[left_index]
                    left_index+=1
                else:
                    right[right_index] = arr[all_index]
                    right_index+=1
                    all_index = all_index+1

            while right_index < len(right):
                arr[all_index] = right[right_index]
                all_index = all_index+1
                right_index = right_index+1

            while left_index < len(left):
                arr[all_index] = left[left_index]
                all_index = all_index+1
                left_index = left_index+1
   但我發現我把分割跟合併做得有點複雜了，跑出來的結果不是很理想，
   
   看了很多的解說影片才明白，Merge_sort是將一個list分割成一個一個的list並進行迭代的比較慢慢組成後，才去進行最後的合併，
   
   起初認為分成左右兩個大list後就可以進行合併比較，後來才發現會有很多mistake，
   
   即是不能確定同一個list裡的值是否已經比較完了，發現了錯誤後，有了之後的寫法
   
   寫法的參考影片: https://www.youtube.com/watch?v=iR1CXiC7OQc
   
   ### 流程圖:
   
   ![](https://github.com/DarrenLUCreate/DarreNC/blob/master/Img/Merge%20sort.jpg)
