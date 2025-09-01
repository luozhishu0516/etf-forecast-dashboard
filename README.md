# 📈 Harfor CSI Artificial Intelligence Industry ETF Dashboard (515980.SS)

This project showcases my ability to combine **Python for data pipelines** and **Power BI for interactive dashboards**.  
It uses the **Harfor CSI Artificial Intelligence Industry ETF (515980.SS)** and benchmark **CSI 300 Index** to demonstrate stock performance, forecasting features, and dashboard design.

---

## 🚀 Features

### 🔹 Python Data Pipeline
- Fetches historical stock data from Yahoo Finance.
- Saves clean CSV datasets for use in Power BI.
- Includes additional stock/ETF benchmark data.

### 🔹 Power BI Dashboard
- **KPI Cards**: Maximum Close, Minimum Close, Latest Close, Total Volume.  
- **Benchmark Comparison**: ETF (515980.SS) vs CSI 300 Index.  
- **Interactive Filters**: 1 Week, 1 Month, 6 Months, 1 Year, All.  
- **Custom Date Slicer** for flexible exploration.  
- **Forecasting Feature** (ARIMA/Statistical model preview) included as a demonstration of time-series skills.  

---

## 📊 Dashboard Preview

<img width="1931" height="1082" alt="image" src="https://github.com/user-attachments/assets/0e57af21-7cff-4572-ade1-c60af279ec12" />


---

## 📂 Repository Contents
- `forecast.py` → Python script to download & save Yahoo Finance data.  
- `ETF_Dashboard.pbix` → Power BI interactive dashboard.  
- `screenshot.png` → Example dashboard view.  
- `README.md` → This documentation.  

---

## 🔧 Setup Instructions

### 1. Python Data Pipeline
```bash
# Clone repository
git clone https://github.com/yourusername/etf-forecast-dashboard.git
cd etf-forecast-dashboard

# Install dependencies
pip install yfinance pandas matplotlib
