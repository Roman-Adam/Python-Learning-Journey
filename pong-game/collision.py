class Collision:
    """Detect collision of the ball with walls, paddles and edges"""

    WALL_LIMIT = 280
    PADDLE_X = 320
    EDGE_X = 380

    def wall(self, ball):
        return ball.ycor() > self.WALL_LIMIT or ball.ycor() < -self.WALL_LIMIT

    def paddle(self, ball, r_paddle, l_paddle):
        hit_right = ball.distance(r_paddle) < 50 and ball.xcor() > self.PADDLE_X
        hit_left = ball.distance(l_paddle) < 50 and ball.xcor() < -self.PADDLE_X
        return hit_right or hit_left

    def right_miss(self, ball):
        return ball.xcor() > self.EDGE_X

    def left_miss(self, ball):
        return ball.xcor() < -self.EDGE_X
