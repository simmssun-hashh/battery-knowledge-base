

--- Page 1 ---

🦞
OpenClaw 完 全 指 南
从原理到实现 的 专家 级解 析
减肥的拉 格朗 日
cyber_newair@163.com
版本  1.0.1 | 2026年 2 月

--- Page 2 ---

ii目 录
第1章  OpenClaw 概 述
1.1 什么是  OpenClaw
1.2 AI Agent 技 术 演 进
1.3 OpenClaw 核 心能力
1.4 适用场 景与人 群
1.5 与自动驾 驶 的 技 术 同 源 性
第2章  核 心 架 构
2.1 架构总 览
2.2 Gateway 详 解
2.3 Agent Runtime 工作机制
2.4 通信协 议
2.5 为什么  OpenClaw 会 火
第3章  OpenClaw 工作 原 理
3.1 Agent Loop 详 解
3.2 工具系 统
3.3 记忆系 统
3.4 规划与推理
第4章  核 心 功 能 深 度 解 析
4.1 内存系 统 深度 解 析
4.2 多代理系 统
4.3 技能系 统
4.4 安全与权 限
4.5 本章小 结
第5章  进 阶 主题

--- Page 3 ---

iii5.1 多代理高 级 配 置
5.2 性能优化
5.3 调试与监控
5.4 沙箱与安全 配 置
5.5 生产环境部 署
第6章  实 践 指 南
6.1 安装指 南
6.2 配置详 解
6.3 实战案例
6.4 故障排 除
第7章  生 态 与 创 业
7.1 Skill 开发 指 南
7.2 社区参与
7.3 创业方 向
7.4 未来展望

--- Page 4 ---

4第1章  OpenClaw 概 述
1.1 什么是  OpenClaw
1.1.1 定义与定位
OpenClaw（发音： / ˈ o ʊ p ə nkl ɔ ː / ）是 一 个开 源 的自托管个人  AI 助 手 网 关（Self-Hosted Personal
AI Agent Gateway ） ， 其 核 心 功 能是 将 主 流即 时通 讯应 用（如  Telegram 、 Discord 、 WhatsApp 、
Slack、 iMessage 、 Feishu 等）与大 型 语 言 模 型 （ LLM ） 驱 动 的  AI 代 理进行 桥 接1。
OpenClaw 的核心定位可 归纳 为以下 四 个 维 度 ：
自托管（ Self-Hosted ）：OpenClaw 运行于用户自主 控 制 的 基 础 设 施 之上（个人服务 器 、 NAS 、
云主机或本地机 器 ） ， 所 有 对话数 据 、 记 忆 存 储 、 配 置 文 件 均 保 留 在本地 环 境 中， 无 需 依 赖 第 三方  SaaS
服务的数 据托 管2。
多通道（ Multi-Channel ）：单一  OpenClaw 网 关实 例 可同时接入多个 异 构 通 讯 平 台 ， 实现 跨 平
台消息的 统 一 路由 与 响 应 ， 支持 平 台原 生特性 的 适 配 （如  Discord 的 线 程 、 Telegram 的 回 调 按 钮 、
Slack 的块 级消息 格 式） 。
代理原生（ agent-native ）：系统架 构专为  AI Agent 工作 模 式 设计 ， 原 生 支持 工 具 调 用（ Tool
Use）、会话状 态管 理 、 长 期记 忆 （ Long-term Memory ） 、 多 代 理 协 作（ Multi-Agent ）等高 级 功
能，而非 简单 的  LLM API 封 装 。
开源开放（ Open Source ）：项目采用  MIT 许 可 证 开 源 ， 代码 托 管 于  GitHub ， 允 许 自 由 修改 、
分发及商业 使用 ， 已 形 成活 跃 的 开发者社区与技能生 态 市 场 （ ClawHub ）3。
1.1.2 吉祥物含义
OpenClaw 的吉 祥 物为龙虾（Lobster ， 🦞） ， 其 命 名与 象 征 意 义 蕴 含 多 层 技 术 隐 喻 ：

--- Page 5 ---

5象征维
度龙虾特性 技术映射
持续成
长龙虾通过 蜕 壳实现体 型 增 长 ，一 生
可蜕壳数 十次AI 助手的 持续学习 能力 ， 通过 新 技能（ Skills ）加 载 与 模
型更新实现 功能 迭 代
多任务
处理龙虾拥有多对 螯 足 ， 可同时进行 探
索、捕食 、防 御多工具并行 调用（ Multi-Tool Use ） ， 同时 执 行文 件 操
作、网络 搜索 、 代码 执 行等 任 务
环境适
应龙虾分布于淡 水 至深 海 多 种 生 态 环
境跨平台适 配能力 ， 可在  macOS 、 Linux 、 Windows 、
Docker 及 嵌入式 设 备 运 行
开放掌
控"Open" + "Claw" = 开 放 的 掌 控用户对数 据与 逻辑 的 完 全 控 制权 ， 区 别 于 封 闭 的 黑 盒 商 业
服务
该命名策略体现了开 源 社区 常见 的具象化隐 喻设计范式 ——通过生物特 征 映 射 技 术 特性 ， 降 低 概 念
理解门槛 的同时增 强 品 牌 辨 识 度 。
1.1.3 技术 栈 构成
OpenClaw 采用多 语 言 混 合 架 构 ， 各组 件 依 据 平 台 特性 选 择 最 优 实现 ：
技术栈构成（基于  GitHub 仓库分析）：
├── TypeScript —— 核⼼⽹关、 Agent 运⾏时、⼯具系统的主要实现语⾔
├── Swift —— macOS/iOS 原⽣应⽤与系统级集成
├── Kotlin —— Android 客户端应⽤
├── Shell —— 安装脚本与运维⼯具
├── Python —— 部分机器学习⼯具与数据科学技能
└── Rust —— 性能关键模块（可选编译扩展）
TypeScript 作为主 导 语 言 的 选 择基 于以下技 术 考 量 ：
1. 运行时效率：Node.js 的 事件 驱 动 非 阻 塞  I/O 模 型 与 网 关 的 高 并 发 消 息 处 理 需 求 高度 契 合
2. 类型安全：静态类 型系 统 确 保复 杂 配 置结 构 与 协 议 接 口 的 正 确 性
3. 生态丰富：npm 生 态提 供 大 量 通 讯 协 议 库 （discord.js、telegraf、@slack/bolt 等）
4. 开发体验：现代语 言特性（ Async/Await 、 Decorator 、 泛 型 ）提 升 代码 可 维护 性

--- Page 6 ---

61.2 AI Agent 技 术 演 进
1.2.1 三代  Agent 技 术 对 比
AI Agent 技 术 的发 展 经 历 了三个明 显 阶 段 ， 每 一 代 在技 术 范 式 、 能力 边 界 与 应 用 场 景 上 均 存 在本 质
差异4：
第一代： 符号  Agent （ Symbolic Agent ， 1990s-2000s ）
符号  Agent 基于物理符号系 统假说（Physical Symbol System Hypothesis ） ， 将 智 能体 建 模 为
通过符号操作进行推理 的 符 号 处 理 器 。 其 核 心特 征 包 括 ：
知识表示：采用谓词 逻辑 （ Predicate Logic ） 、 语 义 网 络 （ Semantic Network ） 、 框 架
（Frame）等 形式化 结 构存 储 领 域 知 识
推理机制：基于规则 引 擎（ Rule Engine ） 或 专家系 统 （ Expert System ）进行 确 定性 或 概 率 性推
理
规划方法：依赖符号 规划算 法（如  STRIPS 、 HTN ） ， 通过 状 态空 间 搜索 生成行动 计 划
代表性系 统包括  Shakey （ SRI ， 1966 ） 、 SOAR （ Laird et al., 1987 ） 、 ACT-R （ Anderson,
1993）。 该范式 的 局 限 在于知识获取 瓶 颈（Knowledge Acquisition Bottleneck ）与符号接地问题
（Symbol Grounding Problem ） —— 难 以 处 理开 放 域 的 自 然 语 言 与 感 知数 据 。
第二代： 统计  Agent （ Statistical Agent ， 2000s-2020s ）
随着机器学习兴 起 ， Agent 技 术转 向 数 据 驱 动 的 统计 学 习 方法 ：
感知能力：基于计算机视觉 （ CNN ） 、 语音识 别 （ HMM/ 深 度学 习 ）实现 环 境 感 知
决策模型：采用强化学习（ Reinforcement Learning ， RL ） 训练 策 略 网 络 ， 代 表作 包 括  Deep Q-
Network（ DQN, 2015 ） 、 AlphaGo （ Silver et al., 2016 ）
自然语言 处理：从统计机 器翻 译 （ SMT ） 演 进 至神 经机 器 翻 译 （ NMT ） ， 引 入注意力机制
（Attention）
该阶段的  Agent 在特定 任 务（ 游 戏 、 机 器 人 控 制）上 取得 突破 ， 但存 在任务特化（Task-Specific）
与样本低效（Sam ple Inefficiency ）问题 ， 难 以 迁 移 至 开 放 域 的 通用 任 务 。
第三代： LLM-based Agent （ 2020s- 至今 ）
以 GPT 系 列 、 Claude 系 列 为 代 表 的 大 型 语 言 模 型 （ LLM ） 催 生了 新一 代  Agent 范 式 ， 其 核 心 创
新在于将  LLM 作为认知中枢（Cognitive Core ） ， 通过 涌 现能力（ Emergent Capabilities ）实现通
用任务处理 ：

--- Page 7 ---

7┌─────────────────────────────────────────────────────────────────┐
│                    LLM-based Agent 架构                           │
├─────────────────────────────────────────────────────────────────┤
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐       │
│  │   ⼯具系统     │ ◄ ── ► │  LLM 认知中枢  │ ◄ ── ► │   记忆系统     │       │
│  │  (Tools)     │    │  (Core)      │    │  (Memory)    │       │
│  └──────────────┘    └──────────────┘    └──────────────┘       │
│         ▲                    │                   ▲                │
│         │                   ▼                    │               │
│         │            ┌──────────────┐           │               │
│         └─────────── ► │  规划与推理    │ ◄ ──────────┘               │
│                      │ (Planning)   │                           │
│                      └──────────────┘                           │
└─────────────────────────────────────────────────────────────────┘
三代技术对 比如下表所 示 ：
维度 符号  Agent 统计  Agent LLM-based Agent
核心引擎 规则引擎 /专家系 统 神经网络 / 强化学习大语言模 型（ Transformer ）
知识获取人工编码 /知 识工 程监督 /强化学习 训练预训练  + 上下文学 习
泛化能力 封闭域、 脆弱 任务特化 、难 迁移开放域、 强 泛化
可解释性高（符号推理 链） 低（黑盒 网 络） 中（思维链可追 溯 ）
人机交互命令行 /结 构化接 口 有限的自 然 语 言 原生自然 语 言对话
工具使用预定义  API 调用 需专门训练 零样本 /少样本工 具 调 用
记忆机制 静态知识库 无显式记忆 动态上下文  + 向 量记 忆
代表系统 SOAR、 ACT-R AlphaGo 、 DQN AutoGPT 、 OpenClaw
1.2.2 传统  Agent 与现 代  LLM-based Agent 的 本 质 差异
从系统架 构视角审 视 ， 两 类  Agent 存 在 根 本性 设计 哲 学 差异 ：
控制流架 构差异
传统  Agent 采用预定义控制 流（Predefined Control Flow ） ： 开发者 显 式 编程 状 态 机 、 规 则 优先
级与决策分 支 ， Agent 的 行为 空 间 被 严 格 约 束 在 设计 者 预 见 的 范围 内 。 例 如 ， 经 典 的 三 层架 构 （ 感 知 - 决
策-执行） 中， 每 一 层 的 接 口 与数 据 格 式 均 需 人工 规 约 。

--- Page 8 ---

8LLM-based Agent 采 用涌现控制 流（Emergent Control Flow ） ： 控 制 逻 辑 不 再 硬 编码 ， 而 是 由
LLM 根据 任务上下文动 态 生成 。 ReAct （ Reasoning + Acting ） 范 式5 是典型代表 ， LLM 在 思 考
（Thought）与行动（ Action ）之间 交 替 迭 代 ， 形 成自 适 应 的 问题 解 决 路 径 。
知识管理差异
传统  Agent 依 赖显式知识库（Explicit Knowledge Base ） ， 知 识 以 结 构 化 形 式（数 据库 、 本体 、
规则集） 存储 ，更 新 需 人工 干预 或 专门 的 机 器 学 习 流程 。
LLM-based Agent 通过参数化知 识  + 上下文 检 索（Parametric Knowledge + In-Context
Retrieval） 管理知 识 ： 世界 知 识 编码 于 模 型 参 数 中， 任 务特定知 识 通过提 示 工 程 （ Prompt
Engineering） 或 检 索 增 强 生成（ RAG, Retrieval-Augmented Generation ）动 态 注入 。
错误处理差异
传统  Agent 的错误 处 理 依 赖异常捕获与回退策 略（Exception Handling & Fallback ） ， 需 预 先 定
义所有可能 的失败 模 式与 恢 复 逻 辑 。
LLM-based Agent 具 备自纠错能力（Self-Correction ） ： 通过 观 察 工 具 执 行 结 果
（Observation） ， LLM 可自主 识 别 错 误 、 分 析 原 因 并 调整 策 略 。 例 如 ， 当 代码 执 行报 错 时 ， Agent 可
将错误信息 反馈 给  LLM ， 生成 修 正后 的 代码重 试 。
1.2.3 涌现能力 ： LLM 作为  Agent 认 知 中 枢 的 基 础
LLM 之所以能成为现 代  Agent 的 认 知 中 枢 ， 源 于其在大 规 模 预 训练 过 程 中 涌 现 的 四 项 关 键 能力6：
上下文学习（ In-Context Learning, ICL ）
ICL 指  LLM 无 需参 数更 新， 仅 通过提 示 中的 少量示 例 （ Few-Shot Examples ） 即 可学 习 任 务 模 式
并泛化至 新输入 的 能力 。 形 式化定 义 为 ： 给 定 任 务分 布  $T、提示  $P = (x_1, y_1, ..., x_k, y_k,
x_{query})，LLM 生成  $y_{query}$ 的 概 率 可表 示 为 ：
$P(y_{query} | x_{query}, P) = \prod_{t=1}^{|y_{query}|} P_\theta(y_t | y_{<t}, x_{query}, P)$
其中   为冻结的 模 型 参数 。 ICL 使  Agent 能 够 快 速 适 应 新 工 具 、新 格 式与 新 任 务 ， 无 需 微 调 成本 。
思维链（ Chain-of-Thought, CoT ）
CoT 指  LLM 通过生成 显 式推理 步 骤 （ "Let's think step by step" ） 解 决 复 杂 问题 的 能力7。研究表
明，在提 示 中加入 " 逐 步 思 考 " 的 指 令 ， 可 显 著 提 升  LLM 在多 步 数学推理 、 逻 辑 谜 题与 决策 规 划 任 务上 的
表现。θ

--- Page 9 ---

9在 Agent 场 景 中， CoT 实现了可解释的决策过 程：LLM 不仅输出最 终 行动 ， 还 展示 推理 路 径 ， 便
于调试与审 计 。 OpenClaw 的  Agent Loop 中， 每 个 迭 代 周 期 均 包 含 推理（ Reasoning ） 步 骤 ， 即  CoT
的工程化 应用 。
指令遵循（ Instruction Following ）
现代  LLM 经过 指 令微 调 （ Instruction Tuning ）与 基 于人类 反 馈 的 强 化学 习 （ RLHF ） ， 能 够 理
解并执行自 然 语 言 指 令 ， 即使任 务在 训练 时 未 曾 见 过 。 这 一 能力 使  Agent 可通过高 层 语 义 描述 （如 " 帮
我整理本 周 邮件并 按 优先 级 分类 " ） 触 发 复 杂 行为 链 ， 无 需低 层  API 调 用 序 列 。
工具使用（ Tool Use ）
工具使用是  Agent 范 式 的 核 心能力 ， 指  LLM 识 别何 时 需 要外部工 具 、 选 择 合 适 工 具 、 构造调 用 参
数并解析 结果 的能力8。典型的工 具使用 流程 如下 ：
┌─────────────────────────────────────────────────────────────────┐
│                     ⼯具使⽤循环（ Tool Use Loop ）                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ⽤户输⼊  ── ►  LLM 推理  ── ►  [ 需要⼯具 ?] ── ►  ⽣成⼯具调⽤           │
│                               │            (JSON/Function Call) │
│                               ▼                                  │
│                          [ ⽆需⼯具 ]                             │
│                               │                                 │
│                               ▼                                  │
│  最终结果  ◄ ── LLM 再推理  ◄ ── ⼯具执⾏结果  ◄ ── 执⾏⼯具             │
│     ▲             │                                              │
│     └────────────┘                                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
OpenClaw 的工 具 系 统 （ Tool System ） 即 基 于 此 能力 构 建 ， 支持 函 数 调 用（ Function
Calling） 、 代码解 释 器 （ Code Interpreter ） 、 浏 览器 控 制（ Browser Control ）等多 种 工 具 类 型 。
1.3 OpenClaw 核 心能力
基于前述技 术背 景 ， OpenClaw 构 建 了面 向 生产 环 境 的 完 整  Agent 能力 栈 ：
1.3.1 多通道通信 网 关
OpenClaw 的网关 层 （ Gateway Layer ）实现了通 讯 协 议 的 抽 象 与 统 一：

--- Page 10 ---

10平台 类型 支持特性
Telegram内置 消息编辑 、回 调按 钮 、 内联 查 询 、 文 件传 输
Discord内置 线程、嵌入 消息 、 斜 杠 命 令 、 角 色 权 限
Slack 内置 块级消息 、 Home Tab 、 Shortcut 、 Workflow
WhatsApp内置 模板消息 、媒体 消 息 、 状 态 跟 踪
IRC 内置 频道消息 、私 聊 、 文 件传 输
Google Chat内置 卡片消息 、群 聊 、 线 程 回 复
Feishu 插件 卡片消息 、群机 器 人 、 审批 集 成
BlueBubbles 插件（推 荐） iMessage 桥接 ， 原 生 消 息体 验
iMessage内置（ legacy） macOS 私 有 协 议 ， 原 生 消 息体 验 （ 已 弃 用 ， 推 荐  BlueBubbles ）
Email 内置 收发邮件 、 附 件 处 理 、 HTML 渲 染
Signal 插件 端到端加 密 消息
Mattermost 插件 企业级消息 协作
Microsoft Teams插件 企业协作与会 议
更多平台 插件 Matrix、 LINE 、 Twitch 、 Zalo 等
网关层通过适配器模式（Adapter Pattern ） 封 装 各 平 台 差异 ， 向  Agent 层暴 露 统 一的 消 息接 口 。
核心接口定义如下 ：

--- Page 11 ---

11// ⽹关消息接⼝定义（概念示例）
interface GatewayMessage {
  id: string;
  platform: Platform;           // telegram | discord | slack | ...
  channel: ChannelInfo;         // 频道 / 群组 / 私聊信息
  author: AuthorInfo;           // 发送者信息
  content: MessageContent;      // ⽂本 / 媒体 / 富⽂本内容
  timestamp: number;
  threadId?: string;            // 线程 / 话题  ID
  replyTo?: string;             // 回复消息  ID
  metadata: PlatformMetadata;   // 平台特定元数据
}
interface GatewayAdapter {
  name: string;
  connect(): Promise<void>;
  disconnect(): Promise<void>;
  send(message: OutboundMessage): Promise<void>;
  onMessage(handler: (msg: GatewayMessage) => void): void;
}
1.3.2 持久化 记 忆 系 统
OpenClaw 实现了分 层 记 忆 架 构 ， 平 衡 上下文长度 限 制与长 期 信息 保 留 ：
短期记忆（ Short-Term Memory ）
维护当前会话 的 完 整 对话 历 史 ， 受  LLM 上下文 窗 口 （ Context Window ） 约 束 。 默 认保 留 最 近  20
轮对话， 支持 配 置 调整 。
长期记忆（ Long-Term Memory ）
基于向量数 据库（ Vector Store ）实现 语 义 检 索 ， 核 心 流程 ：
1. 存储：对话中的 重要信息经  LLM 提 取 为知 识 三 元 组 （实体 - 关系 - 实体） ， 编码 为 向 量 嵌 入
（Embedding）
2. 索引：采用  HNSW（ Hierarchical Navigable Small World ） 算 法 构 建 近 似 最 近 邻 （ ANN ） 索 引
3. 检索：用户查 询时 ， 计 算 查 询向 量 与 记 忆 库向 量 的 余 弦 相 似 度 ， 返 回  Top-K 相关 记 忆
代码实现 参考 ：

--- Page 12 ---

12// 记忆检索接⼝（概念示例）
interface MemoryEntry {
  id: string;
  content: string;
  embedding: number[];          // 向量嵌⼊（默认  1536 维）
  metadata: {
    timestamp: number;
    importance: number;         // 重要性评分（ 0-1 ）
    source: string;             // 来源会话 / ⽂档
    tags: string[];
  };
}
class VectorStore {
  async add(entry: MemoryEntry): Promise<void>;
  async search(
    query: string, 
    topK: number,
    filter?: MetadataFilter
  ): Promise<MemoryEntry[]>;
  async compress(threshold: number): Promise<void>;  // 记忆压缩
}
1.3.3 工具 执行系 统
OpenClaw 内 置  6 大类工 具 ， 覆 盖 常见 自动化 场 景 ：
工具类别 功能描述 典型用例
文件系统 读写文件 、 目录遍 历 、 权 限管 理 代码审查 、日志分 析 、 文 档 生成
Shell 执行命令执行 、 脚本 运 行 、 进 程管 理 系统运维 、 构 建部 署 、 数 据处 理
浏览器控制 网页浏览 、表 单填 充 、 截 图 信息检索 、自动化 测 试 、 数 据 抓 取
代码解释 器安全沙箱内 执行  Python/Node.js 数据分析 、图表生成 、 算 法 验 证
搜索检索 Web 搜索 、 语义 搜索 、 本地 搜索 实时信息 获 取 、知 识库 查 询
系统集成 REST API 调用 、 数 据库 查 询 、 消 息 队 列与外部服务 集成 、 数 据 同 步
工具注册 采用 声明式  Schema ：

--- Page 13 ---

13// ⼯具定义  Schema （概念示例）
interface ToolDefinition {
  name: string;
  description: string;          // LLM ⽤于理解⼯具⽤途
  parameters: JSONSchema;       // 参数结构定义（ JSON Schema ）
  handler: ToolHandler;         // 实际执⾏函数
  permissions?: Permission[];   // 权限要求
  timeout?: number;             // 超时时间（毫秒）
}
// 示例：⽂件读取⼯具
const readFileTool: ToolDefinition = {
  name: "read_file",
  description: " 读取指定路径的⽂件内容 ",
  parameters: {
    type: "object",
    properties: {
      path: { type: "string", description: " ⽂件路径 " },
      encoding: { type: "string", enum: ["utf8", "base64"] }
    },
    required: ["path"]
  },
  permissions: ["file:read"]
};
1.3.4 多代理系 统
OpenClaw 支持多 代 理（ Multi-Agent ） 架 构 ， 允 许 运 行多个 具 有 独 立 配 置 、 记 忆 与行为 的  Agent
实例：
路由机制：基于消息来 源（平 台 、 频 道 、 用户） 将 请 求路由 至 对 应代 理 。 路由规 则 支持 正 则 匹 配 、
条件表达式与 优先 级 配 置 。
代理间通信：代理可通过内部 消 息 总 线（ Message Bus ）进行 协 作 ， 支持任 务 委托 、 结 果 共享 与 状
态同步。
负载均衡：在高并发 场 景下 ， 同 一 代 理可 启 动多个工作进 程 （ Worker ） ， 由 网 关 层 进行请 求 分发 。
配置示例 ：

--- Page 14 ---

14// openclaw.json 多代理配置⽚段（概念示例）
{
  "agents": [
    {
      "id": "coding-assistant",
      "name": " 代码助⼿ ",
      "model": "claude-3-sonnet-20240229",
      "skills": ["github", "vscode", "docker"],
      "routes": [
        { "platform": "slack", "channel": "#dev-*" },
        { "platform": "telegram", "chatId": "-1001234567890" }
      ]
    },
    {
      "id": "personal-assistant",
      "name": " 个⼈助理 ",
      "model": "gpt-4o",
      "skills": ["calendar", "email", "reminders"],
      "routes": [
        { "platform": "imessage", "contact": "*" },
        { "platform": "telegram", "private": true }
      ]
    }
  ]
}
1.3.5 技能 扩 展系 统
技能（ Skills）是  OpenClaw 的 模 块 化 扩 展 机制 ， 每 个  Skill 是 一 个 封 装 特定 功 能 的 目 录 ， 包 含 工
具定义、 配 置文 件 与文 档 ：
skill-name/
├── SKILL.md           # 技能元数据与使⽤说明
├── package.json       # 依赖声明
├── src/
│   ├── tools/         # ⼯具实现
│   ├── hooks/         # ⽣命周期钩⼦
│   └── utils/         # ⼯具函数
└── config/
    └── schema.json    # 配置项校验  Schema
技能市场（ ClawHub ）提 供 社区 贡 献 的 技能 托 管 与分发 ， 支持 通过  CLI 一 键 安 装 ：

--- Page 15 ---

15# 安装 ClawHub CLI
npm i -g clawhub
# 安装社区技能
clawhub install spotify-player
clawhub install weather
# 查看已安装技能
clawhub list
# 更新所有技能
clawhub update --all
1.4 适用场 景与人 群
1.4.1 核心 应用 场 景
个人知识 管理
通过多通道接入 ， 用户可在 任何设 备 、 任何 平 台 与知 识库 交 互 。 OpenClaw 可 整 合理 思 源 笔 记 、
Obsidian 、 Notion 等知 识库 ， 实现自 然 语 言查 询 、 内 容 摘 要与 跨 文 档 关联分 析 。
开发辅助与  DevOps
开发者可通过  IM 直 接 触 发 代码 审 查 、日 志 分 析 、 部 署 操 作 。 典 型场 景 包 括 ：
发送  GitHub PR 链 接 ， Agent 自动 拉 取代码 、 运 行 静 态 分 析 、 生成 审 查 意 见
查询生产 环境 日志 ， Agent 聚 合多个服务 的日 志 并 提 取 异 常 模 式
通过自然 语 言 指令 触 发  CI/CD 流水 线（ " 部 署 前 端 服务到  staging 环 境 " ）
企业自动化工作 流
企业可部 署私 有  OpenClaw 实 例 ， 对接内部系 统 （ ERP 、 CRM 、 OA ） ， 实现 ：
审批流程 的智能预 审 （合同 条 款 检 查 、 报 销 单 据 审 核 ）
跨系统的数 据同 步 与报表生成
内部知识库 的智能问 答
多代理协作系 统
构建由多个  Specialist Agent 组 成 的 协 作 网 络 ：

--- Page 16 ---

16规划  Agent：任务分 解与资 源 协调
研究  Agent：信息搜集与资 料 整 理
执行  Agent：工具调用与操作 执 行
审查  Agent：结果校 验与 质量 把 关
1.4.2 目标用户画 像
用户类型 核心需求 使用模式
开发者 从任何设备通过 消 息 触 达 开发 环 境自托管  + 代码技能
隐私敏感用户 数据不出本地 ， 完 全可 控 内网部署  + 本地  LLM
技术爱好者 深入理解  AI Agent 原 理 源码编译  + 自定义 扩 展
中小企业 低成本自动化与知 识 管 理 Docker 部 署  + 技能市 场
自动驾驶 /AI 研究 者 快速原型 验 证与工 具集 成 多代理  + 自定义工 具
1.5 与自动 驾 驶 的 技 术 同 源 性
1.5.1 架构类 比
OpenClaw 与自动 驾 驶 系 统 在 架 构 设计 上 存 在 深 刻 的 同 源 性 ， 这 种 类 比 有 助 于 具 备自动 驾 驶 背 景 的
读者快速理 解  Agent 系 统 ：

--- Page 17 ---

17┌─────────────────────────────────────────────────────────────────────────────┐
│                        技术架构对⽐图                                          │
├─────────────────────────┬───────────────────────────────────────────────────┤
│     ⾃动驾驶系统          │              OpenClaw Agent 系统                   │
├─────────────────────────┼───────────────────────────────────────────────────┤
│  传感器层                 │  聊天应⽤接⼝层（ Telegram/Discord/Slack/... ）       │
│  （相机 / 激光雷达 / 毫⽶波）  │  ── ►  多源消息采集与预处理                           │
├─────────────────────────┼───────────────────────────────────────────────────┤
│  感知融合层               │  ⽹关适配层（ Gateway Adapter ）                      │
│  （⽬标检测 /跟踪 / 融合）    │  ── ►  协议转换与统⼀消息格式                         │
├─────────────────────────┼───────────────────────────────────────────────────┤
│  定位与地图               │  记忆系统（ Memory System ）                          │
│  （⾼精地图 /SLAM ）        │  ── ►  ⻓期记忆存储与向量检索                         │
├─────────────────────────┼───────────────────────────────────────────────────┤
│  决策规划层               │  LLM 认知中枢  + 规划模块                            │
│  （路径规划 / ⾏为决策）     │  ── ►  思维链推理与任务规划                           │
├─────────────────────────┼───────────────────────────────────────────────────┤
│  控制执⾏层               │  ⼯具执⾏层（ Tool Executor ）                        │
│  （横向 / 纵向控制）         │  ── ►  ⽂件操作 / 浏览器 / 代码执⾏ / 系统集成               │
├─────────────────────────┼───────────────────────────────────────────────────┤
│  ⻋辆执⾏机构             │  外部服务与系统                                     │
│  （转向 / 制动 / 驱动）        │  ── ►  实际业务系统（ GitHub/ 数据库 /API 服务等）        │
└─────────────────────────┴───────────────────────────────────────────────────┘
1.5.2 模块 功能 映 射
自动驾驶 模块 OpenClaw 对 应 模 块功能类比
多传感器融合多通道网关 汇聚异构输入 源（相机 ↔ 雷 达  ↔  Telegram ↔ Discord ）
环境感知工具系统 感知外部 环境状 态 （ 目标 检 测  ↔  Web 搜索 、 API 查 询 ）
高精地图长期记忆 提供先验知 识 支 撑 决策 （地图信息  ↔  用户 偏 好 、 历 史 对话）
轨迹规划 任务规划 生成行动序 列（行 驶 轨 迹  ↔  工 具 调 用 链 ）
运动控制工具执行 将规划转化为实 际 动作（ 转 向 角 / 加 速 度  ↔  文 件 写 / 命 令 执 行）
故障处理错误恢复 异常检测与恢 复（接 管 / 降 级  ↔  重 试 / 回 退 / 人工 确 认 ）
1.5.3 核心算法思 想 借 鉴
感知 -决策 - 执行 循 环

--- Page 18 ---

18自动驾驶 的经典控 制 循 环 （ Sense-Plan-Act ）与  OpenClaw 的  Agent Loop 在本 质 上 一 致 ：
⾃动驾驶:    感知环境  → 定位建图  → 轨迹规划  → 控制执⾏  → 状态反馈
                ↑                                            │
                └────────────────────────────────────────────┘
OpenClaw:    接收消息  → 记忆检索  → LLM 推理  → ⼯具调⽤  → 结果观察
                ↑                                            │
                └────────────────────────────────────────────┘
不确定性 处理
自动驾驶通过概率 图 模 型 （ 贝叶 斯 网 络 、 粒 子 滤 波 ） 处 理 感 知不 确 定性 ； OpenClaw 则 通过  LLM
的概率输出与多 采 样 推理 处 理 语 言 理 解 的 歧 义 性 。 两 者 均 需 在不 确 定性 条件 下 做 出最 优 决策 。
安全机制
自动驾驶 的 冗余 设计 （ 双  ECU 、 异 构 传感 器 、 功 能安全  ISO 26262 ） 启 发了  OpenClaw 的 多 层 安
全策略：
权限沙箱：工具执行 受 限于用户 配 置 的 权 限 边 界 （类 比 ： 车 辆 控 制权 限 分 级 ）
人工确认：敏感操作触发 确 认 请 求 （类 比 ： 自动 驾 驶 接 管 请 求 ）
审计日志：完整记录决策 链 与 执 行过 程 （类 比 ： 自动 驾 驶 黑 匣 子）
本章小结
本章从  OpenClaw 的 定 义 与定位出发 ， 系 统 梳 理了  AI Agent 技 术 的 三 代 演 进 脉 络 ， 详 细 解 析 了
LLM 作为 认知 中 枢 的 四 项 涌 现能力（上下文学 习 、 思 维链 、 指 令 遵 循 、 工 具使 用） 。 在 此 基 础 上 ， 全面
介绍了  OpenClaw 的 五 大 核 心能力 ： 多通道通信 网 关 、 持 久 化 记 忆 系 统 、 工 具 执 行系 统 、 多 代 理系 统 与
技能扩展系 统 。最后 ， 通过与自动 驾 驶 系 统 的 深 度类 比 ， 帮 助具 备相关 背 景 的 读 者 建立直 观 的 技 术认 知
框架。
OpenClaw 代表了个人  AI 助 手 的 工 程 化实现 范 式 —— 它 不是 简单 的 聊 天机 器 人 封 装 ， 而 是 一 个 完
整的基础 设施平 台 ， 将  LLM 的 认 知能力与 真 实 世界 的 数 字 工 具 进行可 靠 、 安全 、 可 扩 展 的 桥 接 。 后 续
章节将深入探讨其 架 构 设计 、 工作 原 理与 具 体实现 细 节 。

--- Page 19 ---

19脚注
参考来源
1. OpenClaw 官 方文 档  - 什 么 是  OpenClaw: https://docs.openclaw.ai
2. OpenClaw GitHub 仓 库 : https://github.com/openclaw/openclaw （ MIT 许 可 证 开 源 ）
3. ClawHub 技能市 场 : 通过  `openclaw skill install ` 命令访问社区技能
4. Agent 技 术 演 进 脉 络参考 ： Wooldridge, M., & Jennings, N. R. (1995). Intelligent agents: Theory and
practice. *Knowledge Engineering Review*, 10(2), 115-152.
5. Yao, S., et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR 2023*.
https://arxiv.org/abs/2210.03629
6. Wei, J., et al. (2022). Emergent Abilities of Large Language Models. *TMLR*.
https://arxiv.org/abs/2206.07682
7. Wei, J., et al. (2022). Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. *NeurIPS
2022*. https://arxiv.org/abs/2201.11903
8. Schick, T., et al. (2023). Toolformer: Language Models Can Teach Themselves to Use Tools. *NeurIPS
2023*. https://arxiv.org/abs/2302.04761

--- Page 20 ---

20第2章  核 心 架 构
OpenClaw 采用 创 新的网 关（ Gateway ） 架 构 设计 ， 将传统  AI 助 手 的 云 服务 模 式 转 变 为本地 优先
的分布式架 构 。本 章 深 入 解 析  OpenClaw 的 系 统 架 构 ， 从 宏 观 分 层 到微 观 实现 ， 揭 示 其技 术设计原 理与
核心机制 。
2.1 架构总 览
2.1.1 官方架 构模 型
OpenClaw 采用 简 洁 的 扁 平化 架 构 设计 ， 核 心 组 件清 晰 分 离 ， 通过 标 准 化 的  Gateway WebSocket
控制平面进行 协调 。 根 据 官 方文 档 ， 系 统 架 构 如下 ：
WhatsApp / Telegram / Slack / Discord / Google Chat / Signal / iMessage / 
BlueBubbles / Microsoft Teams / Matrix / Zalo / Zalo Personal / WebChat
               │
               ▼
┌───────────────────────────────┐
│            Gateway            │
│       (control plane)         │
│     ws://127.0.0.1:18789      │
└──────────────┬────────────────┘
               │
               ├─ Pi agent (RPC)
               ├─ CLI (openclaw …)
               ├─ WebChat UI
               ├─ macOS app
               └─ iOS / Android nodes
核心子系 统（根据官方  README ） ：
Gateway WebSocket network — 统一的控制平面 ， 连 接客户 端 、 工 具 和 事件
Channels — 多通道接入层 ， 支持 主 流 聊 天平 台
Pi Agent Runtime — Agent 执行 运 行时（ RPC 模 式）
Session Management — 会话管理（ 包 含  main、dmScope 等概念）
Control UI — 控制界面

--- Page 21 ---

21Cron + Webhooks — 定时任务和  webhook
2.1.2 组件架 构详 解
官方采用 功能 组 件 化 设计 ， 而 非强 制分 层 ：
┌─────────────────────────────────────────────────────────────────────────────┐
│                              Channels Layer                                 │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐   │
│  │WhatsApp │ │Telegram │ │  Slack  │ │Discord  │ │ Feishu  │ │iMessage │   │
│  │(Baileys)│ │(grammY) │ │ (Bolt)  │ │(discord)│ │(lark)   │ │(osa)    │   │
│  └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘   │
│       └─────────────┴─────────────┴─────────────┴─────────────┴─────────────┘
│                                    │
└────────────────────────────────────┼────────────────────────────────────────┘
                                     │ WebSocket / HTTP API
┌──────────────────────────────────── ▼ ────────────────────────────────────────┐
│                              Gateway Layer                                  │
│                    (ws://127.0.0.1:18789)                                   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                     Gateway WebSocket Control Plane                 │   │
│  │         消息路由  · 会话管理  · 协议处理  · 权限控制                    │   │
│  └──────────────────────────────────┬──────────────────────────────────┘   │
│                                     │
│  ┌──────────────────────────────────┴──────────────────────────────────┐   │
│  │                        Session Management                           │   │
│  │    会话创建  · dmScope 管理  · 上下⽂压缩  · 过期清理                   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────┬───────────────────────────────────────┘
                                      │ RPC / Internal API
┌───────────────────────────────────── ▼ ───────────────────────────────────────┐
│                            Pi Agent Runtime                                 │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────────────┐   │
│  │   Context   │ │    LLM      │ │    Tool     │ │   Streaming /       │   │
│  │  Assembler  │ │   Engine    │ │  Executor   │ │   Reasoning         │   │
│  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
2.1.2 各层职 责详 解
Channels Layer （通道 层 ）
通道层负 责与外部 聊 天平 台 的 集 成 ， 实现多通道 消 息 的 统 一 接入 。 该 层 通过  Provider 模 式 封 装 各
平台的  SDK ， 将不同平 台 的 消 息 格 式 转 换 为  OpenClaw 内部 标 准 格 式 。

--- Page 22 ---

22核心组件包括 ：
WhatsApp Provider: 基于  Baileys 库 实现  WhatsApp Web 协 议 连 接
Telegram Provider: 基于  grammY 框 架 实现  Bot API 集 成
Slack Provider: 基于  Bolt 框架实现  Slack Bot 功 能
Discord Provider: 基于  discord.js 实现  Discord Bot 功 能
Feishu Provider: 基于飞书开 放平 台 的  Lark SDK 实现 企 业 集 成
Google Chat Provider: 基于  Google Chat API 实现 企 业 聊 天 集 成
Signal Provider: 基于  signal-cli 实现  Sign al 协 议 连 接
BlueBubbles Provider: 推荐  iMessage 解 决 方 案 ， 基 于  BlueBubbles 服务
iMessage Provider: 基于  macOS OSA 脚 本实现本地 消 息收发（ legacy ）
Microsoft Teams Provider: 微软  Teams 集成（ extension ）
Matrix Provider: Matrix 去 中心化通信 协 议 （ extension ）
Zalo/Zalo Personal Provider: Zalo 越 南社 交应 用（ extension ）
WebChat Provider: 内置  Web 聊天 界 面
Gateway Layer（ 网 关 层 ）
网关层是  OpenClaw 架 构 的 核 心 创 新， 运 行在本地  127.0.0.1:18789 端口，作为系 统 的中 央 枢 纽
协调各组 件通信 。 根 据 官 方文 档 ， Gateway 包 含 ：
Gateway WebSocket Control Plane: WebSocket 控制平面 ， 统 一 管 理客户 端 、 工 具 和 事件
Session Management: 会话管理 ， 包含 会话 创建 、 dmScope 管 理 、 上下文 压 缩 和过 期清 理
Channels Integration: 通道集成 管理
Cron + Webhooks: 定时任务和  webhook 处 理
Pi Agent Runtime （ Agent 运 行时 层 ）
Agent 运行时层负 责  Agent 的 实 际 执 行 ， 使 用  Pi Agent Runtime（基于  pi-agent-core）作为
核心执行 引 擎 ，通过  RPC 模 式与  Gateway 交 互 。 该 层 实现了  Agent Loop 机制 、 LLM 接 口 封 装 、 工
具调用执行 、 流式 输 出（ streaming ）和推理 控 制（ reasoning ） 。
Infrastructure Services （ 基 础 设 施 服务）
基础设施层提 供底 层 存 储 和通用服务 ， 包 括 ：
Tailscale exposure: Serve/Funnel 用于  Gateway dashboard + WS
Browser control: OpenClaw 管理 的  Chrome/Chromium CDP 控 制

--- Page 23 ---

23Canvas + A2UI: Agent 驱动 的可视化工作 空 间
Voice Wake + Talk Mode: 常开语音和 连续 对话
Nodes: Canvas 、相机拍 照 / 录 像 、 屏 幕 录制 、 位 置 获 取 、 通知推 送
2.1.3 架构 设计原 则
OpenClaw 的架 构 设计 遵 循 以下 核 心 原 则 ：
本地优先（ Local First ）
所有核心 组 件默 认运 行在本地 环 境 ， 数 据 不经过 第 三方 云 服务 。 这 一 设计 确 保 了用户数 据 的 完 全主
权，符合隐私 保 护 和数 据 合 规 要 求 。
模块化（ Modularity ）
各层、各组 件之间通过明 确 定 义 的 接 口交 互 ， 低 耦 合高内 聚 。 这 种设计 允 许 用户 根 据需 求 替 换 或 扩
展特定组 件 ，例如更 换向 量 数 据库 实现 或 添 加 新的 聊 天平 台支持 。
可扩展性（ Extensibility ）
插件系统 允 许开发者通过  Skill 机制 扩 展 功 能 ， 无 需修改 核 心 代码 。 Skill 可以注 册 新 工 具 、 添 加 新
的消息处理 器 或自定 义 行为 逻 辑 。
事件驱动（ Event-Driven ）
系统采用 事件 驱动 架 构 ， 组 件 间通过 异 步 事件 进行通信 。 这 种设计支持 高 并 发 处 理 ， 允 许 同时 管 理
多个会话和  Agent 实 例 。
2.2 Gateway 详 解
Gateway 是  OpenClaw 架 构 的 核 心 枢 纽 ， 其 设计 借 鉴 了 网 络 路由 器 的 概 念 ， 但 路由 的 对 象 是  AI 消
息和命令 。本 节 深 入 解 析  Gateway 的 四 个 核 心子系 统 。
2.2.1 Gateway 总 体 架 构
Gateway 作为独 立 进 程运 行 ， 暴 露  WebSocket API 供 客户 端连 接 。 根 据 官 方文 档 ， 其 核 心 功 能是
作为  WebSocket Control Plane（控制平面） ， 协调  Channels 、 Pi Agent 、 CLI 、 WebChat UI 和 移
动设备节 点之间 的 通信 。

--- Page 24 ---

24┌─────────────────────────────────────────────────────────────────────────────┐
│                         Gateway Process                                     │
│                     (ws://127.0.0.1:18789)                                  │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                     Gateway WebSocket Control Plane                 │   │
│  │                                                                     │   │
│  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │   │
│  │  │   Client    │ │    CLI      │ │  WebChat    │ │   Node      │   │   │
│  │  │  (CLI)      │ │  ( 命令⾏ )   │ │    UI       │ │ (iOS/ 安卓 )  │   │   │
│  │  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘   │   │
│  │                              │                                      │   │
│  │                              ▼                                       │   │
│  │  ┌─────────────────────────────────────────────────────────────┐   │   │
│  │  │              Session Management + Channels Routing            │   │   │
│  │  └─────────────────────────────┬───────────────────────────────┘   │   │
│  └────────────────────────────────┼──────────────────────────────────┘   │
│                                   │                                         │
│                                   ▼                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        Pi Agent Runtime (RPC)                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
2.2.2 Gateway WebSocket Control Plane
Gateway 的核心是  WebSocket Control Plane，运行在  ws://127.0.0.1:18789，提供统 一的
控制平面 供客户 端 、 工 具 和 事件 通信 。
核心职责：
1. 消息路由（ Message Routing ）
接收来自 各  Provider 的 消 息
根据会话 标 识 路由 到对 应 的  Agent 实 例
支持多  Agent 并发 处 理
2. 会话管理（ Session Management ）
维护会话状 态（ sessionKey 、 dmScope 等）
处理会话激活 模式（ 群 聊 中的 触 发方式）
管理上下文压缩和会话 修 剪

--- Page 25 ---

253. 协议处理（ Protocol Handling ）
WebSocket 连接生 命 周 期管 理
心跳检测和 重 连机制
消息序列化和 事件 推 送
2.2.3 通道 集成（ Channels Integration ）
Channels 是  Gateway 的 接入 层 ， 负 责 与外部 聊 天平 台 的 集 成 。
支持的  Provider（根据官方  README ） ：
Provider 实现库 备注
WhatsApp Baileys 主要通道
Telegram grammY 主要通道
Slack Bolt 主要通道
Discord discord.js 主要通道
Google Chat Chat API 主要通道
Signal signal-cli 主要通道
BlueBubbles BlueBubbles iMessage 推 荐方 案
iMessage osa legacy
Microsoft Teams extension 扩展
Matrix extension 扩展
Zalo extension 扩展
Zalo Personal extension 扩展
WebChat built-in 内置
2.2.4 Session 管 理 详 解
Session Management 是  Gateway 的 核 心子系 统 ， 负 责维护 所 有 活 跃 会话 的 状 态 。

--- Page 26 ---

26会话数据模 型（官方  Session 模 型 ， 2026.2.23 版本） ：
interface Session {
  sessionId: string;           // 会话唯⼀标识（ UUID ）
  sessionKey: string;          // 会话键（如  "agent:<agentId>:<mainKey>" ）
  agentId: string;             // 所属  Agent
  channelId: string;           // 来源通道
  threadId?: string;           // 线程 / 话题  ID
  dmScope: DmScope;            // 私信范围配置
  messages: Message[];         // 消息历史
  context: Context;            // 会话上下⽂
  metadata: SessionMetadata;   // 元数据
  inputTokens: number;         // 输⼊  Token 计数
  outputTokens: number;        // 输出  Token 计数
  totalTokens: number;         // 总  Token 计数
  contextTokens: number;       // 上下⽂  Token 计数
  compactionCount?: number;    // 上下⽂压缩次数（新增字段）
  reasoningLevel?: string;     // 推理级别： off|minimal|low|medium|high|xhigh
  verboseLevel?: string;       // 详细程度
  model?: string;              // 当前使⽤的模型
  sendPolicy?: string;         // 发送策略
  groupActivation?: string;    // 群聊激活模式： mention/always
  createdAt: number;           // 创建时间
  updatedAt: number;           // 更新时间
  expiresAt: number;           // 过期时间
}
// dmScope 枚举：定义私信会话的隔离范围
enum DmScope {
  MAIN = 'main',                    // 主会话（所有私信共享）
  PER_PEER = 'per-peer',            // 每个对话对象独⽴会话
  PER_CHANNEL_PEER = 'per-channel-peer',        // 每个通道 + 对象独⽴
  PER_ACCOUNT_CHANNEL_PEER = 'per-account-channel-peer'  // 每个账户 + 通道 + 对象独⽴
}
// 注意：⾃  2026.2.23 版本起，默认  dmScope 已从  'main' 改为  'per-channel-peer'
// 如需共享  DM 会话连续性，需显式设置为  'main'
// 存储路径
// 会话索引 : ~/.openclaw/agents/<agentId>/sessions/sessions.json
// 会话转录 : ~/.openclaw/agents/<agentId>/sessions/<sessionId>.jsonl
会话生命 周 期：
创建 → 激活  → 处理中  → 等待响应  → 完成  → 挂起  → [ 恢复 / 过期清理 ]

--- Page 27 ---

27会话修剪（ Session Pruning ）：
为控制内 存 使用 ， Session Manager 实 施 智 能 修 剪 策 略 ：
1. 时间维度: 过期会话自动 清 理（ 默 认  24 小时无活动）
2. 容量维度: 单会话消息数 量限 制（ 默 认保 留 最 近  100 条 ）
3. 上下文压 缩（ Compaction ）: 当上下文 超过  Token 限 制时 触 发 压 缩 ， 记 录  compactionCount
4. 重要性维度: 重要消息 标记保 留 ， 普 通 消 息可 压 缩
dmScope 详 解：
dmScope（ Direct Message Scope ） 控 制 私 信会话 的 隔 离范围 ：
dmScope 隔离级别 适用场景
main 无隔离 所有私信 共享同 一 个会话上下文
per-peer 按用户隔离 与每个用户 的对话 有 独 立 上下文
per-channel-peer 按通道 +用户 隔离 （ 默 认 ）同一用户在不同平 台 有 不同 的 上下文
per-account-channel-peer完全隔离 最细粒度 的会话 隔 离
⚠ 重要变更: 自 2026.2.23 版本 起 ， CLI 本地  onboarding 默 认将  session.dmScope 设置
为 per-channel-peer。这是  breaking change ， 如 需 共享  DM 会话 连 续 性 ， 需显 式 设置 为
main。
WebSocket 连接 管 理：
Gateway 使用  WebSocket 协 议 进行实时 双向 通信 ， 支持 以下 功 能 ：
连接建立: 客户端发 起  WebSocket 握 手 ， Gateway 验 证身 份 后 建立 连 接
心跳检测: 定期发送  ping/pong 保持 连 接活 跃
重连机制: 支持断线 重 连和会话 恢 复
连接限流: 防止单个客户 端 占 用过多资 源
消息协议定义（官方协 议格式） ** ：

--- Page 28 ---

28// 请求消息格式
interface GatewayRequest {
  type: "req";          // 消息类型：请求
  id: string;           // 请求唯⼀标识
  method: string;       // 请求⽅法 / 类型
  params: unknown;      // 请求参数
}
// 响应消息格式
interface GatewayResponse {
  type: "res";          // 消息类型：响应
  id: string;           // 对应请求  ID
  ok: boolean;          // 是否成功
  payload?: unknown;    // 响应数据（成功时）
  error?: ErrorInfo;    // 错误信息（失败时）
}
// 事件消息格式
interface GatewayEvent {
  type: "event";        // 消息类型：事件
  event: string;        // 事件类型名称
  payload: unknown;     // 事件数据
  seq?: number;         // 序列号（可选）
  stateVersion?: number;// 状态版本（可选）
}
支持的消息类 型：
类型 说明 方向
health 健康检查 Request/Response
status 状态查询 Request/Response
send 发送消息 Request/Response
agent Agent 控制 Request/Response
presence 在线状态 Request/Response
tick 定时心跳 Event
message 新消息通知 Event
shutdown 关闭通知 Event

--- Page 29 ---

292.2.5 Skill 系 统
Skill 系统通过  Skill 机制实现 功 能 扩 展 ， 而 非 独 立 的  "Plugin Manager" 。
Skill 加载机制：
Skill Discovery → Manifest Parsing → Dependency Resolution → 
Module Loading → Hook Registration → Permission Setup
核心功能：
1. 技能发现（ Skill Discovery ）
扫描  ~/.openclaw/skills/ 目录
读取每个  Skill 的  SKILL.md 文件
解析技能 元数 据和 依 赖 关系
2. 钩子管理（ Hook Management ）
支持多种 钩子 点： 消 息接收前 、 消 息发 送 后 、 工 具 调 用前后等
允许  Skill 注 册自定 义 处 理 逻 辑
钩子执行顺序 管理
3. 权限控制（ Permission Control ）
基于角色 的权 限 模 型
工具级别 的  allow/deny 列 表
运行时权 限检 查
权限配置示例：

--- Page 30 ---

30{
  "permissions": {
    "tools": {
      "allow": ["web_search", "file_read", "code_exec"],
      "deny": ["shell_exec", "system_modify"]
    },
    "channels": {
      "allow": ["telegram", "discord"],
      "deny": ["whatsapp"]
    }
  }
}
2.3 Agent Runtime 工作机制
Agent Runtime 是  OpenClaw 的 核 心 执 行 引 擎 ， 负 责 将  LLM 的 能力 封 装 为可 运 行 的 服务 。 本 节
详细解析  Agent Runtime 的 工作机制 。
2.3.1 Agent Loop 流程 详 解
Agent Loop 是  Agent Runtime 的 核 心工作 循 环 ， 实现了 " 感 知 - 推理 - 行动 - 观 察 " 的 闭 环 。 根 据 官 方
文档，完 整 的  Agent Loop 包 含  streaming、reasoning、failover 等关键环 节 ：

--- Page 31 ---

31┌─────────────────────────────────────────────────────────────────────────────┐
│                    Agent Loop 完整流程（含  Streaming/Reasoning ）             │
│                                                                             │
│   ┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────┐  │
│   │   等待输⼊    │──── ► │  上下⽂组装   │──── ► │  LLM 推理    │──── ► │ 决策点   │  │
│   └─────────────┘     └─────────────┘     └─────────────┘     └────┬────┘  │
│                                                                     │       │
│        ┌────────────────────────────────────────────────────────────┘       │
│        │                                                                      │
│        ▼                                                                       │
│   ┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────┐  │
│   │  输出回复    │ ◄ ────│  结果反馈    │ ◄ ────│  ⼯具执⾏    │ ◄ ────│ 需⼯具 ? │  │
│   │  ( 流式 )     │     │             │     │             │     │  ( 是 )   │  │
│   └─────────────┘     └─────────────┘     └─────────────┘     └─────────┘  │
│        ▲                                                             │       │
│        │                                                     ( 否 ) ────┘       │
│   ┌────┴─────────────────────────────────────────────────────────────────┐  │
│   │                      Streaming + Reasoning                           │  │
│   │   • 流式输出  deltas → ⽬标通道                                        │  │
│   │   • 推理块（ reasoning blocks ）处理与显示控制                          │  │
│   │   • 上下⽂修剪决策（ pruning ）                                         │  │
│   │   • ⼯具调⽤前权限检查                                                │  │
│   └──────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
完整流程 步 骤：
1. 等待输入（ Wait for Input ）
监听来自  Gateway 的 消 息
识别会话上下文
触发  Loop 启动
2. 上下文组 装（ Context Assembly ）
加载系统提 示词（ System Prompt ）
加载会话 历史（ Conversation History ）
加载相关 记忆（ Relevant Memories ）
加载可用工 具说明（ Available Tools ）
组装当前用户输入
3. LLM 推理（ LLM Inference ）

--- Page 32 ---

32发送组装好 的上下文到  LLM API
启动流式响 应（ Streaming Response ）
根据  session.reasoningLevel 控 制推理 块 显 示
4. 流式处理与决策（ Streaming & Decision ）
流式输出（ Streaming ）: 实时接收 并转发  assistant deltas 到 目标 通道
推理控制（ Reasoning ）: 处理  reasoning blocks ， 根 据  reasoningLevel 决 定是 否 显 示
上下文检 查: 监控  token 使用 ， 触 发  compaction 决策
5. 决策点（ Decision Point ）
判断  LLM 输出类 型 ： 直 接回 复  / 工 具 调 用  / 需 要更多信息
如果是工 具 调用 ， 解 析 工 具 名 称 和 参 数
执行工具 调用前权 限 检 查
如果是直接回 复 ， 完 成 流 式 输 出
6. 工具执行（ Tool Execution ）
验证工具 调用权 限
执行工具 函数
捕获执行 结果 或错 误
7. 结果反馈（ Result Feedback ）
将工具执行 结果 反 馈 给  LLM
LLM 基于 结果进行下 一 步 推理
可能产生 新的工 具 调 用（多 轮 循 环 ）
8. 输出回复（ Output Response ）
生成最终回 复内 容
通过  Gateway 流 式发 送 到 目标 通道
更新会话状 态
模型故障 转移（ Model Failover ）：
根据官方  CHANGELOG ， Agent Runtime 支持 模 型 故 障 转 移 机制 ：

--- Page 33 ---

33// 配置示例（ openclaw.json ）
{
  "agents": {
    "defaults": {
      "model": "claude-sonnet-4-20250514",
      "failover": {
        "enabled": true,
        "fallbackModels": ["gpt-4o", "gemini-2.0-flash"]
      }
    }
  }
}
故障转移策略 ：
1. 主模型调用失败时自动 降 级 到备用 模 型
2. 支持配置多个备用 模 型 按 优先 级 尝 试
3. 记录  failover 事件 到会话 日 志
Agent Loop 实现 细 节 （ Pi Agent Runtime ）
OpenClaw 使用  Pi Agent Runtime（基于  pi-agent-core）作为核心  Agent 执 行 引 擎 ， 通过
RPC 模式与  Gateway 交 互 。 根 据 官 方  CHANGELOG 2026.2.23 ， 最 新 版本还 包 含  subagents 和
reasoning 控制 功能：
RPC 调用 流程：

--- Page 34 ---

341. Gateway 接收消息
        │
        ▼
2. agent RPC 验证参数
   • 解析 session ，获取  sessionKey
   • 返回 { runId, acceptedAt }
        │
        ▼
3. agentCommand 运⾏  Agent
   • 解析模型  + thinking/verbose/reasoningLevel 默认值
   • 加载 skills snapshot
   • 调⽤ runEmbeddedPiAgent
        │
        ▼
4. runEmbeddedPiAgent 执⾏
   • 通过 per-session + global queues 序列化运⾏
   • 解析模型  + auth profile
   • 订阅 pi 事件并流式传输  assistant/tool deltas
   • 强制执⾏  timeout
        │
        ▼
5. subscribeEmbeddedPiSession
   • 桥接 pi-agent-core 事件到  OpenClaw
   • 流式输出到⽬标通道
序列化执行 模 型：
Per-session Queue: 同一会话 的请 求 按 顺 序 处 理 ， 保证 对话 一 致 性
Global Queue: 所有  Agent 运行全 局 串 行化 ， 避 免 资 源 竞 争
Timeout 控制: 强制超时机制 ， 防止  Agent 无 限运 行
子代理（ Subagents ） 配 置（2026.2.23 新增 ） ：
// openclaw.json 配置
{
  "agents": {
    "defaults": {
      "subagents": {
        "runTimeoutSeconds": 300  // ⼦代理运⾏超时时间
      }
    }
  }
}

--- Page 35 ---

35Subagents 用于 ：
1. 将复杂任务分 解为 并 行子 任 务
2. 隔离不同子 任务 的 上下文
3. 独立控制子 任务 的 超 时和资 源
推理级别控制（ Reasoning Level ）：
级别 说明
off 关闭推理 ， 直接输 出
minimal 最小化推理
low 低级别推理
medium 中等级别推理（ 默 认 ）
high 高级别推理
xhigh 最高级别推理
用户可通过  /think 命令动态 调整当前会话 的  reasoningLevel 。
事件流类 型（Pi Runtime） ：
事件类型 说明
lifecycle Agent 生命 周 期事件 （ start/end/error ）
assistant 流式输出  deltas
tool 工具调用 事件
compaction 上下文压 缩 事件
reasoning 推理块事件（ 新增 ）
2.3.2 事件 驱动架 构
Agent Runtime 采 用 事件 驱 动 架 构 （ Event-Driven Architecture ） ， 通过 异 步 事件 机制实现高 并
发和松耦合 。

--- Page 36 ---

36事件总线 设计（Pi Agent Runtime 事件 类 型 ） ：
┌─────────────────────────────────────────────────────────────────────────────┐
│                            Event Bus                                        │
│                                                                             │
│  Publisher ─────── ►  Event Queue ─────── ►  Event Router ─────── ►  Subscriber  │
│                                                             (Event Handler) │
│                                                                             │
│  事件类型（ Pi Runtime ）：                                                     │
│  • lifecycle       - Agent ⽣命周期事件（ start/end/error ）                    │
│  • assistant       - 流式响应  deltas                                        │
│  • tool            - ⼯具调⽤事件                                            │
│  • compaction      - 上下⽂压缩事件                                          │
│                                                                             │
│  系统事件：                                                                   │
│  • USER_MESSAGE    - ⽤户消息                                                 │
│  • AGENT_RESPONSE  - Agent 响应                                               │
│  • SESSION_START   - 会话开始                                                 │
│  • SESSION_END     - 会话结束                                                 │
└─────────────────────────────────────────────────────────────────────────────┘
事件处理 流程：
1. 事件发布（ Publish ）: 组件产生 事件并 发 布 到 事件总 线
2. 事件排队（ Queue ）: 事件进入异 步队 列 ， 确 保 有 序 处 理
3. 事件路由（ Route ）: 根据事件类 型分发 给 对 应 的 处 理 器
4. 事件处理（ Handle ）: 处理器执行业务 逻 辑
5. 事件确认（ Ack）: 处理成功后 确 认 ， 失 败 可 重 试
并发控制：
单会话顺序: 同一会话 的 消息 按 顺 序 处 理 ， 保证 对话 一 致 性
多会话并发: 不同会话可 并行 处 理 ， 提高 吞 吐 量
资源隔离: 每个会话 有独 立 的 上下文和 状 态 ， 互 不 干 扰
2.3.3 上下文 管理 策 略
上下文管理是  Agent Runtime 的 关 键 挑 战 ， 需 要在 有 限 的  LLM 上下文 窗 口 内最大化信息 效 用 。
上下文优先 级 模 型：

--- Page 37 ---

37⾼优先级 ────────────────────────────────────────────── ►  低优先级
系统提示词  > 当前⽤户输⼊  > 近期对话  > 相关记忆  > 技能说明  > 早期对话
（固定保留）   （必须包含）   （动态调整）  （检索选择）  （按需加载）  （可压缩 / 丢弃）
上下文压 缩技 术：
1. 摘要生成: 对早期对话生成 摘 要 ， 替 代原 始 消 息
2. 记忆提取: 将重要信息提 取 到长 期记 忆
3. 信息去重: 移除冗余信息
4. 分段处理: 超长内容分段 处 理
Token 预算 管理：
interface TokenBudget {
  maxTokens: number;        // LLM 最⼤上下⽂限制
  reservedTokens: {         // 预留  Token 分配
    systemPrompt: number;   // 系统提示词
    currentInput: number;   // 当前输⼊
    responseBuffer: number; // 响应预留
  };
  dynamicTokens: number;    // 动态分配额度
}
2.3.4 错误 处理与 恢 复
Agent Runtime 实现了 完 善 的 错 误 处 理机制 ， 确 保 系 统 稳 定性 。
错误分类：
错误类型 说明 处理策略
网络错误 LLM API 连接失 败 指数退避 重 试
超时错误 请求响应超时 降级到备用 模 型
权限错误 工具调用 被拒绝 返回友好提 示
执行错误 工具执行异 常 捕获错误 并反馈  LLM
上下文错 误 Token 超限 压缩上下文 重 试

--- Page 38 ---

38恢复策略：
1. 重试机制: 临时错误自动 重 试 ， 最多  3 次
2. 降级处理: 主模型失败时切 换 到备用 模 型
3. 优雅降级: 复杂任务失败时提 供 简 化方 案
4. 人工介入: 关键错误通知用户 处 理
2.4 通信协 议
2.4.1 WebSocket 连 接 管 理
Gateway 与客户 端 之间通过  WebSocket 协 议 进行实时通信 ， 本 节 详 述 连 接 管 理 的 实现 细 节 。
连接建立流程：
┌─────────────┐                              ┌─────────────┐
│   Client    │                              │   Gateway   │
└──────┬──────┘                              └──────┬──────┘
       │                                            │
       │  1. HTTP Upgrade Request                   │
       │ ───────────────────────────────────────── ► │
       │                                            │
       │  2. 身份验证                                  │
       │    • 本地信任检查（同⼀机器）                   │
       │    • 配对令牌验证（远程连接）                   │
       │                                            │
       │  3. WebSocket Handshake Response           │
       │ ◄─────────────────────────────────────────│
       │                                            │
       │  4. 连接建⽴，开始双向通信                     │
       │◄══════════════════════════════════════════ ► │
身份验证机制：
1. 本地信任（ Local Trust ）
同一台机 器上 的客户 端 自动信 任
通过文件系 统权 限 控 制 访 问
适用于  CLI 、 macOS App 等本地客户 端

--- Page 39 ---

392. 配对令牌（ Pairing Token ）
远程设备首次 连接 需 要 管 理 员 批 准
使用短期 有 效 的 配 对令 牌 进行 认证
支持设备 白名 单管 理
心跳机制（官方配 置格式） ：
// ⼼跳配置（ openclaw.json 中的  agents.defaults.heartbeat ）
interface HeartbeatConfig {
  every: string;         // ⼼跳间隔（默认  "30m" ，即 30 分钟）
  target: string;        // ⽬标通道（ "last" | "whatsapp" | "telegram" | "discord" | 
"none"）
  directPolicy: string;  // 直连策略（ "allow" | "block" ）
}
// 示例配置
{
  "agents": {
    "defaults": {
      "heartbeat": {
        "every": "30m",
        "target": "last",
        "directPolicy": "allow"
      }
    }
  }
}
连接建立 协 议：
WebSocket 连接 建立 后 ， 客户 端必 须 发 送  connect 帧作为第 一 帧 ， 完 成 身 份 验 证 和会话 初 始 化 ：

--- Page 40 ---

40// connect 帧格式（必须是第⼀帧）
interface ConnectFrame {
  type: 'connect';
  token: string;           // 身份验证令牌
  minProtocol: number;     // 最低⽀持的协议版本
  maxProtocol: number;     // 最⾼⽀持的协议版本
  role: 'operator' | 'node';// 连接⻆⾊
  scopes: string[];        // 权限范围数组
  device: {
    id: string;            // 设备唯⼀标识
    publicKey: string;     // 设备公钥（⽤于签名验证）
    signature: string;     // 对  challenge nonce 的签名
    signedAt: number;      // 签名时间戳
    nonce: string;         // 服务端下发的  nonce
  };
  client: {
    name: string;          // 客户端名称
    version: string;       // 客户端版本
    platform: string;      // 平台标识（如  "macos", "ios", "android", "web" ）
    capabilities: string[];// ⽀持的能⼒列表
  };
  idempotencyKey?: string; // 幂等性键（⽤于重连场景）
}
// connect 响应
interface ConnectResponse {
  type: 'connect_response';
  status: 'success' | 'error';
  sessionId?: string;      // 分配的会话  ID
  deviceToken?: string;    // 设备令牌（⽤于后续连接）
  serverInfo: {
    version: string;
    supportedFeatures: string[];
  };
  error?: ErrorInfo;
}
Token 验 证机制：
Gateway 的 身份 验 证流程 基 于  challenge-response 机制 ：
1. 连接  Challenge 流程
Client          Gateway
  │                │

--- Page 41 ---

41│── connect ──── ▶ │ 1. 发送  connect 帧  │ │ │ ◄ ── challenge ──│ 2. Gateway 发送
connect.challenge 事件  │ (nonce, ts) │ 包含随机  nonce 和时间戳  │ │ │── connect ──── ▶ │ 3. 客
户端签名 nonce 后重新发送  connect │ ( 含  signature)│ │ │ │ ◄ ── success ────│ 4. 验证通过，返回
deviceToken
2. 签名  Payload 版本
v2（兼容版）: 简单  nonce 签名 ， 向 后 兼 容
v3（推荐版）: 绑定  platform + deviceFamily ， 更安全
// v3 签名  payload 示例
interface V3Payload {
  version: 'v3';
  platform: string;      // 如  "macos"
  deviceFamily: string;  // 如  "mac"
  nonce: string;         // 服务端下发的  nonce
  timestamp: number;     // 签名时间戳
}
3. Token 类 型
Gateway Token（OPENCLAW_GATEWAY_TOKEN）
从环境变 量或 配 置 文 件读取 的 静 态 令 牌
用于本地客户 端和 已 配 对 节 点的 认证
格式：oct_ 前缀的随机 字符 串
Device Token（通过配对 获 取）
连接成功后  Gateway 下发 的 长 期 令 牌
存储于客户 端 ，用于后 续 连 接 的 快 速 认证
可通过  connect 帧的  token 字段直接 使用
4. 本地连接自动批 准
loopback 地 址（ 127.0.0.1 ）
Tailnet 地 址（ 100.x.x.x ）
以上地址范围内 的 连 接可 跳 过 显 式 配 对 批 准

--- Page 42 ---

425. 远程连接 配对 流程
非本地连接 需要 管 理 员 显 式 批 准
通过  clawctl pair 或 Gateway UI 进行 配 对
批准后设备 获 得长 期 有 效 的  deviceToken
幂等性键（ Idempotency Keys ）：
对于可能产生副作用 的 操 作（如发 送 消 息 、 创建任 务） ， 客户 端 应 提 供 幂 等性 键 ：
interface IdempotentRequest {
  id: string;              // 请求唯⼀标识
  idempotencyKey: string;  // 幂等性键（客户端⽣成  UUID ）
  type: RequestType;
  payload: unknown;
}
// Gateway 保证：相同  idempotencyKey 的请求只执⾏⼀次
// 响应中包含相同的  idempotencyKey ⽤于确认
interface IdempotentResponse {
  id: string;
  idempotencyKey: string;
  status: 'success' | 'error' | 'duplicate';
  // 'duplicate' 表示该请求已处理过，返回缓存结果
}
2.4.2 消息 格式定 义
OpenClaw 定义了 标 准 化 的 消 息 格 式 ， 确 保 各组 件 间 的 互 操 作性 。
消息信封（ Message Envelope ）：
interface MessageEnvelope {
  version: string;        // 协议版本（如  "1.0" ）
  id: string;            // 消息唯⼀标识（ UUID ）
  type: MessageType;     // 消息类型
  timestamp: number;     // 发送时间戳（ Unix ms ）
  source: EndpointInfo;  // 发送⽅信息
  target?: EndpointInfo; // ⽬标⽅信息（可选）
  payload: unknown;      // 消息载荷
  signature?: string;    // 签名（可选）
}
消息类型定义：

--- Page 43 ---

43enum MessageType {
  // 请求类型
  REQUEST = 'request',
  
  // 响应类型
  RESPONSE = 'response',
  
  // 事件类型
  EVENT = 'event',
  
  // 错误类型
  ERROR = 'error'
}
// 请求类型枚举
enum RequestType {
  HEALTH_CHECK = 'health',
  GET_STATUS = 'status',
  SEND_MESSAGE = 'send',
  AGENT_CONTROL = 'agent',
  SYSTEM_PRESENCE = 'presence'
}
// 事件类型枚举
enum EventType {
  TICK = 'tick',
  AGENT_EVENT = 'agent',
  PRESENCE_UPDATE = 'presence',
  SHUTDOWN = 'shutdown',
  MESSAGE_RECEIVED = 'message'
}
标准消息 载 荷：

--- Page 44 ---

44// ⽤户消息载荷
interface UserMessagePayload {
  content: string;
  attachments?: Attachment[];
  metadata?: Record<string, unknown>;
}
// Agent 响应载荷
interface AgentResponsePayload {
  content: string;
  toolCalls?: ToolCall[];
  reasoning?: string;
}
// ⼯具调⽤载荷
interface ToolCallPayload {
  tool: string;
  parameters: Record<string, unknown>;
  callId: string;
}
// ⼯具结果载荷
interface ToolResultPayload {
  callId: string;
  status: 'success' | 'error';
  result?: unknown;
  error?: ErrorInfo;
}
2.4.3 节点通信 协 议
Nodes（ 设备 节 点 ）通过  Gateway WebSocket 与  Gateway 通信 ， 实现 跨 设 备 的 能力 调 用 。
说明: 以下描述 基于  OpenClaw 官 方文 档 公开 的 功 能说明 ， 部分内部实现 细 节 为 基 于 观 察 的
推测，可能随版本更 新 而 变 化 。
能力发现与 调用 流程（官方文档 确 认） ：
Nodes 通过  Gateway WebSocket 广告  capabilities + permission map ， Gateway 据 此 进行能
力路由。 标 准能力 包 括 ：

--- Page 45 ---

45能力类别（ caps）具体命令（ commands ） 说明
camera camera.snap, camera.clip 相机拍照 、录 像
canvascanvas.navigate, canvas.snapshot,
canvas.eval画布导航 、截图 、 JS 执
行
screen screen.record 屏幕录制
location location.get 位置获取
voice - 语音能力
能力调用 流程（官方流程） ：
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Agent     │──── ► │   Gateway   │──── ► │    Node     │──── ► │   Target    │
│  Runtime    │     │             │     │  Selector   │     │    Node     │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
                                                            │
                                                            ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Agent     │ ◄ ────│   Gateway   │ ◄ ────│    Node     │ ◄ ────│   Target    │
│  Runtime    │     │             │     │  Selector   │     │    Node     │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
1. Agent 请求调⽤节点能⼒
2. Gateway 查询可⽤节点列表（ node.list ）
3. 根据能⼒匹配选择⽬标节点
4. Gateway 转发请求到⽬标节点（ node.invoke ）
5. 节点执⾏命令并返回结果
6. Gateway 将结果返回给  Agent
节点管理命令（官方  CLI 命令） ：

--- Page 46 ---

46命令 说明
node.list 列出所有 已 连接 的 节 点
node.describe 获取节点详 细信息（能力 、 状 态 ）
node.invoke 调用节点上 的特定能力
node.approve 批准新节 点 配对
node.reject 拒绝节点 配对请 求
调用示例（基于实 际 使用 模 式） ：
// 获取节点列表
const nodes = await gateway.request('node.list', {});
// 调⽤特定节点的  camera.snap 能⼒
const result = await gateway.request('node.invoke', {
  nodeId: 'iphone-001',
  command: 'camera.snap',
  params: { facing: 'back' }
});
2.5 为什么  OpenClaw 会 火
📌 作者观 点 声明
本节内容 基于作者 的 个人 观 察 和市 场 分 析 ， 包 含 主 观 判 断 和 预测 。 以下 观 点 不 代 表
OpenClaw 官方 立场 ， 也 不 构 成 投 资 建议 。
OpenClaw 自开 源 以来 迅 速获 得 开发者社区 的 关注 。 本 节从 市 场 时机 、 产品定位 、 技 术 趋 势 和 网 络
效应四个 维度分析  OpenClaw 成 功 的 原 因 。
2.5.1 市场时机 ： AI 应 用 的 转 折 点
作者观点: 2024-2025 年是  AI 应 用 的 关 键 转 折 点， 以下分 析 基 于作者对行业 趋 势 的 观 察 。

--- Page 47 ---

47LLM 能力成 熟（ 2024-2025 ）
2024 年至  2025 年间 ， 大 语 言 模 型 能力实现了 质 的 飞 跃 ：
Claude 3.5 系 列: Anthropic 发 布 的  Claude 3.5 Sonnet 和  Opus 在推理能力上大 幅 提 升 ， 支持 更
复杂的逻辑分析和 代码 生成
GPT-4o: OpenAI 推出 的  GPT-4o 实现 原 生多 模 态支持 ， 文本 、 图 像 、 音 频 的 统 一 处 理能力为
Agent 应用开 辟 新 场 景
成本下降: LLM API 成本在 两 年内下 降  10-100 倍 ， 使得 高 频 调 用 的  Agent 应 用在经 济 上可行
本地模型: Llama 3 、 Qwen 等开 源 模 型 的 性能接 近 商 业 模 型 ， 为本地部 署 提 供 可能
用户需求觉 醒
ChatGPT 等产品 的 普 及完 成了市 场教 育 ：
用户不再满 足于 简单 的 问 答 对话 ， 期 待  AI 能 够 实 际 执 行 复 杂 任 务
企业用户关注数 据 隐私 和合 规 ， 寻 求 自 托 管解 决 方 案
开发者希望 构 建定制化 的  AI 应 用 ， 而 非 使 用 标 准 化 的  SaaS 产品
隐私法规 驱动
全球范围内数 据 保 护 法 规 日 趋 严 格 ：
GDPR（欧盟通用数 据 保 护 条 例 ）要 求 数 据 最小化和用户 控 制
中国企业面临数 据 本地化要 求
医疗、金融等敏 感 行业对数 据 主权 有 强 制要 求
2.5.2 产品定位 ： 填 补 市 场空 白
作者观点: OpenClaw 填补 了 云 服务与 完 全自 研 之间 的 市 场空 白 ， 以下 竞 品分 析 基 于作者 的
市场观察 。
竞品分析 矩 阵

--- Page 48 ---

48产品 部署模式数据控制定制化成本结构多平台
ChatGPT 云服务用户无控制 受限订阅费否
Claude 云服务用户无控制 受限订阅费否
Character.AI 云服务用户无控制 有限订阅费否
OpenClaw自托管 完全控制 完全开放 API 调用 费是
自研方案 自研 完全控制 完全开放开发成本 需开发
OpenClaw 的差异 化 优 势：
1. 比云服务更私 密: 数据完全本地 处 理 ， 不经过 第 三方服务 器
2. 比自研更经济: 基于成熟开 源 框 架 ， 省 去从头 开发 的 成本
3. 开箱即用 的多平 台: 内置支持主 流聊 天平 台 ， 无 需 额 外 集 成
4. 可扩展的 插 件系 统: Skill 机制 允 许无 代码 扩 展 功 能
目标用户画 像（作者分析） ：
技术型个人用户: 关注隐私 ， 具备技 术 能力 ， 希 望 定制个人  AI 助 手
中小企业: 需要  AI 自动化 但 不 愿 承 担  SaaS 订 阅 成本
开发者: 希望基于  OpenClaw 构 建 垂 直 领 域 应 用
数据敏感行业: 医疗、金融 、法 律 等行业用户
2.5.3 技术 趋势 ： 从 " 聊 天 " 到 " 行动 "
作者观点: AI 应用正经 历 从 聊 天机 器 人到自主 代 理 的 范 式 转 移 。
AI 应用演进三 阶段（作者归纳）

--- Page 49 ---

49阶段⼀：聊天机器⼈（ 2022-2023 ）
├─ 能⼒：⾃然语⾔理解与⽣成
├─ 局限：只能对话，⽆法执⾏实际任务
└─ 代表：早期  ChatGPT
阶段⼆：⼯具使⽤（ 2023-2024 ）
├─ 能⼒：调⽤预定义⼯具完成任务
├─ 局限：⼯具需要⼿动集成，灵活性受限
└─ 代表： ChatGPT Plugins 、 Copilot
阶段三：⾃主代理（ 2024-2025 ）
├─ 能⼒：⾃主规划、动态⼯具调⽤、任务执⾏
├─ 特征：具备记忆、可扩展、多平台
└─ 代表： OpenClaw 、 Claude Computer Use 、 AutoGPT
技术范式 转移（作者观察）
传统  AI 应用 采用 " 意图 识 别  →  预 定 义 流程  →  执 行 " 的 模 式 ， 而 现 代  Agent 采 用 " 自 然 语 言 理 解  →
自主推理  →  动 态 执 行 " 的 模 式 ：
维度 传统模式 Agent 模式
交互方式 点击 /命令 自然语言对话
流程定义 硬编码 动态生成
适应性 预定义场 景 开放式场 景
扩展方式 开发新功能 添加新工 具
OpenClaw 的技 术 前 瞻 性（作者评价） ：
率先实现本地 优先 的  Agent 架 构
支持多模 型切 换和 故 障 转 移
事件驱动架 构 支持 高 并 发
模块化设计适 应技 术 演 进
2.5.4 网络效 应 ： 飞 轮 加 速
作者观点: OpenClaw 的开 源 模 式可能 形 成自 增 强 的 社区生 态 。

--- Page 50 ---

50开源社区 驱动（作者推测 的飞轮 模 型 ）
        ┌─────────────┐
        │   开源代码    │
        └──────┬──────┘
               ▼
        ┌─────────────┐
        │  开发者参与   │
        └──────┬──────┘
               ▼
        ┌─────────────┐
        │  Skill ⽣态   │
        └──────┬──────┘
               ▼
        ┌─────────────┐
        │  功能增强    │
        └──────┬──────┘
               ▼
        ┌─────────────┐
        │  更多⽤户    │
        └──────┬──────┘
               │
               └────────── ►  回到起点，循环增强
飞轮效应分析（作者观 点） ：
1. 更多用户  →  更多 反 馈: 用户基数扩大 带 来 丰 富 的 使 用 场 景 和  bug 报告
2. 更多反馈  →  更好产品: 快速迭代 改进 ， 提 升 用户体 验
3. 更好产品  →  更多用户: 口碑传播 ，用户 增 长加 速
4. 更多开发者  →  更多  Skill: 社区贡献丰富 功 能生 态
5. 更多  Skill →  更 强功 能: 平台能力边 界 持 续 扩 展
2.5.5 技术同 源性 ： 与自动 驾 驶 的 共 鸣
📌 非技术性 概念类 比
本节内容纯属作者个人 的 跨 领 域 联 想 ， 旨 在 帮 助具 有 自动 驾 驶 背 景 的 读 者 建立直 观 理 解 。 这
些类比不构成技 术架 构 的 准确 描述，两种系 统 的技 术 实现 差异 巨 大 。
作为自动驾 驶 领域 的 从 业者 ， 能 够 从 专业视 角 理 解  OpenClaw 的 设计 哲 学 ：

--- Page 51 ---

51系统架构对 比（概念类 比 ， 非技 术 描述 ）
OpenClaw 组 件自动驾驶对 应 概念 类比说明（仅作理 解 参考 ）
Gateway 车载中央 计算平 台 统一处理多 源输入 ， 协调各 子系 统
Agent 自动驾驶算法 栈 感知  →  决策  →  规 划 的 完 整 闭 环
Channels 传感器接 口 CAN 总线 、以 太 网 等数 据 接入
Memory 高精地图  + 记忆系 统 存储环境信息和 历 史 轨 迹
Tools 执行器接 口 控制转向 、油门 、 刹 车 等
Skills 算法模块 车道保持 、自动 泊 车 等 功 能
设计原则 共通性（作者的主 观观察 ） ：
1. 实时性要 求: 两者都需要 低延 迟 的 响 应 能力
2. 可靠性要 求: 系统故障可能 导 致 严 重 后果 ， 需 要 完 善 的 错 误 处 理
3. 模块化设计: 支持功能独 立升 级 和 故 障 隔 离
4. 数据闭环: 运行数据 反馈 驱 动 持 续 优 化
创业机会 洞 察（作者观 点） ：
自动驾驶 领域 存在大 量 可用  OpenClaw 解 决 的 痛 点：
数据标注: 自动化数 据预 处 理和 标 注 任 务分发
仿真测试: 测试场景生成和 结 果分 析
模型监控: 模型性能追 踪和 异 常 检 测
文档管理: 技术文档 的智能 检 索 和问 答
本章小结
本章深入 剖析了  OpenClaw 的 核 心 架 构 ， 从官 方文 档 出发 呈 现系 统 的 技 术设计 ：
官方架构方面， OpenClaw 采 用 扁 平化 的 功 能 组 件设计 ， 核 心 包 括  Gateway WebSocket Control
Plane、 Channels 、 Pi Agent Runtime 、 Session Management 和  Cron/Webhooks 。 这 种设计 与 传
统的分层架 构不同 ， 更加 强调组 件 间 的 松 耦 合和 职 责 分 离 。

--- Page 52 ---

52Gateway 核心作为  WebSocket 控 制平面 运 行在本地  127.0.0.1:18789，协调  Channels 、 Pi
Agent、 CLI 、 WebChat UI 和 移 动 设 备 节 点 之间 的 通信 。 Session Management 维护 会话 状 态 ， 支持
dmScope 配 置和上下文 压 缩 。
Agent Runtime 使用  Pi Agent Runtime （ 基 于  pi-agent-core）作为核心执行 引 擎 ， 通过
RPC 模式与  Gateway 交 互 。 Agent Loop 包 含  streaming 、 reasoning 、 failover 等关 键环 节 ， 支持
模型故障 转移和子 代 理（ subagents ） 功 能 。
通信协议采用  WebSocket 实现实时 双向 通信 ， 定 义 了 标 准 化 的 消 息 格 式和 身 份 验 证 机制 。 节 点 通
信协议支持跨 设备能力 调 用（ camera 、 canvas 、 screen 、 location 、 voice ） 。
市场分析（作者观 点）表明 ， OpenClaw 的 成 功 源 于 准确 的 市 场 时机 把 握 、 差异 化 的 产品定位 、 顺
应技术趋势 的架 构 设计 以 及 开 源 社区 的 潜 在 网 络效 应 。 其本地 优先 的 架 构 设计 填 补 了 云 服务与 完 全自 研
之间的市 场空 白 。
参考资料
1. OpenClaw 官方文 档  - 架 构 概 览 : https://docs.openclaw.ai/concepts/architecture
2. OpenClaw 官方文 档  - Agent Loop: https://docs.openclaw.ai/concepts/agent-loop
3. OpenClaw 官方文 档  - Session: https://docs.openclaw.ai/concepts/session
4. OpenClaw 官方文 档  - Gateway Protocol: https://docs.openclaw.ai/gateway/protocol
5. OpenClaw 官 方文 档  - Gateway Configuration:
https://docs.openclaw.ai/gateway/configuration
6. OpenClaw GitHub 仓 库 : https://github.com/openclaw/openclaw
7. OpenClaw Gateway 源码 : https://github.com/openclaw/openclaw/tree/main/src/gateway
8. OpenClaw 入门 指 南 : https://docs.openclaw.ai/start/getting-started

--- Page 53 ---

53术语表
术语 英文 定义
网关 GatewayOpenClaw 的核心 守 护 进 程 （ daemon ） ， WebSocket 控 制
平面，负 责 消息 路由 和 组 件 协调
代理 Agent AI 智能体 ， 执行 具 体 任 务 的 实体
通道 Channel与外部聊天平 台 的 连 接
技能 Skill 可插拔的 功能扩 展 模 块
工具 Tool Agent 可 调用 的 具 体 功 能
会话 Session Agent 与用户 的对话上下文 ， 通过  sessionKey 唯 一 标 识
节点 Node连接到  Gateway 的 能力主机（ capability host ） ， 提 供
caps 和  comm ands
Provider Provider 聊天平台集成实现
sessionKey sessionKey会话键（如  agent:<agentId>:<mainKey>），用于 唯 一
标识和索 引会话
dmScope dmScope私信范围 配 置（ 默 认  per-channel-peer ， 支持  main/per-
peer/per-channel-peer/per-account-channel-peer ）
compactionCount compactionCount会话上下文压 缩次数 计 数 器
reasoningLevel reasoningLevel推理级别控制（ off/minimal/low/medium/high/xhigh ）
groupActivation groupActivation群聊激活 模式（ mention/always ）
subagents Subagents子代理机制 ，用于 并 行 任 务 执 行
failover Failover 模型故障 转移机制
streaming Streaming 流式输出 ，实时 转 发  LLM 响 应  deltas
caps Capabilities节点声明 的高阶能力类 别 （如  camera 、 canvas 、 screen 、
location 、 voice ）

--- Page 54 ---

54术语 英文 定义
comm ands Comm ands节点支持 的 具体可 执 行 命 令（如  camera.snap 、
screen.record）

--- Page 55 ---

55第3章  OpenClaw 工作 原 理
本章深入 剖析  OpenClaw 的 内部工作机制 ， 揭 示 其如 何 思 考 、 记 忆 、 行动 。 理 解 这 些 原 理对于 充 分
发挥  OpenClaw 的 潜 力 至 关 重 要 。
3.1 Agent Loop 详 解
Agent Loop 是  OpenClaw 的 核 心 执 行 引 擎 ， 它 定 义 了 从 接收用户 输 入到生成 响 应 的 完 整 流程 。 这
是一个持续 迭 代 的 循 环 ， 使  Agent 能 够 感 知 环 境 、 做 出 决策 、 执 行动作 并 观 察 结 果 。
3.1.1 Agent Loop 概 述
Agent Loop（智 能体 循 环 ）是  OpenClaw 的 " 心 跳 " ， 它 将消 息 转 化为行动和最 终响 应 ， 同时 保持
会话状态 的一 致性 。 每 一 次 循 环 运 行 称 为 一 个 " 回合 " （ turn ） ， 包 含 从 用户 输 入到系 统 响 应 的 完 整处 理
流程agent-loop。
┌─────────────────────────────────────────────────────────────────┐
│                     Agent Loop 概览                               │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐  │
│  │  输⼊     │───→│  上下⽂   │───→│  LLM 推理  │───→│  决策     │  │
│  │  接收     │    │  组装     │    │  ⽣成     │    │  执⾏     │  │
│  └──────────┘    └──────────┘    └──────────┘    └────┬─────┘  │
│       ↑                                                │        │
│       └───────────────────────────────────────────────┘        │
│                      观察结果反馈                                │
└─────────────────────────────────────────────────────────────────┘
Agent Loop 的核 心特 征 ：
序列化执行：每个会话（ session ） 的 循 环 是 序 列 化 的， 避 免 工 具 / 会话 竞 态 ， 保持 会话 历 史 一 致 性
agent-loop
事件驱动：通过生命 周 期事件 和 流事件 （ stream events ）与外部通信
状态持久化：会话状 态在 每次 循 环 后 被保 存 ， 支持 长对话 历 史
可中断性：支持通过  abort 信号 、 超 时 或 用户 指 令 中 断 当前 执 行

--- Page 56 ---

563.1.2 Agent Loop 8 步 骤 完 整 流程
根据  OpenClaw 官 方文 档 ， Agent Loop 可分为以下  8 个关 键步 骤agent-loop：
步骤  1： RPC 调用与 参 数 验 证
当用户通过 任何 渠 道（ WhatsApp 、 Telegram 、 CLI 等）发 送 消 息时 ， Gateway 接收请 求并 触 发
agent RPC。
// 概念示例： RPC ⼊⼝点
// 注意：此为示意代码，⾮  OpenClaw 实际源码
interface AgentRPCParams {
  message: string;           // ⽤户输⼊
  sessionKey?: string;       // 会话标识
  sessionId?: string;        // 可选：指定会话 ID
  model?: string;            // 可选：模型覆盖
  thinking?: string;         // 可选：思考级别
  timeoutMs?: number;        // 可选：超时时间
}
// RPC 返回⽴即响应，包含  runId 和  acceptedAt
interface AgentRPCResponse {
  runId: string;             // 本次运⾏的唯⼀标识
  acceptedAt: number;        // 接受时间戳
}
此阶段执行 的操作 ：
1. 验证传入 参数 的合法性
2. 解析会话 标 识（ sessionKey 或  sessionId ）
3. 持久化会话 元数 据
4. 立即返回  { runId, acceptedAt }，不等待实 际执行 完 成
步骤  2：会话与工作区 准 备
在 agentCommand 函数中， OpenClaw 准 备 执 行 环 境 ：

--- Page 57 ---

57// 概念示例：会话准备流程
// 注意：此为示意代码，⾮  OpenClaw 实际源码
async function agentCommand(params: AgentRPCParams) {
  // 1. 解析模型和默认配置
  const model = await resolveModel(params.model);
  const thinking = params.thinking ?? defaults.thinking;
  
  // 2. 加载技能快照
  const skillsSnapshot = await loadSkillsSnapshot();
  
  // 3. 解析⼯作区路径
  const workspace = resolveWorkspace(params.sessionKey);
  
  // 4. 获取会话写⼊锁
  const sessionLock = await acquireSessionLock(sessionKey);
  
  // 5. 准备  SessionManager
  const sessionManager = await openSession(sessionKey);
  
  // 6. 调⽤核⼼运⾏时
  return runEmbeddedPiAgent({
    model,
    thinking,
    skillsSnapshot,
    sessionManager,
    workspace,
    // ... 其他参数
  });
}
关键准备 任务 ：
模型解析：确定使用 的  LLM 模 型及 其 配 置
技能加载：加载当前可用 的 技能（ Skills ） 快 照
工作区解析：确定文 件操作 的 根 目 录
会话锁定：获取写入锁 ， 确 保 序 列 化 执 行
沙盒配置：如启用沙盒 ， 重 定 向 到 沙 盒 工作区
步骤  3：队 列与 并 发 控 制
OpenClaw 通过队 列 系 统管 理 并 发 执 行 ：

--- Page 58 ---

58// 概念示例：队列管理
// 注意：此为示意代码，⾮  OpenClaw 实际源码
async function runEmbeddedPiAgent(params: RunParams) {
  // 1. 通过  per-session 队列序列化
  const sessionLane = `session:${params.sessionKey}`;
  
  // 2. 通过  global 队列限制总体并发
  const globalLane = 'main'; // 或  'subagent' 对于⼦代理
  
  // 3. 排队等待执⾏
  return queue.enqueue({
    lanes: [sessionLane, globalLane],
    task: async () => {
      return executeAgentLoop(params);
    },
  });
}
队列特性 ：
Per-session 队 列：确保同 一会话 只 有一 个活 跃 运 行
Global 队 列：通过  agents.defaults.maxConcurrent 限制总体 并发数
Lane 系统：支持不同 优先 级 的 执 行通道（ main, cron, subagent ）queue
步骤  4： Prompt 组 装 与系 统 提 示 词 构 建
OpenClaw 为 每次 运 行 构 建 自定 义 系 统 提 示 词 （ System Prompt ） ， 该 提 示 词 包 含 ：

--- Page 59 ---

59┌────────────────────────────────────────────────────────────┐
│                  系统提示词结构                              │
├────────────────────────────────────────────────────────────┤
│ 1. Tooling （⼯具列表）                                       │
│    - 当前可⽤⼯具列表及简短描述                              │
│                                                            │
│ 2. Safety （安全提示）                                        │
│    - 避免权⼒寻求⾏为的简短提醒                              │
│                                                            │
│ 3. Skills （技能说明，如可⽤）                                │
│    - 技能名称、描述和位置                                    │
│                                                            │
│ 4. OpenClaw Self-Update                                     │
│    - 如何运⾏  config.apply 和  update.run                   │
│                                                            │
│ 5. Workspace （⼯作区）                                       │
│    - ⼯作⽬录路径                                            │
│                                                            │
│ 6. Documentation （⽂档位置）                                 │
│    - 本地  OpenClaw ⽂档路径                                  │
│                                                            │
│ 7. Workspace Files （注⼊的上下⽂⽂件）                       │
│    - AGENTS.md, SOUL.md, TOOLS.md, IDENTITY.md, USER.md    │
│                                                            │
│ 8. Sandbox （如启⽤）                                         │
│    - 沙盒路径和提升执⾏权限信息                              │
│                                                            │
│ 9. Current Date & Time                                      │
│    - ⽤户本地时间、时区                                      │
│                                                            │
│ 10. Reply Tags （可选）                                       │
│    - 回复标签语法说明                                        │
│                                                            │
│ 11. Heartbeats （⼼跳）                                       │
│    - ⼼跳提示和确认⾏为                                      │
│                                                            │
│ 12. Runtime （运⾏时信息）                                    │
│    - host, OS, node, model, repo, thinking level           │
│                                                            │
│ 13. Reasoning （推理）                                        │
│    - 推理可⻅性级别  + /reasoning 切换提示                   │
└────────────────────────────────────────────────────────────┘
系统提示词 构 建 的 关 键 代码 逻 辑 ：

--- Page 60 ---

60// 概念示例：系统提示词构建
// 注意：此为示意代码，⾮  OpenClaw 实际源码
function buildSystemPrompt(context: BuildContext): string {
  const sections: string[] = [];
  
  // 1. ⼯具列表
  sections.push(formatToolList(availableTools));
  
  // 2. 安全提示
  sections.push(SAFETY_GUARDrails);
  
  // 3. 技能列表（如可⽤）
  if (skills.length > 0) {
    sections.push(formatSkillsForPrompt(skills));
  }
  
  // 4. ⾃更新说明
  sections.push(SELF_UPDATE_INSTRUCTIONS);
  
  // 5. ⼯作区信息
  sections.push(`Workspace: ${workspacePath}`);
  
  // 6. ⽂档位置
  sections.push(`Docs: ${docsPath}`);
  
  // 7. 注⼊的引导⽂件
  sections.push('## Workspace Files (injected)');
  for (const file of bootstrapFiles) {
    sections.push(`### ${file.name}`);
    sections.push(file.content);
  }
  
  // 8. 沙盒信息
  if (sandbox.enabled) {
    sections.push(`Sandbox: ${sandbox.path}`);
  }
  
  // 9. 时间信息
  sections.push(`Current Date & Time: ${formatDateTime(timezone)}`);
  
  // 10. 回复标签（如启⽤）
  if (replyTags.enabled) {
    sections.push(formatReplyTagsHelp());
  }
  
  // 11. ⼼跳提示

--- Page 61 ---

61  sections.push(HEARTBEAT_INSTRUCTIONS);
  
  // 12. 运⾏时信息
  sections.push(formatRuntimeInfo(runtime));
  
  // 13. 推理说明
  sections.push(formatReasoningHelp(thinkingLevel));
  
  return sections.join('\n\n');
}
模型特定 的 限制和 压 缩 预 留  token 在 此 阶 段 被 强 制 执 行system-prompt。
Prompt Modes（提 示 词 模 式）
OpenClaw 支持三 种 系 统 提 示 词 模 式 ， 用于不同 场 景system-prompt：
模式 说明 使用场景
full（默认）包含所有部分 ：工 具 、 技能 、 内 存 召 回 、 自更 新 等 标准会话
minimal省略  Skills 、 Memory Recall 、 Self-Update 等部分子代理，减 少上下文开 销
none 仅返回基 础 身份行 特殊用途 ，最小化提 示 词
配置方式 ：
// 标准JSON 配置 : openclaw.json
{
  agents: {
    defaults: {
      systemPromptMode: 'full',  // full | minimal | none
    },
  },
}
子代理默 认使用  minimal 模式以减 少上下文 占 用 ， 主会话 默 认使 用  full 模式以获 得完 整功 能 。
步骤  5： LLM 推理与 流事件 处 理

--- Page 62 ---

62┌────────────────────────────────────────────────────────────┐
│                  LLM 推理流程                                │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  OpenClaw Gateway                                          │
│       │                                                    │
│       ▼                                                     │
│  ┌─────────────┐    WebSocket/SSE    ┌─────────────┐     │
│  │ pi-agent-   │ ◄ ───────────────── ►  │   LLM       │     │
│  │ core runtime│     流式事件          │   Provider  │     │
│  └──────┬──────┘                     └─────────────┘     │
│         │                                                  │
│         ▼                                                   │
│  ┌─────────────────────────────────────────────────────┐  │
│  │                  流式事件类型                          │  │
│  │  • assistant_delta  - 助⼿输出⽚段                    │  │
│  │  • tool_start       - ⼯具调⽤开始                    │  │
│  │  • tool_end         - ⼯具调⽤完成                    │  │
│  │  • lifecycle_start  - 运⾏⽣命周期开始                │  │
│  │  • lifecycle_end    - 运⾏⽣命周期结束                │  │
│  │  • lifecycle_error  - 运⾏错误                        │  │
│  │  • compaction       - 上下⽂压缩事件                  │  │
│  └─────────────────────────────────────────────────────┘  │
│                                                            │
└────────────────────────────────────────────────────────────┘
subscribeEmbeddedPiSession 函数将  pi-agent-core 事件 桥 接到  OpenClaw 的  agent 流 ：
Tool 事件 → stream: "tool"
Assistant deltas → stream: "assistant"
Lifecycle 事件 → stream: "lifecycle" (phase: "start" | "end" | "error")
步骤  6：工 具 调用 执 行
当 LLM 决定 调用工 具 时 ， 执 行 流程 如下 ：

--- Page 63 ---

63// 概念示例：⼯具调⽤处理
// 注意：此为示意代码，⾮  OpenClaw 实际源码
async function executeToolCall(
  toolCall: ToolCall,
  context: ExecutionContext
): Promise<ToolResult> {
  // 1. 查找⼯具处理器
  const handler = toolRegistry.get(toolCall.name);
  if (!handler) {
    throw new ToolNotFoundError(toolCall.name);
  }
  
  // 2. 权限检查
  await checkToolPolicy(toolCall, context);
  
  // 3. 执⾏前钩⼦
  await runHook('before_tool_call', { toolCall, context });
  
  // 4. 执⾏⼯具
  const result = await handler.execute(toolCall.params);
  
  // 5. 执⾏后钩⼦
  await runHook('after_tool_call', { toolCall, result, context });
  
  // 6. 结果处理（⼤⼩限制、图⽚负载清理）
  const sanitizedResult = sanitizeToolResult(result);
  
  // 7. 持久化⼯具结果
  await persistToolResult(toolCall, sanitizedResult, context);
  
  return sanitizedResult;
}
工具执行 的关 键特性 ：
权限控制：根据  tools.deny、tools.allow 和 tools.policy 进行访问控制
钩子系统：支持  before_tool_call 和 after_tool_call 钩子
结果清理：对大型输出和图片 负 载 进行大小 限 制
消息工具追 踪：追踪消息发 送工 具 以 避 免重复 确 认
步骤  7：上下文 管 理与 压 缩
当会话接 近 或超过 模 型 上下文 窗 口 时 ， OpenClaw 触 发自动 压 缩 。

--- Page 64 ---

64压缩策略说明 ：
OpenClaw 采用滑动窗口  + 摘要压 缩的混合策略 ：
1. 保留最近 消息：始终保 留最 近  N 条消 息（ 默 认 约  6-10 条 ）不 压 缩 ， 确 保 短 期 上下文 完 整
2. 摘要压缩：对较早 的 消息 历 史 生成文本 摘 要 ， 替 代原 始 消 息
3. 压缩率：通常将旧 消息压 缩 至 原  Token 数 量 的  10-30%
摘要策略详情 ：
策略类型描述 适用场景
完整摘要对整个历史生成 单 一 段落 摘 要 历史较短时
分段摘要 将历史分段 ， 每段 生成 独 立 摘 要 历史较长时
分层摘要 已有摘要 再次 被 摘 要 ， 形 成 层 级 极长会话
压缩触发 条件（ 精 确 描述 ） ：
OpenClaw 区分 两种 压 缩触 发机制 ：
1. 自动压缩触发：当会话  token 数接 近 或超 过 模 型 上下文 窗 口 时 触 发
触发条件 ：contextTokens > contextWindow - reserveTokensFloor
2. 预压缩内 存 刷 新 触 发：在自动压缩前触 发 记 忆 保 存
触发 条件 ：contextTokens > contextWindow - reserveTokensFloor -
softThresholdTokens
默认  softThresholdTokens 为 4000 tokens
这是软阈 值 ，用于提前 触 发 记 忆 刷 新
压缩率参考数 据 ：
原始历史长度 摘要后长度 压缩率
50 条消息  (~10K tokens) ~1K tokens 90%
100 条消息  (~25K tokens) ~2.5K tokens 90%
200 条消息  (~60K tokens) ~6K tokens 90%

--- Page 65 ---

65注：压缩率 受内 容复 杂 度 影 响 ， 实 际 范围 在  85-95% 之间 。
┌────────────────────────────────────────────────────────────┐
│                  上下⽂压缩流程                              │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  原始会话历史                                                │
│  ┌─────────────────────────────────────────────────────┐  │
│  │ Msg 1 │ Msg 2 │ Msg 3 │ ... │ Msg N-2 │ Msg N-1   │  │
│  │(最早 ) │       │       │     │         │ ( 最新 )    │  │
│  └─────────────────────────────────────────────────────┘  │
│                    │                                       │
│                    ▼                                        │
│  触发条件： contextTokens > contextWindow - reserveTokens   │
│                    │                                       │
│                    ▼                                        │
│  压缩后历史                                                  │
│  ┌─────────────────────────────────────────────────────┐  │
│  │ [压缩摘要 ] │ Msg N-2 │ Msg N-1                      │  │
│  │ (概括旧消息 )│ ( 保留最近消息 )                         │  │
│  └─────────────────────────────────────────────────────┘  │
│                                                            │
│  压缩摘要以  compaction 类型条⽬持久化到  JSONL              │
│                                                            │
└────────────────────────────────────────────────────────────┘
压缩配置 ：
// 标准JSON 配置 : openclaw.json
{
  agents: {
    defaults: {
      compaction: {
        reserveTokensFloor: 20000,  // 预留  token 下限
        memoryFlush: {
          enabled: true,
          softThresholdTokens: 4000,
          systemPrompt: "Session nearing compaction. Store durable memories now.",
          prompt: "Write any lasting notes to memory/YYYY-MM-DD.md; reply with 
NO_REPLY if nothing to store.",
        },
      },
    },
  },
}

--- Page 66 ---

66预压缩内 存刷 新（ memory flush ）是  OpenClaw 的 重 要特性 ： 在自动 压 缩 前 ， 系 统 会 触 发 一 个无
声的代理回合 ，提 醒 模 型将持 久 记 忆 写 入 磁 盘 ， 防止 关 键 上下文 被 压 缩 丢 失memorysession-management-
compaction。
步骤  8：响 应 组 装 与 输 出
最后阶段 将执行 结 果 组 装 为最 终响 应 ：

--- Page 67 ---

67// 概念示例：响应组装
// 注意：此为示意代码，⾮  OpenClaw 实际源码
function assembleReply(context: AssemblyContext): ReplyPayload[] {
  const payloads: ReplyPayload[] = [];
  
  // 1. 添加助⼿⽂本（和可选推理）
  if (assistantText) {
    payloads.push({
      type: 'text',
      content: assistantText,
    });
  }
  
  // 2. 添加内联⼯具摘要（ verbose 模式）
  if (verbose && toolSummaries.length > 0) {
    payloads.push(...formatToolSummaries(toolSummaries));
  }
  
  // 3. 添加助⼿错误⽂本（如发⽣错误）
  if (assistantError) {
    payloads.push({
      type: 'error',
      content: assistantError,
    });
  }
  
  // 4. 过滤  NO_REPLY
  const filtered = payloads.filter(p => !isNoReplyToken(p.content));
  
  // 5. 去重消息⼯具结果
  const deduplicated = deduplicateMessagingResults(filtered);
  
  // 6. 如⽆可渲染内容且⼯具出错，发送回退错误响应
  if (deduplicated.length === 0 && toolErrors.length > 0) {
    return [createFallbackErrorReply(toolErrors)];
  }
  
  return deduplicated;
}
响应组装 的关 键处 理 ：
NO_REPLY 过 滤：以  NO_REPLY 开头的响 应被静默 处 理
重复去除：消息工 具 的 重复结 果 从 最 终 负 载 中 移 除

--- Page 68 ---

68回退机制：当没有可 渲染内 容 且 工 具 出 错 时 ， 发 送 回 退 错 误 响 应
流式输出：支持块 流式（ block streaming ）和 预 览 流 式（ preview streaming ）streaming
3.1.3 Agent Loop 状 态转 换 图
┌─────────────────────────────────────────────────────────────────────┐
│                      Agent Loop 状态机                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────┐    RPC 调⽤       ┌─────────────┐                       │
│   │  IDLE   │ ──────────────→ │  ACCEPTED   │                       │
│   └─────────┘                 └──────┬──────┘                       │
│       ▲                               │                              │
│       │                              ▼                               │
│       │                        ┌─────────────┐    准备失败           │
│       │              准备完成   │ PREPARING   │ ─────────→  ERROR    │
│       │              ◄ ─────────┤  ( 准备阶段 )  │                       │
│       │                        └──────┬──────┘                       │
│       │                               │                             │
│       │                               ▼                              │
│       │                        ┌─────────────┐    推理错误           │
│       │              ⼯具调⽤   │  RUNNING    │ ─────────→  ERROR    │
│       │              ◄ ─────────┤  ( 推理阶段 )  │                      │
│       │              │         └──────┬──────┘                      │
│       │              │                │                             │
│       │              │                ▼                              │
│       │              │         ┌─────────────┐    执⾏错误           │
│       │              └────────→│ EXECUTING   │ ─────────→  ERROR    │
│       │                        │  ( ⼯具执⾏ )  │                      │
│       │                        └──────┬──────┘                      │
│       │                               │                             │
│       │                               ▼                              │
│       │                        ┌─────────────┐                      │
│       │              继续循环   │   WAITING   │                      │
│       │              ◄ ─────────┤  ( 等待⽤户 )  │                      │
│       │                        └──────┬──────┘                      │
│       │                               │                             │
│       │                        组装响应                              │
│       │                               ▼                              │
│       │                        ┌─────────────┐                      │
│       └───────────────────────│  COMPLETED  │                      │
│                                └─────────────┘                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

--- Page 69 ---

693.1.4 超时与终止 条件
Agent Loop 在以下情 况 下会提前 结 束agent-loop：
终止条件说明 配置项
Agent 超时 运行超过 指定时间 被 中 止 agents.defaults.timeoutSeconds (默认  600s)
AbortSignal用户取消或系 统信号 运行时自动 处理
Gateway 断开 RPC 超时 或 网关 连 接 丢 失自动处理
agent.wait 超时仅等待操作 超时 timeoutMs 参数  (默 认  30s)
上下文溢出 超出模型上下文 窗 口 触发压缩后 重 试
工具执行失 败关键工具 执行失 败根据策略 处理
超时配置示例 ：
// 标准JSON 配置 : openclaw.json
{
  agents: {
    defaults: {
      timeoutSeconds: 600,      // Agent 运⾏超时
      compaction: {
        reserveTokensFloor: 20000,  // 压缩预留  token
      },
    },
  },
}
3.1.5 Hook 系 统与 扩 展 点
OpenClaw 提 供 两 套 钩 子系 统 用于 拦 截 和 扩 展  Agent Loopagent-loop：
内部钩子（ Gateway hooks ）
事件驱动 的脚本 ， 用于 命 令和生 命 周 期事件 ：
agent:bootstrap：构建引 导文 件时 运 行 ， 可 添 加 / 移 除引 导 上下文文 件
Command hooks：/new、/reset、/stop 等命令事件
插件钩子（ Plugin hooks ）

--- Page 70 ---

70Agent/工 具生命 周 期 和 网 关 管 道 中的 扩 展 点：
钩子名称 触发时机用途
before_model_resolve会话前（无
messages）确定性覆 盖  provider/model
before_prompt_build 会话加载后注入
prependContext/systemPrompt
before_agent_start 兼容性钩子 向后兼容
agent_end 完成后 检查最终 消息 列表和 元 数 据
before_compaction /
after_compaction压缩前后 观察或注 解压 缩 周 期
before_tool_call /
after_tool_call工具调用前后 拦截工具 参数 / 结果
tool_result_persist 工具结果 持久化前转换工具结果
message_received /
message_sending / message_sent消息收发时 消息处理
session_start / session_end会话生命 周 期边 界会话管理
gateway_start / gateway_stop 网关生命 周 期 网关管理
3.2 工具系 统
OpenClaw 的工 具 系 统 是其与外部 世界 交 互 的 核 心机制 。 工 具使  Agent 能 够 读取 文 件 、 执 行 命 令 、
控制浏览器 、发 送 消 息等 。

--- Page 71 ---

713.2.1 工具系 统架 构
┌─────────────────────────────────────────────────────────────────────┐
│                      ⼯具系统架构                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                     ⼯具调⽤层                                │   │
│  │  • ⼯具解析     • 参数验证     • 权限检查     • 路由分发         │   │
│  └──────────────────────┬──────────────────────────────────────┘   │
│                         │                                          │
│  ┌────────────────────── ▼ ──────────────────────────────────────┐   │
│  │                     ⼯具注册表                                │   │
│  │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐            │   │
│  │  │  read   │ │  write  │ │  exec   │ │ browser │   ...      │   │
│  │  └─────────┘ └─────────┘ └─────────┘ └─────────┘            │   │
│  └──────────────────────┬──────────────────────────────────────┘   │
│                         │                                          │
│  ┌────────────────────── ▼ ──────────────────────────────────────┐   │
│  │                     执⾏适配层                                │   │
│  │  • Sandbox  • Gateway Host  • Node Host  • Remote CDP       │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
3.2.2 六大类工 具 详 解
注意：以下工 具分类为作者 根 据功 能进行 的 归 类 ，非 OpenClaw 官 方分类方式。官方文档按
实际功能 组织工 具 ， 没 有 明 确 分为 " 六 大类 " 。
OpenClaw 的工 具 可分为以下 六 大类 ：
1. 文件操作工 具
文件操作工 具 允 许  Agent 与工作区文 件交 互 。
read（读取文 件）

--- Page 72 ---

72interface ReadParams {
  file_path: string;      // ⽂件路径（相对或绝对）
  offset?: number;        // 起始⾏号（ 1-indexed ）
  limit?: number;         // 最⼤读取⾏数
}
// 功能：
// - ⽀持⽂本⽂件和图像（ jpg, png, gif, webp ）
// - 图像作为附件发送
// - ⽂本输出截断到  2000 ⾏或  50KB
// - 使⽤  offset/limit 处理⼤⽂件
write（写入文 件 ）
interface WriteParams {
  file_path: string;      // ⽂件路径
  content: string;        // ⽂件内容
}
// 功能：
// - 创建新⽂件或覆盖现有⽂件
// - ⾃动创建⽗⽬录
// - ⽀持绝对路径和相对路径
edit（编辑文 件）
interface EditParams {
  file_path: string;      // ⽂件路径
  oldText: string;        // 要替换的精确⽂本
  newText: string;        // 新⽂本
}
// 功能：
// - 精确⽂本替换（包括空⽩字符）
// - ⽤于精确、外科⼿术式编辑
// - oldText 必须完全匹配
2. 命令执行工 具
exec（执行命令）

--- Page 73 ---

73interface ExecParams {
  command: string;                    // 要执⾏的命令
  workdir?: string;                   // ⼯作⽬录
  env?: Record<string, string>;       // 环境变量覆盖
  yieldMs?: number;                   // ⾃动后台化延迟（默认  10000ms ）
  background?: boolean;               // ⽴即后台执⾏
  timeout?: number;                   // 超时秒数（默认  1800 ）
  pty?: boolean;                      // 在伪终端中运⾏
  host?: 'sandbox' | 'gateway' | 'node';  // 执⾏位置
  security?: 'deny' | 'allowlist' | 'full';  // 执⾏模式
  ask?: 'off' | 'on-miss' | 'always'; // 批准提示
  node?: string;                      // node id/name （ host=node 时）
  elevated?: boolean;                 // 请求提升模式
}
Exec 工具 的执行位 置选 项 ：
sandbox（ 默 认）：在隔离 的沙盒 环 境 中 执 行
gateway：在网关主机上执 行
node：在配对 的 节 点上 执 行
安全模式 ：
deny：拒绝执行（ 除非 在  allowlist 中 ）
allowlist：仅在显式 允 许 的 路 径 上 执 行
full：完全执行权 限（ 需 批 准 ）
process（进 程管 理）

--- Page 74 ---

74interface ProcessParams {
  action: 'list' | 'kill' | 'steer' | 'send-keys' | 'write' | 'submit' | 'paste';
  sessionId?: string;     // 会话  ID
  keys?: string[];        // 按键序列
  text?: string;          // ⽂本内容
  // ... 其他参数
}
// 功能：
// - list ：列出正在运⾏的  exec 会话
// - kill ：终⽌会话
// - steer ：向⼦代理发送消息
// - send-keys ：发送按键（⽀持  tmux ⻛格键名）
// - write ：写⼊数据
// - submit ：发送回⻋
// - paste ：粘贴⽂本
3. 浏览器控制工 具
browser（浏 览器 控 制）
interface BrowserParams {
  action: 'status' | 'start' | 'stop' | 'profiles' | 'tabs' | 'open' | 
          'focus' | 'close' | 'snapshot' | 'screenshot' | 'navigate' | 
          'console' | 'pdf' | 'upload' | 'dialog' | 'act';
  profile?: string;       // 浏览器配置⽂件
  target?: string;        // ⽬标位置
  // ... 其他参数
}
// ⽀持的  Action ：
// - status/start/stop ：状态检查和⽣命周期管理
// - profiles/tabs ：配置⽂件和标签⻚管理
// - open/focus/close ：标签⻚操作
// - snapshot ：捕获可交互  UI 的快照
// - screenshot/pdf ：捕获屏幕截图或  PDF
// - navigate ：导航到  URL
// - act ：执⾏  UI 动作（点击、输⼊、拖拽等）
浏览器配 置文 件browser：
chrome：使用  Chrome 扩 展 中 继 接 管 现 有  Chrome 标 签 页
openclaw：OpenClaw 管理 的 隔 离 浏 览器
4. 消息通信工 具

--- Page 75 ---

75message（ 消息发 送 ）
interface MessageParams {
  action: 'send';
  target?: string;        // ⽬标频道 / ⽤户  ID
  message?: string;       // 消息内容
  channel?: string;       // 频道类型
  // ... 其他参数
}
// ⽀持的通道：
// - Telegram 、 Discord 、 Slack
// - WhatsApp 、 Signal 、 iMessage
// - Google Chat 、 Teams
// - 以及其他⽀持的通道
消息工具 的关 键特性 ：
发送消息到 指定通道
支持附件（文 件 、 图片 、 音 频 ）
支持回复 、 引用 、 反应
支持创建投票 、线 程 等高 级 功 能
5. 会话与子 代理工 具
sessions_send（ 向 会话发 送 消 息）
interface SessionsSendParams {
  sessionId?: string;     // ⽬标会话  ID
  message: string;        // 消息内容
  // ... 其他参数
}
subagents（子 代 理 管 理）

--- Page 76 ---

76// ⼦代理管理：列出、终⽌或发送指令给⼦代理
interface SubagentsParams {
  action: 'list' | 'kill' | 'steer';
  target?: string;        // ⽬标⼦代理
  message?: string;       // 要发送的消息（ steer 时使⽤）
  // ... 其他参数
}
// 创建⼦代理（使⽤  sessions_spawn 或  subagents spawn ）
interface SpawnSubagentParams {
  task: string;           // 任务描述（必需）
  label?: string;         // ⽤于⽇志 /UI 的标签
  agentId?: string;       // 在另⼀个  agent id 下⽣成
  model?: string;         // 覆盖⼦代理模型
  thinking?: string;      // 覆盖思考级别
  runTimeoutSeconds?: number;  // 运⾏超时
  thread?: boolean;       // 是否请求线程绑定路由
  mode?: 'run' | 'session';    // thread=true 时默认为  session
  cleanup?: 'delete' | 'keep'; // 默认  keep
}
功能说明 ：
list：列出所 有活 跃子 代 理
kill：终止指定子 代理
steer：向子代理发 送指 令 / 消 息
spawn（通过  task 参数） ： 创建并 启 动子 代 理 执 行 指 定 任 务
子代理特性 ：
隔离性：每个子 代理 运行在自 己 的 会话 中
并行性：子代理可 并行执 行 ， 不 阻 塞 主 代 理
结果汇总：子代理 完成后自动 向 请 求 者 汇 报 结 果
成本控制：可为子 代理 配 置 更 便 宜 的 模 型
6. 其他专业工 具

--- Page 77 ---

77工具 用途 来源
canvas 控制节点画 布（ 展示 / 隐 藏 / 导 航 / 评 估 ） 内置
nodes 发现和控制 配对 节 点 内置
image 使用视觉 模 型分析 图 像 内置
tts 文本转语音 内置
web_search 网络搜索（ Brave API ） 内置
web_fetch 获取  URL 内 容 内置
memory_search 语义记忆 搜索 memory 插 件
memory_get 读取特定 记忆文 件 memory 插 件
feishu_doc 飞书文档操作 技能
feishu_bitable_*飞书多维表 格操作 技能
3.2.3 工具注 册与发现机制
工具注册 采用分层架 构 ：

--- Page 78 ---

78┌─────────────────────────────────────────────────────────────────────┐
│                      ⼯具发现层级                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Level 1: 内置核⼼⼯具                                                │
│  ├── read, write, edit                                               │
│  ├── exec, process                                                   │
│  ├── browser                                                         │
│  ├── message                                                         │
│  └── sessions_send, subagents                                        │
│                                                                     │
│  Level 2: 技能提供的⼯具                                              │
│  ├── ⻜书⼯具集  (feishu_doc, feishu_bitable_*)                       │
│  ├── GitHub ⼯具  (gh_issues)                                         │
│  └── 社区技能提供的⼯具                                               │
│                                                                     │
│  Level 3: 插件提供的⼯具                                              │
│  ├── memory_search, memory_get (memory-core 插件 )                    │
│  └── 其他插件⼯具                                                     │
│                                                                     │
│  Level 4: MCP 服务器⼯具  ( 通过  mcporter)                              │
│  └── 外部  MCP 服务器提供的⼯具                                        │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
工具注册代码示意 ：

--- Page 79 ---

79// 概念示例：⼯具注册机制
// 注意：此为示意代码，⾮  OpenClaw 实际源码
class ToolRegistry {
  private tools: Map<string, ToolHandler> = new Map();
  
  // 注册内置⼯具
  registerBuiltinTools() {
    this.register('read', new ReadTool());
    this.register('write', new WriteTool());
    this.register('edit', new EditTool());
    this.register('exec', new ExecTool());
    this.register('process', new ProcessTool());
    this.register('browser', new BrowserTool());
    this.register('message', new MessageTool());
    // ... 其他内置⼯具
  }
  
  // 从技能加载⼯具
  async loadSkillsTools(skills: Skill[]) {
    for (const skill of skills) {
      const skillTools = await loadSkillTools(skill);
      for (const tool of skillTools) {
        this.register(tool.name, tool.handler);
      }
    }
  }
  
  // 从插件加载⼯具
  async loadPluginTools(plugins: Plugin[]) {
    for (const plugin of plugins) {
      if (plugin.providesTools) {
        const pluginTools = await plugin.getTools();
        for (const [name, handler] of Object.entries(pluginTools)) {
          this.register(name, handler);
        }
      }
    }
  }
  
  // 获取⼯具处理器
  get(name: string): ToolHandler | undefined {
    return this.tools.get(name);
  }
  
  // 获取所有可⽤⼯具列表
  list(): ToolInfo[] {

--- Page 80 ---

80    return Array.from(this.tools.entries()).map(([name, handler]) => ({
      name,
      description: handler.description,
      parameters: handler.parameters,
    }));
  }
}
3.2.4 工具权 限控 制
OpenClaw 提 供多 层 次 的 工 具 权 限 控 制 ：
1. 工具策略（ Tool Policy ）
// 标准JSON 配置 : openclaw.json - ⼯具策略
{
  tools: {
    // 显式允许的⼯具（优先级最⾼）
    allow: ["read", "write", "edit", "exec"],
    
    // 显式拒绝的⼯具
    deny: ["browser", "message"],
    
    // 默认策略： allow | deny
    policy: "deny",
    
    // 按⼯具类型配置
    exec: {
      // Exec ⼯具特定配置
      host: "sandbox",
      security: "allowlist",
      ask: "on-miss",
    },
    
    browser: {
      enabled: true,
      defaultProfile: "chrome",
    },
  },
}
2. 权限检 查流程

--- Page 81 ---

81// 概念示例：⼯具权限检查
// 注意：此为示意代码，⾮  OpenClaw 实际源码
async function checkToolPolicy(
  toolCall: ToolCall,
  context: ExecutionContext
): Promise<void> {
  // 1. 检查是否在  deny 列表中
  if (isDenied(toolCall.name)) {
    throw new ToolDeniedError(`${toolCall.name} is in deny list`);
  }
  
  // 2. 检查是否在  allow 列表中（ policy=deny 时）
  if (context.policy === 'deny' && !isAllowed(toolCall.name)) {
    throw new ToolDeniedError(`${toolCall.name} is not in allow list`);
  }
  
  // 3. ⼯具特定权限检查
  switch (toolCall.name) {
    case 'exec':
      await checkExecPolicy(toolCall.params, context);
      break;
    case 'browser':
      await checkBrowserPolicy(toolCall.params, context);
      break;
    case 'message':
      await checkMessagePolicy(toolCall.params, context);
      break;
    // ... 其他⼯具
  }
}
// Exec ⼯具权限检查
async function checkExecPolicy(params: ExecParams, context: Context) {
  // 检查 host 设置
  if (params.host === 'gateway' || params.host === 'node') {
    // 检查批准
    if (params.ask !== 'off') {
      const approval = await requestApproval(params, context);
      if (!approval.granted) {
        throw new ApprovalDeniedError();
      }
    }
    
    // 检查 allowlist
    if (params.security === 'allowlist') {
      const resolvedPath = await resolveBinaryPath(params.command);

--- Page 82 ---

82      if (!isInAllowlist(resolvedPath)) {
        throw new NotInAllowlistError(resolvedPath);
      }
    }
  }
}
3. 沙盒执行
沙盒提供额外 的隔 离 层 ：
┌─────────────────────────────────────────────────────────────────────┐
│                      沙盒执⾏模型                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Gateway Host                                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                     Sandbox Container                        │   │
│  │  ┌───────────────────────────────────────────────────────┐  │   │
│  │  │               受限执⾏环境                              │  │   │
│  │  │  • ⽂件系统隔离（仅⼯作区可⻅）                         │  │   │
│  │  │  • ⽹络限制（可选）                                     │  │   │
│  │  │  • 资源限制（ CPU/ 内存）                                 │  │   │
│  │  │  • ⽆  root 权限                                         │  │   │
│  │  └───────────────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  配置： agents.defaults.sandbox.enabled = true                       │
│  ⼯作区： agents.defaults.sandbox.workspaceRoot                      │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
4. 批准系 统（ Approvals ）
对于敏感操作 ， OpenClaw 支持 批 准 系 统 ：

--- Page 83 ---

83// 批准请求流程
interface ApprovalRequest {
  id: string;
  tool: string;
  params: ToolParams;
  requester: SessionInfo;
  timestamp: number;
}
interface ApprovalResponse {
  granted: boolean;
  reason?: string;
  expiresAt?: number;
}
// 批准存储
// ~/.openclaw/exec-approvals.json
interface ApprovalStore {
  allowlist: string[];        // 已批准的⼆进制路径
  denials: string[];         // 明确拒绝的路径
  pending: ApprovalRequest[]; // 待批准请求
}
3.2.5 工具  Schema 与上下文成本
工具影响上下文 的 两种 方式context：
1. 工具列表文本：系统提 示词 中 显 示 的  "Tooling" 部分
2. 工具  Schema（ JSON ）：发送给 模 型以便 调 用工 具 ， 计 入上下文 但 不可 见
使用  /context detail 查看工具  Schema 大小 ：
🧠 Context breakdown (detailed)
...
Top tools (schema size):
- browser: 9,812 chars (~2,453 tok)
- exec: 6,240 chars (~1,560 tok)
... (+N more tools)
工具  Schema 格式（ TypeBox ） ：

--- Page 84 ---

84// 使⽤ TypeBox 定义⼯具参数  Schema
import { Type } from '@sinclair/typebox';
const ReadParamsSchema = Type.Object({
  file_path: Type.String({ description: 'Path to the file' }),
  offset: Type.Optional(Type.Number({ description: 'Line to start from' })),
  limit: Type.Optional(Type.Number({ description: 'Max lines to read' })),
});
const ReadToolDefinition = {
  name: 'read',
  description: 'Read file contents',
  parameters: ReadParamsSchema,
};
3.3 记忆系 统
OpenClaw 的 记忆 系 统 是其实现长 期 学 习 和上下文 保持 的 关 键 。 与上下文（ Context ）不同 ， 记 忆
是持久化 存储在 磁 盘 上 的 信息 ， 可在会话之间 共享 。

--- Page 85 ---

853.3.1 记忆系 统架 构
┌─────────────────────────────────────────────────────────────────────┐
│                      记忆系统架构                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    记忆访问层                                 │   │
│  │  ┌─────────────────┐    ┌─────────────────┐                 │   │
│  │  │ memory_search   │    │ memory_get      │                 │   │
│  │  │ ( 语义搜索 )       │    │ ( 精确读取 )       │                 │   │
│  │  └─────────────────┘    └─────────────────┘                 │   │
│  └───────────────────────┬─────────────────────────────────────┘   │
│                          │                                         │
│  ┌─────────────────────── ▼ ─────────────────────────────────────┐   │
│  │                    存储后端                                   │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │   │
│  │  │ Builtin     │  │ QMD         │  │ Vector Store│          │   │
│  │  │ (SQLite)    │  │ ( 实验性 )     │  │ ( 可选 )      │          │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘          │   │
│  └───────────────────────┬─────────────────────────────────────┘   │
│                          │                                         │
│  ┌─────────────────────── ▼ ─────────────────────────────────────┐   │
│  │                    存储格式                                   │   │
│  │  • memory/YYYY-MM-DD.md    ( 每⽇⽇志 )                       │   │
│  │  • MEMORY.md               ( ⻓期记忆 )                       │   │
│  │  • 纯  Markdown 格式                                         │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
3.3.2 短期记 忆与长 期记 忆
OpenClaw 使用 两 层 记 忆 模 型memory：
短期记忆（ Daily Logs ）

--- Page 86 ---

86⽂件：memory/YYYY-MM-DD.md
⽤途：
• 每⽇⽇志（ append-only ）
• ⽇常笔记和运⾏上下⽂
• 会话开始时读取（今天  + 昨天）
示例内容：
─────────────────────────────────────────
# 2026-02-27
## 上午
- 完成了第 3 章的初稿撰写
- 与星总讨论了技术细节
## 下午
- 审核了代码实现
- 更新了项⽬计划
─────────────────────────────────────────
长期记忆（ Curated Memory ）
⽂件：MEMORY.md
⽤途：
• 精选的⻓期记忆
• 决策、偏好、持久事实
• 仅在主私有会话中加载（不在群聊上下⽂中）
示例内容：
─────────────────────────────────────────
# ⻓期记忆
## 偏好
- 星总喜欢简洁的技术⽂档
- 使⽤专业术语，⽆需过度解释基础概念
## 重要决策
- 项⽬使⽤  Markdown 格式编写
- 所有代码必须经过测试验证
## 联系⽅式
- 邮箱: xingzong@example.com
─────────────────────────────────────────

--- Page 87 ---

87记忆写入 原则 ：
决策、偏好和 持久 事 实 → MEMORY.md
日常笔记和 运行上下文 → memory/YYYY-MM-DD.md
当有人说 " 记住这个 " 时 ， 将 其 写 入文 件 （不要 保 留 在  RAM 中 ）
如果需要某 事持久 化 ，要求  Agent 将其写 入 记 忆
3.3.3 向量 存 储与 语 义 搜索
OpenClaw 支持在 记 忆 文 件 上 构 建 向 量索 引 ， 实现 语 义 搜索 ：
┌─────────────────────────────────────────────────────────────────────┐
│                    向量搜索流程                                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. 索引构建                                                          │
│     ┌─────────────┐    ┌─────────────┐    ┌─────────────┐          │
│     │ Markdown    │───→│ ⽂本分割     │───→│ 向量嵌⼊     │          │
│     │ ⽂件         │    │ (chunks)    │    │ (Embeddings)│          │
│     └─────────────┘    └─────────────┘    └──────┬──────┘          │
│                                                   │                 │
│                                              ┌──── ▼ ────┐            │
│                                              │ 向量存储  │            │
│                                              │ (sqlite-│            │
│                                              │  vec)   │            │
│                                              └────┬────┘            │
│                                                   │                 │
│  2. 搜索查询                                        │                 │
│     ┌─────────────┐    ┌─────────────┐           │                 │
│     │ ⽤户查询     │───→│ 查询向量     │───────────┘                 │
│     │ " 数据库配    │    │ (Embedding) │                               │
│     │  置 "       │    │             │                               │
│     └─────────────┘    └─────────────┘                               │
│                              │                                      │
│                              ▼                                       │
│     ┌─────────────┐    ┌─────────────┐    ┌─────────────┐          │
│     │ 相似度计算   │ ◄ ───│ 向量检索     │───→│ 结果排序     │          │
│     │ (cosine)    │    │ (top-k)     │    │ 返回  top N  │          │
│     └─────────────┘    └─────────────┘    └─────────────┘          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
向量存储 配 置

--- Page 88 ---

88// 标准JSON 配置 : openclaw.json - 向量搜索
{
  agents: {
    defaults: {
      memorySearch: {
        // 嵌⼊提供商： local | openai | gemini | voyage | mistral
        provider: 'openai',
        
        // 本地模型配置（ provider=local ）
        local: {
          modelPath: '~/models/embedding.gguf',
        },
        
        // 远程 API 配置
        remote: {
          apiKey: '${EMBEDDING_API_KEY}',
          baseUrl: 'https://api.example.com/v1',
        },
        
        // 搜索限制
        maxResults: 10,
        maxSnippetChars: 2000,
        maxInjectedChars: 10000,
      },
    },
  },
}
自动提供 商选 择
如果  memorySearch.provider 未设置， OpenClaw 自动 选 择 ：
1. local - 如果配 置了  memorySearch.local.modelPath 且文件存在
2. openai - 如果能 解析到  OpenAI key
3. gemini - 如果能 解析到  Gemini key
4. voyage - 如果能 解析到  Voyage key
5. mistral - 如果能 解析到  Mistral key
6. 否则禁用 记忆 搜索直 到 配 置完 成
向量维度对 比
不同嵌入提 供 商 的 向 量 维 度 各 异 ：

--- Page 89 ---

89提供商 模型示例 维度特点
OpenAI text-embedding-3-small 1536性价比高 ，通用 场 景
OpenAI text-embedding-3-large 3072高精度， 复杂 语义
Gemini embedding-001 768多语言支持好
Voyage voyage-3 1024长文本优化
Mistral mistral-embed 1024欧洲隐私合 规
Local nomic-embed-text 768离线运行 ，隐私 优先
Local all-MiniLM-L6-v2 384轻量级，资 源 占用 低
维度选择 建议：
高维（ 1536+）：追求搜索精度 ， 内 存 充 足
中维（ 768-1024）：平衡精度和性能
低维（ 384-768）：边缘部 署 ，资 源 受 限
存储空间对 比（ 每 百万 向 量 ） ：
维度 原始大小 SQLite-vec 压 缩 后 说明
384 1.5 GB ~500 MB 适合移动 端 / 嵌入式
768 3.0 GB ~1.0 GB 平衡选择
1024 4.0 GB ~1.3 GB 主流选择
1536 6.0 GB ~2.0 GB OpenAI 默 认
3072 12.0 GB ~4.0 GB 高精度需 求
QMD 后 端（实 验 性）
QMD（ Query Markdown ）是 一 个本地 优先 的 搜索  sidecar ， 结 合  BM25 + 向 量  + 重 新 排 序
memory：

--- Page 90 ---

90// 标准JSON 配置 : openclaw.json - QMD
{
  agents: {
    defaults: {
      qmd: {
        command: 'qmd',                    // QMD 可执⾏⽂件路径
        searchMode: 'search',              // search | vsearch | query
        
        // 索引配置
        includeDefaultMemory: true,        // ⾃动索引  MEMORY.md + memory/**/*.md
        paths: [                           // 添加额外索引⽬录
          { path: '~/docs', pattern: '**/*.md', name: 'docs' },
          { path: '~/notes', pattern: '**/*.md', name: 'notes' },
        ],
        
        // 更新策略
        update: {
          interval: '5m',                  // 索引更新间隔（如  5m, 1h ）
          onBoot: true,                    // 启动时⽴即更新索引
        },
        
        // 搜索限制
        limits: {
          maxResults: 10,                  // 最⼤返回结果数
          maxSnippetChars: 2000,           // ⽚段最⼤字符数
        },
        
        // 搜索范围策略
        scope: 'workspace',                // workspace | global | session
        
        // 会话 JSONL 索引（实验性）
        sessions: {
          enabled: true,                   // 索引会话历史
          maxAge: '30d',                   // 最⼤会话年龄
        },
        
        // ⾃动回退机制
        fallback: {
          enabled: true,                   // QMD 失败时回退到  builtin
          onError: ['connection', 'timeout', 'crash'],
        },
      },
    },
  },
}

--- Page 91 ---

91QMD 后 端特性 ：
特性 说明
混合搜索 BM25 关 键词 匹 配  + 向 量 语 义 搜索
增量索引 支持定时更 新和启 动时更 新
多路径支持 可索引多个 目录 的  Markdown 文 件
会话索引 可选索引会话  JSONL 历 史
自动回退 QMD 不可用时自动回 退 到  builtin
混合搜索（ Hybrid Search ）
OpenClaw 的 记忆 搜索 采 用 混 合 搜索 策 略 ， 结 合多 种 算 法提高 召 回 质量memory：
混合搜索 组成 ：

--- Page 92 ---

92┌─────────────────────────────────────────────────────────────────────┐
│                      混合搜索架构                                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. 向量相似度（ Vector Similarity ）                                  │
│     • 语义匹配  - 理解查询意图                                        │
│     • 余弦相似度计算                                                 │
│     • 捕获概念相关性                                                 │
│                                                                     │
│  2. BM25 关键词相关性                                                │
│     • 传统关键词匹配                                                 │
│     • 词频 - 逆⽂档频率（ TF-IDF ）改进                                  │
│     • 精确术语匹配                                                   │
│                                                                     │
│  3. 加权合并                                                         │
│     finalScore = vectorWeight * vectorScore + textWeight * textScore│
│                                                                     │
│  4. MMR 重新排序（ Maximal Marginal Relevance ）                      │
│     • 平衡相关性与多样性                                             │
│     • 避免重复内容                                                   │
│     • λ  参数控制权衡（默认  0.5 ）                                     │
│                                                                     │
│  5. 时间衰减（ Temporal Decay ）                                       │
│     • 新内容获得更⾼权重                                             │
│     • 指数衰减函数                                                   │
│     • 可配置半衰期                                                   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
混合搜索 配 置 ：

--- Page 93 ---

93{
  agents: {
    defaults: {
      memorySearch: {
        // 混合搜索权重
        hybrid: {
          vectorWeight: 0.7,     // 向量搜索权重（ 0-1 ）
          textWeight: 0.3,       // BM25 ⽂本搜索权重（ 0-1 ）
        },
        
        // MMR 重新排序
        mmr: {
          enabled: true,
          lambda: 0.5,           // 相关性  vs 多样性权衡（ 0-1 ）
          diversity: 0.3,        // 多样性强度
        },
        
        // 时间衰减
        temporal: {
          enabled: true,
          halfLife: '7d',        // 半衰期（ 7 天内容权重减半）
          reference: 'now',      // 时间参考点
        },
        
        // 嵌⼊缓存（减少  API 调⽤）
        cache: {
          enabled: true,
          maxEntries: 50000,     // 最⼤缓存条⽬数
        },
        
        // 实验性：会话记忆搜索
        experimental: {
          sessionMemory: true,   // 启⽤会话历史搜索
        },
        sources: ['memory', 'sessions'],  // 搜索来源
      },
    },
  },
}
搜索流程示例 ：

--- Page 94 ---

94⽤户查询： " 数据库连接配置 "
Step 1: 查询处理
├─ ⽣成查询向量嵌⼊
├─ 提取关键词（数据库、连接、配置）
└─ 应⽤查询扩展
Step 2: 并⾏检索
├─ 向量搜索  → top-k 语义匹配结果
└─ BM25 搜索  → top-k 关键词匹配结果
Step 3: 加权合并
├─ 归⼀化分数
├─ 应⽤权重： finalScore = 0.7*vScore + 0.3*tScore
└─ 合并去重
Step 4: MMR 重新排序
├─ 选择最相关结果
├─ 迭代添加多样性⾼的结果
└─ 避免内容重复
Step 5: 时间衰减调整
├─ 应⽤时间权重
├─ 新内容获得提升
└─ 最终排序输出
3.3.4 记忆检 索算 法
文本检索（ memory_get ）
memory_get 工具提供对特定  Markdown 文 件 的 精 确 读取 ：
interface MemoryGetParams {
  path: string;           // ⽂件路径
  offset?: number;        // 起始⾏
  limit?: number;         // 最⼤⾏数
}
// 特性：
// - ⽂件不存在时优雅降级（返回空字符串）
// - ⽀持⾏范围读取
// - 适⽤于已知位置的信息检索
语义检索（ memory_search ）
memory_search 工具提供基于 语义 的 回 忆 ：

--- Page 95 ---

95interface MemorySearchParams {
  query: string;          // 搜索查询
  limit?: number;         // 返回结果数量
  // ... 其他参数
}
// 特性：
// - 使⽤向量相似度搜索
// - 即使措辞不同也能找到相关内容
// - 返回带相似度分数的⽚段
检索流程示例
⽤户查询： " 我上周讨论的数据库配置是什么？ "
┌─────────────────────────────────────────────────────────┐
│ Step 1: 确定搜索范围                                      │
│ • 默认搜索  MEMORY.md 和  memory/*.md                     │
│ • 检查 QMD 配置中的额外路径                              │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│ Step 2: 执⾏语义搜索                                      │
│ • 将查询转换为向量嵌⼊                                   │
│ • 在向量存储中检索  top-k 相似⽚段                         │
│ • 计算余弦相似度并排序                                   │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│ Step 3: 结果过滤与格式化                                  │
│ • 应⽤ maxResults 限制                                   │
│ • 截断到  maxSnippetChars                                │
│ • 格式化返回结果                                         │
└─────────────────────────────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────┐
│ Step 4: 结果注⼊上下⽂                                    │
│ • 结果注⼊到模型上下⽂（如果启⽤）                        │
│ • 受 maxInjectedChars 限制                               │
└─────────────────────────────────────────────────────────┘

--- Page 96 ---

963.3.5 自动 记 忆 刷 新
OpenClaw 在会话接 近 自动 压 缩 时 触 发无声的  Agentic 回合，提醒模 型在压缩 前 将持 久 记 忆 写 入 磁
盘memorysession-management-compaction：
┌─────────────────────────────────────────────────────────────────────┐
│                  预压缩记忆刷新流程                                    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  监控条件                                                            │
│  contextTokens > contextWindow - reserveTokensFloor - softThreshold │
│                              │                                      │
│                              ▼                                       │
│  触发⽆声刷新回合                                                    │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  systemPrompt: "Session nearing compaction..."              │   │
│  │  prompt: "Write any lasting notes to memory/YYYY-MM-DD.md"  │   │
│  │  expectedResponse: "NO_REPLY"                               │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                       │
│  模型执⾏记忆写⼊                                                    │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ • 评估哪些信息值得持久化                                     │   │
│  │ • 将重要决策写⼊  MEMORY.md                                  │   │
│  │ • 将⽇常笔记写⼊  memory/YYYY-MM-DD.md                       │   │
│  │ • 返回  NO_REPLY （⽤户不可⻅）                                │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                       │
│  继续正常压缩流程                                                    │
│  （确保重要记忆已保存到磁盘）                                         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
配置：

--- Page 97 ---

97{
  agents: {
    defaults: {
      compaction: {
        reserveTokensFloor: 20000,
        memoryFlush: {
          enabled: true,
          softThresholdTokens: 4000,
          systemPrompt: "Session nearing compaction. Store durable memories now.",
          prompt: "Write any lasting notes to memory/YYYY-MM-DD.md; reply with 
NO_REPLY if nothing to store.",
        },
      },
    },
  },
}
刷新特性 ：
软阈值：当会话  token 估 计超 过  contextWindow - reserveTokensFloor -
softThresholdTokens 时触发
默认静默：提示包含  NO_REPLY，用户不可 见
每压缩周 期 一次：在  sessions.json 中跟踪
只读工作区 跳过：如果会话工作区是 只 读 的， 跳 过 刷 新
3.4 规划与推理
OpenClaw 的 规划 与推理系 统建立 在  LLM 的 强 大能力之上 ， 通过特定 的 策 略 和机制实现 复 杂 任 务
的分解、执行和错 误 恢 复 。
3.4.1 LLM 推理机制
推理流程 概 览

--- Page 98 ---

98┌─────────────────────────────────────────────────────────────────────┐
│                    LLM 推理流程                                       │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐           │
│  │ 系统提示词   │     │  对话历史    │     │  当前输⼊    │           │
│  │             │     │             │     │             │           │
│  │ • ⼯具列表   │  +  │ • ⽤户消息   │  +  │ • ⽤户问题   │           │
│  │ • 安全提示   │     │ • 助⼿回复   │     │ • 附件       │           │
│  │ • 上下⽂     │     │ • ⼯具结果   │     │             │           │
│  └─────────────┘     └─────────────┘     └─────────────┘           │
│         │                   │                   │                   │
│         └───────────────────┴───────────────────┘                   │
│                             │                                       │
│                             ▼                                        │
│                    ┌─────────────────┐                              │
│                    │   LLM Provider  │                              │
│                    │                 │                              │
│                    │ • OpenAI        │                              │
│                    │ • Anthropic     │                              │
│                    │ • Google        │                              │
│                    │ • OpenCode      │                              │
│                    │ • ...           │                              │
│                    └────────┬────────┘                              │
│                             │                                       │
│                             ▼                                        │
│                    ┌─────────────────┐                              │
│                    │    推理输出      │                              │
│                    │                 │                              │
│                    │ • ⽂本回复       │                              │
│                    │ • ⼯具调⽤       │                              │
│                    │ • 推理过程       │                              │
│                    └─────────────────┘                              │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
思考级别（ Thinking Levels ）
OpenClaw 支持多 级别 的 思 考深 度 ：

--- Page 99 ---

99级别 说明 使用场景
off 无显式思 考 简单查询 、 快 速响 应
low 最小思考 标准对话
medium 中等思考 复杂问题
high 深度思考 分析、规划 、 代码 审 查
max 最大思考 复杂架构 设计 、故 障 排查
配置：
// openclaw.json
{
  agents: {
    defaults: {
      thinking: 'medium',  // 默认思考级别
    },
  },
}
// 运⾏时切换
// /thinking high
// /thinking low
推理可见性（ Reasoning Visibility ）

--- Page 100 ---

100┌─────────────────────────────────────────────────────────────────────┐
│                  推理过程控制                                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  /reasoning off                                                     │
│  • 推理过程完全隐藏                                                  │
│  • ⽤户只看到最终答案                                                │
│                                                                     │
│  /reasoning on                                                      │
│  • 推理过程可⻅                                                      │
│  • 作为单独块或内联显示                                              │
│                                                                     │
│  /reasoning stream                                                  │
│  • 推理过程流式传输                                                  │
│  • 实时显示思考过程                                                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
3.4.2 任务分 解策 略
自主任务分 解
OpenClaw Agent 能 够 自主 将复 杂 任 务分 解 为子 任 务 ：

--- Page 101 ---

101⽤户请求： " 帮我开发⼀个完整的⽤户认证系统 "
┌─────────────────────────────────────────────────────────────────────┐
│                  任务分解示例                                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  主任务：开发⽤户认证系统                                            │
│                                                                     │
│  ├─ ⼦任务  1 ：设计数据库模式                                         │
│  │   ├─ 创建⽤户表                                                   │
│  │   ├─ 创建会话表                                                   │
│  │   └─ 创建密码重置表                                               │
│  │                                                                   │
│  ├─ ⼦任务  2 ：实现注册功能                                           │
│  │   ├─ 验证输⼊数据                                                 │
│  │   ├─ 密码哈希处理                                                 │
│  │   └─ 创建⽤户记录                                                 │
│  │                                                                   │
│  ├─ ⼦任务  3 ：实现登录功能                                           │
│  │   ├─ 凭证验证                                                     │
│  │   ├─ 会话管理                                                     │
│  │   └─ JWT 令牌⽣成                                                 │
│  │                                                                   │
│  └─ ⼦任务  4 ：实现密码重置                                           │
│      ├─ 令牌⽣成                                                     │
│      ├─ 邮件发送                                                     │
│      └─ 密码更新                                                     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
使用子代理 并行 执 行
对于可并行 的子 任 务 ， OpenClaw 支持使 用子 代 理（ Sub-agents ） 并 行 处 理subagents：

--- Page 102 ---

102// 概念示例：使⽤⼦代理并⾏执⾏任务
const tasks = [
  { name: 'database-design', task: ' 设计数据库模式 ...' },
  { name: 'register-module', task: ' 实现注册功能 ...' },
  { name: 'login-module', task: ' 实现登录功能 ...' },
  { name: 'reset-module', task: ' 实现密码重置 ...' },
];
// 并⾏启动⼦代理
const subagentPromises = tasks.map(t => 
  subagents({
    action: 'steer',      // 或  'spawn' 根据实现
    target: t.name,
    message: t.task,
  })
);
// 或使⽤  sessions_spawn 创建⼦代理
const spawnPromises = tasks.map(t =>
  sessions_spawn({
    task: t.task,
    label: t.name,
    model: 'openai/gpt-4.1-mini',
    thinking: 'medium',
  })
);
// 等待所有⼦代理完成
const results = await Promise.all(
  subagents.map(s => waitForCompletion(s.runId))
);
// 整合结果
const integratedSolution = await integrateResults(results);
子代理特性 ：
隔离性：每个子 代理 运行在自 己 的 会话 中
并行性：子代理可 并行执 行 ， 不 阻 塞 主 代 理
结果汇总：子代理 完成后自动 向 请 求 者 汇 报 结 果
成本控制：可为子 代理 配 置 更 便 宜 的 模 型
队列模式与 任务 调 度

--- Page 103 ---

103OpenClaw 提 供多 种 队 列模 式 控 制 任 务 处 理queue：
模式 说明 使用场景
collect（默认）合并所有 排队 消息为 单 个后 续 回合 避免重复响 应
steer 立即注入当前 运行 需要立即干预
followup 排队等待下 一个 代 理回合 标准消息 处理
steer-backlog 立即转向 并保 留 消 息用于后 续 复杂交互
interrupt 中止当前 运行 ， 执 行最 新 消 息 紧急操作
队列配置 ：
{
  messages: {
    queue: {
      mode: 'collect',
      debounceMs: 1000,    // 防抖延迟
      cap: 20,             // 最⼤排队数
      drop: 'summarize',   // 溢出策略： old | new | summarize
      byChannel: {
        discord: 'collect',
        telegram: 'steer',
      },
    },
  },
}
3.4.3 错误 恢 复机制
错误类型与 处理策 略

--- Page 104 ---

104┌─────────────────────────────────────────────────────────────────────┐
│                  错误分类与处理                                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  1. ⼯具执⾏错误                                                     │
│     • 命令返回⾮零退出码                                             │
│     • ⽂件不存在                                                     │
│     • ⽹络请求失败                                                   │
│     处理：将错误信息返回给  LLM ，让  Agent 决定下⼀步                  │
│                                                                     │
│  2. LLM 推理错误                                                     │
│     • API 错误（ rate limit, quota exceeded ）                         │
│     • 上下⽂溢出                                                     │
│     • ⽆效响应格式                                                   │
│     处理：模型故障转移、压缩重试、回退响应                           │
│                                                                     │
│  3. 系统级错误                                                       │
│     • Gateway 连接丢失                                               │
│     • 会话损坏                                                       │
│     • 配置错误                                                       │
│     处理：优雅降级、错误报告、⾃动恢复                               │
│                                                                     │
│  4. 超时错误                                                         │
│     • Agent 运⾏超时                                                 │
│     • ⼯具执⾏超时                                                   │
│     • API 调⽤超时                                                   │
│     处理：中⽌运⾏、返回部分结果、通知⽤户                           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
上下文溢出 恢 复
当会话超出 模 型上下文 窗 口 时 ， OpenClaw 的 恢 复流程 ：

--- Page 105 ---

105┌─────────────────────────────────────────────────────────────────────┐
│                上下⽂溢出恢复流程                                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  触发条件                                                            │
│  contextTokens > contextWindow - reserveTokens                      │
│                              │                                      │
│                              ▼                                       │
│  ⾃动压缩流程                                                        │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ 1. 触发  memoryFlush （如启⽤）                                │   │
│  │    - ⽆声回合写⼊持久记忆                                    │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                       │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ 2. 执⾏压缩                                                  │   │
│  │    - 摘要旧对话                                              │   │
│  │    - 保留最近消息                                            │   │
│  │    - 持久化到  JSONL                                         │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                       │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ 3. 重试原始请求                                              │   │
│  │    - 使⽤压缩后的上下⽂                                      │   │
│  │    - 重置内存缓冲区                                          │   │
│  │    - 避免重复输出                                            │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│                              ▼                                       │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ 4. 如仍失败                                                  │   │
│  │    - 返回错误信息                                            │   │
│  │    - 建议⽤户⼿动压缩  (/compact)                            │   │
│  │    - 或创建新会话  (/new)                                    │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
模型故障 转移
当主模型失败时 ， OpenClaw 支持 自动 故 障 转 移 ：

--- Page 106 ---

106// 标准JSON 配置 : openclaw.json - 故障转移
{
  agents: {
    defaults: {
      models: {
        primary: 'anthropic/claude-opus-4-6',
        fallbacks: [
          'openai/gpt-4.1',
          'google/gemini-3-pro-preview',
        ],
      },
      // 触发故障转移的条件
      failover: {
        onRateLimit: true,      // 429 错误
        onTimeout: true,        // 超时
        onError: ['context_length_exceeded', 'server_error'],
        maxRetries: 2,          // 每模型最⼤重试
      },
    },
  },
}
故障转移 逻辑 ：
1. 主模型失 败 → 重试（最多  maxRetries 次）
2. 重试耗尽 → 切换到  fallback[0]
3. fallback 失 败 → 继续下 一个  fallback
4. 全部失败 → 返回最后错误
工具执行错 误 恢 复
工具执行错误 的恢 复 策 略 ：

--- Page 107 ---

107// 概念示例：⼯具错误恢复
// 注意：此为示意代码，⾮  OpenClaw 实际源码
async function executeWithRecovery(toolCall: ToolCall): Promise<Result> {
  try {
    return await executeTool(toolCall);
  } catch (error) {
    // 1. 记录错误
    logToolError(toolCall, error);
    
    // 2. 根据错误类型决定策略
    switch (error.type) {
      case 'ToolNotFound':
        // 告知 Agent ⼯具不可⽤
        return { error: `Tool ${toolCall.name} not found` };
        
      case 'ToolDenied':
        // 权限错误， Agent 需要调整策略
        return { error: `Permission denied for ${toolCall.name}` };
        
      case 'ExecTimeout':
        // 执⾏超时，可建议后台执⾏
        return { 
          error: 'Command timed out',
          suggestion: 'Try running with background: true',
        };
        
      case 'FileNotFound':
        // ⽂件不存在，返回明确错误
        return { error: `File not found: ${error.path}` };
        
      default:
        // 未知错误，返回详细信息
        return { error: error.message };
    }
  }
}
3.4.4 规划 模式与最 佳 实 践
ReAct 模式（ Reasoning + Acting ）
OpenClaw 隐式 支持  ReAct 模 式 ， Agent 能 够 在推理和行动之间 交 替 循 环 ， 直 到 任 务 完 成 。
ReAct 实现机制 ：
1. 循环结构：每个  Agent Loop 回合 包 含  [ 思 考  →  行动  →  观 察 ] 的 循 环

--- Page 108 ---

1082. 隐式规划：LLM 在系 统提 示 词 引 导 下自主 决 定是 否 需 要进 一 步 工 具 调 用
3. 最大回合 限制：默认限制 连续工 具 调 用回合数（通 常  25-50 回合） ， 防止 无 限 循 环
4. 终止条件：当  LLM 返回最 终答 案 （不 含 工 具 调 用）时 循 环 终止
具体实现 细 节补充 ：
实现要素详细说明
最大回合数 默认  50 回合 ，可通过 配 置 调整 ； 超 过 限 制会 触 发  max_turns_exceeded 错误
隐式  ReAct不需要显式 标记思 考 / 行动 ， LLM 自主 决 定 调 用工 具 还是 返 回 结 果
工具调用 格式 使用标准 函数 调用 格 式 ：{"name": "tool_name", "arguments": {...}}
观察结果 处理工具结果自动 添加到上下文 ， 作为下 一 轮 推理 的 输 入
中间状态保 存 每回合的 完 整状 态 （ 思 考 + 行动 + 观 察 ） 持 久 化到  sessions.jsonl
循环中断 支持  /stop 命令中断当前  ReAct 循 环
ReAct 执行 流程 伪 代码 （ 概 念 示 例 ） ：

--- Page 109 ---

109// 概念示例： ReAct 循环实现示意
// 注意：此为基于  ReAct 模式的简化示例，⾮  OpenClaw 官⽅实现细节
async function reactLoop(session, userInput, maxTurns = 50) {
  const context = buildContext(session, userInput);
  
  for (let turn = 0; turn < maxTurns; turn++) {
    // 1. LLM 推理
    const response = await llm.generate(context);
    
    // 2. 检查是否包含⼯具调⽤
    if (!response.hasToolCalls()) {
      // ⽆⼯具调⽤，返回最终答案
      return { answer: response.text, turns: turn + 1 };
    }
    
    // 3. 执⾏⼯具调⽤
    const results = await executeTools(response.toolCalls);
    
    // 4. 观察结果加⼊上下⽂
    context.addObservation(results);
    
    // 5. 持久化回合状态
    await persistTurn(session, response, results);
  }
  
  throw new Error('max_turns_exceeded');
}

--- Page 110 ---

110⽤户："找出我的  GitHub 仓库中最近更新的前  5 个项⽬ "
Agent 思考过程：
─────────────────────────────────────────
回合 1 - 思考：⽤户想了解  GitHub 仓库信息。
         我需要：
         1. 调⽤ GitHub API 获取仓库列表
         2. 按更新时间排序
         3. 提取前  5 个
回合 1 - ⾏动：调⽤  github ⼯具获取仓库
回合 1 - 观察：获取到  20 个仓库，包含名称、更新时间等信息
─────────────────────────────────────────
[循环继续 ...]
─────────────────────────────────────────
回合 2 - 思考：我已获取仓库列表，现在需要排序并提取前  5 个
回合 2 - ⾏动：⽆需额外⼯具，直接从结果中提取
回合 2 - 最终回答：这⾥是您最近更新的前  5 个仓库 ...
─────────────────────────────────────────
关键实现 细 节 ：
组件 说明
推理触发 LLM 根据 任务 复杂 度自主 决 定是 否 需 要多 步 推理
工具选择 基于描述 匹 配 选 择 最合 适 的 工 具
错误恢复工具调用失 败时自动 重 试 或 调整 策 略
会话状态 每回合的思 考和 观 察 结 果 都持 久 化到会话 历 史
自我修正（ Self-Correction ）
Agent 能够检测 并 修 正自 己 的 错 误 ：

--- Page 111 ---

111场景：Agent 尝试编辑⽂件但提供了错误的  oldText
尝试 1：
  edit({ file_path: 'config.js', oldText: 'port: 3000', newText: 'port: 8080' })
  → 失败：oldText 不匹配
Agent 反思：
  错误信息显示  oldText 不匹配。让我重新读取⽂件确认实际内容。
尝试 2：
  read({ file_path: 'config.js' })
  → 返回：port: 3001,
Agent 修正：
  原来实际端⼝是  3001 不是  3000 。
尝试 3：
  edit({ file_path: 'config.js', oldText: 'port: 3001,', newText: 'port: 8080,' })
  → 成功
最佳实践 建议
基于  OpenClaw 的 设计原 理 ， 以下是 规 划 与推理 的 最 佳 实 践 ：
1. 任务分解
将复杂任务分 解为可 管 理 的 子 任 务
使用子代理 并行 处 理 独 立 子 任 务
设置清晰 的子 任务 边 界
2. 错误处理
始终检查工 具返回 值
为关键操作 设置超 时
准备备用方 案
3. 记忆管理
主动将重要信息写 入  MEMORY.md
使用语义 搜索检 索 相关信息
定期整理和压缩 记 忆
4. 上下文优化

--- Page 112 ---

112使用  /compact 主动压缩长会话
利用技能按 需加 载 指 令
保持引导文 件简洁
5. 安全考虑
敏感操作 使用沙盒 执 行
启用工具策略和批 准 系 统
定期审查  exec 批 准列 表
本章小结
本章深入 剖析了  OpenClaw 的 三大 核 心工作机制 ：
Agent Loop 作为  OpenClaw 的 执 行 引 擎 ， 通过  8 个 步 骤 将 用户 输 入 转 化为系 统 响 应 。 其 序 列 化 执
行模型确 保会话 一 致 性 ， 而 队 列 系 统 和 流 式 输 出 则 提 供 了 良 好 的 并 发和用户体 验 。
工具系统 是 OpenClaw 与外部 世界 交 互 的 桥 梁 。 六 大类工 具 （文 件 操 作 、 命 令 执 行 、 浏 览器 控
制、消息通信 、会话 管 理 、 专业工 具 ）通过 统 一的 注 册 和权 限 控 制机制 ， 实现了安全 、 灵 活 的 扩 展 能
力。
记忆系统 使 OpenClaw 能 够 超 越 单 次会话 的 上下文 限 制 ， 实现 真 正 的 长 期 学 习 。 通过 两 层 记 忆 模
型（短期 日志和长 期记 忆 ）和 向 量 语 义 搜索 ， Agent 能 够 积 累 和 检 索 知 识 。
规划与推理 系统建立在  LLM 的 能力之上 ， 通过 任 务分 解 、 错 误 恢 复 和自我 修 正等机制 ， 实现了 复
杂任务的自主执行 。 多 级别 的 思 考 控 制和 队 列模 式为不同 场 景 提 供 了 灵 活性 。
理解这些工作 原理 ， 将 帮 助 用户更 有 效 地与  OpenClaw 协 作 ， 发 挥 其最大 潜 力 。
参考来源
文档版本 ： 2026.2.27
OpenClaw 版本 ： 2026.2.x

--- Page 113 ---

113参考来源
1. OpenClaw 官 方文 档  - Agent Loop: https://docs.openclaw.ai/concepts/agent-loop
2. OpenClaw 官 方文 档  - Memory: https://docs.openclaw.ai/concepts/memory
3. OpenClaw 官 方文 档  - System Prompt: https://docs.openclaw.ai/concepts/system-prompt
4. OpenClaw 官 方文 档  - Streaming: https://docs.openclaw.ai/concepts/streaming
5. OpenClaw 官 方文 档  - Compaction: https://docs.openclaw.ai/concepts/compaction
6. OpenClaw 官 方文 档  - Context: https://docs.openclaw.ai/concepts/context
7. OpenClaw 官 方文 档  - Agent Workspace: https://docs.openclaw.ai/concepts/agent-workspace
8. OpenClaw 官 方文 档  - Multi-Agent Routing: https://docs.openclaw.ai/concepts/multi-agent
9. OpenClaw 官 方文 档  - Command Queue: https://docs.openclaw.ai/concepts/queue
10. OpenClaw 官 方文 档  - Session Management Deep Dive: https://docs.openclaw.ai/reference/session-
management-compaction
11. OpenClaw 官 方文 档  - Browser: https://docs.openclaw.ai/tools/browser
12. OpenClaw 官 方文 档  - Sub-agents: https://docs.openclaw.ai/tools/subagents
13. OpenClaw 官 方文 档  - Model Providers: https://docs.openclaw.ai/concepts/model-providers
14. OpenClaw 官 方文 档  - Exec Tool: https://docs.openclaw.ai/tools/exec

--- Page 114 ---

114第4章  核 心 功 能 深 度 解 析
OpenClaw 作为 一 款先 进 的  AI Agent 平 台 ， 其 核 心 竞 争 力不 仅 体现在 架 构 设计 的 优 雅 性上 ， 更在
于一系列经过 精心 设计 的 核 心 功 能 模 块 。 本 章将 深 入 剖 析 内 存 系 统 、 多 代 理系 统 、 技能系 统 以 及 安全权
限机制四大核心 功 能 ， 揭 示 其技 术 实现 原 理与最 佳 实 践 方法 。
4.1 内存系 统 深度 解 析
内存系统是  OpenClaw 实现长 期 对话能力 的 关 键基 础 设 施 。 与 简单 的 消 息 历 史 存 储 不同 ，
OpenClaw 的内 存 系 统 采 用分 层架 构 设计 ， 结 合 向 量搜索 技 术 与 语 义 理 解 能力 ， 为  Agent 提 供 了接 近 人
类记忆的联 想式回 忆 机制 。
4.1.1 内存架 构 概 览
OpenClaw 的内 存 系 统 遵 循 **" 文 件即真 相 "** （ Files are the Source of Truth ） 的 设计 哲 学 。 所
有记忆以纯  Markdown 格 式 存 储 在  Agent 工作区 中， 模 型 仅 " 记 忆 " 被 写 入 磁 盘 的 内 容 。

--- Page 115 ---

115┌─────────────────────────────────────────────────────────────┐
│                    Memory System Architecture               │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│  │  Daily Logs  │    │ Long-term    │    │  Vector      │  │
│  │  (Short-term)│    │ Memory       │    │  Index       │  │
│  │              │    │ (Curated)    │    │              │  │
│  │ memory/      │    │ MEMORY.md    │    │ SQLite/      │  │
│  │ YYYY-MM-DD.md│    │              │    │ QMD Backend  │  │
│  └──────┬───────┘    └──────┬───────┘    └──────┬───────┘  │
│         │                   │                   │          │
│         └───────────────────┼───────────────────┘          │
│                             │                              │
│                    ┌────────┴────────┐                     │
│                    │  Memory Tools   │                     │
│                    │                 │                     │
│                    │ • memory_search │                     │
│                    │ • memory_get    │                     │
│                    └────────┬────────┘                     │
│                             │                              │
│                    ┌────────┴────────┐                     │
│                    │   AI Agent      │                     │
│                    │   (LLM Core)    │                     │
│                    └─────────────────┘                     │
│                                                             │
└─────────────────────────────────────────────────────────────┘
核心设计原则 ：
原则 说明 技术实现
持久化优先所有重要信息 必须 写 入文 件 Markdown 格式 存 储
分层存储区分短期 日志与长 期记 忆 每日日志  + MEMORY.md
语义检索 支持概念联 想而 非 关 键 词 匹 配 向量搜索  + 相似度 计 算
隐私可控长期记忆仅在主会话加 载 会话类型感知加 载 策 略
4.1.2 内存文 件 组 织 结 构
OpenClaw 采用 双 层 级 内 存 布 局 ：
4.1.2.1 每 日日志（ Daily Logs ）

--- Page 116 ---

116文件路径 ：memory/YYYY-MM-DD.md
每日日志 采用追加写入模式，记录当天 的 所 有 对话 摘 要和关 键 信息 ：
# 2026-02-27
## 上午会话
- 与⽤户讨论了  OpenClaw 内存系统架构
- 确定了⽂档章节结构： 4.1 内存系统、 4.2 多代理系统、 4.3 技能系统、 4.4 安全权限
- ⽤户偏好：代码引⽤需精确到⽂件级，包含架构图
## 下午会话   
- 查阅了官⽅⽂档  https://docs.openclaw.ai/concepts/memory
- 获取了向量搜索配置的详细信息
- 开始撰写第 4 章内容
## 关键决策
- 使⽤ SQLite + sqlite-vec 作为默认向量存储
- QMD 作为可选的⾼级后端
加载策略 ：
会话启动时自动 读取今天和昨天的日志
提供近期上下文 的 快 速 访 问
适合记录临时 的、有 时间 敏 感 性 的 信息
4.1.2.2 长 期记 忆 （ Long-term Memory ）
文件路径 ：MEMORY.md
长期记忆 采用精心策划模式，仅 保 存经过提 炼 的 重 要信息 ：

--- Page 117 ---

117# MEMORY.md - ⽤户⻓期记忆
## 专业背景
- **姓名： ** 星总
- **领域： ** ⾃动驾驶算法专家
- **⼯作模式： ** 处理复杂分析任务、开发与测试
- **沟通偏好： ** 可使⽤专业术语，关注结果与逻辑严谨性
## 项⽬信息
- **当前项⽬： ** 《 OpenClaw 完全指南》技术书籍编写
- **⽬标： ** 200 ⻚以内的专业  OpenClaw 技术指南
- **质量要求： ** 所有内容必须有官⽅来源验证
## 技术偏好
- 代码示例需要精确的⽂件路径引⽤
- 偏好包含架构图和流程图的技术⽂档
- 重视官⽅⽂档和源码级别的准确性
## 安全注意事项
- 私⼈信息严格保密
- 外部操作前需要确认
- 不在公开场合代表⽤户发⾔
加载策略 ：
仅在主会话（ main session ） 中 加 载
在群组聊天等 共享 上下文 中绝不加载
保护个人隐私和敏 感 信息
4.1.3 内存工 具接 口
OpenClaw 向  Agent 暴 露 两 个 核 心内 存 工 具 ：
4.1.3.1 memory_search - 语 义 搜索
功能： 在索引的文本片段 上 执 行 语 义 召 回 ， 即使 措 辞 不同 也 能 找 到相关 笔 记 。
调用示例 ：
// Agent 调⽤内存搜索
const results = await memory_search({
  query: "OpenClaw 的向量搜索是如何实现的？ ",
  limit: 5
});

--- Page 118 ---

118响应格式 ：
{
  "results": [
    {
      "text": " 向量搜索使⽤  sqlite-vec 扩展加速 ...",
      "path": "memory/2026-02-27.md",
      "line": 45,
      "score": 0.89
    },
    {
      "text": "QMD 后端结合了  BM25 + 向量  + 重排序 ...",
      "path": "MEMORY.md", 
      "line": 23,
      "score": 0.85
    }
  ]
}
4.1.3.2 memory_get - 定 向 读取
功能： 读取特定  Markdown 文 件 的 指 定行 范围 ， 支持 优 雅 的 降 级 处 理（文 件 不 存 在时 返 回 空 文本
而非抛出错误） 。
调用示例 ：
// 读取特定⽂件
const content = await memory_get({
  path: "memory/2026-02-27.md",
  offset: 1,
  limit: 50
});
4.1.4 向量搜索实现 原 理
OpenClaw 的 向 量搜索 系 统 是其内 存 系 统 的 核 心技 术 亮 点， 支持 多 种 嵌 入提 供 商 和 存 储 后 端 。
4.1.4.1 系 统架 构

--- Page 119 ---

119┌──────────────────────────────────────────────────────────────┐
│                  Vector Search Architecture                  │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   ┌─────────────┐                                           │
│   │ User Query  │                                           │
│   └──────┬──────┘                                           │
│          │                                                   │
│          ▼                                                    │
│   ┌─────────────────────────────────────┐                   │
│   │      Embedding Provider Selection   │                   │
│   │                                     │                   │
│   │  1. Local (node-llama-cpp)         │                   │
│   │  2. OpenAI (text-embedding-3)      │                   │
│   │  3. Gemini (gemini-embedding-001)  │                   │
│   │  4. Voyage AI                      │                   │
│   │  5. Mistral AI                     │                   │
│   └──────────┬──────────────────────────┘                   │
│              │                                               │
│              ▼                                                │
│   ┌─────────────────────────────────────┐                   │
│   │      Vector Embedding Generation    │                   │
│   │      (query → 1536-dim vector)     │                   │
│   └──────────┬──────────────────────────┘                   │
│              │                                               │
│              ▼                                                │
│   ┌─────────────────────────────────────────────────────┐   │
│   │              Similarity Computation                  │   │
│   │                                                     │   │
│   │   ┌─────────────┐         ┌─────────────────────┐   │   │
│   │   │  SQLite     │         │  QMD Backend        │   │   │
│   │   │  (Default)  │         │  (Experimental)     │   │   │
│   │   │             │         │                     │   │   │
│   │   │ • sqlite-vec│         │ • BM25 + Vector     │   │   │
│   │   │ • Cosine    │         │ • Reranking         │   │   │
│   │   │   Similarity│         │ • Query Expansion   │   │   │
│   │   └─────────────┘         └─────────────────────┘   │   │
│   │                                                     │   │
│   │   Similarity Score = cos( θ ) = (A·B) / (‖A‖ × ‖B‖)  │   │
│   └─────────────────────────────────────────────────────┘   │
│                              │                               │
│                              ▼                                │
│   ┌─────────────────────────────────────────────────────┐   │
│   │              Ranked Results                          │   │
│   │   Top-K most similar chunks with metadata           │   │
│   └─────────────────────────────────────────────────────┘   │

--- Page 120 ---

120│                                                              │
└──────────────────────────────────────────────────────────────┘
4.1.4.2 相似度 计 算算 法
OpenClaw 使用余弦相似度（Cosine Similarity ）作为 默 认 的 相 似 度度 量 ：
算法特性 ：
特性说明
值域理论上为  [-1, 1]； 实 际 应 用 中， 现 代 嵌 入 模 型 （ OpenAI text-embedding-3 、 Gemini
embedding-001 等） 输 出 的 向 量 经过 归 一 化 处 理 ， 相 似 度 计 算 结 果通 常 分 布 在  [0, 1] 区间
实际
分布现代嵌入 模 型（ OpenAI 、 Gemini 等） 输 出 的 向 量 经过 归 一 化和 训练 优 化 ， 实 际 相 似 度通 常 分 布 在
[0, 1] 区间
归一
化自动处理 向 量长度 差异 ， 仅 比 较 方 向
计算
效率O(n) 时间 复杂度 ， 适 合大 规 模 索 引similarity(A,B)=cos(θ)= =∥A∥×∥B∥A⋅B
 
 ×  A  ∑i=1n
i2
 B  ∑i=1n
i2 A ×B ∑i=1n
ii

--- Page 121 ---

121💡 理论与实 践 的差异
虽然余弦相似度 的 数学 值 域 是  [-1, 1] ， 但 在  OpenClaw 的 实 际 应 用 中， 你 很 少 看到 负 值 。 这
是因为：
1. 嵌入模型 训练特性：现代嵌入 模 型（如  OpenAI 的  text-embedding-3 系 列 、 Gemini 的
embedding-001）在 训练 过 程 中 优 化 的 是 语 义 相关性 ， 生成 的 向 量 在 语 义 空 间 中 趋 向 于同 一
象限
2. 归一化处理：大多数 嵌入  API 默 认 返 回  L2 归 一 化后 的 向 量 ， 使得 相 似 度 计 算 结 果 集 中 在  [0,
1] 区间
3. 实际应用 验 证：在  OpenClaw 的 语 义 搜索 实现 中， 典 型查 询 结 果 的 相关性分数通 常 在  0.6-
0.95 之间 ， 低于  0.5 的 结 果通 常被 视为不相关
因此，在 配 置相似 度 阈 值 时 ， 建议 以  0.7-0.8 作为 " 高相关性 " 的 参考基准 ， 而 非 以  0 作为 中 性
点。
代码实现 参考 ：
// 源码位置 : src/memory/vector-search.ts
function cosineSimilarity(a: Float32Array, b: Float32Array): number {
  let dotProduct = 0;
  let normA = 0;
  let normB = 0;
  
  for (let i = 0; i < a.length; i++) {
    dotProduct += a[i] * b[i];
    normA += a[i] * a[i];
    normB += b[i] * b[i];
  }
  
  return dotProduct / (Math.sqrt(normA) * Math.sqrt(normB));
}
4.1.4.3 嵌入提 供 商 自动 选 择
OpenClaw 实现了 智 能 的 嵌 入提 供 商 自动 选 择 机制 ：

--- Page 122 ---

122// 配置位置 : agents.defaults.memorySearch
// ⾃动选择优先级（从⾼到低）：
const providerPriority = [
  { type: 'local', condition: () => config.local?.modelPath && 
fs.existsSync(config.local.modelPath) },
  { type: 'openai', condition: () => resolveApiKey('openai') },
  { type: 'gemini', condition: () => resolveApiKey('google') },
  { type: 'voyage', condition: () => resolveApiKey('voyage') },
  { type: 'mistral', condition: () => resolveApiKey('mistral') }
];
配置示例 ：
// ~/.openclaw/openclaw.json
{
  agents: {
    defaults: {
      memorySearch: {
        provider: "gemini",              // 显式指定提供商
        model: "gemini-embedding-001",   // 嵌⼊模型
        remote: {
          apiKey: "${GEMINI_API_KEY}",   // API 密钥
          baseUrl: "https://generativelanguage.googleapis.com/v1beta",
          headers: { "X-Custom-Header": "value" }
        },
        fallback: "openai"               // 故障转移提供商
      }
    }
  }
}
4.1.4.4 混合 搜索（ Hybrid Search ）
注意: 混合搜索默 认禁 用 ， 需 要 显 式 启 用 ：
OpenClaw 内 置后 端 支持 混 合 搜索 模 式 ， 结 合 向 量 相 似 度和  BM25 关 键 词 相关性 ， 实现更全面 的 语
义检索：

--- Page 123 ---

123{
  agents: {
    defaults: {
      memorySearch: {
        query: {
          hybrid: {
            enabled: true,
            vectorWeight: 0.7,
            textWeight: 0.3,
            candidateMultiplier: 4,
            // 多样性优化  - MMR 重排序（默认禁⽤）
            mmr: {
              enabled: true,  // 默认 : false
              lambda: 0.7  // 相关性  vs 多样性平衡参数
            },
            // 时间衰减（新鲜度提升）（默认禁⽤）
            temporalDecay: {
              enabled: true,  // 默认 : false
              halfLifeDays: 30  // 30 天前的记忆分数减半
            }
          }
        }
      }
    }
  }
}
混合搜索核心 组 件 ：
组件 功能 配置参数
向量相似度 语义匹配 ，理 解 概 念 关联 vectorWeight (0-1)
BM25 关 键词精确匹配 ， 处理 术 语 和专 有 名 词 textWeight (0-1)
MMR 重排序 Maximal Marginal Relevance ， 平 衡 相关性与多 样 性 lambda (0-1)
时间衰减根据记忆年龄 调整 分数 ，新 信息 优先 halfLifeDays
MMR（ Maximal Marginal Relevance ） 算 法 ：
MMR 通过以下公式 计 算 每 个文 档 的 得 分 ：
MMR=λ×Sim(d,q)−(1−λ)×  Sim(d,d)
d∈S′max′

--- Page 124 ---

124$Sim(d, q)$: 文档与查 询 的相 似 度
: 文档与已选结果 的 最大相 似 度
: 平衡参数（ 0.7 表 示 侧 重 相关性 ， 0.3 表 示 侧 重 多 样 性）
时间衰减 计算（ 指 数 衰 减 ） ：
其中  
这与半衰 期公式等 价 ： 30 天后分数 减 半 。
4.1.4.5 嵌入 缓 存
OpenClaw 支持  chunk embeddings 缓 存 ， 避 免重复计 算 嵌 入 向 量 ， 显 著 提 升 性能 ：
{
  agents: {
    defaults: {
      memorySearch: {
        cache: {
          enabled: true,
          maxEntries: 50000  // 最⼤缓存条⽬数
        }
      }
    }
  }
}
缓存机制特 点：
基于文件内 容哈希 ， 内 容 不 变 时 复 用 缓 存
自动淘汰旧 条目（ LRU 策 略 ）
缓存持久化到  SQLite ， 重 启 后 仍 然 有 效
适用于频繁访问 的 长 期记 忆 文 件
4.1.5 QMD 高 级后 端 （实 验 性）
QMD（ Query Markdown ）是 一 个本地 优先 的 搜索 辅 助程 序 ， 结 合了  BM25 文本 搜索 、 向 量 语 义
搜索和重排序技 术 。
4.1.5.1 QMD 架 构maxSim(d,d)′
λ
decayedScore=score×e(−λ×ageInDays)
λ=ln(2)/halfLifeDays

--- Page 125 ---

125┌─────────────────────────────────────────────────────────────┐
│                    QMD Backend Flow                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────┐                                        │
│  │ Markdown Source │                                        │
│  │ (MEMORY.md +    │                                        │
│  │  memory/*.md)   │                                        │
│  └────────┬────────┘                                        │
│           │                                                 │
│           ▼                                                  │
│  ┌──────────────────────────────────────┐                  │
│  │          QMD Index Pipeline           │                  │
│  │                                       │                  │
│  │  1. Chunking (configurable size)     │                  │
│  │  2. BM25 Index Build                 │                  │
│  │  3. Vector Embedding (local GGUF)    │                  │
│  │  4. SQLite Storage                   │                  │
│  └──────────┬───────────────────────────┘                  │
│             │                                               │
│             ▼                                                │
│  ┌──────────────────────────────────────┐                  │
│  │          Search Pipeline              │                  │
│  │                                       │                  │
│  │  Query ── ►  BM25 Retrieval ── ►  Top 100 │                  │
│  │                │                      │                  │
│  │                ▼                       │                  │
│  │         Vector Reranking              │                  │
│  │         (Cross-encoder)               │                  │
│  │                │                      │                  │
│  │                ▼                       │                  │
│  │         Final Ranking ── ►  Top K       │                  │
│  └──────────────────────────────────────┘                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
4.1.5.2 QMD 配 置

--- Page 126 ---

126{
  memory: {
    backend: "qmd",                    // 启⽤  QMD 后端
    citations: "auto",                 // ⾃动添加引⽤标注
    
    qmd: {
      command: "qmd",                  // QMD 可执⾏⽂件路径
      searchMode: "search",            // search/vsearch/query
      includeDefaultMemory: true,      // ⾃动索引默认内存⽂件
      
      // 额外索引路径
      paths: [
        { name: "docs", path: "~/notes", pattern: "**/*.md" },
        { name: "projects", path: "~/projects", pattern: "**/*.md" }
      ],
      
      // 会话历史索引（可选）
      sessions: {
        enabled: true,
        retentionDays: 30,
        exportDir: "~/.openclaw/agents/main/qmd/sessions/"
      },
      
      // 更新配置
      update: {
        interval: "5m",                // 索引更新间隔
        debounceMs: 15000,             // 防抖时间
        onBoot: true,                  // 启动时更新
        waitForBootSync: false,        // 异步启动（不阻塞）
        embedInterval: "30m"           // 嵌⼊更新间隔
      },
      
      // 搜索限制
      limits: {
        maxResults: 6,                 // 最⼤返回结果数
        maxSnippetChars: 2000,         // ⽚段最⼤字符数
        maxInjectedChars: 8000,        // 注⼊上下⽂最⼤字符数
        timeoutMs: 4000                // 搜索超时
      },
      
      // 作⽤域控制（安全）
      scope: {
        default: "deny",
        rules: [
          { action: "allow", match: { chatType: "direct" } },
          { action: "deny", match: { keyPrefix: "discord:channel:" } }
        ]

--- Page 127 ---

127      }
    }
  }
}
4.1.6 记忆压 缩与 清 理
4.1.6.1 自动 记 忆 刷 新 机制
当会话接 近自动压 缩 阈 值 时 ， OpenClaw 会 触 发静默的  Agentic 轮 次，提醒模 型在上下文 被 压 缩 前
写入持久化 记忆 。

--- Page 128 ---

128┌─────────────────────────────────────────────────────────────┐
│              Memory Flush (Pre-compaction)                  │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Session Token Estimate                                     │
│       │                                                     │
│       ▼                                                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Trigger Condition:                                 │   │
│  │  tokens > contextWindow - reserveTokensFloor       │   │
│  │                    - softThresholdTokens            │   │
│  │                                                     │   │
│  │  Example: 128k window, 20k reserve, 4k threshold   │   │
│  │  Trigger at: 128k - 20k - 4k = 104k tokens         │   │
│  └─────────────────────────────────────────────────────┘   │
│                           │                                 │
│                           ▼                                  │
│  ┌─────────────────────────────────────────────────────┐   │
│  │  Silent Agent Turn                                  │   │
│  │                                                     │   │
│  │  System: "Session nearing compaction.               │   │
│  │           Store durable memories now."              │   │
│  │                                                     │   │
│  │  Prompt: "Write any lasting notes to               │   │
│  │           memory/YYYY-MM-DD.md;                     │   │
│  │           reply with NO_REPLY..."                   │   │
│  └─────────────────────────────────────────────────────┘   │
│                           │                                 │
│                           ▼                                  │
│                    [Memory Written]                         │
│                           │                                 │
│                           ▼                                  │
│                    [Context Compacted]                      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
配置参数 ：

--- Page 129 ---

129{
  agents: {
    defaults: {
      compaction: {
        reserveTokensFloor: 20000,      // 保留令牌数下限
        memoryFlush: {
          enabled: true,
          softThresholdTokens: 4000,    // 软阈值令牌数
          systemPrompt: "Session nearing compaction. Store durable memories now.",
          prompt: "Write any lasting notes to memory/YYYY-MM-DD.md; reply with 
NO_REPLY if nothing to store."
        }
      }
    }
  }
}
4.1.6.2 会话压 缩 策 略
当会话历史过长时 ， OpenClaw 会自动 执 行上下文 压 缩 ：
原始会话历史
     │
     ▼
┌────────────────────────────────────────┐
│  ┌────────────┐  ┌──────────────────┐  │
│  │ Recent N   │  │ Older Messages   │  │
│  │ (Keep)     │  │ (Compress)       │  │
│  │            │  │                  │  │
│  │ Full text  │  │ Summarized       │  │
│  │ preserved  │  │ into key points  │  │
│  └────────────┘  └──────────────────┘  │
└────────────────────────────────────────┘
     │
     ▼
压缩后的会话结构
压缩规则 ：

--- Page 130 ---

130阶段策略 说明
保留最近  10-20 条消息 完整保留 ， 确 保即 时上下文
压缩早期对话 总结为关 键信息 点
存档压缩内容 存入每日 记忆文 件
4.2 多代理系 统
OpenClaw 的多 代 理系 统 允 许 在同 一  Gateway 实 例 中 运 行多个 完 全 隔 离 的  Agent ， 每 个  Agent 拥
有独立的工作区 、 配 置 和会话 存 储 。 这为 团 队 协 作 、 多 场 景 应 用提 供 了 强 大 支持 。

--- Page 131 ---

1314.2.1 多代理架 构
┌─────────────────────────────────────────────────────────────────┐
│                     OpenClaw Gateway                            │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    Message Router                        │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐    │   │
│  │  │ Binding │  │ Binding │  │ Binding │  │ Binding │    │   │
│  │  │ Rules   │  │ Rules   │  │ Rules   │  │ Rules   │    │   │
│  │  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘    │   │
│  │       │            │            │            │          │   │
│  │       └────────────┴────────────┴────────────┘          │   │
│  │                      │                                   │   │
│  │                      ▼                                    │   │
│  │              ┌───────────────┐                          │   │
│  │              │ Route Decision│                          │   │
│  │              │ (Most Specific│                          │   │
│  │              │  Match Wins)  │                          │   │
│  │              └───────┬───────┘                          │   │
│  └──────────────────────┼──────────────────────────────────┘   │
│                         │                                       │
│         ┌───────────────┼───────────────┐                      │
│         │               │               │                      │
│         ▼                ▼                ▼                       │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐                 │
│  │ Agent A  │    │ Agent B  │    │ Agent C  │                 │
│  │          │    │          │    │          │                 │
│  │ • Workspace│   │ • Workspace│   │ • Workspace│                │
│  │ • AgentDir │   │ • AgentDir │   │ • AgentDir │                │
│  │ • Sessions │   │ • Sessions │   │ • Sessions │                │
│  │ • Auth     │   │ • Auth     │   │ • Auth     │                │
│  │ • Skills   │   │ • Skills   │   │ • Skills   │                │
│  └──────────┘    └──────────┘    └──────────┘                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
4.2.2 "一个 代理 " 的 定 义
在 OpenClaw 中，一 个  Agent 是一个完全独 立 的 作用 域 " 大 脑 " ， 包 含 ：

--- Page 132 ---

132组件 路径 说明
Workspace~/.openclaw/workspace-<agentId>文件、 AGENTS.md 、
SOUL.md 、 USER.md
AgentDir~/.openclaw/agents/<agentId>/agent认证配置 、 模 型注 册 表 、
Agent 配 置
Sessions ~/.openclaw/agents/<agentId>/sessions 聊天历史 、 路由状 态
Auth
Profiles~/.openclaw/agents/<agentId>/agent/auth-
profiles.json每 Agent 独 立 的 认证 信息
重要原则 ： 永远不要跨  Agent 重 用  agentDir，这会导 致 认证 /会话 冲 突 。
4.2.3 路由机制详 解
OpenClaw 采用确定性路由，遵循 "最 具体 匹 配优先 " 原 则 ：
4.2.3.1 路由 优先 级 （ 从 高到 低 ）
1. peer match ( 精确  DM/ 群组 / 频道  ID)
        ↓
2. parentPeer match ( 线程继承 )
        ↓
3. guildId + roles (Discord ⻆⾊路由 )
        ↓
4. guildId (Discord 服务器 )
        ↓
5. teamId (Slack 团队 )
        ↓
6. accountId match ( 频道账户 )
        ↓
7. channel-level match (accountId: "*")
        ↓
8. fallback to default agent (`agents.list[].default`) ，如果没有设置默认，则使⽤列表中的
第⼀个 agent ，默认为  `main`
规则说明 ：
优先级从高到 低依 次为 ：peer > parentPeer > guildId+roles > guildId > teamId > accountId
> channel > default
同一优先 级内 ， 配 置 文 件 中第一个匹配的规则生 效

--- Page 133 ---

133绑定设置多个 匹 配 字 段 时 ， 所 有 字 段 必 须 同时 满 足 （ AND 语 义 ）
省略  accountId 的绑定仅 匹 配默 认 账 户
使用  accountId: "*" 匹配频道内所 有账 户
4.2.3.2 绑定 配 置示 例

--- Page 134 ---

134{
  agents: {
    list: [
      {
        id: "main",
        default: true,
        workspace: "~/.openclaw/workspace",
        agentDir: "~/.openclaw/agents/main/agent"
      },
      {
        id: "work",
        workspace: "~/.openclaw/workspace-work",
        agentDir: "~/.openclaw/agents/work/agent"
      },
      {
        id: "family",
        workspace: "~/.openclaw/workspace-family",
        agentDir: "~/.openclaw/agents/family/agent"
      }
    ]
  },
  
  // 绑定规则（按优先级排序）
  bindings: [
    // 1. 特定  peer 路由（最⾼优先级）
    {
      agentId: "work",
      match: {
        channel: "whatsapp",
        peer: { kind: "direct", id: "+15551234567" }
      }
    },
    
    // 2. 特定群组路由
    {
      agentId: "family",
      match: {
        channel: "whatsapp",
        peer: { kind: "group", id: "1203630...@g.us" }
      }
    },
    
    // 3. Discord 服务器路由
    {
      agentId: "work",
      match: {
        channel: "discord",

--- Page 135 ---

135        guildId: "123456789012345678"
      }
    },
    
    // 4. 账户级别路由
    {
      agentId: "work",
      match: {
        channel: "whatsapp",
        accountId: "biz"
      }
    },
    
    // 5. 频道默认路由（最低优先级）
    {
      agentId: "main",
      match: {
        channel: "telegram",
        accountId: "*"
      }
    }
  ]
}
4.2.4 代理间通信
4.2.4.1 Agent-to-Agent 消 息 传 递
OpenClaw 支持  Agent 之间 的 显 式通信 ， 但 默 认关闭，需要显式启用 并 配 置 白 名 单 ：
{
  tools: {
    agentToAgent: {
      enabled: true,           // 启⽤代理间通信
      allow: ["home", "work"]  // 允许通信的  Agent ⽩名单
    }
  }
}
使用场景 ：
任务委托 ： 主 Agent 将特定 任 务 委托 给 专业  Agent
信息查询 ： 一个  Agent 向另 一 个  Agent 查 询 特定 领 域 的 知 识
工作流编排 ： 多个  Agent 协作 完 成 复 杂 业务 流程

--- Page 136 ---

1364.2.4.2 通信 流程
┌──────────┐                    ┌──────────┐
│ Agent A  │                    │ Agent B  │
│ (主代理 )  │                    │ ( 专业代理 )│
└────┬─────┘                    └────┬─────┘
     │                              │
     │  1. Send Message             │
     │  "请分析这段代码的  bug"       │
     │ ──────────────────────────── ► │
     │                              │
     │                              │ 2. Process
     │                              │    ( 独⽴会话 )
     │                              │
     │  3. Return Result            │
     │  "发现3 个问题 ..."            │
     │ ◄────────────────────────────│
     │                              │
     │ 4. Continue Task             │
     │    (整合结果 )                 │
     ▼                              ▼
4.2.5 负载均 衡与资 源管 理
4.2.5.1 会话 隔离 与 并 发 控 制
OpenClaw 通过队列化执行确保会话 一 致性 ：

--- Page 137 ---

137┌─────────────────────────────────────────────────────────────┐
│                  Session Lane System                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Session Key: "agent:main:telegram:user123"                 │
│                                                             │
│  ┌────────┐    ┌────────┐    ┌────────┐    ┌────────┐      │
│  │ Msg 1  │─── ► │ Msg 2  │─── ► │ Msg 3  │─── ► │ Msg 4  │      │
│  │        │    │        │    │        │    │        │      │
│  │ Queue  │    │ Queue  │    │ Queue  │    │ Queue  │      │
│  └────┬───┘    └────┬───┘    └────┬───┘    └────┬───┘      │
│       │             │             │             │          │
│       └─────────────┴─────────────┴─────────────┘          │
│                         │                                   │
│                         ▼                                    │
│              ┌─────────────────────┐                       │
│              │   Sequential        │                       │
│              │   Execution         │                       │
│              │   (One at a time)   │                       │
│              └─────────────────────┘                       │
│                         │                                   │
│                         ▼                                    │
│              ┌─────────────────────┐                       │
│              │   Session State     │                       │
│              │   Consistency       │                       │
│              └─────────────────────┘                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
关键机制 ：
每个会话 键（ Session Key ） 拥 有 独 立 的 执 行 队 列
消息按到 达顺序 串 行 处 理
防止工具 /会话竞 态条件
保持会话 历史 的一 致 性
4.2.5.2 队 列模式
消息通道可 选 择不同 的 队 列模 式 ：

--- Page 138 ---

138模式 行为 适用场景
collect 收集模式 ，批 量 处 理 低频高容量消息
steer 引导模式 ， 允 许干预 需要人工 介入
followup 跟进模式 ，自动回 复 标准对话 场 景
4.2.6 Per-Agent 沙 盒 配 置
从 v2026.1.6 开 始 ， OpenClaw 支持 为 每 个  Agent 配 置 独 立 的 沙 盒 和工 具限 制 ， 实现更 精 细 的 安全
隔离：

--- Page 139 ---

139{
  agents: {
    list: [
      {
        id: "personal",
        sandbox: { 
          mode: "off"  // ⽆沙盒限制
        },
        // ⽆⼯具限制，可使⽤所有⼯具
      },
      {
        id: "family",
        sandbox: {
          mode: "all",           // 启⽤完整沙盒
          scope: "agent",        // 沙盒作⽤域
          docker: {
            setupCommand: "apt-get update && apt-get install -y git curl",
            image: "openclaw/sandbox:latest"
          }
        },
        tools: {
          allow: ["read", "memory_search"],  // ⽩名单
          deny: ["exec", "write", "edit", "browser"]   // ⿊名单
        }
      },
      {
        id: "coding",
        sandbox: {
          mode: "all",
          scope: "session"       // 每会话独⽴沙盒
        },
        tools: {
          policy: {
            exec: { permission: "allow" },     // 允许执⾏
            write: { permission: "allow" },    // 允许写⼊
            browser: { permission: "deny" }    // 禁⽤浏览器
          }
        }
      }
    ]
  }
}
Per-Agent 沙 盒 配 置 项 ：

--- Page 140 ---

140配置项 类型说明
sandbox.mode stringoff / read-only / all，沙盒级别
sandbox.scope stringagent（Agent 级共享） / session（会话级 隔离）
sandbox.docker object Docker 沙盒 配 置
tools.allow array 允许的工 具 列表（ 白 名 单 模 式）
tools.deny array禁止的工 具 列表（ 黑 名 单 模 式）
tools.policy object细粒度工 具策略 配 置
安全隔离层 级 ：
┌─────────────────────────────────────────────────────────────┐
│                    Per-Agent Isolation                      │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐         │
│  │  Agent A    │  │  Agent B    │  │  Agent C    │         │
│  │  (personal) │  │  (family)   │  │  (coding)   │         │
│  │             │  │             │  │             │         │
│  │ • No sandbox│  │ • Full      │  │ • Full      │         │
│  │ • All tools │  │   sandbox   │  │   sandbox   │         │
│  │             │  │ • Read-only │  │ • Exec      │         │
│  │             │  │   tools     │  │   allowed   │         │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘         │
│         │                │                │                │
│         └────────────────┼────────────────┘                │
│                          │                                 │
│                   ┌──────┴──────┐                         │
│                   │  Gateway    │                         │
│                   │  (Shared)   │                         │
│                   └─────────────┘                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
4.2.7 多平 台多账 户 配 置
4.2.6.1 WhatsApp 多号 码 配 置

--- Page 141 ---

141{
  agents: {
    list: [
      { id: "home", workspace: "~/.openclaw/workspace-home" },
      { id: "work", workspace: "~/.openclaw/workspace-work" }
    ]
  },
  
  bindings: [
    { agentId: "home", match: { channel: "whatsapp", accountId: "personal" } },
    { agentId: "work", match: { channel: "whatsapp", accountId: "biz" } }
  ],
  
  channels: {
    whatsapp: {
      accounts: {
        personal: { /* 个⼈号配置  */ },
        biz: { /* ⼯作号配置  */ }
      }
    }
  }
}
配置命令 ：
# 分别登录两个  WhatsApp 账号
openclaw channels login --channel whatsapp --account personal
openclaw channels login --channel whatsapp --account biz
4.2.6.2 Discord 多机 器 人 配 置

--- Page 142 ---

142{
  agents: {
    list: [
      { id: "main", workspace: "~/.openclaw/workspace-main" },
      { id: "coding", workspace: "~/.openclaw/workspace-coding" }
    ]
  },
  
  bindings: [
    { agentId: "main", match: { channel: "discord", accountId: "default" } },
    { agentId: "coding", match: { channel: "discord", accountId: "coding" } }
  ],
  
  channels: {
    discord: {
      groupPolicy: "allowlist",
      accounts: {
        default: {
          token: "DISCORD_BOT_TOKEN_MAIN",
          guilds: {
            "123456789012345678": {
              channels: {
                "222222222222222222": { allow: true, requireMention: false }
              }
            }
          }
        },
        coding: {
          token: "DISCORD_BOT_TOKEN_CODING",
          guilds: {
            "123456789012345678": {
              channels: {
                "333333333333333333": { allow: true, requireMention: false }
              }
            }
          }
        }
      }
    }
  }
}

--- Page 143 ---

1434.3 技能系 统
技能系统（ Skills System ）是  OpenClaw 扩 展 能力 的 核 心机制 。 通过 标 准 化 的  SKILL.md 格 式 ，
开发者可以为  Agent 添 加 新的 能力 ， 实现与外部工 具 、 API 和服务 的 集 成 。

--- Page 144 ---

1444.3.1 技能系 统架 构
┌─────────────────────────────────────────────────────────────────┐
│                     Skills System Architecture                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    Skill Discovery                       │   │
│  │                                                          │   │
│  │   ┌──────────────┐      ┌──────────────┐               │   │
│  │   │ Local Skills │      │ Global Skills│               │   │
│  │   │              │      │              │               │   │
│  │   │ workspace/   │      │ ~/.openclaw/ │               │   │
│  │   │ skills/      │      │ skills/      │               │   │
│  │   └──────────────┘      └──────────────┘               │   │
│  │            │                   │                       │   │
│  │            └─────────┬─────────┘                       │   │
│  │                      ▼                                   │   │
│  │         ┌────────────────────────┐                     │   │
│  │         │   Skill Registry       │                     │   │
│  │         │   (Loading & Caching)  │                     │   │
│  │         └───────────┬────────────┘                     │   │
│  └─────────────────────┼──────────────────────────────────┘   │
│                        │                                       │
│                        ▼                                        │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                 Skill Resolution                         │   │
│  │                                                          │   │
│  │   User Query ── ►  Intent Detection ── ►  Skill Matching   │   │
│  │                                                          │   │
│  │   • Name matching       • Description similarity        │   │
│  │   • Keyword matching    • Capability matching           │   │
│  │                                                          │   │
│  └────────────────────────┬────────────────────────────────┘   │
│                           │                                     │
│                           ▼                                      │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                  Skill Execution                         │   │
│  │                                                          │   │
│  │   ┌──────────┐    ┌──────────┐    ┌──────────┐         │   │
│  │   │ Parse    │─── ► │ Validate │─── ► │ Execute  │         │   │
│  │   │ SKILL.md │    │ Params   │    │ Tool     │         │   │
│  │   └──────────┘    └──────────┘    └──────────┘         │   │
│  │                                          │              │   │
│  │                                          ▼               │   │
│  │                              ┌─────────────────────┐    │   │

--- Page 145 ---

145│  │                              │ Return Result to    │    │   │
│  │                              │ Agent               │    │   │
│  │                              └─────────────────────┘    │   │
│  │                                                          │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
4.3.2 SKILL.md 格 式 规 范
SKILL.md 是  OpenClaw 技能 的 标 准 定 义 文 件 ， 采 用  YAML Front Matter + Markdown 的 混 合
格式。
4.3.2.1 完 整 格式定 义

--- Page 146 ---

146---
name: skill-name                    # 技能标识符（必填）
description: " 简短描述 "            # 技能描述（必填）
homepage: https://example.com      # 技能主⻚（可选）
metadata:                          # 元数据（可选）
  {
    "openclaw": {
      "emoji": " 🔧 ",               # 技能图标
      "requires": {                # 依赖要求
        "bins": ["gh", "git"],     # 必需的⼆进制⽂件
        "env": ["GITHUB_TOKEN"],   # 必需的环境变量
        "node": ">=18.0.0"         # Node.js 版本要求
      },
      "install": [                 # 安装指令
        {
          "id": "brew",
          "kind": "brew",
          "formula": "gh",
          "bins": ["gh"],
          "label": "Install via Homebrew"
        },
        {
          "id": "apt",
          "kind": "apt",
          "package": "gh",
          "bins": ["gh"],
          "label": "Install via apt"
        }
      ],
      "primaryEnv": "GITHUB_TOKEN" # 主环境变量
    }
  }
---
# Skill Name
## When to Use
✅ **使⽤场景： **
- 场景1 的具体描述
- 场景2 的具体描述
❌ **不适⽤场景： **
- 不适⽤的场景 1
- 不适⽤的场景 2
## Usage

--- Page 147 ---

147### 命令1
```bash
command1 arg1 arg2
```
参数说明：
- `arg1`: 参数 1 说明
- `arg2`: 参数 2 说明
### 命令2
```bash
command2 --option value
```
## Examples
### 示例1 ： xxx
```bash
# 具体命令
command --specific-args
```
### 示例2 ： yyy
```bash
# 具体命令
command --other-args
```
## Notes
- 注意事项 1
- 注意事项 2
4.3.2.2 字段详 解

--- Page 148 ---

148字段 类型必
填说明
name string ✅技能唯一 标 识 符 ， 小 写 字 母 + 连 字 符
description string ✅技能功能描述 ，用于 匹 配 用户意图
homepage string ❌技能官方主页 或文 档 链 接
user-invocable boolean❌是否作为用户 斜 杠 命 令 暴 露 （ 默 认  true）
disable-model-invocation boolean❌是否从模 型提 示 中 排 除 （ 默 认  false）
command-dispatch string ❌ 设为  tool 时斜杠命令 直接分 派 到工 具
command-tool string ❌command-dispatch: tool 时调用的工 具
名
command-arg-mode string ❌参数转发 模式 ，raw（默认） 转发 原 始参 数
字符串
metadata.openclaw object ❌ OpenClaw 特定 的 元 数 据
metadata.openclaw.emoji string ❌技能图标 ， 显 示在对话 中
metadata.openclaw.requires object ❌依赖要求定义
metadata.openclaw.requires.bins array ❌ 必需的可 执行文 件 列 表
metadata.openclaw.requires.env array ❌ 必需的环境 变 量 列 表
metadata.openclaw.install array ❌自动安装 指令
metadata.openclaw.primaryEnv string ❌主要环境 变 量名 称
字段使用 示例 ：

--- Page 149 ---

149---
name: github
user-invocable: true              # ⽤户可⽤  /github 调⽤
disable-model-invocation: false   # 模型可以看到此技能
command-dispatch: tool            # 斜杠命令直接分派到⼯具
command-tool: gh                  # 调⽤  gh ⼯具
command-arg-mode: raw             # 原始参数传递
description: "GitHub operations via gh CLI..."
metadata:
  openclaw:
    emoji: " 🐙 "
    requires:
      bins: ["gh"]
      env: ["GITHUB_TOKEN"]
---
4.3.2.3 典 型  SKILL.md 示 例
示例 1： GitHub Skill

--- Page 150 ---

150---
name: github
description: "GitHub operations via `gh` CLI: issues, PRs, CI runs, code review, 
API queries. Use when: (1) checking PR status or CI, (2) creating/commenting on 
issues, (3) listing/filtering PRs or issues, (4) viewing run logs. NOT for: complex 
web UI interactions requiring manual browser flows, bulk operations across many 
repos, or when gh auth is not configured."
metadata:
  {
    "openclaw":
      {
        "emoji": " 🐙 ",
        "requires": { "bins": ["gh"] },
        "install":
          [
            {
              "id": "brew",
              "kind": "brew",
              "formula": "gh",
              "bins": ["gh"],
              "label": "Install GitHub CLI (brew)",
            },
            {
              "id": "apt",
              "kind": "apt",
              "package": "gh",
              "bins": ["gh"],
              "label": "Install GitHub CLI (apt)",
            },
          ],
      },
  }
---
# GitHub Skill
## When to Use
✅ **USE this skill when:**
- Checking PR status, reviews, or merge readiness
- Viewing CI/workflow run status and logs
- Creating, closing, or commenting on issues
- Creating or merging pull requests
❌ **DON'T use this skill when:**
- Local git operations (commit, push, pull) → use `git` directly
- Non-GitHub repos (GitLab, Bitbucket) → different CLIs

--- Page 151 ---

151- Cloning repositories → use `git clone`
## Setup
```bash
# Authenticate (one-time)
gh auth login
# Verify
gh auth status
```
## Common Commands
### Pull Requests
```bash
# List PRs
gh pr list --repo owner/repo
# Check CI status
gh pr checks 55 --repo owner/repo
# View PR details
gh pr view 55 --repo owner/repo
```
示例 2： Tavily Search Skill

--- Page 152 ---

152---
name: tavily
description: AI-optimized web search via Tavily API. Returns concise, relevant 
results for AI agents.
homepage: https://tavily.com
metadata: {"openclaw":{"emoji":" 🔍 ","requires":{"bins":["node"],"env":
["TAVILY_API_KEY"]},"primaryEnv":"TAVILY_API_KEY"}}
---
# Tavily Search
AI-optimized web search using Tavily API. Designed for AI agents - returns clean, 
relevant content.
## Search
```bash
node {baseDir}/scripts/search.mjs "query"
node {baseDir}/scripts/search.mjs "query" -n 10
node {baseDir}/scripts/search.mjs "query" --deep
```
## Options
- `-n <count>`: Number of results (default: 5, max: 20)
- `--deep`: Use advanced search for deeper research
- `--topic <topic>`: Search topic - `general` or `news`
## Extract content from URL
```bash
node {baseDir}/scripts/extract.mjs "https://example.com/article"
```
Notes:
- Needs `TAVILY_API_KEY` from https://tavily.com
- Tavily is optimized for AI - returns clean, relevant snippets
4.3.3 技能加 载机制
4.3.3.1 技能 搜索路 径
OpenClaw 按以下 顺 序 搜索 技能 ：

--- Page 153 ---

1531. **Workspace skills**: `{workspace}/skills/{skill-name}/SKILL.md` ( 最⾼优先级 )
2. **Managed/Local skills**: `~/.openclaw/skills/{skill-name}/SKILL.md`
3. **Bundled skills**: `/opt/homebrew/lib/node_modules/openclaw/skills/{skill-
name}/SKILL.md` ( 最低优先级 )
注意: 如果技能名 称冲 突 ， 优先 级 高 的 技能会 覆 盖 优先 级 低 的 技能 。
4.3.3.2 技能加 载流程
┌─────────────────────────────────────────────────────────────┐
│                  Skill Loading Pipeline                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. DISCOVERY                                               │
│     ├── Scan workspace/skills/                             │
│     ├── Scan ~/.openclaw/skills/                           │
│     └── Scan built-in skills directory                     │
│                          │                                  │
│                          ▼                                   │
│  2. PARSING                                                 │
│     ├── Read SKILL.md                                      │
│     ├── Parse YAML Front Matter                            │
│     └── Validate metadata schema                           │
│                          │                                  │
│                          ▼                                   │
│  3. RESOLUTION                                              │
│     ├── Check binary dependencies                          │
│     ├── Check environment variables                        │
│     └── Verify tool availability                           │
│                          │                                  │
│                          ▼                                   │
│  4. CACHING                                                 │
│     ├── Create skill snapshot                              │
│     ├── Index for quick lookup                             │
│     └── Store in memory cache                              │
│                          │                                  │
│                          ▼                                   │
│  5. INJECTION                                               │
│     ├── Add to system prompt                               │
│     ├── Register tool handlers                             │
│     └── Make available to agent                            │
│                                                             │
└─────────────────────────────────────────────────────────────┘

--- Page 154 ---

1544.3.4 Token 影响
技能列表注入系 统 提 示 会产生 一 定 的  token 开 销 ， 了 解 其 计 算 方式 有 助 于 优 化  Agent 配 置 ：
Token 开 销 计算公式 ：
total = 195 + Σ (97 + len(name_escaped) + len(description_escaped) + 
len(location_escaped))
重要说明:
XML 转义会增加 字 符 长度 ：& → &amp;, < → &lt;, > → &gt;, " → &quot;, ' →
&apos;
Token 估算 基于 模 型 分 词 器 ， OpenAI 风格 约 为  4 字 符 /token
实际开销可能 因特 殊 字 符 而 增 加
组成部分 说明
基础开销 195 字符（当  ≥ 1 个技能时）
每个技能 97 字符  + 转义后 的 名 称 、 描述 、 位 置 长度
估算 约 97 字符  ≈  24 tokens （ OpenAI 风格 ）
实际示例 ：
10 个技能约增加：
195 + 10 × (97 + 20 + 50 + 15) = 约  2000 字符  ≈ 500 tokens
优化建议 ：
保持技能描述 简洁 ， 聚 焦 核 心 功 能
使用  disable-model-invocation: true 隐藏不需要 模 型感 知 的 技能
定期清理工作区 中 未 使 用 的 技能
对于高频场 景 ， 考 虑 合 并 相关技能
4.3.5 社区技能生 态
4.3.4.1 ClawHub 技能市 场

--- Page 155 ---

155ClawHub（https://clawhub.com ）是 OpenClaw 的 官 方技能市 场 ， 提 供 技能 的 发现 、 安 装 和发
布功能。
常用命令 ：
# 安装 ClawHub CLI
npm i -g clawhub
# 搜索技能
clawhub search "postgres backups"
clawhub search "github"
# 安装技能
clawhub install my-skill
clawhub install my-skill --version 1.2.3
# 更新技能
clawhub update my-skill
clawhub update --all
# 列出已安装技能
clawhub list
# 发布技能
clawhub publish ./my-skill \
  --slug my-skill \
  --name "My Skill" \
  --version 1.2.0 \
  --changelog "Fixes + docs"
4.3.4.2 技能分类
类别说明 示例
开发工具 代码管理 、 CI/CD github, coding-agent, gh-issues
生产力笔记、任务 、日 历 apple-notes, apple-reminders, things-mac
通信 消息、邮件 、通话 imsg, himalaya, discord
媒体图片、视 频 、 音 频 songsee, video-frames, gifgrep
智能家居 设备控制 openhue, eightctl, sonoscli
搜索信息检索 tavily, web_search, web_fetch

--- Page 156 ---

1564.3.5 自定义技能开发
4.3.5.1 开发 流程
┌─────────────────────────────────────────────────────────────┐
│                 Custom Skill Development                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. PLAN                                                    │
│     └── Define skill scope and use cases                   │
│                          │                                  │
│                          ▼                                   │
│  2. STRUCTURE                                               │
│     └── Create skill directory structure                   │
│         my-skill/                                          │
│         ├── SKILL.md                                       │
│         ├── scripts/                                       │
│         └── README.md                                      │
│                          │                                  │
│                          ▼                                   │
│  3. IMPLEMENT                                               │
│     └── Write SKILL.md with:                               │
│         - Clear description                                │
│         - Usage examples                                   │
│         - Setup instructions                               │
│                          │                                  │
│                          ▼                                   │
│  4. TEST                                                    │
│     └── Validate skill functionality                       │
│         - Test in local workspace                          │
│         - Verify all examples work                         │
│                          │                                  │
│                          ▼                                   │
│  5. PUBLISH (Optional)                                      │
│     └── Share with community                               │
│         - Publish to ClawHub                               │
│         - Share on Discord                                 │
│                                                             │
└─────────────────────────────────────────────────────────────┘
4.3.5.2 技能 目录 结 构

--- Page 157 ---

157my-skill/
├── SKILL.md              # 技能定义⽂件（必需）
├── README.md             # 详细⽂档（可选）
├── scripts/              # 辅助脚本（可选）
│   ├── search.mjs
│   └── extract.mjs
├── assets/               # 静态资源（可选）
│   └── icon.png
└── examples/             # 示例⽂件（可选）
    └── example1.md
4.3.5.3 开发最佳 实 践
1. 描述清 晰 具体
# ✅ 好的描述
"GitHub operations via `gh` CLI: issues, PRs, CI runs. Use when checking PR status, 
creating issues. NOT for local git operations."
# ❌ 差的描述
"A skill for GitHub"
2. 提供完 整 示例
## Examples
### List open issues
```bash
gh issue list --repo owner/repo --state open
```
### Check PR CI status
```bash
gh pr checks 42 --repo owner/repo
```
3. 明确边 界 条件

--- Page 158 ---

158## When to Use
✅ **USE when:**
- Checking PR status or CI
- Creating/commenting on issues
❌ **DON'T use when:**
- Local git operations → use `git` directly
- Non-GitHub repos
4. 声明依 赖关系
metadata:
  openclaw:
    requires:
      bins: ["gh", "jq"]           # 必需命令
      env: ["GITHUB_TOKEN"]        # 必需环境变量
      node: ">=18.0.0"             # Node 版本
4.4 安全与权 限
安全是  OpenClaw 设计 的 核 心 考 量 。 系 统 通过多 层 次 的 安全机制 ， 确 保  Agent 在 执 行 任 务时 既 能
充分发挥能力 ， 又 不会 造 成意外 的 安全 风 险 。

--- Page 159 ---

1594.4.1 安全架 构 概 览
┌─────────────────────────────────────────────────────────────────┐
│                     Security Architecture                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                  Policy Layers                           │   │
│  │                                                          │   │
│  │   Layer 1: Global Config          ~/.openclaw/          │   │
│  │   Layer 2: Agent Config           per-agent             │   │
│  │   Layer 3: Tool Policy            per-tool              │   │
│  │   Layer 4: Provider Policy        per-LLM               │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                              │                                  │
│                              ▼                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                  Protection Mechanisms                   │   │
│  │                                                          │   │
│  │   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │   │
│  │   │   Sandbox    │  │  Allowlist   │  │ Confirmation │ │   │
│  │   │   Mode       │  │   Access     │  │   Required   │ │   │
│  │   │              │  │   Control    │  │              │ │   │
│  │   │ • File       │  │              │  │ • Destructive│ │   │
│  │   │   system     │  │ • Peer       │  │   ops        │ │   │
│  │   │ • Network    │  │   allowlist  │  │ • External   │ │   │
│  │   │ • Execution  │  │ • Channel    │  │   sends      │ │   │
│  │   │              │  │   policy     │  │ • Large      │ │   │
│  │   │              │  │              │  │   transfers  │ │   │
│  │   └──────────────┘  └──────────────┘  └──────────────┘ │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                              │                                  │
│                              ▼                                   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                  Audit & Monitoring                      │   │
│  │                                                          │   │
│  │   • Session Logging         • Tool Call Traces          │   │
│  │   • Message History         • Error Tracking            │   │
│  │   • Configuration Changes   • Access Attempts           │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

--- Page 160 ---

1604.4.2 工具权 限控 制
4.4.2.1 工 具策略 配 置
OpenClaw 允 许在多个 层 级 配 置 工 具 权 限 ：

--- Page 161 ---

161{
  // Layer 1: Global defaults
  tools: {
    defaults: {
      permission: "allow",           // 默认允许所有⼯具
      dangerousPermission: "confirm" // 危险操作需要确认
    },
    
    // Layer 3: Per-tool policy
    policy: {
      // 完全禁⽤某些⼯具
      exec: { permission: "deny" },
      process: { permission: "deny" },
      
      // 特定⼯具配置
      browser: {
        permission: "allow",
        dangerousPermission: "confirm",
        options: {
          allowedDomains: ["*.github.com", "*.openclaw.ai"]
        }
      },
      
      file: {
        permission: "allow",
        dangerousPermission: "confirm",
        options: {
          allowOutsideWorkspace: false
        }
      }
    }
  },
  
  // Layer 2: Per-agent override
  agents: {
    list: [
      {
        id: "coding",
        tools: {
          policy: {
            exec: { permission: "allow" }  // coding agent 允许  exec
          }
        }
      }
    ]

--- Page 162 ---

162  }
}
权限级别 ：
级别 说明 适用场景
allow 允许使用 安全工具（如  read 、 search ）
confirm 需要确认 危险操作（如  delete 、 exec ）
deny 完全禁用 高风险工 具（如  rm -rf ）
4.4.2.2 危险操作定 义
以下操作 被视为危 险操 作 ， 默 认 需 要 确 认 ：
// 源码参考 : src/tools/policy.ts
const DANGEROUS_OPERATIONS = [
  // ⽂件系统
  { tool: 'write', path: '/etc/*' },           // 写⼊系统⽬录
  { tool: 'edit', pathMatches: /\.env$/ },     // 编辑环境⽂件
  { tool: 'delete', recursive: true },          // 递归删除
  
  // 执⾏
  { tool: 'exec', command: /rm\s+.*-rf?/ },     // 强制删除
  { tool: 'exec', command: /sudo/ },            // 提权执⾏
  { tool: 'exec', command: /curl.*\|.*sh/ },    // 管道执⾏远程脚本
  
  // ⽹络
  { tool: 'fetch', protocol: 'http' },          // ⾮安全协议
  { tool: 'message', bulk: true },              // 批量消息发送
  
  // 系统
  { tool: 'process', action: 'kill' },          // 终⽌进程
];
4.4.3 敏感操作 确 认 机制
4.4.3.1 确 认流程

--- Page 163 ---

163┌─────────────────────────────────────────────────────────────┐
│               Sensitive Operation Confirmation              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Agent 请求执⾏危险操作                                      │
│       │                                                     │
│       ▼                                                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 1. Detect Dangerous Operation                       │   │
│  │                                                     │   │
│  │   Tool: exec                                        │   │
│  │   Command: "rm -rf /important/data"                │   │
│  │   Risk Level: HIGH                                  │   │
│  └─────────────────────────────────────────────────────┘   │
│       │                                                     │
│       ▼                                                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 2. Pause Execution                                  │   │
│  │                                                     │   │
│  │   Status: WAITING_FOR_CONFIRMATION                  │   │
│  └─────────────────────────────────────────────────────┘   │
│       │                                                     │
│       ▼                                                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 3. Present to User                                  │   │
│  │                                                     │   │
│  │   ⚠  敏感操作需要确认                                 │   │
│  │                                                     │   │
│  │   操作 : 删除⽬录                                      │   │
│  │   路径 : /important/data                             │   │
│  │   命令 : rm -rf /important/data                      │   │
│  │                                                     │   │
│  │   [ 确认执⾏ ]  [ 取消 ]  [ 修改命令 ]                     │   │
│  └─────────────────────────────────────────────────────┘   │
│       │                                                     │
│       ▼                                                      │
│  ┌─────────────────────────────────────────────────────┐   │
│  │ 4. User Decision                                    │   │
│  │                                                     │   │
│  │   Option A: Confirm ── ►  Execute & Log              │   │
│  │   Option B: Cancel ─── ►  Abort & Return Error       │   │
│  │   Option C: Modify ─── ►  Update Command & Re-eval   │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘

--- Page 164 ---

1644.4.3.2 配 置 确 认 行为
{
  tools: {
    defaults: {
      // 危险操作确认⽅式
      dangerousPermission: "confirm",  // confirm / allow / deny
      
      // 确认超时设置
      confirmationTimeout: "5m",
      
      // 批量确认阈值
      bulkConfirmationThreshold: 10
    }
  }
}
4.4.4 沙盒 模式
4.4.4.1 沙 盒 级别
OpenClaw 提 供可 选 的 沙 盒 来 限 制  Agent 权 限 ：
{
  agents: {
    defaults: {
      sandbox: {
        mode: "non-main",  // "off" | "non-main" | "all"
        scope: "session",   // "session" | "agent" | "shared"
        workspaceAccess: "none"  // "none" | "ro" | "rw"
      }
    }
  }
}
沙盒模式说明 ：
模式 行为 适用场景
"off"不启用沙盒 完全信任 环境
"non-main"仅对非主会话启用 沙 盒 （ 默 认 ） 日常聊天在主会话 ， 其 他 会话 沙 盒 化
"all"所有会话 都在沙盒 中 运 行 高安全要 求 环境

--- Page 165 ---

165沙盒级别对 比 ：
级别文件系统 网络 执行命令适用场景
off 无限制 无限制 无限制 完全信任 环境
non-main 非主会话 限制 非主会话 限制 非主会话 限制 日常开发（推 荐）
all 完全限制 完全限制 完全限制高风险环境
4.4.4.2 工作区 隔 离
每个  Agent 拥 有独 立 的 工作区 ， 默 认 作为当前工作 目 录 ：
~/.openclaw/
├── workspace/              # 默认  Agent ⼯作区
│   ├── skills/            # Agent 专属技能
│   ├── memory/            # Agent 记忆⽂件
│   ├── AGENTS.md          # Agent ⾏为规范
│   ├── SOUL.md            # Agent 身份定义
│   └── USER.md            # ⽤户信息
│
├── workspace-work/        # "work" Agent ⼯作区
│   ├── skills/
│   └── ...
│
└── workspace-family/      # "family" Agent ⼯作区
    ├── skills/
    └── ...
注意： 相对路径在工作区内 解 析 ， 但 绝 对 路 径 可 访 问主机其 他 位 置 ， 除非 启 用 沙 盒 。
4.4.5 访问控制
4.4.5.1 配对机制（ Pairing ）
DM（私信）安全通过 配 对机制 控 制 ：

--- Page 166 ---

166{
  channels: {
    telegram: {
      dmPolicy: "pairing",        // pairing / allowlist / allowall
      
      // 配对模式：需要⽤户先发消息才能回复
      // 适合：公共机器⼈，防⽌垃圾消息
    },
    
    whatsapp: {
      dmPolicy: "allowlist",
      allowFrom: ["+15551230001", "+15551230002"],
      
      // ⽩名单模式：只允许特定联系⼈
      // 适合：私⼈助理，限制访问范围
    }
  }
}
DM 策略类 型 ：
策略 行为 安全级别
pairing 用户先发 消息后  Agent 才 能回 复 高
allowlist仅白名单 中的用户可以 交 互 很高
allowall 允许所有用户（不推 荐 用于生产） 低
4.4.5.2 DM 会话 隔 离 （ dmScope ）
OpenClaw 支持通过  dmScope 配置控制私信会话 的 隔 离 级别 ， 平 衡 安全性与 连 续 性 ：
{
  session: {
    dmScope: "per-channel-peer"  // 或  "per-account-channel-peer" / "main"
  }
}
dmScope 模式详 解 ：

--- Page 167 ---

167模式 行为 适用场景
"main"（默认）所有  DM 共享 一个主会话 ， 保持 长 期 连 续
性个人助理 ， 需要 记 忆 历 史 对
话
"per-channel-peer"每个  channel + sender 组 合 拥 有 独 立 会
话安全  DM 模式 ， 隔 离 不同来
源的对话
"per-account-channel-
peer"多账户场 景下 ， 每 个 账 户 的  channel +
sender 独 立多账号托 管 ，严 格 隔 离
会话键格式 ：
模式: "main"
键格式: agent:<agentId>:<mainKey>
示例: agent:main:telegram:user123
模式: "per-channel-peer"
键格式: agent:<agentId>:<channel>:<peer>
示例: agent:main:telegram:direct:user123
模式: "per-account-channel-peer"
键格式: agent:<agentId>:<account>:<channel>:<peer>
示例: agent:main:biz:telegram:direct:user123
安全性对 比 ：

--- Page 168 ---

168┌─────────────────────────────────────────────────────────────┐
│  DM Session Isolation Levels                                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  main ( 低隔离 )                                              │
│  ┌─────────────────────────────────────────────┐           │
│  │  User A  ◄ ───── 同⼀个会话  ───── ►   User B   │           │
│  └─────────────────────────────────────────────┘           │
│                                                             │
│  per-channel-peer ( 中隔离 )                                  │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐     │
│  │ User A -    │    │ User B -    │    │ User C -    │     │
│  │ Session 1   │    │ Session 2   │    │ Session 3   │     │
│  └─────────────┘    └─────────────┘    └─────────────┘     │
│                                                             │
│  per-account-channel-peer ( ⾼隔离 )                          │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐           │
│  │Acc1-U1  │ │Acc1-U2  │ │Acc2-U1  │ │Acc2-U3  │           │
│  │Session1 │ │Session2 │ │Session3 │ │Session4 │           │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
配置建议 ：
个人使用："main" 保持对话 连续性
公共服务："per-channel-peer" 隔离不同用户
多账号企业 场 景："per-account-channel-peer" 实现严格隔离
4.4.5.3 群 组访问 控 制

--- Page 169 ---

169{
  channels: {
    discord: {
      groupPolicy: "allowlist",    // allowlist / denylist / allowall
      
      guilds: {
        "123456789012345678": {
          channels: {
            "222222222222222222": {
              allow: true,
              requireMention: true,  // 需要  @ 机器⼈
              allowedRoles: ["admin", "moderator"]
            }
          }
        }
      }
    }
  }
}
4.4.6 审计 日志
4.4.6.1 日志内 容
OpenClaw 记录以下安全相关 事件 ：
事件类型记录内容 存储位置
会话事件会话创建 、激活 、 关 闭 、 异 常 ~/.openclaw/agents/<id>/sessions/
工具调用工具名称 、 参数 、 结 果 、 执 行时间会话历史
消息事件发送 /接收 的 消息 元 数 据 （不 含 内 容 ）会话历史
配置变更配置文件 修改 、权 限 变 更 系统日志
安全事件确认操作 、权 限拒 绝 、 异 常 访 问审计日志
4.4.6.2 日志 格式

--- Page 170 ---

170{
  "timestamp": "2026-02-27T10:30:00Z",
  "level": "info",
  "event": "tool.execution",
  "agentId": "main",
  "sessionId": "sess_abc123",
  "tool": "exec",
  "params": {
    "command": "ls -la",
    "workdir": "/home/user/project"
  },
  "result": {
    "exitCode": 0,
    "duration": 150
  },
  "confirmation": {
    "required": false,
    "granted": null
  }
}
4.4.6.3 会话 历史 查 看
# 查看会话列表
openclaw sessions list
# 查看特定会话历史
openclaw sessions log <session-id>
# 导出会话为  JSONL
openclaw sessions export <session-id> --format jsonl
4.4.7 安全最佳实 践
4.4.7.1 配 置检 查清单

--- Page 171 ---

171## OpenClaw 安全配置检查清单
### 基础安全
- [ ] 启⽤沙盒模式  (`sandbox.enabled: true`)
- [ ] 配置  DM 配对或⽩名单  (`dmPolicy: "pairing"` 或  `"allowlist"`)
- [ ] 限制群组访问  (`groupPolicy: "allowlist"`)
- [ ] 禁⽤不需要的⼯具（如  `exec: { permission: "deny" }` ）
### 数据保护
- [ ] 使⽤只读  API 密钥
- [ ] 敏感配置使⽤环境变量⽽⾮硬编码
- [ ] 定期备份  `~/.openclaw/` ⽬录
- [ ] 加密存储认证信息
### 监控审计
- [ ] 启⽤详细⽇志记录
- [ ] 定期检查会话历史
- [ ] 监控异常⼯具调⽤模式
- [ ] 配置告警机制
### 更新维护
- [ ] 保持  OpenClaw 为最新版本
- [ ] 定期审查技能权限
- [ ] 检查依赖项安全更新
4.4.7.2 生产 环境 推 荐 配 置

--- Page 172 ---

172{
  // 安全沙盒
  sandbox: {
    enabled: true,
    mode: "limited",
    allowPaths: ["~/.openclaw/workspace"],
    denyPaths: ["/etc", "/usr", "/var", "~/.ssh"],
    network: "limited",
    exec: "sandboxed"
  },
  
  // ⼯具策略
  tools: {
    defaults: {
      permission: "allow",
      dangerousPermission: "confirm"
    },
    policy: {
      exec: { permission: "deny" },
      process: { permission: "deny" },
      write: {
        permission: "allow",
        options: { allowOutsideWorkspace: false }
      }
    }
  },
  
  // 通道安全
  channels: {
    telegram: {
      dmPolicy: "pairing"
    },
    discord: {
      groupPolicy: "allowlist",
      requireMention: true
    }
  },
  
  // 审计
  logging: {
    level: "info",
    audit: {
      enabled: true,
      retentionDays: 90
    }

--- Page 173 ---

173  }
}
4.5 本章小 结
本章深入 剖析了  OpenClaw 的 四 大 核 心 功 能系 统 ：
内存系统
文件即真相的设计理念 ，所 有 记 忆 以  Markdown 格 式 持 久 化
双层级架 构：每日日志（短 期 ） + MEMORY.md （长 期 ）
向量搜索支持语义检 索 ， 使 用 余 弦 相 似 度 计 算
QMD 后 端提供  BM25 + 向 量  + 重排 序 的 高 级 检 索 能力
自动压缩机制在上下文过长前 触 发 记 忆 刷 新
多代理系 统
完全隔离的 Agent 架 构 ， 每 个  Agent 拥 有 独 立 工作区 、 认证 和会话
确定性路由遵循最具体 匹 配优先 原 则
队列化执行确保会话 一 致性和 并 发安全
Agent-to-Agent 通信支持任务委托和工作 流编排
多平台多账户配置实现 一个  Gateway 托 管 多个号 码 / 机 器 人
技能系统
SKILL.md 标准格式 ， 结合  YAML Front Matter 和  Markdown
三级搜索路 径：工作区技能  →  全 局 技能  →  内 置 技能
ClawHub 市 场提供技能 的发现 、 安 装 和发 布
自动依赖检 查支持二进制 、 环境 变 量 和  Node 版本
自定义开发遵循规划 →实现 → 测 试 → 发 布 的 流程
安全与权 限
四层策略：全局  →  Agent →  工 具  →  提 供 商

--- Page 174 ---

174沙盒模式支持  limited/strict/none 三 级 隔 离
敏感操作 确 认机制保护危险操作
配对和白名 单控制  DM 访问
审计日志记录所有安全相关 事件
这些核心 功能 共同 构 成了  OpenClaw 强 大 而 灵 活 的 平 台 能力 ， 使 其 既 能 满 足 个人用户 的日 常 需 求 ，
也能支撑 企业 级 的 复 杂 应 用 场 景 。
参考来源
1. 官方文档
Memory System: https://docs.openclaw.ai/concepts/memory
Multi-Agent Routing: https://docs.openclaw.ai/concepts/multi-agent
Agent Loop: https://docs.openclaw.ai/concepts/agent-loop
Getting Started: https://docs.openclaw.ai/start/getting-started
2. GitHub 源码
技能系统 : https://github.com/openclaw/openclaw/tree/main/src/skills
内存实现 : https://github.com/openclaw/openclaw/tree/main/src/memory
多代理路由 : https://github.com/openclaw/openclaw/tree/main/src/agent
3. 技能市场
ClawHub: https://clawhub.com
4. 本地安装
内置技能 路径 : /opt/homebrew/lib/node_modules/openclaw/skills/
用户配置路径 : ~/.openclaw/openclaw.json

--- Page 175 ---

175第5章  进 阶 主题
本章深入探讨  OpenClaw 的 高 级 配 置 与 优 化技 术 。 当系 统 进入生产 环 境 或 需 要 支 撑 复 杂 业务 场 景
时，基础 配 置往往难 以 满 足需 求 。 本 章将 涵 盖 多 代 理系 统 的 高 级 配 置 策 略 、 性能 优 化技 术 、 调试 与 监 控
方案，以 及生产部 署 方法 ， 帮 助读 者 构 建 企 业 级 的  AI 代 理系 统 。
参考文档：本章内 容 基于  OpenClaw 官 方文 档 编 写
Gateway 配 置 参考
多代理概念 指 南
Cron Jobs
Sandboxing
5.1 多代理高 级 配 置
OpenClaw 的多 代 理系 统 允 许 在同 一  Gateway 下 运 行多个 独 立 的 代 理实 例 ， 每 个 代 理 拥 有 独 立 的
Workspace 、agentDir（状态目录）和会话 存 储 。 本 节介 绍 如 何设计 和 配 置复 杂 的 多 代 理 架 构 。
5.1.1 什么是 " 一个 代 理 "
在 OpenClaw 中，一 个代理是一个完全独 立 的 作用 域 ， 包 含 以下 组 成部分 ：
组件说明 存储路径
Workspace文件、
AGENTS.md/SOUL.md/USER.md 、
本地笔记 、人 格规 则~/.openclaw/workspace-<agentId>
AgentDir认证配置文 件 、 模 型 注 册 表 、 代 理 级 配
置~/.openclaw/agents/<agentId>/agent
Session
Store聊天记录和 路由状 态 ~/.openclaw/agents/<agentId>/sessions

--- Page 176 ---

176重要原则：agentDir 绝对不能在多个 代 理之间 复 用 ， 否 则 会 导 致 认证 和会话 冲 突 。
5.1.2 代理 配 置结 构
OpenClaw 使用  JSON5 格 式（ 支持 注 释 和 尾 随 逗 号）进行 配 置 ， 所 有 字 段均 为可 选 。
单代理模式（ 默 认 ）
如果不进行多 代理 配 置 ， OpenClaw 默 认运 行 单代 理 模 式 ：
agentId 默认为  main
会话键格式为  agent:main:<mainKey>
Workspace 默 认 为  ~/.openclaw/workspace
状态目录默 认为  ~/.openclaw/agents/main/agent
多代理配 置结 构

--- Page 177 ---

177{
  agents: {
    list: [
      {
        id: "home",
        default: true,
        name: "Home",
        workspace: "~/.openclaw/workspace-home",
        agentDir: "~/.openclaw/agents/home/agent"
      },
      {
        id: "work",
        name: "Work",
        workspace: "~/.openclaw/workspace-work",
        agentDir: "~/.openclaw/agents/work/agent"
      },
      {
        id: "dev",
        name: "Dev Assistant",
        workspace: "~/.openclaw/workspace-dev",
        agentDir: "~/.openclaw/agents/dev/agent",
        identity: {
          name: "DevBot",
          emoji: " 🤖 ",
          theme: "coding assistant"
        },
        groupChat: {
          mentionPatterns: ["@devbot", "@dev"]
        }
      }
    ]
  }
}
关键字段说明：

--- Page 178 ---

178字段 类型 必填说明
id string是 代理唯一 标 识 符
default boolean否是否为默 认代理 ， 路由 无 匹 配 时回 退 到 此代 理
name string否 代理显示名 称
workspace string否 代理工作区 路径
agentDir string是 代理状态目录 ，每个代理 必须独 立
identity object否 代理身份 设置（名 称 、 主题 、 emoji 、 头 像 ）
groupChat object否群聊配置 ，如提 及 模 式
使用命令行 创建代 理
# 使⽤向导添加新代理
openclaw agents add work
# 指定⼯作区路径
openclaw agents add work --workspace ~/.openclaw/workspace-work
# 列出所有代理
openclaw agents list
# 查看代理绑定关系
openclaw agents list --bindings
5.1.3 路由规则与 绑 定
路由规则决定了入站 消 息如 何 分 配 给 不同 的 代 理 。 OpenClaw 使 用  bindings 配置实现灵活 的 代
理路由。
绑定配置结 构

--- Page 179 ---

179{
  agents: {
    list: [
      { id: "home", workspace: "~/.openclaw/workspace-home", agentDir: 
"~/.openclaw/agents/home/agent" },
      { id: "work", workspace: "~/.openclaw/workspace-work", agentDir: 
"~/.openclaw/agents/work/agent" }
    ]
  },
  bindings: [
    { agentId: "home", match: { channel: "whatsapp", accountId: "personal" } },
    { agentId: "work", match: { channel: "whatsapp", accountId: "biz" } },
    { agentId: "home", match: { channel: "telegram", peer: { kind: "direct", id: 
"+15551234567" } } }
  ]
}
路由优先 级（ 从高到 低 ）
优先级 匹配类型 说明
1 peer 精确匹配 特定  DM/群 组 / 频 道  ID
2 parentPeer 匹配 线程继承 匹 配
3 guildId + roles Discord 角 色路由
4 guildId Discord 服务 器 匹 配
5 teamId Slack 团队 匹 配
6 accountId 匹配 特定账户 绑定
7 accountId: "*" 通道级匹 配（所 有 账 户）
8 default: true 的代理 默认代理 兜底
重要说明：
绑定省略  accountId 时，仅匹 配默 认账 户
使用  accountId: "*" 作为通道 级回退（所 有 账 户）
多个匹配 规则在同 一 层 级 时 ， 配 置 顺 序 中第一条生效
基于用户 的  DM 路由 （ 单 账 户多 代 理）

--- Page 180 ---

180可以在一个  WhatsApp 账 户下 ， 将 不同 的 私 信 路由 到不同 代 理 ：
{
  agents: {
    list: [
      { id: "alex", workspace: "~/.openclaw/workspace-alex", agentDir: 
"~/.openclaw/agents/alex/agent" },
      { id: "mia", workspace: "~/.openclaw/workspace-mia", agentDir: 
"~/.openclaw/agents/mia/agent" }
    ]
  },
  bindings: [
    {
      agentId: "alex",
      match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551230001" } }
    },
    {
      agentId: "mia",
      match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551230002" } }
    }
  ],
  channels: {
    whatsapp: {
      dmPolicy: "allowlist",
      allowFrom: ["+15551230001", "+15551230002"]
    }
  }
}
使用  CLI 管理 绑定
# 列出所有绑定
openclaw agents list --bindings
# JSON 格式输出
openclaw agents list --bindings --json
注意：绑定配 置 需 直接 编 辑  openclaw.json 文件， CLI 暂不提 供  bind/unbind 命 令 。
5.1.4 代理 身份与 群 聊 配 置
身份设置

--- Page 181 ---

181每个代理可以 配 置 独 立 的 身 份 信息 ：
{
  agents: {
    list: [
      {
        id: "main",
        identity: {
          name: "OpenClaw",
          theme: "space lobster",
          emoji: " 🦞 ",
          avatar: "avatars/openclaw.png"
        }
      }
    ]
  }
}
通过  CLI 设置身份 ：
# 从 IDENTITY.md ⽂件加载
openclaw agents set-identity --workspace ~/.openclaw/workspace --from-identity
# 显式设置字段
openclaw agents set-identity --agent main --name "OpenClaw" --emoji " 🦞 " --avatar 
avatars/openclaw.png
群聊提及 模式
{
  agents: {
    list: [
      {
        id: "family",
        groupChat: {
          mentionPatterns: ["@family", "@familybot"]
        }
      }
    ]
  }
}

--- Page 182 ---

1825.1.5 代理间通信 控 制
OpenClaw 支持 配 置代 理之间 的 工 具 调 用权 限 ：
{
  tools: {
    agentToAgent: {
      enabled: false,        // 是否启⽤代理间通信
      allow: ["home", "work"] // 允许通信的⽬标代理列表（当  enabled 为  true 时）
    }
  }
}
使用场景：
enabled: false：代理完全隔离 ， 无法相 互调 用
enabled: true + allow: [...]：仅允许向指定 代 理发 起 调 用
5.2 性能优化
性能优化是生产 环 境 部 署 的 核 心 考 量 。 OpenClaw 提 供 多 种 配 置选 项 来 优 化 延 迟 、 内 存 使 用和 并 发
处理能力 。
5.2.1 并发控制 配 置
OpenClaw 支持 配 置代 理和子 代 理 的 并 发数 ：
{
  agents: {
    defaults: {
      maxConcurrent: 1,       // 代理级最⼤并发数（默认： 1 ）
      subagents: {
        maxConcurrent: 1,     // ⼦代理级最⼤并发数（默认： 1 ）
        model: "minimax/MiniMax-M2.1",  // ⼦代理使⽤的模型
        runTimeoutSeconds: 900,         // ⼦代理运⾏超时（秒）
        archiveAfterMinutes: 60         // 归档时间（分钟）
      }
    }
  }
}

--- Page 183 ---

1835.2.2 模型 配 置 优 化
模型故障 转移
OpenClaw 支持多 模 型 提 供 商 配 置 ， 实现自动 故 障 转 移 ：
{
  models: {
    mode: "merge",
    providers: {
      "anthropic": {
        baseUrl: "https://api.anthropic.com",
        apiKey: "${ANTHROPIC_API_KEY}",
        api: "anthropic-messages",
        models: [
          { id: "claude-opus-4-6", maxTokens: 4096 }
        ]
      },
      "openai": {
        baseUrl: "https://api.openai.com/v1",
        apiKey: "${OPENAI_API_KEY}",
        api: "openai-chat",
        models: [
          { id: "gpt-4o", maxTokens: 4096 }
        ]
      }
    }
  },
  agents: {
    defaults: {
      model: {
        primary: "anthropic/claude-opus-4-6",
        fallbacks: ["openai/gpt-4o"]
      }
    }
  }
}
重要说明：
models.providers 是对象类型（ object） ， 键 为提 供 商  ID
代理的模 型 配 置在  agents.defaults.model，不在  models.defaults
使用新的 模 型  ID 格 式 ， 如  claude-opus-4-6
通道级模 型 覆 盖

--- Page 184 ---

184可以为特定通道 或 聊 天 设置 固 定 的 模 型 ：
{
  channels: {
    modelByChannel: {
      discord: {
        "123456789012345678": "anthropic/claude-opus-4-6"
      },
      slack: {
        C1234567890: "openai/gpt-4.1"
      },
      telegram: {
        "-1001234567890": "openai/gpt-4.1-mini",
        "-1001234567890:topic:99": "anthropic/claude-sonnet-4-6"
      }
    }
  }
}
5.2.3 会话压 缩与 清 理
OpenClaw 自动压 缩 会话 历 史 以 控 制上下文长度 ：
{
  agents: {
    defaults: {
      compaction: {
        mode: "safeguard",           // 压缩模式： "default" | "safeguard"
        reserveTokensFloor: 24000,   // 保留的最低  token 数
        memoryFlush: {
          enabled: true,
          softThresholdTokens: 6000,
          systemPrompt: "You are a memory management assistant...",
          prompt: "Summarize the following conversation..."
        }
      }
    }
  }
}
压缩策略：
mode: 压缩模式 ，"default" 为默认模式 ，"safeguard" 为安全模式
reserveTokensFloor: 会话保留 的最 低  token 数 量

--- Page 185 ---

185memoryFlush: 内存刷新 配 置 ， 用于在会话过长时生成 摘 要
enabled: 是否启用内 存刷 新
softThresholdTokens: 软阈值  token 数
systemPrompt: 系统提示词
prompt: 用户提示词 模板
5.2.4 上下文 剪 枝
OpenClaw 支持自动 剪 枝 旧 的 工 具结 果以 控 制上下文长度 ：
{
  agents: {
    defaults: {
      contextPruning: {
        enabled: true,               // 是否启⽤上下⽂剪枝
        maxToolResults: 20,          // 保留的最⼤⼯具结果数
        preserveRecent: 5            // 始终保留的最近结果数
      }
    }
  }
}
配置说明：
enabled: 启用上下文剪 枝 功 能
maxToolResults: 当工具结果 超过 此 数 量 时 触 发 剪 枝
preserveRecent: 始终保留 的最 近 工 具结 果数 量
5.2.5 消息 流式输 出
Telegram 等通道 支持流 式 响 应 ， 改 善 用户体 验 ：

--- Page 186 ---

186{
  channels: {
    telegram: {
      streaming: "partial",  // off | partial | block | progress
      // off: 关闭流式
      // partial: 流式预览（发送消息  + 编辑）
      // block: 分块发送
      // progress: 进度指示器
    }
  }
}
5.2.6 Cron 任务 优 化
Cron 执行 模式
{
  cron: {
    enabled: true,
    maxConcurrentRuns: 2,
    sessionRetention: "24h",     // 清理已完成的隔离运⾏会话
    runLog: {
      maxBytes: "2mb",           // 运⾏⽇志⼤⼩限制（⽀持字符串格式）
      keepLines: 2000            // 保留的⽇志⾏数（默认： 2000 ）
    }
  }
}
Cron 调度错 峰
OpenClaw 自动为 整 点 调 度表 达 式 添 加最多  5 分 钟 的 错 峰窗 口 ， 减 少 负 载 峰 值 ：

--- Page 187 ---

187{
  cron: {
    jobs: [
      {
        jobId: "hourly-task",
        schedule: {
          kind: "cron",
          cron: "0 * * * *",      // 每⼩时执⾏
          staggerMs: 0            // --exact 强制精确时间
        }
      }
    ]
  }
}
Cron 调度错 峰
OpenClaw 自动为 整 点 调 度表 达 式 添 加最多  5 分 钟 的 错 峰窗 口 ， 减 少 负 载 峰 值 ：
{
  cron: {
    jobs: [
      {
        jobId: "hourly-task",
        schedule: {
          kind: "cron",
          cron: "0 * * * *",      // 每⼩时执⾏
          staggerMs: 0            // --exact 强制精确时间
        }
      }
    ]
  }
}
5.3 调试与 监 控
完善的调试和监控 体系是 保 障 系 统 稳 定 运 行 的 基 础 。
5.3.1 日志系 统
OpenClaw 提 供详 细 的日 志 记 录 功 能 ， 支持 通过  CLI 查 看 。
查看日志命令

--- Page 188 ---

188# 查看最近⽇志
openclaw logs
# 实时跟踪⽇志
openclaw logs --follow
# JSON 格式输出
openclaw logs --json
# 限制输出⾏数
openclaw logs --limit 500
# 本地时区时间戳
openclaw logs --local-time
# 组合使⽤
openclaw logs --follow --local-time
Gateway 日志 级别
启动  Gateway 时 指 定 日 志 级别 ：
# 调试模式启动
openclaw gateway --log-level debug
# 或使⽤环境变量
DEBUG=openclaw:* openclaw gateway
# 特定模块调试
DEBUG=openclaw:agent,openclaw:tools openclaw gateway
5.3.2 诊断命令
doctor 命令

--- Page 189 ---

189# 运⾏完整系统诊断
openclaw doctor
# 深度扫描（检查所有组件）
openclaw doctor --deep
# ⾃动修复问题
openclaw doctor --repair
openclaw doctor --fix
# 其他常⽤选项
openclaw doctor --force              # 强制修复
openclaw doctor --yes                # ⾃动确认
openclaw doctor --non-interactive    # ⾮交互模式
Gateway 状 态管 理
# 查看 Gateway 运⾏状态
openclaw gateway status
# 启动 Gateway
openclaw gateway start
# 停⽌ Gateway
openclaw gateway stop
# 重启 Gateway
openclaw gateway restart
通道状态检 查
# 检查所有通道状态
openclaw channels status
# 探针测试通道连接
openclaw channels status --probe

--- Page 190 ---

1905.3.3 技能 管理
# 列出已安装技能
openclaw skills list
# 显示符合条件的技能（满⾜依赖）
openclaw skills list --eligible
# 查看技能详情
openclaw skills info coding-agent
# 检查技能更新
openclaw skills check
5.3.4 会话 管理
# 列出活跃会话（默认显示最近活跃的会话）
openclaw sessions
# 查看所有代理的会话
openclaw sessions --all-agents
# 按代理筛选
openclaw sessions --agent main
# 显示指定时间内活跃的会话（分钟）
openclaw sessions --active 30
# JSON 格式输出
openclaw sessions --json
# 清理已完成 / 过期会话
openclaw sessions cleanup
5.4 沙箱与安全 配 置
OpenClaw 支持通过  Docker 容 器 运 行工 具 ， 限 制 执 行 环 境 的 影 响范围 。

--- Page 191 ---

1915.4.1 沙箱模式
{
  agents: {
    defaults: {
      sandbox: {
        mode: "non-main",    // off | non-main | all
        scope: "session",    // session | agent | shared
        prune: {             // 沙箱⾃动清理配置
          idleHours: 24,     // 空闲多少⼩时后清理
          maxAgeDays: 7      // 最⼤保留天数
        }
      }
    }
  }
}
模式说明：
模式 说明
off 不使用沙 箱 ，所 有 工 具 在主机上 运 行
non-main 仅对非主会话 使用 沙 箱 （推 荐 ）
all 所有会话 都在沙 箱 中 运 行
作用域说明：
作用域 说明
session 每个会话 一个 容 器 （ 默 认 ）
agent 每个代理 一个 容 器
shared 所有沙箱化会话 共享 一 个 容 器

--- Page 192 ---

1925.4.2 工作区访问 控 制
{
  agents: {
    defaults: {
      sandbox: {
        workspaceAccess: "none"  // none | ro | rw
      }
    }
  }
}
模式说明
none沙箱使用独 立工作区（~/.openclaw/sandboxes）
ro以只读方式 挂 载代 理工作区到  /agent
rw以读写方式 挂 载代 理工作区到  /workspace
5.4.3 自定义 挂 载
{
  agents: {
    defaults: {
      sandbox: {
        docker: {
          binds: ["/home/user/source:/source:ro", "/var/data/myapp:/data:ro"]
        }
      }
    },
    list: [
      {
        id: "build",
        sandbox: {
          docker: {
            binds: ["/mnt/cache:/cache:rw"]
          }
        }
      }
    ]
  }
}

--- Page 193 ---

1935.4.4 沙箱浏 览器
{
  agents: {
    defaults: {
      sandbox: {
        browser: {
          enabled: false,              // 是否启⽤沙箱浏览器（默认： false ）
          autoStart: true,             // ⾃动启动浏览器
          autoStartTimeoutMs: 12000,   // 启动超时（默认： 12000ms ）
          network: "openclaw-sandbox-browser",
          allowHostControl: false,
          cdpPort: 9222,               // Chrome DevTools Protocol 端⼝
          cdpSourceRange: "172.21.0.1/32",
          vncPort: 5900,               // VNC 端⼝
          noVncPort: 6080,             // noVNC Web 端⼝
          headless: false,             // 是否⽆头模式
          enableNoVnc: true            // 是否启⽤  noVNC
        }
      }
    }
  }
}
5.5 生产环 境部 署
5.5.1 环境 配 置分 离
建议区分开发 、测 试 和生产 环 境 ：
# 使⽤不同配置⽂件
openclaw gateway --config ~/.openclaw/config/production.json
# 或使⽤环境变量
OPENCLAW_PROFILE=production openclaw gateway
配置目录 结 构 示例 ：

--- Page 194 ---

194~/.openclaw/
├── config/
│   ├── development.json
│   ├── staging.json
│   └── production.json
└── agents/
    ├── home/agent/
    ├── work/agent/
    └── dev/agent/
5.5.2 Gateway 安全 配 置
{
  gateway: {
    port: 18789,
    mode: "local",
    bind: "loopback",     // loopback | all
    auth: {
      mode: "token",      // token | none
      token: "${GATEWAY_TOKEN}"
    },
    tailscale: {
      mode: "off",        // off | client | server
      resetOnExit: false
    }
  }
}
5.5.3 通道安全 配 置
DM 和群 组访问策 略
所有通道 支持  DM 策 略 和 群 组 策 略 配 置 ：
DM 策略：

--- Page 195 ---

195策略 行为
pairing (默认 ) 未知发送者 获 得 一 次性 配 对 码 ， 需 所 有 者 批 准
allowlist 仅允许  allowFrom 中的发送者
open 允许所有入站  DM （ 需  allowFrom: ["*"]）
disabled 忽略所有入站  DM
群组策略：
策略 行为
allowlist (默认 ) 仅允许匹 配配 置 的 群 组
open 绕过群组白名 单（提 及限 制 仍 适 用）
disabled 阻止所有群 组 / 房间 消 息
Telegram 安全 配 置示 例
{
  channels: {
    telegram: {
      enabled: true,
      botToken: "${TELEGRAM_BOT_TOKEN}",
      dmPolicy: "pairing",
      allowFrom: ["tg:123456789"],
      groups: {
        "*": { requireMention: true },
        "-1001234567890": {
          allowFrom: ["@admin"],
          systemPrompt: "Keep answers brief."
        }
      },
      configWrites: false  // 阻⽌  Telegram 发起的配置写⼊
    }
  }
}
WhatsApp 安全 配 置示 例

--- Page 196 ---

196{
  channels: {
    whatsapp: {
      dmPolicy: "pairing",
      allowFrom: ["+15555550123", "+447700900123"],
      groups: {
        "*": { requireMention: true }
      },
      groupPolicy: "allowlist",
      groupAllowFrom: ["+15551234567"],
      sendReadReceipts: true
    }
  }
}
5.5.4 备份与 恢 复
配置备份
# 备份配置⽬录
tar -czf openclaw-config-backup.tar.gz ~/.openclaw/config/
# 备份代理状态
tar -czf openclaw-agents-backup.tar.gz ~/.openclaw/agents/
# 完整备份（排除⽇志和缓存）
tar -czf openclaw-full-backup.tar.gz ~/.openclaw/ \
  --exclude='*.log' \
  --exclude='cache/' \
  --exclude='logs/'
数据恢复
# 恢复配置
tar -xzf openclaw-config-backup.tar.gz -C /
# 完整恢复
tar -xzf openclaw-full-backup.tar.gz -C /
建议：定期将备份文 件 同 步 到 云存 储 或 版本 控 制系 统 。

--- Page 197 ---

1975.5.5 Cron 任务 配 置
添加定时 任务
# ⼀次性提醒任务
openclaw cron add \
  --name "Reminder" \
  --at "2026-03-01T09:00:00Z" \
  --session main \
  --system-event " 提醒：检查今⽇待办事项 " \
  --wake now \
  --delete-after-run
# 周期性任务（ Main 会话）
openclaw cron add \
  --name "health-check" \
  --schedule "*/5 * * * *" \
  --session main \
  --system-event " 执⾏系统健康检查 "
# 隔离任务（独⽴会话，带通知）
openclaw cron add \
  --name "daily-report" \
  --schedule "0 9 * * *" \
  --tz "Asia/Shanghai" \
  --session isolated \
  --message " ⽣成昨⽇⼯作总结报告 " \
  --announce \
  --channel telegram \
  --to "123456789"
# 每周报告
openclaw cron add \
  --name "weekly-report" \
  --schedule "0 10 * * 1" \
  --session isolated \
  --message " ⽣成本周⼯作报告 " \
  --announce
管理定时 任务

--- Page 198 ---

198# 列出所有任务
openclaw cron list
# 查看任务运⾏历史
openclaw cron runs
openclaw cron runs --id <job-id>
# 禁⽤/ 启⽤任务
openclaw cron disable <job-id>
openclaw cron enable <job-id>
# 编辑任务
openclaw cron edit <job-id> --announce --channel telegram --to "123456789"
# ⽴即运⾏任务
openclaw cron run <job-id>
# 删除任务
openclaw cron rm <job-id>
Cron 任务 配 置 参 数

--- Page 199 ---

199参数 说明
--name 任务名称
--schedule Cron 表达式（ 5 字 段 或 6 字 段 ）
--at 一次性执行时间（ ISO 8601 ）
--tz 时区（ IANA 格式 ， 如  Asia/Shanghai ）
--session 执行模式 ：main 或 isolated
--message 代理消息（ isolated 模 式）
--system-event 系统事件（ main 模 式）
--announce 通知模式（ isolated 默 认 ）
--no-deliver 不发送通知
--channel 通知通道
--to 通知目标
--wake 唤醒模式 ：now 或 next-heartbeat
--delete-after-run 运行后删 除（ 一次性 任 务）
--exact 精确时间（无错 峰 ）
--stagger 错峰窗口（如  30s, 1m, 5m ）
本章小结
本章系统介 绍了  OpenClaw 的 进 阶 主题 ， 涵 盖 以下 五 个 核 心 领 域 ：
多代理高 级 配 置：每个代理拥 有独 立 的  Workspace 、agentDir 和会话存储 。通过  agents.list
配置多代理 ，bindings 配置路由规则 。 路由 优先 级从  peer 精确匹配到默 认代 理回 退 。agentDir
绝不能在 代理间 复 用 。

--- Page 200 ---

200性能优化：通过  maxConcurrent 控制并发数 ， 通过  compaction 配置会话压缩 和
memoryFlush ， 通过  contextPruning 配置上下文剪 枝 ， 通过  modelByChannel 实现通道 级 模 型 覆
盖。 Cron 任务 支持 错 峰 调 度以 减 少 负 载 峰 值 。
调试与监控：使用  openclaw logs 查看日志（ 支持  --follow、--json、--limit、--
local-time 等选项） ，openclaw doctor 运行诊断 ，openclaw gateway status 检查  Gateway 状
态。openclaw skills 管理技能 ，openclaw sessions 管理会话 。
沙箱与安全：通过  sandbox.mode 和 sandbox.scope 配置容器化执行 环 境 。 支持 工作区 访 问 控 制
和自定义挂 载 。生产 环 境 应 配 置 适 当 的  DM 和 群 组 访 问 策 略 。
生产环境部 署：使用环境分离 、 安全 配 置 、 备 份 恢 复 策 略 和  Cron 任 务 管 理 ， 构 建 稳 定可 靠 的
OpenClaw 生产 环 境 。
参考资源
官方文档
Gateway 配 置 参考
多代理路由
Cron Jobs
Sandboxing
CLI 命令 参考
Channel 配 置
GitHub 项 目
OpenClaw 主仓 库
Issue 讨论
版本说明
本章内容适用于  OpenClaw 2026.2.x 及更高版本 。 配 置 基 于  JSON5 格 式（ 支持 注 释 和 尾 随 逗
号）。所 有 配 置字 段均 为可 选 ， OpenClaw 使 用安全 的 默 认 值 。

--- Page 201 ---

201最后更新 : 2026-02-28 （ 基 于  OpenClaw 2026.2.23 官 方 配 置 ）

--- Page 202 ---

202第6章  实 践 指 南
本章概要
本章是《 OpenClaw 完 全 指 南 》 的 实 践 篇 ， 提 供 从 零 开 始 部 署 、 配 置 和 使 用  OpenClaw 的 完 整指
导。无论您是初次接 触 的新 用户 ， 还是 希 望 深 入 优 化 配 置 的 高 级 用户 ， 本 章都将 为您提 供 详尽 的 操 作 步
骤、配置说明和实 战 经 验 。
学习目标 ：
掌握  OpenClaw 的 安 装 部 署 方法
理解  openclaw.json 配 置 体系
学会配置主 流通 讯 平 台 的 通道 集 成
了解典型应用 场 景 的 完 整 实现
具备独立排查和 解 决 问题 的 能力
6.1 安装指 南
6.1.1 系统要 求
6.1.1.1 硬 件要 求
OpenClaw 的硬 件 需 求取 决 于您 的 使 用 场 景 和 预 期 负 载 。 以下是 基 于不同 场 景 的 配 置建议 ：
使用场景 CPU内存 存储 网络适用对象
个人轻量使用 2核+ 4GB+ 10GB SSD 稳定宽带个人用户 、开发者体 验
日常使用 4核+ 8GB+ 20GB SSD 50Mbps+个人主力 助手
多通道部 署 4核+ 16GB+ 50GB SSD 100Mbps+ 团队使用
详细说明 ：
CPU 要求：
基础运行仅 需 支持  x86_64 或  ARM64 架 构 的 现 代 处 理 器

--- Page 203 ---

203多通道场 景下 ， CPU 核 心数 直 接 影 响 并 发 处 理能力
内存要求：
网关进程本 身占用 约  200-500MB 内 存
每个活跃会话 约占 用  50-100MB 内 存
本地  LLM 运行 需 要 额 外  4-16GB （ 取 决 于 模 型 大小）
存储要求：
系统安装 ： 约  500MB （ 含  Node.js 运 行时）
依赖缓存 ： 约  1-2GB （ npm 包 缓 存 ）
日志存储 ： 建议预 留  5GB+
6.1.1.2 软 件要 求
操作系统支持 矩 阵 ：
操作系统 支持版本 安装方式 推荐程度
macOS 13+ (Ventura)安装脚本 /npm ★★★★★
Ubuntu 22.04 LTS+ 安装脚本 /npm ★★★★★
Debian 11+ 安装脚本 /npm ★★★★ ☆
CentOS/RHEL 8+ 安装脚本 /npm ★★★★ ☆
Fedora 38+ 安装脚本 /npm ★★★★ ☆
Arch Linux Rolling npm ★★★☆☆
Windows 10/11 (WSL2)安装脚本 /npm ★★★☆☆
⚠ Windows 用户注意 ： Windows 必须通过  WSL2 运 行（ strongly recommended ） 。
必需软件依 赖 ：

--- Page 204 ---

204# Node.js 运⾏时（官⽅要求  Node 22+ ）
Node.js >= 22.0.0
# 包管理器
npm >= 9.0.0 或  pnpm >= 8.0.0
# Git（⽤于扩展安装）
Git >= 2.30.0
6.1.2 安装  OpenClaw
方式一： 官方安 装 脚 本（推 荐 ）
# macOS/Linux
curl -fsSL https://openclaw.ai/install.sh | bash
# Windows (PowerShell)
iwr -useb https://openclaw.ai/install.ps1 | iex
方式二： npm 全 局 安 装
# 全局安装  OpenClaw
npm install -g openclaw@latest
# 验证安装
openclaw --version
使用  pnpm（ 磁盘 效 率 更高） ：
# 安装 pnpm （如未安装）
npm install -g pnpm
# 使⽤ pnpm 安装
pnpm add -g openclaw
6.1.3 初始化 配 置
安装完成后 ， 运行 初 始 化 向 导 ：

--- Page 205 ---

205# 启动配置向导并安装系统服务
openclaw onboard --install-daemon
# 或仅运⾏向导（不安装服务）
openclaw onboard
初始化向 导将 ：
1. 创建  ~/.openclaw/ 配置目录
2. 生成默认 的  openclaw.json 配置文件
3. 配置  LLM 提 供 商 （推 荐  Anthropic ）
4. 安装系统服务（ 使 用  --install-daemon 时）
6.1.4 首次启动
启动  Gateway ：
# 默认启动（端⼝  18789 ）
openclaw gateway
# 指定端⼝启动
openclaw gateway --port 18789
# 查看⽹关状态
openclaw gateway status
验证启动 ：
# 检查⽹关状态
openclaw gateway status
# 查看健康状态
openclaw gateway health --url ws://127.0.0.1:18789
# 打开控制⾯板
openclaw dashboard

--- Page 206 ---

2066.2 配置详 解
6.2.1 配置文 件结 构
OpenClaw 的主 配 置 文 件 位于  ~/.openclaw/openclaw.json。以下是 官方推 荐 的 完 整配 置格 式 ：

--- Page 207 ---

207{
  // Agent 配置
  agents: {
    defaults: {
      workspace: "~/.openclaw/workspace",
      model: {
        primary: "anthropic/claude-sonnet-4-5",
        fallbacks: ["openai/gpt-5.2"],
      },
      models: {
        "anthropic/claude-sonnet-4-5": { alias: "Sonnet" },
        "openai/gpt-5.2": { alias: "GPT" },
      },
    },
    list: [
      {
        id: "main",
        groupChat: {
          mentionPatterns: ["@openclaw"],
        },
      },
    ],
  },
  
  // 通道配置
  channels: {
    whatsapp: {
      enabled: true,
      dmPolicy: "pairing",
      allowFrom: ["+15551234567"],
    },
    telegram: {
      enabled: true,
      botToken: "123:abc",
      dmPolicy: "pairing",
    },
    discord: {
      enabled: true,
      token: "${DISCORD_BOT_TOKEN}",
    },
  },
  
  // 会话配置
  session: {
    dmScope: "per-channel-peer",
    threadBindings: {
      enabled: true,

--- Page 208 ---

208      idleHours: 24,
      maxAgeHours: 0,
    },
    reset: {
      mode: "daily",
      atHour: 4,
      idleMinutes: 120,
    },
  },
  
  // Cron 作业配置
  cron: {
    enabled: true,
    maxConcurrentRuns: 2,
    sessionRetention: "24h",
  },
  
  // Webhook 配置
  hooks: {
    enabled: true,
    token: "shared-secret",
    path: "/hooks",
  },
  
  // 多代理路由配置
  bindings: [
    {
      agentId: "main",
      match: {
        channel: "whatsapp",
      },
    },
  ],
}
关键配置块说明 ：
agents.defaults - 默认  Agent 设置 ， 包 含 模 型 配 置
agents.defaults.models - 模型目录 ，定义 可用 模 型及别 名 ， 用于  /model 命令切换
agents.list - Agent 列表 ，可 配 置 多个  Agent
channels - 各通讯通道 的 配 置
session - 会话相关 设置 ， 包 含  threadBindings 和  reset 配 置
cron - 定时任务（ Cron 作业） 配 置

--- Page 209 ---

209hooks - Webhook 配 置 ， 用于外部系 统集 成
bindings - 多代理 路由 配 置 ， 实现不同通道 绑 定不同  Agent
6.2.2 核心 配 置 项
6.2.2.1 Agent 配 置
模型配置（agents.defaults.model + agents.defaults.models）：
{
  agents: {
    defaults: {
      model: {
        primary: "anthropic/claude-sonnet-4-5",
        fallbacks: ["openai/gpt-5.2", "openai/gpt-4.1"],
      },
      models: {
        "anthropic/claude-sonnet-4-5": { alias: "Sonnet" },
        "openai/gpt-5.2": { alias: "GPT" },
        "openai/gpt-4.1": { alias: "GPT-4.1" },
      },
    },
  },
}
说明：
model.primary - 主模型 ，对话默 认使 用
model.fallbacks - 备用模 型 列表 ， 主 模 型 不可用时自动 切 换
models - 模型目录 ，定义 所 有 可用 模 型及 其 别 名 ， 用户可通过  /model 命令在对话 中切 换
多 Agent 配 置 ：

--- Page 210 ---

210{
  agents: {
    defaults: {
      workspace: "~/.openclaw/workspace",
      model: {
        primary: "anthropic/claude-sonnet-4-5",
      },
    },
    list: [
      {
        id: "main",
        groupChat: {
          mentionPatterns: ["@openclaw", "@ 助⼿ "],
        },
      },
      {
        id: "coding-agent",
        workspace: "/home/user/coding-workspace",
        model: {
          primary: "openai/gpt-5.2",
        },
      },
    ],
  },
}
6.2.2.2 消息 配 置
{
  agents: {
    list: [
      {
        id: "main",
        groupChat: {
          // 触发响应的 @ 模式
          mentionPatterns: ["@openclaw", "@ 助⼿ "],
        },
      },
    ],
  },
}
6.2.2.3 会话 配 置 （ session ）

--- Page 211 ---

211{
  session: {
    // DM 会话范围： per-channel-peer | per-peer | global
    dmScope: "per-channel-peer",
    
    // 线程绑定配置（ Discord ⽀持  /focus 、 /unfocus 等命令）
    threadBindings: {
      enabled: true,
      idleHours: 24,
      maxAgeHours: 0,
    },
    
    // 会话重置配置
    reset: {
      mode: "daily",        // daily | idle | off
      atHour: 4,            // daily 模式下每天⼏点重置
      idleMinutes: 120,     // idle 模式下空闲多少分钟后重置
    },
  },
}
session.reset 说明 ：
模式 说明
daily 每天在指定时间 重置 会话（ 配 合  atHour）
idle 空闲指定时间后 重置 （ 配 合  idleMinutes）
off 禁用自动 重置
6.2.2.4 Cron 作业 配 置
{
  cron: {
    enabled: true,
    maxConcurrentRuns: 2,
    sessionRetention: "24h",
    runLog: {
      maxBytes: "2mb",
      keepLines: 2000,
    },
  },
}

--- Page 212 ---

212说明：
enabled - 启用  Cron 作业
maxConcurrentRuns - 最大并发 运行数
sessionRetention - 已完成 运行会话 的 保 留 时间
runLog - 运行日志 的 存储 限 制
6.2.2.5 Webhook 配 置 （ hooks ）
{
  hooks: {
    enabled: true,
    token: "shared-secret",
    path: "/hooks",
    defaultSessionKey: "hook:ingress",
    allowRequestSessionKey: false,
    allowedSessionKeyPrefixes: ["hook:"],
    mappings: [
      {
        match: { path: "gmail" },
        action: "agent",
        agentId: "main",
        deliver: true,
      },
    ],
  },
}
6.2.2.6 多 代理 路由 配 置 （ bindings ）

--- Page 213 ---

213{
  agents: {
    list: [
      { id: "home", default: true, workspace: "~/.openclaw/workspace-home" },
      { id: "work", workspace: "~/.openclaw/workspace-work" },
    ],
  },
  bindings: [
    {
      agentId: "home",
      match: {
        channel: "whatsapp",
        accountId: "personal",
      },
    },
    {
      agentId: "work",
      match: {
        channel: "whatsapp",
        accountId: "biz",
      },
    },
    {
      agentId: "work",
      match: {
        channel: "feishu",
        peer: { kind: "group", id: "oc_xxx" },
      },
    },
  ],
}
bindings 路由字 段 说明 ：
字段 说明
agentId 目标  Agent ID
match.channel通道名称（ whatsapp 、 telegram 、 discord 、 feishu 等）
match.accountId账号  ID（多账号时 使 用）
match.peer.kind会话类型 ：direct（私聊） 或  group（群组）
match.peer.id用户  ID（ ou_xxx ） 或 群 组  ID （ oc_xxx ）

--- Page 214 ---

2146.2.3 环境 变 量
OpenClaw 支持通过多 种 方式 配 置 环 境 变 量 ：
6.2.3.1 .env 文 件
OpenClaw 自动加 载 以下位 置 的  .env 文件：
当前工作 目录 的  .env 文件
~/.openclaw/.env 全局配置文 件
# 创建 ~/.openclaw/.env ⽂件
cat > ~/.openclaw/.env <<EOF
# LLM API 密钥
ANTHROPIC_API_KEY=sk-ant-xxxxxxxx
OPENAI_API_KEY=sk-xxxxxxxx
# 通道 Token
TELEGRAM_BOT_TOKEN=123:abc
DISCORD_BOT_TOKEN=xxx
FEISHU_APP_ID=cli_xxx
FEISHU_APP_SECRET=xxx
# OpenClaw 配置
OPENCLAW_HOME="~/.openclaw"
OPENCLAW_STATE_DIR="/var/openclaw"
OPENCLAW_CONFIG_PATH="/etc/openclaw.json"
EOF
# OpenClaw 会⾃动加载  ~/.openclaw/.env
6.2.3.2 环境 变 量 引 用
在配置文 件 中可以 使 用  ${VAR_NAME} 语法引用 环境 变 量 ：

--- Page 215 ---

215{
  channels: {
    telegram: {
      botToken: "${TELEGRAM_BOT_TOKEN}",
    },
    discord: {
      token: "${DISCORD_BOT_TOKEN}",
    },
    feishu: {
      accounts: {
        main: {
          appId: "${FEISHU_APP_ID}",
          appSecret: "${FEISHU_APP_SECRET}",
        },
      },
    },
  },
  gateway: {
    auth: {
      token: "${OPENCLAW_GATEWAY_TOKEN}",
    },
  },
}
规则：
仅匹配大写名 称 ：[A-Z_][A-Z0-9_]*
缺失或空 值会在加 载 时报 错
使用  $__SHELL_VAR_1__ 可输出字面 量  ${VAR}
支持在  $include 文件中使用
6.2.3.3 内联 环境 变 量 （ env.vars ）
{
  env: {
    vars: {
      OPENROUTER_API_KEY: "sk-or-...",
      GROQ_API_KEY: "gsk-...",
    },
  },
}
6.2.3.4 SecretRef 配 置

--- Page 216 ---

216对于支持  SecretRef 的 字 段 ， 可以 使 用以下方式 引 用 敏 感 信息 ：
{
  models: {
    providers: {
      openai: {
        apiKey: {
          source: "env",
          provider: "default",
          id: "OPENAI_API_KEY",
        },
      },
    },
  },
  skills: {
    entries: {
      "nano-banana-pro": {
        apiKey: {
          source: "file",
          provider: "filemain",
          id: "/skills/entries/nano-banana-pro/apiKey",
        },
      },
    },
  },
  channels: {
    googlechat: {
      serviceAccountRef: {
        source: "exec",
        provider: "vault",
        id: "channels/googlechat/serviceAccount",
      },
    },
  },
}
SecretRef 来 源类 型 ：
类型 说明
env 从环境变 量读取
file 从文件读取
exec 从命令执行 结果 读取

--- Page 217 ---

2176.2.3.5 Shell 环境 导 入
{
  env: {
    shellEnv: {
      enabled: true,
      timeoutMs: 15000,
    },
  },
}
或环境变 量 ：OPENCLAW_LOAD_SHELL_ENV=1
6.2.4 通道 配 置实 战
6.2.4.1 WhatsApp 配 置
配对  WhatsApp ：
# 扫描⼆维码配对
openclaw channels login --channel whatsapp
# 或交互式选择
openclaw channels login
配置示例 ：
{
  channels: {
    whatsapp: {
      enabled: true,
      dmPolicy: "pairing",      // 必需字段
      allowFrom: ["+8613800138000"],  // 仅允许特定号码
      groupPolicy: "allowlist", // allowlist | open | disabled
      groupAllowFrom: ["+8613800138000"],
    },
  },
}
dmPolicy 说明 ：

--- Page 218 ---

218值 行为
"pairing" 默认。未知用户 获 得 配 对 码 ， 需 批 准 后 聊 天
"allowlist" 仅 allowFrom 中的 用户可以 聊 天
"open" 允许所有用户（ 需 在  allowFrom 中 设置  "*"）
"disabled" 禁用私信
6.2.4.2 Telegram 配 置
创建  Bot ：
1. 在 Telegram 搜索  @BotFather
2. 发送  /newbot 命令
3. 按提示设置  Bot 名 称 和用户名
4. 保存返回 的  Bot Token
配置示例 ：
{
  channels: {
    telegram: {
      enabled: true,
      botToken: "${TELEGRAM_BOT_TOKEN}",  // 或环境变量  TELEGRAM_BOT_TOKEN
      dmPolicy: "pairing",   // pairing | allowlist | open | disabled
      allowFrom: ["tg:123"], // 必须是数字⽤户 ID ，不⽀持  @username
      groups: {
        "-1001234567890": {
          groupPolicy: "open",
          requireMention: true,
        },
      },
    },
  },
}
⚠ 注意：allowFrom 必须填写数字用户 ID（格式  tg:123），不支持  @username。
6.2.4.3 Discord 配 置
创建应用 ：
1. 访问  https://discord.com/developers/applications

--- Page 219 ---

2192. 点击  "New Application" ， 命 名 并创建
3. 在 "Bot" 页面 点 击  "Add Bot"
4. 重置并保 存  Token
配置示例 ：
{
  channels: {
    discord: {
      enabled: true,
      token: "${DISCORD_BOT_TOKEN}",
      dmPolicy: "pairing",
      groupPolicy: "allowlist",
      guilds: {
        "YOUR_SERVER_ID": {
          requireMention: true,
          users: ["YOUR_USER_ID"],
        },
      },
    },
  },
}
关键字段 ：
token - Bot Token
guilds - 服务器配 置 ， 支持  requireMention 和 users
6.2.4.4 飞 书（ Feishu ） 配 置
飞书是企业 协作平 台 ， OpenClaw 通过  WebSocket 长 连 接接收 消 息 ， 无 需 暴 露 公 网  Webhook
URL。
Step 1: 安 装飞 书 插 件
openclaw plugins install @openclaw/feishu
Step 2: 创建飞 书 应 用
1. 访问  飞书开放平 台 并登录
国际版  Lark 用户 访 问  https://open.larksuite.com/app
需要在配 置 中 设置  domain: "lark"

--- Page 220 ---

2202. 点击  创建企业自 建应用，填写应用名 称和 描述
3. 在 凭证与基 础信息 中复制：
App ID（格式：cli_xxx）
App Secret
4. 配置权限（关键步 骤） ：
进入  权限管理，点击  批量导入，粘贴以下内 容 ：
   {
     "scopes": {
       "tenant": [
         "aily:file:read",
         "aily:file:write",
         "application:application.app_message_stats.overview:readonly",
         "application:application:self_manage",
         "application:bot.menu:write",
         "contact:user.employee_id:readonly",
         "corehr:file:download",
         "event:ip_list",
         "im:chat.access_event.bot_p2p_chat:read",
         "im:chat.members:bot_access",
         "im:message",
         "im:message.group_at_msg:readonly",
         "im:message.p2p_msg:readonly",
         "im:message:readonly",
         "im:message:send_as_bot",
         "im:resource"
       ],
       "user": [
         "aily:file:read",
         "aily:file:write",
         "im:chat.access_event.bot_p2p_chat:read"
       ]
     }
   }
核心权限说明 ：

--- Page 221 ---

221权限 说明
aily:file:read / aily:file:write Aily 文件读写（ AI 功 能）
im:message 消息权限（核心权 限 ）
im:message:readonly 读取消息
im:message:send_as_bot 以机器人 身份发 送 消 息
im:chat.access_event.bot_p2p_chat:read 私聊访问 事件
im:chat.members:bot_access 访问群成 员信息
application:application:self_manage 应用自管理
contact:user.employee_id:readonly 读取用户 员工号
5. 开启机器人能力：
进入  应用能力 > 机器人，启用机 器人能力 并设置 名 称
6. 配置事件订 阅：
进入  事件订阅：
选择  使用长连接接收 事件（WebSocket 模 式）
添加事件 ：im.message.receive_v1
⚠ 注意： 配置事件订 阅前 ， 确 保 ：
已运行  openclaw channels add 添加飞书通道
Gateway 正在 运行（openclaw gateway status）
7. 发布应用：
在 版本管理与发 布 中创建版本 并提 交 审 核 ， 等 待 管 理 员 批 准
Step 3: 配 置  openclaw.json

--- Page 222 ---

222{
  channels: {
    feishu: {
      enabled: true,
      dmPolicy: "pairing",
      // domain: "lark",  // 国际版  Lark ⽤户取消注释此⾏
      connectionMode: "websocket",  // websocket | webhook
      accounts: {
        main: {
          appId: "cli_xxxxxxxxxxxx",
          appSecret: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
          botName: "AI 助⼿ ",
        },
      },
      // 群组配置
      groupPolicy: "open",
      groups: {
        "oc_xxxxxxxxxxxxxxxx": {
          requireMention: true,
        },
      },
      // ⾼级配置
      streaming: true,          // 启⽤流式卡⽚输出
      blockStreaming: true,     // 启⽤块级流式
      textChunkLimit: 2000,     // 消息分块⼤⼩
      mediaMaxMb: 30,           // 媒体⼤⼩限制
    },
  },
}
或使用环境 变 量 ：
export FEISHU_APP_ID="cli_xxxxxxxxxxxx"
export FEISHU_APP_SECRET="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
飞书高级 配 置字段 ：

--- Page 223 ---

223字段 说明 默认值
domain API 域名（feishu 或 lark） feishu
connectionMode 事件传输 模式（websocket 或 webhook） websocket
verificationToken Webhook 模式 需 要 -
webhookPath Webhook 路由路 径 /feishu/events
webhookHost Webhook 绑定主机 127.0.0.1
webhookPort Webhook 绑定 端 口 3000
streaming 启用流式 卡片输出 true
blockStreaming启用块级流式 true
textChunkLimit 消息分块大小 2000
mediaMaxMb 媒体大小 限制 30
Step 4: 配对测 试
# 1. 启动  Gateway
openclaw gateway
# 2. 在⻜书中找到机器⼈，发送消息
# 3. 机器⼈会回复配对码，执⾏批准命令
openclaw pairing approve feishu < 配对码 >
# 4. 查看配对列表
openclaw pairing list feishu
国内部署注意 事 项 ：
1. 网络环境：确保服务 器可以 访 问 飞 书 开 放 平 台  API （open.feishu.cn）
2. 备案要求：如需使用  Webhook 模 式（ 非  WebSocket ） ， 确 保 域 名 已完 成  ICP 备 案
3. 企业认证：部分高 级权 限 需 要 企 业 完 成 飞 书 认证
4. 长连接稳定性：WebSocket 模 式 适 合国内部 署 ， 无 需 公 网  IP 或 域 名
飞书常用命令 ：

--- Page 224 ---

224命令 说明
/status 显示  Bot 状 态
/reset 重置会话
/model 显示 /切换模 型
注意：飞 书暂不 支持原 生 命 令 菜 单 ， 需 手动 输 入 命 令 。
获取用户 /群 组  ID ：
启动  Gateway 后 ， 在 日 志 中 查 看（openclaw logs --follow）
用户  ID 格式 ：ou_xxx
群组  ID 格式 ：oc_xxx
6.3 实战案 例
6.3.1 案例 一：个人  AI 助 手
场景描述 ： 构建一个个人  AI 助 手 ， 通过  WhatsApp 或  Telegram 随 时 访 问 。
配置实现 ：

--- Page 225 ---

225// ~/.openclaw/openclaw.json
{
  agents: {
    defaults: {
      workspace: "~/.openclaw/workspace",
      model: {
        primary: "anthropic/claude-sonnet-4-5",
      },
      models: {
        "anthropic/claude-sonnet-4-5": { alias: "Sonnet" },
      },
    },
    list: [
      {
        id: "main",
      },
    ],
  },
  channels: {
    whatsapp: {
      enabled: true,
      dmPolicy: "pairing",
      allowFrom: ["${MY_PHONE_NUMBER}"],
    },
  },
  session: {
    dmScope: "per-channel-peer",
    reset: {
      mode: "daily",
      atHour: 4,
    },
  },
}
启动步骤 ：

--- Page 226 ---

226# 1. 配对  WhatsApp
openclaw channels login --channel whatsapp
# 2. 启动  Gateway
openclaw gateway
# 3. 批准配对
openclaw pairing approve whatsapp <CODE>
# 4. 开始对话
# 在 WhatsApp 中向⾃⼰发送消息
6.3.2 案例 二 ： 团 队 协 作 助 手
场景描述 ： 为团队配 置 一个  Discord 机 器 人 ， 协 助 日 常 沟 通 。
配置实现 ：

--- Page 227 ---

227{
  agents: {
    defaults: {
      workspace: "~/.openclaw/workspace",
      model: {
        primary: "openai/gpt-5.2",
      },
      models: {
        "openai/gpt-5.2": { alias: "GPT" },
      },
    },
    list: [
      {
        id: "main",
        groupChat: {
          mentionPatterns: ["@Assistant", "@ 助⼿ "],
        },
      },
    ],
  },
  channels: {
    discord: {
      enabled: true,
      token: "${DISCORD_BOT_TOKEN}",
      dmPolicy: "pairing",
      guilds: {
        "${TEAM_GUILD_ID}": {
          channels: ["${GENERAL_CHANNEL}"],
          requireMention: true,
        },
      },
    },
  },
  hooks: {
    enabled: true,
    token: "${WEBHOOK_TOKEN}",
    path: "/hooks",
  },
}
部署步骤 ：

--- Page 228 ---

228# 1. 配置环境变量
export DISCORD_BOT_TOKEN="xxx"
export TEAM_GUILD_ID="xxx"
export GENERAL_CHANNEL="xxx"
export WEBHOOK_TOKEN="xxx"
# 2. 启动服务
openclaw gateway --port 18789
# 3. 在 Discord 中 @ 机器⼈进⾏对话
6.3.3 案例三 ：多平 台统 一 助 手
场景描述 ： 同时连接  WhatsApp 、 Telegram 、 Discord 和 飞 书 ， 统 一 管 理 。
配置实现 ：

--- Page 229 ---

229{
  agents: {
    defaults: {
      workspace: "~/.openclaw/workspace",
      model: {
        primary: "anthropic/claude-sonnet-4-5",
        fallbacks: ["openai/gpt-5.2"],
      },
      models: {
        "anthropic/claude-sonnet-4-5": { alias: "Sonnet" },
        "openai/gpt-5.2": { alias: "GPT" },
      },
    },
    list: [
      {
        id: "main",
        default: true,
        groupChat: {
          mentionPatterns: ["@openclaw"],
        },
      },
      {
        id: "coding",
        workspace: "/home/user/coding-workspace",
        model: {
          primary: "openai/gpt-5.2",
        },
      },
    ],
  },
  channels: {
    whatsapp: {
      enabled: true,
      dmPolicy: "pairing",
      allowFrom: ["+8613800138000"],
    },
    telegram: {
      enabled: true,
      botToken: "${TELEGRAM_BOT_TOKEN}",
      dmPolicy: "pairing",
      allowFrom: ["tg:123456789"],
    },
    discord: {
      enabled: true,
      token: "${DISCORD_BOT_TOKEN}",
      dmPolicy: "pairing",
    },

--- Page 230 ---

230    feishu: {
      enabled: true,
      dmPolicy: "pairing",
      accounts: {
        main: {
          appId: "${FEISHU_APP_ID}",
          appSecret: "${FEISHU_APP_SECRET}",
        },
      },
      streaming: true,
      blockStreaming: true,
    },
  },
  session: {
    dmScope: "per-channel-peer",
    threadBindings: {
      enabled: true,
      idleHours: 24,
    },
    reset: {
      mode: "idle",
      idleMinutes: 120,
    },
  },
  cron: {
    enabled: true,
    maxConcurrentRuns: 2,
  },
  bindings: [
    {
      agentId: "main",
      match: { channel: "whatsapp" },
    },
    {
      agentId: "main",
      match: { channel: "telegram" },
    },
    {
      agentId: "main",
      match: { channel: "discord" },
    },
    {
      agentId: "coding",
      match: {
        channel: "feishu",
        peer: { kind: "group", id: "${FEISHU_CODING_GROUP_ID}" },
      },

--- Page 231 ---

231    },
    {
      agentId: "main",
      match: {
        channel: "feishu",
        peer: { kind: "direct" },
      },
    },
  ],
}
6.3.4 案例 四 ： 配 置 文 件 分 割
场景描述 ： 配置复杂时 ， 使用  $include 分割配置文 件 。
主配置：
// ~/.openclaw/openclaw.json
{
  gateway: { port: 18789 },
  agents: { $include: "./agents.json5" },
  channels: { $include: "./channels.json5" },
  session: { $include: "./session.json5" },
}
agents.json5 ：
{
  defaults: {
    workspace: "~/.openclaw/workspace",
    model: {
      primary: "anthropic/claude-sonnet-4-5",
    },
    models: {
      "anthropic/claude-sonnet-4-5": { alias: "Sonnet" },
    },
  },
  list: [
    { id: "main" },
  ],
}
说明：

--- Page 232 ---

232单文件：替 换 包含 的 对 象
文件数组 ：按顺序 深 度合 并 （后 覆 盖 前）
同级键：在  include 后合 并 （ 覆 盖  included 值 ）
支持嵌套  include ， 最多  10 层
相对路径 ：相对于 包 含 文 件 的 目 录 解 析
6.4 故障排 除
6.4.1 常见问题  FAQ
Q: 安装时提 示权 限 错 误 （ EACCES ）
解决方案 ：
# ⽅法 1 ：使⽤  npx
npx openclaw <command>
# ⽅法 2 ：更改  npm 默认⽬录
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
# ⽅法 3 ：使⽤  nvm
nvm install 22
nvm use 22
npm install -g openclaw
Q: 启动网关时提 示 端 口被 占 用
解决方案 ：
# 查找占⽤进程
lsof -i :18789
# 更换端⼝启动
openclaw gateway --port 18790
Q: 无法连接到  LLM API
诊断步骤 ：

--- Page 233 ---

233# 1. 检查  API 密钥是否设置
echo $ANTHROPIC_API_KEY
# 2. 测试⽹络连通性
curl https://api.anthropic.com/v1/models \
  -H "x-api-key: $ANTHROPIC_API_KEY"
# 3. 检查代理设置
echo $HTTPS_PROXY
Q: WhatsApp 无法 配 对
解决方案 ：
# 重新配对
openclaw channels login --channel whatsapp
# 查看配对列表
openclaw pairing list whatsapp
# 批准配对
openclaw pairing approve whatsapp <CODE>
# 检查⽇志
openclaw logs --follow
Q: Discord Bot 显 示 离 线
检查清单 ：
 Token 是否正 确
 Bot 是否 已加入服务 器
 Intents 是否启用（ Privileged Gateway Intents ）
 权限是否 足够
Q: 飞书机 器人无响 应
检查清单 ：
 应用是否 已发 布并 通过 审 核
 事件订阅是否 包含  im.message.receive_v1
 是否选择  长连接接收 事件 模式
 应用权限是否 完 整 （ 17 个  tenant + 3 个  user 权 限 ）

--- Page 234 ---

234 Gateway 是否正在 运 行
 检查日志 ：openclaw logs --follow
 网络是否可以访问  open.feishu.cn
6.4.2 配置热 重载
OpenClaw 支持 配 置 文 件 热 重载 ， 无 需 手动 重 启  Gateway 。
重载模式 ：
{
  gateway: {
    reload: {
      mode: "hybrid",      // hybrid | hot | restart | off
      debounceMs: 300,
    },
  },
}
模式 行为
hybrid（默认） 安全更改 即时热 应 用 ， 关 键 更 改 自动 重 启
hot 仅热应用安全更 改 ， 需 要 重 启 时 记 录 警 告
restart 任何更改 都重启  Gateway
off 禁用文件监控
需要重启 的 配 置更 改 ：
类别 字段
Gateway 服务 器 gateway.*（端口、 绑定 、 认证 、 TLS 等）
基础设施 discovery、canvasHost、plugins
无需重启 的 配 置更 改 ：
所有通道 配 置
Agent 和 模 型 配 置

--- Page 235 ---

235自动化（ hooks 、 cron 、 heartbeat ）
会话和消息 配 置
工具和多媒体 配 置
6.4.3 日志分析
查看日志（推 荐方式） ：
# 实时查看⽹关⽇志
openclaw logs --follow
# 查看最近⽇志
openclaw logs
# 搜索错误
openclaw logs | grep ERROR
日志文件位 置 ：
~/.openclaw/logs/
├── gateway.log          # ⽹关⽇志
└── channels/            # 通道⽇志
    ├── whatsapp.log
    ├── telegram.log
    ├── discord.log
    └── feishu.log
6.4.4 获取 帮 助
官方资源 ：
官方文档 ：https://docs.openclaw.ai
GitHub：https://github.com/openclaw/openclaw
Discord 社区 ：https://discord.gg/openclaw
提交  Issue ：

--- Page 236 ---

236## 问题描述
清晰描述遇到的问题
## 复现步骤
1. 执⾏ '...'
2. 输⼊ '...'
3. 看到错误
## 环境信息
- OpenClaw 版本：（运⾏  openclaw --version ）
- Node.js 版本：（运⾏  node --version ）
- 操作系统：
## 配置⽂件
```json5
（脱敏后的  openclaw.json ）
```
## ⽇志输出
```
（相关的错误⽇志）
```
本章总结
本章介绍了  OpenClaw 的 实 践 应 用 ：
安装部署：通过官方安 装脚 本 或  npm 全 局 安 装 ， 使 用  openclaw onboard 初始化配 置 。
配置详解：~/.openclaw/openclaw.json 采用  JSON5 格式 ， 支持 注 释 和 尾 随 逗 号 。 核 心 配 置 块 包
括：
agents.defaults + agents.list - Agent 配 置
agents.defaults.models - 模型目录（用于  /model 命令）
channels.* - 各通道 配 置
session - 会话配 置（含  threadBindings 、 reset ）
cron - 定时任务 配 置
hooks - Webhook 配 置
bindings - 多代理 路由 配 置

--- Page 237 ---

237环境变量：支持  .env 文件、${VAR} 引用语法 、 SecretRef （ env/file/exec ）和内联  env.vars
配置。
实战案例：涵盖个人 助手 、 团 队 协 作 、 多平 台 部 署 和 飞 书 集 成 四种 典 型场 景 。
故障排除：常见问题 解决方 案 、 配 置 热 重载 机制和 日 志 分 析 方法 。
实践建议 ：
1. 从简单开 始：先配置单 一通道 ， 验 证 成 功 后 再 扩 展
2. 安全配置：使用  allowFrom 限制访问 ，避 免 未 授 权 使 用
3. 环境变量：敏感信息（ API 密 钥 、 Token ）通过 环 境 变 量或  SecretRef 注入
4. 监控日志：使用  openclaw logs --follow 实时查看 日志
5. 及时配对：新用户首次 使用 需 要 执 行 配 对 批 准
6. 配置文件分 割：复杂配 置使用  $include 分割为多个文 件
参考资源
OpenClaw 官方文 档
OpenClaw GitHub 仓 库
配置参考文档
完整配置字段 参考
WhatsApp 配 置
Telegram 配 置
Discord 配 置
飞书配置
Anthropic API 文 档
OpenAI API 文档

--- Page 238 ---

238第7章  生 态 与 创 业
OpenClaw 不仅是 一 个 强 大 的  AI 代 理 框 架 ， 更是 一 个 蓬勃 发 展 的 开发者生 态 系 统 。 本 章将 深 入 探
讨如何参与  OpenClaw 生 态建设 —— 从 开发自定 义  Skill 到社区 贡 献 ， 再 到 基 于  OpenClaw 的 创 业机
会与未来 展望 。
7.1 Skill 开发 指 南
Skill 是  OpenClaw 生 态 系 统 的 核 心 组 件 ， 它 将  Codex 从 一 个通用  AI 助 手 转 变 为特定 领 域 的 专业
代理。掌握  Skill 开发 ， 意 味 着 你能 够 无 限 扩 展  OpenClaw 的 能力 边 界 。
7.1.1 Skill 体系架 构 理 解
什么是  Skill ？
Skill 是一个自 包含 的 功 能 模 块 ， 包 含 以下要 素 ：
SKILL.md（必需） ： 模块 的 核 心定 义 文 件 ， 包 含 元 数 据 和 操 作 指 南
Scripts/（可选） ：可执行 脚 本 ， 用于实现 确 定性 任 务
References/（可选） ： 参考文 档 ， 供  AI 按 需 加 载
Assets/（可选） ： 模板 、 图 标 等 输 出资 源
Skill 的核心 设计 哲 学是渐进式披 露（Progressive Disclosure ） ：
1. Level 1 - 元数 据：name + description 始终存在于上下文 中 （ 约 100 词 ）
2. Level 2 - SKILL.md 正文：当  Skill 触发时加 载 （ <5000 词 ）
3. Level 3 - 捆 绑资 源：根据需要动 态加 载 （无 限 制）
这种设计 确 保了上下文 窗 口 的 高 效 利 用 —— 只 有 真 正 需 要 的 信息 才 会 被 加 载 。
Skill 存储位 置与加 载 优先 级
Skills 从以下三个位 置 加 载 ， 优先 级从 高到 低 ：
1. Workspace skills: <workspace>/skills（最高优先 级 ，用于 项 目 专 属 技能）
2. Managed/local skills: ~/.openclaw/skills（用户安 装 的本地技能）
3. Bundled skills: 随 OpenClaw 安 装包 附 带 （最 低优先 级 ）

--- Page 239 ---

239也可通过 配 置  skills.load.extraDirs 添加额外 的技能加 载目 录 。
Skill 触发机制
OpenClaw 通过以下方式 判 断 何 时 使 用 某 个  Skill ：
---
name: feishu-doc
description: Feishu document read/write operations. Activate when user mentions 
Feishu docs, cloud docs, or docx links.
---
description 字段 是关 键 触 发 器，它需要 ：
清晰描述  Skill 的 功 能
明确列出触发 条件
覆盖所有 使用 场 景
7.1.2 SKILL.md 规 范详 解
Frontmatter 格式
每个  SKILL.md 必 须 以  YAML frontmatter 开 头 ：
---
name: skill-name
description: Skill 功能描述，包含触发条件和使⽤场景
---
命名规范：
仅使用小写 字母 、 数 字 和 连 字 符
动词开头 ，描述动作（如  gh-issues, nano-pdf）
长度控制在  64 字 符 以内
文件夹名与  Skill 名 完 全 一 致
可选字段：

--- Page 240 ---

240字段 类型说明
user-invocable Boolean是否暴露为用户 斜 杠 命 令 ， 默 认  true
disable-model-invocation Boolean是否从模 型提 示 中 排 除 ， 默 认  false
command-dispatch String设置为  tool 时斜杠命令 直接 调 度到工 具
command-tool Stringcommand-dispatch 为 tool 时调用的工 具名
command-arg-mode String参数模式 ，raw（默认） 将原 始参 数 字 符 串 转 发 给 工 具
homepage String在 macOS Skills UI 中 显 示 为  "Website" 的  URL
字段说明：
user-invocable: 设置为  false 时，用户无法通过 斜 杠 命 令 调 用 该  Skill ， 只 能通过 模 型 自动 触
发
disable-model-invocation: 设置为  true 时，模型不会自动 触 发 该  Skill ， 只 能通过用户 斜 杠
命令调用
metadata.openclaw 字 段 说明
SKILL.md 支持在  frontmatter 中 添 加  OpenClaw 专 属 元 数 据 。metadata 字段使用单行  JSON
格式嵌入  YAML frontmatter 中：
---
name: my-skill
description: Skill 描述
metadata:
  {"openclaw": {"emoji": " 🔧 ", "requires": {"bins": ["python3"], "env": 
["API_KEY"]}, "primaryEnv": "API_KEY"}}
---
关键要点：
name 和 description 使用  YAML 格式（ 冒 号分 隔 ）
metadata 字段使用单行  JSON（避免多行  frontmatter 解 析 问题）
官方解析 器仅 支持单 行  frontmatter 键值
字段说明：

--- Page 241 ---

241字段类型说明
emoji String Skill 的标 识  emoji ， 用于  UI 展示
requires Object依赖声明 ， 包含  bins（二进制数 组） 、env（环境变 量数 组） 、
config（openclaw.json 中 必 须 为  truthy 的 配 置路 径 列 表） 、
anyBins（任一即可 的 二进制数 组 ）
primaryEnv String主要环境 变 量名 ， 用于  API Key 关联 。 可通过  skills.entries.
<skill>.apiKey 配置覆盖
install Array安装指令数 组 ， 支持 多 种 安 装 器 类 型 ， 见 下方 详 细 说明
always Boolean是否始终 包含 此  Skill （不 依 赖 触 发 条件 ）
os Array支持的操作系 统 列 表（ darwin 、 linux 、 win32 ）
requires 字段详解：
子字段类型说明
bins Array必需的二进制文 件 列 表 ， 如  ["python3", "node"]
anyBins Array满足任一 即可 的 二 进制文 件 ， 如  ["python3", "python"]
env Array必需的环境 变 量 列 表 ， 如  ["API_KEY", "SECRET_TOKEN"]
config Array openclaw.json 中 必 须 为  truthy 的 配 置路 径 列 表 ， 如  ["browser.enabled"]
install 安装器配 置：
install 数组定义自动安 装 依 赖 的 指 令 ， 支持 以下类 型 ：

--- Page 242 ---

242安装器说明 示例
pip Python 包安 装 {"type": "pip", "packages": ["requests", "pandas"]}
npm Node.js 包安 装 {"type": "npm", "packages": ["lodash", "axios"]}
brew Homebrew 包安 装{"type": "brew", "packages": ["ffmpeg",
"imagemagick"]}
aptDebian/Ubuntu
包{"type": "apt", "packages": ["libpq-dev"]}
script自定义脚本 {"type": "script", "script": "./scripts/setup.sh"}
环境变量注入机制：
primaryEnv 指定的变 量可通过  skills.entries.<skill>.apiKey 配置
环境注入仅在  agent run 期 间 有 效 ， 运 行 结 束 后 恢 复
如果变量已 存在于进 程 中， config 中的 值 不会 覆 盖
特殊占位 符：
{baseDir} - 引用  Skill 文 件 夹 路 径 ， 用于 指 令 中 引 用 脚 本 或 资 源 文 件
示例 : python {baseDir}/scripts/process.py
示例：
---
name: pdf-processor
description: PDF ⽂档处理⼯具，⽀持旋转、合并、拆分、提取⽂本等操作。
metadata:
  {"openclaw": {"emoji": " 📄 ", "requires": {"bins": ["python3"]}, "install": 
[{"type": "pip", "packages": ["pypdf", "pillow", "pdf2image"]}]}}
---
正文结构
标准  SKILL.md 应包 含 以下部分 ：

--- Page 243 ---

243# Skill 名称
## 概述
简要介绍 Skill 的功能和⽤途。
## 使⽤场景
- 场景1 ： ...
- 场景2 ： ...
## 核⼼操作
### 操作1 ： xxx
详细说明和示例代码。
### 操作2 ： xxx
...
## 最佳实践
- 建议1
- 建议2
## 注意事项
- 限制1
- 限制2
内容组织 原则
1. 简洁优先
上下文窗 口是公 共 资 源 。 只 添 加  Codex 不 具 备 的 信息 ：
❌ 不推荐：
"Python 是⼀种⾼级编程语⾔，由  Guido van Rossum 于  1991 年创建 ..."
✅ 推荐：
"使⽤ pdfplumber 提取⽂本： "
[直接代码示例 ]
2. 自由度 匹 配
根据任务 的 确定性和可 变 性 设置 适 当自 由 度 ：

--- Page 244 ---

244自由度级别适用场景 实现方式
高 多种方法 有 效 ， 需 上下文 判 断 文本说明  + 启发式 指 导
中 有推荐模式 ， 允 许 一 定 变 化 伪代码  + 可 配 置 参 数
低 操作脆弱 ， 需严 格 一 致 性 特定脚本 ，极 少 参 数
3. 渐进式 组织
对于复杂  Skill ， 将 变 体内 容 分 离 到 参考 文 件 ：
skill-name/
├── SKILL.md              # 核⼼⼯作流  + 导航
├── references/
│   ├── aws.md           # AWS 部署模式
│   ├── gcp.md           # GCP 部署模式
│   └── azure.md         # Azure 部署模式
└── scripts/
    └── deploy.py
7.1.3 Skill 开发 流程
阶段一： 需 求分析 与 示 例 收 集
在编码之前 ，明 确  Skill 的 具 体 使 用方式 ：
问题清单：
1. Skill 应该⽀持哪些功能？
2. ⽤户会如何描述需求？
3. 有哪些典型使⽤示例？
4. 边界情况有哪些？
示例收集技巧：
与潜在用户对话 ， 收 集真 实用 例
生成示例 并与用户 确 认
记录成功和失败 的 边 界 情 况
阶段二：资 源规划
分析每个 示例 ， 确 定 需 要 哪 些 资 源 ：

--- Page 245 ---

245示例任务 分析 所需资源
"帮我旋转  PDF" 每次重写 代码 scripts/rotate_pdf.py
"生成  React 待 办 应 用 " 重复样板 代码 assets/react-template/
"查询今日登录用户 " 需表结构信息 references/schema.md
阶段三：初 始化  Skill
创建  Skill 目录 结 构 有 两种 方式 ： 使 用  ClawHub CLI 或 手动 创建 。
方式一： 使用  ClawHub CLI （推 荐 ）
# 安装 ClawHub CLI
npm i -g clawhub
# 查看已安装的  skills 作为参考
clawhub list
# 安装已有  skill 到本地（可作为模板参考）
clawhub install <skill-slug>
# 发布⾃⼰的  Skill （开发完成后）
clawhub publish ./my-skill --slug my-skill --version 1.0.0
# 同步备份所有已安装  Skill 配置
clawhub sync --all
# 更新所有已安装  Skill
clawhub update --all
ClawHub CLI 是 官 方推 荐 的  Skill 管 理工 具 ， 支持搜索 、 安 装 、 更 新 和发 布  Skills 。 详 细 文 档 参
见：https://docs.openclaw.ai/tools/clawhub
方式二：手动 创建目 录 结 构
# 创建 Skill ⽬录
mkdir -p ~/.openclaw/skills/my-skill/{scripts,references,assets}
# 创建 SKILL.md ⽂件
touch ~/.openclaw/skills/my-skill/SKILL.md
标准  Skill 目录 结 构 ：

--- Page 246 ---

246my-skill/
├── SKILL.md              # 核⼼定义⽂件（必需）
├── scripts/              # 可执⾏脚本（可选）
│   └── example.py
├── references/           # 参考⽂档（可选）
│   └── guide.md
└── assets/               # 模板资源（可选）
    └── template.txt
阶段四：实现资 源
Scripts 开发：

--- Page 247 ---

247# scripts/pdf_processor.py
#!/usr/bin/env python3
"""
PDF 处理脚本
⽤法: python pdf_processor.py <action> <input> [options]
依赖安装: pip install pypdf pillow pdf2image
"""
import sys
import argparse
from pypdf import PdfReader, PdfWriter
def rotate_pdf(input_path, output_path, degrees=90):
    """旋转 PDF ⻚⾯ """
    reader = PdfReader(input_path)
    writer = PdfWriter()
    
    for page in reader.pages:
        page.rotate(degrees)
        writer.add_page(page)
    
    with open(output_path, 'wb') as f:
        writer.write(f)
    print(f" 已旋转并保存⾄ : {output_path}")
def merge_pdfs(input_paths, output_path):
    """合并多个  PDF"""
    writer = PdfWriter()
    
    for input_path in input_paths:
        reader = PdfReader(input_path)
        for page in reader.pages:
            writer.add_page(page)
    
    with open(output_path, 'wb') as f:
        writer.write(f)
    print(f" 已合并  {len(input_paths)} 个⽂件⾄ : {output_path}")
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='PDF 处理⼯具 ')
    parser.add_argument("action", choices=["rotate", "merge", "split"],
                       help='操作类型 : rotate( 旋转 ), merge( 合并 ), split( 拆分 )')
    parser.add_argument("input", nargs="+", help=' 输⼊⽂件路径 ')
    parser.add_argument("-o", "--output", required=True, help=' 输出⽂件路径 ')
    parser.add_argument("-d", "--degrees", type=int, default=90,
                       help='旋转⻆度（默认 90 度） ')
    

--- Page 248 ---

248    args = parser.parse_args()
    
    # 执⾏逻辑
    if args.action == "rotate":
        rotate_pdf(args.input[0], args.output, args.decrees)
    elif args.action == "merge":
        merge_pdfs(args.input, args.output)
References 编写：
<!-- references/api-guide.md -->
# API 使⽤指南
## 认证
```bash
curl -H "Authorization: Bearer $TOKEN" ...
```
## 端点列表
### GET /api/v1/users
获取⽤户列表
**参数** ：
- `limit`: 返回数量（默认  20 ，最⼤  100 ）
- `offset`: 分⻚偏移量
**响应** ：
```json
{
  "users": [...],
  "total": 100,
  "has_more": true
}
```
Assets 准备：

--- Page 249 ---

249assets/
├── webapp-template/        # React 项⽬模板
│   ├── package.json
│   ├── src/
│   └── public/
├── report-template.docx    # Word 模板
└── logo.png               # 品牌资源
阶段五： 编写  SKILL.md
Frontmatter 示例：
---
name: pdf-processor
description: PDF ⽂档处理⼯具，⽀持旋转、合并、拆分、提取⽂本等操作。使⽤场景： 1) 旋转扫描⽂档到
正确⽅向 2) 合并多个  PDF 为单个⽂件  3) 提取  PDF 中的⽂本内容  4) 压缩  PDF ⽂件⼤⼩。触发条件：
⽤户提及 PDF 处理、⽂档旋转、⽂件合并等需求。
---
正文示例：

--- Page 250 ---

250# PDF 处理器
## 快速开始
### 旋转 PDF
```bash
python scripts/pdf_processor.py rotate input.pdf -o output.pdf -d 90
```
### 合并 PDF
```bash
python scripts/pdf_processor.py merge file1.pdf file2.pdf -o merged.pdf
```
## ⾼级功能
### 批量处理
对于⽬录中的所有  PDF ：
```bash
for f in *.pdf; do
  python scripts/pdf_processor.py rotate "$f" -o "rotated/$f"
done
```
### ⽂本提取
使⽤ `extract` 动作提取纯⽂本（保留布局）。
## 限制说明
- 不⽀持密码保护的  PDF
- 加密 PDF 需先解密
- 最⼤⽂件⼤⼩： 100MB
7.1.4 测试与 调试
单元测试
# 测试脚本功能
python scripts/pdf_processor.py rotate test.pdf -o test_out.pdf
# 验证输出
ls -lh test_out.pdf
集成测试
在真实对话 环境 中 测 试  Skill ：

--- Page 251 ---

251⽤户：帮我旋转这个  PDF 90 度
AI：我将使⽤  pdf-processor skill 帮您旋转 ...
[观察触发是否正确 ]
[观察执⾏是否成功 ]
[观察输出是否符合预期 ]
调试技巧
1. 触发问题：
检查  description 是 否 包 含 关 键 词
确认  description 清 晰 描述 了 使 用 场 景
2. 执行问题：
测试脚本是否可独 立运 行
检查依赖是否 完 整
3. 输出问题：
验证脚本输出 格式
检查错误 处理 逻辑
7.1.5 打包与发 布
打包验证
Skill 开发 完成后 ， 需 要 验 证 其 结 构 和内 容 ：
手动验证清单：
 YAML frontmatter 格 式正 确 （以  --- 开始和结束 ， name/desc 使 用  YAML ， metadata 使
用单行  JSON）
name 字段存在且与 目录名 一 致
description 字段存在且 清 晰描述 功 能
 脚本文件具 有可执 行权 限 （如 需 要）
 依赖已在  metadata.openclaw.requires 中 声 明
测试  Skill：

--- Page 252 ---

252# 1. 放置到  skills ⽬录
ln -s $(pwd)/my-skill ~/.openclaw/skills/
# 2. 重启  Gateway 或重新加载技能
openclaw gateway restart
# 3. 测试触发  - 在对话中尝试触发该  Skill
分发准备：
# 打包为 tar.gz （可选）
tar -czf my-skill-v1.0.0.tar.gz my-skill/
# 或创建 git 标签发布
git tag v1.0.0
git push origin v1.0.0
分发方式
方式一：本地分发
# 复制到⽬标机器
scp -r my-skill/ user@host:~/.openclaw/skills/
方式二： Git 仓 库 分 享（推荐）
# 推送 Skill 到  GitHub
git init
git add .
git commit -m "Initial skill release"
git remote add origin https://github.com/user/my-skill.git
git push -u origin main
# 创建发布标签
git tag v1.0.0
git push origin v1.0.0
用户可通过  ClawHub CLI 直 接安 装 ：

--- Page 253 ---

253# 安装 ClawHub CLI
npm i -g clawhub
# 搜索 Skill
clawhub search "pdf"
# 安装指定  Skill
clawhub install pdf-processor
# 更新所有已安装  Skill
clawhub update --all
# 发布⾃⼰的  Skill
clawhub publish ./my-skill --slug my-skill --version 1.0.0
# 同步备份  Skill 配置
clawhub sync --all
方式三： ClawHub 市 场（推荐）
ClawHub 是  OpenClaw 的 官 方  Skill 市 场 ， 已 正式上线 运 营 。
ClawHub 特 点：
公共  Skill 注 册表 ， 集 中 管 理社区  Skills
语义搜索（ embeddings 驱 动 ， 非 仅 关 键 词 匹 配 ）
版本管理（遵 循  semver 规 范 ）
星级评分和用户 评 论
内容审核机制 保障 质量
访问地址：https://clawhub.ai
7.1.6 Skill 开发最 佳 实 践
设计原则
1. 单一职责：每个  Skill 解决 一 个 具 体问题 域
2. 自包含：所有依 赖 应在  Skill 内 解 决
3. 渐进加载：大型文档按 需加 载
4. 可测试：所有脚本 应可独 立运 行
反模式避 免

--- Page 254 ---

254❌ 不要创建这些⽂件：
- README.md （信息应已在  SKILL.md ）
- INSTALLATION_GUIDE.md （ SKILL.md 应包含基本使⽤）
- QUICK_REFERENCE.md （同上）
- CHANGELOG.md （版本信息可通过  Git 管理）
❌ 不要在  SKILL.md 中：
- 解释显⽽易⻅的内容
- 复制参考⽂档中的详细  API
- 包含 Skill 创建过程的描述
性能优化
# ⼤型 Skill 优化示例
## 基础使⽤（始终在上下⽂中）
[简要说明和示例 ]
## ⾼级功能
- **表单处理 ** ：⻅  [FORMS.md](references/FORMS.md)
- **API 参考 ** ：⻅  [API.md](references/API.md)
- **示例集合 ** ：⻅  [EXAMPLES.md](references/EXAMPLES.md)
官方设计 参考
OpenClaw 官方提 供 了 一 系 列 设计 参考 文 档 ， 帮 助 开发者 创建 高 质量 的  Skill ：
官方文档：https://docs.openclaw.ai/tools/skills
SKILL.md 完 整 规 范 说明
Frontmatter 格式 详 细 要 求
metadata 字段 完 整参考
workflows.md - 工作流设计 模式
标准  Skill 工作 流程 模 板
多步骤任务 编排 模 式
错误处理和 重 试机制
异步任务 处理 模式
output-patterns.md - 输出格式 规范
标准响应格式（成 功 / 失 败 ）

--- Page 255 ---

255表格和列表输出最 佳 实 践
代码块和 日志输出 规 范
进度反馈和状 态更 新 模 式
ClawHub 文 档：https://docs.openclaw.ai/tools/clawhub
CLI 安装和 使用 指 南
Skill 发布流程
版本管理 规范
配置参考：
~/.openclaw/openclaw.json - 全局配 置
skills.entries - Skill 级 配 置 覆盖
环境变量命名 规范
官方示例 仓 库：https://github.com/openclaw/openclaw/tree/main/skills
标准  Skill 结 构 示 例
常见集成 模式 参考
测试和调试模板
开发者应在 创建  Skill 前 查 阅 这 些参考 资 料 ， 确 保设计 符 合  OpenClaw 生 态标 准 。
Skill Token 消 耗 优 化
Skills 会占用 模 型 的 上下文 窗 口 ， 了 解  Token 消 耗 计 算 有 助 于 优 化  Skill 设计 ：
Token 计算公式：
total = 195 + Σ (97 + len(name_escaped) + len(description_escaped) + 
len(location_escaped))
基础开销（当有≥ 1个  skill 时） ： 195 字 符
每个  skill：97 字符  + 转义后 的  name/description/location 长度
约 97 字符  ≈  24 tokens
优化建议：
1. 保持  description 简洁明确 ，避 免 冗 余描述
2. 使用  always: false（默认）避 免不 必 要 的  Skill 常 驻 上下文

--- Page 256 ---

2563. 将详细文档 放入  references/ 按需加载 ， 而 非全部 写 在  SKILL.md 正文
4. 合理拆分大 型  Skill ， 避 免单 个  Skill 内 容 过多
版本管理最佳实 践
ClawHub 使用 语 义 化版本（ semver ） 管 理  Skill 版本 ：
主版本.次版本 . 修订版本
  1  .   0   .   0
主版本：破坏性 变更 ，不 兼 容 的  API 修改
次版本：向下兼 容 的 功能 添 加
修订版本：向下兼 容 的问题 修 复
版本发布流程：
# 1. 更新  SKILL.md 中的版本信息
# 2. 提交代码
git add .
git commit -m "feat: add new feature"
# 3. 创建版本标签
git tag v1.0.0
git push origin v1.0.0
# 4. 发布到  ClawHub
clawhub publish ./my-skill --slug my-skill --version 1.0.0
版本管理特 点：
每次发布创建 新的  SkillVersion，保留完 整版本 历 史
支持  tags（如  latest）指向特定版本
本地更改与  registry 版本通过内 容 哈 希 比 较
用户可通过  clawhub update 获取最新版本
7.2 社区参与
OpenClaw 的成 功 离 不开活 跃 的 开发者社区 。 本 节将介 绍 如 何 参 与社区 建设 ， 从代码 贡 献 到社区 互
动。

--- Page 257 ---

2577.2.1 GitHub 贡 献 指 南
项目结构
OpenClaw 项 目托 管 在  GitHub ：https://github.com/openclaw/openclaw
官方资源 链接 ：
📖 官方文档：https://docs.openclaw.ai
🐙 GitHub 仓 库：https://github.com/openclaw/openclaw
🌐 ClawHub 市 场：https://clawhub.ai
💬 Discord 社区：https://discord.gg/clawd
openclaw/
├── src/                    # 核⼼源代码
├── extensions/             # 扩展模块
│   ├── feishu/            # ⻜书集成
│   ├── discord/           # Discord 集成
│   └── ...
├── skills/                # 内置  Skills
│   ├── core/              # 核⼼  Skills
│   └── community/         # 社区  Skills
├── docs/                  # ⽂档
└── tests/                 # 测试套件
贡献类型
1. Bug 修 复
## 提交 Bug 报告
1. 搜索现有  issues ，避免重复
2. 使⽤ Bug 报告模板
3. 提供最⼩复现步骤
4. 包含环境信息（ OS 、版本等）
## 修复流程
1. Fork 仓库
2. 创建分⽀： `git checkout -b fix/issue-number`
3. 编写修复  + 测试
4. 提交 PR ，关联  issue
2. 功能开发

--- Page 258 ---

258## 新功能流程
1. 先开 Issue 讨论设计
2. 等待维护者反馈
3. 获得批准后开发
4. 包含⽂档和测试
3. 文档改进
## ⽂档贡献
- 修复 typo 和链接
- 添加使⽤示例
- 翻译⽂档
- 改进 API ⽂档
代码规范
// TypeScript 规范示例
// 1. 使⽤明确的类型
function processSkill(skill: Skill): Result {
  // 2. 添加  JSDoc 注释
  /**
   * 处理 Skill ⽂件
   * @param skill - Skill 对象
   * @returns 处理结果
   */
  
  // 3. 使⽤早期返回
  if (!skill.isValid) {
    return { success: false, error: "Invalid skill" };
  }
  
  // 4. 避免深层嵌套
  return processValidSkill(skill);
}
Pull Request 流程

--- Page 259 ---

259# 1. 同步上游
git remote add upstream https://github.com/openclaw/openclaw.git
git fetch upstream
git rebase upstream/main
# 2. 创建功能分⽀
git checkout -b feature/my-feature
# 3. 开发并提交
git add .
git commit -m "feat: add new feature
- 详细描述变更
- 修复 #123"
# 4. 推送并创建  PR
git push origin feature/my-feature
# 然后在 GitHub 上创建  Pull Request ：
# https://github.com/openclaw/openclaw/compare
PR 描述模板：
## 描述
简要描述这个  PR 的⽬的
## 变更类型
- [ ] Bug 修复
- [ ] 新功能
- [ ] ⽂档更新
- [ ] 性能优化
## 检查清单
- [ ] 代码通过测试
- [ ] 添加了必要的⽂档
- [ ] 遵循代码规范
## 关联 Issue
Fixes #123
7.2.2 Discord 社区 参 与
频道结构

--- Page 260 ---

260OpenClaw Discord
├── 📢 announcements    # 官⽅公告
├── 💬 general         # ⼀般讨论
├── ❓ help            # 求助频道
├── 💡 ideas           # 功能建议
├── 🎨 showcase        # 作品展示
├── 🔧 development     # 开发讨论
├── 🤝 contribution    # 贡献协调
└── 🌐 i18n            # 国际化
社区礼仪
## DO（推荐）
✅ 友好和建设性地交流
✅ 分享你的  Skill 和使⽤案例
✅ 帮助回答他⼈的问题
✅ 使⽤搜索功能查找已有讨论
✅ 在正确频道发布内容
## DON'T （避免）
❌ 发送垃圾信息或⼴告
❌ 使⽤攻击性语⾔
❌ 重复提问（先搜索）
❌ 在多个频道重复发帖
❌ 分享敏感信息或密钥
获取帮助

--- Page 261 ---

261## 提问技巧
1. **提供上下⽂ **
   - OpenClaw 版本
   - 操作系统
   - 相关配置
2. **描述问题 **
   - 你想做什么？
   - 实际发⽣了什么？
   - 错误信息是什么？
3. **提供复现步骤 **
   - 最⼩复现示例
   - 相关代码⽚段
## 示例
❌ "我的 Skill 不⼯作，怎么办？ "
✅ "我创建了⼀个  PDF 处理  Skill ，
打包时报错  'Invalid YAML frontmatter' 。
OpenClaw v0.5.2 ， macOS 14 。
SKILL.md 内容： [ 粘贴内容 ]"
7.2.3 Skill 市 场生 态
市场结构
Skill 市场
├── 官⽅ Skills （ Core ）
│   ├── 基础⼯具（ file, web, image ）
│   ├── ⽣产⼒（ calendar, email, notes ）
│   └── 系统集成（ github, notion, feishu ）
│
├── 社区 Skills （ Community ）
│   ├── 已审核（ Verified ）
│   └── 实验性（ Experimental ）
│
└── 第三⽅  Skills （ Third-party ）
    └── 独⽴开发者发布
发布流程
Skill 发布 步 骤：

--- Page 262 ---

2621. 准备阶段
确保  SKILL.md 规 范 完 整
测试所有脚本 功能
准备  README.md （如分 享给他 人）
2. GitHub 发 布（推荐）
   # 创建发布标签
git tag v1.0.0
git push origin v1.0.0
# 在 GitHub 创建  Release
# 上传打包⽂件（如已打包）
3. 分享方式
GitHub 仓 库链接
压缩包下 载
添加到  Awesome OpenClaw 列 表
4. 用户安装
   # ⽅式1 ： Git 克隆
git clone https://github.com/user/my-skill.git ~/.openclaw/skills/my-skill
# ⽅式2 ：下载解压
curl -L https://github.com/user/my-skill/archive/v1.0.0.tar.gz | tar -xz -C 
~/.openclaw/skills/
Skill 评分系 统

--- Page 263 ---

263## 评分维度
| 维度 | 权重  | 说明  |
|------|------|------|
| 下载量 | 25% | 受欢迎程度  |
| 评分 | 30% | ⽤户评分（ 1-5 星） |
| 活跃度 | 20% | 近期更新频率  |
| 质量分 | 25% | ⽂档完整度  + 代码质量  |
## 提升排名技巧
1. 完善⽂档和示例
2. 及时响应⽤户反馈
3. 保持定期更新
4. 添加详细的使⽤说明
7.2.4 社区 贡 献 路 径
新⼿⼊⻔
    ↓
使⽤ OpenClaw → 报告  Bug → 改进⽂档
    ↓
进阶参与
    ↓
开发 Skill → 提交  PR → 审核他⼈贡献
    ↓
核⼼贡献者
    ↓
维护模块 → 指导新⼈  → 参与架构决策
7.3 创业方 向
OpenClaw 不仅是 一 个技 术 工 具 ， 更是 一 个 充满 商 业机会 的 平 台 。 本 节将 探讨 基 于  OpenClaw 的
五大创业方 向 。
7.3.1 方向 一： 垂 直 领 域  AI 代 理服务
市场机会

--- Page 264 ---

264## 痛点分析
传统 SaaS 产品需要⽤户学习复杂界⾯，⽽  AI 代理可以通过⾃然语⾔直接完成任务。
## ⽬标市场
| 领域 | 痛点  | AI 代理价值  |
|------|------|-------------|
| 法律 | 合同审查耗时  | ⾃动审查  + ⻛险提示  |
| 医疗 | 病历整理繁琐  | ⾃动提取  + 结构化  |
| ⾦融 | 报告⽣成重复  | 数据抓取  + ⾃动报告  |
| 电商 | 多平台运营复杂  | ⼀键多平台管理  |
| 教育 | 个性化教学难  | ⾃适应学习路径  |
商业模式
## SaaS 订阅模式
- **基础版 ** ： $29/ ⽉，单⼈使⽤，基础功能
- **专业版 ** ： $99/ ⽉，团队协作，⾼级功能
- **企业版 ** ：定制报价，私有化部署，专属⽀持
## 按需付费模式
- 按处理⽂档数量计费
- 按 API 调⽤次数计费
- 按存储容量计费
实施路线

--- Page 265 ---

265Phase 1 （ 1-3 ⽉）： MVP 开发
├── 确定垂直领域
├── 开发核⼼  Skill
├── 集成 OpenClaw
└── 内测验证
Phase 2 （ 3-6 ⽉）：产品迭代
├── 收集⽤户反馈
├── 完善功能集
├── 优化⽤户体验
└── 建⽴付费转化
Phase 3 （ 6-12 ⽉）：规模扩展
├── 市场推⼴
├── 团队扩张
├── 多领域拓展
└── 融资准备
7.3.2 方向 二 ： Skill 开发工作 室
服务定位
## 服务内容
1. **定制  Skill 开发 **
   - 企业内部系统集成
   - 特定业务⼯作流⾃动化
   - 遗留系统现代化改造
2. **Skill 市场运营 **
   - 开发通⽤  Skills 出售
   - Skill 订阅服务
   - Skill 定制开发
3. **咨询与培训 **
   - OpenClaw 部署咨询
   - Skill 开发培训
   - 团队能⼒建设
定价策略

--- Page 266 ---

266## 服务定价
| 服务类型  | 定价模式  | 参考价格  |
|----------|----------|----------|
| 简单 Skill | 固定价格  | $500-2000 |
| 复杂 Skill | 按⼯时  | $150-300/ ⼩时  |
| 企业培训  | 按天  | $2000-5000/ 天  |
| 咨询服务  | 项⽬制  | $10000+ |
## Skill 销售定价
- **免费版 ** ：基础功能，获客引流
- **专业版 ** ： $9-29/ ⽉，⾼级功能
- **企业版 ** ： $99+/ ⽉， SLA ⽀持
竞争优势
## 核⼼竞争⼒
1. **技术积累 **
   - 丰富的 Skill 开发经验
   - 各领域最佳实践
   - 可复⽤的组件库
2. **快速交付 **
   - 标准化的开发流程
   - 成熟的质量体系
   - 模块化复⽤
3. **持续服务 **
   - ⻓期维护⽀持
   - 版本迭代更新
   - 7x24 技术⽀持
7.3.3 方向三 ： 企 业 级  AI 平 台集 成
解决方案架 构

--- Page 267 ---

267## 企业部署模式
### 模式⼀：云端  SaaS
[客户系统 ] ← → [OpenClaw Cloud] ← → [AI 模型 ]
### 模式⼆：混合部署
[客户内⽹ ] → [OpenClaw Gateway] → [ 加密通道 ] → [AI 模型 ]
### 模式三：私有化部署
[客户数据中⼼ ] → [OpenClaw 私有化 ] → [ 本地 / 私有  AI 模型 ]
目标行业
## ⾼价值⾏业
1. **⾦融⾏业 **
   - 合规报告⾃动⽣成
   - 客户⽂档智能处理
   - ⻛险预警系统
2. **制造业 **
   - 设备维护助⼿
   - 质量检测报告⽣成
   - 供应链智能分析
3. **医疗健康 **
   - 病历智能整理
   - 医学⽂献检索
   - 临床研究助⼿
4. **法律服务 **
   - 合同智能审查
   - 案例检索分析
   - 法律⽂书⽣成
商业化路 径

--- Page 268 ---

268## 收⼊模型
- **软件许可 ** ：年度订阅  $50000-200000
- **实施服务 ** ：项⽬交付  $100000-500000
- **运维⽀持 ** ：年度合同  $30000-100000
- **定制开发 ** ：按需求报价
## 客户获取
1. **直销团队 ** ：⼤客户⼀对⼀跟进
2. **渠道合作 ** ：与系统集成商合作
3. **⾏业展会 ** ：垂直领域展会参展
4. **案例营销 ** ：标杆客户案例推⼴
7.3.4 方向 四 ： AI 教 育 培 训
课程体系
## 课程体系设计
### 初级课程： OpenClaw ⼊⻔
- AI 代理基础概念
- OpenClaw 安装配置
- 基础 Skill 使⽤
- 实战项⽬练习
### 中级课程： Skill 开发
- SKILL.md 规范详解
- 脚本开发实践
- 第三⽅ API 集成
- 调试与优化技巧
### ⾼级课程：企业级应⽤
- ⼤规模部署架构
- 安全与合规
- 性能优化
- 团队管理
交付形式

--- Page 269 ---

269## 产品形态
| 形态 | 价格区间  | 特点  |
|------|----------|------|
| 录播课程  | $49-199 | ⾃学为主，成本低  |
| 直播训练营  | $299-999 | 互动性强，周期短  |
| 企业内训  | $5000-20000 | 定制化，上⻔服务  |
| 认证考试  | $99-299 | 官⽅背书，职业认证  |
市场策略
## 获客渠道
1. **内容营销 **
   - 技术博客
   - 视频教程
   - 免费试听课
2. **社区运营 **
   - Discord 社群
   - 线下 Meetup
   - 技术沙⻰
3. **合作推⼴ **
   - 与培训机构合作
   - 企业 HR 部⻔合作
   - ⾼校合作
7.3.5 方向五 ： AI 代 理 基 础 设 施
技术机会

--- Page 270 ---

270## 基础设施需求
1. **模型服务层 **
   - 多模型路由
   - 负载均衡
   - 成本优化
2. **数据管理层 **
   - 向量数据库
   - 知识库构建
   - 数据管道
3. **安全合规层 **
   - 数据脱敏
   - 访问控制
   - 审计⽇志
4. **监控运维层 **
   - 性能监控
   - 错误追踪
   - 成本分析
产品形态
## 产品矩阵
### 产品⼀： OpenClaw Cloud
托管版 OpenClaw ，免运维，即开即⽤
### 产品⼆： Model Gateway
统⼀管理多供应商  AI 模型，统⼀  API 接⼝
### 产品三： Knowledge Base Service
企业知识库托管服务，⾃动同步更新
### 产品四： Security Gateway
数据安全⽹关，敏感信息检测与脱敏
竞争格局

--- Page 271 ---

271## 市场定位
| ⼚商 | 定位  | OpenClaw 机会  |
|------|------|---------------|
| OpenAI | 模型供应商  | 上层应⽤编排  |
| LangChain | 开发框架  | 企业级封装  |
| Zapier | ⾃动化平台  | AI 原⽣深度集成  |
| ⾃研 | 内部⼯具  | 开源  + 服务  |
7.3.6 创业实施 路 线图
第 1 年：验证与起步
├── Q1：选定⽅向，组建团队
├── Q2：开发  MVP ，获取⾸批⽤户
├── Q3：产品迭代，验证商业模式
└── Q4：规模获客，实现盈亏平衡
第 2 年：增⻓与扩张
├── Q1-Q2 ：产品市场匹配，快速增⻓
├── Q3-Q4 ： A 轮融资，团队扩张
第 3 年：领导地位
├── 成为细分领域领导者
├── 拓展国际市场
└── 战略并购或融资

--- Page 272 ---

2727.3.7 风险提 示与 应 对 策 略
## 主要⻛险
### 1. 技术⻛险
- **⻛险** ： OpenClaw ⽣态尚未成熟， API 可能变更
- **应对** ：保持技术栈灵活性，关注官⽅更新
### 2. 市场⻛险
- **⻛险** ： AI 代理市场教育成本⾼，⽤户接受度不确定
- **应对** ：聚焦痛点明确的垂直领域，提供明确  ROI
### 3. 竞争⻛险
- **⻛险** ：⼤⼚可能推出类似产品，竞争加剧
- **应对** ：构建细分领域壁垒，提供差异化服务
### 4. 合规⻛险
- **⻛险** ： AI 监管政策变化，数据安全要求提⾼
- **应对** ：提前布局合规能⼒，关注政策动向
## 成功关键因素
1. **技术能⼒ ** ：深度掌握  OpenClaw 和  AI 技术
2. **⾏业洞察 ** ：对⽬标领域有深刻理解
3. **执⾏速度 ** ：快速迭代，抢占市场
4. **资⾦⽀持 ** ：充⾜的现⾦流⽀持发展

--- Page 273 ---

2737.3.8 竞品分析与市 场 定位
## 主要竞品对⽐
| 产品/ 框架  | 类型  | 优势  | 劣势  | OpenClaw 差异化  |
|-----------|------|------|------|----------------|
| **LangChain** | 开发框架  | 社区⼤、⽣态成熟  | 学习曲线陡峭、企业⽀持弱  | 更易⽤的 Skill 系统 
|
| **AutoGPT** | ⾃主代理  | 全⾃动执⾏  | 稳定性差、成本⾼  | ⼈机协作更可靠  |
| **Zapier** | ⾃动化平台  | 集成丰富、易⽤  | AI 能⼒有限、灵活性差  | AI 原⽣深度集成  |
| **Microsoft Copilot** | 企业助⼿  | ⼤⼚背书、 Office 集成  | 封闭⽣态、定制化难  | 开源可定制 
|
| **Dify** | AI 应⽤平台  | 可视化强、国内友好  | 侧重⼯作流⾮代理  | Skill ⽣态更开放  |
## 市场空⽩机会
1. **中⼩企业市场 ** ：⼤企业有资源⾃研，中⼩企业需要开箱即⽤⽅案
2. **垂直⾏业深度 ** ：通⽤⼯具难以满⾜特定⾏业需求
3. **私有化部署 ** ：数据敏感型企业需要本地化⽅案
4. **开发者⽣态 ** ：技术⽤户需要可扩展、可定制的平台
## OpenClaw 定位建议
**核⼼定位 ** ：⾯向开发者和企业的开源  AI 代理编排平台
**价值主张 ** ：
- 对开发者：最灵活的  Skill 开发体验
- 对企业：可控的私有化  AI 代理⽅案
- 对创业者：低⻔槛的  AI 应⽤构建平台
7.4 未来展 望
7.4.1 技术 趋势
趋势一：多 模 态能力 增 强

--- Page 274 ---

274## 发展⽅向
1. **视觉理解 **
   - 图像内容识别
   - 图表数据提取
   - UI ⾃动化操作
2. **语⾳交互 **
   - 实时语⾳对话
   - 多语⾔⽀持
   - 情感识别
3. **视频处理 **
   - 视频内容分析
   - ⾃动剪辑⽣成
   - 直播实时处理
## 对 Skill 开发的影响
- Skill 将⽀持多模态输⼊输出
- 新的⼯具类型： image_gen, video_edit
- 更⾃然的交互⽅式
趋势二：自主 代理（ Autonomous Agents ）
## 能⼒演进
Level 1: ⼯具调⽤（当前）
  → 根据⽤户指令调⽤⼯具
Level 2: 任务分解
  → ⾃动将复杂任务分解为⼦任务
Level 3: ⾃主规划
  → ⾃主制定执⾏计划
Level 4: 持续学习
  → 从执⾏中学习优化
Level 5: 完全⾃主
  → 独⽴⽬标设定与执⾏
趋势三：边 缘 计算 与本地部 署

--- Page 275 ---

275## 技术驱动
1. **模型⼩型化 **
   - 7B 参数模型能⼒接近  GPT-4
   - 量化技术降低资源需求
2. **硬件进步 **
   - Apple Silicon NPU
   - NVIDIA Jetson
   - 专⽤ AI 芯⽚
3. **隐私需求 **
   - 数据不出境
   - 本地化合规要求
## OpenClaw 的机遇
- 本地模型管理  Skill
- 边缘设备编排
- 混合云部署⽅案
趋势四： AI 原生 应 用 架 构
## 架构演进
传统架构：
前端 → 后端  API → 数据库
  ↓（添加 AI ）
前端 → 后端  API → AI 服务  → 数据库
AI 原⽣架构：
AI 代理（ Orchestrator ）
  ├─→ ⼯具/ 技能（ Skills ）
  ├─→ 记忆系统（ Memory ）
  ├─→ 规划系统（ Planning ）
  └─→ ⽤户界⾯（ UI ）
OpenClaw 定位：
AI 原⽣应⽤的操作系统
7.4.2 OpenClaw 路 线图
近期目标（ 6个 月 内）

--- Page 276 ---

276## 核⼼功能
- [ ] 图形化  Skill 编辑器
- [ ] 团队协作功能
- [ ] 更丰富的内置  Skills
- [ ] 性能优化与稳定性提升
- [ ] 改进的调试⼯具
## 社区建设
- [ ] 官⽅  Skill 市场上线
- [ ] 认证开发者计划
- [ ] 年度开发者⼤会
- [ ] 多语⾔⽂档完善
中期目标（ 1-2年）
## 技术突破
- [ ] 多模态  Skill ⽀持
- [ ] ⾃主代理能⼒
- [ ] 分布式部署架构
- [ ] 企业级安全特性
- [ ] 实时协作功能
## ⽣态扩展
- [ ] 1000+ 社区  Skills
- [ ] 500+ 认证开发者
- [ ] 100+ 企业客户
- [ ] 全球化社区
长期愿景（ 3-5年）

--- Page 277 ---

277## 平台愿景
成为 AI 代理时代的核⼼基础设施：
1. **技术层⾯ **
   - 最成熟的  AI 代理框架
   - 最强⼤的  Skill ⽣态系统
   - 最⼴泛的企业采⽤
2. **社区层⾯ **
   - 百万开发者社区
   - 活跃的开源贡献
   - 丰富的学习资源
3. **商业层⾯ **
   - ⽀撑数⼗亿美元的商业⽣态
   - 孵化成功的创业公司
   - 创造⼤量就业机会
7.4.3 开发者机会
个人开发者
## 发展路径
1. **Skill 开发者 **
   - 开发热⻔  Skills 获得收⼊
   - 建⽴个⼈技术品牌
   - 积累领域专业知识
2. **AI 顾问 **
   - 帮助企业落地  AI
   - 定制解决⽅案
   - ⾼价值咨询服务
3. **内容创作者 **
   - 技术教程与课程
   - YouTube/ 博客内容
   - 付费社区运营
创业团队

--- Page 278 ---

278## 创业机会
1. **垂直领域产品 **
   - 法律 AI 助⼿
   - 医疗 AI 助⼿
   - ⾦融 AI 助⼿
2. **基础设施服务 **
   - 托管 OpenClaw 服务
   - Skill 开发⼯具
   - AI 安全合规平台
3. **咨询与实施 **
   - 企业数字化转型
   - AI 战略咨询
   - 系统集成服务
7.4.4 行业 影响预测
## 短期（ 1-2 年）：⼯具增强
- 个⼈⽣产⼒提升  30-50%
- 重复性⼯作⾃动化
- 新的 Skill 开发岗位出现
## 中期（ 3-5 年）：流程重构
- 企业业务流程重塑
- 新的组织形态出现
- 部分岗位转型或消失
## ⻓期（ 5-10 年）：范式转移
- AI 代理成为标准⼯作⽅式
- ⼈机协作成为常态
- 全新的商业模式涌现
7.4.5 结语
OpenClaw 代表 的 不 仅 是技 术 的 进 步 ， 更是人机 协 作方式 的 变 革 。 在这个  AI 代 理时 代 ， 我们 每 个
人都有机会成为 变 革 的 推动者 —— 无论是通过开发  Skill 贡 献 社区 ， 还是 基 于  OpenClaw 创 造 商 业 价
值。
未来已来 ， 让我们 共 同 塑 造  AI 代 理 的 明天 。

--- Page 279 ---

279本章小结
本章全面 介 绍了  OpenClaw 生 态 系 统 与 创 业机会 ：
7.1 Skill 开发 指 南：从  SKILL.md 规 范 、 开发 流程 到 测 试 发 布 ， 详 细 阐 述 了如 何创建 高 质量 的
OpenClaw Skills 。
7.2 社区 参与：涵盖  GitHub 贡 献 、 Discord 社区 互 动和  Skill 市 场 生 态 ， 帮 助 开发者 融 入
OpenClaw 社区 。
7.3 创业方 向：分析了 五大 创业方 向 —— 垂 直 领 域  AI 服务 、 Skill 开发工作 室 、 企 业 级 平 台集 成 、
AI 教育培训和 基础 设 施 服务 。
7.4 未来 展望：探讨了多 模 态 、 自主 代 理 、 边 缘 计 算 等技 术 趋 势 ， 以 及  OpenClaw 的 路 线图和行业
影响预测 。
OpenClaw 生 态正在 快 速 发 展 ， 现在正是加入 的 最 佳 时机 。 无论你是开发者 、 创 业者还是技 术爱 好
者，都能在这个生 态 中 找 到 属 于自 己 的 位 置 。
本章完

--- Page 280 ---

280附录
本附录提 供  OpenClaw 的 快 速参考 信息 ， 包 括 完 整配 置示 例 、 常 用 命 令 速 查 、 错 误 代码 对 照 、 资 源
链接和版本 历史 。
A. 完整配 置示 例
A.1 配置文 件位 置
OpenClaw 的主 配 置 文 件 位于 ：
~/.openclaw/openclaw.json
A.2 最小可用 配 置
最简单的 配 置 只需 启 用 一 个通道 ：
{
  "channels": {
    "telegram": {
      "enabled": true,
      "botToken": "${TELEGRAM_BOT_TOKEN}"
    }
  }
}

--- Page 281 ---

281A.3 完整配 置示例
{
  "wizard": {
    "lastRunAt": "2026-02-24T14:43:18.363Z",
    "lastRunVersion": "2026.2.23",
    "lastRunCommand": "onboard",
    "lastRunMode": "local"
  },
  "auth": {
    "profiles": {
      "anthropic:default": {
        "provider": "anthropic",
        "mode": "api_key"
      },
      "openai:default": {
        "provider": "openai",
        "mode": "api_key"
      }
    }
  },
  "models": {
    "mode": "merge",
    "providers": {
      "anthropic": {
        "baseUrl": "https://api.anthropic.com/",
        "api": "anthropic-messages",
        "models": [
          {
            "id": "claude-opus-4-5",
            "name": "Claude Opus",
            "reasoning": true,
            "input": ["text", "image"],
            "cost": {
              "input": 15.0,
              "output": 75.0,
              "cacheRead": 1.5,
              "cacheWrite": 18.75
            },
            "contextWindow": 200000,
            "maxTokens": 4096
          },
          {
            "id": "claude-sonnet-4-5",
            "name": "Claude Sonnet",
            "input": ["text", "image"],

--- Page 282 ---

282            "cost": {
              "input": 3.0,
              "output": 15.0,
              "cacheRead": 0.3,
              "cacheWrite": 3.75
            },
            "contextWindow": 200000,
            "maxTokens": 8192
          }
        ]
      },
      "openai": {
        "baseUrl": "https://api.openai.com/v1",
        "api": "openai-chat",
        "models": [
          {
            "id": "gpt-4o",
            "name": "GPT-4o",
            "input": ["text", "image"],
            "cost": {
              "input": 5.0,
              "output": 15.0
            },
            "contextWindow": 128000,
            "maxTokens": 4096
          }
        ]
      }
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "anthropic/claude-sonnet-4-5"
      },
      "models": {
        "anthropic/claude-sonnet-4-5": {
          "alias": "Claude Sonnet"
        }
      },
      "workspace": "/Users/username/.openclaw/workspace",
      "compaction": {
        "mode": "safeguard"
      },
      "maxConcurrent": 4,
      "subagents": {
        "maxConcurrent": 8

--- Page 283 ---

283      }
    },
    "list": [
      {
        "id": "work-agent",
        "name": " ⼯作助⼿ ",
        "models": {
          "primary": "anthropic/claude-opus-4-5"
        },
        "workspace": "~/.openclaw/workspace-work",
        "tools": {
          "policy": "allow",
          "deny": ["process"]
        }
      },
      {
        "id": "home-agent",
        "name": " 家庭助⼿ ",
        "models": {
          "primary": "openai/gpt-4o"
        },
        "workspace": "~/.openclaw/workspace-home",
        "tools": {
          "policy": "deny",
          "allow": ["message", "calendar", "reminders", "read"]
        }
      }
    ]
  },
  "messages": {
    "ackReactionScope": "group-mentions"
  },
  "commands": {
    "native": "auto",
    "nativeSkills": "auto",
    "restart": true,
    "ownerDisplay": "raw"
  },
  "session": {
    "dmScope": "per-channel-peer"
  },
  "hooks": {
    "internal": {
      "enabled": true,
      "entries": {
        "boot-md": {
          "enabled": true

--- Page 284 ---

284        },
        "bootstrap-extra-files": {
          "enabled": true
        },
        "command-logger": {
          "enabled": true
        },
        "session-memory": {
          "enabled": true
        }
      }
    }
  },
  "channels": {
    "telegram": {
      "enabled": true,
      "botToken": "${TELEGRAM_BOT_TOKEN}",
      "groupPolicy": "open",
      "streaming": true
    },
    "whatsapp": {
      "enabled": true,
      "allowFrom": ["+86138xxxx1234", "+86139xxxx5678"],
      "groupPolicy": "owner-only"
    },
    "discord": {
      "enabled": true,
      "token": "${DISCORD_BOT_TOKEN}",
      "clientId": "${DISCORD_CLIENT_ID}",
      "groupPolicy": "open"
    },
    "feishu": {
      "enabled": true,
      "appId": "${FEISHU_APP_ID}",
      "appSecret": "${FEISHU_APP_SECRET}",
      "domain": "feishu",
      "groupPolicy": "disabled",
      "streaming": true,
      "blockStreaming": true
    }
  },
  "gateway": {
    "port": 18789,
    "mode": "local",
    "bind": "loopback",
    "tailscale": {
      "mode": "off",

--- Page 285 ---

285      "resetOnExit": false
    },
    "nodes": {
      "denyCommands": [
        "camera.snap",
        "camera.clip",
        "screen.record"
      ]
    }
  },
  "skills": {
    "install": {
      "nodeManager": "npm"
    }
  },
  "cron": {
    "jobs": [
      {
        "name": "daily-summary",
        "schedule": "0 20 * * *",
        "command": "agent",
        "args": {
          "prompt": " 总结今天的⽇历事件和待办事项，发送⽇报 "
        }
      },
      {
        "name": "health-check",
        "schedule": "0 */6 * * *",
        "command": "agent",
        "args": {
          "prompt": " 检查系统健康状态，如有异常发送通知 "
        }
      }
    ]
  },
  "webhooks": {
    "github-pr": {
      "path": "/webhook/github/pr",
      "agent": "work-agent",
      "command": "agent",
      "args": {
        "prompt": " 审查这个  PR 的代码变更 "
      }
    },
    "sentry-alert": {
      "path": "/webhook/sentry",
      "command": "agent",

--- Page 286 ---

286      "args": {
        "prompt": " 分析错误报告，判断严重程度，通知相关⼯程师 "
      }
    }
  },
  "plugins": {
    "entries": {
      "feishu": {
        "enabled": true
      }
    }
  },
  "meta": {
    "lastTouchedVersion": "2026.2.23",
    "lastTouchedAt": "2026-02-24T14:43:18.396Z"
  }
}
A.4 配置字段详 解
A.4.1 顶级字段

--- Page 287 ---

287字段 类型说明
wizard Object 向导运行 记录
auth Object 认证配置
models Object 模型提供 商标 识和 配 置
agents Object 代理默认 配 置和多 代 理 列 表
messages Object 消息处理 配 置
commands Object命令系统 配 置
session Object会话管理 配 置
hooks Object 钩子系统 配 置
channels Object通道配置（ Telegram 、 WhatsApp 等）
gateway Object 网关核心 配 置
skills Object技能系统 配 置
cron Object定时任务 配 置
webhooks Object Webhook 端 点 配 置
plugins Object 插件配置
meta Object 元数据（自动生成）
A.4.2 认证 配 置  (auth)
{
  "auth": {
    "profiles": {
      "provider:label": {
        "provider": "anthropic|openai|google|...",
        "mode": "api_key|oauth|..."
      }
    }
  }
}

--- Page 288 ---

288A.4.3 代理 配 置  (agents)
字段 类型 默认值 说明
defaults.model.primary String - 默认主模 型
defaults.workspace String~/.openclaw/workspace默认工作 空间
defaults.compaction.mode Stringsafeguard 会话压缩 模式
defaults.maxConcurrent Number 4最大并发会话
数
defaults.subagents.maxConcurrent Number 8子代理最大 并
发数
list Array -多代理配 置 列
表
A.4.4 网关 配 置  (gateway)
字段 类型 默认值 说明
port Number 18789 网关端口
mode String local 运行模式
bind String loopback 绑定地址
tailscale.mode String off Tailscale 模式
nodes.denyCommands Array [] 禁止的节 点命令
注意：Gateway 认证 通过 环 境 变 量  OPENCLAW_GATEWAY_TOKEN 配置， 而 非配 置 文 件 中的
auth.token。
# 设置 Gateway Token 环境变量
export OPENCLAW_GATEWAY_TOKEN="your-secure-token-here"
# 启动 Gateway
openclaw gateway start

--- Page 289 ---

289A.4.5 通道 配 置  (channels)
Telegram:
{
  "telegram": {
    "enabled": true,
    "botToken": "${TELEGRAM_BOT_TOKEN}",
    "groupPolicy": "open|owner-only|disabled",
    "streaming": true
  }
}
WhatsApp:
{
  "whatsapp": {
    "enabled": true,
    "allowFrom": ["+86138xxxx1234"],
    "groupPolicy": "open|owner-only|disabled"
  }
}
Discord:
{
  "discord": {
    "enabled": true,
    "token": "${DISCORD_BOT_TOKEN}",
    "clientId": "${DISCORD_CLIENT_ID}",
    "guilds": {
      "guild_id_1": {
        "channels": ["channel_id_1", "channel_id_2"]
      },
      "guild_id_2": {
        "channels": ["*"]
      }
    }
  }
}
Feishu:

--- Page 290 ---

290{
  "feishu": {
    "enabled": true,
    "appId": "${FEISHU_APP_ID}",
    "appSecret": "${FEISHU_APP_SECRET}",
    "domain": "feishu|lark",
    "groupPolicy": "open|owner-only|disabled",
    "streaming": true,
    "blockStreaming": true
  }
}
A.4.6 Cron 任务 配 置  (cron)
{
  "cron": {
    "jobs": [
      {
        "name": "job-name",
        "schedule": "0 8 * * *",
        "command": "agent|message|exec",
        "args": {
          "prompt": " 任务描述 "
        }
      }
    ]
  }
}
Schedule 格式遵 循  cron 表 达 式 ：
* * * * *
│ │ │ │ └─ 星期  (0-7, 0 和 7 都是周⽇ )
│ │ │ └─── ⽉份  (1-12)
│ │ └───── ⽇期  (1-31)
│ └─────── ⼩时  (0-23)
└───────── 分钟  (0-59)
常用示例 ：
0 8 * * * - 每天上午  8:00
0 */6 * * * - 每 6 小时
*/15 * * * * - 每 15 分钟

--- Page 291 ---

2910 9 * * 1 - 每周一上午  9:00
B. 常用命令 速 查
B.1 网关 管理
命令 说明 示例
openclaw gateway start启动网关 openclaw gateway start
openclaw gateway stop停止网关 openclaw gateway stop
openclaw gateway status 查看网关状 态 openclaw gateway status
openclaw gateway restart 重启网关 openclaw gateway restart
openclaw gateway health检查网关 健康状 态 openclaw gateway health
B.2 通道 管理
命令 说明 示例
openclaw channels login登录 /连接通道 openclaw channels login telegram
openclaw channels logout断开通道 连接 openclaw channels logout telegram
openclaw channels list 列出已配 置通道 openclaw channels list
openclaw channels status查看通道状 态 openclaw channels status
openclaw status 查看所有通道状 态openclaw status

--- Page 292 ---

292B.3 配置管理
命令 说明 示例
openclaw
configure交互式配
置向导openclaw configure
openclaw config
get获取配置
值openclaw config get channels.telegram.enabled
openclaw config
set设置配置
值openclaw config set agents.defaults.model.primary
anthropic/claude-opus-4-5
openclaw config
unset删除配置
项openclaw config unset cron.jobs
openclaw
onboard初始化设
置向导openclaw onboard
openclaw setup初始化工
作空间openclaw setup
B.4 代理操作
命令 说明 示例
openclaw agent 运行代理 单次回合openclaw agent --message " 你好 "
openclaw agents list 列出所有 代理 openclaw agents list
openclaw agents add 创建新代理 openclaw agents add work-agent
openclaw agents delete 删除代理 openclaw agents delete old-agent
openclaw tui 打开终端 交 互界面openclaw tui

--- Page 293 ---

293B.5 消息发 送
命令 说明 示例
openclaw message
send发送
消息openclaw message send --channel telegram --target
+86138xxxx --message "Hello"
openclaw
sessions列出
会话openclaw sessions
B.6 模型管理
命令 说明 示例
openclaw models list 列出可用 模 型 openclaw models list
openclaw models scan扫描模型提 供 商openclaw models scan
openclaw models add 添加自定义 模 型openclaw models add provider/model-id
B.7 技能 管理
命令 说明 示例
openclaw skills list 列出可用技能 openclaw skills list
openclaw skills check检查技能依 赖 openclaw skills check
openclaw skills info 查看技能详情 openclaw skills info skill-name
ClawHub CLI 命 令（用于技能市 场操 作 ， 推 荐使 用  npx ） ：

--- Page 294 ---

294命令 说明 示例
npx clawhub list 列出已安 装技能 npx clawhub list
npx clawhub search 搜索技能市 场 npx clawhub search "github"
npx clawhub install安装技能 npx clawhub install skill-name
npx clawhub update更新技能 npx clawhub update skill-name
npx clawhub uninstall 卸载技能 npx clawhub uninstall skill-name
B.8 Cron 任务
命令 说明 示例
openclaw cron
list列出定时 任务 openclaw cron list
openclaw cron
add添加定时 任务openclaw cron add --name daily --
schedule "0 8 * * *"
openclaw cron
rm删除定时 任务（ 支持
rm/remove/delete ）openclaw cron rm daily
B.9 Webhook 管 理
命令 说明 示例
openclaw webhooks gmail Gmail Pub/Sub 钩 子openclaw webhooks gmail setup
B.10 调试与 诊断
命令 说明 示例
openclaw doctor 运行诊断检 查 openclaw doctor
openclaw logs 查看日志 openclaw logs --follow
openclaw dashboard 打开控制面板 openclaw dashboard

--- Page 295 ---

295B.11 设备与 节 点
命令 说明 示例
openclaw devices list 列出配对 设备 openclaw devices list
openclaw nodes list 列出节点 openclaw nodes list
openclaw qr 生成配对 二 维 码 openclaw qr
B.12 系统管理
命令 说明 示例
openclaw update status检查更新状 态 openclaw update status
openclaw update 执行更新 openclaw update
openclaw reset 重置配置 openclaw reset
openclaw uninstall 卸载  OpenClaw openclaw uninstall
openclaw --version 显示版本 openclaw --version
B.13 常用 选 项
选项 说明 示例
--dev 开发模式 openclaw --dev gateway start
--profile <name> 使用指定 配 置openclaw --profile work gateway start
--log-level <level> 日志级别 openclaw --log-level debug gateway start
--no-color 禁用颜色 openclaw --no-color status
--help 显示帮助 openclaw --help

--- Page 296 ---

296C. 错误代码对 照表
⚠ 免责声明：以下错误 代码表为社区 整 理 的 参考 信息 ， 非  OpenClaw 官 方 标 准 文 档 内 容 。
OpenClaw 官方主要 使 用  openclaw doctor 命令进行错误 诊断 和 修 复 。 如 遇 问题 ， 建议 优先 运
行 openclaw doctor 或 openclaw doctor --fix 进行排查 。
C.1 网关错 误  (Gateway)
错误代码 错误信息 原因 解决方案
GATEWAY_EADDRINUSE Port already in use 端口被占用更换端口或停止 占 用进 程
GATEWAY_ECONNREFUSED Connection refused网关未启动运行  openclaw
gateway start
GATEWAY_ETIMEDOUT Connection timeout连接超时检查网络 或增加 超 时时间
GATEWAY_EAUTH Authentication failed认证失败检查  token 配 置
GATEWAY_EWS_UPGRADEWebSocket upgrade
failedWebSocket 升 级
失败检查代理 或防 火 墙 设置
C.2 通道错 误  (Channel)
错误代码 错误信息 原因 解决方案
CHANNEL_ENOT_ENABLED Channel not enabled通道未启用在配置中启用通道
CHANNEL_EAUTH Authentication failed 认证失败检查  bot token 或 凭 据
CHANNEL_ECONN Connection failed 连接失败检查网络连接
CHANNEL_ETIMEOUT Request timeout请求超时 重试或检 查 网 络
CHANNEL_ERATE_LIMIT Rate limit exceeded 速率限制 降低请求频率
CHANNEL_EFORBIDDEN Forbidden 权限不足检查  bot 权 限设置

--- Page 297 ---

297C.3 代理错 误  (Agent)
错误代码 错误信息 原因 解决方案
AGENT_EMODEL Model not found 模型不存在检查模型 配 置
AGENT_EAUTH API key invalid API 密钥无 效检查  auth 配 置
AGENT_ERATE_LIMIT Rate limit exceeded 模型请求限制降低请求频率 或更 换模 型
AGENT_ECONTEXT Context too long上下文超长开启会话压 缩 或 新 开会话
AGENT_EMAX_TURNS Max turns exceeded达到最大 轮数简化任务 或 调整配 置
AGENT_EEXEC_DENIED Comm and denied命令被拒绝检查权限 配 置
C.4 配置错 误  (Config)
错误代码 错误信息 原因 解决方案
CONFIG_ENOT_FOUND Config file not found配置文件不 存在运行  openclaw setup
CONFIG_EPARSE Invalid JSON JSON 格式错 误检查配置文 件 语法
CONFIG_EVALIDATION Validation failed 配置验证失 败根据错误信息 修正 配 置
CONFIG_EMISSING_FIELD Required field missing缺少必填 字段补充缺失 的 配 置 项
C.5 工具错 误  (Tools)
错误代码 错误信息 原因 解决方案
TOOL_ENOT_FOUND Tool not found 工具不存在检查工具名 称 或安 装 技能
TOOL_EPERMISSION Permission denied权限不足检查工具权 限 配 置
TOOL_EEXEC Execution failed 执行失败 查看详细错 误信息
TOOL_EINVALID_ARGS Invalid arguments 参数无效检查参数 格式
TOOL_ETIMEOUT Tool execution timeout执行超时增加超时时间 或简 化 任 务

--- Page 298 ---

298C.6 内存错 误  (Memory)
错误代码 错误信息 原因 解决方案
MEMORY_ENOT_FOUND Memory not found记忆不存在检查记忆  ID
MEMORY_ESEARCH Search failed 搜索失败检查向量 存 储状 态
MEMORY_EINDEX Index error 索引错误 运行  openclaw memory reindex
MEMORY_ESTORE Storage error 存储错误检查磁盘 空间和权 限
C.7 HTTP 状 态码
OpenClaw API 返 回 的 标 准  HTTP 状 态码 ：
状态码含义 常见场景
200 OK 请求成功
400 Bad Request 请求参数错 误
401 Unauthorized 认证失败
403 Forbidden 权限不足
404 Not Found 资源不存在
429 Too Many Requests 速率限制
500 Internal Server Error 服务器内部错 误
503 Service Unavailable 服务不可用
C.8 常见错 误 排查
C.8.1 网关无法启 动
# 检查端⼝占⽤
lsof -i :18789
# 强制启动（⾃动释放端⼝）
openclaw gateway start --force

--- Page 299 ---

299C.8.2 通道 连接失 败
# 检查通道状态
openclaw channels status
# 重新登录
openclaw channels logout <channel>
openclaw channels login <channel>
C.8.3 模 型 调用失 败
# 检查模型配置
openclaw models list
# 验证 API 密钥
openclaw config get auth.profiles
# 检查⽹关⽇志
openclaw logs
C.8.4 配 置文 件错 误
# 验证配置
openclaw doctor
# 重置配置（谨慎使⽤）
openclaw reset

--- Page 300 ---

300D. 资源链接 汇 总
D.1 官方资 源
资源 链接 说明
官方网站 https://openclaw.ai 项目主页
官方文档 https://docs.openclaw.ai 完整文档
GitHub 仓 库 https://github.com/openclaw/openclaw 源码仓库
安装指南 https://docs.openclaw.ai/start/installation 安装教程
配置参考 https://docs.openclaw.ai/configuration/overview 配置说明
API 文档 https://docs.openclaw.ai/api API 参考
D.2 社区资 源
资源 链接 说明
Discord 社区 https://discord.gg/clawd 官方  Discord
Reddit https://reddit.com/r/openclaw 官方  Subreddit
Twitter/X https://twitter.com/openclaw 官方推特
技能市场 https://clawhub.com 技能商店
D.3 相关工 具
工具 链接 说明
Home Assistant https://www.home-assistant.io 智能家居 集成
Tailscale https://tailscale.com 安全网络连接
ngrok https://ngrok.com 本地服务暴 露

--- Page 301 ---

301D.4 API 提 供 商
提供商 链接 说明
Anthropic https://console.anthropic.com Claude API
OpenAI https://platform.openai.com GPT API
Google AI https://ai.google.dev Gemini API
Groq https://console.groq.com 快速推理  API
D.5 学习资 源
资源 链接 说明
Awesome OpenClaw https://github.com/hesamsheikh/awesome-openclaw 精选资源
OpenClaw Blog https://openclaw.ai/blog 官方博客
YouTube 频道 https://youtube.com/@openclaw 视频教程
D.6 内部工 具 链接
服务 地址 说明
Gateway API ws://127.0.0.1:18789 WebSocket 网关
Control UI http://127.0.0.1:18789/ui 控制面板
Canvas http://127.0.0.1:18789/canvas 画布服务
Health Endpoint http://127.0.0.1:18789/health 健康检查

--- Page 302 ---

302E. 版本历 史
说明：以下版本 历史 为 示 例 内 容 ， 基 于开发 计 划 整 理 。 实 际 版本 历 史 请 参考  GitHub
Releases。
E.1 版本号说明
OpenClaw 使用  日历版本号（CalVer） 格式 ：YYYY.M.D
例如：2026.2.23 表示  2026 年  2 月  23 日 发 布
E.2 主要版本 历史
2026.2.23 (2026-02-23)
新特性：
新增  Feishu 插 件完 整 支持
新增  feishu_doc、feishu_wiki、feishu_drive、feishu_bitable 工具
改进子代理 并发控 制
优化会话压缩算法
修复：
修复  WhatsApp 群 聊 消 息 处 理问题
修复  Discord 私信 路由 错 误
修复  Cron 任务时区问题
改进：
提升  Gateway 启 动 速 度
优化内存 使用
2026.2.15 (2026-02-15)
新特性：
新增浏览器控制增 强功 能
支持多标 签页 管理
新增  A2UI 交 互协 议

--- Page 303 ---

303修复：
修复部分通道 重 连 问题
修复模型缓 存失 效 问题
2026.2.1 (2026-02-01)
新特性：
新增多代理 支持
新增代理间 路由 功 能
新增技能依 赖 管理
改进：
重构工具 调用系 统
优化错误 处理
2026.1.20 (2026-01-20)
新特性：
新增  Tailscale 集 成
新增设备 配对 功能
新增  iOS 应用 支持
修复：
修复内存 泄 漏问题
修复  Webhook 并 发问题
2026.1.10 (2026-01-10)
新特性：
初始版本发 布
支持  Telegram 、 WhatsApp 、 Discord
基础工具系 统

--- Page 304 ---

304E.3 版本检 查与更 新
# 检查更新
openclaw update status
# 安装更新
openclaw update
# 升级后建议运⾏  doctor 检查配置兼容性
openclaw doctor
E.4 兼容性说明
版本 Node.js 支持平台
2026.2.x ≥ 20.0 macOS, Linux, Windows
2026.1.x ≥ 18.0 macOS, Linux
注意：bun 为实 验性 支持 ， 不推 荐 用于  Gateway 运 行时 。

--- Page 305 ---

305F. 快速启动 脚本
F.1 一键安 装 脚本  (macOS/Linux)
#!/bin/bash
# install-openclaw.sh
echo " 🦞  安装  OpenClaw..."
# 检查 Node.js
if ! command -v node &> /dev/null; then
    echo " ❌  请先安装  Node.js 20+"
    exit 1
fi
# 安装 OpenClaw CLI
npm install -g openclaw
# 初始化配置
openclaw setup
# 启动⽹关
echo " 🚀  启动⽹关 ..."
openclaw gateway start
echo " ✅  安装完成！ "
echo " 📖  访问  http://127.0.0.1:18789/ui 打开控制⾯板 "

--- Page 306 ---

306F.2 Docker Compose 配 置
# docker-compose.yml
version: '3.8'
services:
  openclaw:
    image: openclaw/openclaw:latest
    container_name: openclaw
    ports:
      - "18789:18789"
    volumes:
      - ./openclaw-data:/root/.openclaw
    environment:
      - OPENCLAW_CONFIG=/root/.openclaw/openclaw.json
      - OPENCLAW_GATEWAY_TOKEN=${OPENCLAW_GATEWAY_TOKEN}
    restart: unless-stopped
注意：Docker 部 署时 建议 通过 环 境 变 量  OPENCLAW_GATEWAY_TOKEN 配置网关 认证 。
F.3 Systemd 服务文 件
# /etc/systemd/system/openclaw.service
[Unit]
Description=OpenClaw Gateway
After=network.target
[Service]
Type=simple
User=openclaw
ExecStart=/usr/bin/openclaw gateway start
ExecStop=/usr/bin/openclaw gateway stop
Restart=on-failure
RestartSec=10
Environment="OPENCLAW_GATEWAY_TOKEN=your-secure-token-here"
[Install]
WantedBy=multi-user.target
启用服务 ：

--- Page 307 ---

307sudo systemctl enable openclaw
sudo systemctl start openclaw
sudo systemctl status openclaw
G. 术语表
术语 英文 说明
代理 Agent AI 代理， OpenClaw 的 核 心 执 行 单元
网关 Gateway 消息路由和 代理 管 理 的中 心服务
通道 Channel 聊天平台 连接（ Telegram 、 WhatsApp 等）
技能 Skill 可复用的 功能扩 展包
工具 Tool 代理可调用 的 具体 功 能
记忆 Memory 代理的持久化 存 储 系 统
会话 Session 一次完整 的对话上下文
绑定 Binding用户与代理 的关联 配 置
节点 Node 受网关管理 的 设备
钩子 Hook 事件触发 的回 调机制
Cron Cron 定时任务 调度
Webhook Webhook HTTP 回 调接 口
附录版本: v1.1
适用  OpenClaw 版本: 2026.2.23
最后更新: 2026-02-28