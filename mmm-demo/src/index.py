from manim import Scene, Circle, Create, PINK, Square, Transform, PI, FadeOut, BLUE, GREEN, LEFT, RIGHT, Rotate, UP, RED, YELLOW, WHITE, Dot, Line, MathTex, DOWN, Write, Axes
# from manim import *


class CreateCircle(Scene):

    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class SquareToCircle(Scene):

    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square,
                            circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation


class AnimatedSquareToCircle(Scene):

    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(Transform(square,
                            circle))  # transform the square into a circle
        self.play(square.animate.set_fill(
            PINK, opacity=0.5))  # color the circle on screen


class DifferentRotations(Scene):

    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(left_square.animate.rotate(PI),
                  Rotate(right_square, angle=PI),
                  run_time=2)
        self.wait()


# 创造一种新的场景 求抛物线 y = 8x 上与焦点的距离等于 6 的点的坐标。创建一个求解过程
class Parabola(Scene):

    def construct(self):
        # Create a parabola
        parabola = Circle(radius=2, color=YELLOW).shift(UP * 2)
        self.play(Create(parabola))

        # Create the focus point
        focus = Dot(color=RED).shift(UP * 2 + RIGHT * 2)
        self.play(Create(focus))

        # Create the point on the parabola
        point_on_parabola = Dot(color=BLUE).shift(UP * 2 + LEFT * 2)
        self.play(Create(point_on_parabola))

        # Show the distance between the point and the focus
        distance_line = Line(point_on_parabola.get_center(),
                             focus.get_center(),
                             color=GREEN)
        self.play(Create(distance_line))

        # Create the equation of the parabola
        equation = MathTex("y = 8x^2", color=WHITE).shift(DOWN * 2)
        self.play(Write(equation))

        # Create the equation of the parabola
        equation = MathTex("y = 8x^2", color=WHITE).shift(DOWN * 2)
        self.play(Write(equation))


# most common type of asymptotic notation in computer science used to measure worst case complexity
