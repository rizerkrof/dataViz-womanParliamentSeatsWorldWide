# Python 3.8
import pycountry_convert as pc
import pycountry

def country_to_continent(country_alpha3):
    try:
        country_alpha2 = pycountry.countries.lookup(country_alpha3).alpha_2
        country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
        country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
        return country_continent_name
    except:
        return 'error'

# function to get the trace index by country for highlighting
def getFigDataIndexFromCountryName(fig, targetCountryName):
    for i in range(len(fig.data)):
        hoverTemplateAttributeList = fig.data[i].hovertemplate.split("<br>")
        countryName = hoverTemplateAttributeList[1].split("=")[1]
        if countryName == targetCountryName:
            return i
    pass
