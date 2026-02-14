"""Unit tests for AstraPort Core modules."""

import pytest
from src.data_ingestion import DataIngestion
from src.risk_scoring import RiskScoring
from src.diversification import Diversification
from src.prediction import Prediction


class TestDataIngestion:
    """Tests for data ingestion module."""

    def setup_method(self):
        """Initialize test fixtures."""
        self.ingestion = DataIngestion()

    def test_fetch_wallet_data(self):
        """Test wallet data fetching."""
        wallet = "GCXLG46FFQMEMR5WDQVDH3CXLXLCJ3RQWKZFEZXS73FCJMV3EWFSMVL"
        data = self.ingestion.fetch_wallet_data(wallet)
        
        assert data["address"] == wallet
        assert "balances" in data

    def test_fetch_market_data(self):
        """Test market data fetching."""
        assets = ["USD", "EUR"]
        data = self.ingestion.fetch_market_data(assets)
        
        assert data["assets"] == assets
        assert "prices" in data


class TestRiskScoring:
    """Tests for risk scoring module."""

    def setup_method(self):
        """Initialize test fixtures."""
        self.risk_scorer = RiskScoring()

    def test_calculate_volatility(self):
        """Test volatility calculation."""
        prices = [100, 102, 101, 105, 103]
        volatility = self.risk_scorer.calculate_volatility(prices)
        
        assert volatility > 0
        assert isinstance(volatility, float)

    def test_calculate_concentration_risk(self):
        """Test concentration risk calculation."""
        holdings = {"USD": 5000, "EUR": 3000, "GBP": 2000}
        risk = self.risk_scorer.calculate_concentration_risk(holdings)
        
        assert 0 <= risk <= 1

    def test_score_portfolio_risk(self):
        """Test portfolio risk scoring."""
        portfolio = {"holdings": {}, "prices": []}
        scores = self.risk_scorer.score_portfolio_risk(portfolio)
        
        assert "volatility_risk" in scores
        assert "concentration_risk" in scores
        assert "overall_risk_score" in scores


class TestDiversification:
    """Tests for diversification module."""

    def setup_method(self):
        """Initialize test fixtures."""
        self.diversifier = Diversification()

    def test_suggest_allocation(self):
        """Test allocation suggestion."""
        allocation = self.diversifier.suggest_allocation({}, "conservative")
        
        assert "stable_assets" in allocation
        assert "growth_assets" in allocation
        assert allocation["stable_assets"] > allocation["growth_assets"]

    def test_suggest_allocation_all_profiles(self):
        """Test allocation for all risk profiles."""
        profiles = ["conservative", "moderate", "aggressive"]
        
        for profile in profiles:
            allocation = self.diversifier.suggest_allocation({}, profile)
            total = sum(allocation.values())
            assert total == 1.0


class TestPrediction:
    """Tests for prediction module."""

    def setup_method(self):
        """Initialize test fixtures."""
        self.predictor = Prediction()

    def test_forecast_asset_price(self):
        """Test asset price forecasting."""
        forecast = self.predictor.forecast_asset_price("USD", 7)
        
        assert forecast["asset"] == "USD"
        assert "forecasts" in forecast
        assert "confidence_lower" in forecast

    def test_predict_portfolio_performance(self):
        """Test portfolio performance prediction."""
        portfolio = {}
        performance = self.predictor.predict_portfolio_performance(portfolio, "month")
        
        assert "expected_return" in performance
        assert "probability_positive" in performance


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
