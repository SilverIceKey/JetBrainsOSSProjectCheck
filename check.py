import requests
from datetime import datetime, timedelta

def get_commit_dates(repo_url):
    repo_owner, repo_name = repo_url.rstrip('/').split('/')[-2:]
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    params = {
        'per_page': 100
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    commits = response.json()
    commit_dates = [commit['commit']['committer']['date'] for commit in commits]
    return commit_dates

def check_commit_activity(commit_dates):
    now = datetime.now()
    six_months_ago = now - timedelta(days=6*30)
    commit_dates = [datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ") for date in commit_dates]
    monthly_commits = [0] * 6

    for date in commit_dates:
        if date > six_months_ago:
            month_diff = (now.year - date.year) * 12 + now.month - date.month
            if month_diff < 6:
                monthly_commits[month_diff] += 1

    reasons = []
    for i in range(6):
        if monthly_commits[i] == 0:
            reasons.append(f"{i+1}个月前没有代码提交。")
    return all(commits > 0 for commits in monthly_commits), reasons

if __name__ == "__main__":
    repo_url = input("请输入GitHub仓库地址: ")

    commit_dates = get_commit_dates(repo_url)
    is_active, reasons = check_commit_activity(commit_dates)
    if is_active:
        print("你的仓库符合活动要求。")
    else:
        print("你的仓库不符合活动要求，原因如下：")
        for reason in reasons:
            print(reason)
