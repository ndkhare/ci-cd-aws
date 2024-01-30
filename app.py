#!/usr/bin/env python3
import aws_cdk as cdk
from my_ci_cd_pipeline.my_ci_cd_pipeline_stack import MyPipelineStack

app = cdk.App()
MyPipelineStack(app, "MyPipelineStack",
    env=cdk.Environment(account="148240742232", region="us-east-1")
)

app.synth()