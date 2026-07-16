# 10 Learning Agent

## Responsibility

This workflow:

1. Accepts the output of `09-feedback-collector`.
2. Uses OpenRouter first and NVIDIA as fallback.
3. Extracts reusable writing preferences.
4. Produces a stable writing memory contract.
5. Does not directly update prompts or Qdrant.

## Required n8n Credentials

- `OpenRouter Bearer Auth` on `CallOpenRouterLearning`
- `NVIDIA NIM Bearer Auth` on `CallNvidiaLearning`

## Webhook

- Method: `POST`
- Path: `/webhook/phoenix/learn`

## Output

The final output contains:

- `memoryId`
- `writingMemory.rules`
- `writingMemory.avoidPhrases`
- `writingMemory.preferredPatterns`
- `writingMemory.summary`
- `metadata.status = memory_generated`

## Confidence rule

Because one article is weak evidence, the prompt instructs the model not to assign confidence above `0.65` for single-article observations.

## Manual test

Run `ManualTest`.

Expected learned preferences include:

- question-style titles
- avoiding generic AI phrases
- more direct openings
- conversational CTA
