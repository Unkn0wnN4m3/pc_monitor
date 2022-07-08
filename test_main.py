import pytest
from main import show_bars, show_usage


@pytest.mark.parametrize("input_a, input_b, expected", [
    (69.69, 40, 40),
    (89.53, 25, 25),
    (34.54, 50, 50),
])
def test_show_bars(input_a, input_b, expected):
    assert len(show_bars(input_a, input_b)) == expected
