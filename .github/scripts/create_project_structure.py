import yaml
from github import Github
from datetime import datetime
import os

# GitHubオブジェクトの初期化
g = Github(os.environ['GITHUB_TOKEN'])

# リポジトリの取得
repo = g.get_repo(os.environ['GITHUB_REPOSITORY'])

# プロジェクトの作成（既に存在する場合はスキップ）
projects = list(repo.get_projects())
project = next((p for p in projects if p.name == project_name), None)
if project is None:
    try:
        project = repo.create_project(project_name, body="将棋序盤知識整理アプリケーション開発プロジェクト")
    except Exception as e:
        print(f"プロジェクトの作成に失敗しました: {e}")
        # プロジェクトが作成できなくても続行
        project = None

# マイルストーンとイシューの作成
for milestone_data in project_structure['project']['milestones']:
    # マイルストーンの作成
    milestone_title = milestone_data['name']
    milestone = next((m for m in repo.get_milestones() if m.title == milestone_title), None)
    if milestone is None:
        due_date = datetime.strptime(milestone_data['due_date'], '%Y-%m-%d')
        milestone = repo.create_milestone(title=milestone_title, due_on=due_date)
    
    # イシューの作成
    for issue_data in milestone_data['issues']:
        issue_title = issue_data['title']
        existing_issues = list(repo.get_issues(milestone=milestone, state='all'))
        if not any(issue.title == issue_title for issue in existing_issues):
            issue = repo.create_issue(
                title=issue_title,
                body=issue_data.get('description', ''),  # 詳細説明を本文として追加
                milestone=milestone,
                labels=issue_data['labels']
            )
            # イシューをプロジェクトに追加
            project.create_card(content_id=issue.id, content_type='Issue')

print("Project structure created successfully!")
