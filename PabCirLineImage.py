from manim import *
from math import sin, cos

config.tex_template.add_to_preamble("\\usepackage{pifont}")

class Image(Scene):
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

        dapanA=Tex(r'$A. \ (0;5]$').scale(0.7).to_corner(LEFT).shift(2.4*UP)
        self.add(dapanA)
        dapanB=Tex(r'$B. \ (5;8)$').scale(0.7).shift(2.4*UP,2*LEFT)
        self.add(dapanB)
        dapanC=Tex(r'$C. \ [8;10)$').scale(0.7).shift(2.4*UP,2*RIGHT)
        self.add(dapanC)
        dapanD=Tex(r'$D. \ [10;+\infty)$').scale(0.7).shift(2.4*UP,6*RIGHT)
        self.add(dapanD)

        solution=Text(
            text="Lời giải: Vu Dinh Thai",
            font = "Times New Roman",
            color= YELLOW,
            weight=BOLD,
            slant=ITALIC
        ).scale(0.5).shift(2*UP)
        self.add(solution)

        #Loi giai duoi day la loi giai-------------------------
        dkz1 = MathTex(
            r'\bullet \ \ |z-4+2i|=|2z+\overline{z}|'
        ).scale(0.7).to_corner(LEFT).shift(1.65*UP)
        self.add(dkz1)

        dkz2 = MathTex(
            r'\bullet \ \ |z-4+2i|^2-|2z+\overline{z}|^2=0'
        ).scale(0.7).to_corner(LEFT).shift(1.65*UP)
        #self.play(Transform(dkz1,dkz2))

        CALC1 = Tex(
            r'CALC z=100+0,01i  $\Rightarrow VT=$'
        ).scale(0.7).to_corner(LEFT).shift(1.2*UP)
        self.add(CALC1)

        DichsoZ_1 = MathTex(
            r'80779,96'
        ).scale(0.7).next_to(CALC1)
        #self.add(DichsoZ_1)

        DichsoZ_2 = Tex(
            r'8 \ \ 07 \ \ 79, \ \ 96'
        ).scale(0.7).next_to(CALC1)
        self.add(DichsoZ_2)

        DichsoZ_3 = MathTex(
            r'8 \ \ \ \ 8 \ \ -20 \ -4'
        ).scale(0.7).shift(0.8*UP,0.7*LEFT)
        #self.add(DichsoZ_3)
        
        DichsoZ_4 = MathTex(
            r'8x^2+8x-20-4y=0'
        ).scale(0.7).shift(0.8*UP,0.1*LEFT)
        self.add(DichsoZ_4)

        z = MathTex(
            r'\Rightarrow (P): y = 2x^2+2x-5'
        ).scale(0.7).shift(0.3*UP)
        z.set_color_by_tex("x", RED)
        self.add(z)

        dkw1 = MathTex(
            r'\bullet \ \  (w-8-10i)(\overline{w}-6+10i)'
        ).scale(0.7).to_corner(LEFT).shift(0.3*DOWN)
        self.add(dkw1)

        dkw1text = Text(
            text= 'thuần ảo',
            font='Times New Roman',
            slant=ITALIC,
            font_size=defaultfont
        ).next_to(dkw1).shift(0.075*UP)
        self.add(dkw1text)

        dkw2 = MathTex(
            r'\xrightarrow{\text{w=x+yi}} [ \ (x-8)+(y-10)i \ ] \ \cdot [ \ (x-6)-(y-10)i \ ] '
        ).scale(0.7).to_corner(LEFT).shift(0.8*DOWN)
        self.add(dkw2)

        dkw2text = Text(
            text= 'thuần ảo',
            font='Times New Roman',
            slant=ITALIC,
            font_size=defaultfont
        ).next_to(dkw2)
        self.add(dkw2text)

        dkw3 = MathTex(
            r'\Leftrightarrow (x-8)(x-6)+(y-10)^2=0 '
        ).scale(0.7).to_corner(LEFT).shift(1.4*DOWN)
        self.add(dkw3)

        w = MathTex(
            r'\Leftrightarrow (C): (x-7)^2+(y-10)^2=1 '
        ).scale(0.7).next_to(dkw3)
        w.set_color_by_tex("x", BLUE)
        self.add(w)

        dku1 = MathTex(
            r'\bullet \ \ |u+1-2i|=|u-2+i|'
        ).scale(0.7).to_corner(LEFT).shift(2*DOWN)
        self.add(dku1)

        dku2 = MathTex(
            r'\xrightarrow{\text{u=x+yi}} '
        ).scale(0.7).next_to(dku1).shift(0.05*UP)
        self.add(dku2)

        u = MathTex(
            r'(d): y=x '
        ).scale(0.7).next_to(dku2).shift(0.1*DOWN)
        u.set_color_by_tex("x", ORANGE)
        self.add(u)

