# 学习Python的姿势——工具篇（Windows）
回顾上周，主要工作集中在研究各种工具的使用，语言本身因为有些底子，进步空间不是那么大。

## 终端：cmder
是cmd和powershell的替代品，具体优势还不是很明确，目前用到以下快捷功能：
- Tab键自动补全目录
- up键选择上条命令
- 选中文本后，Ctrl+V直接复制
- Ctrl+R历史命令搜索
- 修改Cmder目录下vendor\profile.ps1文件，Like This：

    Set-Alias st "C:\Program Files\Sublime Text 3\sublime_text.exe"
    function Git-Status { git status }
    Set-Alias gs Git-Status
    function go-Work {cd E:\work\web\cdn\}
    Set-Alias gw go-Work

st xxx就用实现以sublimeText打开xxx文件；gw下就能进入所设置的目录;gs相当于在使用git文件目录下用git status


## 编辑器：Atom
之前使用sublime比较顺手，Atom还没有深入研究，如何配置，如何作为IDE使用，待补充.找了一个![基础教程](http://wiki.jikexueyuan.com/project/atom/basis.html)

## 编辑器：Jupyter Notebook
天呐，这什么玩意，好难用啊，目前存在以下几个问题：
- 无法提供markdown预览
- 无法高亮代码关键字
- 直接运行代码的功能还不错，但是有时候点运行无响应，直接新开了一个cell
- 交互性到底在哪？

## 版本管理工具：Git
目前还没有意识到版本管理的重要性，每一次更新都会将之前的文件备份，并标注差异。

### 配置 SSH Key
1. 检查电脑上是否已有SSH Key,有的话会列出所有.pub文件，重新生成会删除原有文件

    $ ls -al ~/.ssh 
    
2. 生成 SSH Key

    $ ssh-keygen -t rsa -b 4096 -C "Github绑定的邮箱" # 之后会让输文件密码，可以回车跳过
    
 3. 添加SSH Key到ssh-agent
 
     $ ssh-agent -s 
     $ ssh-add ~/.ssh/id_rsa
     
 4. 复制id_rsa.pub文件内容到黏贴板
 
     $ clip < ~/.ssh/id_rsa.pub
 
 5. 将复制的内容黏贴到github.com上的账户中的Setting中的SSH Keys中
 
 6. 测试连接
 
     $ ssh -T git@github.com # github账号




### 克隆仓库与更新仓库
1. 克隆仓库到本地：

    $ cd path # 进入你想创建克隆仓库的目录
    $ git clone GitURL # 克隆仓库,例如git clone https://github.com/freeape/hello-world.git

2. 本地修改后上传至服务器

    $ git status # 查看本地当前工作仓库与历史版本的文件差异
    $ git add filepath # 添加某个更改文件到缓存区 # or $ git add. # or $ git add -A 添加所有文件更改到缓存区
    $ git commit -m "change info" # 提交版本
    $ git push origin master # 更新本地版本至服务器

## 搜索引擎：Google
使用指南：待补充


## 安装管理程序：Anaconda

### 配置不同版本的Python环境

    $ conda create --name py36 python=3.6 anaconda # 后缀annaconda可以为环境安装各种常用包