<!--
 * @Author: your name
 * @Date: 2020-05-20 13:39:28
 * @LastEditTime: 2020-12-02 12:42:38
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit
 * @FilePath: \github_test\README.md
--> 
# STC COVID-19 Dataset

This data repository stores COVID-19 virus case and related natural and social factors (e.g. environmental observation, policy index) in multi-scale based on ISO standard.

## Data Organization
Datasets are organized by region area ranging from global to countries as shown below. Underneath each folder, multi-scale daily reports and summary reports are provided separately.

## Field Description

### Daily Data
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



### Summary Data

Summary data records the COVID-19 cases, and related attributes, to show the timeline of cases.

| Attribute Name | Description                                                  | Format     | Example |
| -------------- | ------------------------------------------------------------ | ---------- | ------- |
| country_name | Name of the country.                               | string               | "US" |
| iso3           | 3 digit ISO country codes.                                   | varchar(3) |   USA      |
| admin1_name    | The name for admin 1 level.  | string               | State for USA |
| date           | The date representing the current day in which the data represents. UTC time is used for this dataset, all values will calculated before the end of UTC time of the date. | UTC | YYYY/MM/DD |

## Tutorial - Visualize Virus Cases on Map using QGIS
[<img src="https://dl.dropboxusercontent.com/s/fjursbp8dwjpnkp/qgis_join_tutorial.jpg" width="60%">](https://www.youtube.com/watch?v=VzaBCje7OGk)


## Overall Data Sources by Country
##### Legend for data source and operation status
 ![](https://img.shields.io/badge/source-data_source_-9cf)  ![](https://img.shields.io/badge/source-validaiton_source_-orange) ![](https://img.shields.io/badge/status-passing-greeen) ![](https://img.shields.io/badge/status-pause-yellow)
| Country / Region                                           | Continent                 | Admin level  |   Data Source                                                                                           |   Temporal Coverage |   Operation Status |
|----------------------------------------------------------|---------------------------|--------------|--------------------------------------------------------------------------------------------------------|--------------|----------------------------------------------------------|
| Global                                                   |  Global                   | 0            | [![](https://img.shields.io/badge/source-Johns_Hopkins_CSSE_-9cf)](https://github.com/CSSEGISandData/) [![](https://img.shields.io/badge/source-WHO_-orange)](https://covid19.who.int/?gclid=CjwKCAjwtqj2BRBYEiwAqfzur8E04Dtrt6iZ7eQa9fojCCcZiwlPSNI6pPVog4PQlBiYNwupjhfF-BoCmvYQAvD_BwE)| 2020/1/22 to current|  ![](https://img.shields.io/badge/status-passing-greeen)|
| United States                                            |  North America            | 1 , 2     | [![](https://img.shields.io/badge/source-Johns_Hopkins_CSSE_-9cf)](https://github.com/CSSEGISandData/)  [![](https://img.shields.io/badge/source-USAFACTS_-9cf)](https://usafacts.org/visualizations/coronavirus-covid-19-spread-map/)  [![](https://img.shields.io/badge/source-CDC.gov-orange)](https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html) | admin0: 2020/1/22 to current, admin1: 2020/1/27 to current|  ![](https://img.shields.io/badge/status-passing-greeen)|
| China                                                    | Asia                      | 1 , 2        | [![](https://img.shields.io/badge/source-Ding_Xiang_Yuan_-9cf)](https://ncov.dxy.cn/ncovh5/view/pneumonia?source=) [![](https://img.shields.io/badge/source-NHC-orange)]([![](http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml)) | admin0: 2020/1/22 to current, admin1: 2020/1/24 to current|  ![](https://img.shields.io/badge/status-passing-greeen)|
| Canada                                                   | North America             | 1          |[![](https://img.shields.io/badge/source-Johns_Hopkins_CSSE_-9cf)](https://github.com/CSSEGISandData/) [![](https://img.shields.io/badge/source-canada.ca_-orange)](https://www.canada.ca/en/public-health/services/diseases/coronavirus-disease-covid-19.html)| 2020/1/26 to current|  ![](https://img.shields.io/badge/status-passing-greeen)|
| Australia                                                | Oceania                   | 1          |[![](https://img.shields.io/badge/source-Johns_Hopkins_CSSE_-9cf)](https://github.com/CSSEGISandData/) [![](https://img.shields.io/badge/source-health.gov.au-orange)](https://www.health.gov.au/news/health-alerts/novel-coronavirus-2019-ncov-health-alert/coronavirus-covid-19-current-situation-and-case-numbers) | 2020/1/27 to current|  ![](https://img.shields.io/badge/status-passing-greeen)|
| Italy                                                    | Europe                    | 1 , 2          | [![](https://img.shields.io/badge/source-protezionecivile.it-9cf)](http://www.protezionecivile.it/)   [![](https://img.shields.io/badge/source-world0meters_-orange)](https://www.worldometers.info/coronavirus/country/italy/)  |  2020/2/24 to current|  ![](https://img.shields.io/badge/status-passing-greeen)|
| Germany                                                  | Europe                    | 1          | [![](https://img.shields.io/badge/source-covid19--eu--data-9cf)](https://github.com/covid19-eu-zh/covid19-eu-data) [![](https://img.shields.io/badge/source-rki.de-orange)](https://www.rki.de/DE/Content/InfAZ/N/Neuartiges_Coronavirus/Fallzahlen.html) |   2020/2/29 to current|  ![](https://img.shields.io/badge/status-passing-greeen)|
| Austria                                                  | Europe                    | 1          |[![](https://img.shields.io/badge/source-sozialministerium.at-9cf)](https://www.sozialministerium.at/public.html) [![](https://img.shields.io/badge/source-sozialministerium.at-orange)](https://www.sozialministerium.at/Informationen-zum-Coronavirus/Neuartiges-Coronavirus-(2019-nCov).html)|  2020/3/4 to current|  ![](https://img.shields.io/badge/status-passing-greeen)| 
| Brazil                                                   | South America             | 1          |[![](https://img.shields.io/badge/source-covid.saude.gov.br-9cf)](https://covid.saude.gov.br/)   [![](https://img.shields.io/badge/source-covid.saude.gov.br-orange)](https://covid.saude.gov.br/)       |   2020/2/26 to current|  ![](https://img.shields.io/badge/status-passing-greeen)|
| Chile                                                    | South America             | 1          | [![](https://img.shields.io/badge/source-Covid--19_Latinoamérica-9cf)](https://datastudio.google.com/u/0/reporting/9b824956-4055-46da-8c40-0d46ded5ffba/page/QkcKB)  [![](https://img.shields.io/badge/source-minsal.cl-orange)](https://www.minsal.cl/nuevo-coronavirus-2019-ncov/casos-confirmados-en-chile-covid-19/)|  2020/3/2 to current|  ![](https://img.shields.io/badge/status-passing-greeen)| 
| Japan                                                    | Asia                      | 1          | [![](https://img.shields.io/badge/source-covid--2019.live-9cf)](https://covid-2019.live/en/)   [![](https://img.shields.io/badge/source-stopcovid.jp-orange)](https://www.stopcovid19.jp/) |    2020/1/15 to current|  ![](https://img.shields.io/badge/status-passing-greeen)|
| Russia                                                   | Europe                    | 1          | [![](https://img.shields.io/badge/source-yandex.ru-9cf)](https://yandex.ru/maps/covid19?ll=41.775580%2C54.894027&z=3)  [![](https://img.shields.io/badge/source-стопкоронавирус.рф-orange)](https://xn--80aesfpebagmfblc0a.xn--p1ai/information/)|   2020/3/22 to current|  ![](https://img.shields.io/badge/status-passing-greeen)| 
| South Africa                                             | Africa                    | 1          |[![](https://img.shields.io/badge/source-NICD-9cf)](https://www.nicd.ac.zamedia/)  [![](https://img.shields.io/badge/source-health.gov.za-9cf)](https://www.nicd.ac.zamedia/)  [![](https://img.shields.io/badge/source-statssa.gov.za-orange)](http://www.statssa.gov.za/) |   2020/3/5 to current|  ![](https://img.shields.io/badge/status-passing-greeen)|
| Croatia                                                   |Europe                     | 1          |[![](https://img.shields.io/badge/source-koronavirus.hr-9cf)](https://koronavirus.hr/) [![](https://img.shields.io/badge/source-koronavirus.hr-orange)](https://koronavirus.hr/) | 2020/3/21 to current|  ![](https://img.shields.io/badge/status-passing-greeen)|
| Sweden                                                   |Europe                     | 1          |[![](https://img.shields.io/badge/source-folkhalsomyndigheten.se-9cf)](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/utbrott/aktuella-utbrott/covid-19/bekraftade-fall-i-sverige) [![](https://img.shields.io/badge/source-Folkhälsomyndigheten-orange)](https://experience.arcgis.com/experience/09f821667ce64bf7be6f9f87457ed9aa) | 2020/3/16 to current|  ![](https://img.shields.io/badge/status-passing-greeen)|
| India                                                   |Asia                     | 1          |[![](https://img.shields.io/badge/source-api.rootnet.in/-9cf)](https://api.rootnet.in/) [![](https://img.shields.io/badge/source-mohfw.gov.in/-orange)](https://www.mohfw.gov.in/) | 2020/3/10 to current|  ![](https://img.shields.io/badge/status-passing-greeen)|
| Hungary                                                  |Europe                     | 1          |[![](https://img.shields.io/badge/source-koronavirus.gov.hu/-9cf)](https://koronavirus.gov.hu/) [![](https://img.shields.io/badge/source-koronavirus.gov.hu/-orange)](https://koronavirus.gov.hu/)|  2020/3/31 to current|  ![](https://img.shields.io/badge/status-passing-greeen)|
| Denmark                                                  |Europe                     | 1          |[![](https://img.shields.io/badge/source-ssi.dk/-9cf)](https://www.ssi.dk/sygdomme-beredskab-og-forskning/sygdomsovervaagning/c/covid19-overvaagning) [![](https://img.shields.io/badge/source-ssi.dk/-orange)](https://www.ssi.dk/sygdomme-beredskab-og-forskning/sygdomsovervaagning/c/covid19-overvaagning)| 2020/5/20 to current|  ![](https://img.shields.io/badge/status-passing-greeen)|
| Ukraine                                                  |Europe                     | 1          |[![](https://img.shields.io/badge/source-rnbo.gov.ua/-9cf)](https://covid19.rnbo.gov.ua/) [![](https://img.shields.io/badge/source-rnbo.gov.ua/-orange)](https://covid19.rnbo.gov.ua/)| 2020/4/5 to current|  ![](https://img.shields.io/badge/status-passing-greeen)|
| Latvia                                                  |Europe                     | 1          |[![](https://img.shields.io/badge/source-data.gov.lv/-9cf)](https://data.gov.lv/dati/eng/dataset/covid-19-pa-adm-terit) [![](https://img.shields.io/badge/source-data.gov.lv/-orange)](https://data.gov.lv/dati/eng/dataset/covid-19-pa-adm-terit)| 2020/3/19 to current|  ![](https://img.shields.io/badge/status-passing-greeen)|
| Albania                                                 |Europe                     | 1          |[![](https://img.shields.io/badge/source-NovelCoronavirus/-9cf)](https://github.com/lucil/covid19-albanian-data) [![](https://img.shields.io/badge/source-coronavirus.al/-orange)](https://coronavirus.al/statistika/)| 2020/4/22 to current|  ![](https://img.shields.io/badge/status-passing-greeen)|
| Haiti                                                 |North America                    | 1          |[![](https://img.shields.io/badge/source-coronahaiti.org/-9cf)](https://www.coronahaiti.org/) [![](https://img.shields.io/badge/source-coronahaiti.org/-orange)](https://www.coronahaiti.org/)| 2020/3/19 to current|  ![](https://img.shields.io/badge/status-passing-greeen)|
| Romania                                                 |Europe                    | 1          |[![](https://img.shields.io/badge/source-covid_19_ro/-9cf)](https://github.com/gabrielpreda/covid_19_ro) [![](https://img.shields.io/badge/source-mai.gov.ro/-orange)](https://www.mai.gov.ro/category/comunicate-de-presa/)| 2020/4/2 to current|  ![](https://img.shields.io/badge/status-passing-greeen)|
| Mexico                                                 |North America                    | 1          |[![](https://img.shields.io/badge/source-Latin--Americ--Covid19/-9cf)](https://github.com/DataScienceResearchPeru/covid-19_latinoamerica) [![](https://img.shields.io/badge/source-gob.mxS-orange)](https://www.gob.mx/salud/documentos/informacion-internacional-y-nacional-sobre-nuevo-coronavirus-2019-ncov)| 2020/4/25 to current|  ![](https://img.shields.io/badge/status-passing-greeen)|
| Nigeria                                                 |Africa                        | 1          |[![](https://img.shields.io/badge/source-Nigeria--Novel--Coronavirus/-9cf)](https://github.com/Kamparia/nigeria-covid19-data) [![](https://img.shields.io/badge/source-gncdc.gov.ng-orange)](https://covid19.ncdc.gov.ng/)| 2020/2/27 to current|  ![](https://img.shields.io/badge/status-passing-greeen)|
| Pakistan                                                 |Asia                        | 1          |[![](https://img.shields.io/badge/source-Goverenment_of_Pakistan-9cf)](http://covid.gov.pk/stats/pakistan) [![](https://img.shields.io/badge/source-Goverenment_of_Pakistan-orange)](http://covid.gov.pk/stats/pakistan)| 2020/3/10 to current|  ![](https://img.shields.io/badge/status-passing-greeen)|
| Bolivia                                                 |South America                        | 1          |[![](https://img.shields.io/badge/source-BoliviaSegura-9cf)](https://www.boliviasegura.gob.bo/) [![](https://img.shields.io/badge/source-BoliviaSegura-orange)](https://www.boliviasegura.gob.bo/)| 2020/6/4 to 2020/7/29|  ![](https://img.shields.io/badge/status-pause-yellow)|
| Guatemala                                                 |North America                        | 1          |[![](https://img.shields.io/badge/source-Gobierno--de--Guatemala-9cf)](https://tablerocovid.mspas.gob.gt/) [![](https://img.shields.io/badge/source-Gobierno--de--Guatemala-orange)](https://covid19.gob.sv/)| 2020/3/15 to 2020/8/14|  ![](https://img.shields.io/badge/status-pause-yellow)|
| El Salvador                                                 |North America                        | 1          |[![](https://img.shields.io/badge/source-Gobierno--de--El--Salvador-9cf)](https://tablerocovid.mspas.gob.gt/) [![](https://img.shields.io/badge/source-Gobierno--de--El--Salvador-orange)](https://covid19.gob.sv/)| 2020/6/6 to 2020/7/4|  ![](https://img.shields.io/badge/status-pause-yellow)|
| Switzerland                                               |Europe                        | 1          |[![](https://img.shields.io/badge/source-Schweizerische--Eidenossenschaft-9cf)](https://www.bag.admin.ch/bag/en/home/krankheiten/ausbrueche-epidemien-pandemien/aktuelle-ausbrueche-epidemien/novel-cov/situation-schweiz-und-international.html#-1199962081) [![](https://img.shields.io/badge/source-Schweizerische--Eidenossenschaft-orange)](https://www.bag.admin.ch/bag/en/home/krankheiten/ausbrueche-epidemien-pandemien/aktuelle-ausbrueche-epidemien/novel-cov/situation-schweiz-und-international.html#-1199962081)| 2020/6/1 to 2020/8/10|  ![](https://img.shields.io/badge/status-pause-yellow)|
| Bulgaria                                                 |Europe                        | 1          |[![](https://img.shields.io/badge/source-coronavirus.bg-9cf)](https://coronavirus.bg/bg/statistika) [![](https://img.shields.io/badge/source-coronavirus.bg-orange)](https://coronavirus.bg/bg/statistika)| 2020/6/6 to 2020/8/10 |  ![](https://img.shields.io/badge/status-pause-yellow)|

## Recommended Citation
- Sha, D., Liu, Y, Liu, Q., Li, Y., Tian, Y., Beaini, F., Zhong, C., Hu, T., Wang, Z., Lan, H., Zhou, Y., Zhang, Z. and Yang, C., 2020. A spatiotemporal data collection of viral cases for COVID-19 rapid response, Big Earth Data, pp.1-21. DOI: 10.1080/20964471.2020.1844934
```BibTeX
@article{doi:10.1080/20964471.2020.1844934,
  author = { Dexuan   Sha  and  Yi   Liu  and  Qian   Liu  and  Yun   Li  and  Yifei   Tian  and  Fayez   Beaini  and  Cheng   Zhong  and  Tao   Hu  and  Zifu   Wang  and  Hai   Lan  and  You   Zhou  and  Zhiran   Zhang  and  Chaowei   Yang },
  title = {A spatiotemporal data collection of viral cases for COVID-19 rapid response},
  journal = {Big Earth Data},
  volume = {0},
  number = {0},
  pages = {1-21},
  year  = {2020},
  publisher = {Taylor & Francis},
  doi = {10.1080/20964471.2020.1844934}
  }
```
- Liu, Q., Liu, W., Sha, D., Kumar, S., Chang, E., Arora, V., Lan, H., Li, Y., Wang, Z., Zhang, Y. and Zhang, Z., 2020. An Environmental Data Collection for COVID-19 Pandemic Research. *Data*, 5(3), p.68.  
```BibTeX
@article{liu2020environmental,
  title={An Environmental Data Collection for COVID-19 Pandemic Research},
  author={Liu, Qian and Liu, Wei and Sha, Dexuan and Kumar, Shubham and Chang, Emily and Arora, Vishakh and Lan, Hai and Li, Yun and Wang, Zifu and Zhang, Yadong and others},
  journal={Data},
  volume={5},
  number={3},
  pages={68},
  year={2020},
  publisher={Multidisciplinary Digital Publishing Institute}
}
```
- Yang, C., Sha, D., Liu, Q., Li, Y., Lan, H., Guan, W.W., Hu, T., Li, Z., Zhang, Z., Thompson, J.H. and Wang, Z., 2020. Taking the pulse of COVID-19: A spatiotemporal perspective. *International Journal of Digital Earth*, pp.1-26.
```BibTeX
@article{yang2020taking,
  title={Taking the pulse of COVID-19: A spatiotemporal perspective},
  author={Yang, Chaowei and Sha, Dexuan and Liu, Qian and Li, Yun and Lan, Hai and Guan, Weihe Wendy and Hu, Tao and Li, Zhenlong and Zhang, Zhiran and Thompson, John Hoot and others},
  journal={International Journal of Digital Earth},
  pages={1--26},
  year={2020},
  publisher={Taylor \& Francis}
}
```


## Source Changing Log
- Greece from https://github.com/iMEdD-Lab/open-data/tree/master/COVID-19 to https://eody.gov.gr/ after 2020/6/9
- Slovenia from https://www.korona.gov.sk/en/coronavirus-covid-19-in-the-slovak-republic-in-numbers/ to https://www.nijz.si/sites/www.nijz.si/files/uploaded/ after 2020/6/10
- Romania from https://instnsp.maps.arcgis.com/apps/opsdashboard/index.html#/5eced796595b4ee585bcdba03e30c127 to https://github.com/gabrielpreda/covid_19_ro after 2020/6/10
- Slovakia from https://www.korona.gov.sk/en/coronavirus-covid-19-in-the-slovak-republic-in-numbers/ to  https://apify.com/davidrychly/covid-sk-3 after 2020/6/11

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
- Swetha Bhattaram, data validation.
- Yogya Kalra, data validation.

## Disclaimer
All data in this repository was collected/calculated/calibrated from multiple publicly available data sources that do not always agree. While we'll try our best to keep the information up to date and correct, we make no representations or warranties of any kind, express or implied, about the completeness, accuracy, reliability, with respect to the data. We do not bear any legal responsibility for any consequence caused by the usage of data provided. Reliance on the data for medical guidance or use of the data in commerce is strictly prohibited. NSF STcenter hereby disclaims any and all representations and warranties with respect to the data repository, including accuracy, fitness for use, and merchantability. 
For countries where there are internal disputes and sensitive region or area, we do not include that part of data in our datasets. If you are interested in this part of data, you can contact us directly.
