# Live2dTK

Live2d performance on tkinter based on live2d_py



```python
from tkinter import Tk, Frame
from Live2dTK import Live2dFrame

demo = Tk()
demo.attributes('-transparent', 'black')	# 想要实现背景透明，必须有这一行
frame = Frame(demo)
frame.pack()
Debugging = Live2dFrame(frame, model_path=r"E:\IDE\Plugins\live2d\米塔\3.model3.json",
                        width=1000, height=1000)
Debugging.pack()
demo.mainloop()
```

模型位置不强求，但仍然建议构建规范的项目目录：

```ini
.scr
+-live2d
	+model_name
+py_file
```



结果：

![](https://pic1.imgdb.cn/item/67cd37e6066befcec6e1cd02.png)



其中，附加函数：

```python
def on_start_callback(cls, group: str, no: int):"""动作开始触发事件"""
def on_finish_callback(cls):"""动作结束调用函数"""
def end(cls):"""结束之后的资源释放事件"""
def touch(self):"""被点击事件"""

```



该模块主要集成的live2d功能来自[live2d-py](https://github.com/Arkueid/live2d-py) 可以根据改项目的其他方法改写以实现更多的可玩性，当前模块后续也会封装更多的api，加油啊，做黄油的大哥哥！