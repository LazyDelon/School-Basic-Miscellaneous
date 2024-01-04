# 組合語言 程式語法 與 解讀
```
Introduction to Computer Organization with x86-64 Assembly Language & GNU/Linux
Robert G. Plantz
http://bob.cs.sonoma.edu/IntroCompOrg-x64/book.htm
```
```
https://download-mirror.savannah.gnu.org/releases/pgubook/ProgrammingGroundUp-1-0-booksize.pdf
```

# intel語法 vs AT&T語法
```
不同平臺有不同的instruction set(指令集)，比如x86, PowerPC, ARM等平臺的指令集是不同的。
彙編一直存在兩種不同的語法:intel語法 vs AT&T語法
在intel的官方文件中使用intel語法，Windows也使用intel語法
UNIX 系統的彙編器一直使用AT&T語法
```

## AT&T 與 Intel 組合語言的比較
```
https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/433209/
http://colorben.blogspot.com/2010/01/at.html
https://iter01.com/195956.html
```
```
(1)字首
AT&T  ==>暫存器前冠以“％”，而立即數前冠以“$”    %eax 
Intel ==>暫存器和和立即數都沒有字首             eax

AT&T  ==>立即數前冠以“$”    movl $_value, %ebx            把_value的位址(address)放入eax寄存器
Intel ==>立即數都沒有字首   mov eax,_value 

AT&T  ==>十六進位制立即數前冠以“0x”,           
Intel ==>十六進位制和二進位制立即數字尾分別冠以“h”和“b”


AT&T  ==> Movl $8,%eax
Intel ==> Mov eax 8

(2)運算元的方向 ==>Intel 與AT&T 運算元的方向正好相反

AT&T  ==> 運算子  來源運算元 --> 目的運算元
Intel ==> 運算子  目的運算元 <-- 來源運算元

(3)記憶體單元運算元 ==>

AT&T  ==>基底暫存器 用“（）”括起來    movl 5（%ebx）,%eax
Intel ==>基底暫存器 用“[]”括起來      mov eax, [ebx 5]

(4)定址方式(Addressing)

直接定址方式
AT&T  ==> _booga　; _booga是一個全局的C變量
Intel ==> [_booga]

加上$是表示位址引用(取址address)，不加是表示值引用(取值value)


間接定址方式
AT&T  ==>immed32(basepointer,indexpointer,indexscale) 
Intel ==> [basepointer + indexpointer*indexscale + imm32)

AT&T  ==>
Intel ==>

AT&T  ==> Movl   0x20(%ebx),%eax
Intel ==> mov    eax,[ebx 20h]

AT&T  ==>
Intel ==>

(5) 操作碼的字尾

AT&T  ==> 操作碼後面有一個字尾，其含義就是指出操作碼的大小。
          “l”表示長整數（32 位），“w”表示字（16 位），“b”表示位元組（8 位）
          movb
          
Intel ==> 在記憶體單元運算元的前面加上byte ptr、word ptr 和dword ptr，
          “dword”對應“long”
          mov 

AT&T  ==> movb  %bl, %al
Intel ==> mov   al,  bl

AT&T  ==>
Intel ==>

AT&T  ==>
Intel ==>
```

```
Table 10.1: Conditional jump instructions

```
