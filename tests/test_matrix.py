from core.geom import Point, Vector
from core.matrix import Matrix, IDENTITY_MATRIX
from core.math_util import equal

def test_creating_4x4_matrix():
    values = (1, 2, 3, 4,
        5.5, 6.5, 7.5, 8.5,
        9, 10, 11, 12,
        13.5, 14.5, 15.5, 16.5)
    m = Matrix(values)

    assert m(0,0) == 1
    assert m(0,3) == 4
    assert m(1,0) == 5.5
    assert m(1,2) == 7.5
    assert m(2,2) == 11
    assert m(3,0) == 13.5
    assert m(3,2) == 15.5

    assert m == Matrix(values)

def test_creating_2x2_matrix():
    values = (
        -3, 5,
        1, -2)
    m = Matrix(values)
    assert m(0,0) == -3
    assert m(0,1) == 5
    assert m(1,0) == 1
    assert m(1,1) == -2
    assert m == Matrix(values)
    assert m != Matrix((1, 2, 3, 4))

def test_creating_3x3_matrix():
    values = (
        -3, 5, 0,
        1, -2, -7,
        0, 1, 1)
    m = Matrix(values)
    assert m(0,0) == -3
    assert m(0,1) == 5
    assert m(1,0) == 1
    assert m(1,1) == -2
    assert m == Matrix(values)
    assert m(2,2) == 1

def test_matrix_multiplication():
    A = Matrix((
        1, 2, 3, 4,
        5, 6, 7, 8,
        9, 8, 7, 6,
        5, 4, 3, 2))
    B = Matrix((
        -2, 1, 2, 3,
        3, 2, 1, -1,
        4, 3, 6, 5,
        1, 2, 7, 8))

    C = A * B

    assert C == Matrix((
        20, 22, 50, 48,
        44, 54, 114, 108,
        40, 58, 110, 102,
        16, 26, 46, 42))

def test_multiplication_by_point():
    m = Matrix((
        1, 2, 3, 4,
        2, 4, 4, 2,
        8, 6, 4, 1,
        0, 0, 0, 1))
    p = Point(1, 2, 3)

    new_point = m * p
    assert new_point == Point(18, 24, 33)

def test_multiplication_by_vector():
    m = Matrix((
        1, 2, 3, 4,
        2, 4, 4, 2,
        8, 6, 4, 1,
        0, 0, 0, 1))
    v = Vector(1, 2, 3)

    new_vector = m * v
    assert new_vector == Vector(14, 22, 32)

def test_multiplying_by_identity_matrix():
    m = Matrix((
        0, 1, 2, 4,
        1, 2, 4, 8,
        2, 4, 8, 16,
        4, 8, 16, 32))

    new_matrix = m * IDENTITY_MATRIX

    assert new_matrix == m

def test_multiplying_point_by_identity_matrix():
    p = Point(1, 2, 3)

    new_point = IDENTITY_MATRIX * p

    assert new_point == p

def test_multiplying_vector_by_identity_matrix():
    v = Vector(1, 2, 3)

    new_vector = IDENTITY_MATRIX * v

    assert new_vector == v

def test_transposing_matrix():
    m = Matrix((
        0, 9, 3, 0,
        9, 8, 9, 8,
        1, 8, 5, 3,
        0, 0, 5, 8))

    transposed = m.transpose()

    assert transposed == Matrix((
        0, 9, 1, 0,
        9, 8, 8, 0,
        3, 9, 5, 5,
        0, 8, 3, 8))

def test_calculate_determinant_of_2x2_matrix():
    m = Matrix((
        1, 5,
        -3, 2))

    det = m.determinant()

    assert det == 17

def test_find_submatrix_of_3x3_matrix():
    m = Matrix((
        1, 5, 0,
        -3, 2, 7,
        0, 6, -3))

    submatrix = m.submatrix(0, 2)

    assert submatrix == Matrix((
        -3, 2,
        0, 6))

def test_find_submatrix_of_4x4_matrix():
    m = Matrix((
        -6, 1, 1, 6,
        -8, 5, 8, 6,
        -1, 0, 8, 2,
        -7, 1, -1, 1))

    submatrix = m.submatrix(2, 1)

    assert submatrix == Matrix((
        -6, 1, 6,
        -8, 8, 6,
        -7, -1, 1))

def test_calculating_minor_of_3x3_matrix():
    m = Matrix((
        3, 5, 0,
        2, -1, -7,
        6, -1, 5))

    submatrix = m.submatrix(1, 0)

    assert submatrix.determinant() == 25
    assert m.minor(1, 0) == 25

def test_calculating_cofactor_of_3x3_matrix():
    m = Matrix((
        3, 5, 0,
        2, -1, -7,
        6, -1, 5))

    assert m.minor(0, 0) == -12
    assert m.cofactor(0, 0) == -12

def test_calculate_determinant_of_3x3_matrix():
    m = Matrix((
        1, 2, 6,
        -5, 8, -4,
        2, 6, 4))

    assert m.cofactor(0, 0) == 56
    assert m.cofactor(0, 1) == 12
    assert m.cofactor(0, 2) == -46
    assert m.determinant() == -196

def test_calculate_determinant_of_4x4_matrix():
    m = Matrix((
        -2, -8, 3, 5,
        -3, 1, 7, 3,
        1, 2, -9, 6,
        -6, 7, 7, -9))

    assert m.cofactor(0, 0) == 690
    assert m.cofactor(0, 1) == 447
    assert m.cofactor(0, 2) == 210
    assert m.cofactor(0, 3) == 51
    assert m.determinant() == -4071

def test_invertable_matrix_for_invertability():
    m = Matrix((
        6, 4, 4, 4,
        5, 5, 7, 6,
        4, -9, 3, -7,
        9, 1, 7, -6))

    assert m.determinant() == -2120
    assert m.is_invertible()

def test_noninvertable_matrix_for_invertability():
    m = Matrix((
        -4, 2, -2, -3,
        9, 6, 2, 6,
        0, -5, 1, -5,
        0, 0, 0, 0))

    assert m.determinant() == 0
    assert not m.is_invertible()

def test_calculating_inverse_of_matrix():
    m = Matrix((
        -5, 2, 6, -8,
        1, -5, 1, 8,
        7, 7, -6, -7,
        1, -3, 7, 4))

    assert m.determinant() == 532
    assert m.cofactor(2, 3) == -160
    assert m.cofactor(3, 2) == 105

    inverse = m.inverse()
    assert equal(inverse(3, 2), -160/532)
    assert equal(inverse(2, 3), 105/532)

    assert inverse == Matrix((
        0.21805, 0.45113, 0.24060, -0.04511,
        -0.80827, -1.45677, -0.44361, 0.52068,
        -0.07895, -0.22368, -0.05263, 0.19737,
        -0.52256, -0.81391, -0.30075, 0.30639))

