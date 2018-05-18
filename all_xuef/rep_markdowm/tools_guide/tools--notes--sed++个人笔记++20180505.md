

+ ```bash
  sed 's/root/alice/' /etc/passwd # 替换每行第一个匹配的内容
  sed 's/root/alice/gi' /etc/passwd # 替换每行所有匹配的内容
  # i 忽略大小写
  ```

+ 替换整行 c

```bash
sed '/root/cAlice' /etc/passwd
```

+ 删除空行

```bash
sed '/^\s*$/d' filename
```

+ 查找替换时匹配特殊字符

```bash
sed '20,70s#/linux#/LINUX#g'
```



# sed 101 hacks

### sed 处理流程

#### 语法

```bash
sed [options] {sed-commands} {input-file} 
sed -n '1,5p' /etc/passwd 

sed -n -e '/^root/ p' -e '/^nobody/ p' /etc/passwd

sed [options] '{
sed-command-1
sed-command-2
}' input-file 
```

#### 流程

1. 读取一行进模式空间
2. 执行命令（就在模式空间中，故不改变源内容）
3. 打印该行（处理后的），模式空间清空
4. 回到1，循环，直到文杰末尾

### 过滤行

#### 指定行

```bas
sed -n '1,5p' /etc/passwd # 1到5行
$ sed -n '2,$ p' employee.txt # 到行尾
# sed -n '2,+5p' /etc/passwd # 第2行开始，读取5行

1~2 matches 1,3,5,7, etc.
2~2 matches 2,4,6,8, etc.
1~3 matches 1,4,7,10, etc.
2~3 matches 2,5,8,11, etc
```

#### 模式匹配

```bash
$ sed -n '/Jane/ p' employee.txt 

# Print lines starting from the 1st match of "Jason" until the 4th line:
$ sed -n '/Jason/,4 p' employee.txt 

# Print lines starting from the line matching "Raj" until the line matching "Jane":
$ sed -n '/Raj/,/Jane/ p' employee.txt 

# Print the line matching "Jason" and 2 lines immediately after that:
$ sed -n '/Jason/,+2 p' employee.txt 
```



### 删除行

```bash
# Delete only the 2nd line:
$ sed '2 d' employee.txt 

# Delete from line 1 through 4:
$ sed '1,4 d' employee.txt 

# Delete from line 2 through the last line:
$ sed '2,$ d' employee.txt 

# Delete only odd number of lines:
$ sed '1~2 d' employee.txt

# Delete lines matching the pattern "Manager":
$ sed '/Manager/ d' employee.txt 

# Delete lines starting from the 1st match of "Jason" until the 4th line:
$ sed '/Jason/,4 d' employee.txt 

# Delete lines starting from the 1st match of "Raj" until the last line:
$ sed '/Raj/,$ d' employee.txt

# Delete lines starting from the line matching "Raj" until the line matching "Jane":
$ sed '/Raj/,/Jane/ d' employee.txt

# Delete lines starting from the line matching "Jason" and 2 lines immediately after that:
$ sed '/Jason/,+2 d' employee.txt 

```

#### 很有用的行删除实例

```bash
# Delete all the empty lines from a file:
sed '/^$/ d' employee.txt
# Delete all comment lines (assuming the comment starts with #):
sed '/^#/ d' employee.txt
```



### 替换

```bash
sed '[address-range|pattern-range] s/original-string/replacement-string/[substitute-flags]' inputfile

# Replace Manager with Director only on lines that contain the keyword 'Sales':
# 包含 Sales 的行---行过滤
$ sed '/Sales/s/Manager/Director/' employee.txt

# 忽略大小写
# Replace “john” or “John” with Johnny:
$ sed 's/john/Johnny/i' employee.txt

# 12. Execute Flag (e flag)
$ cat files.txt
/etc/passwd
/etc/group

Add the text "ls -l " in front of every line in the files.txt and print the output:
$ sed 's/^/ls -l /' files.txt
ls -l /etc/passwd
ls -l /etc/group

Add the text "ls -l " in front of every line in the files.txt and execute the output:
$ sed 's/^/ls -l /e' files.txt
-rw-r--r-- 1 root root 1547 Oct 27 08:11 /etc/passwd
-rw-r--r-- 1 root root 651 Oct 27 08:11 /etc/group
```



#### 16. Power of & - Get Matched Pattern

```bash
# 我上次对Windows下编辑的文件操作，无效。是文件格式?还是没用 # 分隔符?
sed 's#^.*#<a href="&" target="_blank">&</a>#' url.txt 
<a href="https://www.baidu.com" target="_blank">https://www.baidu.com</a>
<a href="https://47.97.197.165:8080" target="_blank">https://47.97.197.165:8080</a>

```































