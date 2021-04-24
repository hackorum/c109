import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as pg
import statistics

df = pd.read_csv("csv/data.csv")

height_list = df["Height(Inches)"].tolist()

weight_list = df["Weight(Pounds)"].tolist()

height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)

standard_deviation = statistics.stdev(height_list)

height_first_stdev_start = height_mean - standard_deviation
height_first_stdev_end = height_mean + standard_deviation

height_second_stdev_start = height_mean - (2 * standard_deviation)
height_second_stdev_end = height_mean + (2 * standard_deviation)

height_third_stdev_start = height_mean - (3 * standard_deviation)
height_third_stdev_end = height_mean + (3 * standard_deviation)

list_of_data_within_first_stdev = [
    result
    for result in height_list
    if result > height_first_stdev_start and result < height_first_stdev_end
]

list_of_data_within_second_stdev = [
    result
    for result in height_list
    if result > height_second_stdev_start and result < height_second_stdev_end
]

list_of_data_within_third_stdev = [
    result
    for result in height_list
    if result > height_third_stdev_start and result < height_third_stdev_end
]

print(
    f"{len(list_of_data_within_first_stdev) * 100 / len(height_list)}% of data lies between first standard deviation"
)
print(
    f"{len(list_of_data_within_second_stdev) * 100 / len(height_list)}% of data lies between second standard deviation"
)
print(
    f"{len(list_of_data_within_third_stdev) * 100 / len(height_list)}% of data lies between third standard deviation"
)

fig = ff.create_distplot([height_list], ["Height List"], show_hist=False)
fig.add_trace(
    pg.Scatter(x=[height_mean, height_mean], y=[0, 0.2], mode="lines", name="Mean")
)
fig.add_trace(
    pg.Scatter(
        x=[height_first_stdev_start, height_first_stdev_start],
        y=[0, 0.2],
        mode="lines",
        name="First STDEV",
    )
)
fig.add_trace(
    pg.Scatter(
        x=[height_first_stdev_end, height_first_stdev_end],
        y=[0, 0.2],
        mode="lines",
        name="First STDEV",
    )
)
fig.add_trace(
    pg.Scatter(
        x=[height_second_stdev_start, height_second_stdev_start],
        y=[0, 0.2],
        mode="lines",
        name="Second STDEV",
    )
)
fig.add_trace(
    pg.Scatter(
        x=[height_second_stdev_end, height_second_stdev_end],
        y=[0, 0.2],
        mode="lines",
        name="Second STDEV",
    )
)

fig.add_trace(
    pg.Scatter(
        x=[height_third_stdev_start, height_third_stdev_start],
        y=[0, 0.2],
        mode="lines",
        name="Third STDEV",
    )
)
fig.add_trace(
    pg.Scatter(
        x=[height_third_stdev_end, height_third_stdev_end],
        y=[0, 0.2],
        mode="lines",
        name="Third STDEV",
    )
)


fig.show()
