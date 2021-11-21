from bokeh.plotting import figure, row, column
from bokeh.io import curdoc
from bokeh.util.hex import hexbin
from bokeh.transform import linear_cmap
from bokeh.palettes import all_palettes
from bokeh.layouts import layout
from bokeh.models import Slider
import numpy as np

n_points = 100000
scale = 0.5
scale_b = 0.5
global g3, g4

def generate_data():
    xs = np.random.normal(scale = scale, size = n_points)
    ys = np.random.normal(scale = scale_b, size = n_points)
    histx, binsx = np.histogram(xs, bins=100, density=True)
    histy, binsy = np.histogram(ys, bins=100, density=True)
    bix = []
    biy = []
    for i in range(len(binsx)-1):
        bix.append((binsx[i]+binsx[i+1])/2)
    for i in range(len(binsy)-1):
        biy.append((binsy[i]+binsy[i+1])/2)
    data = {'xs': xs, 'ys': ys}
    datax = {'hx': histx, 'bx': bix}
    datay = {'hy': histy, 'by': biy}
    return data, datax, datay

def callback(attr, old, new):
    global n_points, scale, scale_b
    n_points = points_slider.value
    scale = scale_slider.value
    scale_b = scale_b_slider.value
    data, datax, datay = generate_data()
    g1.data_source.data = data
    binned_data = hexbin(data['xs'], data['ys'], 0.01)
    cmap = linear_cmap('counts', 'Turbo256', 0, max(binned_data['counts']))
    g2.glyph.fill_color = cmap
    g2.data_source.data = binned_data
    g3.data_source.data = datax
    g4.data_source.data = datay

data, datax, datay = generate_data()

points_slider = Slider(start = 1000, end = 1000000, step = 1000, value = n_points, title = 'punkty', width = 300)
scale_slider = Slider(start = 0.01, end = 1, step = 0.01, value = scale, title = 'skala x', width = 300)
scale_b_slider = Slider(start = 0.01, end = 1, step = 0.01, value = scale_b, title = 'skala y', width = 300)

f1 = figure(match_aspect = True)
g1 = f1.circle('xs', 'ys', source = data, alpha = 0.01)

binned_data = hexbin(data['xs'], data['ys'], 0.01)
cmap = linear_cmap('counts', 'Turbo256', 0, max(binned_data['counts']))
f2 = figure(match_aspect = True)
f2.background_fill_color = all_palettes['Turbo'][256][0]
f2.grid.visible = False
g2 = f2.hex_tile(size = 0.01, source = binned_data, fill_color = cmap, line_color = None)

f3 = figure(match_aspect = True)
g3 = f3.circle('bx', 'hx', source = datax)

f4 = figure(match_aspect = True)
g4 = f4.circle('by', 'hy', source = datay)

l = layout([column(points_slider, scale_slider, scale_b_slider), row(f1, f2), row(f3, f4)], sizing_mode = 'stretch_width')

points_slider.on_change('value_throttled', callback)
scale_slider.on_change('value_throttled', callback)
scale_b_slider.on_change('value_throttled', callback)

curdoc().add_root(l)
