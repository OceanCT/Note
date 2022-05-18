# 今日内容

	1. 概念
    2. 步骤
    3. 执行原理
    4. 生命周期
    5. Servlet3.0 注解配置
    6. Servlet的体系结构



# Servlet：  server applet
	* 概念：运行在服务器端的小程序
		* Servlet就是一个接口，定义了Java类被浏览器访问到(tomcat识别)的规则。
		* 将来我们自定义一个类，实现Servlet接口，复写方法。


	* 快速入门：
		1. 创建JavaEE项目
		2. 定义一个类，实现Servlet接口
			* public class ServletDemo1 implements Servlet
		3. 实现接口中的抽象方法
		4. 配置Servlet
			 在web.xml中配置：
		    <!--配置Servlet -->
		    <servlet>
		        <servlet-name>demo1</servlet-name>
		        <servlet-class>ServletDemo1</servlet-class>
		    </servlet>
		
		    <servlet-mapping>
		        <servlet-name>demo1</servlet-name>
		        <url-pattern>/demo1</url-pattern>
		    </servlet-mapping>

	* 执行原理：
		1. 当服务器接受到客户端浏览器的请求后，会解析请求URL路径，获取访问的Servlet的资源路径
		2. 查找web.xml文件，是否有对应的<url-pattern>标签体内容。
		3. 如果有，则在找到对应的<servlet-class>全类名
		4. tomcat会将字节码文件加载进内存，并且创建其对象
		5. 调用其方法

	* Servlet中的生命周期方法：
		1. 被创建：执行init方法，只执行一次
			* Servlet什么时候被创建？
				* 默认情况下，第一次被访问时，Servlet被创建
				* 可以配置执行Servlet的创建时机。
					* 在<servlet>标签下配置
						1. 第一次被访问时，创建
	                		* <load-on-startup>的值为负数
			            2. 在服务器启动时，创建
			                * <load-on-startup>的值为0或正整数


			* Servlet的init方法，只执行一次，说明一个Servlet在内存中只存在一个对象，Servlet是单例的
				* 多个用户同时访问时，可能存在线程安全问题。
				* 解决：尽量不要在Servlet中定义成员变量。即使定义了成员变量，也不要对修改值

		2. 提供服务：执行service方法，执行多次
			* 每次访问Servlet时，Service方法都会被调用一次。
		3. 被销毁：执行destroy方法，只执行一次
			* Servlet被销毁时执行。服务器关闭时，Servlet被销毁
			* 只有服务器正常关闭时，才会执行destroy方法。
			* destroy方法在Servlet被销毁之前执行，一般用于释放资源

	* Servlet3.0：
		* 好处：
			* 支持注解配置。可以不需要web.xml了。

		* 步骤：
			1. 创建JavaEE项目，选择Servlet的版本3.0以上，可以不创建web.xml
			2. 定义一个类，实现Servlet接口
			3. 复写方法
			4. 在类上使用@WebServlet注解，进行配置
				* @WebServlet("资源路径")


				@Target({ElementType.TYPE})
				@Retention(RetentionPolicy.RUNTIME)
				@Documented
				public @interface WebServlet {
				    String name() default "";//相当于<Servlet-name>
				
				    String[] value() default {};//代表urlPatterns()属性配置
				
				    String[] urlPatterns() default {};//相当于<url-pattern>
				
				    int loadOnStartup() default -1;//相当于<load-on-startup>
				
				    WebInitParam[] initParams() default {};
				
				    boolean asyncSupported() default false;
				
				    String smallIcon() default "";
				
				    String largeIcon() default "";
				
				    String description() default "";
				
				    String displayName() default "";
				}


##6. Servlet的体系结构
   Servlet -- 接口
   |
   GenericServlet -- 抽象类
   |
   HttpServlet  -- 抽象类

    * GenericServlet：将Servlet接口中其他的方法做了默认空实现，只将service()方法作为抽象
        * 将来定义Servlet类时，可以继承GenericServlet，实现service()方法即可

    * HttpServlet：对http协议的一种封装，简化操作
        1. 定义类继承HttpServlet
        2. 复写doGet/doPost方法



#http
* 概念：Hyper Text Transfer Protocol 超文本传输协议
   * 传输协议：定义了，客户端和服务器端通信时，发送数据的格式
   * 特点：
      1. 基于TCP/IP的高级协议
      2. 默认端口号:80
      3. 基于请求/响应模型的:一次请求对应一次响应
      4. 无状态的：每次请求之间相互独立，不能交互数据

   * 历史版本：
      * 1.0：每一次请求响应都会建立新的连接
      * 1.1：复用连接

* 请求消息数据格式
   1. 请求行
      请求方式 请求url 请求协议/版本
      GET /login.html	HTTP/1.1

      * 请求方式：
         * HTTP协议有7中请求方式，常用的有2种
            * GET：
               1. 请求参数在请求行中，在url后。
               2. 请求的url长度有限制的
               3. 不太安全
            * POST：
               1. 请求参数在请求体中
               2. 请求的url长度没有限制的
               3. 相对安全
   2. 请求头：客户端浏览器告诉服务器一些信息
      请求头名称: 请求头值
      * 常见的请求头：
         1. User-Agent：浏览器告诉服务器，我访问你使用的浏览器版本信息
            * 可以在服务器端获取该头的信息，解决浏览器的兼容性问题

         2. Referer：http://localhost/login.html
            * 告诉服务器，我(当前请求)从哪里来？
               * 作用：
                  1. 防盗链：
                  2. 统计工作：
   3. 请求空行
      空行，就是用于分割POST请求的请求头，和请求体的。
   4. 请求体(正文)：
      * 封装POST请求消息的请求参数的

   * 字符串格式：
     POST /login.html	HTTP/1.1
     Host: localhost
     User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0
     Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
     Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
     Accept-Encoding: gzip, deflate
     Referer: http://localhost/login.html
     Connection: keep-alive
     Upgrade-Insecure-Requests: 1

     username=zhangsan	


* 响应消息：服务器端发送给客户端的数据
    * 数据格式：
        1. 响应行
            1. 组成：协议/版本 响应状态码 状态码描述
            2. 响应状态码：服务器告诉客户端浏览器本次请求和响应的一个状态。
                1. 状态码都是3位数字
                2. 分类：
                    1. 1xx：服务器就收客户端消息，但没有接受完成，等待一段时间后，发送1xx多状态码
                    2. 2xx：成功。代表：200
                    3. 3xx：重定向。代表：302(重定向)，304(访问缓存)
                    4. 4xx：客户端错误。
                        * 代表：
                            * 404（请求路径没有对应的资源）
                            * 405：请求方式没有对应的doXxx方法
                    5. 5xx：服务器端错误。代表：500(服务器内部出现异常)


        2. 响应头：
           1. 格式：头名称： 值
           2. 常见的响应头：
           1. Content-Type：服务器告诉客户端本次响应体数据格式以及编码格式
           2. Content-disposition：服务器告诉客户端以什么格式打开响应体数据
           * 值：
           * in-line:默认值,在当前页面内打开
           * attachment;filename=xxx：以附件形式打开响应体。文件下载
           3. 响应空行
           4. 响应体:传输的数据


	* 响应字符串格式
		HTTP/1.1 200 OK
		Content-Type: text/html;charset=UTF-8
		Content-Length: 101
		Date: Wed, 06 Jun 2018 07:08:42 GMT

		<html>
		  <head>
		    <title>$Title$</title>
		  </head>
		  <body>
		  hello , response
		  </body>
		</html>