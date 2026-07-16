# Phoenix Event Contract v2

Version: `2.0.0`

This document defines the canonical event contract shared by Phoenix AI Content Engine workflows.

## Design goals

- Every workflow receives and returns one root event object.
- A workflow appends or updates only the section it owns.
- Existing upstream sections must be preserved.
- Missing optional sections are normalized to empty objects.
- Contract validation occurs before business logic.
- Errors use one consistent shape.

## Root event

```json
{
  "version": "2.0.0",
  "article": {},
  "analysis": {},
  "research": {},
  "styleRag": {},
  "writingMemoryContext": {},
  "promptContext": {},
  "draft": {},
  "review": {},
  "publication": {},
  "feedback": {},
  "metadata": {}
}
```

## Ownership

| Section | Owner workflow |
|---|---|
| `article` | ingestion pipeline |
| `analysis` | content analyzer |
| `research` | research agent |
| `styleRag` | style RAG |
| `writingMemoryContext` | style memory retriever |
| `promptContext` | shared prompt builder |
| `draft` | writer agent |
| `review` | reviewer agent |
| `publication` | publisher |
| `feedback` | feedback collector |
| `metadata` | shared; append-only by convention |

## Immutable upstream rule

A workflow must preserve all upstream sections.

Examples:

- `05-style-rag` may append `styleRag` but must preserve `article`, `analysis`, and `research`.
- `12-style-memory-retriever` may append `writingMemoryContext` but must preserve every existing section.
- `06-writer-agent` may append `draft` but must not rewrite `analysis`, `research`, `styleRag`, or `writingMemoryContext`.
- `07-reviewer-agent` may append `review`. Any revised article body belongs in `review.revisedDraft` or a later normalization step.

## Versioning

`version` uses semantic versioning.

- `2.x.x`: compatible with this root shape.
- A breaking root-field rename requires a new major version.
- Workflows must reject unsupported major versions.

## Section definitions

### article

```json
{
  "id": "source-specific-id",
  "source": "rss|webhook|telegram|manual|x",
  "url": "https://example.com/article",
  "title": "Source title",
  "language": "zh-TW",
  "author": "",
  "publishedAt": "",
  "content": "Normalized source content",
  "images": [],
  "tags": []
}
```

Required when the pipeline reaches analysis:

- `id`
- `source`
- `url`
- `content`

### analysis

```json
{
  "topic": "",
  "coreIdea": "",
  "audience": "",
  "score": 0,
  "shouldWrite": false,
  "angles": [],
  "keywords": [],
  "researchQuestions": [],
  "riskNotes": []
}
```

### research

```json
{
  "query": "",
  "sources": [],
  "sourceCount": 0,
  "summary": "",
  "notes": ""
}
```

### styleRag

```json
{
  "query": "",
  "collection": "medium_style_chunks_v2",
  "model": "nvidia/llama-nemotron-embed-1b-v2",
  "matches": [],
  "matchCount": 0
}
```

### writingMemoryContext

```json
{
  "query": "",
  "collection": "writing_memory_v1",
  "memories": [],
  "memoryCount": 0,
  "mergedRules": [],
  "avoidPhrases": [],
  "preferredPatterns": []
}
```

### promptContext

```json
{
  "systemPromptId": "writer-v2",
  "enabledRules": [],
  "temperature": 0.4,
  "maxTokens": 4000,
  "assembledPrompt": ""
}
```

### draft

```json
{
  "title": "",
  "subtitle": "",
  "summary": "",
  "tags": [],
  "markdown": "",
  "wordCountEstimate": 0
}
```

### review

```json
{
  "score": 0,
  "approved": false,
  "issues": [],
  "revisionNotes": [],
  "revisedDraft": {}
}
```

### publication

```json
{
  "provider": "github",
  "repository": "",
  "branch": "",
  "path": "",
  "fileUrl": "",
  "commitUrl": "",
  "action": "created|updated"
}
```

### feedback

```json
{
  "feedbackId": "",
  "editorialDiff": {},
  "metrics": {}
}
```

### metadata

```json
{
  "eventId": "",
  "eventType": "",
  "createdAt": "",
  "updatedAt": "",
  "timezone": "Asia/Taipei",
  "language": "zh-TW",
  "currentWorkflow": "",
  "status": "",
  "history": []
}
```

`history` is append-only by convention.

Each entry:

```json
{
  "workflow": "06-writer-agent",
  "version": "2.0.0",
  "status": "drafted",
  "timestamp": "2026-07-16T00:00:00.000Z"
}
```

## Error contract

A workflow failure should emit or log:

```json
{
  "version": "2.0.0",
  "error": {
    "code": "PHOENIX_CONTRACT_INVALID",
    "message": "Human-readable message",
    "workflow": "contract-validator",
    "details": []
  },
  "metadata": {
    "status": "error",
    "updatedAt": "2026-07-16T00:00:00.000Z"
  }
}
```

## Validator behavior

The shared validator:

1. Accepts either a raw event or a webhook body.
2. Rejects unsupported major versions.
3. Creates missing optional root sections as empty objects.
4. Ensures `metadata` exists.
5. Adds default metadata fields.
6. Appends a validation entry to `metadata.history`.
7. Returns the normalized event.

## Compatibility rule

A workflow is v2-compatible when:

- input validates against `schemas/phoenix-event.schema.json`
- output preserves all input root sections
- output only changes its owned section plus metadata
- output keeps `version` at `2.x.x`
