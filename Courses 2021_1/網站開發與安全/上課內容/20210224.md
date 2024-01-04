# 上課內容
```
XAMPP安裝
建置簡單的client程式
```

# XAMPP安裝
```
https://www.apachefriends.org/download.html
```
```
開發工具
visual studio community
https://visualstudio.microsoft.com/zh-hant/downloads/
```
```
notepad ++
https://notepad-plus-plus.org/downloads/
```
# 範例程式
```
https://www.w3schools.com/html/default.asp
https://www.w3schools.com/css/default.asp
https://www.w3schools.com/js/DEFAULT.asp
```
## HTML_1.html
```
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
</head>
<body>

<h1>聳動的標題 Heading</h1>
<p>段落分明 paragraph.</p>

</body>
</html>
```
## HTML_2.html
```
加入中文編碼
<meta charset="utf-8">
```
```
<!DOCTYPE html>
<html>
<head>
<title>Page Title</title>
<meta charset="utf-8">
</head>
<body>

<h1>聳動的標題 Heading</h1>
<p>段落分明 paragraph.</p>

</body>
</html>
```

## HTML_CSS_1.html
```
添加CSS 彩妝 ==>
<style>
 .........
</style>
```
```
<!DOCTYPE html>
<html>
<head>
<style>
body {
  background-color: lightblue;
}

h1 {
  color: white;
  text-align: center;
}

p {
  font-family: verdana;
  font-size: 20px;
}
</style>
<meta charset="utf-8">
</head>
<body>

<h1>聳動的標題 Heading</h1>
<p>段落分明 paragraph.</p>

</body>
</html>

```

##  HTML_JS_1.html
```
添加JAVAscript互動 ==>
```
```
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
</head>
<body>

<h2>我的互動式JavaScript 超人家的</h2>

<button type="button"
onclick="document.getElementById('demo').innerHTML = Date()">
Click me to display Date and Time.</button>

<p id="demo"></p>

</body>
</html> 
```

## PHP_A_1.php
```
<HTML>
<HEAD>
</HEAD>
<BODY>
<h2>我的第一個 PHP 程式</h2>
<?php
echo "山中相送罷，日暮掩柴扉。";
echo "春草明年綠，王孫歸不歸？";
?>
</BODY>
</HTML>
```
## PHP_A_2.php
```
<!doctype html>
<html>
  <head>
    <meta charset="utf-8">
    <title>我的第一個PHP程式</title>
  </head>
  <body>
    <?php
      echo("Hello World!");
      phpinfo();
    ?>
  </body>
</html>
```

## PHP_A_3.php
```
<!doctype html> 
<html>
  <head>
    <meta charset="utf-8">
    <title>我的第一個PHP程式</title>
  </head>
  <body>
    <?php
      include_once("demo.inc");
    ?>
  </body>
</html>
```

```
<?php
//檔案名稱:demo.inc
// 單行註解comment:This is a single-line comment
# This is also a single-line comment

  echo("Hello World!");
  phpinfo();
  
 /*
 多行註解comment
This is a multiple-lines comment block
that spans over multiple
lines
*/
?>
```
