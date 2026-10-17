from graphics import *
import time


def main():
    win = GraphWin("Bouncing Ball", 400, 600)
    win.setBackground("white")

    # Ask for the initial release height
    label = Text(Point(200, 250), "Enter release height in meters:")
    label.draw(win)

    entry = Entry(Point(200, 280), 10)
    entry.setText("10")
    entry.draw(win)

    button = Text(Point(200, 330), "Click to start")
    button.draw(win)

    win.getMouse()

    try:
        height = float(entry.getText())
        if height <= 0:
            raise ValueError
    except ValueError:
        label.setText("Invalid height!")
        entry.undraw()
        button.setText("Click to close")
        win.getMouse()
        win.close()
        return

    entry.undraw()
    label.undraw()
    button.undraw()

    # Map the window coordinates to meters.
    # The bottom of the window (y=0) is the ground.
    win.setCoords(-2, 0, 2, height * 1.2)

    ground = Line(Point(-2, 0), Point(2, 0))
    ground.setWidth(3)
    ground.draw(win)

    ball_radius = height * 0.025
    ball_radius = min(ball_radius, height * 0.1)

    ball = Circle(Point(0, height), ball_radius)
    ball.setFill("red")
    ball.draw(win)

    bounce_height = height
    bounces = 0

    while bounce_height >= 0.001:
        # Ball falls from the top of its bounce to the ground.
        steps = 40
        for i in range(steps + 1):
            y = bounce_height * (1 - i / steps)
            ball.undraw()
            ball = Circle(Point(0, max(y, ball_radius)),
                          ball_radius)
            ball.setFill("red")
            ball.draw(win)
            time.sleep(0.015)

        # Count the bounce and reduce the height by 40%.
        bounces += 1
        bounce_height *= 0.60

        if bounce_height < 0.001:
            break

        # Ball rises to the next, lower bounce height.
        for i in range(steps + 1):
            y = bounce_height * (i / steps)
            ball.undraw()
            ball = Circle(Point(0, max(y, ball_radius)),
                          ball_radius)
            ball.setFill("red")
            ball.draw(win)
            time.sleep(0.015)

    message = Text(Point(0, height * 0.9),
                   "Total bounces: " + str(bounces))
    message.draw(win)

    Text(Point(0, height * 0.8),
         "Click anywhere to close").draw(win)

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()