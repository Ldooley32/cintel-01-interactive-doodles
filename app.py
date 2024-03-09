import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from shiny.express import ui, input, render

# add page option
ui.page_opts(title="Laura's Slider Input & Histogram Output", fillable=True)

# Create slidebar and slider input
with ui.sidebar():
    ui.input_slider("n", "Input Required", 0, 100, 42)

#Create a dropdown box to chooose histogram color
ui.input_select("histogram_color", "Histogram Color", 
                    choices=["skyblue", "salmon", "green", "gold", "purple",
                             "orange", "pink", "lavender", "red", "lightgreen"],
                    selected="orange")

#Create a dropdown box to choose scatterplot color
ui.input_select("scatterplot_color", "Scatterplot Color", 
                    choices=["skyblue", "salmon", "green", "gold", "purple",
                             "orange", "pink", "lavender", "red", "lightgreen"],
                    selected="purple")

@render.plot(alt="Output Histogram")
def histogram():

#define the number of points to generate
    count_of_points = int = 437
#set randome seed 
    np.random.seed(6)
#generate random data
    random_data_array = 100 + 15 * np.random.randn(count_of_points)
#create histogram with random data using matplotlib's hist() function
    plt.hist(random_data_array, input.n(), density=True, color = input.histogram_color())

#create a scatterplot using seaborn's scatterplot() function
@render.plot(alt="A scatterplot")
def scatterplot():
    np.random.seed(3)
    x = np.random.normal(size=100)
    y = np.random.normal(size=100)
    sns.scatterplot(x=x, y=y, color = input.scatterplot_color())
