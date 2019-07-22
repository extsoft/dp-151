import pytest
from mimesis import Person


class TestEmailsGeneration:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self) -> None:
        self.email = Person().email()

    def test_length_more_then_17(self) -> None:
        assert len(self.email) > 17

    def test_length_less_then_254(self) -> None:
        assert len(self.email) < 254

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
        assert isinstance(Person().email(), str)

    def test_email_contains_dog(self) -> None:
        assert (Person().email().count("@")) == 1

    def test_second_part_of_email(self) -> None:
        assert len((Person().email().split(".")).pop(1)) <= 4

    def test_special_symbols_are_absent(self) -> None:
        special_symbols = list(str("!$#%^&*()+=?/," "№;:?*[]{}|"))
        for each_symbol in special_symbols:
            assert each_symbol is not Person().email()
