# サンプルスクリプト3

import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=300)

with dpg.window(label="Label of Window1", pos=(10, 10), width=250, height=200, tag="window1"):
    button1 = dpg.add_button(label="My parerent is window1.", tag="button1")

dpg.add_button(label="My parerent is Window1, too.", parent="window1", tag="button1")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
