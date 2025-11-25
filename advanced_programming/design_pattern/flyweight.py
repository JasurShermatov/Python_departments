from typing import Dict, Tuple


class Glyph:

    def __init__(self, char: str):
        self.char = char

    def draw(self, position: Tuple[int, int], size: int, color: str) -> None:
        x, y = position
        print(
            f"Draw '{self.char}' at ({x},{y}), size={size}, color={color}, "
            f"glyph_id={id(self)}"
        )

    def __repr__(self) -> str:
        return f"<Glyph char={self.char!r} id={id(self)}>"


class GlyphFactory:

    def __init__(self):
        self._pool: Dict[str, Glyph] = {}

    def get_glyph(self, char: str) -> Glyph:
        if char not in self._pool:
            self._pool[char] = Glyph(char)
        return self._pool[char]

    def pool_size(self) -> int:
        return len(self._pool)

    def debug_pool(self) -> None:
        print("Glyph pool:", list(self._pool.values()))


class Character:

    def __init__(self, glyph: Glyph, position: Tuple[int, int], size: int, color: str):
        self.glyph = glyph
        self.position = position
        self.size = size
        self.color = color

    def render(self) -> None:
        self.glyph.draw(self.position, self.size, self.color)


def example():
    factory = GlyphFactory()

    text = "hello flyweight pattern"
    characters = []

    x = 0
    for ch in text:
        glyph = factory.get_glyph(ch)
        char_obj = Character(glyph, position=(x, 0), size=12, color="black")
        characters.append(char_obj)
        x += 8

    for c in characters:
        c.render()

    print()
    factory.debug_pool()
    print("Total Character objects:", len(characters))
    print("Total distinct Glyph objects (pool size):", factory.pool_size())


if __name__ == "__main__":
    example()