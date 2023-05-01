from core.matrix import Matrix

def test_creating_4x4_matrix():
    m = Matrix((1, 2, 3, 4,
        5.5, 6.5, 7.5, 8.5,
        9, 10, 11, 12,
        13.5, 14.5, 15.5, 16.5))

    assert m(0,0) == 1
    assert m(0,3) == 4
    assert m(1,0) == 5.5
    assert m(1,2) == 7.5
    assert m(2,2) == 11
    assert m(3,0) == 13.5
    assert m(3,2) == 15.5