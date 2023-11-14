# Jinja
Jinha is a [SF_Web Templating Engine](SF_Web-Templating-Engine) for [Python](../Week-6-Python/CS50x_Python.md) which allows the creation of HTML templates and customization of tags with variables


## Sytanx
### Layouts
Templates are blocks of html tags that can be used in multiple HTML files avoiding constant repetition

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <title></title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="css/style.css" rel="stylesheet">
    </head>
    <body>
        {% block body %}{% endblock %}
    </body>
</html>

```

On another html file this layout can be referenced with: 
```html
{% extends "layout.html" %}
{% block body %}
    <!-- unique tags -->
{% endblock %}
```

All tags in the first block will be plugged on the second one, adn the unique tags will be inserted as `body`

### Variables and Logic
Jinja allows the use of variables and logic inside html files
```html
{% for user in users %}
    {{ user.username }}
    {{ user.password }}
{% endfor %}
```
