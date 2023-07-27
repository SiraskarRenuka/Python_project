from bokeh.plotting import figure,output_file,show,ColumnDataSource
import pandas as pd
from bokeh.models.tools import HoverTool
from bokeh.transform import factor_cmap
from bokeh.palettes import Blues8

# read data from csv file
df = pd.read_csv('cars.csv')

# create columnDatasource from data frame
source = ColumnDataSource(df)

#call html file
output_file('index.html')

#create variable for car list and get data from 
car_list = source.data['Car'].tolist()

#add plot for data visualization
p = figure( 
    y_range =car_list,
    plot_width=800,
    plot_height=600,
    title='Cars With Top Horsepower', 
    x_axis_label='Horsepower',
    tools='pan,box_select,zoom_in,zoom_out,save,reset'
    )

#Render glyph
p.hbar(
    y='Car',
    right='Horsepower',
    left=0,
    height=0.4,
    fill_color=factor_cmap(
        'Car',
        palette=Blues8,
        factors=car_list
    ),
    fill_alpha=0.9,
    source=source,
    legend = 'Car'
)

# Add legend
p.legend.orientation = 'vertical'
p.legend.location = 'top_right'
p.legend.label_text_font_size = '10px'

# Add Tooltips
hover = HoverTool()
hover.tooltips = """
    <div>
        <h3>@Car</h3>
        <div><strong>Price: </strong>@Price</div>
        <div><strong>HP: </strong>@Horsepower</div>
        <div><img src="@Image" alt="Image not available" width="200"/></div>
    </div>
"""
p.add_tools(hover)

#show result
show(p)

