from graphics import *
import math


def draw_ngon(win, n, radius=100):
    """Draw an n-sided polygon and return the polygon object."""
    angle = 360 / n
    vertices = []

    center_x = 250
    center_y = 250

    for i in range(n):
        x = center_x + radius * math.cos(math.radians(i * angle))
        y = center_y - radius * math.sin(math.radians(i * angle))
        vertices.append(Point(x, y))

    polygon = Polygon(vertices)
    polygon.draw(win)

    return polygon


def inButton(click, button):
    """Return True if the click is inside the button; False otherwise."""
    p1 = button.getP1()
    p2 = button.getP2()

    x = click.getX()
    y = click.getY()

    return (p1.getX() <= x <= p2.getX() and
            p1.getY() <= y <= p2.getY())


def main():
    win = GraphWin("Draw an N-Sided Polygon", 500, 500)
    win.setBackground("white")

    # Entry label and input box
    label = Text(Point(120, 40), "Number of sides:")
    label.draw(win)

    entry = Entry(Point(250, 40), 5)
    entry.setText("5")
    entry.draw(win)

    # Graph button
    button = Rectangle(Point(200, 70), Point(300, 110))
    button.setFill("lightblue")
    button.draw(win)

    button_text = Text(Point(250, 90), "Graph")
    button_text.draw(win)

    # Wait until the user clicks inside the Graph button
    while True:
        click = win.getMouse()

        if inButton(click, button):
            break

    # Read the number of sides and draw the polygon
    try:
        n = int(entry.getText())

        if n < 3:
            Text(Point(250, 140),
                 "Enter at least 3 sides").draw(win)
            win.getMouse()
        else:
            draw_ngon(win, n)

    except ValueError:
        Text(Point(250, 140),
             "Please enter a valid integer").draw(win)
        win.getMouse()

    # Change the button label to Exit
    button_text.setText("Exit")

    # Wait until the user clicks inside the Exit button
    while True:
        click = win.getMouse()

        if inButton(click, button):
            break

    win.close()


if __name__ == "__main__":
    main()