# Get My Course of SUSTech

基于Selenium for Python的快速一键退/选课脚本
部分代码由BabyXinORZ提供, 链接: https://github.com/BabyXinORZ/SUSTech-2019Autumn-course_selector

如果不会使用或配置环境或者出现问题可直接联系QQ2433988494

| 版本号 |
| ------ |
| v1.0.0 |



## 环境要求

| Python版本 | 3.*                |
| ---------- | ------------------ |
| Python模块 | selenium, requests |
| 系统要求   | Win32/64           |



## 开始



###  1. 安装Python, 配置环境变量

###  2. 在Python环境配置好的情况下, 使用下列命令安装模块

```shell
pip install requests
pip install selenium
```

###  3. 安装Chrome

###  4. 安装Chrome Driver 

#### Win
可在[链接](http://npm.taobao.org/mirrors/chromedriver)中下载Chrome版本对应的chromedriver.exe放在Python安装目录文件夹下的Scripts文件夹下

#### Linux
以Ubuntu为例

> 一、安装Chrome浏览器
> 1、安装依赖
>
> ```shell
> sudo apt-get install libxss1 libappindicator1 libindicator7
> ```
>
> 2、下载Chrome安装包
>
> ```shell
> wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
> ```
>
> 3、安装
>
> ```shell
> sudo dpkg -i google-chrome*.deb
> sudo apt-get install -f
> ```
>
> 二、安装ChromeDriver
> 1、安装xvfb以便我们可以无头奔跑地运行Chrome
>
> ```shell
> sudo apt-get install xvfb
> ```
>
> 2、安装依赖
>
> ```shell
> sudo apt-get install unzip
> ```
>
> 3、下载安装包
>
> ```shell
> wget -N http://chromedriver.storage.googleapis.com/2.26/chromedriver_linux64.zip
> ```
>
> 4、解压缩+添加执行权限
>
> ```shell
> unzip chromedriver_linux64.zip
> ```
>
> 5、移动
>
> ```shell
> sudo mv -f chromedriver /usr/local/share/chromedriver
> ```
>
> 6、建立软连接
>
> ```shell
> sudo ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver
> sudo ln -s /usr/local/share/chromedriver /usr/bin/chromedriver
> ```
>
> 三、无头运行Chrome
> 1、安装Python依赖
>
> ```shell
> pip3 install pyvirtualdisplay
> ```
> 四、完成

###  5. 开始测试脚本吧



## 使用脚本开始
待添加

## 用法

请使用```python  Gmcs.py help获取帮助```
