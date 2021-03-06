#今日内容
* 1.HTML简介
* 2.排版标签
* 3.文本格式化标签
* 4.语义化标签
* 5.图片标签    
* 6.列表标签    
* 7.链接标签  
* 8.表格标签
* 9.表单标签

# 1. HTML简介

## 1.1 定义 
- HTML 指的是超文本标记语言 (**H**yper **T**ext **M**arkup **L**anguage)是用来描述网页的一种语言。
	- HTML 不是一种编程语言，而是一种**标记语言 (markup language)**
	- 标记语言是一套标记标签 (markup tag)
- 所谓超文本，有2层含义 
	1. 因为它可以加入图片、声音、动画、多媒体等内容（**超越文本限制**）
	2. 不仅如此，它还可以从一个文件跳转到另一个文件，与世界各地主机的文件连接（**超级链接文本**）。
	
## 1.2 语法

	<!DOCTYPE html>
	<html lang="en">
		<head>
			<meta charset="UTF-8">
			<title>Title</title>
		</head>
		<body>	
		</body>
	</html>

1. html文档后缀名 .html 或者 .htm
2. 标签分为		
	*  注释标签 <!-- 注释内容 -->
	*  双标签：有开始标签和结束标签，如 <html> </html>。
	*  单标签：空元素。开始标签和结束标签在一起。如 <br/>
3. 标签可以嵌套：  
	* 要正确嵌套，不能你中有我，我中有你
	* 错误：`<a><b></a></b>`
	* 正确：`<a><b></b></a>`
4. 在开始标签中可以定义属性。属性是由键值对构成，值需要用引号(单双都可)引起来
5. html的标签不区分大小写，但是建议使用小写。

## 1.3 html基本标签

* `<!DOCTYPE html>`
	* `<!DOCTYPE>`声明必须是 HTML 文档的第一行，位于<html> 标签之前。
	* `<!DOCTYPE>`声明不是 HTML 标签，是一条指令，它用于向浏览器说明当前文档使用哪种HTML标准规范，包括HTML版本和类型，这样浏览器将按指定的文档类型进行解析。
	* `<!DOCTYPE>`声明和浏览器的兼容性相关。<!DOCTYPE>声明被删除后，如何展示HTML页面的权利就交给了浏览器，即页面的显示效果由浏览器决定。   

* `<html lang="en">`
	* html文档的根标签, <html>标签标志着HTML文档的开始，</html>标签则标志着HTML文档的结束
	* lang = "en", lang属性指定html 语言种类，即，该html标签内的内容，所用语言为英文。
		* zh-CN 中文
		* en  英文

* `<head> </head>头标签`。
	* 用于指定html文档的一些属性。
	* 引入外部的资源
	* `<meta charset="UTF-8">` 单标签，charset表示该html文件，以"utf-8"编码保存。
		* utf-8是目前最常用的字符集编码方式，常用的字符集编码方式还有gbk和gb2312。
		* gb2312 简单中文  包括6763个汉字  GUO BIAO
		* BIG5   繁体中文 港澳台等用
		* GBK包含全部中文字符    是GB2312的扩展，加入对繁体字的支持，兼容GB2312
		* UTF-8则基本包含全世界所有国家需要用到的字符
	* title：标题标签。

* `<body> </body>`：体标签
	* 用于定义HTML文档所要显示的内容，也被称为主体标签。
	* 浏览器中显示的所有文本、图像、音频和视频等信息都必须位于<body>标签内，才能最终展示给用户。
  	* 需要注意的是，一个HTML文档只能含有一对<body>标签，且<body>标签必须在<html>标签内，位于<head>标签之后，与<head>标签是并列关系。

# 2. 排版标签

## 2.1 标题标签 `<h1> to <h6>`
	* h1~h6:字体大小逐渐递减
## 2.2 段落标签 `<p></p>`
## 2.3 换行标签 `<br>`
## 2.4 水平线 `<hr>` 
* 展示一条水平线
* 属性：
  * color：颜色
  * width：宽度
  * size：高度
  * align：对其方式
  * center：居中
  * left：左对齐
  * right：右对齐
