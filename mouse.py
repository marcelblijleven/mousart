from pynput import mouse


class ClickEvent:
    def __init__(self, x, y, button, pressed):
        self.x = x
        self.y = y
        self.button = button
        self.pressed = pressed

    def __repr__(self) -> str:
        return f'<ClickEvent x: {self.x}, y: {self.y}, button: {self.button}, pressed {self.pressed}>'

    def __str__(self) -> str:
        return f'x: {self.x}, y: {self.y}, button: {self.button}, pressed {self.pressed}'


class ScrollEvent:
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def __repr__(self) -> str:
        return f'<ScrollEvent x: {self.x}, y: {self.y}, dx: {self.dx}, dy: {self.dy}>'

    def __str__(self) -> str:
        return f'x: {self.x}, y: {self.y}, dx: {self.dx}, dy: {self.dy}'


class MouseTracker:
    def __init__(self):
        self.positions: list[tuple[float, float]] = []
        self.scrolls: list[ScrollEvent] = []
        self.clicks: list[ClickEvent] = []
        self.listener = mouse.Listener(
            on_move=self.on_move,
            on_click=self.on_click,
            on_scroll=self.on_scroll
        )

    def start(self) -> None:
        self.listener.start()

    def stop(self) -> None:
        self.listener.stop()

    def on_move(self, x, y) -> None:
        self.positions.append((x, y))

    def on_click(self, x, y, button, pressed) -> None:
        self.clicks.append(ClickEvent(x, y, button, pressed))

    def on_scroll(self, x, y, dx, dy) -> None:
        self.scrolls.append(ScrollEvent(x, y, dx, dy))
