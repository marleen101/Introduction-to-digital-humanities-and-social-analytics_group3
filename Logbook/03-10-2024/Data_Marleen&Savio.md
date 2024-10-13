## Data documentation
### Corruption Perceptions Index:
The following "Short Methodology Note" is from the folder "CPI 2023 Methodology" downloaded from https://www.transparency.org/en/cpi/2023
##### Short Methodology Note
The Corruption Perceptions Index (CPI) aggregates data from a number of different
sources that provide perceptions by business people and country experts of the level
of corruption in the public sector.
The following steps are followed to calculate the CPI:
1. Select data sources: Each data source that is used to construct the CPI must
fulfil the following criteria to qualify as a valid source:
• Quantifies perceptions of corruption in the public sector
• Be based on a reliable and valid methodology, which scores and ranks
multiple countries on the same scale
• Performed by a credible institution
• Allow for sufficient variation of scores to distinguish between countries
• Gives ratings to a substantial number of countries
• The rating is given by a country expert or business person
• The institution repeats their assessment at least every two years
The CPI is calculated using 13 different data sources from 12 different
institutions that capture perceptions of corruption within the past two years.
These sources are described in detail in the accompanying source description
document.
2. Standardise data sources to a scale of 0-100 where a 0 equals the highest level
of perceived corruption and 100 equals the lowest level of perceived corruption.
This standardisation is done by subtracting the mean of each source in the
baseline year from each country score and then dividing by the standard
deviation of that source in the baseline year. This subtraction and division using
the baseline year parameters ensures that the CPI scores are comparable year
on year since 2012. After this procedure, the standardised scores are
transformed to the CPI scale by multiplying with the value of the CPI standard
deviation in 2012 (20) and adding the mean of CPI in 2012 (45), so that the data
set fits the CPI’s 0-100 scale.
-> Be aware of the inconsistent way of measurement before and after 2012!!! -> standardise?
3. Calculate the average: For a country or territory to be included in the CPI, a
minimum of three sources must assess that country. A country’s CPI score is
then calculated as the average of all standardised scores available for that
country. Scores are rounded to whole numbers.
4. Report a measure of uncertainty: The CPI is accompanied by a standard error
and confidence interval associated with the score, which captures the variation in
scores of the data sources available for that country/territory.

CPI measurement issue:[ Pre-2012 CPI Scores CANNOT Be Compared Across Time–So Please Stop Doing It! ](https://globalanticorruptionblog.com/2014/09/30/pre-2012-cpi-scores-cannot-be-compared-across-time-so-please-stop-doing-it/)
- Before 2012, the CPI was measured relative to other countries, so comparing their CPI scores across the years would be meaningless. 
- After 2012, the CPI measurement changed, making it possible to compare themselves across the year. 
#####  This may risk our loss of usable data. 

### Suggestion: 
- Change the country indicator to GDP (more objective)
- Argue: Choose GDP over GDP per capita => We only analyze the data of one country. 

Quick scatter plot to see how much of a correlation we can see at a glance. And yes it is just the gdp from the dataset, dividing by populations will give the same graph but with smaller numbers.
	
 <img width="375" alt="Screenshot 2024-10-08 at 14 57 31" src="https://github.com/user-attachments/assets/5bfa1982-db52-4c2a-8d6e-d42ec05168cd">

r-value 0.5261597456173477 (0.53)

p-value 0.004816144363577555 (0.005)	
