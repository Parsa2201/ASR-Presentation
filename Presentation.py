from manim import *
from manim_slides.slide import ThreeDSlide
import random

from util.slide_number import SlideNumber
from util.table_of_contents import show_toc
from src.asr import ASRSlides

Text.set_default(font="Consolas") 

toc_items = [
    "1. What is ASR?",
]

class Presentation(ThreeDSlide):
    def construct(self):
        t1 = Tex("ASR", font_size=60)
        t2 = Tex("and Whisper", font_size=42).next_to(t1, DOWN, buff=0.5)
        t3 = Tex("Presenter: Parsa Salamatipour", font_size=20).next_to(t2, DOWN, buff=1)
        t4 = Tex("Novavira", font_size=20).next_to(t3, DOWN, buff=0.2)
        title = VGroup(
            t1, t2, t3, t4
        ).move_to(ORIGIN)

        self.play(Write(title))
        self.next_slide()
        self.play(Unwrite(title))

        show_toc(self, toc_items)

        slide_number = SlideNumber(self, slide_count=1)

        asr_slides = ASRSlides(self, slide_number)
        asr_slides.show()

        title = Text("Thanks for watching!", font_size=72)
        title.set_color_by_gradient(BLUE, PURPLE)
        self.play(Write(title), run_time=2)

        self.play(Circumscribe(title, color=WHITE, time_width=0.5, fade_out=True))