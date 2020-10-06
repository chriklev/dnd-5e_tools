import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches
import field_of_view as fov


def plot_fov(vision_origin_x, vision_origin_y, points_x, points_y, connections, save_fig=None):

    polygon_x, polygon_y = fov.get_vision_polygon(
        vision_origin_x, vision_origin_y, points_x, points_y, connections)

    checked = []
    for i, neighbors in enumerate(connections):
        for j in neighbors:
            if j not in checked:
                plt.plot([points_x[i], points_x[j]],
                         [points_y[i], points_y[j]],
                         c="red",
                         linewidth=3,
                         zorder=5)
        checked.append(i)

    plt.fill(polygon_x,
             polygon_y, zorder=0)
    plt.scatter([vision_origin_x], [vision_origin_y],
                marker='*', s=200, zorder=10)
    if save_fig is not None:
        plt.savefig(save_fig)
    plt.show()


def animated_fov(positions_x, positions_y, points_x, points_y, connections):
    fig = plt.figure()
    fig.set_dpi(100)
    fig.set_size_inches(7, 6.5)

    ax = plt.axes(xlim=(0, 5), ylim=(0, 5))

    checked = []
    for i, neighbors in enumerate(connections):
        for j in neighbors:
            if j not in checked:
                ax.plot([points_x[i], points_x[j]],
                        [points_y[i], points_y[j]],
                        c="red", linewidth=3, zorder=5)
        checked.append(i)

    polygon_x, polygon_y = fov.get_vision_polygon(
        positions_x[0], positions_y[0], points_x, points_y, connections)
    polygon_patch = patches.Polygon(
        np.array([polygon_x, polygon_y]).T, zorder=0, alpha=.2)

    position_patch, = ax.plot(
        [positions_x[0]], [positions_y[0]], 'o', c="g", zorder=1000)

    def init():
        ax.add_patch(polygon_patch)
        return polygon_patch, position_patch

    def animate(i):
        polygon_x, polygon_y = fov.get_vision_polygon(
            positions_x[i], positions_y[i], points_x, points_y, connections)
        polygon_patch.set_xy(np.array([polygon_x, polygon_y]).T)

        position_patch.set_data([positions_x[i]], [positions_y[i]])

        return polygon_patch, position_patch

    anim = animation.FuncAnimation(fig, animate, np.arange(1, len(positions_x)), init_func=init,
                                   interval=25, blit=True)
    anim.save("anim-test.mp4")
    plt.show()


if __name__ == "__main__":
    points_x = np.array([0, 5, 5, 0, 2, 1, 2, 3, 4])
    points_y = np.array([0, 0, 5, 5, 2, 3, 3, 3, 2])
    connections = [
        [3, 1],
        [0, 2],
        [1, 3],
        [2, 0],
        [5],
        [4],
        [7],
        [6, 8],
        [7]
    ]

    positions_x = np.linspace(4.5, 0.5, 300)
    positions_y = np.linspace(4, 4, 300)
    positions_x = np.append(positions_x, np.linspace(0.5, 4.5, 300))
    positions_y = np.append(positions_y, np.linspace(4, 1, 300))
    positions_x = np.append(positions_x, np.linspace(4.5, 4.5, 300))
    positions_y = np.append(positions_y, np.linspace(1, 4, 300))

    animated_fov(positions_x, positions_y, points_x, points_y, connections)
