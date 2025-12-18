from space_invaders.enemy import Enemy


def test_enemy_moves_right():
    enemy = Enemy(x=50, y=0, speed=5, direction=1, screen_width=200)
    enemy.move()
    assert enemy.x == 55


def test_enemy_moves_left():
    enemy = Enemy(x=50, y=0, speed=5, direction=-1, screen_width=200)
    enemy.move()
    assert enemy.x == 45


def test_enemy_changes_direction_at_right_edge():
    enemy = Enemy(x=160, y=0, speed=5, direction=1, screen_width=200)
    enemy.move()
    assert enemy.direction == -1
    assert enemy.y == 20


def test_enemy_changes_direction_at_left_edge():
    enemy = Enemy(x=0, y=0, speed=5, direction=-1, screen_width=200)
    enemy.move()
    assert enemy.direction == 1
    assert enemy.y == 20
