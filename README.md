# 基于scrapy框架爬取腾讯社会招聘职位信息
## 本项目是一个用Python语言编写的爬虫，通过Windows控制台运行选择爬取，爬取腾讯招聘网的招聘信息，保存到数据库中，再运行一次选择展示，将前边爬取下来的数据，运用数据库查询语句从数据库中提取到控制台并显示出来
<br><br>
### 下边就是我们要爬取的腾讯招聘网
![](https://github.com/dafeizhu/python-spider-scrapy/blob/master/images/Tencent腾讯招聘网.png)
<br><br>
## Srcapy框架介绍
### 开发技术：python<br>
### 主要特点：速度快、层次高<br>
### 主要功能：从屏幕抓取数据、通过访问API提取数据<br>
### 主要使用领域：数据挖掘、信息处理、历史记录打包等
<br><br>
## 项目介绍
### 第一步：通过网络爬虫访问腾讯招聘网<br>
### 第二步：爬取招聘网站全部招聘信息<br>
### 第三步：将爬取的数据存入数据库<br>
### 第四步：根据筛选条件进一步得到所需数据
<br><br>
## 相关代码介绍
### Scrapy框架内控制爬虫
![](https://github.com/dafeizhu/python-spider-scrapy/blob/master/images/Scrapy框架内控制爬虫.JPG)
<br><br>
### 使用CSS提取器和Xpath确定参数属性提取数据
![](https://github.com/dafeizhu/python-spider-scrapy/blob/master/images/使用CSS提取器和Xpath确定参数属性提取数据.JPG)
<br><br>
### 将数据传到数据库
![](https://github.com/dafeizhu/python-spider-scrapy/blob/master/images/将数据传到数据库.JPG)
<br><br>
## 下边为控制台的运行截图
### 如下，选择1操作，开始进行爬取网页内容
![](https://github.com/dafeizhu/python-spider-scrapy/blob/master/images/运行截图1.PNG)
<br><br>
### 再爬取结束或者Ctrl+c强制结束后，再次运行，选择2，输出相关筛选信息
![](https://github.com/dafeizhu/python-spider-scrapy/blob/master/images/运行截图2.PNG)
<br><br><br><br>
## 本项目为本人在校期间，自学Python的爬虫后，做出来的一个小项目，可惜的是本项目并没有一个前端页面来展示爬取到的数据，而只是通过控制台来显示，效果欠佳，除了该项目，还有一个是爬取链家租房网的类似的爬虫项目，后续会上传上来，该项目仅供学习参考。
## 如想继续完善本项目，可以通过自学djnago框架，去做出一个前端展示页面来，并将项目发布至个人服务器中，这样该项目就可以做到真正模拟腾讯招聘网
