
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import matplotlib.dates as mdates
from datetime import datetime

def plot_windspeeds2(t, u, title=None, show=False, xlim=None):
    """
    Plot one or multiple wind speed time series with datetime x-axis.

    Parameters
    ----------
    t : array-like
        Time array (strings like '2017-01-02 00:00:00' or datetime objects)
    u : array-like or list of array-like
        One or multiple wind speed arrays
    """

    # Convert timestamps to datetime if needed
    if isinstance(t[0], str):
        t = [datetime.strptime(ts, "%Y-%m-%d %H:%M:%S") for ts in t]

    fig, ax = plt.subplots(figsize=(9, 4))

    # Ensure u is iterable
    if isinstance(u, (list, tuple)):
        wind_arrays = u
    else:
        wind_arrays = [u]

    # Plot wind speeds
    for i, ui in enumerate(wind_arrays):
        ax.plot(t, ui, label=f"Wind speed {i+1}")

    ax.set_ylabel("Wind speed (m/s)")
    ax.set_xlabel("Time")

    # Format datetime axis nicely
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d\n%H:%M"))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())

    fig.autofmt_xdate()

    # Optional x-limits (must be datetime if used)
    if xlim is not None:
        ax.set_xlim(xlim)

    if len(wind_arrays) > 1:
        ax.legend()

    if title is not None:
        ax.set_title(title)

    if show:
        plt.show()

    return fig, ax