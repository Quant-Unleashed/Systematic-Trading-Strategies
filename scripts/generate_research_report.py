import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

REPORT_DIR = Path("reports")
FIG_DIR = REPORT_DIR / "figures"

FIG_DIR.mkdir(parents=True, exist_ok=True)

leaderboard = pd.read_csv("reports/research_leaderboard.csv")

leaderboard = leaderboard.sort_values("sharpe", ascending=False)

top = leaderboard.head(10)

# Sharpe leaderboard chart
plt.figure()

plt.barh(top["strategy"], top["sharpe"])

plt.gca().invert_yaxis()

plt.title("Top Strategies by Sharpe")

plt.xlabel("Sharpe")

plt.tight_layout()

plt.savefig(FIG_DIR / "top_strategies.png")

plt.close()

# return vs drawdown
plt.figure()

plt.scatter(
    leaderboard["annual_return"],
    leaderboard["max_drawdown"]
)

plt.xlabel("Annual Return")
plt.ylabel("Max Drawdown")

plt.title("Return vs Drawdown")

plt.tight_layout()

plt.savefig(FIG_DIR / "return_vs_drawdown.png")

plt.close()

print("Research report generated")
