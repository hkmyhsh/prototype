# Runbook: GitHub Actions Runner 待機時間アラート

## 1. アラート概要

GitHub Actions の Workflow Job が20分以上 queued 状態の場合に通知される。

## 2. 初動確認

通知を受けたら、以下を確認する。

1. 通知内の run URL を開く
2. 対象Jobの labels を確認する
3. 利用可能な Self-hosted Runner が存在するか確認する
4. Runner が offline になっていないか確認する
5. ARC/EKS の場合、Runner Pod が起動しているか確認する
6. concurrency 設定により待機していないか確認する

## 3. 主な原因と確認方法

### Runner不足

確認:

- Runner一覧で idle runner があるか
- 対象 labels に一致する runner があるか

対応:

- Runner数を増やす
- ARCのスケール設定を確認する

### Runner offline

確認:

- GitHub の Runner 画面で offline runner を確認する
- Kubernetes / EC2 / Jenkins連携などの基盤状態を確認する

対応:

- Runnerプロセス再起動
- Pod再作成
- EC2再起動

### Label不一致

確認:

- Workflow の `runs-on` を確認する
- Runner の label を確認する

対応:

- Workflow側のlabel修正
- Runner側のlabel修正

### concurrency待ち

確認:

- Workflow の concurrency 設定を確認する
- 同一groupの実行中Workflowを確認する

対応:

- 実行中Workflowの完了を待つ
- 必要に応じて concurrency group を見直す

## 4. エスカレーション基準

以下の場合は基盤担当へエスカレーションする。

- 複数Repositoryで同時多発している
- Runner全体がofflineになっている
- ARC/EKSのスケールが機能していない
- GitHub API エラーが継続している
- 30分以上解消しない

## 5. 調査時に残す情報

- 発生時刻
- Repository
- Workflow名
- Job名
- run URL
- labels
- 待機時間
- Runner状態
- 推定原因
- 実施した対応

## 6. 復旧後確認

- 対象Jobが実行開始したか
- 新規queued jobが増えていないか
- 通知が継続していないか
- 同様の原因が再発しそうか
