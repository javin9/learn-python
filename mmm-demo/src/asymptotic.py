from manim import Scene, MathTex, Axes, Create, Write, RED, GREEN, WHITE, UP, DOWN, RIGHT
class AsymptoticNotation(Scene):
    def construct(self):
        # Title
        title = MathTex(r"\text{Big O Notation}", color=WHITE).shift(UP * 2)
        self.play(Write(title))
        # Create axes and complexity functions
        axes = Axes(x_range=[0, 5], y_range=[0, 25], axis_config={"color": WHITE}).shift(DOWN * 0.5)
        self.play(Create(axes))
        quadratic = axes.plot(lambda x: x**2, color=RED, x_range=[0, 5])
        linear = axes.plot(lambda x: 5*x, color=GREEN, x_range=[0, 5])
        # Labels
        quad_label = MathTex(r"O(n^2)", color=RED).shift(RIGHT * 3 + UP * 1)
        lin_label = MathTex(r"O(n)", color=GREEN).shift(RIGHT * 3 + DOWN * 1)
        # Animation
        self.play(Create(quadratic), Write(quad_label))
        self.play(Create(linear), Write(lin_label))
        # Explanation text
        explanation = MathTex(r"\text{Worst-case time complexity analysis}", color=WHITE).shift(DOWN * 3)
        self.play(Write(explanation))
        self.wait(2)
