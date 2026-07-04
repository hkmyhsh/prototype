# サンプル構成

## ファイル構成

```
.agent/
  task.md              # 今回の依頼
  state.json           # 現在状態
  plan.md              # Plannerの計画
  decisions.md         # 判断理由
  reviewer_notes.md    # Reviewerの指摘
  runbook_updates.md   # Runbook反映候補
```

## コンテキストサンプル

```
あなたはCI基盤改善Agentです。

作業開始時:
- .agent/state.json を読む
- .agent/plan.md を読む
- .agent/decisions.md を読む

作業中:
- 判断したことは decisions.md に追記する
- TODOの進捗は state.json に反映する
- 不明点・ブロッカーは state.json の blocked_reason に書く

作業終了時:
- 次にやるべきことを next_action に1つだけ書く
- レビュー待ちなら status を review_required にする
```