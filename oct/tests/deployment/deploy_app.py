# pylint: disable=no-self-use # pyATS-related exclusion
# pylint: disable=no-member
# pylint: disable=invalid-name
# pylint: disable=too-many-branches

import os
from enum import Enum
from pyats.topology import Device
from pyats.aetest import Testcase, test
from pyats.utils.fileutils import FileUtils
from requests.exceptions import ConnectTimeout
from oct.tests import run_testcase


class Status(Enum):
    ON = 2
    OFF = 0


def copy_file_to_server(device: Device) -> None:
    futils = FileUtils(testbed=device.testbed)
    futils.copyfile(
        source=f"{os.path.join(os.getcwd(), 'docker-compose.yaml')}",
        destination=f"scp://{device.connections.main.ip}/home/vagrant/oct",
    )


def is_deploy_app(device: Device, is_run: int) -> bool:
    non_empty_lines_counter = 0
    for iterator in device.execute("docker-compose ps -q"):
        if iterator == "\n":
            non_empty_lines_counter += 1
    return non_empty_lines_counter == is_run


class DeployApp(Testcase):
    @test
    def deploy_app(self, device: Device) -> None:
        try:
            device.connect()
            device.execute("mkdir oct")
            copy_file_to_server(device)
            device.execute("cd oct")
            device.execute(f"APP_HOST={device.connections.main.ip} docker-compose up -d")
            assert is_deploy_app(device, Status.ON.value)
        except ConnectTimeout:
            self.failed()
        finally:
            device.disconnect()


if __name__ == "__main__":
    run_testcase()
