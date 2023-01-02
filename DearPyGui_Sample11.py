# サンプルスクリプト11

import os
import threading
import numpy as np
import cv2
import dearpygui.dearpygui as dpg

# UVCカメラは0で起動します。適当な番号にしてください。
# この時点でテクスチャーのサイズが決まります。
CAP = cv2.VideoCapture(0)
ret, frame = CAP.read()
CAP_W = int(CAP.get(cv2.CAP_PROP_FRAME_WIDTH))
CAP_H = int(CAP.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(f"Width = {CAP_W}")
print(f"Height = {CAP_H}")

# 初期は[stop]の状態
isContinuousGrab = False

# 撮像した画像
frame = None

# テクスチャー「dynamic_texture」に画像を登録します
def set_image_to_dynamic_texture(image):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)
    dpg.set_value("dynamic_texture", image/255)

# 連続撮像を行い、テクスチャー「dynamic_texture」に画像を登録します
def grab_and_set_image():
    global frame
    while isContinuousGrab:
        ret, frame = CAP.read()
        set_image_to_dynamic_texture(frame)

# [start]ボタンを押した時のコールバック
def button_start(sender, app_data, user_data):
    global isContinuousGrab
    if isContinuousGrab is not True:
        isContinuousGrab = True
        thread = threading.Thread(target=grab_and_set_image)
        thread.start()

# [stop]ボタンを押した時のコールバック
def button_stop(sender, app_data, user_data):
    global isContinuousGrab
    if isContinuousGrab is not False:
        isContinuousGrab = False

# 以下、DearPyGuiの基本構成     
dpg.create_context()
dpg.create_viewport(title='Title', width=300, height=300)

# テクスチャーレジストリの作成
with dpg.texture_registry():
    img_white = np.ones((CAP_W, CAP_H, 4), np.uint8)
    dpg.add_dynamic_texture(CAP_W, CAP_H, img_white, tag="dynamic_texture")

# window01の作成（ボタンの作成）
with dpg.window(label="window01") as parent_window01:
    dpg.add_button(label="start", callback=button_start)
    dpg.add_button(label="stop", callback=button_stop)

# window02の作成（画像の表示）
with dpg.window(label="window02", pos=(100,0)) as parent_window02:
    dpg.add_image("dynamic_texture", tag ="dynamic_image")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
