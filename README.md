# Market Risk Dashboard

This dashboard provides real-time market risk indicators including S&P500, VIX, High Yield Spread, and Nasdaq indices.

## Features

- Interactive date range selection
- Real-time market data visualization
- Multiple market indicators
- Responsive layout

## Setup

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Set up your API keys:
   - FRED API key
   - Nasdaq Data Link API key

3. Run the dashboard:
```bash
streamlit run dashboard.py
```

## Data Sources

- S&P500, VIX, and Nasdaq data from Yahoo Finance
- High Yield Spread data from FRED
- Data is delayed by 15-20 minutes

## Note

The dashboard uses delayed market data. The most recent complete trading data is from the previous trading day. 