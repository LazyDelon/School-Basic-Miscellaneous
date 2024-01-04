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

# 9.3 操作中斷點的指令
## test3.c
```
#include <stdio.h>

int sum (inta){
  int i ,res=O;
  
  for(i=O ; i<a ;i ++){
    res +=i;

    return res ;
}

int main(void){
   int a= 10;
   int asum = sum(a);
   printf("sum is %d \n", asum); 
   return O;
}
```
```
(1)使用break 指令設定中斷點。
(gdb) break 7

(2)執行程式並使用 watch指令，設定觀察點運算式為i=3 。
(gdb) watch i ==3

(3)刪除中斷點1 。
(gdb) db 1

(4）繼續執行程式。
(gdb) continue
```

## test4.c
```
#linclude <stdio.h>
#include <stdlib.h>
#include <string.h>

my_print(char *string){
  printf("The string is %s\n", string)
}

void my print2 (char *string){
   char *string2 ;
   int size , i;
   
   size = strlen(string);
   string2 = (char*) malloc(size+ 1);  /*為string2 分配儲存空間*/

    for(i = 0; i < size; i++)
       string2[size-i]= string [i];
      
    string2[size+l] = '\0' ;      /* ＼0 ==>結束符號*/
    
    printf("The string printed backward is %s\n ", string2);
}

int main (void){
    char my_string[] = "hello there"; 
    
    my_print(my_string);
    my_print2(my_string);
    
    return 0;
}
```
### 執行此錯誤程式
```

gcc -g -o test4 test4.c

./test4
```

### 使用gdb除錯
```

```
