#!/usr/bin/env python3

import aws_cdk as cdk
from eks_cdk_python.eks_cdk_python_stack import EksCdkPythonStack

app = cdk.App()
EksCdkPythonStack(app, "EksCdkPythonStack")

app.synth()
