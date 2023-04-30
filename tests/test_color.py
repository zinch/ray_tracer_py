from core.color import Color

def test_color_components():
    c = Color(0.5, 0.4, 0.7)

    assert c.red == 0.5
    assert c.green == 0.4
    assert c.blue == 0.7

def test_adding_colors():
    c1 = Color(0.9, 0.6, 0.75)
    c2 = Color(0.7, 0.1, 0.25)

    assert c1 + c2 == Color(1.6, 0.7, 1.0)

def test_subtracting_colors():
    c1 = Color(0.9, 0.6, 0.75)
    c2 = Color(0.7, 0.1, 0.25)

    assert c1 - c2 == Color(0.2, 0.5, 0.5)

def test_multiplying_color_by_scalar():
    c = Color(0.2, 0.3, 0.4)
    assert c * 2 == Color(0.4, 0.6, 0.8)

def test_multiplying_colors():
    c1 = Color(1, 0.2, 0.4)
    c2 = Color(0.9, 1, 0.1)

    assert c1 * c2 == Color(0.9, 0.2, 0.04)
