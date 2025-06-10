from aws_cdk import (
    Stack,
    aws_eks as eks,
    aws_ec2 as ec2,
    aws_lambda as _lambda,
)
from constructs import Construct

class AwsEksCdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        eks.Cluster(
            self, "MyEksCluster",
            version=eks.KubernetesVersion.V1_29,
            kubectl_layer=eks.KubectlLayer(self, "KubectlLayer"),
            default_capacity=2,
            default_capacity_instance=ec2.InstanceType("t3.medium"),
        )