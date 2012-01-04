from fabric.api import *

def production():
    env.hosts = ["184.106.228.246:1195"]
    env.user = "money"


def restart():
    sudo("/etc/init.d/nginx restart")
    sudo("/etc/init.d/apache2 restart")


def virtualenv(command):
    source = "source ~/env/bin/activate && "
    run(source + command)


def run_fwd(command):
    try:
        # catch the port number to pass to ssh
        local('ssh -p %s -A %s@%s "%s"' % (env.port, env.user, env.host, command))
    except ValueError:
        local('ssh -A %s@%s "%s"' % (env.user, env.host, command))


def deploy():
    local("git push")
    run_fwd("cd ~/site && git pull")
    with cd("~/site/moresense"):
        virtualenv("python manage.py migrate spendings")
        virtualenv("python manage.py collectstatic --noinput")
    restart()