## 2.5 div和span
 * div和span 是没有语义的，是网页布局主要的2个盒子
	 * div 就是 “division”  的缩写分割， 分区的意思  其实有很多div 来组合网页。
	 * span 跨度，跨距；范围的意思
* div标签：用来布局的，但是现在一行只能放一个div
* span标签：用来布局的，一行上可以放好多个span

## 2.5 排版标签总结

| 标签名        | 定义       | 说明                                  |
| ------------- | :--------- | :------------------------------------ |
| `<hx></hx>`     | 标题标签   | 作为标题使用，并且依据重要性递减      |
| `<p></p>  `     | 段落标签   | 可以把 HTML 文档分割为若干段落        |
| `<hr />  `      | 水平线标签 | 没啥可说的，就是一条线                |
| `<br /> `       | 换行标签   |                                       |
| `<div></div>`   | div标签    | 用来布局的，但是现在一行只能放一个div |
|` <span></span>` | span标签   | 用来布局的，一行上可以放好多个span    |

# 3. 文本格式化标签	

* 字体加粗: `<b>`和`<Strong>`
* 字体斜体:`<i>`和`<em>`
* 文字加删除线：`<s>`和`<del>`
* 文字加下划线：`<u>`和`<ins>`

四组标签中，后者带有语义，例如Strong 除了可以加粗还有 强调的意思，语义更强烈

# 4. 语义化标签介绍

* 含义：在HTML中，语义化标签就是指这个标签本身直观表达出了它所包含的内容是什么。
* 好处
	* 代码结构得到了优化，即使没有css，也能呈现出完整、清晰的结构，更加方便阅读和理解，同时提高了团队合作的效率
	* 有利于搜索引擎的优化，爬虫依赖标签确定关键字的权重，可以帮助爬虫爬出更多有效信息
	* 方便其他设备解析（如屏幕阅读器、盲人阅读器、移动设备）以语义的方式来渲染网页	
* 常见的语义化标签
	*  < h1>~< h6>标签：标题标签，h1等级最高，h6等级最低
	*  header元素：用于定义页面的介绍展示区域，通常包括网站logo、主导航、全站链接以及搜索框
	*  footer元素：文档的底部信息
	*  strong元素：用于强调文本
	*  nav元素：定义页面的导航链接部分区域
	*  main元素：定义页面的主要内容，一个页面只能使用一次。
	*  article元素：定义页面独立的内容，它可以有自己的header、footer、sections等
	*  section元素：元素用于标记文档的各个部分，例如长表单文章的章节或主要部分
	*  aside元素：一般用于侧边栏	
	*  small元素：呈现小号字体效果

# 5. 图像标签：

## 5.1 img标签
* 属性：
	* src：指定图片的位置
	* alt: 图像不能显示时的替换文本
	* title：鼠标悬停时显示的内容
	* width：设置图像的宽度
	* height：设置图像的高度
	* border：设置图像边框的宽度
## 5.2 路径问题
* 相对路径
	* 同一级路径“ ”：只需输入图像文件的名称即可，如`<img src="baidu.gif" />`
	* 下一级路径“/”：图像文件位于HTML文件同级文件夹下（例如文件夹名称为：images），如`<img src="images/baidu.gif" />`
	* 上级路径：在文件名之前加入“../” ，如果是上两级，则需要使用 “../ ../”，以此类推，如`<img src="../images/baidu.gif" />`
	
* 绝对路径
	* 绝对路径以Web站点根目录为参考基础的目录路径。之所以称为绝对，意指当所有网页引用同一个文件时，所使用的路径都是一样的。
	* “D:\web\img\logo.gif”，或完整的网络地址，例如“http://www.itcast.cn/images/logo.gif”。

**注意：**
绝对路径用的较少，我们理解下就可以了。  但是要注意，它的写法 特别是符号  \  并不是 相对路径的   /


#6. 链接标签：
* 标签`<a>` : anchor 的缩写  [ˈæŋkə(r)] ,定义一个超链接
* 语法格式  

 		`<a href="跳转目标" target="目标窗口的弹出方式">文本或图像</a>` 
