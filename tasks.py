from invoke import task


@task
def local_dev(c):
    c.run("docker-compose run -d local-setup")
