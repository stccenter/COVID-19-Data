<!--
 * @Author: your name
 * @Date: 2020-05-20 13:39:28
 * @LastEditTime: 2020-06-03 14:31:43
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \github_test\README.md
--> 
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

## Tutorial - Visualize Virus Cases on Map using QGIS
[<img src="https://dl.dropboxusercontent.com/s/fjursbp8dwjpnkp/qgis_join_tutorial.jpg" width="60%">](https://www.youtube.com/watch?v=VzaBCje7OGk)


## Overall data sources by Country

![](https://img.shields.io/badge/source-data_source_-9cf)  ![](https://img.shields.io/badge/source-validaiton_source_-orange)
| Country / Region                                           | Continent                 | Admin level  |   DataSource                                                                                           |   
|----------------------------------------------------------|---------------------------|--------------|--------------------------------------------------------------------------------------------------------|
| Global                                                   |  Global                   | 0            | [![](https://img.shields.io/badge/source-Johns_Hopkins_CSSE_-9cf)](https://github.com/CSSEGISandData/) [![](https://img.shields.io/badge/source-WHO_-orange)](https://covid19.who.int/?gclid=CjwKCAjwtqj2BRBYEiwAqfzur8E04Dtrt6iZ7eQa9fojCCcZiwlPSNI6pPVog4PQlBiYNwupjhfF-BoCmvYQAvD_BwE)| 
| United States                                            |  North America            | 1 , 2     | [![](https://img.shields.io/badge/source-Johns_Hopkins_CSSE_-9cf)](https://github.com/CSSEGISandData/)  [![](https://img.shields.io/badge/source-USAFACTS_-9cf)](https://usafacts.org/visualizations/coronavirus-covid-19-spread-map/)  [![](https://img.shields.io/badge/source-CDC.gov-orange)](https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html) | 
| China                                                    | Asia                      | 1         | [![](https://img.shields.io/badge/source-Ding_Xiang_Yuan_-9cf)](https://ncov.dxy.cn/ncovh5/view/pneumonia?source=) [![](https://img.shields.io/badge/source-NHC-orange)]([![](http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml)) | 
| Canada                                                   | North America             | 1          |[![](https://img.shields.io/badge/source-Johns_Hopkins_CSSE_-9cf)](https://github.com/CSSEGISandData/) [![](https://img.shields.io/badge/source-canada.ca_-orange)](https://www.canada.ca/en/public-health/services/diseases/coronavirus-disease-covid-19.html)|
| Australia                                                | Oceania                   | 1          |[![](https://img.shields.io/badge/source-Johns_Hopkins_CSSE_-9cf)](https://github.com/CSSEGISandData/) [![](https://img.shields.io/badge/source-health.gov.au-orange)](https://www.health.gov.au/news/health-alerts/novel-coronavirus-2019-ncov-health-alert/coronavirus-covid-19-current-situation-and-case-numbers) |
| Italy                                                    | Europe                    | 1          | [![](https://img.shields.io/badge/source-protezionecivile.it-9cf)](http://www.protezionecivile.it/)   [![](https://img.shields.io/badge/source-world0meters_-orange)](https://www.worldometers.info/coronavirus/country/italy/)  | 
| Germany                                                  | Europe                    | 1          | [![](https://img.shields.io/badge/source-covid19--eu--data-9cf)](https://github.com/covid19-eu-zh/covid19-eu-data) [![](https://img.shields.io/badge/source-rki.de-orange)](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html) |  
| Austria                                                  | Europe                    | 1          |[![](https://img.shields.io/badge/source-sozialministerium.at-9cf)](https://www.sozialministerium.at/public.html) [![](https://img.shields.io/badge/source-sozialministerium.at-orange)](https://www.sozialministerium.at/Informationen-zum-Coronavirus/Neuartiges-Coronavirus-(2019-nCov).html)|  
| Brazil                                                   | South America             | 1          |[![](https://img.shields.io/badge/source-covid.saude.gov.br-9cf)](https://covid.saude.gov.br/)   [![](https://img.shields.io/badge/source-covid.saude.gov.br-orange)](https://covid.saude.gov.br/)       |  
| Chile                                                    | South America             | 1          | [![](https://img.shields.io/badge/source-Covid--19_Latinoamérica-9cf)](https://datastudio.google.com/u/0/reporting/9b824956-4055-46da-8c40-0d46ded5ffba/page/QkcKB)  [![](https://img.shields.io/badge/source-minsal.cl-orange)](https://www.minsal.cl/nuevo-coronavirus-2019-ncov/casos-confirmados-en-chile-covid-19/)|  
| Japan                                                    | Asia                      | 1          | [![](https://img.shields.io/badge/source-covid--2019.live-9cf)](https://covid-2019.live/en/)   [![](https://img.shields.io/badge/source-stopcovid.jp-orange)](https://www.stopcovid19.jp/) |   
| Russia                                                   | Europe                    | 1          | [![](https://img.shields.io/badge/source-yandex.ru-9cf)](https://yandex.ru/maps/covid19?ll=41.775580%2C54.894027&z=3)  [![](https://img.shields.io/badge/source-стопкоронавирус.рф-orange)](https://xn--80aesfpebagmfblc0a.xn--p1ai/information/)|   
| South Africa                                             | Africa                    | 1          |[![](https://img.shields.io/badge/source-NICD-9cf)](https://www.nicd.ac.zamedia/)  [![](https://img.shields.io/badge/source-health.gov.za-9cf)](https://www.nicd.ac.zamedia/)  [![](https://img.shields.io/badge/source-statssa.gov.za-orange)](http://www.statssa.gov.za/) |  
| Croatia                                                   |Europe                     | 1          |[![](https://img.shields.io/badge/source-koronavirus.hr-9cf)](https://koronavirus.hr/) [![](https://img.shields.io/badge/source-koronavirus.hr-orange)](https://koronavirus.hr/) |



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
