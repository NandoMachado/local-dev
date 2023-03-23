from invoke import task


@task
def local_dev_up(c):
    c.run("docker-compose run -d local-setup")


@task
def local_dev_down(c):
    c.run("docker-compose down -v")
