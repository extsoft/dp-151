# pylint: disable=no-self-use # pyATS-related exclusion
import random
import string


class EmailsGeneration:
    def creating_full_email(self) -> str:
        first_part_of_email = str("".join(random.choice(string.ascii_letters) for _ in range(7)))
        return "".join(list(first_part_of_email + "@mailinator.com"))
