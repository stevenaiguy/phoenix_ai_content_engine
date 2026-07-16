# 11 Style Memory Updater

## Responsibility

This workflow:

1. Accepts `writingMemory` from `10-learning-agent`.
2. Builds a compact memory document.
3. Creates a NVIDIA passage embedding.
4. Creates the Qdrant collection when missing.
5. Stores the writing memory as a Qdrant point.

It does not rewrite the Writer Prompt directly.

## Required n8n Credentials

### NVIDIA NIM Bearer Auth

Assign to:

- `CreateMemoryEmbedding`

### Qdrant API Key

Credential type: Header Auth

- Header name: `api-key`
- Header value: Qdrant Cloud API key

Assign to:

- `CheckMemoryCollection`
- `CreateMemoryCollection`
- `UpsertWritingMemory`

## Configuration

Edit `SetMemoryConfig`:

- `qdrantBaseUrl`
- `collection`

Default collection:

```text
writing_memory_v1
```

The collection uses:

- vector size: 2048
- distance: Cosine
- embedding model: `nvidia/llama-nemotron-embed-1b-v2`

## Webhook

- Method: `POST`
- Path: `/webhook/phoenix/style-memory/update`

## Manual test

Run `ManualTest`.

Expected final fields:

- `memoryStorage.provider`
- `memoryStorage.collection`
- `memoryStorage.pointId`
- `metadata.status = memory_stored`
