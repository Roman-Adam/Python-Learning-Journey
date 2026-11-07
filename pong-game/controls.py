class Controls:
    """Keyboard controls: W/S for left paddle, Up/Down for right paddle"""

    def __init__(self, screen, l_paddle, r_paddle):
        screen.listen()
        screen.onkeypress(r_paddle.go_up, "Up")
        screen.onkeypress(r_paddle.go_down, "Down")
        screen.onkeypress(l_paddle.go_up, "w")
        screen.onkeypress(l_paddle.go_down, "s")
