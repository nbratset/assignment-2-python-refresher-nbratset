from my_utils import get_column
country='United States of America'
county_column = 0
fires_column = 4
file_name = 'Agrofood_co2_emission.csv'
fires = get_column(file_name,county_column,country,fires_column)
print(fires)