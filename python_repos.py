import requests


# 执行API调用并且存储响应
def get_response(url):
    """存储一个响应，并且为存储响应建立列表"""
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    return r

def get_repo_dicts(r):
    """用requests调用API；调用get()并将URL传递给它，再将响应对象赋给变量r"""
    print(f"Status code:{r.status_code}")
    # 将API响应赋给一个变量
    response_dict = r.json()
    print(f"Total repositpries:{response_dict['total_count']}")
    # 探索有关仓库的信息
    repo_dicts = response_dict['items']
    print(f"Repositorie returned:{len(repo_dicts)}")
    return repo_dicts


def print_repo_dicts(repo_dicts):
    """研究第一个打印输出repo_dicts"""
    repo_dict = repo_dicts[0]
    # print(f"\nKeys:{len(repo_dict)}")
    # for key in sorted(repo_dict.keys()):
    #     print(key)
    print("\nSelected information about first repository:")
    for repo_dict in repo_dicts:
        print(f"Name:{repo_dict['name']}")
        print(f"Owner:{repo_dict['owner']['login']}")
        print(f"Stars:{repo_dict['stargazers_count']}")
        print(f"Repos=sitory:{repo_dict['html_url']}")
        print(f"Created:{repo_dict['created_at']}")
        print(f"Updated:{repo_dict['updated_at']}")
        print(f"Description:{repo_dict['description']}")

if __name__ == '__main__':  # 主函数放在if中，这样导入时不会直接运行
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = get_response(url)
    repo_dicts = get_repo_dicts(r)
    print_repo_dicts(repo_dicts)

