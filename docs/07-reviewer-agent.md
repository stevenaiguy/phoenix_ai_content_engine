# 07 Reviewer Agent

## Responsibility

This workflow:

1. Accepts a draft from `06-writer-agent`.
2. Reviews structure, clarity, fact risk, style, duplication, and SEO.
3. Calls OpenRouter first.
4. Falls back to NVIDIA when the primary response fails or is invalid.
5. Applies necessary revisions and returns approval status.

It does not publish the article.

## Required n8n Credentials

- `OpenRouter Bearer Auth` on `CallOpenRouterReviewer`
- `NVIDIA NIM Bearer Auth` on `CallNvidiaReviewer`

## Webhook

- Method: `POST`
- Path: `/webhook/phoenix/review`

## Approval rule

The final article is approved only when:

- score is at least 85
- model returned `approved: true`
- no issue has `severity: high`

## Manual test

Run `ManualTest`.

Expected final fields:

- `review.score`
- `review.approved`
- `review.issues`
- `article.markdown`
- `metadata.status`
