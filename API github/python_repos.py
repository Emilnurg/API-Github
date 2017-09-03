import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Создание вызова API и сохранение ответа
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Статус: ", r.status_code)

# Сохранение ответа API в переменной
response_dict = r.json()
print("Всего проектов на питоне:",response_dict['total_count'])

# Анализ информации о репозиториях
repo_dicts = response_dict['items']
print("Отображено проектов на странице: ", len(repo_dicts))

names, stars_dict = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    star_dict = {
        'value' : repo_dict['stargazers_count'],
        'label' : str(repo_dict['description']),
        'xlink' : repo_dict['html_url']
        }
    stars_dict.append(star_dict)
# Построение визуализации
chart_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(config=my_config, style=chart_style)
chart.title = 'Самые "звездные" проекты на Гитхабе'
chart.x_labels = names
chart.add('', stars_dict)
chart.render_to_file('python_repos2.svg')



"""# Анализ первого репозитория
repo_dict1 = repo_dicts[0]
print('\nЧисло пунктов: ', len(repo_dict1))
print('Выбранная инфа о каждом репозитории')
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])"""

