"""
This code is a python program that uses the Tkinter library for creating a graphical user interface or for short -GUI
and the Matplotlib library for plotting graphs. This program simulates the motion of a projectile under the influence of
gravity, according the velocity, launch angle, and launch height the user choose.
"""

# Importing all the necessary libraries to create this program- tkinter for creating the GUI, matplotlib.pyplot for
# plotting graphs, math and ttk for themed tkinter widgets.
import math
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt


def on_velocity_slide(event):
    """
    This function is used whenever the velocity slider's value changes. This function updates the displayed value of the
    velocity.
    :param event: an event object that is triggered when the value of the velocity slider changes.
    :return: None (this function updates the GUI elements directly)
    """
    velocity_value.set(int(velocity_slider.get()))
    velocity_label.config(text=f"Initial Velocity: {int(velocity_slider.get())}")


def on_angle_slide(event):
    """
    This function is used whenever the angle slider's value changes. This function updates the displayed value of the
    angle.
    :param event: an event object that is triggered when the value of the angle slider changes.
    :return: None (this function updates the GUI elements directly)
    """
    angle_value.set(int(angle_slider.get()))
    angle_label.config(text=f"Launch Angle: {int(angle_slider.get())}")


def on_height_slide(event):
    """
    This function is used whenever the height slider's value changes. This function updates the displayed value of the
    height.
    :param event: an event object that is triggered when the value of the height slider changes.
    :return: None (this function updates the GUI elements directly)
    """
    height_value.set(int(height_slider.get()))
    height_label.config(text=f"Launch Height: {int(height_slider.get())}")


def simulate_projectile_motion():
    """
    This function calculates the parameters needed for the projectile motion simulation based on the slider values.
    :return: None
    """
    # Getting the parameter values from the sliders
    v0 = int(velocity_slider.get())
    angle = int(angle_slider.get())
    height = int(height_slider.get())

    # Converting the angle to radians
    angle_rad = math.radians(angle)

    # Calculating the initial velocities in x and y
    v0x = v0 * math.cos(angle_rad)
    v0y = v0 * math.sin(angle_rad)

    # Acceleration due to gravity
    g = 9.8

    # Calculating the time it would take the object to fly
    t_flight = 2 * v0y / g

    # Calculating the total horizontal distance
    d_total = v0x * t_flight

    # Calculating the number of segments
    num_steps = int(d_total)

    # Time increment
    dt = t_flight / num_steps

    # Initialize lists to store velocities and positions
    time = []
    v_horizontal = []
    v_vertical = []
    x_horizontal = []
    y_vertical = []

    # This loop goes over each time frame, calculates the corresponding x and y positions using kinematic
    # equations, and updates the velocities.
    for i in range(num_steps):
        # Updating the time
        t = dt * i
        time.append(t)

        # Calculating the x and y coordinates
        x = v0x * t
        y = v0y * t - 0.5 * g * t ** 2 + height
        x_horizontal.append(x)
        y_vertical.append(y)

        # Calculateing the horizontal and vertical velocities
        vx = v0x
        vy = v0y - g * t
        v_horizontal.append(vx)
        v_vertical.append(vy)

    # Plotting the velocity graphs
    plt.subplot(2, 1, 1)
    plt.plot(time, v_horizontal, label='Horizontal Velocity')
    plt.plot(time, v_vertical, label='Vertical Velocity')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Projectile Motion - Velocities')
    plt.legend()

    # Plotting the position graphs
    plt.subplot(2, 1, 2)
    plt.plot(time, x_horizontal, label='Horizontal Position')
    plt.plot(time, y_vertical, label='Vertical Position')
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.title('Projectile Motion - Positions')
    plt.legend()

    # Displaying the graphs
    plt.tight_layout()
    plt.show()


# Starting the tkinter window
root = tk.Tk()
root.title("Projectile Motion Simulator")
root.geometry("400x200")

# Creating sliders for the parameters
velocity_label = ttk.Label(root, text="Initial Velocity:")
velocity_label.pack()
velocity_value = tk.IntVar()
velocity_slider = ttk.Scale(root, from_=0, to=50, length=300, orient=tk.HORIZONTAL, variable=velocity_value,
                            command=on_velocity_slide)
velocity_slider.set(20)
velocity_slider.pack()

angle_label = ttk.Label(root, text="Launch Angle:")
angle_label.pack()
angle_value = tk.IntVar()
angle_slider = ttk.Scale(root, from_=0, to=90, length=300, orient=tk.HORIZONTAL, variable=angle_value,
                         command=on_angle_slide)
angle_slider.set(45)
angle_slider.pack()

height_label = ttk.Label(root, text="Launch Height:")
height_label.pack()
height_value = tk.IntVar()
height_slider = ttk.Scale(root, from_=0, to=20, length=300, orient=tk.HORIZONTAL, variable=height_value,
                          command=on_height_slide)
height_slider.set(10)
height_slider.pack()

# Create a button to start the simulation
start_button = ttk.Button(root, text="Start Simulation", command=simulate_projectile_motion)
start_button.pack()

# Start the tkinter event loop
root.mainloop()
