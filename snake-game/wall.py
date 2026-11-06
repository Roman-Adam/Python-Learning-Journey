class Wall:
    """Step 6: Detect collision with wall"""

    LIMIT = 290

    def is_collision(self, snake_head):
        return (
            snake_head.xcor() > self.LIMIT
            or snake_head.xcor() < -self.LIMIT
            or snake_head.ycor() > self.LIMIT
            or snake_head.ycor() < -self.LIMIT
        )
