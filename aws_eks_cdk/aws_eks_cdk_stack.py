from aws_cdk import (
    Stack,
    aws_eks as eks,
    aws_lambda as _lambda,
)
from constructs import Construct

class AwsEksCdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create an EKS cluster
        kubectl_layer = eks.KubectlLayer(self, "KubectlLayer")

        eks.Cluster(
            self, "MyEksCluster",
            version=eks.KubernetesVersion.V1_29,
            default_capacity=2,
            kubectl_layer=kubectl_layer,
            default_capacity_instance=eks.InstanceType("t3.medium"),
        )