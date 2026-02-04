# Critical Analysis: Advanced Deep Learning in Medical Imaging & Automated Software Engineering

[![LaTeX](https://img.shields.io/badge/LaTeX-Project-47A141?logo=latex&logoColor=white)](https://www.latex-project.org/)
[![uv](https://img.shields.io/badge/uv-managed-purple?logo=python&logoColor=white)](https://github.com/astral-sh/uv)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active_Research-orange)]()
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

> **HCMUS Master's Degree Project - 2026**
> A comprehensive reproduction, analysis, and critique of state-of-the-art methodologies in Neurodegenerative Disease Detection, Hematology AI, and LLM-based Code Quality Assurance.

---

## 📖 Executive Summary

This repository hosts the **LaTeX source code** for the critical analysis report and associated Python utilities for asset management (such as PDF extraction). The core of this project is the written analysis found in `latex_playground/`.

## 🏗️ Repository Structure

This project follows a structure designed for Latex-first development with Python support:

```text
.
├── latex_playground/      # ✍️ Main LaTeX Project Source
│   ├── main.tex           # Entry point for the report
│   ├── sections/          # Chapter/Section modules
│   ├── settings/          # Preamble and package configurations
│   ├── bib/               # Bibliography references
│   ├── figures/           # Generated figures
│   └── images/            # Static image assets
├── src/                   # 🐍 Python Support Scripts
│   └── papers_extractor.py # Utility to extract papers from PDFs
├── test/                  # 🧪 Tests & Exploratory Scripts
│   ├── extract_papers.py
│   └── inspect_pdf.py
├── docs/                  # Additional documentation & slides
├── notebooks/             # Data analysis notebooks
├── pyproject.toml         # Python project configuration (uv)
└── uv.lock                # Dependency lockfile
```

## 🚀 Getting Started

This project uses **[uv](https://github.com/astral-sh/uv)** for extremely fast Python package management and virtual environment handling.

### Prerequisites

- **LaTeX Distribution** (TeX Live, MacTeX, or MikTeX)
- **uv** (Install via `curl -LsSf https://astral.sh/uv/install.sh | sh` or `brew install uv`)

### 🐍 Python Environment Setup

We use `uv` to manage dependencies. No manual virtualenv activation is strictly required if you use `uv run`.

1. **Install Dependencies**:
   ```bash
   uv sync
   ```

2. **Run Scripts**:
   Execute Python helper scripts using `uv run` to automatically use the correct environment:
   ```bash
   # Example: Inspect a PDF file
   uv run test/inspect_pdf.py
   ```

### ✍️ Compiling the Report

Navigate to the Latex directory and compile `main.tex`:

```bash
cd latex_playground
# Standard compilation chain
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

*Note: Depending on your editor (VS Code with LaTeX Workshop, Overleaf, TexShop), the build process might be automated.*

## 🛠️ Utilities

The `src/` directory contains helper tools used to process reference materials.
- **`papers_extractor.py`**: A tool to extract specific pages or sections from large proceedings PDFs to organize the `docs/` or `data/` folders.