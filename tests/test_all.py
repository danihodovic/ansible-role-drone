import pytest


def test_server_running(host):
    if host.backend.get_hostname() != "drone-web":
        pytest.skip()
    result = host.run("curl localhost/healthz -s")
    assert result.exit_status == 0


def test_worker_running(host):
    if host.backend.get_hostname() != "drone-worker":
        pytest.skip()
    result = host.run("curl localhost:3000/healthz -s")
    assert result.exit_status == 0
