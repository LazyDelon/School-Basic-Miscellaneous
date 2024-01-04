
# iris
```
https://zh.wikipedia.org/wiki/%E9%B8%A2%E5%B0%BE%E5%B1%9E
https://en.wikipedia.org/wiki/Sepal#/media/File:Petal-sepal.jpg
```
```
https://gist.github.com/netj/8836201

按raw
```
```
Google colab

!wget
https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv
```
```
import csv

# 開啟 CSV 檔案
with open('iris.csv', newline='') as csvfile:

  # 讀取 CSV 檔案內容
  rows = csv.reader(csvfile)

  # 以迴圈輸出每一列
  for row in rows:
    print(row)
```
```
Python 讀取與寫入 CSV 檔案教學與範例
2018/03/22
https://blog.gtwang.org/programming/python-csv-file-reading-and-writing-tutorial/
```
