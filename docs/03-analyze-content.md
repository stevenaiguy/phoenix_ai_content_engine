# 03 Analyze Content

## Responsibility

This workflow:

1. Accepts one normalized content item.
2. Builds a strict JSON-only analysis prompt.
3. Calls OpenRouter first.
4. Falls back to NVIDIA NIM when the primary response fails or is invalid.
5. Merges the structured analysis into the content contract.

It does not perform research, RAG, article writing, or publishing.

## Required n8n Credentials

- OpenRouter Bearer Auth
- NVIDIA NIM Bearer Auth

API keys must not be stored in Workflow JSON, GitHub, Set nodes, Code nodes, or plain headers.

`NVIDIA_NIM_MODEL` must be a model ID currently available in the user's NVIDIA Build account.

## Manual test

Run `ManualTest`.

Expected final fields:

- `score`
- `shouldWrite`
- `analysis.topic`
- `analysis.coreIdea`
- `analysis.angles`
- `metadata.provider`
- `metadata.status = analyzed`

## Fallback behavior

OpenRouter is considered invalid when:

- HTTP status is not 2xx.
- The response cannot be parsed as JSON.
- `score` is missing or non-numeric.
- `shouldWrite` is not boolean.

In those cases, the workflow calls NVIDIA NIM once.
