# 05 Style RAG

## Responsibility

This workflow:

1. Receives the researched content item.
2. Builds a semantic style query.
3. Creates a multilingual query embedding through NVIDIA NIM.
4. Searches the `medium_style_chunks` collection in Qdrant Cloud.
5. Returns the most similar historical writing excerpts.
6. Checks whether the configured Qdrant collection exists.
7. Creates it automatically when missing.
8. Uses vector size `2048`.
9. Uses cosine distance.
10. Continues to embedding and similarity search.


It does not import Medium articles or write the new article.

## Required n8n Credentials

### NVIDIA NIM Bearer Auth

- Credential type: Bearer Auth
- Token: NVIDIA API key
- Assign this credential to `CreateQueryEmbedding`

### Qdrant API Key

- Credential type: Header Auth
- Header name: `api-key`
- Header value: Qdrant Cloud API key
- Assign this credential to `QueryQdrantStyle`

The API keys are encrypted by n8n and are not stored in Workflow JSON.

## Required node configuration

Open `SetRagConfig` and replace:

```text
https://YOUR-QDRANT-CLUSTER.cloud.qdrant.io
```

with the cluster URL shown in Qdrant Cloud.

The collection must use vectors produced by the same embedding model and dimension as this query workflow.

Default model:

```text
nvidia/llama-nemotron-embed-1b-v2
```

Default vector size: 2048.

## Default collection:

```text
medium_style_chunks_v2
```

## Assign the same Qdrant Header Auth credential to:

- `CheckQdrantCollection`
- `CreateQdrantCollection`
- `QueryQdrantStyle`


## Manual test

1. Configure both credentials.
2. Replace the Qdrant URL.
3. Confirm the collection exists and contains payload fields such as `title`, `url`, and `text`.
4. Run `ManualTest`.
5. Confirm `styleRag.matches` and `metadata.status = style_retrieved`.

An empty `matches` array is valid when the collection has no sufficiently similar points.
