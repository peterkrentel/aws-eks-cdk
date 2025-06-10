from aws_cdk import (
    Stack,
    aws_eks as eks,
)
from constructs import Construct

class YourProjectStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        eks.Cluster(
            self, "MyEksCluster",
            version=eks.KubernetesVersion.V1_29,
            default_capacity=2,
        )