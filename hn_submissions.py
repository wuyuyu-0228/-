# 执行API调用并且存储响应
from operator import itemgetter
from plotly import offline
import requests

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
# print("Status code:", r.status_code)

# 处理每篇文章的信息
submission_ids = r.json()  # 将响应文本转换为一个python列表
submission_dicts = []

# 遍历前30篇文章的id
for submission_id in submission_ids[:30]:
    # 对每篇文章，都执行一个API调用
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url)
    # print(f"id:{submission_id}\status:{r.status_code}")
    response_dict = submission_r.json()
    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comment': response_dict.get('descendants', 0),
    }
    submission_dicts.append(submission_dict)

# 处理数据
comment_number, labels, links ,titles= [], [], [],[]
submission_dicts = sorted(submission_dicts, key=itemgetter('comment'), reverse=True)
print(len(submission_dicts))
for submission_dict in submission_dicts:
    # print("\nTitle:", submission_dict['title'])
    # print("Discussion link:", submission_dict['link'])
    # print("Comments:", submission_dict['comment'])
    link=f"<a href='{submission_dict['link']}'>{submission_dict['title']}</a>"
    links.append(link)
    titles.append(submission_dict['title'])
    comment_number.append(submission_dict['comment'])
    label = f"{submission_dict['title']}<br />{submission_dict['link']}"
    labels.append(label)
# print(links)
# print(comment_number)
# print(labels)
# 可视化
data = [{
    'type': 'bar',
    'x':links,
    'y': comment_number,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60,100,150)',
        'line': {'width': 1.5, 'color': 'rgb(25,25,25)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': 'Hacker News 上最活跃的讨论',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Acticals',
        'titlefont': {'size': 20},
        'tickfont': {'size': 10},
    },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 20},
        'tickfont': {'size': 14},
    },
}
fig={'data':data,'layout':my_layout}
offline.plot(fig,filename='hacker_news.html')