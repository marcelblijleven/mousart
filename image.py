from PIL import Image, ImageDraw

COLORS = {
    'BLACK': (0, 0, 0, 255),
}


class ImageDrawer:
    def __init__(
            self,
            mode: int or str,
            size: tuple[int, int],
            color: int or float
    ):
        self.image = Image.new(mode, size, color)
        self.draw = ImageDraw.Draw(self.image)
        self.size = size

    def draw_line(self, positions: list[tuple[float, float]], fill: int or float, width: int):
        joint = 'curve'  # Rounded edges
        self.draw.line(positions, fill=fill, width=width, joint=joint)

    def draw_image(self):
        pass
