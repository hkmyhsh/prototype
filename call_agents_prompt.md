## 初回コール

```
このリポジトリを解析してください。

まず

AGENTS.md

を読み、

続いて

.agent/project_rules.md

を読み、

その後

.agent/task.md

を読んでください。

state.json が存在する場合は現在状態を復元してください。
```

### codexの動き

```
AGENTS.md

↓

役割理解

↓

project_rules

↓

task

↓

state

↓

現在位置理解

↓

plan更新

↓

実装開始
```

## 次回以降①

```
Executorとして作業してください。
```

### codexの動き

```
state.json

↓

next_action

↓

実装

↓

plan更新

↓

state更新

↓

decision更新
```

## 次回以降②

```
Reviewerとしてレビューしてください。
```

### codexの動き

```
review.md

更新

↓

state.json

status=review_required

↓

改善案追加
```

## 次回以降③

```
昨日の続きからお願いします。
```

### codexの動き

```
state.json

↓

next_action

↓

続き開始
```