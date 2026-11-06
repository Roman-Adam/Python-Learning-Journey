  self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("orange")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-270, 270), random.randint(-270, 270))

    def is_collision(self, snake_head):
        return snake_head.distance(self) < 15
