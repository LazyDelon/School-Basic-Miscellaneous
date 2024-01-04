# A2_1_組合語言CTF解題
```
pico-ctf-2014
reverse-engineering/basic-asm-60

angstromCTF 2016:asm-tracing-45
```
# pico-ctf-2014 reverse-engineering/basic-asm-60
```
pico-ctf-2014
reverse-engineering/basic-asm-60

We found this program snippet.txt, but we're having some trouble figuring it out. 
What's the value of %eax when the last instruction (the NOP) runs?
```

```
# This file is in AT&T syntax - see http://www.imada.sdu.dk/Courses/DM18/Litteratur/IntelnATT.htm
# and http://en.wikipedia.org/wiki/X86_assembly_language#Syntax. Both gdb and objdump produce
# AT&T syntax by default.

MOV $10814,%ebx
MOV $2972,%eax
MOV $10017,%ecx
CMP %eax,%ebx
JL L1
JMP L2
L1:
IMUL %eax,%ebx
ADD %eax,%ebx
MOV %ebx,%eax
SUB %ecx,%eax
JMP L3
L2:
IMUL %eax,%ebx
SUB %eax,%ebx
MOV %ebx,%eax
ADD %ecx,%eax
L3:
NOP
```
```
https://github.com/VulnHub/ctf-writeups/blob/master/2014/picoctf/basic-asm.md

https://ehsan.dev/pico2014/reverse_engineering/basic_asm.html
```
# angstromCTF 2016 : asm-tracing-45
```
Reading assembly language is one of the core skills for reverse engineering. 
Test your abilities by tracing this code and seeing what %eax contains by the end! 
Enter the result as an unsigned decimal integer.

# This ASM is AT&T syntax: http://www.imada.sdu.dk/Courses/DM18/Litteratur/IntelnATT.htm
# All the GNU tools (as, gdb, and objdump) use AT&T syntax by default
start:
	mov $1337, %eax
	mov $6098, %ebx
	mov $4352, %ecx
	xor %edx, %edx
	
	sub %ecx, %ebx
	cmp %ebx, %eax
	jge next1
	jmp next2
next1:
	cmp $4, %edx
	jg end
	inc %edx
next2:
	xchg %eax, %ebx
	idiv %ebx
	add %edx, %eax
	imul %ecx
	jmp next1
end:
```
# Python 逆向工程題
# JAVA 逆向工程題 Towers of Toast - 90
```
Pico CTF 2014 Towers of Toast - 90

https://ehsan.dev/pico2014/reverse_engineering/towers_of_toast.html
https://tuonilabs.wordpress.com/2017/01/12/picoctf-2014-write-up/
```

```
https://penafieljlm.com/2017/05/01/picoctf-2017-write-up/
```
