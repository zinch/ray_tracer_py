from core.canvas import Canvas
from core.color import Color

import pytest

@pytest.fixture
def canvas():
    return Canvas(10, 20)

def test_creating_canvas(canvas):
    assert canvas.width == 10
    assert canvas.height == 20

def test_writing_pixel(canvas):
    red = Color(1, 0, 0)
    canvas.write_pixel(2, 3, red)

    assert canvas.pixel_at(2, 3) == Color(1, 0, 0)
    assert canvas.pixel_at(0, 0) == Color(0, 0, 0)
    assert canvas.pixel_at(9, 19) == Color(0, 0, 0)

