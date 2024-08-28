import yaml
from github import Github
from github.GithubException import GithubException
from datetime import datetime, date
import os
import sys

def load_project_structure(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def create_or_get_milestone(repo, milestone_data):
    title = milestone_data['name']
    due_date = milestone_data['due_date']
    if isinstance(due_date, str):
        due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
    elif isinstance(due_date, date):
        due_date = due_date
    else:
        print(f"警告: マイルストーン '{title}' の日付形式が不正です。スキップします。")
        return None

    milestones = list(repo.get_milestones())
    milestone = next((m for m in milestones if m.title == title), None)
    if milestone is None:
        try:
            milestone = repo.create_milestone(title=title, due_on=due_date)
            print(f"マイルストーン '{title}' を作成しました。")
        except GithubException as e:
            print(f"マイルストーン '{title}' の作成に失敗しました: {e}")
            return None
    else:
        print(f"既存のマイルストーン '{title}' を使用します。")
    return milestone

def create_issue(repo, milestone, issue_data):
    title = issue_data['title']
    existing_issues = list(repo.get_issues(milestone=milestone, state='all'))
    if not any(issue.title == title for issue in existing_issues):
        try:
            issue = repo.create_issue(
                title=title,
                body=issue_data.get('description', ''),
                milestone=milestone,
                labels=issue_data.get('labels', [])
            )
            print(f"イシュー '{title}' を作成しました。")
        except GithubException as e:
            print(f"イシュー '{title}' の作成に失敗しました: {e}")
    else:
        print(f"イシュー '{title}' は既に存在します。スキップします。")

def main():
    # GitHubオブジェクトの初期化
    github_token = os.environ.get('GITHUB_TOKEN')
    if not github_token:
        print("Error: GITHUB_TOKEN が設定されていません。")
        sys.exit(1)

    g = Github(github_token)

    # リポジトリの取得
    repo_name = os.environ.get('GITHUB_REPOSITORY')
    if not repo_name:
        print("Error: GITHUB_REPOSITORY が設定されていません。")
        sys.exit(1)

    try:
        repo = g.get_repo(repo_name)
    except GithubException as e:
        print(f"リポジトリの取得に失敗しました: {e}")
        sys.exit(1)

    # プロジェクト構造YAMLファイルの読み込み
    try:
        project_structure = load_project_structure('.github/project-structure.yml')
    except Exception as e:
        print(f"プロジェクト構造の読み込みに失敗しました: {e}")
        sys.exit(1)

    # マイルストーンとイシューの作成
    for milestone_data in project_structure['project']['milestones']:
        milestone = create_or_get_milestone(repo, milestone_data)
        if milestone:
            for issue_data in milestone_data['issues']:
                create_issue(repo, milestone, issue_data)

    print("プロジェクト構造の作成が完了しました。")

if __name__ == "__main__":
    main()