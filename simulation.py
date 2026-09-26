import random
import numpy as np
import matplotlib.pyplot as plt

print("\n===== QUANT RISK SIMULATION =====\n")

INITIAL_CAPITAL = float(
    input("Enter Initial Capital: ")
)

WIN_RATE = float(
    input("Enter Win Rate (%) : ")
) / 100

RISK_REWARD = float(
    input("Enter Risk Reward Ratio (e.g. 1.5): ")
)

RISK_PER_TRADE = float(
    input("Enter Risk Per Trade (%) : ")
) / 100

NUM_TRADES = int(
    input("Enter Number of Trades: ")
)

NUM_SIMULATIONS = int(
    input("Enter Number of Simulations: ")
)

RUIN_THRESHOLD = float(
    input("Enter Ruin Threshold Capital: ")
)


def run_simulation():

    capital = INITIAL_CAPITAL

    equity_curve = [capital]

    peak = capital
    max_drawdown = 0

    for _ in range(NUM_TRADES):

        risk_amount = capital * RISK_PER_TRADE

        if random.random() < WIN_RATE:

            capital += risk_amount * RISK_REWARD

        else:

            capital -= risk_amount

        equity_curve.append(capital)

        peak = max(peak, capital)

        drawdown = (peak - capital) / peak

        max_drawdown = max(max_drawdown, drawdown)

        if capital <= RUIN_THRESHOLD:

            return capital, max_drawdown, True, equity_curve

    return capital, max_drawdown, False, equity_curve


final_capitals = []
drawdowns = []
ruins = []

best_curve = None
worst_curve = None

best_final = -float('inf')
worst_final = float('inf')

for _ in range(NUM_SIMULATIONS):

    final_capital, dd, ruined, curve = run_simulation()

    final_capitals.append(final_capital)

    drawdowns.append(dd)

    ruins.append(ruined)

    if final_capital > best_final:
        best_final = final_capital
        best_curve = curve

    if final_capital < worst_final:
        worst_final = final_capital
        worst_curve = curve


avg_final_capital = np.mean(final_capitals)

expected_profit = (
    avg_final_capital - INITIAL_CAPITAL
)

survival_probability = (
    (NUM_SIMULATIONS - sum(ruins))
    / NUM_SIMULATIONS
) * 100

risk_of_ruin = (
    sum(ruins)
    / NUM_SIMULATIONS
) * 100

average_drawdown = (
    np.mean(drawdowns)
) * 100

worst_drawdown = (
    np.max(drawdowns)
) * 100

median_final = np.median(final_capitals)

percentile_5 = np.percentile(
    final_capitals,
    5
)

percentile_95 = np.percentile(
    final_capitals,
    95
)

print("\n" + "="*60)
print("QUANT RISK ANALYSIS REPORT")
print("="*60)

print(f"Initial Capital          : {INITIAL_CAPITAL:,.2f}")

print(f"Expected Profit          : {expected_profit:,.2f}")

print(f"Average Final Capital    : {avg_final_capital:,.2f}")

print(f"Median Final Capital     : {median_final:,.2f}")

print(f"Best Final Capital       : {best_final:,.2f}")

print(f"Worst Final Capital      : {worst_final:,.2f}")

print(f"Survival Probability     : {survival_probability:.2f}%")

print(f"Risk Of Ruin             : {risk_of_ruin:.2f}%")

print(f"Average Drawdown         : {average_drawdown:.2f}%")

print(f"Worst Drawdown           : {worst_drawdown:.2f}%")

print(f"5th Percentile Outcome   : {percentile_5:,.2f}")

print(f"95th Percentile Outcome  : {percentile_95:,.2f}")

print("="*60)


# Histogram

plt.figure(figsize=(10,6))

plt.hist(
    final_capitals,
    bins=50
)

plt.title(
    "Monte Carlo Distribution of Final Capital"
)

plt.xlabel(
    "Final Capital"
)

plt.ylabel(
    "Frequency"
)

plt.grid(True)

plt.show()


# Best vs Worst Path

plt.figure(figsize=(12,6))

plt.plot(
    best_curve,
    label="Best Simulation"
)

plt.plot(
    worst_curve,
    label="Worst Simulation"
)

plt.title(
    "Best vs Worst Equity Curve"
)

plt.xlabel(
    "Trade Number"
)

plt.ylabel(
    "Capital"
)

plt.legend()

plt.grid(True)

plt.show()