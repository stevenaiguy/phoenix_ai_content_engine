# 08 Publisher

## Responsibility

This workflow:

1. Accepts only approved articles.
2. Builds a Markdown file with YAML front matter.
3. Checks whether the target draft already exists.
4. Creates or updates the draft through the GitHub Contents API.
5. Returns file and commit URLs.

It does not publish directly to Medium.

## Required n8n Credential

Create a Header Auth credential:

- Name: `GitHub API Token`
- Header name: `Authorization`
- Header value: `Bearer YOUR_GITHUB_TOKEN`

Assign the same credential to:

- `CheckExistingDraft`
- `CommitDraftToGitHub`

The token should have permission to write repository contents.

## Configuration

Edit `SetPublisherConfig`:

- `githubOwner`
- `githubRepo`
- `githubBranch`
- `draftDirectory`

Default repository:

```text
stevenaiguy/phoenix_ai_content_engine
```

Default draft directory:

```text
drafts
```

## Webhook

- Method: `POST`
- Path: `/webhook/phoenix/publish`

## Manual test

Run `ManualTest`.

Expected final fields:

- `publication.repository`
- `publication.path`
- `publication.fileUrl`
- `publication.commitUrl`
- `publication.action`
- `metadata.status = published_to_drafts`
