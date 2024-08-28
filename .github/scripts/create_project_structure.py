import yaml
from github import Github
from github.GithubException import GithubException
from datetime import datetime
import os
import sys

def load_project_structure(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def create_or_get_project(repo, project_name):
    try:
        projects = list(repo.get_projects())
        project = next((p for p in projects if p.name == project_name), None)
        if project is None:
            project = repo.create_project(project_name, body="将棋序盤知識整理アプリケーション開発プロジェクト")
            print(f"プロジェクト '{project_name}' を作成しました。")
        else:
            print(f"既存のプロジェクト '{project_name}' を使用します。")
        return project
    except GithubException as e:
        print(f"プロジェクトの作成に失敗しました: {e}")
        return None

def create_or_get_milestone(repo, milestone_data):
    title = milestone_data['name']
    due_date = datetime.strptime(milestone_data['due_date'], '%Y-%m-%d')
    milestones = list(repo.get_milestones())
    milestone = next((m for m in milestones if m.title == title), None)
    if milestone is None:
        milestone = repo.create_milestone(title=title, due_on=due_date)
        print(f"マイルストーン '{title}' を作成しました。")
    else:
        print(f"既存のマイルストーン '{title}' を使用します。")
    return milestone

def create_issue(repo, project, milestone, issue_data):
    title = issue_data['title']
    existing_issues = list(repo.get_issues(milestone=milestone, state='all'))
    if not any(issue.title == title for issue in existing_issues):
        issue = repo.create_issue(
            title=title,
            body=issue_data.get('description', ''),
            milestone=milestone,
            labels=issue_data.get('labels', [])
        )
        if project:
            project.create_card(content_id=issue.id, content_type='Issue')
        print(f"イシュー '{title}' を作成しました。")
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
    project_structure = load_project_structure('.github/project-structure.yml')

    # プロジェクト名の取得
    project_name = project_structure['project']['name']

    # プロジェクトの作成または取得
    project = create_or_get_project(repo, project_name)

    # マイルストーンとイシューの作成
    for milestone_data in project_structure['project']['milestones']:
        milestone = create_or_get_milestone(repo, milestone_data)
        for issue_data in milestone_data['issues']:
            create_issue(repo, project, milestone, issue_data)

    print("プロジェクト構造の作成が完了しました。")

if __name__ == "__main__":
    main()