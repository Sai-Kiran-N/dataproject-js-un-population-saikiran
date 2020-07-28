import json
from csv import reader
from collections import defaultdict


def csv_reader(file_name, asean_countries, saarc_countries):
    with open(file_name, 'r') as csv_object:
        csv_data = list(reader(csv_object))
        asean_countries_dict = defaultdict(dict)
        saarc_countries_dict = defaultdict(int)
        india_population = dict()
        for row in csv_data[1:]:
            country = row[0]
            year = int(row[2])
            population = float(row[3])
            if year > 2000:
                if country in asean_countries:
                    asean_countries_dict[country][year] = population
                elif country in saarc_countries:
                    if country == 'India':
                        india_population[year] = population
                    saarc_countries_dict[year] += population
        return asean_countries_dict, saarc_countries_dict, india_population


def plot1(india_population):
    year_list = list(range(2001, 2016))
    population = list(india_population.values())
    data = {}
    data['x_axis_points'] = year_list
    data['x_axis_title'] = 'Year'
    data['title'] = 'India population over years (2001-15)'
    data['plot_data'] = [{'name': 'Population', 'data': population}]
    data['y_axis_title'] = 'Population'
    with open('./json/plot1.json', 'w') as json_object:
        json_object.write(json.dumps(data, indent=4))


def plot2(asean_countries, asean_countries_dict):
    population = [
        [country, asean_countries_dict[country][2014]]
        for country in asean_countries]
    data = {}
    data['title'] = 'Population of ASEAN countries (2014)'
    country_list = list(asean_countries.values())
    data['x_axis_title'] = 'ASEAN countries'
    data['y_axis_title'] = 'Population'
    data['x_axis_points'] = country_list
    data['plot_data'] = [{'name': 'Population', 'data': population}]
    with open('./json/plot2.json', 'w') as json_object:
        json_object.write(json.dumps(data, indent=4))


def plot3(saarc_countries_dict):
    year_list = list(range(2001, 2016))
    population = [saarc_countries_dict[year] for year in year_list]
    data = {}
    data['x_axis_points'] = year_list
    data['x_axis_title'] = 'Year'
    data['title'] = 'Total population of SAARC countries'
    data['plot_data'] = [{'name': 'Population', 'data': population}]
    data['y_axis_title'] = 'Population'
    with open('./json/plot3.json', 'w') as json_object:
        json_object.write(json.dumps(data, indent=4))


def plot4(asean_countries, asean_countries_dict):
    year_list = list(range(2011, 2016))
    population = []
    for country in asean_countries:
        temp_list = []
        for year in year_list:
            temp_list.append(
                ['population', asean_countries_dict[country][year]])
        population.append(
            {'name': asean_countries[country], 'data': temp_list})
    data = {}
    data['x_axis_points'] = year_list
    data['x_axis_title'] = 'Year'
    data['title'] = 'Grouped Bar chart (ASEAN population vs year)'
    data['plot_data'] = population
    data['y_axis_title'] = 'Population'
    with open('./json/plot4.json', 'w') as json_object:
        json_object.write(json.dumps(data, indent=4))


if __name__ == '__main__':
    asean_countries = {
        'Brunei Darussalam': 'Brunei', 'Cambodia': 'Cambodia',
        'Indonesia': 'Indonesia',
        "Lao People's Democratic Republic": 'Lao PDR',
        'Malaysia': 'Malaysia',
        'Myanmar': 'Myanmar', 'Philippines': 'Philippines',
        'Singapore': 'Singapore', 'Thailand': 'Thailand',
        'Viet Nam': 'Viet Nam'
    }
    saarc_countries = [
        'Afghanistan', 'Bangladesh', 'Bhutan', 'India',
        'Maldives', 'Nepal', 'Pakistan', 'Sri Lanka'
    ]

    csv_file_name = 'population-estimates_csv.csv'
    asean_countries_dict, saarc_countries_dict, \
        india_population = csv_reader(
            csv_file_name, asean_countries, saarc_countries)
    plot1(india_population)
    plot2(asean_countries, asean_countries_dict)
    plot3(saarc_countries_dict)
    plot4(asean_countries, asean_countries_dict)
