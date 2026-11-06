class Tail:
    """Step 7: Detect collision with tail"""

    def is_collision(self, snake):
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                return True
        return False
