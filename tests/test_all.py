# pylint: disable=redefined-outer-name,invalid-name
import pytest
from testinfra.host import Host


@pytest.fixture(scope="session")
def target_host(request):
    def fn(host, sudo=True):
        return Host.get_host(
            f"ansible://{host}?ansible_inventory={request.config.option.ansible_inventory}",
            sudo=sudo,
        )

    return fn


def test_server_running(target_host):
    host = target_host("drone_web")
    result = host.run("curl localhost:9999/healthz -s")
    assert result.exit_status == 0


def test_worker_running(target_host):
    host = target_host("drone_worker")
    result = host.run("curl localhost:14000/healthz -s")
    assert result.exit_status == 0


def test_data_dir(target_host):
    host = target_host("drone_web")
    assert host.file("/opt/foo/database.sqlite").is_file
