import requests
import threading
from datetime import datetime
from main_script import get_commit_dates, check_commit_activity  # 假设主脚本保存为 main_script.py
from tqdm import tqdm
import os

def get_user_repos(user_url, headers):
    user = user_url.rstrip('/').split('/')[-1]
    url = f"https://api.github.com/users/{user}/repos"
    params = {
        'per_page': 100
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    repos = response.json()
    repo_urls = [repo['html_url'] for repo in repos if not repo['archived']]
    return repo_urls

def worker(repo_url, results, headers, progress_bar):
    commit_dates = get_commit_dates(repo_url, headers)
    is_active, reasons = check_commit_activity(commit_dates)
    results.append((repo_url, is_active, reasons))
    progress_bar.update(1)

def check_user_repos(user_url, headers):
    repo_urls = get_user_repos(user_url, headers)
    threads = []
    results = []

    with tqdm(total=len(repo_urls), desc="检查进度") as progress_bar:
        for repo_url in repo_urls:
            thread = threading.Thread(target=worker, args=(repo_url, results, headers, progress_bar))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

    results.sort(key=lambda x: (not x[1], len(x[2])))

    with open("result.md", "w", encoding="utf-8") as f:
        f.write(f"# 仓库活动检查结果 ({datetime.now().strftime('%Y-%m-%d %H:%M:%S')})\n\n")
        for repo_url, is_active, reasons in results:
            f.write(f"## {repo_url}\n")
            if is_active:
                f.write("符合活动要求。\n\n")
            else:
                f.write("不符合活动要求，原因如下：\n")
                for reason in reasons:
                    f.write(f"- {reason}\n")
                f.write("\n")

def get_token():
    token_file = 'access_token.txt'
    if os.path.exists(token_file):
        with open(token_file, 'r') as file:
            token = file.read().strip()
    else:
        token = input("请输入GitHub个人访问令牌: ")
        with open(token_file, 'w') as file:
            file.write(token)
    return token

if __name__ == "__main__":
    user_url = input("请输入GitHub用户地址: ")
    token = get_token()
    headers = {
        'Authorization': f'token {token}'
    }
    check_user_repos(user_url, headers)
