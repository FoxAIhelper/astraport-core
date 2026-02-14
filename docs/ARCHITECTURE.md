# Architecture

## System Design

AstraPort Core follows a modular architecture with clear separation of concerns:

```
┌─────────────┐
│   Main      │ - Entry point and orchestration
└──────┬──────┘
       │
   ┌───┴──────────┬─────────────┬──────────────┐
   ▼              ▼              ▼              ▼
┌──────────┐ ┌──────────┐ ┌──────────────┐ ┌──────────┐
│  Data    │ │  Risk    │ │Diversif.    │ │Prediction│
│Ingestion │ │ Scoring  │ │ Strategy    │ │ Engine   │
└──────────┘ └──────────┘ └──────────────┘ └──────────┘
```

## Module Responsibilities

1. **Data Ingestion**: Handles all external data fetching
   - Stellar network queries
   - Market data APIs
   - Historical price data

2. **Risk Scoring**: Evaluates portfolio risk
   - Volatility calculation
   - Concentration metrics
   - ML-based risk models

3. **Diversification**: Portfolio optimization
   - Asset correlation analysis
   - Allocation suggestions
   - Rebalancing calculations

4. **Prediction**: Future trend forecasting
   - Price forecasting
   - Performance prediction
   - Opportunity identification

## Data Flow

1. Fetch wallet and market data
2. Calculate risk metrics
3. Analyze diversification
4. Make predictions
5. Return comprehensive analysis
