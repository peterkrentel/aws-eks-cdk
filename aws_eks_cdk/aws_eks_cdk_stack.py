from aws_cdk import (
    Stack,
    aws_eks as eks,
    aws_ec2 as ec2,
)
from constructs import Construct

class AwsEksCdkStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "EksVpc", max_azs=2)

        cluster = eks.Cluster(
            self, "MyEksCluster",
            version=eks.KubernetesVersion.V1_29,
            vpc=vpc,
            default_capacity=0  # No default EC2 nodes
        )

        cluster.add_nodegroup_capacity("DefaultNodeGroup",
            desired_size=2,
            instance_types=[ec2.InstanceType("t3.medium")]
        )