class Graph(Scene):
    def construct(self):
        import manimpango
        defaultfont = 26
        
        solution=Text(
            text="Lời giải: Vu Dinh Thai",
            font = "Times New Roman",
            color= YELLOW,
            weight=BOLD,
            slant=ITALIC
        ).scale(0.5).shift(2*UP)
        self.add(solution)

        dapanB=Tex(r'$B. \ (5;8)$').scale(0.7).shift(2.4*UP,2*LEFT)
        self.add(dapanB)

        ax = Axes(
            x_range=[-6.5,12.5,3],x_length=4,
            y_range=[-7,13,3],y_length=4.3,
            tips=False
        ).scale(1.3).shift(3.5*RIGHT,1*DOWN)
        pointO = Tex('O').scale(0.5).shift(1.7*DOWN,2.5*RIGHT)
        self.add(pointO, ax)

        parab = ax.plot(lambda x: (2*x**2+2*x-5), x_range=[-3.5,2.5])
        parab.set_color_by_gradient(RED)
        z_label = MathTex(
            r'(P)', color = RED
        ).scale(0.6).shift(1.6*UP,1.3*RIGHT)
        self.add(parab, z_label)

        line = ax.plot(lambda x: x, x_range=[-6,12])
        line.set_color_by_gradient(ORANGE)
        u_label = MathTex(
            r'(d)', color = ORANGE
        ).scale(0.7).next_to(line).shift(0*RIGHT,2.6*UP)
        self.add(line, u_label)

        def c1(t):
            return (cos(t) +7, sin(t)+10)
        cir1 = ax.plot_parametric_curve(c1, color=BLUE, t_range=[0, 2 * PI])
        w1_label = MathTex(
            r'(C)', color = BLUE
        ).scale(0.6).next_to(cir1, UP).shift(0.1*DOWN)
        self.add(cir1, w1_label)

        def c2(t):
            return (cos(t) +10, sin(t)+7)
        cir2 = ax.plot_parametric_curve(c2, color=GREEN, t_range=[0, 2 * PI])
        w2_label = MathTex(
            r"""(C')""", color = GREEN
        ).scale(0.6).next_to(cir2)
        self.add(cir2, w2_label)

        #Chữ ---------------------------------------
        loigiai1 = MathTex(
            r"""\bullet \ \  M(z) \in (P): y=2x^2+2x-5 """
        ).scale(0.7).to_corner(LEFT).shift(1.6*UP)
        loigiai1.set_color_by_tex("x", RED)
        loigiai1[0][0].set_color(WHITE)
        self.add(loigiai1)
        loigiai2 = MathTex(
            r""" N(w) \in (C):(x-7)^2+(y-10)^2=1 """
        ).scale(0.7).to_corner(LEFT).shift(1.2*UP,0.4*RIGHT)
        loigiai2.set_color_by_tex("x", BLUE)
        self.add(loigiai2)
        loigiai3 = MathTex(
            r"""A(u) \in (d):y=x """
        ).scale(0.7).to_corner(LEFT).shift(0.8*UP,0.4*RIGHT)
        loigiai3.set_color_by_tex("x", ORANGE)
        self.add(loigiai3)

        loigiai4 = Text(
            text= """Lấy N' đối xứng với N qua (d)""",
            font='Times New Roman',
            slant=ITALIC,
            font_size=defaultfont
        ).to_corner(LEFT).shift(0.4*UP)
        self.add(loigiai4)

        loi4bosung = MathTex(
            r"""\Rightarrow AN=AN' """
        ).scale(0.7).next_to(loigiai4)
        self.add(loi4bosung)

        loigiai5 = MathTex(
            r"""\Rightarrow N'(w') \in (C'):(x-10)^2+(y-7)^2=1 """
        ).scale(0.7).to_corner(LEFT).shift(0.1*DOWN)
        loigiai5.set_color_by_tex("x", GREEN)
        self.add(loigiai5)

        loigiai6 = MathTex(
            r"""\bullet \ \ T &= |u-z|+|u-w| = MA+NA
            \\ &= MA+N'A  """
        ).scale(0.7).to_corner(LEFT).shift(0.75*DOWN)
        self.add(loigiai6)

        loigiai7 = MathTex(
            r"""\geqslant MN' \geqslant MI' - 1  """
        ).scale(0.7).shift(1*DOWN,2.2*LEFT)
        self.add(loigiai7)

        loigiai8 = MathTex(
            r"""\bullet \ \ M(x, \ 2x^2+2x-5), \ \ I'(10,7)  """
        ).scale(0.7).to_corner(LEFT).shift(1.5*DOWN)
        self.add(loigiai8)

        loigiai9 = MathTex(
            r"""\Rightarrow T \geqslant \sqrt{(x-10)^2+(2x^2+2x-12)^2}-1"""
        ).scale(0.7).to_corner(LEFT).shift(2*DOWN)
        self.add(loigiai9)

        loigiai10 = MathTex(
            r"""TABLE \Rightarrow T_{min} \approx 6,96147..."""
        ).scale(0.7).to_corner(LEFT).shift(2.6*DOWN)
        self.add(loigiai10)

        khoanhtron = Circle(
            color= RED
        ).scale(0.3).next_to(dapanB).shift(1.6*LEFT)
        self.add(khoanhtron)
