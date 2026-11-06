
    def down(self):
        if self.snake.head.heading() != UP:
            self.snake.head.setheading(DOWN)

    def left(self):
        if self.snake.head.heading() != RIGHT:
            self.snake.head.setheading(LEFT)

    def right(self):
        if self.snake.head.heading() != LEFT:
            self.snake.head.setheading(RIGHT)
