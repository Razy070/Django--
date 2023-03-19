# word = input()
# if str(word) == str(word)[::-1] :
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# word = input()
# if str(word) == "".join(reversed(word)) :
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# function which return reverse of a string

# def isPalindrome(s):
# 	return s == s[::-1]
#
#
# s = "malayalam"
# ans = isPalindrome(s)
#
# if ans:
# 	print("Yes")
# else:
# 	print("No")

#####################################################
# arr = [1, 2, 2, 3, 3, 3]
# tmp = {}
# res = set()
# for i in arr:
#     tmp[i] = tmp.get(i, 0) + 1
#     res.add(i if tmp[i] < 2 else str(i) * tmp[i])
# print(*res)


# в общем html файл с добавлением постов будет выглядить так
# <!DOCTYPE html>
# <html lang="ru">
#     <head>
#         <meta charset="utf-8" />
#         <title>MyBlog</title>
#         <link href="{{STATIC_URL}}bootstrap/css/bootstrap.css" rel="stylesheet">
#         <style>
#             body {
#                 padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
#             }
#         </style>
#         <link href="{{STATIC_URL}}bootstrap/css/bootstrap-responsive.css" rel="stylesheet">
#         <!--[if lt IE 9]>
#         <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
#         <![endif]-->
#         <script src="{{STATIC_URL}}bootstrap/js/bootstrap.js" type="text/javascript"></script>
#         {% block extrahead %}
#         {% endblock %}
#         <script type="text/javascript">
#         $(function(){
#         {% block jquery %}
#         {% endblock %}
#         });
#         </script>
#     </head>
# <body>
#
# <div class="navbar navbar-inverse navbar-fixed-top">
#     <div class="navbar-inner">
#         <div class="container">
#             <div class="brand">My Blog</div>
#             <ul class="nav">
#                 <li><a href="{% url 'list' %}" class="">Список постов</a></li>
#             </ul>
#         </div>
#     </div>
#
# </div>
#
# <div class="container">
#      {% block content %}Empty page{% endblock %}
# </div> <!-- container -->
#
# </body>
# </html>