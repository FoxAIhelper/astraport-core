"""Example: Basic portfolio analysis."""

from main import AstraPortCore


def example_basic_analysis():
    """Demonstrate basic portfolio analysis."""
    # Initialize the engine
    engine = AstraPortCore()
    
    # Example Stellar wallet address
    wallet = "GCXLG46FFQMEMR5WDQVDH3CXLXLCJ3RQWKZFEZXS73FCJMV3EWFSMVL"
    
    # Run analysis
    results = engine.analyze_portfolio(wallet)
    
    print("=== Portfolio Analysis Results ===")
    print(f"Wallet: {results['wallet_address']}")
    print(f"\nRisk Metrics: {results['risk_metrics']}")
    print(f"\nAllocation Suggestions: {results['allocation_suggestions']}")
    print(f"\nPerformance Forecast: {results['performance_forecast']}")


def example_risk_assessment():
    """Demonstrate risk assessment module."""
    from src.risk_scoring import RiskScoring
    
    risk_scorer = RiskScoring()
    
    # Example price history (closing prices)
    prices = [100, 102, 101, 105, 103, 107, 106, 108]
    volatility = risk_scorer.calculate_volatility(prices)
    print(f"Portfolio Volatility: {volatility}")
    
    # Example holdings
    holdings = {
        "USDC": 5000,
        "BTC": 0.5,
        "ETH": 2.5,
        "XLM": 1000,
    }
    concentration = risk_scorer.calculate_concentration_risk(holdings)
    print(f"Concentration Risk: {concentration}")


def example_diversification():
    """Demonstrate diversification module."""
    from src.diversification import Diversification
    
    diversifier = Diversification()
    
    # Get allocation suggestions for different risk profiles
    for profile in ["conservative", "moderate", "aggressive"]:
        allocation = diversifier.suggest_allocation({}, profile)
        print(f"{profile}: {allocation}")


if __name__ == "__main__":
    print("Running AstraPort Core Examples\\n")
    
    print("--- Basic Analysis ---")
    example_basic_analysis()
    
    print("\n--- Risk Assessment ---")
    example_risk_assessment()
    
    print("\n--- Diversification ---")
    example_diversification()
