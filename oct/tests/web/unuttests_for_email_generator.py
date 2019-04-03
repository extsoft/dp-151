# pylint: disable=no-self-use # pyATS-related exclusion
import re
from pyats.aetest import Testcase, test
from oct.tests import run_testcase
from oct.tests.web.creating_emails import EmailsGeneration


class TestsForCreatingEmail(Testcase, EmailsGeneration):
    @test
    def test_creating_emails_is_string(self) -> None:
        assert isinstance(EmailsGeneration().creating_full_email(), str)

    @test
    def test_emails_pattern(self) -> None:
        random_email = EmailsGeneration().creating_full_email()
        assert random_email == ((re.findall(r"\w{1,7}@\w+.\w+", random_email)).pop(0))

    @test
    def test_email_contains_dog(self) -> None:
        assert (EmailsGeneration().creating_full_email().count("@")) == 1

    @test
    def test_length_first_part_of_email(self) -> None:
        assert len((EmailsGeneration().creating_full_email().split("@")).pop(0)) == 7

    @test
    def test_second_part_of_email(self) -> None:
        assert len((EmailsGeneration().creating_full_email().split(".")).pop(1)) <= 4

    @test
    def test_special_symbols_are_absent(self) -> None:
        special_symbols = list(str("!$#%^&*()+=?/," "№;:?*[]{}|"))
        for each_symbol in special_symbols:
            assert not EmailsGeneration().creating_full_email().count(each_symbol)


if __name__ == "__main__":
    run_testcase()
