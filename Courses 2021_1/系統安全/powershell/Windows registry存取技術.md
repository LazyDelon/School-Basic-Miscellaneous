# Windows registry登錄檔
```
登錄檔（英語：Registry，中國大陸譯作註冊表，台灣、港、澳譯作登錄檔）是Microsoft Windows操作系統和其應用程式中
的一個重要的層次型資料庫，用於儲存系統和應用程式的設定資訊。

早在Windows 3.0推出OLE技術的時候，登錄檔就已經出現。
但是，從Windows 95開始，登錄檔才真正成為Windows使用者經常接觸的內容，並在其後的作業系統中繼續沿用至今。
隨後推出的Windows NT是第一個從系統級別廣泛使用登錄檔的作業系統

https://zh.wikipedia.org/wiki/%E6%B3%A8%E5%86%8C%E8%A1%A8
```
```
登錄檔由鍵（key，或稱「項」）、子鍵（subkey，子項）和值項（value）構成。
一個鍵就是樹狀資料結構中的一個節點，而子鍵就是這個節點的子節點，子鍵也是鍵。
一個值項則是一個鍵的一條內容，由名稱（name）、資料類型（datatype）以及資料（data）組成。
一個鍵可以有一個或多個值，每個值的名稱各不相同，如果一個值的名稱為空，則該值為該鍵的預設值。
```
```
登錄檔的分支結構
登錄檔有五個一級分支：

HKEY_CLASSES_ROOT ==>	儲存Windows可辨識的檔案類型的詳細列表，以及相關聯的程式。
HKEY_CURRENT_USER ==>	儲存當前使用者設定的資訊。
HKEY_LOCAL_MACHINE ==>	包括安裝在電腦上的硬體和軟體的資訊。
HKEY_USERS ==>	包含使用電腦的使用者的資訊。
HKEY_CURRENT_CONFIG ==>	這個分支包含電腦當前的硬體組態資訊
```
# regedit.exe
```
%windir%\regedit.exe
```
# reg /?
```
reg /?

REG Operation [Parameter List]

  Operation  [ QUERY   | ADD    | DELETE  | COPY    |
               SAVE    | LOAD   | UNLOAD  | RESTORE |
               COMPARE | EXPORT | IMPORT  | FLAGS ]

傳回碼: (除了 REG COMPARE)

  0 - 成功
  1 - 失敗

針對特定操作類型的說明:

  REG Operation /?

範例:

  REG QUERY /?
  REG ADD /?
  REG DELETE /?
  REG COPY /?
  REG SAVE /?
  REG RESTORE /?
  REG LOAD /?
  REG UNLOAD /?
  REG COMPARE /?
  REG EXPORT /?
  REG IMPORT /?
  REG FLAGS /?
```
# 使用powershell存取
```
Windows Registry Tutorial
https://www.netwrix.com/windows_registry_tutorial.html?itm_source=blog&itm_medium=context&itm_campaign=windows-server&itm_content=none&_ga=2.194294820.885143600.1600880847-650513495.1600880847
```
# 使用python 存取
```
winreg — Windows registry access
https://docs.python.org/3/library/winreg.html
```

# 
```
Working with Registry Entries
https://docs.microsoft.com/en-us/powershell/scripting/samples/working-with-registry-entries?view=powershell-7.1

Working With Files, Folders and Registry Keys
https://docs.microsoft.com/en-us/powershell/scripting/samples/working-with-files-folders-and-registry-keys?view=powershell-7.1

Working with Registry Keys
https://docs.microsoft.com/en-us/powershell/scripting/samples/working-with-registry-keys?view=powershell-7.1
```
