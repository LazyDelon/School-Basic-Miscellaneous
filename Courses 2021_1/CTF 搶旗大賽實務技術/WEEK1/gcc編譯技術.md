# gcc編譯技術
```
GCC, the GNU Compiler Collection
https://gcc.gnu.org/
```
# gcc 常用指令
```
gcc -v
```
```
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/8/lto-wrapper
OFFLOAD_TARGET_NAMES=nvptx-none
OFFLOAD_TARGET_DEFAULT=1
Target: x86_64-linux-gnu   ==> 
Configured with: ../src/configure -v --with-pkgversion='Debian 8.3.0-6' --with-bugurl=file:///usr/share/doc/gcc-8/README.Bugs --enable-languages=c,ada,c++,go,brig,d,fortran,objc,obj-c++ --prefix=/usr --with-gcc-major-version-only --program-suffix=-8 --program-prefix=x86_64-linux-gnu- --enable-shared --enable-linker-build-id --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --libdir=/usr/lib --enable-nls --enable-bootstrap --enable-clocale=gnu --enable-libstdcxx-debug --enable-libstdcxx-time=yes --with-default-libstdcxx-abi=new --enable-gnu-unique-object --disable-vtable-verify --enable-libmpx --enable-plugin --enable-default-pie --with-system-zlib --with-target-system-zlib --enable-objc-gc=auto --enable-multiarch --disable-werror --with-arch-32=i686 --with-abi=m64 --with-multilib-list=m32,m64,mx32 --enable-multilib --with-tune=generic --enable-offload-targets=nvptx-none --without-cuda-driver --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
Thread model: posix
gcc version 8.3.0 (Debian 8.3.0-6) 
```
# 範例
## 範例1>compile 32-bit program on 64-bit gcc in C and C++
```
https://www.geeksforgeeks.org/compile-32-bit-program-64-bit-gcc-c-c/
```
```
// C program to demonstrate difference 
// in output in 32-bit and 64-bit gcc 
// File name: geek.c 
#include<stdio.h> 
int main() 
{ 
    printf("Size = %lu", sizeof(size_t)); 
} 
```
```
The 32-bit environment sets int, long and pointer to 32 bits 
and generates code that runs on any i386 system.

The 64-bit environment sets int to 32 bits and 
long and pointer to 64 bits and generates code for AMD’s x86-64 architecture.
```
### 編譯成64位元執行檔
```
gcc -m64 geek.c -o out
./out
Size = 8
```
```
file geek

geek: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=f2ba27a69189854b70b7db70b13c57a4a507027e, not stripped
```


### 編譯成32位元執行檔  ==> 錯誤 64 bits kali linux

```
gcc -m32 geek.c -o geek

In file included from geek.c:1:
/usr/include/stdio.h:27:10: fatal error: bits/libc-header-start.h: No such file or directory
 #include <bits/libc-header-start.h>
          ^~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
```

```
https://blog.csdn.net/Stephan14/article/details/46944023?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-4.control&dist_request_id=&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-4.control
```
```
For C language: sudo apt-get install gcc-multilib
For C++ language: sudo apt-get install g++-multilib
```
```
sudo apt-get install libc6-dev-i386

Reading package lists... Done
Building dependency tree       
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 gsettings-desktop-schemas : Breaks: mutter (< 3.31.4) but 3.30.2-7 is to be installed
 libc6-dev : Breaks: libgcc-8-dev (< 8.4.0-2~) but 8.3.0-6 is to be installed
 python3-tornado : Breaks: mitmproxy (< 5.0~) but 4.0.4-5 is to be installed
E: Error, pkgProblemResolver::Resolve generated breaks, this may be caused by held packages.
```
```
gcc -m32 geek.c -o geek
./out
Size = 4
```

## 範例2>
