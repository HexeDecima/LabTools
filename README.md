# LabTools

This is a Python application that reads temperature and humidity data from a CSV file and plots it using Matplotlib. The application provides a graphical user interface (GUI) built with Tkinter, allowing users to select a date range and visualize the data for that period.

## Features

- **Date Range Selection**: Users can select the start and end dates to filter the data.
- **Interactive Plotting**: The application plots temperature and humidity data on two subplots, sharing the same x-axis.
- **Customizable X-Axis Labels**: The x-axis labels show the date and time in a custom format.
- **Matplotlib Integration**: The plots are created using Matplotlib, and the GUI integrates a Matplotlib toolbar for additional functionality.

## Prerequisites

- Python 3.x
- Required Python packages:
  - `matplotlib`
  - `pandas`
  - `tkinter`
  - `tkcalendar`

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/temperature-humidity-plotter.git
    cd temperature-humidity-plotter
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install matplotlib pandas tkcalendar
    ```

4. Ensure the CSV file (`arduino_data.csv`) is in the `files` directory.

## CSV File Format

The CSV file should be named `arduino_data.csv` and placed in the `files` directory. It should have the following columns:

- `year`: Year of the data point
- `month`: Month of the data point
- `day`: Day of the data point
- `hour`: Hour of the data point
- `temperature`: Temperature value
- `humidity`: Humidity value

Example:

```csv
year,month,day,hour,temperature,humidity
2024,7,16,12,25.3,60
2024,7,16,13,26.1,58
2024,7,16,14,26.8,57
...

