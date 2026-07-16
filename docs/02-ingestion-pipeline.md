# 02 Ingestion Pipeline

## Responsibility

This workflow only handles ingestion:

1. Receive content from Webhook or manual test input.
2. Normalize different source payloads.
3. Remove duplicates inside the current batch.
4. Validate the minimum content contract.
5. Return normalized items for `03-analyze-content`.

It does not call an LLM, query Qdrant, perform research, or write an article.

## Webhook

- Method: `POST`
- Path: `/webhook/phoenix/ingest`

Example body:

```json
{
  "items": [
    {
      "source": "rss",
      "title": "Example",
      "url": "https://example.com/post",
      "content": "Article text",
      "language": "zh-TW",
      "publishedAt": "2026-07-16T00:00:00.000Z"
    }
  ]
}
```

The webhook uses `responseMode: lastNode`, so the HTTP response is the output of `ValidateContent`.

## Deduplication

This version removes duplicates only inside the current execution:

- URL is the preferred deduplication key.
- Content is used when URL is unavailable.
- Persistent deduplication across days will be added later using n8n Data Tables or another free persistent store.

## Manual test

Run `ManualTest`. The sample input contains two records with the same URL. The final output should contain one normalized item.

## Expected output

```json
{
  "id": "rss:https://example.com/posts/ai-agent",
  "source": "rss",
  "title": "AI Agent 與工作流",
  "url": "https://example.com/posts/ai-agent",
  "language": "zh-TW",
  "content": "AI Agent 不只生成文字，也應根據工具結果決定下一步。",
  "images": [],
  "tags": [],
  "score": 0,
  "shouldWrite": false,
  "analysis": {},
  "metadata": {
    "collector": "02-ingestion-pipeline",
    "version": "0.2.0",
    "status": "normalized"
  }
}
```
