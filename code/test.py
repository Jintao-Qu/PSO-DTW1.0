import tkinter as tk
def myLabel(event):
    global root
    s = tk.Label(root, text="Hello world")
    s.pack()
root = tk.Tk()
B = tk.Button(root, text="点击")
B.bind("<Button-1>", myLabel)
B.pack(side=tk.LEFT)

root.mainloop()