## jemmy-s_blog项目
#### 一、项目结构
![项目结构](http://p9doppo4j.bkt.clouddn.com/%E5%AF%BC%E5%9B%BE.png)
#### 二、不足与改进
1. 评论功能没有设置回复
  <br>思路：重新设计comment模型结构，采取树状结构上实现评论的回复
2. 博客详情页面中，博客内容采用markdown格式编辑，但是页面采用JS渲染，效果不是很好，这可能是因为我后台使用马克飞象编写，前台使用django-markdown，二者在一些语法处理上有细微差别
  <br>解决思路：前后台统一使用django-markdown编辑；在后台渲染好之后传回
