from fabric.api import env, task
from envassert import detect, file, package, port, process, service


@task
def mysql():
    env.platform_family = detect.detect()

    packages = ["holland", "mysql-server"]
    for pkg in packages:
        assert package.installed(pkg)

    assert port.is_listening(3306)
    assert process.is_up("mysqld")

    root_my_cnf = "/root/.my.cnf"
    assert file.exists(root_my_cnf)
    assert file.mode_is(root_my_cnf, 600)
    assert file.owner_is(root_my_cnf, "root")