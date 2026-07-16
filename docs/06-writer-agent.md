# 06 Writer Agent

## Responsibility

This workflow:

1. Accepts content enriched by analysis, research, and style RAG.
2. Builds a constrained long-form writing prompt.
3. Calls OpenRouter first.
4. Falls back to NVIDIA when the primary response fails or is invalid.
5. Outputs a normalized article object with Markdown.

It does not review, publish, or learn from human edits.

## Required n8n Credentials

- `OpenRouter Bearer Auth` on `CallOpenRouterWriter`
- `NVIDIA NIM Bearer Auth` on `CallNvidiaWriter`

## Webhook

- Method: `POST`
- Path: `/webhook/phoenix/write`

## Manual test

Run `ManualTest`.

Expected final fields:

- `article.title`
- `article.subtitle`
- `article.summary`
- `article.tags`
- `article.markdown`
- `metadata.status = drafted`
