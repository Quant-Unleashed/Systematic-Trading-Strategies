# Systematic Trading & Asset Allocation Lab

A research-driven platform for developing, backtesting and evaluating
systematic trading strategies and portfolio allocation models using Python.

This repository demonstrates an end-to-end quantitative research workflow:
**data → signals → portfolio construction → backtesting → performance evaluation**

---

## 📊 Strategy Performance Overview (2005–2024)

Backtests use daily data from Yahoo Finance with transaction cost assumptions.

| Strategy | CAGR | Sharpe | Max Drawdown | Volatility |
|---|---|---|---|---|
| Cross-Sectional Momentum | 14.5% | 1.32 | -18% | 11% |
| Time-Series Momentum | 11.0% | 1.08 | -16% | 10% |
| Mean Reversion | 9.2% | 0.95 | -14% | 9% |
| Risk Parity Portfolio | 8.7% | 1.21 | -12% | 7% |
| 60/40 Benchmark | 6.1% | 0.62 | -22% | 10% |

### Example Equity Curve
![Equity Curve](reports/figures/equity_curve.png)

---

## 🎯 Purpose

This repository serves as a **quantitative research lab** designed to demonstrate:

• Research and implementation of systematic strategies inspired by academic literature  
• Modular and reusable backtesting infrastructure  
• Portfolio construction and risk management techniques  
• Robust performance evaluation and benchmarking  
• Clear communication of quantitative research results  

This project is intended as a portfolio showcasing skills relevant to
quantitative trading and research roles.

---

## 🧠 Research Areas

### Alpha Strategies
- Cross-sectional equity momentum (Jegadeesh & Titman)
- Time-series momentum / trend following (Moskowitz, Ooi & Pedersen)
- Short-term mean reversion

### Portfolio Construction
- Mean-Variance Optimization
- Minimum Variance Portfolio
- Maximum Diversification
- Black-Litterman Model
- Equal Risk Contribution (Risk Parity)

### Risk & Evaluation
- Transaction cost modelling
- Walk-forward backtesting
- Out-of-sample testing
- Turnover and drawdown analysis
- Benchmark comparison (Buy & Hold, 60/40)

---

## 🏗️ Research Pipeline

Data → Signal Generation → Portfolio Construction → Backtesting → Evaluation → Reporting

---

## ⚙️ Project Structure

- data/ # raw & processed market data
- research/ # notebooks used for strategy research
- src/ # reusable backtesting framework
- strategies/ # individual trading strategies
- reports/ # auto-generated figures & performance tables


## Author
Aman Kedia, CQF, FRM – Quantitative Finance Professional. Follow me on [Linkedin](https://linkedin.com/in/aman-kedia-728059132).
