import sys

from mouse import MouseTracker
from image import COLORS, ImageDrawer


class Mousart:
    def __init__(self):
        self.tracker: MouseTracker = MouseTracker()
        self.file_name: str = ""

    def start(self, file_name: str) -> None:
        self.file_name = file_name
        self.tracker.start()

    def stop(self) -> None:
        self.tracker.stop()

    @property
    def max_x(self) -> int:
        max_position = max([x for x, y in self.tracker.positions])
        return int(max_position + 1)

    @property
    def max_y(self) -> int:
        max_position = max([y for x, y in self.tracker.positions])
        return int(max_position + 1)


def _get_file_name(args: list[str]) -> str:
    if len(args) == 1:
        raise ValueError('no file name provided')

    return args[1]


if __name__ == '__main__':
    output_file = _get_file_name(sys.argv)
    mousart = Mousart()
    mousart.start(output_file)

    input("Press key to stop tracking...")
    mousart.stop()
    image_drawer = ImageDrawer(mode="RGBA", size=(mousart.max_x, mousart.max_y), color=(255, 255, 255, 0))
    image_drawer.draw_line(positions=mousart.tracker.positions, fill=COLORS['BLACK'], width=0)
    image_drawer.image.show()
