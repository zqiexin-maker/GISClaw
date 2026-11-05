"""
GISClaw
==============
UrbanComp Lab (https://urbancomp.net) 开发的轻量级 Python 地理信息分析工具集。
参考 QGIS Processing Framework 设计，支持空间分析、路网分析、栅格处理与 AI Skill。

版权:
  Copyright (c) 2025 UrbanComp Lab, https://urbancomp.net
  MIT License
"""

__version__     = "3.2.0"
# v3.0.0 (2026-03)  SRE Phase 3：uncertainty_assessor（五维不确定性量化）、
#                   AnalysisMode（exploratory/causal 识别）、ParameterSensitivityHint、
#                   MAUP 风险评估、scale_effects_notes，344 tests 全通过
__author__      = "UrbanComp Lab"
__author_url__  = "https://urbancomp.net"
__license__     = "MIT"
__description__ = "Python GIS Toolkit by UrbanComp Lab"

# 快速导入常用类
from gisclaw.core.layer   import GeoLayer
from gisclaw.core.project import GISClawProject
from gisclaw.memory       import get_memory, MemoryManager
