from manim import *
from math import *

config.tex_template.add_to_preamble("\\usepackage{pifont}")

class Video1(Scene):
    def construct(self):
        import manimpango

        #Debai----------------------------------------

        defaultfont = 26

        debai1 = Text(
            text= 'Cho các số phức  z, w, u thỏa mãn',
            font='Times New Roman',
            slant=ITALIC,
            font_size=defaultfont
        ).to_corner(UL).shift(0.2*UP)
        self.play(Write(debai1))

        debai2 = Tex(
            r'$|z-4+2i|=|2z+\overline{z}|, \ \dfrac{w-8-10i}{w-6-10i}$'
        ).scale(0.7).next_to(debai1)
        self.play(Write(debai2))

        debai3 = Text(
            text= 'thuần ảo,',
            font='Times New Roman',
            slant=ITALIC,
            font_size=defaultfont
        ).next_to(debai2)
        self.play(Write(debai3), run_time = 0.5)

        debai4 = Tex(
            r'$|u+1-2i|=|u-2+i|.$'
        ).scale(0.7).to_corner(UL).shift(0.45*DOWN)
        self.play(Write(debai4), run_time = 0.5)

        debai5 = Text(
            text= 'Giá trị nhỏ nhất của biểu thức ',
            font='Times New Roman',
            slant=ITALIC,
            font_size=defaultfont
        ).next_to(debai4).shift(0.05*UP)
        self.play(Write(debai5))

        debai6 = Tex(
            r'$T=|u-z|+|\overline{u}-\overline{w}|$'
        ).scale(0.7).next_to(debai5).shift(0.05*DOWN)
        self.play(Write(debai6))

        debai7 = Text(
            text= 'thuộc',
            font='Times New Roman',
            slant=ITALIC,
            font_size=defaultfont
        ).next_to(debai6)
        self.play(Write(debai7), run_time = 0.5)

        dapanA=Tex(r'$A.(0;5]$').scale(0.7).to_corner(LEFT).shift(2.4*UP)
        self.play(Write(dapanA), run_time = 0.75)
        dapanB=Tex(r'$B.(5;8)$').scale(0.7).shift(2.4*UP,2*LEFT)
        self.play(Write(dapanB), run_time = 0.75)
        dapanC=Tex(r'$C.[8;10)$').scale(0.7).shift(2.4*UP,2*RIGHT)
        self.play(Write(dapanC), run_time = 0.75)
        dapanD=Tex(r'$D.[10;+\infty)$').scale(0.7).shift(2.4*UP,6*RIGHT)
        self.play(Write(dapanD), run_time = 0.75)

        self.wait(5)

        solution=Text(
            text="Lời giải: Vu Dinh Thai",
            font = "Times New Roman",
            color= YELLOW,
            weight=BOLD,
            slant=ITALIC
        ).scale(0.5).shift(2*UP)
        self.play(Write(solution))
        self.wait(2)

        #Loi giai duoi day la loi giai-------------------------
        dkz1 = MathTex(
            r'\bullet \ \ |z-4+2i|=|2z+\overline{z}|'
        ).scale(0.7).to_corner(LEFT).shift(1.65*UP)
        self.play(Write(dkz1))
        self.wait(2)

        dkz2 = MathTex(
            r'\bullet \ \ |z-4+2i|^2-|2z+\overline{z}|^2=0'
        ).scale(0.7).to_corner(LEFT).shift(1.65*UP)
        self.play(Transform(dkz1,dkz2))
        self.wait(2)

        CALC1 = Tex(
            r'CALC z=100+0,01i  $\Rightarrow VT=$'
        ).scale(0.7).to_corner(LEFT).shift(1.2*UP)
        self.play(Write(CALC1))

        DichsoZ_1 = MathTex(
            r'80779,96'
        ).scale(0.7).next_to(CALC1)
        self.play(Write(DichsoZ_1))

        DichsoZ_2 = Tex(
            r'8 \ \ 07 \ \ 79, \ \ 96'
        ).scale(0.7).next_to(CALC1)
        self.play(Transform(DichsoZ_1, DichsoZ_2))
        self.wait(1)

        DichsoZ_3 = MathTex(
            r'8 \ \ \ \ 8 \ \ -20 \ -4'
        ).scale(0.7).shift(0.8*UP,0.7*LEFT)
        self.play(Write(DichsoZ_3))
        self.wait(2)
        
        DichsoZ_4 = MathTex(
            r'8x^2+8x-20-4y=0'
        ).scale(0.7).shift(0.8*UP,0.1*LEFT)
        self.play(Transform(DichsoZ_3, DichsoZ_4))
        self.wait(2)

        z = MathTex(
            r'\Rightarrow (P): y = 2x^2+2x-5'
        ).scale(0.7).shift(0.3*UP)
        z.set_color_by_tex("x", RED)
        self.play(Write(z))
        self.wait(2)

        dkw1 = MathTex(
            r'\bullet \ \  (w-8-10i)(\overline{w}-6+10i)'
        ).scale(0.7).to_corner(LEFT).shift(0.3*DOWN)
        self.play(Write(dkw1))

        dkw1text = Text(
            text= 'thuần ảo',
            font='Times New Roman',
            slant=ITALIC,
            font_size=defaultfont
        ).next_to(dkw1).shift(0.075*UP)
        self.play(Write(dkw1text), run_time = 0.5)
        self.wait(5)

        dkw2 = MathTex(
            r'\xrightarrow{\text{w=x+yi}} [ \ (x-8)+(y-10)i \ ] \ \cdot [ \ (x-6)-(y-10)i \ ] '
        ).scale(0.7).to_corner(LEFT).shift(0.8*DOWN)
        self.play(Write(dkw2), run_time = 1.5)

        dkw2text = Text(
            text= 'thuần ảo',
            font='Times New Roman',
            slant=ITALIC,
            font_size=defaultfont
        ).next_to(dkw2)
        self.play(Write(dkw2text), run_time = 0.5)
        self.wait(3)

        dkw3 = MathTex(
            r'\Leftrightarrow (x-8)(x-6)+(y-10)^2=0 '
        ).scale(0.7).to_corner(LEFT).shift(1.4*DOWN)
        self.play(Write(dkw3))
        self.wait(1)

        w = MathTex(
            r'\Leftrightarrow (C): (x-7)^2+(y-10)^2=1 '
        ).scale(0.7).next_to(dkw3)
        w.set_color_by_tex("x", BLUE)
        self.play(Write(w))
        self.wait(2)

        dku1 = MathTex(
            r'\bullet \ \ |u+1-2i|=|u-2+i|'
        ).scale(0.7).to_corner(LEFT).shift(2*DOWN)
        self.play(Write(dku1))
        self.wait(2)

        dku2 = MathTex(
            r'\xrightarrow{\text{u=x+yi}} '
        ).scale(0.7).next_to(dku1).shift(0.05*UP)
        self.play(Write(dku2))

        u = MathTex(
            r'(d): y=x '
        ).scale(0.7).next_to(dku2).shift(0.1*DOWN)
        u.set_color_by_tex("x", ORANGE)
        self.play(Write(u))
        self.wait(10)

        #Xoa Scene1------------------------
        self.play(
            FadeOut(dkz1),FadeOut(CALC1),
            FadeOut(DichsoZ_1),FadeOut(DichsoZ_3),
            FadeOut(z),
            FadeOut(dkw1),FadeOut(dkw1text),
            FadeOut(dkw2),FadeOut(dkw2text),
            FadeOut(dkw3),FadeOut(w),
            FadeOut(dku1),FadeOut(dku2),
            FadeOut(u)
        )
        self.wait(1)

