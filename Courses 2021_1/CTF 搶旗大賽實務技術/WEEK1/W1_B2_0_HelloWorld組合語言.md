# nasm程式碼架構
```
http://www.posix.nl/linuxassembly/nasmdochtml/nasmdoca.html
http://athena.nitc.ac.in/piyush_b130057cs/NASM/NASM%20TUTORIAL.pdf
```
```
由不同section組成,各section有不同功能
```

```
section .data  ==>  Section containing initialised data《有初值的資料》

section .bss   ==>  Section containing uninitialized data《沒有初值的資料》 ;可有可無的選項

section .text  ==>  ; Section containing code 《執行程式碼》
```
## 線上組譯器
```
http://rextester.com/l/nasm_online_compiler
```
## 32-bit helloworld32.asm
```
;nasm 2.11.08

section .data
    hello:     db 'Hello world!',10    ; 'Hello world!' plus a linefeed character
    helloLen:  equ $-hello             ; Length of the 'Hello world!' string

section .text
	global _start

_start:
	mov eax,4            ; The system call for write (sys_write)  32位元Linux系統呼叫
	mov ebx,1            ; File descriptor 1 - standard output
	mov ecx,hello        ; Put the offset of hello in ecx
	mov edx,helloLen     ; helloLen is a constant, so we don't need to say
	                     ;  mov edx,[helloLen] to get it's actual value
	int 80h              ; Call the kernel

	mov eax,1            ; The system call for exit (sys_exit)   32位元Linux系統呼叫
	mov ebx,0            ; Exit with return code of 0 (no error)
	int 80h;
```
### 執行
```
$ nasm -f elf32 helloworld32.asm
$ ld helloworld32.o -o helloworld32
$ ./helloworld32
```
### 用hexdump看看
```
hd helloworld32.o
```
```
00000000  7f 45 4c 46 01 01 01 00  00 00 00 00 00 00 00 00  |.ELF............|
00000010  01 00 03 00 01 00 00 00  00 00 00 00 00 00 00 00  |................|
00000020  40 00 00 00 00 00 00 00  34 00 00 00 00 00 28 00  |@.......4.....(.|
00000030  07 00 03 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
000000a0  70 01 00 00 22 00 00 00  00 00 00 00 00 00 00 00  |p..."...........|
000000b0  10 00 00 00 00 00 00 00  0d 00 00 00 03 00 00 00  |................|
000000c0  00 00 00 00 00 00 00 00  a0 01 00 00 31 00 00 00  |............1...|
000000d0  00 00 00 00 00 00 00 00  01 00 00 00 00 00 00 00  |................|
000000e0  17 00 00 00 02 00 00 00  00 00 00 00 00 00 00 00  |................|
000000f0  e0 01 00 00 70 00 00 00  05 00 00 00 06 00 00 00  |....p...........|
00000100  04 00 00 00 10 00 00 00  1f 00 00 00 03 00 00 00  |................|
00000110  00 00 00 00 00 00 00 00  50 02 00 00 26 00 00 00  |........P...&...|
00000120  00 00 00 00 00 00 00 00  01 00 00 00 00 00 00 00  |................|
00000150  04 00 00 00 08 00 00 00  00 00 00 00 00 00 00 00  |................|
00000160  48 65 6c 6c 6f 20 77 6f  72 6c 64 21 0a 00 00 00  |Hello world!....|
00000170  b8 04 00 00 00 bb 01 00  00 00 b9 00 00 00 00 ba  |................|
00000180  0d 00 00 00 cd 80 b8 01  00 00 00 bb 00 00 00 00  |................|
00000190  cd 80 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
000001a0  00 2e 64 61 74 61 00 2e  74 65 78 74 00 2e 73 68  |..data..text..sh|
000001b0  73 74 72 74 61 62 00 2e  73 79 6d 74 61 62 00 2e  |strtab..symtab..|
000001c0  73 74 72 74 61 62 00 2e  72 65 6c 2e 74 65 78 74  |strtab..rel.text|
000001d0  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  |................|
*
00000240  1f 00 00 00 00 00 00 00  00 00 00 00 10 00 02 00  |................|
00000250  00 68 65 6c 6c 6f 77 6f  72 6c 64 2e 61 73 6d 00  |.helloworld.asm.|
00000260  68 65 6c 6c 6f 00 68 65  6c 6c 6f 4c 65 6e 00 5f  |hello.helloLen._|
00000270  73 74 61 72 74 00 00 00  00 00 00 00 00 00 00 00  |start...........|
00000280  0b 00 00 00 01 02 00 00  00 00 00 00 00 00 00 00  |................|
00000290
```
### 32位元Linux系統呼叫
```
http://syscalls.kernelgrok.com/
```
# 64-bit helloworld64.asm
```
; 64-bit "Hello World!" in Linux NASM

global _start            ; global entry point export for ld

section .text
_start:

    ; sys_write(stdout, message, length)  系統呼叫
    mov    rax, 1        ; sys_write
    mov    rdi, 1        ; stdout
    mov    rsi, message    ; message address
    mov    rdx, length    ; message string length
    syscall

    ; sys_exit(return_code) 系統呼叫
    mov    rax, 60        ; sys_exit
    mov    rdi, 0        ; return 0 (success)
    syscall

section .data
    message: db 'Hello, world!',0x0A    ; message and newline
    length:    equ    $-message        ; NASM definition pseudo-instruction
```
### 執行
```
$ nasm -f elf64 helloworld64.asm
$ ld helloworld64.o -o helloworld64
$ ./helloworld64
```
### 用hexdump看看
```
hd helloworld64.o
```
### 64位元Linux系統呼叫
```
http://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/

最新版的定義
https://github.com/torvalds/linux/blob/master/arch/x86/entry/syscalls/syscall_64.tbl
```
