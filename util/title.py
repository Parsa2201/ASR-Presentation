from manim import *
from manim_slides.slide import ThreeDSlide

class TitleUtil:
    def __init__(self, scene):
        self.scene = scene
        self.title = None

    def show(self, text):
        title = Tex(text, font_size=48, color=BLUE).to_edge(UP)

        if self.title is None:
            self.scene.play(Write(title))
        else:
            self.scene.play(ReplacementTransform(self.title, title))

        self.title = title

    def end(self):
        self.scene.play(Unwrite(self.title))
        self.title = None