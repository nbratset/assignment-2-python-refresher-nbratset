from my_utils import get_column
country='United States of America'
county_column = 0
# fires_column = 3  # optional integer (index) or string handling for fires_column
fires_column = 'Forest fires'
file_name = 'Agrofood_co2_emission.csv'
fires = get_column(file_name,county_column,country,fires_column)
print(fires)