from manim import *
from manim_slides.slide import ThreeDSlide

from util.slide_number import SlideNumber
from util.title import TitleUtil

class IntroductionSlides:
    def __init__(self, scene: ThreeDSlide, slide_number: SlideNumber):
        self.scene = scene
        self.slide_number = slide_number

    def what_is_asr(self):
        pass