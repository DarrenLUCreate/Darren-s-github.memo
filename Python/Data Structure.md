# DATA STRUCTURE BASIC!!

### What is class??

class就像是一個模組，用來生產具有相似特性的實體

會有**相同**的屬性以及**不同**參數
  
     class Cake:

       def __init__(self,name):
  
        self.name = name
        
     a = Cake("Brownie")

     print("a.name")
     
這樣我就建立了Cake這個類別，之後都可以用這個類別做事，以免重複函式的設定

def __init__這邊代表宣告時會自動執行的函式，也就是宣告類別的"起手式"，所以一般會拿來放基礎的屬性設定

所以我在創造Cake的時候都必須再給name這個參數才能成功地創造實體

class的自由度很高，不一定需要def__init__來宣告參數屬性

def__init__可以賦予空值，之後再新增資料就可以了，自由度非常高

[學習資料](https://medium.com/@weilihmen/%E9%97%9C%E6%96%BCpython%E7%9A%84%E9%A1%9E%E5%88%A5-class-%E5%9F%BA%E6%9C%AC%E7%AF%87-5468812c58f2)


