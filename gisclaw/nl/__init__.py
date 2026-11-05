# Copyright (c) 2025 UrbanComp Lab (https://urbancomp.net) — MIT License
"""
gisclaw.nl
==================
自然语言 GIS 操作系统。

  NLProcessor  — 自然语言 → 结构化意图（AI模式 / 规则模式）
  NLExecutor   — 意图 → GIS 函数执行
  GeoAgent     — 多轮对话代理（Processor + Executor 一体化）
  ParsedIntent — 解析意图数据类
"""

from gisclaw.nl.processor import NLProcessor, ParsedIntent
from gisclaw.nl.executor  import NLExecutor, ExecutionResult
from gisclaw.nl.agent     import GeoAgent, ChatMessage

__all__ = [
    "NLProcessor", "ParsedIntent",
    "NLExecutor",  "ExecutionResult",
    "GeoAgent",    "ChatMessage",
]
