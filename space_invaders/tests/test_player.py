from space_invaders.player import Player


def test_player_move_left():
    player = Player(x=50, speed=5)
    player.move_left()
    assert player.x == 45


def test_player_move_right():
    player = Player(x=50, speed=5)
    player.move_right()
    assert player.x == 55
