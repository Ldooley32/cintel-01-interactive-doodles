import matplotlib.pyplot as plt
import numpy as np
from shiny.express import ui, input, render

# add page option
ui.page_opts(title="Laura's Slider Input & Histogram Output", fillable=True)

# Create slidebar and slider input
with ui.sidebar():
    ui.input_slider("n", "Input Required", 0, 100, 42)

@render.plot(alt="Output Histogram")
def histogram():
    np.random.seed(6)
    random_data_array = 100 + 15 * np.random.randn(437)
    plt.hist(random_data_array, input.n(), density=True)
