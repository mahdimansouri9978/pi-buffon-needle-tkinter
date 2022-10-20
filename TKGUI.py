import tkinter as tk
from chart import base_chart
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from PIL import Image, ImageTk
from calculate import calculate


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("1300x640")

        self.figure = None
        self.plot = None
        self.toolbar = None

        self.root.title("Buffon's needle")
        self.root.configure(bg="#F5EFE6")
        self.frame = tk.Frame(self.root)

        self.explanation = "This puzzle first was proposed by Buffon in 1733 and expressed with what probability a thrown needle\n can cut a straight line.This problem was solved by Buffon's himself in 1777."

        self.label = tk.Label(self.root, text="Calculate PI based on Monte Carlo method (Buffon's Needle)", font=("Comic Sans MS", 22))
        self.label.pack()

        self.explain = tk.Label(self.root, text=self.explanation, font=("Comic Sans MS", 14), bg="#AEBDCA")
        self.explain.pack(pady=20)

        self.canvas = tk.Canvas(self.root, width=1200, heigh=52, bg="#7D6E83")
        self.canvas.pack(pady=0)

        self.point_lab = tk.Label(self.root, text="number of needles:", font=("Comic Sans MS", 12), bg="#7D6E83")
        self.canvas.create_window(77, 26, window=self.point_lab)

        self.input_num = tk.Entry(self.root, width=30)
        self.canvas.create_window(250, 26, window=self.input_num)

        self.submit = tk.Button(self.root, text="Calculate", command=self.points_chart, font=("Comic Sans MS", 10), bg="#AEBDCA")
        self.canvas.create_window(400, 26, window=self.submit)

        self.ba_chart()

        self.text_canvas = tk.Canvas(self.root, width=700, heigh=398, bg="#E8DFCA", highlightthickness=0)
        self.text_canvas.place(x=550, y=198)

        self.points_in = tk.Label(self.root, text="points in :", font=("Comic Sans MS", 14))

        self.points_out = tk.Label(self.root, text="points out :", font=("Comic Sans MS", 14))

        self.image = ImageTk.PhotoImage(Image.open("Untitled.png"))
        self.text_canvas.create_image(350, 220, image=self.image)

        self.pi = tk.Label(self.root, text="PI : ", font=("Comic Sans MS", 14))

        self.root.mainloop()

    def ba_chart(self):
        arrays = base_chart()
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.plot = self.figure.add_subplot(111)
        self.plot.plot(arrays[0], arrays[1], color="#B73E3E", linewidth=4)
        self.plot.plot(arrays[0], arrays[2], color="#B73E3E", linewidth=4)

        b_chart = FigureCanvasTkAgg(self.figure, self.root)
        b_chart.draw()
        b_chart.get_tk_widget().place(x=50, y=198)

        self.plot.set_xlim([-2.5, 15])
        self.plot.set_ylim([-1, 7])
        self.plot.set_xticks([])
        self.plot.set_yticks([])
        self.figure.set_facecolor("#D0B8A8")
        self.figure.tight_layout()

        self.toolbar = NavigationToolbar2Tk(b_chart, self.root)
        self.toolbar.configure(bg="#7D6E83")
        self.toolbar.pack(padx=(50, 50))

        for button in self.toolbar.winfo_children():
            button.config(background="#7D6E83")
        self.toolbar.update()

    def points_chart(self):
        self.toolbar.destroy()
        self.pi.destroy()
        self.points_out.destroy()
        self.points_in.destroy()
        self.ba_chart()
        nums = int(self.input_num.get())
        arrays = calculate(nums)

        for i in range(len(arrays[1])):
            self.plot.plot(arrays[1][i], arrays[2][i], color="#256D85", linewidth=2)

        for j in range(len(arrays[3])):
            self.plot.plot(arrays[3][j], arrays[4][j], color="#FF1E1E", linewidth=2)

        self.points_out = tk.Label(self.root, width=15, text=f"needles out : {len(arrays[3])}", font=("Comic Sans MS", 12), bg="#E8DFCA")
        self.points_in = tk.Label(self.root, width=15, text=f"needles on : {len(arrays[1])}", font=("Comic Sans MS", 12), bg="#E8DFCA")
        self.pi = tk.Label(self.root, width=10, text=f"PI : {round(arrays[0], 4)}", font=("Comic Sans MS", 18), bg="#E8DFCA")
        self.text_canvas.create_window(102, 20, window=self.points_in)
        self.text_canvas.create_window(105, 60, window=self.points_out)
        self.text_canvas.create_window(100, 380, window=self.pi)
