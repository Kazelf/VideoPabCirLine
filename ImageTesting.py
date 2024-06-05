from manim import *
from math import *

TexTemplateLibrary


class Image(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-6.5,12.5,3],x_length=4,
            y_range=[-7,13,3],y_length=4.3,
            tips=False
        ).scale(1.3).shift(3.5*RIGHT,1*DOWN)
        pointO = Tex('O').scale(0.5).shift(2*DOWN,2.4*RIGHT)
        self.add(pointO, ax)


        parab = ax.plot(lambda x: (2*x**2+2*x-5), x_range=[-3.5,2.5])
        parab.set_color_by_gradient(RED)
        self.add(parab)

        line = ax.plot(lambda x: x, x_range=[-6,12])
        line.set_color_by_gradient(ORANGE)
        self.add(line)

        def c1(t):
            return (cos(t) +7, sin(t)+10)
        cir1 = ax.plot_parametric_curve(c1, color=BLUE, t_range=[0, 2 * PI])
        self.add(cir1)

        def c2(t):
            return (cos(t) +10, sin(t)+7)
        cir2 = ax.plot_parametric_curve(c2, color=GREEN, t_range=[0, 2 * PI])
        self.add(cir2)

        underhalf_cir1 = ax.plot(
            lambda x: 10-sqrt(1-(x-7) ** 2), x_range=[6,8]
        ).set_color_by_gradient(BLUE)
        self.add(underhalf_cir1)


        #Khai bao valuetracker-------------------------------------------------------
        parabolvt = ValueTracker(0)
        linevt = ValueTracker(0)
        circlevt = ValueTracker(6)
        cir2vt = ValueTracker(10)
        
        #ve cac diem =======================================
        dotM = always_redraw(
            lambda: Dot(color=YELLOW).move_to(
                ax.c2p(parabolvt.get_value(), parab.underlying_function(parabolvt.get_value()))
            )
        ).scale(0.2)

        M_text = Text(r'M').scale(0.4).set_color_by_tex("x",YELLOW)
        M_text.add_updater(lambda x: x.next_to(dotM, UP))

        dotA = always_redraw(
            lambda: Dot(color=YELLOW).move_to(
                ax.c2p(linevt.get_value(), line.underlying_function(linevt.get_value()))
            )
        )
        A_text = Text(r'A').scale(0.4).set_color_by_tex("x",YELLOW)
        A_text.add_updater(lambda x: x.next_to(dotA, UP))

        dotN = always_redraw(
            lambda: Dot(color=YELLOW).move_to(
                ax.c2p(circlevt.get_value(), underhalf_cir1.underlying_function(circlevt.get_value()))
            )
        )
        N_text = Text(r'N').scale(0.4).set_color_by_tex("x",YELLOW)
        N_text.add_updater(lambda x: x.next_to(dotN, UP))

        #ve line======================================================
      
        AM = Line().set_color_by_gradient(PURPLE)
        AM.add_updater(
            lambda mob: mob.put_start_and_end_on(dotA.get_center(), dotM.get_center())
        )

        AN = Line().set_color_by_gradient(PINK)
        AN.add_updater(
            lambda mob: mob.put_start_and_end_on(dotA.get_center(), dotN.get_center())
        )
        #chay ========================================================
        self.add(dotM, M_text, dotA, A_text, dotN, N_text, AM, AN)
        self.play(
            parabolvt.animate.set_value(2.5),
            linevt.animate.set_value(8),
            circlevt.animate.set_value(8),
            run_time = 3
        )
      