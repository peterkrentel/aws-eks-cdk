from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_eks as eks,
    aws_iam as iam,
)
from constructs import Construct

class EksCdkPythonStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(self, "EksVpc", max_azs=3)

        cluster_admin = iam.Role(self, "AdminRole",
            assumed_by=iam.AccountRootPrincipal()
        )

        cluster = eks.Cluster(self, "EksCluster",
            vpc=vpc,
            version=eks.KubernetesVersion.V1_27,
            default_capacity=2,
            masters_role=cluster_admin
        )
