# Critical Analysis: Advanced Deep Learning in Medical Imaging & Automated Software Engineering

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-ee4c2c?logo=pytorch&logoColor=white)](https://pytorch.org/)
[![YOLOv11](https://img.shields.io/badge/YOLO-v11-00FFFF)](https://github.com/ultralytics/ultralytics)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active_Research-orange)]()

> **HCMUS Master's Degree Project - 2026**
> A comprehensive reproduction, analysis, and critique of state-of-the-art methodologies in Neurodegenerative Disease Detection, Hematology AI, and LLM-based Code Quality Assurance.

---

## 📖 Executive Summary

This repository hosts the source code, experimental notebooks, and presentation materials for the critical analysis of three pivotal papers in the domain of Applied AI. Our mission is to evaluate the robustness, reproducibility, and architectural innovations of these methods.


## 🏗️ Repository Structure

We follow the **Cookiecutter Data Science** structure to ensure reproducibility and maintainability.

```text
.
├── data/                  # Dataset samples (LeukemiaAttri, MRI slices, Code Snippets)
├── docs/                  # Presentation slides, referenced papers, and diagrams
├── notebooks/             # Jupyter Notebooks for exploratory analysis & demos
│   ├── 1.0_alzheimer_fusion_analysis.ipynb
│   ├── 2.0_leukemia_yolo_gcli_demo.ipynb
│   └── 3.0_llm_judge_benchmark.ipynb
├── src/                   # Production-ready source code
│   ├── vision/            # Computer Vision modules (GCLI implementation, VGG Fusion)
│   ├── nlp/               # NLP modules (LLM prompting templates, Metrics logic)
│   └── utils/             # Helper functions (Visualization, Logging)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation