"""Main entry point for AstraPort Core AI engine."""

import logging
import sys
from typing import Dict, Any

from src.data_ingestion import DataIngestion
from src.risk_scoring import RiskScoring
from src.diversification import Diversification
from src.prediction import Prediction

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class AstraPortCore:
    """Main AI engine for AstraPort portfolio analysis."""

    def __init__(self):
        """Initialize all modules."""
        self.data_ingestion = DataIngestion()
        self.risk_scoring = RiskScoring()
        self.diversification = Diversification()
        self.prediction = Prediction()
        logger.info("AstraPort Core initialized")

    def analyze_portfolio(self, wallet_address: str) -> Dict[str, Any]:
        """
        Perform complete portfolio analysis.

        Args:
            wallet_address: Stellar wallet address to analyze

        Returns:
            Comprehensive portfolio analysis results
        """
        logger.info(f"Starting analysis for wallet: {wallet_address}")
        
        # Step 1: Fetch data
        wallet_data = self.data_ingestion.fetch_wallet_data(wallet_address)
        logger.debug(f"Retrieved wallet data: {wallet_data}")
        
        # Step 2: Score risk
        risk_metrics = self.risk_scoring.score_portfolio_risk(wallet_data)
        logger.debug(f"Risk metrics: {risk_metrics}")
        
        # Step 3: Suggest diversification
        suggestions = self.diversification.suggest_allocation(wallet_data, "moderate")
        logger.debug(f"Allocation suggestions: {suggestions}")
        
        # Step 4: Make predictions
        forecast = self.prediction.predict_portfolio_performance(wallet_data, "month")
        logger.debug(f"Performance forecast: {forecast}")
        
        return {
            "wallet_address": wallet_address,
            "risk_metrics": risk_metrics,
            "allocation_suggestions": suggestions,
            "performance_forecast": forecast,
        }


def main():
    """Main entry point."""
    try:
        engine = AstraPortCore()
        
        # Example wallet analysis
        example_wallet = "GCXLG46FFQMEMR5WDQVDH3CXLXLCJ3RQWKZFEZXS73FCJMV3EWFSMVL"
        results = engine.analyze_portfolio(example_wallet)
        
        logger.info("Analysis complete")
        logger.info(f"Results: {results}")
        
        return 0
    except Exception as e:
        logger.error(f"Error during analysis: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
