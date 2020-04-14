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


## Overall data sources by Country

- Worldwide/United States/Australia/Canada: 2019 Novel Coronavirus COVID-19 (2019-nCoV) Data Repository by [Johns Hopkins CSSE](https://github.com/CSSEGISandData/COVID-19)
- China/Worldwide: COVID-19/2019-nCoV Time Series Infection Data Warehouse (data crawled from Ding Xiang Yuan)
- United States (county level): [USAFACTS](https://usafacts.org/visualizations/coronavirus-covid-19-spread-map/)
- Italy: Dati COVID-19 Italia
- South Korea: parksw3/COVID19-Korea
- France: cedricguadalupe/FRANCE-COVID-19
- Germany/Austria/Netherlands/Sweden/Poland/Norway/Czechia: covid19-eu-zh/covid19-eu-data
- Japan: https://covid-2019.live/
- Spain: datadista/datasets
- Switzerland: daenuprobst/covid19-cases-switzerland
- United Kingdom: tomwhite/covid-19-uk-data
- Iran/Chile: Wikipedia
- Portugal: Dados relativos à pandemia COVID-19 em Portugal
- Brazil: COVID-19 Brazil - time series data
- Malaysia: ynshung/covid-19-malaysia
- Belgium: eschnou/covid19-be
- Russia: grwlf/COVID-19_plus_Russia
- Ecuador/Mexico/Argentina/Peru: Latin America Covid-19 Data Repository by DSRP
- India: covid19india
- Ireland: andrewm4894/ireland_covid19_data
- South Africa: Coronavirus COVID-19 (2019-nCoV) Data Repository for South Africa
- Philippines: gigerbytes/ncov-ph-data
- Romania: Coronavirus COVID-19 România
- Indonesia: Monitoring COVID19 Indonesia by catchmeup.id
- Saudi Arabia: Saudi Arabia Coronavirus disease (COVID-19) situation
- Thailand: TH-STAT.com

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
- Feyaz Beaini, data source collection and evaluation, quality control. 
- Tao Hu, cooperation leader from Harvard University and China Data Lab.
- Zifu Wang and Hai Lan, IT infrastructure and network security support.
