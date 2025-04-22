from decimal import Decimal
import datetime

import pandas as pd
import boto3


def handler(event, context):
    df = pd.read_html(
        "https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html",
        attrs={'class': "forextable"},
    )
    df = df[0].iloc[:, [0, 2]]

    print(df)

    # Save in bucket
    bucket = 'miax13-project-1'
    current_date = datetime.datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    df.to_csv(f"s3://{bucket}/ccy/{current_date}.csv")

    df = df.rename(columns={'Currency': 'ISO_CODE'})

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('CCY')

    records = df.to_dict(orient='records')
    for record in records:
        record['DATE'] = current_date
        record['Spot'] = Decimal(str(record.get('Spot')))
        response = table.put_item(
            Item=record
        )
