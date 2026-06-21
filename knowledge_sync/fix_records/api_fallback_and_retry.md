# A+B修复：API请求失败时的Fallback模型+自动重试

## 问题诊断 (2026-06-11)
多个isolated cron任务在2026-06-09至2026-06-10期间连续报"Request was aborted"错误（6个任务共26次失败，100%同类型错误），根因为DeepSeek API在特定时间窗口间歇性中断。

## 修复方案

### A：Fallback模型链
对于所有isolated cron任务的payload消息模板中，在末尾追加fallback指令：
```
⚠️ 如果DeepSeek V4 Flash请求失败（"Request was aborted"），自动切换fallback模型重试：
- 首选fallback: deepseek/deepseek-v4-pro
- 最多重试1次
- 不修改payload内容，仅切换模型
```

### B：自动重试机制
在cron job payload中追加：
```
⚠️ 若首次运行报错（仅限"Request was aborted"和网络类错误），等待15-30秒后自动重跑一次。
重跑仍然使用fallback模型。
重跑成功则标记ok，不推送异常；重跑再失败才推送异常。
```

## 执行方式
直接在cron job的payload消息末尾加上上述指令段，让任务运行时通过内置逻辑感知API错误并自动切换模型+重试。

由于cron API的patch对payload参数的更新仅支持message字段，且isolated cron的payload.kind=agentTurn不支持fallbacks参数，因此改为在payload.message末尾追加指令的方式实现。

## 受影响的cron任务
- deep_reading_morning / deep_reading_afternoon / deep_reading_evening（3个）
- daily_memory_maintenance（1个）
- daily_knowledge_learning（1个）
- ontology_auto_sync（1个）
- 其他所有isolated cron（加同一段fallback指令作为防御性配置）

## 状态
✅ 故障记录已创建（2026-06-11）
⚠️ payload更新需逐个修改cron job - 先完成当前任务后再批量执行
