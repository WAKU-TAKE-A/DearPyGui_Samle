# サンプルスクリプト8

import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=300)

def button_callback(sender, app_data):
    value = dpg.get_value("checkbox1")
    dpg.set_value("text1", value)

with dpg.window(label="window1", width=250, height=150):
    dpg.add_checkbox(label="checkbox1", tag="checkbox1")
    dpg.add_checkbox(label="checkbox2", source="checkbox1")
    dpg.add_button(label="Get the value of checkbox1.", callback=button_callback)

with dpg.window(label="window2", pos=(0,150)):
    dpg.add_text("***", tag="text1")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
