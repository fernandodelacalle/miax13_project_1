import pandas as pd

df = pd.read_html(
    "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html",
    attrs={'class': "forextable"},
)
df = df[0].iloc[:, [0, 2]]

print(df)
