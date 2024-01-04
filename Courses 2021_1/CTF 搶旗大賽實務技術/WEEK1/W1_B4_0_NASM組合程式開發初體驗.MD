# nasm
```
https://zh.wikipedia.org/wiki/Netwide_Assembler

Netwide Assembler （簡稱 NASM）是一款基於英特爾 x86 架構的彙編與反彙編工具。
它可以用來編寫16位、32位（IA-32）和64位（x86-64）的程序。 
NASM被認為是Linux平台上最受歡迎的彙編工具之一。[1]

NASM 最初是在朱利安·霍爾的協助下由西蒙·泰瑟姆開發的。 
截至2016年，它被一個由H.Peter Anvin領導的小團隊所維護。
它是一款基於簡化版（二句版）BSD許可證的開放原始碼軟體。[3]
```
# 官方網址
```
https://www.nasm.us/


https://www.nasm.us/docs.php

https://www.nasm.us/xdoc/2.15.05/html/nasmdoc0.html
```
# 學習資源
```
Learn Assembly Language ==> NASM x86 assembly language on linux
https://asmtutor.com/
```
# How To Install nasm on kali
```
sudo apt-get install nasm

https://installlion.com/kali/kali/main/n/nasm/install/index.html

How to install NASM and compile Assembly program in kali linux.
- July 22, 2018
http://mycodingpage.blogspot.com/2018/07/how-to-install-and-compile-assembly.html
```
# 檢查linux 是否為64位元
```
cat /proc/version

Linux version 4.19.0-kali4-amd64 (devel@kali.org) 
(gcc version 8.3.0 (Debian 8.3.0-2)) #1 SMP Debian 4.19.28-2kali1 (2019-03-18)
```
# 範例練習 1
```
NASM Tutorial

https://cs.lmu.edu/~ray/notes/nasmtutorial/
```

```
; ----------------------------------------------------------------------------------------
; Writes "Hello, World" to the console using only system calls. Runs on 64-bit Linux only.
; To assemble and run:
;
;     nasm -felf64 hello.asm && ld hello.o && ./a.out
; ----------------------------------------------------------------------------------------

          global    _start

          section   .text
_start:   mov       rax, 1                  ; system call for write
          mov       rdi, 1                  ; file handle 1 is stdout
          mov       rsi, message            ; address of string to output
          mov       rdx, 13                 ; number of bytes
          syscall                           ; invoke operating system to do the write
          mov       rax, 60                 ; system call for exit
          xor       rdi, rdi                ; exit code 0
          syscall                           ; invoke operating system to exit

          section   .data
message:  db        "Hello, World", 10      ; note the newline at the end
```
# 範例練習 2==> 32 位元
```
Learn Assembly Language ==> NASM x86 assembly language on linux
https://asmtutor.com/

https://asmtutor.com/#lesson1
```

```
; Hello World Program - asmtutor.com
; Compile with: nasm -f elf helloworld.asm
; Link with (64 bit systems require elf_i386 option): ld -m elf_i386 helloworld.o -o helloworld
; Run with: ./helloworld
 
SECTION .data
msg     db      'Hello World!', 0Ah     ; assign msg variable with your message string
 
SECTION .text
global  _start
 
_start:
 
    mov     edx, 13     ; number of bytes to write - one for each letter plus 0Ah (line feed character)
    mov     ecx, msg    ; move the memory address of our message string into ecx
    mov     ebx, 1      ; write to the STDOUT file
    mov     eax, 4      ; invoke SYS_WRITE (kernel opcode 4)
    int     80h
```

# 範例程式1: 
## hello.asm
```
section .text
 global _start
  _start:
 mov edx,len
 mov ecx,msg
 mov ebx,1
 mov eax,4
 int 0x80
 
 mov eax,1
 int 0x80

  section .data
  msg db 'hello World!' , 0xa
  len equ $ -msg
```
## 組譯與執行 ==> 64 位元執行檔(binary)
```
nasm -f elf64 hello.asm     # assemble the program  64位元

ld hello.o -o hello

./hello
```
### binary 簡單分析
```
file hello

hello: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), statically linked, not stripped
```
```
strings hello


hello World!
hello.asm
__bss_start
_edata
_end
.symtab
.strtab
.shstrtab
.note.gnu.property
.text
.data
```

## 組譯與執行 ==> 32 位元執行檔(binary)
```
nasm -f elf32 hello.asm -o hello2.o

ld -m elf_i386  hello2.o -o hello

./hello
```

### binary 簡單分析
```
file hello

hello: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, not stripped
```
```
strings hello


hello World!
hello.asm
__bss_start
_edata
_end
.symtab
.strtab
.shstrtab
.note.gnu.property
.text
.data
```

```
hexdump hello


0000000 457f 464c 0101 0001 0000 0000 0000 0000
0000010 0002 0003 0001 0000 9000 0804 0034 0000
0000020 2128 0000 0000 0000 0034 0020 0004 0028
0000030 0007 0006 0001 0000 0000 0000 8000 0804
0000040 8000 0804 00d0 0000 00d0 0000 0004 0000
0000050 1000 0000 0001 0000 1000 0000 9000 0804
0000060 9000 0804 001d 0000 001d 0000 0005 0000
0000070 1000 0000 0001 0000 2000 0000 a000 0804

```
# ld
```
ld -V
GNU ld (GNU Binutils for Debian) 2.31.1
  Supported emulations:
   elf_x86_64
   elf32_x86_64
   elf_i386
   elf_iamcu
   elf_l1om
   elf_k1om
   i386pep
   i386pe
```
