# ⚽ Football Team Generator & Exporter API

A robust FastAPI-based backend application that generates rich, randomized football team profiles—complete with tactical squads, managers, stadiums, fan culture, and club identity—and provides multi-format export capabilities (JSON, YAML, and Excel spreadsheets packaged inside a single ZIP archive).

---

## 🚀 Features

* **Procedural Team Generation**: Instantly creates fully realized football clubs with customizable leagues, player rosters, financial budgets, and tactical formations.
* **Comprehensive Data Models**: Powered by Pydantic for strict data validation across:
  * Club Identity, History, and Fan Culture
  * Squad Rosters (Attributes, Overall/Potential ratings, Physical & Technical stats)
  * Management (Manager preferences & styles) and Stadium infrastructure
  * Team Kit Assets
* **Multi-Format Exporters**:
  * **JSON & YAML**: Clean serialization of team overviews, player lists, and asset trees.
  * **Excel (.xlsx)**: Formatted spreadsheets built using openpyxl with multi-sheet breakdowns (*Overview*, *Players*, *Manager & Stadium*, and *Identity & Culture*).
  * **ZIP Archives**: In-memory compression bundling the complete package into a structured directory tree ready for download.
* **Robust Encoding Support**: Handles international character sets (including Cyrillic localization) seamlessly without codec crashes.

---


## 🛠️ Tech Stack

* **Python 3.10+**
* **FastAPI**: Modern, high-performance web framework for building APIs.
* **Pydantic v2**: Data parsing and validation using Python type hints.
* **openpyxl**: Python library to read/write Excel 2010 xlsx/xlsm files.
* **PyYAML**: YAML parsing and emission.

## ⚙️ Quick Start

Clone the repository and navigate to the project directory:

```bash
git clone <your-repository-url>
cd <project-directory>
```

Install dependencies using `uv`:

```bash
uv pip install fastapi uvicorn pydantic openpyxl pyyaml
```

Run the application or development server using `uv run`:

```bash
uv run python -m app.main
```

Or run via uvicorn:

```bash
uv run uvicorn app.main:app --reload
```
