import yaml
from github import Github
from github.GithubException import GithubException
from datetime import datetime, date
import os
import sys
import time

def load_project_structure(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def get_or_create_project(repo, project_name):
    try:
        projects = list(repo.get_projects(state='all'))
        project = next((p for p in projects if p.name == project_name), None)
        if project is None:
            project = repo.create_project(project_name, body="将棋序盤知識整理アプリケーション開発プロジェクト")
            print(f"プロジェクト '{project_name}' を作成しました。")
        else:
            print(f"既存のプロジェクト '{project_name}' を使用します。")
        return project
    except GithubException as e:
        print(f"プロジェクトの取得または作成に失敗しました: {e}")
        return None

def get_or_create_milestone(repo, milestone_data):
    title = milestone_data['name']
    due_date = milestone_data['due_date']
    if isinstance(due_date, str):
        due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
    elif isinstance(due_date, date):
        due_date = due_date
    else:
        print(f"警告: マイルストーン '{title}' の日付形式が不正です。スキップします。")
        return None

    try:
        milestones = list(repo.get_milestones(state='all'))
        milestone = next((m for m in milestones if m.title == title), None)
        if milestone is None:
            milestone = repo.create_milestone(title=title, due_on=due_date)
            print(f"マイルストーン '{title}' を作成しました。")
        else:
            print(f"既存のマイルストーン '{title}' を使用します。")
        return milestone
    except GithubException as e:
        print(f"マイルストーン '{title}' の取得または作成に失敗しました: {e}")
        return None

def create_or_update_issue(repo, project, milestone, issue_data):
    title = issue_data['title']
    try:
        existing_issues = list(repo.get_issues(state='all'))
        existing_issue = next((i for i in existing_issues if i.title == title), None)
        
        if existing_issue:
            if existing_issue.milestone != milestone:
                existing_issue.edit(milestone=milestone)
                print(f"イシュー '{title}' のマイルストーンを更新しました。")
            else:
                print(f"イシュー '{title}' は既に正しいマイルストーンが設定されています。")
            issue = existing_issue
        else:
            issue = repo.create_issue(
                title=title,
                body=issue_data.get('description', ''),
                milestone=milestone,
                labels=issue_data.get('labels', [])
            )
            print(f"イシュー '{title}' を作成しました。")

        # イシューをプロジェクトに追加
        if project:
            try:
                project.create_card(content_id=issue.id, content_type='Issue')
                print(f"イシュー '{title}' をプロジェクトに追加しました。")
            except GithubException as e:
                print(f"イシュー '{title}' のプロジェクトへの追加に失敗しました: {e}")

    except GithubException as e:
        print(f"イシュー '{title}' の作成または更新に失敗しました: {e}")

def main():
    github_token = os.environ.get('GITHUB_TOKEN')
    if not github_token:
        print("Error: GITHUB_TOKEN が設定されていません。")
        sys.exit(1)

    g = Github(github_token)

    repo_name = os.environ.get('GITHUB_REPOSITORY')
    if not repo_name:
        print("Error: GITHUB_REPOSITORY が設定されていません。")
        sys.exit(1)

    try:
        repo = g.get_repo(repo_name)
    except GithubException as e:
        print(f"リポジトリの取得に失敗しました: {e}")
        sys.exit(1)

    try:
        project_structure = load_project_structure('.github/project-structure.yml')
    except Exception as e:
        print(f"プロジェクト構造の読み込みに失敗しました: {e}")
        sys.exit(1)

    project_name = project_structure['project']['name']
    project = get_or_create_project(repo, project_name)

    for milestone_data in project_structure['project']['milestones']:
        milestone = get_or_create_milestone(repo, milestone_data)
        if milestone:
            for issue_data in milestone_data['issues']:
                create_or_update_issue(repo, project, milestone, issue_data)
                time.sleep(1)  # API制限を避けるために1秒待機

    print("プロジェクト構造の作成または更新が完了しました。")

if __name__ == "__main__":
    main()