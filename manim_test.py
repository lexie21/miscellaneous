#trying manim
from manim import *
class MyScene(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        group = VGroup(square,circle)
        self.play(Create(group))
        self.wait(1)
        self.play(group.animate.scale(2))
        self.wait(1)

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        self.play(Create(circle))

