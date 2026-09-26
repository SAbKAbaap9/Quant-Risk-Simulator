#  Quant Risk Simulation

A Monte Carlo-based quantitative finance simulator for evaluating trading strategy performance under uncertainty. The project models thousands of possible trading outcomes to estimate expected returns, risk of ruin, survival probability, drawdowns, and capital growth distributions.

## Features

* Monte Carlo simulation of trading strategies
* Expected Value (EV) analysis
* Risk of Ruin calculation
* Survival Probability estimation
* Maximum Drawdown analysis
* Best and Worst Equity Curve visualization
* Final Capital Distribution histogram
* Configurable trading parameters
* Quantitative risk assessment framework

---

##  Metrics Analyzed

### Expected Profit

Average profit generated across all simulations.

### Average Final Capital

Mean ending portfolio value after all simulated trading paths.

### Survival Probability

Probability that the account remains above the ruin threshold.

### Risk of Ruin

Probability that the account falls below a user-defined ruin level.

### Drawdown Analysis

Measures peak-to-trough declines in portfolio value.

### Percentile Outcomes

* 5th Percentile (Worst-case region)
* 95th Percentile (Best-case region)

---

##  User Inputs

The simulator accepts the following parameters:

| Parameter             | Description                              |
| --------------------- | ---------------------------------------- |
| Initial Capital       | Starting account balance                 |
| Win Rate (%)          | Probability of a winning trade           |
| Risk Reward Ratio     | Reward earned per unit risk              |
| Risk Per Trade (%)    | Fraction of capital risked per trade     |
| Number of Trades      | Trades executed per simulation           |
| Number of Simulations | Total Monte Carlo runs                   |
| Ruin Threshold        | Capital level considered account failure |

---

##  Simulation Process

For each simulation:

1. Start with initial capital.
2. Execute a sequence of trades.
3. Determine trade outcome using the specified win probability.
4. Update capital based on risk and reward parameters.
5. Track drawdowns and account growth.
6. Detect account ruin if capital falls below the threshold.
7. Repeat across thousands of independent simulations.

---

## Visualizations

### Final Capital Distribution

Histogram showing the distribution of ending account values across all simulations.

### Equity Curve Analysis

Comparison of:

* Best-performing simulation
* Worst-performing simulation

This helps visualize variability and risk exposure.

---

##  Technologies Used

* Python
* NumPy
* Matplotlib
* Monte Carlo Simulation
* Probability Theory
* Quantitative Risk Analysis

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/pranny-coder/quant-risk-simulation.git
cd quant-risk-simulation
```

Install dependencies:

```bash
pip install numpy matplotlib
```

Run:

```bash
python simulation.py
```

---

##  Example Input

```text
Initial Capital: 10000
Win Rate (%): 55
Risk Reward Ratio: 1.5
Risk Per Trade (%): 2
Number of Trades: 500
Number of Simulations: 1000
Ruin Threshold Capital: 1000
```

---

##  Example Output

```text
Expected Profit          : 12,850
Average Final Capital    : 22,850
Survival Probability     : 96.40%
Risk Of Ruin             : 3.60%
Average Drawdown         : 18.20%
Worst Drawdown           : 57.40%
```

---

##  Applications

* Quantitative Finance Research
* Trading Strategy Evaluation
* Risk Management
* Portfolio Stress Testing
* Algorithmic Trading Education
* Probability-Based Decision Making

---

##  Future Improvements

* Kelly Criterion Position Sizing
* Value at Risk (VaR)
* Conditional VaR (CVaR)
* Sharpe Ratio & Sortino Ratio
* Geometric Brownian Motion Models
* Multi-Asset Portfolio Simulation
* Streamlit Dashboard
* Historical Market Data Integration

---

## Author

**Ansh Sabhaya**

Computer Science, BITS Pilani Hyderabad Campus

Interested in Quantitative Finance, Machine Learning, Cryptography, and Algorithm Design.
