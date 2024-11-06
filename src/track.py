import matplotlib

from utils import dist
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
matplotlib.use('TkAgg')

class Track():
    def __init__(self, cones : list[tuple[float, float]]):
        self.cones = cones

    #Return all cones inside a circle with radius range surrounding the position
    def get_near_cones(self, position: tuple[float, float], range:float) -> list[tuple[float, float]]:
        near_cones = []
        for cone in self.cones:
            if dist(position, cone) < range:
                near_cones.append(cone)
        return near_cones


    #def visualize(self):




if __name__ == '__main__':
    track = Track([(1.,0.),(1.,1.),(1.,1.2),(1.,1.4)])
    # Initialize the figure and axis
    fig, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(-5, 5)

    cone_size = .5

    # Number of cones
    num_cones = len(track.cones)
    x_data, y_data = zip(*track.cones)
    cone_plots = []

    coneplot, = plt.plot(x_data, y_data, 'ro')
    cone_plots.append(coneplot)

    def update(frame):
        # Update x data to move cones to the right
        for i, cone in enumerate(cone_plots):
            cone.set_xdata(track.cones[i][0]+ frame*.01)
        return cone_plots


    # Animation function
    anim = FuncAnimation(fig, update, frames=1000)
    plt.show()