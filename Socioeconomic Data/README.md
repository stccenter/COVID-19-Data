<!--
 * @Author: your name
 * @Date: 2020-10-06 13:08:13
 * @LastEditTime: 2020-11-05 15:50:58
 * @LastEditors: Please set LastEditors
 * @Description: In User Settings Edit           
 * @FilePath: \github_test\README-econ.md
-->
# COVID-19 Socioeconomic Data Collection

This repository specific keeps and provides the spatiotemporal data collection of socio-economic factors for COVID-19 research/studies of USA, including the popular driven factors (demography, education, poverty, income, housing and employment status), and effected economic factors under COVID-19 pandemic from multi-data sources by weekly/monthly/quarterly time frequency.

## Metadata and attribute description

The dataset is organized based on the topic and usage for COVID-19 studies.  The following table list the metadata of sub-topics/attributes included, spatial resolution (admin level, admin1/2 refers to state/county), time frequency and range for each topic.  The dynamic (weekly/monthly) dataset is provided by two data report: 1) timely update report based on timestamp and 2) time-series summary report based on attribute.

### Economic indexes for multiple time-frequency
| Topic                                     | Attributes                                           | Description                                                                                                                                                                                                 | Time Frequency | Time Range (of raw data source) |
| ----------------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------------------------- |
| [Gross Domestic Product (GDP)](https://github.com/stccenter/COVID-19-Data/tree/master/Socioeconomic%20Data/Gross%20Domestic%20Product%20(GDP))              | Real GDP                                             | inflation-adjusted measure that reflects the value of all goods and services produced by an economy in a given year                                                                                         | quarterly      | 2004 Q1 -2020 Q2                |
|                                           | Current-dollar GDP                                   | gross domestic product (GDP) evaluated at current market prices                                                                                                                                             | quarterly      | 2005 Q1 -2020 Q2                |
|                                           | Chain-type quantity indexes                          | eliminate the substitution bias found in indexes with unchanging (or “fixed”)weights, and their movements are not affected by the choice of the reference period.                                           | quarterly      | 2006 Q1 -2020 Q2                |
| [Personal Income](https://github.com/stccenter/COVID-19-Data/tree/master/Socioeconomic%20Data/Personal%20Income)                          | Overall Compensation                                 | compensation include all categories                                                                                                                                                                         | quarterly      | 1948 Q1 -2020 Q2                |
|                                           | Farm Compensation                                    | compensation for farm relate employees                                                                                                                                                                      | quarterly      | 1948 Q1 -2020  Q2               |
|                                           | Nonfarm Compensation                                 | compensation for non-farm relate employees                                                                                                                                                                  | quarterly      | 1948 Q1 -2020  Q2               |
|                                           | Per capita personal income                           | is calculated as the total personal income of the residents of a state divided by the population of the state.                                                                                              | quarterly      | 1948 Q1 -2020  Q2               |
| International Trade in Goods and Services | Export - Manufactured Commodities                    | amount of manufactured commodities that export in millions of dollars                                                                                                                                       | monthly        | 2006/1/1 - 2020/8/1             |
|                                           | Export - Non-Manufactured Commodities                | amount of non-manufactured commodities that export includes agricultural, forestry, fishery products, mineral commodities, scrap, waste and used or second-hand merchandise in millions of dollars          | monthly        | 2006/1/1 - 2020/8/1             |
|                                           | Import - Manufactured Commodities                    | amount of manufactured commodities that import in millions of dollars                                                                                                                                       | monthly        | 2006/1/1 - 2020/8/1             |
|                                           | Import - Non-Manufactured Commodities                | amount of non-manufactured commodities that import includes agricultural, forestry, fishery products, mineral commodities, scrap, waste and used or second-hand merchandise in millions of dollars          | monthly        | 2006/1/1 - 2020/8/1             |
| [Employment](https://github.com/stccenter/COVID-19-Data/tree/master/Socioeconomic%20Data/Employment)                               | All employees-Total nonfarm                          | Number of employees in thousands which are nonfarm relate jobs seasonally adjusted                                                                                                                          | monthly        | 1990/1  -2020/9                 |
|                                           | All employees-Manufacturing                          | Number of employees in thousands which are manufacturing relate seasonally adjusted                                                                                                                         | monthly        | 1990/1  -2020/9                 |
|                                           | All employees-Education and Health Services          | Number of employees in thousands which are education and health services relate  seasonally adjusted                                                                                                        | monthly        | 1990/1  -2020/9                 |
|                                           | Unemployment rate                                    | Number unemployed as a percent of the labor force                                                                                                                                                           | monthly        | 1976/1 - 2020/9                 |
|                                           | Employment                                           | Number of employed persons                                                                                                                                                                                  | monthly        | 1976/1 - 2020/9                 |
|                                           | Labor force participation rate                       | Proportion of the population that is in the labor force                                                                                                                                                     | monthly        | 1976/1 - 2020/9                 |
|                                           | Initial unemployment claim                           | An initial claim is a claim filed by an unemployed individual after a separation from an employer.                                                                                                          | weekly         | 1967/1/7 -2020/9/26             |
|                                           | Insured Unemployment Rate                            | The rate computed by dividing Total Unemployed by the Civilian Labor Force                                                                                                                                  | weekly         | 1967/1/7 -2020/9/26             |
|                                           | Continued Claims                                     | A person who has already filed an initial claim and who has experienced a week of unemployment then files a continued claim to claim benefits for that week of unemployment                                 | weekly         | 1967/1/7 -2020/9/26             |
| [Housing market](https://github.com/stccenter/COVID-19-Data/tree/master/Socioeconomic%20Data/Housing%20Market)                            | Total number of housing units                        | Total number of privately owned housing units unadjusted                                                                                                                                                    | monthly        | 2019/1 -2020/9                  |
|                                           | Single family house                                  | Total number of single housing units unadjusted                                                                                                                                                             | monthly        | 2019/1 -2020/9                  |
|                                           | Multi-family units - includes 2, 3, 4, and 5 or more | Total number of multi-unit homes unadjusted                                                                                                                                                                 | monthly        | 2019/1 -2020/9                  |
|                                           | Days on Market                                       | The median number of days property listings spend on the market                                                                                                                                             | monthly        | 2019/10 - 2020/9                |
|                                           | Median listing price                                 | The median listing price during the specified month                                                                                                                                                         | monthly        | 2019/10 - 2020/9                |
|                                           | Price increase count                                 | The count of listings which have had their price increased                                                                                                                                                  | monthly        | 2019/10 - 2020/9                |
|                                           | All-Transactions                                     | It is based on sales price and appraisal values from refinance mortgages are added to the purchase-only data. Units: Index, not seasonally adjusted                                                         | quarterly      | 1991/1  -2020/9                 |
|                                           | ExpandedData                                         | It is based on  sales price information sourced from Enterprise, Federal Housing Administration (FHA), and Real Property County Recorder Data Licensed from DataQuick Units: Index, not seasonally adjusted | quarterly      | 1991/1  -2020/9                 |
|                                           | PurchaseOnly                                         | It is based on more than 6 million repeat sales transactions on the same single-family properties. Units: Index, seasonally adjusted                                                                        | quarterly      | 1991/1  -2020/9                 |

### [Socioeconomic determinants](https://github.com/stccenter/COVID-19-Data/tree/master/Socioeconomic%20Data/Socioeconomic%20determinants)
| Attributes                 | Description                                                           | Unit  | Topic                                |
| -------------------------- | --------------------------------------------------------------------- | ----- | ------------------------------------ |
| Area size                  | the state area measurements, in square kilometers                     | sq-km | Geographic                           |
| Population size            | annual estimates of the total population (2019)                       | #     | Demographic                          |
| Population density         | people per sq. km                                                     | #     | Demographic                          |
| Senior Population          | population age 65+ (% of total)                                       | %     | Demographic - age group              |
| Young Population           | population ages 0-14 (% of total)                                     | %     | Demographic - age group              |
| Male Population            | population gender male (% of total)                                   | %     | Demographic - gender group           |
| White Population           | population race white (% of total)                                    | %     | Demographic - racial group           |
| Africa-American Population | population race Africa American (% of total)                          | %     | Demographic - racial group           |
| Hispanic population        | population ethnic Hispanic of any race (% of total)                   | %     | Demographic - ethnic group           |
| Internet access            | population using internet and computer (2019 data)                    | %     | Computers and internet subscriptions |
| High school degree         | population with high school and equivalent degrees (% of total)       | %     | Education                            |
| Bachelor degrees           | population with Bachelor's degree or higher (% of total)              | %     | Education                            |
| Median household income    | median household income                                               | $     | Income                               |
| Poverty rate               | Poverty rate household income below poverty line.                     | %     | Poverty                              |
| Uninsured                  | Population without health care coverage in United States (% of total) | %     | Insurance                            |
| Household size             | Average number of persons in a household                              | #     | Household                            |
| House Owner                | owner-occupied housing (% of total household)                         | %     | Household                            |
| hospital                   | Number of hospitals                                                   | #     | health resource                      |
| hospital bed               | Number of hospital beds                                               | #     | health resource                      |
| ICU bed                    | Number of ICU beds                                                    | #     | health resource                      |
| Nurses                     | Number of nurses per 1000 population                                  | #     | health resource                      |
| Medical Doctors            | Number of medical doctors per 1000 population                         | #     | health resource                      |



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