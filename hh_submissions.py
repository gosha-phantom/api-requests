import requests
from operator import itemgetter

# создание вызова api и сохранение ответа
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
req = requests.get(url)
print('Status cde: ', req.status_code)

# обработка информации о каждой статье
submission_ids = req.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    # создание отдельного вызова api для каждой статьи
    url = ('https://hacker-news.firebaseio.com/v0/item' + 
            str(submission_id) + '.json')
    submission_req = requests.get(url)
    print(submission_req.status_code, submission_id)
    response_dict = submission_req.json()

    print(response_dict.keys())
    # submission_dict = {
    #     'title': response_dict['title'],
    #     'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
    #     'comments': response_dict.get('descendants', 0)
    # }
    # submission_dicts.append(submission_dict)

    # # сортировка массива
    # submission_dicts = sorted(submission_dicts, 
    #         key=itemgetter('comments'), reverse=True)
    
    # # вывод в консоль
    # for submission_dict in submission_dicts:
    #     print('\nTitle: ', submission_dict['title'])
    #     print('Discussion link: ', submission_dict['link'])
    #     print('Comments: ', submission_dict['comment'])