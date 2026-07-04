# Codex Agent Harness Template 日本語版

Codex を利用して、AIエージェントに計画、設計、実装、テスト、レビュー、ドキュメント化を継続的に行わせるためのテンプレートです。

## 使い方

1. このテンプレートを対象リポジトリに配置する
2. `.agent/task.md` を案件内容に合わせて書き換える
3. `.agent/project_rules.md` にプロジェクト固有ルールを追加する
4. Codex に Planner mode から依頼する

## 最初の依頼例

```text
Planner mode で作業してください。
AGENTS.md と .agent 配下のMemory Storeを読み、今回の案件に合わせて .agent/plan.md と .agent/state.json を更新してください。
実装はまだ行わないでください。
```

## Memory Store

`.agent/` 配下を Codex 用 Memory Store として利用します。

- `state.json`: 現在状態
- `plan.md`: 計画
- `decisions.md`: 判断履歴
- `review.md`: レビュー結果
- `project_rules.md`: 案件固有ルール
- `prompts/`: 各エージェント役割のプロンプト

## 6つの役割

- Planner: 計画
- Architect: 設計
- Executor: 実装
- Tester: テスト
- Reviewer: レビュー
- Documenter: ドキュメント化

## 検証

`state.json` の形式確認には以下を利用できます。

```bash
python scripts/validate_state.py
```
