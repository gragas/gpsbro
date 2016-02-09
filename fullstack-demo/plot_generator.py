import os
import matplotlib.pyplot as plt
import numpy as np


def gen_plot(site_id):
    t = np.arange(0.0, 2.0, 0.01)
    s = np.sin(2*np.pi*t)
    plt.plot(t, s)

    plt.xlabel("time (s)")
    plt.ylabel("voltage (mV)")
    plt.title("Default Network/{}".format(site_id))
    plt.grid(True)
    plt.savefig(os.path.join("static", "default_network", "{}.png".format(site_id)))

if __name__ == "__main__":
    gen_plot("test")
