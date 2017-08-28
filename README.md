# 个人sublime设置

1.  [个人使用sublime的插件](#user-content-个人使用sublime的插件)
2.  [0sublime设置+绑定键](#user-content-0sublime设置绑定键)
3.  [1汉化包(放到install package)](#user-content-1汉化包放到install-package)
4.  [2c_c++设置(放到user文件夹)](#user-content-2c_c设置放到user文件夹)
5.  [3python代码段设置+时间设置(放到user文件夹)](#user-content-3python代码段设置时间设置放到user文件夹)
6.  [4asm汇编设置(放到user文件夹)](#user-content-4asm汇编设置放到user文件夹)
7.  [5批处理设置(放到user文件夹)](#user-content-5批处理设置放到user文件夹)
8.  [6Java设置(放到user文件夹)](#user-content-6java设置放到user文件夹)
9.  [7php设置(放到user文件夹)](#user-content-7php设置放到user文件夹)
10. [sublime注册码.txt](#user-content-sublime注册码)



### 个人使用sublime的插件

* **Markdown Preview**  
    * 预览显示markdown

* **LiveReload**        
    * 保存重载，与Markdown Preview配合使用，即可实时预览markdown

* **MarkdownEditing**   
    * markdown的插件，可设置markdown的主题，推荐黑色

* **Python PEP8 Autoformat**  
    * python代码格式化，按照PEP8规则

* **Jedi - Python autocompletion** 
    * 写python有用

* **SublimeREPL**           
    * sublime的python插件，可以在sublime运行python

* **C Improved**        
    * C语言语法高亮插件，用C++后就无使用了

* **ConvertToUTF8**     
    * 用于解决C/C++编译运行后控制台中文乱码

* **PackageResourceViewer** 
    * 用于查看sublime插件里面的文件

* **SublimeAStyleFormatter** 
    * 用于C/C++代码格式化

* **Emmet** 
    * 写HTML有用的吧

* **Restructured Text (RST) Snippets**

* **RestructuredText Improved**

* **Table Editor**

---

### 0sublime设置+绑定键

- **KeyBinding-user: 用户的按键绑定**

    * <kbd>f5</kbd> 绑定：编译运行C/C++
        - 需要将‘2c_c++设置(放到user文件夹)’/C++C.sublime-build放入sublime根目录的Packages\User目录下
        - 并下载MinGW， 并设置到环境变量中

    * sublime的 <kbd>ctrl</kbd> + <kbd>enter</kbd> 与 <kbd>shift</kbd> + <kbd>enter</kbd> 快捷键交换，为了和pycharm一样可以shift+enter换行

    * <kbd>ctrl</kbd> + <kbd>1</kbd> 绑定插入信息，信息如下(主要是插入到python程序前)
        - \# -\*- coding: utf-8 -\*-
        - \# @Author   : Sdite
        - \# @DateTime : 2017-08-28 11:11:29
        - 需要将‘3python代码段设置+时间设置(放到user文件夹)’中的showtime.py放入sublime根目录的Packages\User目录下

    * <kbd>f1</kbd> <kbd>f2</kbd> 分别绑定python程序的运行和python控制台
        * 需要sublime安装 sublimeREPL

    * <kbd>f3</kbd> 绑定markdown preview，用于显示预览markdown
        - markdown preview具体设置见该插件的README
        - markdown preview实时预览需要sublime安装LiveReload插件

- **PackageControlDownload**
    
    * 安装sublime package control的命令
        - sublime中按 <kbd>ctrl</kbd>+<kbd>~</kbd> 显示面板
        - 复制粘贴命令到该处回车即可
        
- **Sublime-setting**

    * 个人的sublime设置，包括左上侧的小预览，禁止sublime升级，字体大小，文件夹哪类文件隐藏等

---

### 1汉化包(放到install package)

- sublime的汉化，放到sublime根目录的 install package中

---

### 2c_c++设置(放到user文件夹)

- **C++C.sublime-build**
    - C/C++ 代码编译运行的sublime设置

- **c++.sublime-snippet**
    - 需要放入sublime根目录的Packages\User目录下
    - C/C++ snippet代码段，插入的代码段如下(c/c++文件打cpp按tab即可插入如下代码段)
    
    ```C++
    # include <bits/stdc++.h>

    using namespace std;

    int main(int argc, char const *argv[])
    {
        
        return 0;
    }
    ```

---

### 3python代码段设置+时间设置(放到user文件夹)

- **python.sublime-snippet**
    - 需要放入sublime根目录的Packages\User目录下
    - python插入代码段，插入的是函数和类的注释文档代码段（先打'''再按tab）
    
    ```python
    '''
    文档注释

    Args: 
        :

    Returns: 
        :
    '''
    ```

- **Showtime.py**
    - <kbd>ctrl</kbd> + <kbd>1</kbd> 绑定插入信息，信息如下(主要是插入到python程序前)
    * \# -\*- coding: utf-8 -\*-
    * \# @Author   : Sdite
    * \# @DateTime : 2017-08-28 11:11:29
    * 需要将showtime.py放入sublime根目录的Packages\User目录下

---

### 4asm汇编设置(放到user文件夹)

- **sublimeassembly-master**
    * 汇编程序的语法高亮配置文件
    * 将该文件夹放入sublime根目录的Packages\User目录下即可

- **Asm.sublime-build**
    * 汇编程序的编译运行配置文件
    * 需要dosbox的支持，还有要找到dosbox的配置文件，做好一份副本来执行
    * dosbox也要设置到环境变量中
    * dosbox配置文件要虚拟挂载路径
    * 详情不介绍《靠记忆回忆吧 

- **ASM.sublime-snippet**
    * 需要放入sublime根目录的Packages\User目录下
    * 汇编程序的代码段(先打asm再按tab)
    ```assembly
    assume cs:code

    stack segment
        db 128 dup(0)
    stack ends

    code segment
        start:
            mov ax, stack
            mov ss, ax
            mov sp, 128

            
            
            
            
            

            mov ax, 4c00h
            int 21h
            
    code ends
    end start
    ```

---

### 5批处理设置(放到user文件夹)

- **Bat.sublime-build**
    - 批处理文件的执行配置
    - 需要放入sublime根目录的Packages\User目录下

---

### 6Java设置(放到user文件夹)

- **Java.sublime-build**
    - JAVA文件的执行配置需要搭配runJava.bat
    - 需要放入sublime根目录的Packages\User目录下

- **runJava.bat**
    - 放到Java的bin目录下

---

### 7php设置(放到user文件夹)
- **php.sublime-buildd**
    - php文件的执行配置
    - 需要配置好php环境， 具体已经忘记了呃。以后再说
    - 需要放入sublime根目录的Packages\User目录下

---

### sublime注册码

- sublim的注册码，还可以使用


