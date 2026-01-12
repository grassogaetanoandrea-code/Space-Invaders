class Enemy:
    def __init__(
        self,
        x: int,
        y: int,
        speed: int,
        direction: int,
        screen_width: int,
    ):
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction  # 1 = right, -1 = left
        self.screen_width = screen_width
        self.width = 40
        self.drop_distance = 20

    def move(self):
        self.x += self.speed * self.direction

        if self.x <= 0 or self.x >= self.screen_width - self.width:
            self.change_direction_and_drop()

    def change_direction_and_drop(self):
        self.direction *= -1
        self.y += self.drop_distance
