from github import Github

# 输入你的GitHub用户名和访问令牌
username = "Ldreamstar"
token = "token"

# 创建GitHub对象
g = Github(username, token)

# 获取当前用户（你的GitHub用户）
user = g.get_user()

# 获取关注者列表
followers = user.get_followers()

# 创建一个空列表用于存储所有关注者的仓库数据
all_repos_data = []

# 遍历关注者列表
for follower in followers:
    print(f"Getting repositories for {follower.login}")
    try:
        # 获取关注者的仓库列表
        repos = follower.get_repos()

        # 将仓库数据添加到列表
        for repo in repos:
            repo_data = {
                "name": repo.name,
                "description": repo.description,
                "language": repo.language,
                "forks_count": repo.forks_count,
                "stargazers_count": repo.stargazers_count,
                "watchers_count": repo.watchers_count,
                # 添加其他你需要的仓库信息
            }
            all_repos_data.append(repo_data)
    except Exception as e:
        print(f"Error getting repositories for {follower.login}: {str(e)}")

# 将数据存储到本地文件
import json

output_file = "followers_repos_data.json"
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(all_repos_data, f, ensure_ascii=False, indent=4)

print(f"Data saved to {output_file}")
