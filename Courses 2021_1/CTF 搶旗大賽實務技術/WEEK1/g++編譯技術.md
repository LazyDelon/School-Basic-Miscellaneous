#
```

```

# 範例練習 1
```
Compiling with g++
Last Updated : 27 Dec, 2020
https://www.geeksforgeeks.org/compiling-with-g-plus-plus/
```

```
g++ --version ==> Check g++ compiler version information:
```
```
// hello.cpp file

#include <iostream>
int main()
{
    std::cout << "Hello Geek\n";
    return 0;
}
```
### 執行
```
//練習1
g++ hello.cpp
./a.out
```

```
//練習2
g++ -o main.exe hello.cpp
```

```
//練習3
g++ -S hello.cpp
```

```
//練習4
g++ -c hello.cpp
```
# 範例練習 2: 多個檔案編譯
```
// hello.cpp file
#include "helloWorld.h"
#include <iostream>
int main()
{
    std::cout << "Hello Geek\n";
    helloWorld();
    return 0;
}
```


```
// helloWorld.cpp file
#include <iostream>
void helloWorld()
{
    std::cout << "Hello World\n";
}
```

```
// helloWorld.h file
void helloWorld();
```
```
//練習1

g++ -c helloWorld.cpp hello.cpp

g++ -o main.exe helloWorld.o hello.o

./main.exe
```


```
//練習
