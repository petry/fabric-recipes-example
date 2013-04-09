from fabric.api import env, task
from recipes.project import ProjectDeploy

my_deploy = ProjectDeploy()


@task
def deploy():
    my_deploy.deploy()


@task
def status():
    my_deploy.status()
