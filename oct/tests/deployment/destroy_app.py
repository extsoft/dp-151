# pylint: disable=no-self-use # pyATS-related exclusion
# pylint: disable=no-member
# pylint: disable=invalid-name
# pylint: disable=too-many-branches
# pylint: disable=duplicate-code
from pyats.topology import Device
from pyats.aetest import Testcase, test
from requests.exceptions import ConnectTimeout, ReadTimeout
from oct.tests import run_testcase
from oct.tests.deployment.deploy_app import is_deploy_app


class DestroyApp(Testcase):
    @test
    def destroy_app(self, server: Device) -> None:
        try:
            server.connect()
            server.execute("cd oct")
            server.execute("docker-compose down")
            assert is_deploy_app(server, 0)
            server.execute("cd ~")
            server.execute("rm -rf oct")
        except (ConnectTimeout, ReadTimeout):
            self.failed()
        finally:
            server.disconnect()


if __name__ == "__main__":
    run_testcase()
