# COVID-19 Socioeconomic Data Collection

This repository specific keeps and provides the spatiotemporal data collection of socio-economic factors for COVID-19 research/studies of USA, including the popular driven factors (demography, education, poverty, income, housing and employment status), and effected economic factors under COVID-19 pandemic from multi-data sources by weekly/monthly/quarterly time frequency.

## Overview of data topics

The dataset is organized based on the topic and usage for COVID-19 studies.  The following table list the metadata of sub-topics/attributes included, spatial resolution (admin level, admin1/2 refers to state/county), time frequency and range for each topic.  The dynamic (weekly/monthly) dataset is provided by two data report: 1) timely update report based on timestamp and 2) time-series summary report based on attribute.

| Topic                        | Attributes                                                   | Admin Level | Time Frequency | Time Range                   |
| ---------------------------- | ------------------------------------------------------------ | ----------- | -------------- | ---------------------------- |
| Socioeconomic driven factors | Demographic; Education; Poverty and income; Housing; Employment status | admin 1/2   | static*        | 2018 ACS 5-year Estimation * |
| Medical resource             | Beds; ICU beds; hospital; medical staff                      | admin 1/2   | static**       | data by 2020/2               |
| Household Pulse Survey       | employment status<br/>food security<br/>housing security<br/>education disruptions<br/>physical and mental wellbeing | admin 1     | weekly         |                              |
| Housing Inventory            | days on market; median listing price; price increase count   | admin 1     | monthly        |                              |
| Small Business Pulse Survey  | Financial Assistance<br/>Cash on Hand<br/>Pivot to Delivery/Carry-Out; etc. | admin 1     | weekly         |                              |
| Unemployment data            | Continued claims; covered employment; initial claims; insured unemployment rate | admin 1     | monthly        |                              |

\* the static for driven factors refers to 5-year estimation value of 2018, since this dataset is collected and provided by United States Census Bureau, it is updated by year.

\** the static frequency is the updated summary of numbers for the medical resources of each geographic regions.

## Data sources

General data sources of socioeconomic measurement is listed below. More details of data sources under each topic is presented under sub folder of this page.

- Bureau of Economic Analysis: https://www.bea.gov/data/gdp
- Data and Statistics about the U.S: https://www.usa.gov/statistics
- Statistics and Data Sets of University of Cincinnati: https://guides.libraries.uc.edu/c.php?g=222397&p=2419059
- U.S. Department of Commerce: https://www.commerce.gov/data-and-reports/economic-indicators
- The World Bank: https://data.worldbank.org/country/united-states?view=chart



**Contact Us:**

- Email: [ytian20@masonlive.gmu.edu](ytian20@masonlive.gmu.edu); [dsha@gmu.edu](mailto:dsha@gmu.edu)

**Terms of Use:**

1. This data set is licensed under the Creative Commons Attribution 4.0 International (CC BY 4.0) by the George Mason University on behalf of its NSF Spatiotemporal Innovation Center. Copyright NSF Spatiotemporal Innovation Center 2020.