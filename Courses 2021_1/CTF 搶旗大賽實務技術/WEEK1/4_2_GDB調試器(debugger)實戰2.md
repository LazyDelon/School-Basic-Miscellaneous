# 教科書
```
王者歸來－Linux C 系統整合開發設計, 4/e
吳岳  佳魁資訊  2016-04-19

第9 章 gdb
9.1 列出來源程式
9.2 執行程式的指令 
9.3 操作中斷點的指令
9.4 檢視執行時資料 
9.5 改變程式的執行
9.6 gdb 高級應用
```

# 9.2 執行程式的指令  test2.c
```
#include <stdio.h>
#include <stdlib.h>

int main(int argc,char *argv[])
{
   if(argc != 3){ 
      printf("Usage:hello wordl word2");
      exit(0);
   }
   
   printf("wordl is %s \n word2 is %s \n" , argv[1] , argv[1]);

   //printstar();
   return (0);
}
```

## 
```
gcc test2.c -o test2

./test2

./test2 Google Linux
```

```
gcc -g test2.c -o test2

gdb ./test2

(gdb) run linux gdb
(gdb) show args
(gdb) set args chgl chg2    ==> 使用set 指令可以設定新的參數，輸入
(gdb) run
```
