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
        ecs_patterns.ApplicationLoadBalancedFargateService(self, settings.get_id("FargateService"),
            cluster=cluster,
            cpu=512,
            desired_count=6,
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=ecs.ContainerImage.from_registry("amazon/amazon-ecs-sample")
            ),
            memory_limit_mib=2048,
            public_load_balancer=True
        )
        
