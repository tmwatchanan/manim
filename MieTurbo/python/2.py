from manimlib.imports import *


class Abs(Scene):
    CONFIG = {
        "number_line_config": {
            "x_min": -8,
            "x_max": 8,
            "include_numbers": True,
            "include_tip": False,
            "tick_size": 0.10,
            "unit_size": .75,
            "numbers_to_show": range(-8, 8+1, 2),
        }
    }

    def construct(self):
        nl = NumberLine(**self.number_line_config)
        nl.shift(2 * DOWN)

        self.add(nl)
        self.play(FadeInFrom(nl, LEFT))

        self.wait(1)

        x_text = TexMobject("x = ")

        tracker = ValueTracker(0)
    
        x_number = DecimalNumber(0)
        x_number.next_to(x_text, RIGHT)
        x_number.add_updater(lambda m: m.set_value(tracker.get_value()))

        abs_text = TexMobject("\\abs{x}", "=")
        abs_text.set_color_by_tex_to_color_map({
            "\\abs{x}": YELLOW,
        })
        abs_number = DecimalNumber(0)
        abs_number.next_to(abs_text, RIGHT)
        abs_number.add_updater(lambda m: m.set_value(abs(tracker.get_value())))

        abs_g = VGroup(abs_text, abs_number)
        abs_g.to_edge(UP + RIGHT, buff=2)

        x_g = VGroup(x_text, x_number)
        x_g.next_to(abs_g, LEFT)
        x_g.to_edge(LEFT, buff=2)

        d1 = Dot()
        d1.add_updater(lambda d: d.next_to(nl.number_to_point(tracker.get_value()), 2 * UP))

        abs_line = Line(nl.number_to_point(0), nl.number_to_point(0.001), color=YELLOW)
        def abs_line_to(m):
            start = nl.number_to_point(0)
            val = tracker.get_value()
            end = nl.number_to_point(val)
            if val != 0:
                m.put_start_and_end_on(start, end)
        abs_line.add_updater(abs_line_to)

        self.play(FadeIn(abs_line), FadeIn(d1), FadeIn(x_g), FadeIn(abs_g))
        self.wait()
        self.play(tracker.set_value, -6, run_time=3)
        self.wait()
        self.play(tracker.set_value, 5, run_time=3)
        self.wait()
