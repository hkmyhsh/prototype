# Codex Agent Harness テンプレート

このリポジトリは、Codex を利用して AI エージェントを半自律的に動かすための Harness テンプレートです。

目的は、AI に毎回口頭で前提や進捗を説明するのではなく、リポジトリ内の Memory Store を参照・更新させながら、計画、実行、テスト、レビュー、ドキュメント化を継続できる状態を作ることです。

---

## 基本方針

Codex は作業開始時に、必ず以下を読むこと。

1. `.agent/task.md`
2. `.agent/state.json`
3. `.agent/project_rules.md`
4. `.agent/plan.md`
5. `.agent/decisions.md`

作業終了時には、実施内容に応じて以下を更新すること。

- `.agent/state.json`
- `.agent/plan.md`
- `.agent/decisions.md`
- `.agent/review.md`
- `docs/design.md`
- `docs/runbook.md`

途中で作業を止める場合は、`.agent/state.json` の `next_action` に次回再開時の最初の行動を1つだけ記録すること。

---

## エージェント構成

このテンプレートでは、Codex に以下の6つの役割を切り替えさせる。

### 1. Planner

タスクを整理し、実施計画を作る。

担当範囲:

- 目的の明確化
- 完了条件の整理
- タスク分割
- 優先順位付け
- リスクの初期洗い出し
- `.agent/plan.md` の更新

Planner は原則として実装を行わない。

### 2. Architect

設計方針を決める。

担当範囲:

- アーキテクチャ検討
- 方式比較
- 非機能要件の確認
- セキュリティ・運用観点の整理
- `docs/design.md` の更新
- `.agent/decisions.md` の更新

### 3. Executor

実装・調査・修正を行う。

担当範囲:

- コード作成
- 設定ファイル作成
- 既存コード調査
- 小さな修正
- 動作確認
- `.agent/state.json` の更新

### 4. Tester

テスト観点と検証結果を整理する。

担当範囲:

- テストケース作成
- 単体テスト・結合テスト方針の作成
- 異常系確認
- 再実行条件の整理
- 検証結果の記録

### 5. Reviewer

成果物をレビューする。

担当範囲:

- 要件との整合確認
- 設計妥当性確認
- セキュリティ確認
- 運用性確認
- 保守性確認
- `.agent/review.md` の更新

Reviewer は原則として直接修正せず、指摘と修正方針を記録する。

### 6. Documenter

人間が利用するドキュメントに整理する。

担当範囲:

- Runbook 更新
- 設計書更新
- README 更新
- 判断履歴の整形
- 引き継ぎメモ作成

---

## Codex への依頼例

### 計画を作る

```text
Planner mode で作業してください。
AGENTS.md と .agent 配下のMemory Storeを読み、.agent/plan.md を更新してください。
実装はまだ行わないでください。
```

### 設計する

```text
Architect mode で作業してください。
現在の plan.md をもとに設計方針を検討し、docs/design.md と .agent/decisions.md を更新してください。
```

### 実装する

```text
Executor mode で作業してください。
.agent/state.json の next_action を実行し、作業後に state.json と decisions.md を更新してください。
```

### テストする

```text
Tester mode で作業してください。
実装内容に対するテスト観点を整理し、必要なテストを実行または提案してください。
```

### レビューする

```text
Reviewer mode で作業してください。
設計・実装・テスト・Runbookをレビューし、.agent/review.md に指摘を記録してください。
```

### ドキュメント化する

```text
Documenter mode で作業してください。
今回の成果を docs/design.md と docs/runbook.md に反映し、人間が読める形に整えてください。
```

---

## Memory Store運用ルール

Memory Store は、AI が次回作業を再開するための作業状態である。
監査ログそのものではない。

- 短期記憶: `.agent/state.json`
- 計画: `.agent/plan.md`
- 判断履歴: `.agent/decisions.md`
- レビュー結果: `.agent/review.md`
- プロジェクト固有ルール: `.agent/project_rules.md`
- 人間向け成果物: `docs/`

判断理由が発生した場合は、必ず `.agent/decisions.md` に記録する。
次回再開に必要な情報は、必ず `.agent/state.json` に記録する。

---

## 禁止事項

Codex は以下を行わないこと。

- 本番環境への直接変更
- 秘密情報の平文保存
- 人間承認なしの破壊的操作
- `state.json` を更新しないまま作業終了
- 判断理由を残さない設計変更
- テスト未実施のまま完了扱いにすること

---

## 完了条件

作業完了時は、以下を満たすこと。

- `state.json` の `status` が適切である
- `next_action` が空、または次回行動として明確である
- 主要な判断が `decisions.md` に記録されている
- レビュー観点が `review.md` に記録されている
- 人間向けドキュメントが更新されている
