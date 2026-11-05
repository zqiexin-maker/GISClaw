"""
GISClaw 安装配置
UrbanComp Lab (https://urbancomp.net)
支持: pip install . 或 pip install -e .（开发模式）
安装后可用命令: gisclaw
"""

from setuptools import setup, find_packages
from pathlib import Path

long_desc = (Path(__file__).parent / "README.md").read_text(encoding="utf-8") \
    if (Path(__file__).parent / "README.md").exists() else ""

setup(
    name="gisclaw",
    version="3.2.0",
    description="Python GIS 工具集 — 空间分析 · 路网 · 栅格 · AI Skill",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    author="UrbanComp Lab",
    author_email="contact@urbancomp.net",
    url="https://github.com/zqiexin-maker/GISClaw",
    python_requires=">=3.9",
    packages=find_packages(exclude=["tests*", "examples*"]),
    include_package_data=True,
    package_data={
        "gisclaw": ["skills/builtin/*.py", "reasoning/templates/*.yaml", "reasoning/rules/*.yaml"],
        "web": ["index.html"],
    },
    install_requires=[
        "geopandas>=0.14", "shapely>=2.0", "pyproj>=3.5",
        "numpy>=1.24", "pandas>=2.0", "matplotlib>=3.7",
        "click>=8.0", "requests>=2.28", "PyYAML>=6.0",
    ],
    extras_require={
        "full": ["folium>=0.14", "contextily>=1.3", "mapclassify>=2.6",
                 "rasterio>=1.3", "scipy>=1.10", "osmnx>=1.7", "anthropic>=0.25"],
        "web": ["flask>=3.0", "flask-cors>=4.0"],
        "dev":  ["pytest>=7.0", "black", "isort"],
    },
    entry_points={"console_scripts": ["gisclaw=gisclaw.cli:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: GIS",
    ],
)
