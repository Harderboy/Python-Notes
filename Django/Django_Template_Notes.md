# Django Template

## Django 模板标签

- 定义模板

  - 变量
    - 视图传递给模板的数据
    - 遵守标识符规则
    - 模板语法

        ```html
        view：{"HTML变量名" : "views变量名"}
        HTML：{{变量名}}
        ```

        注意：使用的变量不存在，则插入的是空字符串
    - 在模板中使用点语法：`{{stu.sname}}`
      - 字典查询（先按字典查询）
      - 属性或方法
      - 数字索引

    - 在模板中调用对象的方法
      - 注意：不成传递参数，下面这种写法是错误的

      ```python
      def getName(self,str):
          return self.sname + str
      ```

  - 标签
    - 语法：{% tag %}
    - 作用：
      - 输出中创建模板
      - 控制逻辑和循环

    - if

      格式：

        ```html
        {% if condition %}
            ... display
        {% endif %}

        或者

        {% if condition %}
            ... display 1
        {% else %}
            ... display 2
        {% endif %}

        或者

        {% if condition1 %}
            ... display 1
        {% elif condition2 %}
            ... display 2
        {% else %}
            ... display 3
        {% endif %}
        ```

      - {% if %} 标签接受 and ， or 或者 not 关键字来对多个变量做判断 ，或者对变量取反（ not )

    - for

      格式：

        ```html
        <!-- Y 是要迭代的序列而 X 是在每一个特定的循环中使用的变量名称 -->

        {% for X in Y %}
            语句1
        {% endfor %}
        
        或者

        {% for X in Y %}
            语句1
        <!-- 序列 Y 为空或者序列不存在，循环为空时（即 in 后面的参数布尔值为 False ）执行语句2，可选的 -->
        {% empty %}  
            语句2
        {% endfor %}

        <!-- 在 {% for %} 标签里可以通过 {{forloop}} 变量获取循环序号 -->
        {{forloop.counter}}

        ```

      示例：

        ```html
        <body>
            <h1>学生信息列表</h1>
            <ul>
                    {% for student in studentss %}
                    <li>
                        {{forloop.counter}}--{{student.sname}}--{{student.scontent}}--{{student.sgrade}}
                    </li>
                    {% empty %}
                        <h3>目前没有学生</h3>
                    {% endfor %}
            </ul>

        </body>
        ```

    - comment
      - 注释多行

        ```html
        {% comment %}
            <h1>comment测试</h1>
            <h1>comment语法</h1>
            {{stu.sname}}
        {% endcomment%}
        ```

      - 单行注释：`{# #}`
        `{# 这是一个注释 #}`

    - ifequal、ifnotequal
      - 作用：判断是否相等或者不相等
      - 格式：

        ```html
        {% ifequal 值1 值2 %}
            <!-- 值1和值2相等时执行下面语句 -->
            <h1>Welcome!</h1>
        {% endifequal %}

        <!-- 和 {% if %} 类似， {% ifequal %} 支持可选的 {% else %} 标签 -->

        {% ifequal section 'sitenews' %}
            <h1>Site News</h1>
        {% else %}
            <h1>No News Here</h1>
        {% endifequal %}

        ```

      - 示例：

        ```html
        {% ifequal 'sunck' 'sunck' %}
            <!-- 值1和值2相等时执行下面语句 -->
            <h1>Welcome!</h1>
        {% endifequal %}

        {% ifnotequal 'sunck' 'kai' %}
            <!-- 值1和值2相等时执行下面语句 -->
            <h1>Not welcome!</h1>
        {% endifnotequal %}
        ```

    - include
      - 作用：加载模板并以标签内的参数渲染
      - 格式：`{% include '模板目录' 参数1 参数2 %}`
    - url
      - 作用：反向解析
      - 在 templates 模板的 HTML 文件中使用名称空间，语法格式如下：`{% url'namespace' p1 p2 %}`
      `{% url "app名称：路由别名" 参数1 参数n %}`

        ```python

        # 新版本django，须在对应app目录下的url.py文件中添加一行代码：app_name = 'app'（自定义app名称），这种方法来命名app
        app_name = 'app'
        urlpatterns = [ url(r'^good/(\d+)/(\d+)$', views.good, name="good"),]

        # 定义视图函数，传递两个参数
        def good(request, num1, num2):
            return render(request, 'myApp/good.html', {'num1': num1, 'num2': num2})
        
        # 在 templates 模板的 HTML 文件中使用名称空间，链接指定url
        <a href="{% url 'app:good' 123 456%}">链接2</a>

        # 使用传递的参数值
        <h1>good--{{num1}}--{{num2}}</h1>
        ```

    - csrf_token
      - 作用：用于跨站请求伪造保护
      - 格式：`{% csrf_token %}`
    - block、extends
      - 作用：用于模板继承
    - autoescape
      - 作用：用于 HTML 转义

  - 过滤器
    - 语法：`{{var|过滤器}}`，过滤器使用管道字符
    - 作用：模板过滤器可以在变量被显示前修改它
    - lower：内置函数
    - upper：`<h2>{{str|upper}}</h2>`
    - 过滤器可以传递参数，参数用引号引起来
      - `join`：`{{序列|join:''}}`
    - 如果变量没有被提供，或者值为 false、空，可以使用默认值
      - default
        - 格式：`{{var|default:''}}`
        - 示例：`{{test|default:'没有'}}`
    - 根据给定格式转换日期为字符串
      - date
        - 格式：`{{datevat|date:'y-m-d'}}`
    - HTML 转义：escape
    - 加减乘除
      - 示例：

        ```html
        <h2>{{num}}</h2>
        <h2>{{num|add:10}}</h2>
        <h2>{{num|add:-10}}</h2>

        <!-- 标签 -->
        <!-- num/1*5 -->
        <!-- num*5 -->
        <h2>{% widthratio num 1 5%}</h2>
        <!-- num/5 -->
        <h2>{% widthratio num 5 1%}</h2>
        ```

  - 注释
    - 单行注释
    - 多行注释
    - 同上

  - 反向解析见上

  - 模板继承
    - 作用：模板继承可以减少页面的内容的重复定义，实现页面的复用
    - block标签：在父模板预留区域，子模版去填充
      - 语法：

        ```html
        {% block 标签名1 %}

        {% endblock 标签名1 %}

        {% block 标签名2 %}

        {% endblock 标签名2 %}

        ```

    - extends标签：继承模板，将继承模板文件写在第一行
      - 语法：`{% extends '父模板路径' %}`
    - 示例
      - 定义父模板
      - 定义子模版
      - 继承模板

        ```html
        {% extends 'myApp/base.html' %}

        {% block main %}
            <h1>sunck is nice man</h1>
        {% endblock main %}

        {% block main2 %}
            <h1>htomato is nice man</h1>
        {% endblock main2 %}
        ```

  - HTML 转义
    - 将接收到的字符串当成 HTML 代码渲染

      ```python

      def getstudent(request):
          student = Students.stuObject2.get(pk=1)
          return render(request, 'myApp/index2.html', {'stu': student, 'num': 10, 'str': 'sunck is good man', 'list': ['sunck', 'good', 'man'], 'test': False, 'code': '<h2>sunck is good!</h2>'})

      {{code}}
      # 当成普通字符串，不转义
      {{code|escape}}

      # 两种方式
      # 方式1
      {{code|safe}}
      # 方式2
      # off为关闭禁止转义  on为开启禁止转义
      {% autoescape off%}
      {{code}}
      {% endautoescape %}
      ```

  - CSRF：跨站请求伪造
  某些恶意的网站，包含链接、表单、按钮，利用登录用户在浏览器中认证，从而攻击服务。

    - 防止 CSRF
      - `settings.py` 的 `MIDDLEWARE` 添加

        `MIDDLEWARE = ['django.middleware.csrf.CsrfViewMiddleware',]`  连自己也防

      - `{% csrf_token %}` 前提：开启了 `MIDDLEWARE = ['django.middleware.csrf.CsrfViewMiddleware',]`
        - 需要隐藏起来

      - 没有绝对的安全，如果拿到了 `{% csrf_token %}` 的值也可能导致 CSRF

      - 实例文件：`postfile.html`、`showinfo.html`

  - 验证码
    - 在用户注册、登录页面的时候使用，为了防止暴力请求，减轻服务器的压力
    - 防止 csrf 的一种方式