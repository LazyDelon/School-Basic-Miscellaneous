# LD_PRELOAD技術
```
使用LD_PRELOAD技術完成簡易型駭客程式注入
```
## 範例
```
// main.c
#include <stdio.h>
#include <math.h>

int main() {
  double x;
  
  scanf("%lf", &x);
  printf("%f\n", sqrt(x));
  return 0;
}
```
### 執行看看正確答案
```
gcc -o main main.c -lm
./main
```
### 撰寫駭客程式
```
//hook.c
double sqrt(double x) {
  return 2;
}
```
### 編譯並執行看看被竄改的答案
```
gcc -o hook.so -shared hook.c
LD_PRELOAD=./hook.so ./main
```
###
```
ksu@KSU-Ubuntu-1604-32:~$ gedit main.c
ksu@KSU-Ubuntu-1604-32:~$ gcc -o main main.c -lm
ksu@KSU-Ubuntu-1604-32:~$ ./main
foo
-nan
ksu@KSU-Ubuntu-1604-32:~$ ./main
16
4.000000


ksu@KSU-Ubuntu-1604-32:~$ gedit hook.c
ksu@KSU-Ubuntu-1604-32:~$ gcc -o hook.so -shared hook.c
ksu@KSU-Ubuntu-1604-32:~$ LD_PRELOAD=./hook.so ./main
5
2.000000

```
