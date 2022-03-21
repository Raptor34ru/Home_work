from jinja2 import Template


menu = [
    {'href': '/index', 'link': 'Главная'},
    {'href': '/news', 'link': 'Новости'},
    {'href': '/about', 'link': 'О компании'},
    {'href': '/shop', 'link': 'Магазин'},
    {'href': '/contacts', 'link': 'Контакты'}
]
link = """<select name ="menu">
<ul>
{% for m in menu -%}
{% if m.link == 'Главная' -%}  
    <li> <a ="{{m['href']}}" class="active"> {{m["link"] }} </a></li>
{% else -%}
    <li> <a ="{{m['href']}}"> {{m["link"] }} </a></li>
{% endif -%}
{% endfor -%}
</ul>
</select>
"""

tm = Template(link)
msg = tm.render(menu=menu)

print(msg)