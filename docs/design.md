# 設計書: GitHub Actions Self-hosted Runner 待機時間監視

## 1. 目的

GitHub Actions の Self-hosted Runner 利用時に、20分以上 queued 状態となっている Workflow Job を検知し、運用担当者へ通知する。

## 2. 背景

Self-hosted Runner は、Runner の台数不足、Runner offline、ラベル不一致、runner group 設定、ARC/EKS のスケール遅延などにより、ジョブが長時間待機する可能性がある。

待機が長期化すると、開発者のビルド待ち時間が増加し、問い合わせや障害対応が発生する。

## 3. 想定構成

```text
EventBridge Scheduler
  ↓
Lambda
  ↓
GitHub App 認証
  ↓
GitHub REST API / GraphQL API
  ↓
queued job 抽出
  ↓
20分以上待機判定
  ↓
Slack 通知
  ↓
CloudWatch Logs
```

## 4. 主要コンポーネント

### EventBridge Scheduler

定期的に Lambda を起動する。

例:

- 5分間隔
- 10分間隔

### Lambda

以下を担当する。

- GitHub App のJWT作成
- Installation Access Token取得
- 対象RepositoryまたはOrganizationのWorkflow Job取得
- queued duration の計算
- 通知対象の抽出
- Slack通知
- CloudWatch Logsへの出力

### GitHub App

GitHub API 呼び出しに利用する。

必要権限は案件ごとに精査する。
原則として、Personal Access Token ではなく GitHub App を利用する。

### Slack通知

通知内容の例:

- Repository
- Workflow名
- Job名
- 待機時間
- run URL
- runner labels
- 推定原因

## 5. 検知条件

初期案:

- Job status が `queued`
- queued 開始から20分以上経過
- 対象RepositoryまたはOrganizationに属する

## 6. 通知抑止

同じJobに対して通知が重複しすぎないようにする。

候補:

- DynamoDB に通知済み run_id / job_id を保存する
- 一定時間内は同一Jobを再通知しない
- 初期版では重複許容、Runbookで運用回避する

## 7. セキュリティ

- GitHub App の秘密鍵は Secrets Manager に保存する
- Slack Webhook URL は Secrets Manager または Parameter Store に保存する
- Lambda IAM Role は最小権限にする
- 通知文に機密情報を含めすぎない

## 8. 監視・ログ

CloudWatch Logs に以下を出力する。

- 実行開始時刻
- 対象Repository数
- 取得Job数
- 通知対象Job数
- APIエラー
- Slack通知結果

## 9. 未決事項

- GitHub API の具体的なエンドポイント
- 対象Repositoryの列挙方法
- 通知重複抑止の保存先
- Slack通知方式
- Lambda実装言語
