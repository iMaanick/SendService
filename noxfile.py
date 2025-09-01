import nox

nox.options.default_venv_backend = "uv"
nox.options.reuse_existing_virtualenvs = True


@nox.session(tags=["ci"])
def unit(session: nox.Session):
    session.run("uv", "sync", "--extra", "dev")

    session.run("pytest", "tests")