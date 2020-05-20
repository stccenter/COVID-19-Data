# STC COVID-19 Dataset

This data repository stores COVID-19 virus case and related natural and social factors (e.g. environmental observation, policy index) in multi-scale based on ISO standard.

## Data Organization
Datasets are organized by region area ranging from global to countries as shown below. Underneath each folder, multi-scale daily reports and summary reports are provided separately.

## Field description

### Daily data
Daily data provides automatically updated information of COVID-19 cases, and related attributes daily.

| Attribute Name | Description                                                  | Format               | Example |
| :------------- | ------------------------------------------------------------ | -------------------- | ------- |
| date           | The date representing the current day in which the data represents. UTC time is used for this dataset, all values will calculated before the end of UTC time of the date. | Date (YYYY/MM/DD) in UTC | 2020/04/09 |
| country_name | Name of the country.                               | string               | United States |
| iso3           | 3 digit ISO country codes.                                   | varchar(3)           | USA |
| admin1_name    | The name for admin 1 level.  | string               | Virginia |
| hasc1 | This will represent the Hierarchical administrative subdivision codes (HASC) for admin 1 level. | string | US.VA (for Virginia, United States) |
| local_id1 | This will represent the ID for specific admin 1 level. ID that represents the country's admin 1 level | string | VA (for Virginia, United States) |
| admin2_name | The name for admin 2 level. | string | Fairfax County |
| hasc2 | This will represent the Hierarchical administrative subdivision codes (HASC) for admin 2 level. | string | US.VA.FX (for Fairfax, Virginia, United States) |
| local_id2 | This will represent the ID for specific admin 2 level. ID that represents the country's admin 2 level. | string | 51059 (for Fairfax, Virginia, United States) |
| confirmed | The number of confirmed cases. | integer | 777 |
| death | The number of death cases. | integer | 19 |
| recovered | The number of recovered cases. (might be null for admin 2 level) | integer | null |
| Miscellaneous | Other data attributed to our dataset. | TBD | TBD |



### Summary data

Summary data records the COVID-19 cases, and related attributes, to show the timeline of cases.

| Attribute Name | Description                                                  | Format     | Example |
| -------------- | ------------------------------------------------------------ | ---------- | ------- |
| country_name | Name of the country.                               | string               | "US" |
| iso3           | 3 digit ISO country codes.                                   | varchar(3) |   USA      |
| admin1_name    | The name for admin 1 level.  | string               | State for USA |
| date           | The date representing the current day in which the data represents. UTC time is used for this dataset, all values will calculated before the end of UTC time of the date. | UTC | YYYY/MM/DD |

## Tutorial - Visulize Virus Cases on Map using QGIS
[<img src="https://dl.dropboxusercontent.com/s/fjursbp8dwjpnkp/qgis_join_tutorial.jpg" width="60%">](https://www.youtube.com/watch?v=VzaBCje7OGk)


## Overall data sources by Country

| Country / Area                                             | Data Source                                                                                                                                                                                                         |   
|------------------------------------------------------------|---------------------------------|
| Global                                                   | [![](https://img.shields.io/badge/source-Johns_Hopkins_CSSE_-9cf)](https://github.com/CSSEGISandData/) |  
| China                                                   | [![](https://img.shields.io/badge/source-Ding_Xiang_Yuan_-9cf)](https://ncov.dxy.cn/ncovh5/view/pneumonia?source=) | 
| United States                                              | [![](https://img.shields.io/badge/source-Johns_Hopkins_CSSE_-9cf)](https://github.com/CSSEGISandData/)  [![](https://img.shields.io/badge/source-USAFACTS_-9cf)](https://usafacts.org/visualizations/coronavirus-covid-19-spread-map/)  | 
| Canada                                                     | [![](https://img.shields.io/badge/source-Johns_Hopkins_CSSE_-9cf)](https://github.com/CSSEGISandData/) |
| Australia                                                  |[![](https://img.shields.io/badge/source-Johns_Hopkins_CSSE_-9cf)](https://github.com/CSSEGISandData/) |
| Italy                                                      | [![](https://img.shields.io/badge/source-protezionecivile.it-9cf)](http://www.protezionecivile.it/)   | 
| Germany                                                    | [![](https://img.shields.io/badge/source-covid19--eu--data-9cf)](https://github.com/covid19-eu-zh/covid19-eu-data)   |  
| Austria                                                    | [![](https://img.shields.io/badge/source-sozialministerium.at-9cf)](https://www.sozialministerium.at/public.html) |  
| Brazil                                                     | [![](https://img.shields.io/badge/source-covid.saude.gov.br-9cf)](https://covid.saude.gov.br/)        |  
| Chile                                                      | [![](https://img.shields.io/badge/source-Covid--19_Latinoamérica-9cf)](https://datastudio.google.com/u/0/reporting/9b824956-4055-46da-8c40-0d46ded5ffba/page/QkcKB) |  
| Japan                                                      | [![](https://img.shields.io/badge/source-covid--2019.live-9cf)](https://covid-2019.live/en/)  |   
| Russia                                                     |  [![](https://img.shields.io/badge/source-yandex.ru-9cf)](https://yandex.ru/maps/covid19?ll=41.775580%2C54.894027&z=3) |   
| South Africa                                               |[![](https://img.shields.io/badge/source-NICD-9cf)](https://www.nicd.ac.zamedia/)  [![](https://img.shields.io/badge/source-health.gov.za-9cf)](https://www.nicd.ac.zamedia/) ||   


## People Contribution & Credit

- Phil Yang, PI and supervisor.
- Wendy Guan, Co-PI
- Shuming Bao, colloborator
- Dexuan Sha, project leader, metadata and standard design, crawler and ETL development, operation management.
- Yun Li, GitHub management, data report generation and quality control.
- Qian Liu, Environmental factor design, acquisition and preprocessing.
- Chen Zhong, data crawler and ETL development.
- You Zhou, policy, news and publication collection, coding, and labelling. Daily operation and data quality control.
- Yifei Tian, data crawler and ETL development.
- Fayez Beaini, data source collection and evaluation, quality control. 
- Tao Hu, cooperation leader from Harvard University and China Data Lab.
- Zifu Wang and Hai Lan, IT infrastructure and network security support.
- Zhiran Zhang, visualization 
- Wei Liu, data processing
- Akhil Kumar, data validation.
- Andrew Ding, data validation.
- Jerry Sun, data validation.
- Swetha Bhattaram, data validation.
- Yogya Kalra, data validation.

## Disclaimer
All data in this repository was collected/calculated/calibrated from multiple publicly available data sources that do not always agree. While we'll try our best to keep the information up to date and correct, we make no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, with respect to the data. We do not bear any legal responsibility for any consequence caused by the usage of data provided. Reliance on the data for medical guidance or use of the data in commerce is strictly prohibited. NSF STcenter hereby disclaims any and all representations and warranties with respect to the data repository, including accuracy, fitness for use, and merchantability. 