class Graph(Scene):
    def construct(self):
        import manimpango
        defaultfont = 26

        #Debai----------------------------------------------------------------
        defaultfont = 26
        debai1 = Text(
            text= 'Cho các số phức  z, w, u thỏa mãn',
            font='Times New Roman',
            slant=ITALIC,
            font_size=defaultfont
        ).to_corner(UL).shift(0.2*UP)
        self.add(debai1)
        debai2 = Tex(
            r'$|z-4+2i|=|2z+\overline{z}|, \ \dfrac{w-8-10i}{w-6-10i}$'
        ).scale(0.7).next_to(debai1)
        self.add(debai2)
        debai3 = Text(
            text= 'thuần ảo,',
            font='Times New Roman',
            slant=ITALIC,
            font_size=defaultfont
        ).next_to(debai2)
        self.add(debai3)
        debai4 = Tex(
            r'$|u+1-2i|=|u-2+i|.$'
        ).scale(0.7).to_corner(UL).shift(0.45*DOWN)
        self.add(debai4)
        debai5 = Text(
            text= 'Giá trị nhỏ nhất của biểu thức ',
            font='Times New Roman',
            slant=ITALIC,
            font_size=defaultfont
        ).next_to(debai4).shift(0.05*UP)
        self.add(debai5)
        debai6 = Tex(
            r'$T=|u-z|+|\overline{u}-\overline{w}|$'
        ).scale(0.7).next_to(debai5).shift(0.05*DOWN)
        self.add(debai6)
        debai7 = Text(
            text= 'thuộc',
            font='Times New Roman',
            slant=ITALIC,
            font_size=defaultfont
        ).next_to(debai6)
        self.add(debai7)
        dapanA=Tex(r'$A.(0;5]$').scale(0.7).to_corner(LEFT).shift(2.4*UP)
        self.add(dapanA)
        dapanB=Tex(r'$B.(5;8)$').scale(0.7).shift(2.4*UP,2*LEFT)
        self.add(dapanB)
        dapanC=Tex(r'$C.[8;10)$').scale(0.7).shift(2.4*UP,2*RIGHT)
        self.add(dapanC)
        dapanD=Tex(r'$D.[10;+\infty)$').scale(0.7).shift(2.4*UP,6*RIGHT)
        self.add(dapanD)
        solution=Text(
            text="Lời giải: Vu Dinh Thai",
            font = "Times New Roman",
            color= YELLOW,
            weight=BOLD,
            slant=ITALIC
        ).scale(0.5).shift(2*UP)
        self.add(solution)
        self.wait(2)


        #Graph ----------------------------------------------------------------------------
        ax = Axes(
            x_range=[-6.5,12.5,3],x_length=4,
            y_range=[-7,13,3],y_length=4.3,
            tips=False
        ).scale(1.3).shift(3.5*RIGHT,1*DOWN)
        pointO = Tex('O').scale(0.5).shift(1.7*DOWN,2.5*RIGHT)
        self.play(Create(ax), Write(pointO))


        parab = ax.plot(lambda x: (2*x**2+2*x-5), x_range=[-3.5,2.5])
        parab.set_color_by_gradient(RED)
        z_label = MathTex(
            r'(P)', color = RED
        ).scale(0.6).shift(1.6*UP,1.3*RIGHT)

        line = ax.plot(lambda x: x, x_range=[-6,12])
        line.set_color_by_gradient(ORANGE)
        u_label = MathTex(
            r'(d)', color = ORANGE
        ).scale(0.7).next_to(line).shift(0*RIGHT,2.6*UP)

        def c1(t):
            return (cos(t) +7, sin(t)+10)
        cir1 = ax.plot_parametric_curve(c1, color=BLUE, t_range=[0, 2 * PI])
        w1_label = MathTex(
            r'(C)', color = BLUE
        ).scale(0.6).next_to(cir1, UP).shift(0.1*DOWN)

        def c2(t):
            return (cos(t) +10, sin(t)+7)
        cir2 = ax.plot_parametric_curve(c2, color=GREEN, t_range=[0, 2 * PI])
        w2_label = MathTex(
            r"""(C')""", color = GREEN
        ).scale(0.6).next_to(cir2)

        #Loigiai ===========================================================================
        loigiai1 = MathTex(
            r"""\bullet \ \  M(z) \in (P): y=2x^2+2x-5 """
        ).scale(0.7).to_corner(LEFT).shift(1.6*UP)
        loigiai1.set_color_by_tex("x", RED)
        loigiai1[0][0].set_color(WHITE)
        loigiai2 = MathTex(
            r""" N(w) \in (C):(x-7)^2+(y-10)^2=1 """
        ).scale(0.7).to_corner(LEFT).shift(1.2*UP,0.4*RIGHT)
        loigiai2.set_color_by_tex("x", BLUE)
        loigiai3 = MathTex(
            r"""A(u) \in (d):y=x """
        ).scale(0.7).to_corner(LEFT).shift(0.8*UP,0.4*RIGHT)
        loigiai3.set_color_by_tex("x", ORANGE)

        self.play(
            Create(parab), Write(z_label),
            Create(line), Write(u_label),
            Create(cir1), Write(w1_label),
            Write(loigiai1), Write(loigiai2), Write(loigiai3),
            run_time = 2
        )
        self.wait(2)

        underhalf_cir1 = ax.plot(
            lambda x: 10-sqrt(1-(x-7) ** 2), x_range=[6,8]
        ).set_color_by_gradient(BLUE)

        abovehalf_cir2 = ax.plot(
            lambda x: 7+sqrt(1-(x-10) ** 2), x_range=[9,11]
        ).set_color_by_gradient(GREEN)


        #Khai bao valuetracker-------------------------------------------------------
        parabolvt = ValueTracker(0)
        linevt = ValueTracker(-1)
        circlevt = ValueTracker(6)
        cir2vt = ValueTracker(10)
        
        #ve cac diem =======================================
        dotM = always_redraw(
            lambda: Dot(color=YELLOW).move_to(
                ax.c2p(parabolvt.get_value(), parab.underlying_function(parabolvt.get_value()))
            )
        ).scale(0.2)

        M_text = Text(r'M', color= YELLOW_B).scale(0.4).next_to(dotM, UP)
        M_text.add_updater(lambda x: x.next_to(dotM, UP))

        dotA = always_redraw(
            lambda: Dot(color=YELLOW).move_to(
                ax.c2p(linevt.get_value(), line.underlying_function(linevt.get_value()))
            )
        )
        A_text = Text(r'A', color= YELLOW_B).scale(0.4).next_to(dotA, UP)
        A_text.add_updater(lambda x: x.next_to(dotA, UP))

        dotN = always_redraw(
            lambda: Dot(color=YELLOW).move_to(
                ax.c2p(circlevt.get_value(), underhalf_cir1.underlying_function(circlevt.get_value()))
            )
        )
        N_text = Text(r'N', color= YELLOW_B).scale(0.4).next_to(dotN, UP)
        N_text.add_updater(lambda x: x.next_to(dotN, UP))

        dotNdx = always_redraw(
            lambda: Dot(color=YELLOW).move_to(
                ax.c2p(cir2vt.get_value(), abovehalf_cir2.underlying_function(cir2vt.get_value()))
            )
        )
        Ndx_text = Text(r""" N' """, color= YELLOW_B).scale(0.4).next_to(dotNdx, UP)
        Ndx_text.add_updater(lambda x: x.next_to(dotNdx, UP))

        #ve line======================================================
      
        AM = Line().set_color_by_gradient(PURPLE)
        AM.add_updater(
            lambda mob: mob.put_start_and_end_on(dotA.get_center(), dotM.get_center())
        )

        AN = Line().set_color_by_gradient(PINK)
        AN.add_updater(
            lambda mob: mob.put_start_and_end_on(dotA.get_center(), dotN.get_center())
        )

        ANdx = Line().set_color_by_gradient(PINK)
        ANdx.add_updater(
            lambda mob: mob.put_start_and_end_on(dotA.get_center(), dotNdx.get_center())
        )
        #chay ========================================================
        
        self.play(
            Create(AM), Create(AN),
            Create(dotM), Write(M_text),
            Create(dotN), Write(N_text),
            Create(dotA), Write(A_text),
            run_time = 1.5
        )
        self.wait(1.5)
        self.play(
            parabolvt.animate.set_value(2.3),
            linevt.animate.set_value(8),
            circlevt.animate.set_value(8),
            run_time = 3
        )
        self.wait(5)

        #Diem doi xung duong tron an' =======================================================

        loigiai4 = Text(
            text= """Lấy N' đối xứng với N qua (d)""",
            font='Times New Roman',
            slant=ITALIC,
            font_size=defaultfont
        ).to_corner(LEFT).shift(0.4*UP)

        loi4bosung = MathTex(
            r"""\Rightarrow AN=AN' """
        ).scale(0.7).next_to(loigiai4)

        self.play(
            Write(loigiai4), Create(cir2), Write(w2_label),
            run_time = 1.5
        )
        self.wait()
        self.add(dotNdx, Ndx_text)
        self.wait(0.5)
        self.play(
            Create(ANdx),
            Create(dotNdx), Write(Ndx_text),
            Write(loi4bosung)
        )
        self.wait()
        self.play(
            circlevt.animate.set_value(7),
            cir2vt.animate.set_value(9),
            linevt.animate.set_value(5),
            run_time = 2
        )
        self.wait(3)

        loigiai5 = MathTex(
            r"""\Rightarrow N'(w') \in (C'):(x-10)^2+(y-7)^2=1 """
        ).scale(0.7).to_corner(LEFT).shift(0.1*DOWN)
        loigiai5.set_color_by_tex("x", GREEN)
        self.play(Write(loigiai5))
        self.wait(1.5)

        loigiai6 = MathTex(
            r"""\bullet \ \ T &= |u-z|+|u-w| = MA+NA
            \\ &= MA+N'A  """
        ).scale(0.7).to_corner(LEFT).shift(0.75*DOWN)
        self.play(Write(loigiai6))

        self.play(  #Cho bien mat cir1
            FadeOut(cir1), FadeOut(AN), FadeOut(dotN), FadeOut(N_text), FadeOut(w1_label)
        )

        loigiai7 = MathTex(
            r"""\geqslant MN' \geqslant MI' - 1  """
        ).scale(0.7).shift(1*DOWN,2.2*LEFT)
        self.play(Write(loigiai7))

        self.play(
            parabolvt.animate.set_value(2.097176),
            linevt.animate.set_value(7.334171),
            cir2vt.animate.set_value(9.007765),
            run_time = 2
        )
        self.wait()

        loigiai8 = MathTex(
            r"""\bullet \ \ M(x, \ 2x^2+2x-5), \ \ I'(10,7)  """
        ).scale(0.7).to_corner(LEFT).shift(1.5*DOWN)
        self.play(Write(loigiai8))
        self.wait(2)

        loigiai9 = MathTex(
            r"""\Rightarrow T \geqslant \sqrt{(x-10)^2+(2x^2+2x-12)^2}-1"""
        ).scale(0.7).to_corner(LEFT).shift(2*DOWN)
        self.play(Write(loigiai9), run_time = 1.5)
        self.wait(3)

        loigiai10 = MathTex(
            r"""TABLE \Rightarrow T_{min} \approx 6,96147..."""
        ).scale(0.7).to_corner(LEFT).shift(2.6*DOWN)
        self.play(Write(loigiai10))
        self.wait(5)

        khoanhtron = Circle(
            color= RED
        ).scale(0.3).next_to(dapanB).shift(1.55*LEFT)
        self.play(Create(khoanhtron))
        self.wait()
