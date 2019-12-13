from typing import Any
from unittest import TestCase

large = 1000
string = "Napis test"
float = 1.0
broken_int = "To powinna byc liczba calkowita"

# Testy czy zmienne zachowuja im określone z góry typy
assert large > 500
assert type(string) == type("")
assert type(float) == type(1.0)
assert type(broken_int) == type(string)

a = "25"
b = "25"


class RunTest(TestCase):

    def assertEqual(self, first: Any, second: Any, msg: Any = ...) -> None:
        super().assertEqual(first, second, msg)


RunTest.assertEqual(RunTest, "a", "b")
