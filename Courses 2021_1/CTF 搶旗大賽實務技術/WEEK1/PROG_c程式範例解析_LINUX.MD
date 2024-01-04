#
```
王者歸來-LINUX C系統整合開發設計-第四版
吳岳
出版社：佳魁資訊  2016-04-20

書號：TB1604
ISBN：9789863793144

http://www.deepstone.com.tw/xmdoc/cont?xsmsid=0J191295271158913049&sid=0J338194422913126466&sq=LINUX%20C
```
```
https://github.com/capss22/IPAS-/tree/master/linux-C
```
# 第10 章 執行緒環境
```
See 10.2.7 動態記憶體管理
C 語言中只能透過malloc 和其衍生函數動態申請記憶體。
malloc 作為一個程式庫函數，其Linux 版本封裝了sbrk（）系統呼叫，
而該系統呼叫負責向作業系統申請記憶體。

malloc 函數分配的記憶體分配在Heap 中，其記憶體空間在未釋放之前均可以被參考，保證其生命期。
```
### malloc.c
```
#include <stdio.h>
#include <stdlib.h>

//動態分配的記憶體的生命期
//
void f1(int **p)
{
	*p = (int *)malloc(sizeof(int));
}

//
void f2(int *p)
{
	printf("the heap is %d\n", *p);
}

int main(void)
{
	int *p;
			
	f1(&p);
	*p = 4;
	f2(p);

	free(p); //釋放記憶體
	f2(p); 
	
	return 0;
}
```
```
gedit malloc.c
root@kali:~# gcc malloc.c -o malloc
root@kali:~# ./malloc 
the heap is 4
the heap is 0
```
```
程式定義一個函數
在函數的內部呼叫malloc 函數申請一塊記憶體，並將該記憶體空間的首位址作為傳回值傳回。
之後在main 函數中使用該位址參考這塊空間中的內容，進行給予值操作， 
```
