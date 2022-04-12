from aws_cdk.aws_ecr_assets import DockerImageAsset, NetworkMode
from os import path
import os

from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns
)
from constructs import Construct

from conf import settings

class CdkTransactionsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        vpc_id = settings.get_id("vpc")
        vpc = ec2.Vpc(self, vpc_id,  max_azs=2)
        cluster = ecs.Cluster(self, settings.get_id("Cluster"), vpc=vpc)
        dirname = os.path.dirname(__file__)
        full_dir = path.join(dirname, "../transactions_backend")
        asset = DockerImageAsset(self, "transactionsImage",
            directory=full_dir,
            network_mode=NetworkMode.HOST
        )
        ecs_patterns.ApplicationLoadBalancedFargateService(self, settings.get_id("FargateService"),
            cluster=cluster,
            cpu=512,
            desired_count=6,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_docker_image_asset(asset=asset)
            ),
            memory_limit_mib=2048,
            public_load_balancer=True
        )
        
