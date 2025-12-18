from space_invaders.collisions import check_collision

class MockObj:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def test_collision_hit():
    assert check_collision(MockObj(10, 10), MockObj(10, 10)) is True

def test_collision_miss():
    assert check_collision(MockObj(10, 10), MockObj(20, 20)) is False