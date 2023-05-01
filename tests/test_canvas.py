from core.canvas import Canvas, to_ppm_format
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

def test_formatting_as_ppm():
    canvas = Canvas(5, 3)
    canvas.write_pixel(0, 0, Color(1.5, 0, 0))
    canvas.write_pixel(2, 1, Color(0, 0.5, 0))
    canvas.write_pixel(4, 2, Color(-0.5, 0, 1))

    ppm = to_ppm_format(canvas)
    assert ppm == '''
P3
5 3
255
255 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 128 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 255
'''
