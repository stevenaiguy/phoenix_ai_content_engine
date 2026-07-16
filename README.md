# Phoenix AI Content Engine

以 n8n Community Edition 為協調核心的個人內容 Agent。

## 固定技術棧

- n8n：VPS 自架
- 時區：Asia/Taipei
- 主模型：OpenRouter 免費模型
- 備援：NVIDIA NIM 免費額度
- RAG：Qdrant Cloud Free
- 來源：Webhook、RSS、Telegram
- 草稿：Markdown / GitHub
- 通知：Slack 或 Discord
- 發布：人工確認後貼至 Medium

## 開發原則

1. 除既有 VPS 成本外，優先使用免費額度與開源服務。
2. 所有 n8n Workflow 必須提供可直接匯入的 JSON。
3. API Key 不進入 Git；只在 n8n Credentials 或 VPS 環境變數中設定。
4. OpenRouter 失敗、限流或輸出無效時，切換 NVIDIA NIM。
5. X 不依賴官方付費 API；以 Webhook、Telegram 與 RSS 為主要入口。
6. 每天最多產出一篇草稿，避免耗盡免費模型額度。
7. Medium 歷史文章只保存文字切塊與 metadata，不保存圖片 binary。

## 專案階段

- v0.1 Foundation
- v0.2 Source Collector
- v0.3 Research Agent
- v0.4 Style RAG
- v0.5 Writer Agent
- v0.6 Reviewer
- v0.7 Publisher
- v0.8 Learning Agent

## 目前內容

此版本建立 Repository 骨架、設定、資料 Schema、Analyzer Prompt 與驗證腳本。
已加入第一個以 n8n 2.29.7 為目標的 `workflows/00-bootstrap.json`。
