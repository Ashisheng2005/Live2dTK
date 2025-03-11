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
from time import sleep
import live2d.v3 as live2d
import live2d.v2 as live2d_v2

CURRENT_DIRECTORY = path.split(__file__)[0]
RESOURCES_DIRECTORY = path.join(CURRENT_DIRECTORY, "..", "Resources")


class Live2dFrame(OpenGLFrame):

    def __init__(self, *args, model_versions=3, model_path=None,fps=60, **kwargs):
        self.live2d_model_version = model_versions
        if self.live2d_model_version == 2:
            self.live2d = live2d_v2

        else:
            self.live2d = live2d

        self.live2d_model_path = model_path
        self.fps = fps
        if not self.live2d_model_path:
            raise ValueError("Live2dFrame not find model_path value")

        OpenGLFrame.__init__(self, *args, **kwargs)
        self.model = None

    def end(self):
        """结束之后的资源释放事件"""
        self.live2d.dispose()

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
        self.live2d.init()
        self.live2d.setLogEnable(True)
        self.live2d.glewInit()
        self.model = self.live2d.LAppModel()
        if self.live2d.LIVE2D_VERSION == 2:

            self.model.LoadModelJson(path.join(RESOURCES_DIRECTORY, self.live2d_model_path))

        else:
            self.model.LoadModelJson(path.join(RESOURCES_DIRECTORY, self.live2d_model_path))

        self.model.Resize(self.width, self.height)

    def _live2d_(self):
        """live2d模型的相关设置"""

        screen_x, screen_y = position()
        x = screen_x - self.winfo_rootx()
        y = screen_y - self.winfo_rooty()
        self.live2d.clearBuffer()
        self.model.Update()
        self.model.Drag(x, y)
        self.model.Draw()

    def redraw(self):
        """重绘，刷新时调用"""

        glClear(GL_COLOR_BUFFER_BIT)
        self._live2d_()
        # 控制帧率
        if self.fps < 120:
            sleep(1 / self.fps)


if __name__ == '__main__':
    from tkinter import Tk, Frame

    demo = Tk()
    demo.attributes('-transparent', 'black')
    frame = Frame(demo)
    frame.pack()
    Debugging = Live2dFrame(frame, model_path=r"E:\IDE\Plugins\live2d\米塔\3.model3.json",fps=120,
                            width=1000, height=1000)
    Debugging.pack()
    Debugging.bind("<Button-1>", lambda _: Debugging.model.StartRandomMotion())
    demo.mainloop()

    Debugging.end()

