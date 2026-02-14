# AstraPort Core Development Guide

## Setting Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies
pip install -e ".[dev]"
```

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=src

# Run specific test file
pytest tests/test_modules.py
```

## Code Quality

```bash
# Format code with Black
black src/ tests/ main.py

# Lint with Flake8
flake8 src/ tests/ main.py

# Type checking with mypy
mypy src/ main.py
```

## Running the Application

```bash
# Basic execution
python main.py

# With debug logging
export PYTHONPATH=/workspaces/astraport-core
python -c "import logging; logging.basicConfig(level=logging.DEBUG); from main import main; main()"
```

## Running Examples

```bash
python examples/portfolio_analysis.py
```

## Project Structure

```
astraport-core/
├── src/                 # Core modules
│   ├── __init__.py
│   ├── data_ingestion.py
│   ├── risk_scoring.py
│   ├── diversification.py
│   └── prediction.py
├── docs/               # Documentation
│   ├── GUIDE.md
│   └── ARCHITECTURE.md
├── examples/           # Example usage scripts
│   └── portfolio_analysis.py
├── tests/              # Unit tests
│   └── test_modules.py
├── main.py            # Application entry point
├── requirements.txt   # Python dependencies
├── setup.py           # Build configuration
├── pyproject.toml     # Project metadata
├── .gitignore         # Git ignore patterns
└── README.md          # Project overview
```

## Contributing

1. Create a new branch for features/fixes
2. Write tests for new functionality
3. Run quality checks before submitting PR
4. Update documentation as needed
