import os
from fabric.decorators import task
from fabric.api import env
from os.path import join

from recipes import DjangoDeploy

env.project_name = "my_project"
env.project_domain = "my_project.com"
env.base_dir = os.path.realpath(os.path.join(os.path.dirname(env.real_fabfile)))
# env.user = "ubuntu"
env.gunicorn_port = 8888

# env.key_filename = "/tmp/backstaging.pem"
env.host_string = '192.168.33.199'
env.user = "vagrant"
# env.port = '2222'

env.remote_build_path = join('/opt/projetos/', env.project_name)
env.remote_virtualenv_path = join(env.remote_build_path, "virtualenv")
env.remote_app_path = join(env.remote_build_path, 'app')
env.remote_release_path = join(env.remote_app_path, 'releases')
env.remote_current_path = join(env.remote_app_path, 'current')


my_deploy = DjangoDeploy()


@task
def setup():
    my_deploy.setup()


@task
def deploy():
    my_deploy.deploy()