from invoke import task


@task
def nando(c):
    c.run("docker-compose run -d local-setup")
