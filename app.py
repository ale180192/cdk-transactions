import aws_cdk as cdk
from conf import settings

from cdk_transactions.cdk_transactions_stack import CdkTransactionsStack


REGION = settings.get_value("REGION")
ACCOUNT = settings.get_value("ACCOUNT")

app = cdk.App()

CdkTransactionsStack(app, "CdkTransactionsStack")
app.synth()
