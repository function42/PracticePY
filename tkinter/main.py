# -*- coding: utf-8 -*-

# In[1]
import tkinter as tk

# In[2]
def simple_example():
	top = tk.Tk(className='测试')
	top.iconbitmap('data.ico')
	# 进入消息循环
	top.mainloop()
	
def button_example():
	def echo(message='hello'):
		print(message)
	
	def add_label(event):
		label = tk.Label(root, text='被新增的标签', background='red')
		label.pack()
	
	echo()
	root = tk.Tk()
	root.wm_title('有按钮')
	root.iconbitmap('data.ico')
	
	w1 = tk.Label(root, text='这是个标签', background='blue')
	
	b1 = tk.Button(root, text='点击新增标签')
	b1['width'] = 20
	b1['height'] = 4
	b1.bind('<Button-1>', add_label)
	
	li = ['ANALYSIS', 'DATABASE', 'STATS', 'CALCULATE']
	li_part = tk.Listbox(root)
	
	for item in li:
		li_part.insert(0, item)
	
	w1.pack()
	b1.pack()
	li_part.pack()
	root.mainloop()

def layout_example():
	root = tk.Tk()
	root.wm_title('菜单案例')
	root.iconbitmap('data.ico')
	root['width'] = 800
	root['height'] = 600
	
	l1 = tk.Button(root, text='数据')
	l2 = tk.Button(root, text='生成')
	
	
	l1.grid(row=0, sticky=tk.W)
	l2.grid(row=1, sticky=tk.W)
	root.mainloop()

def menu_example():
	root = tk.Tk()
	root.wm_title('有按钮')
	root.iconbitmap('data.ico')
	root['width'] = 800
	root['height'] = 600
	
	menu_bar = tk.Menu(root)
	data_menu = tk.Menu(menu_bar)
	about_menu = tk.Menu(menu_bar)
	
	for item in ['导入', '导出']:
		data_menu.add_command(label=item)
		
	data_menu.add_separator()
	data_menu.add_command(label='清除')
	
	for item in ['作者', '版本', '更新']:
		about_menu.add_command(label=item)
	
	menu_bar.add_cascade(label='数据', menu=data_menu)
	menu_bar.add_cascade(label='关于', menu=about_menu)
	
	root['menu'] = menu_bar
	root.mainloop()

def dialog_example():
	pass

def canvas_example():
	def echo(message='hello'):
		print(message)
	import random
	def add_label(event):
		label = tk.Label(root, text='NO.'+str(random.randint(0,10))+' 被新增的标签', background='red')
		label.grid(row=1, columnspan=2)
	
	echo()
	root = tk.Tk()
	root.wm_title('有按钮')
	root.iconbitmap('data.ico')
	root['width'] = 800
	root['height'] = 600
	
	b1 = tk.Button(root, text='点击新增标签')
	b1['width'] = 20
	b1['height'] = 4
	b1.bind('<Button-1>', add_label)
	
	c1 = tk.Canvas(root)
	
	coord = 10, 50, 240, 210
	c1.create_arc(coord, start=0, extent=150, fill="blue")

	b1.grid(row=0, column=0)
	c1.grid(row=0, column=1)
	root.mainloop()
	
def complex_example():
	import numpy as np
	import matplotlib
	matplotlib.use('TkAgg')
	from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
	from matplotlib.figure import Figure
	import random

	def draw_pic(event):
		sample_num = 100
		x=np.random.randint(0, 100, size=sample_num)
		y=np.random.randint(0, 100, size=sample_num)
		draw_pic.f.clf()
		a = draw_pic.f.add_subplot(111)
		color=['b+','r.','ys','gx']
		a.plot(x, y, random.choice(color))
		draw_pic.canvas.show()

	root = tk.Tk()
	root.wm_title('有按钮')
	root.iconbitmap('data.ico')
	root['width'] = 800
	root['height'] = 600
	
	b1 = tk.Button(root, text='点击画图')
	b1['width'] = 20
	b1['height'] = 4
	b1.bind('<Button-1>', draw_pic)
	
	f = Figure(figsize=(5,4), dpi=100)	
	draw_pic.f = f
	canvas = FigureCanvasTkAgg(f, master=root)
	draw_pic.canvas = canvas

	b1.grid(row=0, column=0, sticky=tk.N)
	canvas.get_tk_widget().grid(row=0, column=1)
	root.mainloop()
	
if __name__ == '__main__':
#	simple_example()'
#	button_example()
#	layout_example()
#	menu_example()
#	dialog_example()
#	canvas_example()
	complex_example()