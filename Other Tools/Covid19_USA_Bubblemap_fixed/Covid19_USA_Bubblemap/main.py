import pandas as pd
import csv
from contextlib import closing
import codecs
import requests
from lib.geo_choroplethmap import choroplethmap
from lib.plot import png2gif, addtext

# read raw data file
def readCountyData():   
    #df = pd.read_csv(epidemic_file, sep=',')
    url = 'https://raw.githubusercontent.com/stccenter/COVID-19-Data/master/US/County_level_summary/US_County_summary_covid19_confirmed.csv'
    county_number = {} # the number of confirmed cases for each county every day
    with closing(requests.get(url, stream=True)) as r:
        reader = csv.reader(codecs.iterdecode(r.iter_lines(), 'utf-8'))
        lines = list(reader)
        header, values = lines[0], lines[1:]
        for row in values:
            number = []
            for i in row[3:]:
                if int(i) <= 0 or int(i) > 20:
                    number.append(int(i))
                elif int(i) > 0 and int(i) <= 20:
                    number.append(20)                    
            county_number[row[1]] = number #=list(map(int, row[2:]))
    return county_number, header

# obtain the coordinates for each county
def readCoordinate():
    # print(coordinate_file)
    data = pd.read_csv(coordinate_file, names = ['State','Name','Hasc','FIPS','Longitude','Latitude'], 
                     header = None, skiprows=1)
    county_info = [] # [['lat','lon','20200122','20200123',...],[],...]
    for i in range(len(data)):
        county_Hasc = data.iloc[i]['Hasc']
        if county_Hasc in county_number:
            county_info.append([data.iloc[i]['Latitude'], data.iloc[i]['Longitude']] + county_number[county_Hasc])
    return county_info

def selectDate(date):
    selected_date = []
    #reverse_date = list(reversed(date))
    for i in range(len(date)):
        if i%4 == 0:
            selected_date.append(date[i])            
    return selected_date
    
def main():
    date = columns_name[3:]
    analyze_date = date[date.index(from_date):]
    
    # legend data
    legend_info = []
    legend_info.append([23.5,-72.4] + number_days * [20])    
    legend_info.append([24.6,-72.1] + number_days * [100])    
    legend_info.append([26,-71.7] + number_days * [1000])
    legend_info.append([28,-71.1] + number_days * [10000])
    legend_info.append([32,-69.8] + number_days * [50000])
    
    # Bubble map data
    for_map = pd.DataFrame(county_info, columns = ['lat', 'lon'] + date)#all data
    for_legend = pd.DataFrame(legend_info, columns = ['lat', 'lon'] + date)
    for date in analyze_date:
        print("The current date is: " + date)
        choroplethmap(for_map[['lat', 'lon', date]], for_legend, date, image_path)
    
    # add legend text on each .png
    addtext(analyze_date, image_path)
   
    # generate gif
    # selected_date = selectDate(date)
    # png2gif(image_path, selected_date, gif_name, 600)

if __name__ == '__main__':
    data_path = './data/'
    image_path = './images/'
    gif_npath = './gif/'
    
    epidemic_file = data_path + 'county_confirmed.csv'
    coordinate_file = data_path + 'county_coordinate.csv'
    gif_name = gif_npath + 'county_bubblemap.gif'
    from_date = '2021-01-01' #map analyze from this day
    
    county_number, columns_name = readCountyData()
    county_info = readCoordinate()
    # print(county_info)
    number_days = len(county_info[0]) - 2 # number of days
    
    main()