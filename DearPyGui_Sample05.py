# サンプルスクリプト5

import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=300)

def button_callback(sender, app_data, user_data):
    print(f"sender is: {sender}")
    print(f"app_data is: {app_data}")
    print(f"user_data is: {user_data}")

with dpg.window(label="Tutorial"):
    dpg.add_button(label="button1", callback=button_callback, user_data="push button1")
    dpg.add_button(label="button2", callback=button_callback, user_data="push button2")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
