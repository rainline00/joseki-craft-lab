# Joseki Craft Lab（定跡クラフトラボ）
![Build Status](https://github.com/rainline00/joseki-craft-lab/actions/workflows/frontend-ci.yml/badge.svg)
![Build Status](https://github.com/rainline00/joseki-craft-lab/actions/workflows/`backend-ci.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/github/rainline00/joseki-craft-lab/badge.svg?branch=main)](https://coveralls.io/github/rainline00/joseki-craft-lab?branch=main)
[![Dependency Status](https://david-dm.org/rainline00/joseki-craft-lab/status.svg?path=frontend)](https://david-dm.org/rainline00/joseki-craft-lab?path=frontend)

![License](https://img.shields.io/github/license/rainline00/joseki-craft-lab)
![Python Version](https://img.shields.io/badge/python-3.12+-blue.svg)
![TypeScript](https://badgen.net/badge/TypeScript/4.9.5/blue)
![React](https://img.shields.io/badge/react-18.3.1-blue)

Joseki Craft Lab（定跡クラフトラボ）は、将棋の定跡（序盤戦略）を作成、管理、分析するための革新的なツールです。グラフデータベース技術を活用することで、将棋の複雑な序盤手順を探索し理解するためのユニークで強力な方法を提供します。

## 機能（予定）

- 対局手の入力と可視化のための対話型将棋盤
- 定跡戦略のグラフベース表現
- 将棋エンジン（やねうら王）との統合による手の評価
- KIF（棋譜）ファイルのインポートと分析
- 定跡ツリーのビジュアルナビゲーション
- カスタマイズ可能な評価指標

## 技術スタック

- フロントエンド：React（TypeScript使用）
- バックエンド：FastAPI（Python）
- データベース：Memgraph（Neo4j互換のグラフデータベース）
- 将棋エンジン：やねうら王
- 開発環境管理：Poetry、asdf（pyenv）
- コンテナ化：Docker

## プロジェクト構造

```
./
├── frontend/          # Reactフロントエンドアプリケーション
│   ├── src/
│   └── tests/
├── backend/           # FastAPIバックエンドアプリケーション
│   ├── src/
│   ├── tests/
│   ├── pyproject.toml # Poetry設定ファイル
│   └── poetry.lock    # Poetryロックファイル
├── docs/              # プロジェクトドキュメント
│   ├── api/
│   ├── development/
│   ├── deployment/
│   └── user-guide/
├── shared/            # 共有ユーティリティと型定義
│   ├── types/
│   └── utils/
├── config/            # 設定ファイル
├── scripts/           # ユーティリティスクリプト
├── docker/            # Docker関連ファイル
├── .tool-versions     # asdf用のバージョン指定ファイル
└── README.md
```

## セットアップ

### 前提条件

- [asdf](https://asdf-vm.com/)がインストールされていること
- [Docker](https://www.docker.com/)がインストールされていること

1. リポジトリのクローン：
   ```
   git clone https://github.com/your-username/joseki-craft-lab.git
   cd joseki-craft-lab
   ```

2. asdfを使用してPythonをインストール：
   ```
   asdf install
   ```

3. Poetryのインストール：
   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```

4. バックエンドのセットアップ：
   ```
   cd backend
   poetry install
   poetry run uvicorn src.main:app --reload
   ```

5. フロントエンドのセットアップ：
   ```
   cd frontend
   npm install
   npm start
   ```

6. Dockerを使用したMemgraphのセットアップ：
   ```
   cd docker
   docker-compose up -d
   ```

## 開発

開発を始める前に、必ず正しい Python バージョンがアクティブになっていることを確認してください：

```
asdf current
```

バックエンドの依存関係を追加または更新する場合は、Poetry を使用してください：

```
poetry add <package-name>
```

## 開発状況

このプロジェクトは現在、開発の初期段階にあります。最小限の実用的な製品（MVP）の構築に焦点を当てた反復的なアプローチを採用しています。

## 貢献

Joseki Craft Labへの貢献を歓迎します！プルリクエストを提出する前に、貢献ガイドライン（今後追加予定）をお読みください。

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。詳細は[LICENSE](LICENSE)ファイルをご覧ください。

## 謝辞

- インスピレーションとサポートを提供してくれた将棋コミュニティの皆様
- 優れた将棋エンジンを開発されたやねうら王の開発者の皆様
- 強力なグラフデータベースを提供してくれたMemgraphチーム

## ロードマップ

- [ ] 基本的な将棋盤UIの実装
- [ ] 将棋の局面用グラフデータベーススキーマのセットアップ
- [ ] やねうら王との統合による手の評価
- [ ] 定跡ツリーの管理とクエリのためのAPI開発
- [ ] KIFファイルのインポート機能の実装
- [ ] 定跡ツリーの可視化機能の作成
- [ ] ユーザー認証とデータ永続化の開発

開発ロードマップの進行に伴い、更新情報をお待ちください！