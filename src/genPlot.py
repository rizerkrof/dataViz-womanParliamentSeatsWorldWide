# Python 3.8
import pandas as pd
import plotly.express as px
import utils

# import data
df = pd.read_csv('../data/Viz5_August_Female_Political_Representation.csv')

# add continents
df["Continent"] = df["Country Code"].apply(utils.country_to_continent)
df = df[df.Continent != 'error']

#To have bests countries rendered mostly on top
df.sort_values(by=['Year', 'Proportion of seats held by women in national parliaments (%)'], inplace=True, ascending=[True, False])

#add mean data for each continent
dfConcat = pd.DataFrame()
for continent in ["Europe", "Asia", "Africa", "Oceania", "South America", "North America"]:
    # get data only for the continent 
    dfCountry = df[df.Continent == continent]
    #calculate mean data
    dfMeanCountry = dfCountry.groupby(['Year']).mean().reset_index()
    dfMeanCountry["CountryName"] = continent
    dfMeanCountry["Continent"] = continent
    dfMeanCountry["Country Code"] = continent
    # adding the new mean data to the df
    dfConcat = pd.concat([dfMeanCountry, dfConcat])
    
df = pd.concat([df, dfConcat])

# plot
fig = px.line(
    df,
    x="Year",
    y="Proportion of seats held by women in national parliaments (%)",
    line_group="CountryName",
    facet_col="Continent"
)

# default line color 
fig.update_traces(line_color='#dedede', line_width=2)

# let's highlight bests and mean
highLightWidth = 12
highLightColor = "#ff2600"
meanWidth = 9
meanColor = "#000000"

# highlight bests
for country in ["Rwanda", "Bolivia", "New Zealand", "United Arab Emirates", "Sweden", "Cuba"]:
    fig.data[utils.getFigDataIndexFromCountryName(fig, country)].line.color = highLightColor
    fig.data[utils.getFigDataIndexFromCountryName(fig, country)].line.width = highLightWidth

# highlight mean
for mean in ["Europe", "Asia", "Africa", "North America", "South America", "Oceania"]:
    fig.data[utils.getFigDataIndexFromCountryName(fig, mean)].line.color = meanColor
    fig.data[utils.getFigDataIndexFromCountryName(fig, mean)].line.width = meanWidth

#set dimensions
fig.update_layout (
    plot_bgcolor =  'rgba(0,0,0,0)',
    width=2000,
    height=800
)

fig.show()
