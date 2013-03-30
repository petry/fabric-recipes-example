import os
from fabric.decorators import task
from fabric.api import env
from fabricdeploy.functions import nginx_setup_server, python_enviroment, gunicorn_setup, \
    create_folder_for_project, upload_project, install_pip_dependancies, gunicorn_deploy, \
    nginx_setup_site, collect_static

from fabricdeploy.fabutils import server_upgrade, puts, install_packages
from os.path import join

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


def instaling_project_dependencies():
    install_packages(
        [
            'git-core',
            'python-virtualenv'
        ]
    )


@task
def setup():
    server_upgrade()
    instaling_project_dependencies()
    nginx_setup_server()
    gunicorn_setup()
    puts('server setup done, running deploy')
    deploy()


@task
def deploy():
    puts("Deploying Project...")
    create_folder_for_project()
    python_enviroment()
    upload_project()
    install_pip_dependancies()
    collect_static()
    gunicorn_deploy()
    nginx_setup_site()