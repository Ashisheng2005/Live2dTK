#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2025/3/9 下午1:41 
# @Author : Huzhaojun
# @Version：V 1.0
# @File : __init__.py.py
# @desc : README.md

from OpenGL.GL import *
from pyopengltk import OpenGLFrame
from pyautogui import position
from os import path
import live2d.v3 as live2d


class Live2dFrame(OpenGLFrame):

    def __init__(self,*args, model_path=None, **kwargs):
        self.live2d_model_path = model_path
        if not self.live2d_model_path:
            raise ValueError("Live2dFrame not find model_path value")

        OpenGLFrame.__init__(self, *args, **kwargs)
        self.global_coordinates = True
        self.MAPP = round(200 / 980, 2)
        self.model = None

    @classmethod
    def on_start_callback(cls, group: str, no: int):
        """动作开始触发事件"""
        print(f"touched and motion [{group}_{no}] is started")

    @classmethod
    def on_finish_callback(cls):
        """动作结束调用函数"""
        print("motion finished")

    @classmethod
    def end(cls):
        """结束之后的资源释放事件"""
        live2d.dispose()

    def touch(self):
        """被点击事件"""
        print("被点击")
        x, y = 100, 100
        self.model.Touch(x, y, self.on_start_callback, self.on_finish_callback)
        self.model.StartMotion("LipSync", 0, live2d.MotionPriority.FORCE)

    def coordinate_compression(self):
        """坐标压缩函数，将UI内，live2dframe外的坐标压缩为frame内地映射坐标"""

        screen_x, screen_y = position()
        # x = screen_x - self.winfo_rootx()
        y = screen_y - self.winfo_rooty()

        if y > 160:
            y *= 0.2

    def initgl(self):
        """初始化"""

        self.animate = 1
        # self.after(100, self.printContext)
        # live2D初始化
        live2d.init()
        live2d.setLogEnable(False)
        live2d.glewInit()
        # glViewport(0, 0, self.width, self.height)
        # glClearColor(0.0, 1.0, 0.0, 0.0)

        self.model = live2d.LAppModel()
        if live2d.LIVE2D_VERSION == 2:
            # self.model.LoadModelJson(r"..\live2d\UG\ugofficial.model3.json")
            # print(self.live2d_model_path)
            self.model.LoadModelJson(self.live2d_model_path)

        else:
            self.model.LoadModelJson(self.live2d_model_path)

        self.model.Resize(self.width, self.height)

    def _live2d_(self):
        """live2d模型的相关设置"""

        screen_x, screen_y = position()
        x = screen_x - self.winfo_rootx()
        y = screen_y - self.winfo_rooty()
        # sleep(0.02)
        live2d.clearBuffer()
        self.model.Update()
        self.model.Drag(x, y)
        self.model.Draw()

    def redraw(self):
        """重绘，刷新时调用"""

        glClear(GL_COLOR_BUFFER_BIT)
        self._live2d_()


if __name__ == '__main__':
    from tkinter import Tk, Frame

    demo = Tk()
    demo.attributes('-transparent', 'black')
    frame = Frame(demo)
    frame.pack()
    Debugging = Live2dFrame(frame, model_path=r"E:\IDE\Plugins\live2d\米塔\3.model3.json",
                            width=1000, height=1000)
    Debugging.pack()
    demo.mainloop()
