# 05a Medium Style Importer

## Responsibility

This workflow indexes historical Medium articles into Qdrant Cloud.

1. Fetch Medium RSS.
2. Parse article HTML from RSS items.
3. Split articles into overlapping chunks.
4. Create NVIDIA passage embeddings.
5. Upsert points into `medium_style_chunks_v2`.

NVIDIA requires `input_type: passage` while indexing. The query workflow uses `input_type: query`. Qdrant stores each point as a vector plus payload.

## Required n8n Credentials

### NVIDIA NIM Bearer Auth
Assign to `CreatePassageEmbedding`.

### Qdrant API Key
Credential type: Header Auth.
Header name: `api-key`.
Assign to `UpsertQdrantPoint`.

## Required configuration

Edit `SetImporterConfig`:

- `mediumRssUrl`
- `qdrantBaseUrl`

The target collection must already exist. Run `05-style-rag` v0.5.2 once to create it automatically, or create it manually with vector size 2048 and Cosine distance.

## Limitation

Medium RSS usually exposes only recent posts, not a complete account archive. This MVP imports whatever the RSS feed returns. Older articles can later be submitted through a URL-list importer.

## Test

Run `ManualTest`. Every final item represents one imported chunk.
