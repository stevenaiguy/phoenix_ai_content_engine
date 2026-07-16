# Workflows

這個目錄只接受可由 n8n 直接匯入的 Workflow JSON。

在尚未確認目標 n8n 版本與最新節點 `typeVersion` 前，不放入推測格式的 Workflow，
避免匯入失敗或使用已淘汰節點。

## Workflow pipeline

```text
00-bootstrap
01-daily-orchestrator
02-ingestion-pipeline
03-analyze-content
04-research-agent
05-style-rag
06-writer-agent
07-reviewer-agent
08-publisher
09-learning-agent
99-error-handler
```

`02-ingestion-pipeline` is responsible for receiving, normalizing, deduplicating, and validating source records. It does not perform AI analysis.
