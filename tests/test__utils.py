import json

import pytest

from github_manager import utils


@pytest.mark.parametrize(
    "text, colour, expected",
    [
        ("empty", "", f"empty{utils.RESET}"),
        ("red", utils.RED, f"{utils.RED}red{utils.RESET}"),
        ("blue + bold", utils.BLUE + utils.BOLD, f"{utils.BLUE + utils.BOLD}blue + bold{utils.RESET}"),
    ],
)
def test__colour(text: str, colour: str, expected: str):
    assert expected == utils.colour(text, colour)


def test__repr_encoder_can_encode_objects():
    class Foo:
        def __repr__(self) -> str:
            return "awh yeah"

    jsn = json.dumps(
        {"foo": Foo()},
        cls=utils.ReprEncoder,
    )

    assert jsn == '{"foo": "awh yeah"}'
