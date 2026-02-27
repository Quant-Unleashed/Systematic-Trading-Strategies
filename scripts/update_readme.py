import pandas as pd


leaderboard = pd.read_csv("reports/strategy_leaderboard.csv")

table = leaderboard.to_markdown(index=False)

with open("README.md","r") as f:
    readme = f.read()

start = "<!-- LEADERBOARD_START -->"
end = "<!-- LEADERBOARD_END -->"

new_section = f"{start}\n{table}\n{end}"

import re

readme = re.sub(
    f"{start}.*?{end}",
    new_section,
    readme,
    flags=re.S
)

with open("README.md","w") as f:
    f.write(readme)

print("README updated.")
