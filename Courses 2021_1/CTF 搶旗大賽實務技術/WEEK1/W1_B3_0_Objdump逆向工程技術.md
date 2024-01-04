# Objdump逆向工程技術
```
objdump -d /bin/bash  ==> 預設使用 AT&T 語法格式
objdump -d -M intel /bin/bash ==> 使用intel 語法格式
```

```
objdump -S helloCTFer
注意編譯時要加gcc helloCTFer.c -o helloCTFer -g

```

# 範例程式  
```
// helloCTFer.c
#include <stdio.h>

int main()
{
   printf("Hello CTFer\n ”);
   return 0;
}
```
## 編譯成Intel 格式的組語
```
gcc -S  -O0 -fno-asynchronous-unwind-tables assignment1.c
```

