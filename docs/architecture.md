# Architecture

```text
Schedule / Webhook / RSS / Telegram
                 |
                 v
         Content Normalizer
                 |
                 v
           Analyzer Agent
                 |
                 v
      Free Research Sub-workflow
                 |
                 v
       Qdrant Cloud Style RAG
                 |
                 v
 OpenRouter Writer -> NVIDIA fallback
                 |
                 v
             Reviewer
                 |
                 v
       Markdown / GitHub Draft
                 |
                 v
        Slack / Discord Notice
```

VPS 僅執行 n8n。外部服務透過 HTTPS API 連線。
