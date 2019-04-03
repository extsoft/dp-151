import pytest
import re
from oct.tests.web.creating_emails import EmailsGeneration


class TestEmailsGeneration:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self) -> None:
        self.email = EmailsGeneration().creating_full_email()

    def test_length_more_then_17(self) -> None:
        assert len(self.email) > 17

    def test_length_less_then_254(self) -> None:
        assert len(self.email) < 254

    def test_find_domain_name(self) -> None:
        assert "@mailinator.com" in self.email

    def test_absence_dot_dog(self) -> None:
        assert ".@" not in self.email

    def test_one_at_character(self) -> None:
        dog_counter = 0
        for iterator in self.email:
            if iterator == "@":
                dog_counter += 1
        assert dog_counter == 1

    def test_absence_com_dot(self) -> None:
        assert "com." not in self.email

    def test_first_symbol_isalpha(self) -> None:
        assert self.email[0].isalpha()

    def test_creating_emails_is_string(self) -> None:
        assert isinstance(EmailsGeneration().creating_full_email(), str)

    def test_emails_pattern(self) -> None:
        random_email = EmailsGeneration().creating_full_email()
        assert random_email == ((re.findall(r"\w{1,7}@\w+.\w+", random_email)).pop(0))

    def test_email_contains_dog(self) -> None:
        assert (EmailsGeneration().creating_full_email().count("@")) == 1

    def test_length_first_part_of_email(self) -> None:
        assert len((EmailsGeneration().creating_full_email().split("@")).pop(0)) == 7

    def test_second_part_of_email(self) -> None:
        assert len((EmailsGeneration().creating_full_email().split(".")).pop(1)) <= 4

    def test_special_symbols_are_absent(self) -> None:
        special_symbols = list(str("!$#%^&*()+=?/," "№;:?*[]{}|"))
        for each_symbol in special_symbols:
            assert each_symbol is not EmailsGeneration().creating_full_email()
