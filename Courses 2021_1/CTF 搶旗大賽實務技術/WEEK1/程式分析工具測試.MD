# 程式分析工具
```
strings
file
hexdump
ldd
objdump
ltrace
strace
nc
ncat
checksec
IDA pro
gdb

Python - pwntools
Python - ctypes
```

# netcat(nc) | socat | Ncat
```
netcat(nc)原始版本是一個類Unix程式。原作者叫做*Hobbit*。
socat是netcat較複雜的姊妹程式。它比起netcat功能更多。
Ncat是由Nmap開發團隊實做的另一個netcat版本。
```
### nc
```
https://zh.wikipedia.org/wiki/Netcat

netcat (often abbreviated to nc) is a computer networking utility for 
reading from and writing to network connections using TCP or UDP. 

The command is designed to be a dependable back-end 
that can be used directly or easily driven by other programs and scripts. 

At the same time, it is a feature-rich network debugging and investigation tool, 
since it can produce almost any kind of connection its user could need 
and has a number of built-in capabilities.

Its list of features includes port scanning, transferring files, and port listening, 
and it can be used as a backdoor.
```
# ncat 
```

Ncat Reference Guide
https://nmap.org/book/ncat-man-options-summary.html
```
```
https://nmap.org/ncat/guide/ncat-exec.html

There are three ways of running a command:
--exec runs a command without shell interpretation.
--sh-exec runs a command by passing a string to a system shell.
--lua-exec runs a Lua program using Ncat's built-in Lua interpreter.
```
```
ncat -lkv -p port -c 'command'    
ncat -lkv -p port -e 'command'
```


# checksec.sh
```
$ wget -O checksec.sh \
'https://raw.githubusercontent.com/slimm609/checksec.sh/master/checksec'

$ chmod 755 ./checksec.sh

$ ./checksec.sh --file binary
```

#
```


```
