
## Part 1: Plotting with matplotlib

Refer to today's [lecture files](https://github.com/zipfian/DSI_Lectures/blob/master/pandas-seaborn) for more examples. You may also find these links useful:
- [matplotlib tutorial](http://matplotlib.org/users/pyplot_tutorial.html)
- [More about matplotlib's Figure and Axes classes](http://matplotlib.org/users/artists.html)
- [Seaborn tutorial](https://web.stanford.edu/~mwaskom/software/seaborn/tutorial.html)
- [Plotting with pandas](http://pandas.pydata.org/pandas-docs/version/0.15.0/visualization.html)

Start your file with these imports
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```
If you are working in an ipython notebook, add the line
```python
%matplotlib inline
```

If you are running a script, call ```plt.figure()``` before each figure and ```plt.show()``` after each one.


#### Pro tip zone
- You can change the default style of your plots with ```plt.style.use()```. You can view your options with ```plt.style.available```
- Use ```plt.title()```, ```plt.xlabel()```, and ```plt.ylabel()``` to specify axis labels and plot titles
- Use ```plt.xlim()```, ```plt.ylim()```, and/or ```plt.axis()``` to change the range of values displayed on your plot. These functions take lists as arguments: ```[xmin, xmax]```, ```[ymin, ymax]```, and ```[xmin, xmax, ymin, ymax]``` respectively.


#### These tasks should help familiarize you with the matplotlib basics

1. The following code generates two arrays populated with integers from 0 to 999
  ```python
  a = np.random.randint(1000, size=50)
  b = np.random.randint(1000, size=50)
  ```
  Make a scatterplot of a vs. b, and give the points different colors based on whether or not the sum of a and b for that point is even.  

 #### Pro tip zone
   - The ```c``` keyword argument of ```plt.scatter()``` accepts an array of the same length as your data specifying a color for each point, either as a string (such as ```'r'``` or ```'b'```) or as a number to which a colormap is applied (you can use the  ```cmap``` keyword argument to specify which colormap to use; pick your favorite [here](http://matplotlib.org/examples/color/colormaps_reference.html)). You can even pass it an array of booleans, since ```True``` will be treated as ```1``` and ```False``` as ```0```. Very useful for dichotomously categorized data! Use ```plt.colorbar()``` to display the colormap on the plot.

1. Plot the functions ```y = 3x + 0.5``` and ```y = 5*sqrt(x)``` on the same figure for values of `x` between 0 and 5. Remember that ```plt.plot()``` takes an array of x-values and an array of y-values. You may find ```np.arange()``` or ```np.linspace()``` helpful.
 - Add a legend using ```plt.legend()```. Note that you'll have to specify ```label='something'``` for each ```plt.plot()``` command.
 - How does this graph look with x and/or y on a log scale? Use ```plt.xscale()```
 - Change the color, [line style](http://matplotlib.org/api/lines_api.html#matplotlib.lines.Line2D.set_linestyle) and [marker style](http://matplotlib.org/api/markers_api.html#module-matplotlib.markers) using the "format string" shorthand.  
 For example, ```plt.plot(x, y, 'k--*')``` would plot a black (```'k'```) dashed (```'--'```) line with asterisks (```'*'```) at each point.

1. The following code generates a bar plot
 ```python
 barheights = [3,5,1]
 barlabels = ['grapes', 'oranges', 'hockey pucks']
 plt.bar(np.arange(len(barheights)), barheights)
 plt.xticks(np.arange(len(barheights)), barlabels, rotation=45)
 plt.show()
 ```
 How would you change the x-position of the labels?

1. Make a 2x2 subplot of four plots so far.
  ```python
  plt.figure(figsize=(8,8)) # use this to change the size of the figure

  plt.subplot(2, 2, 1) # (rows, columns, subplot index)
  ### plotting code here

  plt.subplot(2, 2, 2)
  ### plotting code here

  plt.subplot(2, 2, 3)
  ### plotting code here

  plt.subplot(2, 2, 4)
  ### plotting code here

  plt.tight_layout() # ensures that plot titles and axis labels don't overlap
  plt.show()
  ```

1. Save the last figure using ```plt.savefig()```

## Part 2: Bike Share Data
You will be exploring and graphing the data from the Bay Area Bike Share. The data directory contains a README with further explanation.
```
data/bay_area_bikeshare/README.txt
```
Let's start out by looking at some weather data. Use your bash shell's ```head``` command (which you can access in ipython by prepending with a bang, i.e.  ```!head```) to look at the first few lines of this file:
```
data/bay_area_bikeshare/201402_weather_data_v2.csv
```
The first line is all column labels. The following code will turn that into an easy-to-access list.
```python
with open('data/bay_area_bikeshare/201402_weather_data_v2.csv') as f:
    labels = f.readline().strip().split(',')
[(i, label) for i, label in enumerate(labels)]
```

```
[(0, 'date'),
 (1, 'max_temperature_f'),
 (2, 'mean_temperature_f'),
 (3, 'min_temperature_f'),
 (4, 'max_dew_point_f'),
 (5, 'mean_dew_point_f'),
 (6, 'min_dewpoint_f'),
 (7, 'max_humidity'),
 (8, 'mean_humidity'),
 (9, 'min_humidity'),
 (10, 'max_sea_level_pressure_in'),
 (11, 'mean_sea_level_pressure_in'),
 (12, 'min_sea_level_pressure_in'),
 (13, 'max_visibility_miles'),
 (14, 'mean_visibility_miles'),
 (15, 'min_visibility_miles'),
 (16, 'max_wind_speed_m_p_h'),
 (17, 'mean_wind_speed_m_p_h'),
 (18, 'max_gust_speed_m_p_h'),
 (19, 'precipitation_in'),
 (20, 'cloud_cover'),
 (21, 'events'),
 (22, 'wind_dir_degrees'),
 (23, 'zip')]
```
#### Importing data with numpy
1. Let's import a subset of these columns into a numpy array. While it appears that everything except 'date' is numerical, the precipitation column occasionally contains the string 'T' for 'trace amounts'. For sanity reasons, let's avoid putting strings in a numpy array.
  ```python
  cols = [2, 5, 8, 11, 14, 17]
  filepath = 'data/bay_area_bikeshare/201402_weather_data_v2.csv'
  weather = np.loadtxt(filepath, delimiter=',', skiprows=1, usecols=cols)
  ```

1. Make some scatterplots and histograms using some of these columns. Sometimes you have to change the number of ```bins``` in ```plt.hist()``` to get something informative.

#### Importing data with pandas
1. Pandas will conveniently label the columns automatically. How nice!  
  ```df_weather = pd.read_csv(filepath)```  
  Scope it out with ```df_weather.head()```

1. Pandas dataframes have plotting functions as methods, so you can call
  ```python
  df_weather.plot(kind='scatter', x='column name', y='another column name')
  ```
  and
  ```python
  df_weather['some column'].hist()
  ```
  Try it out!


#### Explore!
Import the trip data and station data into pandas dataframes and dive deep!

1. Create a graph that is based on data from only one of the columns of the original data.  For example, this might be a histogram of that data.

2. Create a graph that is based on data from only two columns of the original data.  This might be a scatterplot, a faceted histogram, etc.

3. Create graph that is based on data from at least 3 columns of the original data.  This could be a colored scatterplot, a scatterplot matrix, faceted histograms, etc.

For each of the three parts, your goal should be to create the most interesting or insightful graph you can, given the constraints on how much data is used.  Create a separate document that explains why you find each graph insightful and/or what you learn from the results.


#### Extra credit: plotting vs date
Import the weather data again but tell pandas to parse the date column as a ```DateTime``` object and set it as the index.

```python
df_weather = pd.read_csv(filepath,parse_dates=['date'], index_col='date')
```
Now you can plot a column over time with
```python
df_weather['column'].plot()
```
Note that there are multiple zip codes in the data, with the date repeated for each one, so you'll have to either subset or aggregate the data accordingly before you plot the time trace.
