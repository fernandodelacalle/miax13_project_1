import pandas as pd
import datetime

df = pd.read_html(
    "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html",
    attrs={'class': "forextable"},
)
df = df[0].iloc[:, [0, 2]]

print(df)

bucket = 'miax13-project-1'
current_date = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
df.to_csv(f"s3://{bucket}/ccy/{current_date}.csv")
