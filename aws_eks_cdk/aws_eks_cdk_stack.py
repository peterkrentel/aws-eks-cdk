from aws_cdk import (
    Stack,
    aws_eks as eks,
    aws_ec2 as ec2,
)
from constructs import Construct

class AwsEksCdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        # Create VPC for the cluster (required)
        vpc = ec2.Vpc(self, "EksVpc", max_azs=2)

        # Required: explicitly provide the kubectl layer
        kubectl_layer = eks.KubectlLayer(self, "KubectlLayer")

        # Create EKS Cluster
        cluster = eks.Cluster(
            self, "MyEksCluster",
            version=eks.KubernetesVersion.V1_29,
            vpc=vpc,
            kubectl_layer=kubectl_layer,
            default_capacity=2,
            default_capacity_instance_type=ec2.InstanceType("t3.medium"),
        )