* 属性：
	* href：指定访问资源的URL(统一资源定位符)
	* target：指定打开资源的方式
		* _self:默认值，在当前页面打开
		* _blank：在空白页面打开
* 注意：
	1. 外部链接 需要添加 http:// www.baidu.com
	2. 内部链接 直接链接内部页面名称即可 比如 < a href="index.html"> 首页 </a >
	3. 如果当时没有确定链接目标时，通常将链接标签的href属性值定义为“#”(即href="#")，表示该链接暂时为一个空链接。
	4. 不仅可以创建文本超链接，在网页中各种网页元素，如图像、表格、音频、视频等都可以添加超链接。

#7. 表格标签：
## 7.1 表格 Table的作用
  现在还是较为常用的一种标签，但不是用来布局，**常见显示、展示表格式数据。**
	* 数据显示的非常的规整，可读性非常好
	* **特别是后台展示数据的时候表格运用是否熟练就显得很重要**，一个清爽简约的表格能够把繁杂的数据表现得很有条理，虽然 div 布局也可以做到，但是总没有表格来得方便。
	* 表格的示意图  
	  ![表格的示意图]('./media/07table基本结构.jpg')	  

## 7.2 表格的基本语法
* table：定义表格
	* width：宽度
	* border：边框
	* cellpadding：定义内容和单元格的距离
	* cellspacing：定义单元格之间的距离。如果指定为0，则单元格的线会合为一条、
	* bgcolor：背景色
	* align：对齐方式
* tr：定义行，必须嵌套在 table标签中。
	* bgcolor：背景色
	* align：对齐方式
* td：定义单元格，必须嵌套在`<tr></tr>`标签中。
	* colspan：合并列
	* rowspan：合并行
	* th：定义表头单元格
	* `<caption>`：表格标题
	* `<thead>`：表示表格的头部分
	* `<tbody>`：表示表格的体部分
	* `<tfoot>`：表示表格的脚部分
	* 表格属性 <img src='./media/07table基本结构.jpg'>
## 7.3 合并单元格的两种方式

* 跨行合并：row，行。rowspan="合并单元格的个数"
* 跨列合并：column，列。colspan="合并单元格的个数"
  
* 合并效果图见 <img src='./media/08table合并单元格.jpg'>
* 合并单元格顺序
	* 与汉字的书写顺序一样：按照   先上 后下     先左  后右 的顺序
* 合并单元格三步曲
	1. 先确定是跨行还是跨列合并
	2. 根据 先上 后下   先左  后右的原则找到目标单元格    然后写上 合并方式 还有 要合并的单元格数量  比如 ： <td colspan="3">   </td>
	3. 删除多余的单元格 单元格
	
## 7.4 复杂的表格
* 对于比较复杂的表格，表格的结构也就相对的复杂了，所以又将表格分割成三个部分：题头、正文和脚注。而这三部分分别用:thead,tbody,tfoot来标注， 这样更好的分清表格结构

**注意：**   
	1.  `<thead></thead>`：用于定义表格的头部。用来放标题之类的东西。<thead> 内部必须拥有 <tr> 标签！   
	2. `<tbody></tbody>`：用于定义表格的主体。放数据本体 。   
	3. `<tfoot></tfoot>`:放表格的脚注之类。   
	4. 以上标签都是放到table标签中。

| 标签名              | 定义           | 说明                                         |
| ------------------- | :------------- | :------------------------------------------- |
| `<table></table>`     | 表格标签       | 就是一个四方的盒子                           |
| `<tr></tr>   `        | 表格行标签     | 行标签要再table标签内部才有意义              |
| `<td></td>  `         | 单元格标签     | 单元格标签是个容器级元素，可以放任何东西     |
| `<th></th> `          | 表头单元格标签 | 它还是一个单元格，但是里面的文字会居中且加粗 |
|` <caption></caption>` | 表格标题标签   | 表格的标题，跟着表格一起走，和表格居中对齐   |
| `clospan 和 rowspan`  | 合并属性       | 用来合并单元格的                             |

# 8. 列表标签：

