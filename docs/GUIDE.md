# Documentation

## Getting Started

AstraPort Core is an AI engine that analyzes Stellar wallet portfolios and provides intelligent insights.

### Installation

```bash
pip install -r requirements.txt
```

### Quick Start

```python
from main import AstraPortCore

engine = AstraPortCore()
results = engine.analyze_portfolio("YOUR_STELLAR_ADDRESS")
```

## Modules Overview

### Data Ingestion
Fetches wallet balances and market data from Stellar network and external APIs.

### Risk Scoring
Calculates portfolio volatility, concentration risk, and overall risk metrics using ML models.

### Diversification
Analyzes asset correlation and suggests optimal allocation strategies based on risk profile.

### Prediction
Forecasts asset prices and portfolio performance using time-series models.

## API Reference

See module docstrings in `/src` for detailed API documentation.
