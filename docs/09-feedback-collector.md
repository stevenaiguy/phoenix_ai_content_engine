# 09 Feedback Collector

## Responsibility

This workflow:

1. Receives the AI draft and the final human-edited version.
2. Normalizes the feedback payload.
3. Computes a line-level editorial diff.
4. Records title, subtitle, summary, and Markdown changes.
5. Outputs a stable feedback contract for the Learning Agent.

It does not call an LLM, update prompts, or write to Qdrant.

## Webhook

- Method: `POST`
- Path: `/webhook/phoenix/feedback`

## Required input

```json
{
  "articleId": "article-001",
  "sourceUrl": "https://example.com/source",
  "draft": {
    "title": "AI draft title",
    "subtitle": "AI draft subtitle",
    "summary": "AI draft summary",
    "markdown": "# AI draft"
  },
  "edited": {
    "title": "Human title",
    "subtitle": "Human subtitle",
    "summary": "Human summary",
    "markdown": "# Human final version"
  },
  "editor": "human",
  "editedAt": "2026-07-16T00:00:00.000Z",
  "metrics": {
    "views": 0,
    "reads": 0,
    "claps": 0,
    "responses": 0
  }
}
```

## Output

The final output contains:

- `feedbackId`
- `editorialDiff`
- `originalDraft`
- `finalVersion`
- `metrics`
- `metadata.status = feedback_collected`

## Manual test

Run `ManualTest`.

Expected differences include:

- changed title
- changed subtitle
- changed introduction
- changed conclusion CTA