* 概念：容器里面装载着结构，样式一致的文字或图表的一种形式，叫列表
* 特点：列表最大的特点就是  整齐 、整洁、 有序，跟表格类似，但是他可组合自由度会更高。  
* 作用：表格是用来显示数据的，那么列表就是用来布局的。 因为非常整齐和自由

## 8.1无序列表：

无序列表的各个列表项之间没有顺序级别之分，是并列的。其基本语法格式如下：

	<ul>
	  <li>列表项1</li>
	  <li>列表项2</li>
	  <li>列表项3</li>
	  ......
	</ul>

**注意**

	i. <ul></ul>中只能嵌套<li></li>，直接在<ul></ul>标签中输入其他标签或者文字的做法是不被允许的。
	ii. <li>与</li>之间相当于一个容器，可以容纳所有元素。
	iii. 无序列表会带有自己样式属性，放下那个样式，一会让CSS来！

## 8.2 有序列表：
有序列表即为有排列顺序的列表，其各个列表项按照一定的顺序排列定义，有序列表的基本语法格式如下：

	<ol>
	  <li>列表项1</li>
	  <li>列表项2</li>
	  <li>列表项3</li>
	  ......
	</ol>


## 8.3 定义列表
定义列表常用于对术语或名词进行解释和描述，定义列表的列表项前没有任何项目符号。其基本语法如下：

	<dl>
	  <dt>名词1</dt>
	  <dd>名词1解释1</dd>
	  <dd>名词1解释2</dd>
	  ...
	  <dt>名词2</dt>
	  <dd>名词2解释1</dd>
	  <dd>名词2解释2</dd>
	  ...
	</dl>


# 9. 表单：

* 概念：用于采集用户输入的数据的。用于和服务器进行交互。
* form：用于定义表单的。可以定义一个范围，范围代表采集用户数据的范围   
	* 表单域 `<img src="media/bd.png" />`


## 9.1 表单项标签

### 9.1.1 input
可以通过type属性值，改变元素展示的样式。type属性如下：
* text：文本输入框，默认值
	* placeholder：指定输入框的提示信息，当输入框的内容发生变化，会自动清空提示信息	
* password：密码输入框
* radio:单选框
	* 注意：
		1. 要想让多个单选框实现单选的效果，则多个单选框的name属性值必须一样。
		2. 一般会给每一个单选框提供value属性，指定其被选中后提交的值
		3. checked属性，可以指定默认值
* checkbox：复选框
	* 注意：
		1. 一般会给每一个单选框提供value属性，指定其被选中后提交的值
		2. checked属性，可以指定默认值

* file：文件选择框
* hidden：隐藏域，用于提交一些信息。
* 按钮：
	* submit：提交按钮。可以提交表单
	* button：普通按钮
	* image：图片提交按钮
		* src属性指定图片的路径	

### 9.1.2 label：指定输入项的文字描述信息
* label标签为 input 元素定义标注；
* label标签主要目的是为了提高用户体验。 为用户提高最优秀的服务。
* 用于绑定一个表单元素, 当点击label标签的时候, 被绑定的表单元素就会获得输入焦点。
* 注意：
	* label的for属性一般会和 input 的 id属性值 对应。如果对应了，则点击label区域，会让input输入框获取焦点。

### 9.1.3 select: 下拉列表
* 子元素：option，指定列表项	

### 9.1.4 textarea：文本域

* cols：指定列数，每一行有多少个字符
* rows：默认多少行。
* cols="每行中的字符数" rows="显示的行数"  我们实际开发不用

## 9.2 form表单域
* action：指定提交数据的URL
* method:指定提交方式，一共7种，2种比较常用
	* get：
		1. 请求参数会在地址栏中显示。会封装到请求行中(HTTP协议后讲解)。
		2. 请求参数大小是有限制的。
		3. 不太安全。
	* post：
		1. 请求参数不会再地址栏中显示。会封装在请求体中(HTTP协议后讲解)
		2. 请求参数的大小没有限制。
		3. 较为安全。

* 表单项中的数据要想被提交：必须指定其name属性
