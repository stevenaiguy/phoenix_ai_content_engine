# 04 Research Agent

## Responsibility

This free MVP:

1. Receives an analyzed content item.
2. Builds a research query from `analysis.topic` and `analysis.keywords`.
3. Calls the public Chinese Wikipedia API.
4. Returns up to five background sources.
5. Merges the research context into the content contract.

It does not call a paid search API, write the article, or query Qdrant.

## Webhook

- Method: `POST`
- Path: `/webhook/phoenix/research`

The input should be the output of `03-analyze-content`.

## Manual test

Run `ManualTest`.

Expected final fields:

- `research.query`
- `research.sources`
- `research.sourceCount`
- `metadata.status = researched`

## Limitation

Wikipedia is useful for stable background knowledge, but not enough for time-sensitive facts. A later version can add official RSS feeds and source allowlists.
