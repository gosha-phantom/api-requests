import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# создание вызова api и сохранение ответа
url = 'https://api.github.com/search/repositories?q=language:python&sort=star'

req = requests.get(url)
print('Status code: ', req.status_code)

# сохранение ответа api в переменной
response_dict = req.json()
print('Total repositories: ', response_dict['total_count'])

# анализ информации о репозиториях
repo_dicts = response_dict['items']
# print('repositories returned: ', len(repo_dicts))
# print('\nSelected information about each repository:')
# for repo_dict in repo_dicts:
#     print('\nName: ', repo_dict['name'])
#     print('Owner: ', repo_dict['owner']['login'])
#     print('Stars: ', repo_dict['stargazers_count'])
#     print('Repository: ', repo_dict['html_url'])
#     print('Description: ', repo_dict['description'])

names, plot_dicts = [], []
for repo in repo_dicts:
    names.append(repo['name'])
    plot_dict = {
        'value': repo['stargazers_count'],
        'label': repo['description'],
        'xlink': repo['html_url']
    }
    plot_dicts.append(plot_dict)

# print(plot_dicts)

# построение визуализации
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)

# chart = pygal.Bar(style=my_style, x_label_rotation=45,
#                     show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')



# анализ первого репозитория
# repo_dict = repo_dicts[0]
# print('\nKeys:', len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

# обработка результатов
# print(response_dict.keys(), response_dict['incomplete_results'])

# анализ информации о репозиториях
