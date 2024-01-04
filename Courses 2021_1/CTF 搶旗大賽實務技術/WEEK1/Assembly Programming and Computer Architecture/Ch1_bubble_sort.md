#
```

```
# 
```
// Chapter 1
// C++ Bubble Sort
// Copyright (c) 2017 Hall & Slonka

int main(){
   
   int  size = 5;
   int  value[5] = {3, 2, 6, 4, 1};
   int  i, tmp;
   bool swapped;
   
   do
   {
      swapped = false;
      for (i = 0; i < size - 1; i++){
         if (value[i + 1] < value[i])
         {
            tmp = value[i];
            value[i] = value[i + 1];
            value[i + 1] = tmp;
            swapped = true;
         }
      }
   }  while (swapped);

   return 0;
}
```

# Ch1_Bubble_GAS_Linux.s
```
# Chapter 1
# Assembly Bubble Sort - GAS, Clang/LLVM on Linux (32-bit)
# Copyright (c) 2017 Hall & Slonka

.data
array: .long 3, 2, 6, 4, 1
count: .long 5

.text
.globl _main
_main:

mov count, %ecx
dec %ecx

outerLoop:
push %ecx
lea array, %esi

innerLoop:
mov (%esi), %eax
cmp %eax, 4(%esi)
jg nextStep
xchg 4(%esi), %eax
mov %eax, (%esi)

nextStep:
add $4, %esi
loop innerLoop
pop %ecx
loop outerLoop

movl $1, %eax
movl $0, %ebx
int $0x80
.end
```

# x86_64/Ch1_Bubble_GAS_Linux.s
```
# Chapter 1
# Assembly Bubble Sort - GAS, Clang/LLVM on Linux (64-bit)
# Copyright (c) 2019 Hall & Slonka

.data
array: .long 3, 2, 6, 4, 1
count: .long 5

.text
.global _main
_main:

movslq count(%rip), %rcx
dec %rcx

outerLoop:
push %rcx
leaq array(%rip), %rsi

innerLoop:
movl (%rsi), %eax
cmpl %eax, 4(%rsi)
jg nextStep
xchgl 4(%rsi), %eax
movl %eax, (%rsi)

nextStep:
addq $4, %rsi
loop innerLoop
popq %rcx
loop outerLoop

movq $60, %rax
xorq %rdi, %rdi
syscall
.end
```
