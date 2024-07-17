import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import pandas as pd
from tkinter import *
from tkcalendar import DateEntry

# READING DATA FROM ARDUINO
arduino_data = pd.read_csv('files/arduino_data.cvs')

# Convert columns to a datetime format
arduino_data['Date'] = pd.to_datetime(arduino_data[['year', 'month', 'day']])
arduino_data.set_index('Date', inplace=True)


# PLOT FUNCTION CONTAINING MATPLOTLIB
def plot():
    # Get the date range from the date pickers
    start_date = start_date_picker.get_date()
    end_date = end_date_picker.get_date()
    # Filter the data based on the selected date range
    filtered_data = arduino_data[start_date:end_date]

    # Create the figure that will contain the plot
    fig, (axis_teplota, axis_vlhkost) = plt.subplots(2, 1, sharex=True, figsize=(12, 8))

    # Plot Teplota on the primary axis
    axis_teplota.plot(filtered_data.index, filtered_data['temperature'], 'r-', label='Teplota')
    axis_teplota.set_xlabel('Čas')
    axis_teplota.set_ylabel('Teplota (°C)', color='r')
    axis_teplota.tick_params(axis='y', labelcolor='r')
    axis_teplota.grid(which='major', axis='both', linestyle='--', color='gray')

    # Plot Vlhkost on the secondary axis
    axis_vlhkost.plot(filtered_data.index, filtered_data['humidity'], 'b-', label='Vlhkost')
    axis_vlhkost.set_ylabel('Vlhkost (%)', color='b')
    axis_vlhkost.tick_params(axis='y', labelcolor='b')
    axis_vlhkost.grid(which='major', axis='both', linestyle='--', color='gray')

    # Custom x-axis labels
    x_labels = [
        f"{row['day']}.{row['month']}.{row['year']}\n{row['hour']}"
        for _, row in filtered_data.iterrows()
    ]

    # Set custom x-ticks
    axis_vlhkost.set_xticks(filtered_data.index)
    axis_vlhkost.set_xticklabels(x_labels, rotation=45, ha='right')

    # Add a title and show the plot
    # plt.title('Teplota a vlhkost časově')
    fig.tight_layout()

    # TKINTER CANVAS
    # Containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    # Placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
    # Creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()
    # Placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()


# TKINTER GUI
# The main tkinter window
window = Tk()
# Setting the title
window.title('Teplota a vlhkost')
# Setting the dimensions of the main window
window.geometry("1200x800")

# Frame for the date pickers and plot button
frame = Frame(window)
frame.pack(pady=10)

# DATE PICKERS
# Start date
start_date_label = Label(frame, text="Od:")
start_date_label.grid(row=0, column=0, padx=5)
start_date_picker = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2)
start_date_picker.grid(row=0, column=1, padx=5)
# End date
end_date_label = Label(frame, text="Do:")
end_date_label.grid(row=0, column=2, padx=5)
end_date_picker = DateEntry(frame, width=12, background='darkblue', foreground='white', borderwidth=2)
end_date_picker.grid(row=0, column=3, padx=5)
# Plot button
plot_button = Button(frame, command=plot, height=2, width=10, text="Zobrazit")
plot_button.grid(row=0, column=4, padx=5)


# Run the gui
window.mainloop()
