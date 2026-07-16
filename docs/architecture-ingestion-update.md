# Architecture update: ingestion naming

The former `02-source-collector` name is replaced by `02-ingestion-pipeline`.

```text
Schedule / Webhook / RSS / Telegram
                 |
                 v
       02 Ingestion Pipeline
 Receive -> Normalize -> Deduplicate -> Validate
                 |
                 v
        03 Analyze Content
```

The ingestion workflow does not contain LLM, RAG, research, or writing logic.
