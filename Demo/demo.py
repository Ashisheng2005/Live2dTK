from tkinter import Tk, Frame, BOTH
from Live2dTK import Live2dFrame


def set_window_bottom_right(window, width, height):
    # 获取屏幕尺寸
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # 计算右下角坐标
    x = screen_width - width
    y = screen_height - height + 50 # 预留50像素避免遮挡任务栏（可选调整）

    # 设置窗口位置和大小
    window.geometry(f"{width}x{height}+{x}+{y}")


demo = Tk()
demo.attributes('-transparent', 'black')    # 想要实现背景透明，必须有这一行
# demo.attributes("-alpha", 0.8)
# 使用attributes方法将窗口设置为置顶
demo.attributes('-topmost', True)
demo.overrideredirect(True)
window_width = 1000
window_height = 800
set_window_bottom_right(demo, window_width, window_height)

frame = Frame(demo)
frame.pack()
# "E:\IDE\Plugins\live2d\米塔\3.model3.json"
Debugging = Live2dFrame(frame, model_path=r".\live2d\Hiyori\Hiyori.model3.json",
                        width=window_width, height=window_height)
Debugging.pack(fill=BOTH, expand=True)

demo.bind("<Button-1>", lambda _: Debugging.model.StartRandomMotion())

demo.mainloop()