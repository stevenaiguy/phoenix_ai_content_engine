# 00-Bootstrap 測試

1. 在 n8n 2.29.7 開啟 **Workflows → Import from File**。
2. 匯入 `workflows/00-bootstrap.json`。
3. 執行 `ManualTrigger`。
4. `ValidateRuntimeConfig` 應輸出 `status: ready`。
5. 在正式串接 NVIDIA 前，請將 `BuildRuntimeConfig.fallbackModel` 改成 NVIDIA Build 帳號中目前可用的模型 ID。
6. 此 Workflow 不保存 API Key；Credentials 會在後續 Provider Workflow 中建立。

預期輸出包含：

- `timezone: Asia/Taipei`
- `primaryProvider: openrouter`
- `primaryModel: openrouter/free`
- `fallbackProvider: nvidia`
- `qdrantCollection: medium_style_chunks`
- `status: ready`
