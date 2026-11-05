# Copyright (c) 2025 UrbanComp Lab (https://urbancomp.net) — MIT License
"""
gisclaw.memory
======================
GISClaw 记忆系统。

  ShortTermMemory  — 会话内短期记忆（操作日志 + 中间结果缓存）
  LongTermMemory   — 跨会话长期记忆（持久化知识库）
  MemoryManager    — 统一管理入口
  get_memory()     — 获取全局单例

  MemoryArchive    — 会话快照存档系统（v2.3.0+）
  get_archive()    — 获取全局存档管理器

  VectorSearch     — TF-IDF/神经网络向量语义检索（v2.3.0+）
  get_vector_search() — 获取全局向量搜索实例
"""

from gisclaw.memory.short_term   import ShortTermMemory, MemoryEntry, OperationRecord
from gisclaw.memory.long_term    import LongTermMemory,  LongTermEntry, CATEGORIES
from gisclaw.memory.manager      import MemoryManager,   get_memory, reset_memory
from gisclaw.memory.archive      import MemoryArchive,   ArchiveEntry, get_archive
from gisclaw.memory.vector_search import VectorSearch,   SearchResult, get_vector_search

__all__ = [
    # 短期记忆
    "ShortTermMemory", "MemoryEntry", "OperationRecord",
    # 长期记忆
    "LongTermMemory",  "LongTermEntry", "CATEGORIES",
    # 统一管理
    "MemoryManager",   "get_memory",    "reset_memory",
    # 存档系统 (v2.3.0+)
    "MemoryArchive",   "ArchiveEntry",  "get_archive",
    # 向量检索 (v2.3.0+)
    "VectorSearch",    "SearchResult",  "get_vector_search",
]
