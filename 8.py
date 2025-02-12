import tkinter as tk
from tkinter import ttk
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

class ShapeViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("نمایش اشکال سه‌بعدی")

        # ایجاد فریم برای دکمه‌ها
        frame_buttons = ttk.Frame(self.root)
        frame_buttons.pack(side=tk.LEFT, padx=10, pady=10)

        # دکمه‌ها برای اشکال مختلف
        btn_cube = ttk.Button(frame_buttons, text="مکعب", command=self.show_cube)
        btn_cube.pack(pady=5)

        btn_sphere = ttk.Button(frame_buttons, text="کره", command=self.show_sphere)
        btn_sphere.pack(pady=5)

        btn_pyramid = ttk.Button(frame_buttons, text="هرم", command=self.show_pyramid)
        btn_pyramid.pack(pady=5)

        btn_cylinder = ttk.Button(frame_buttons, text="استوانه", command=self.show_cylinder)
        btn_cylinder.pack(pady=5)

    def show_cube(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        r = [-1, 1]
        X, Y = np.meshgrid(r, r)
        ax.plot_surface(X, Y, 1, alpha=0.5, rstride=100, cstride=100)
        ax.plot_surface(X, Y, -1, alpha=0.5, rstride=100, cstride=100)
        ax.plot_surface(X, 1, Y, alpha=0.5, rstride=100, cstride=100)
        ax.plot_surface(X, -1, Y, alpha=0.5, rstride=100, cstride=100)
        ax.plot_surface(1, X, Y, alpha=0.5, rstride=100, cstride=100)
        ax.plot_surface(-1, X, Y, alpha=0.5, rstride=100, cstride=100)
        plt.show()

    def show_sphere(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        u = np.linspace(0, 2 * np.pi, 100)
        v = np.linspace(0, np.pi, 100)
        x = 1 * np.outer(np.cos(u), np.sin(v))
        y = 1 * np.outer(np.sin(u), np.sin(v))
        z = 1 * np.outer(np.ones(np.size(u)), np.cos(v))
        ax.plot_surface(x, y, z, color='b')
        plt.show()

    def show_pyramid(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        vertices = np.array([[0, 0, 1], [1, 1, 0], [1, -1, 0], [-1, -1, 0], [-1, 1, 0]])
        faces = [[vertices[j] for j in [0, 1, 2]], [vertices[j] for j in [0, 2, 3]], [vertices[j] for j in [0, 3, 4]], [vertices[j] for j in [0, 4, 1]], [vertices[j] for j in [1, 2, 3, 4]]]
        for face in faces:
            face = np.array(face)
            ax.add_collection3d(plt.Polygon(face, alpha=0.5))
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        ax.set_zlim([0, 1])
        plt.show()

    def show_cylinder(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        z = np.linspace(0, 1, 100)
        theta = np.linspace(0, 2 * np.pi, 100)
        theta_grid, z_grid = np.meshgrid(theta, z)
        x_grid = np.cos(theta_grid)
        y_grid = np.sin(theta_grid)
        ax.plot_surface(x_grid, y_grid, z_grid, alpha=0.5)
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeViewerApp(root)
    root.mainloop()