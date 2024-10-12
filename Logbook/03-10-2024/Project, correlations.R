##date to years
#function to only get the year 
year <- function(date){
  substr(data, 1, 4)
}
years <- as.data.frame(year(pirate_attacks$date))#make dataset of only the years

pirate_attacks$years <-years$`year(pirate_attacks$date)`#add the information of only the years to the datset

#GDP & pirate attacks in Nigeria
nigeria <- which(pirate_attacks$nearest_country == "NGA") #every row where nigeria was the nearest country of the pirate attack
new <- pirate_attacks[c(nigeria),]# make a new dataset of only the data where nigeria was the nearest country

gdp_nigeria <- country_indicators[c(3861:3887),]#these are the indicators of Nigeria

freq((pirate_attacks$nearest_country)) #559 frequencies



#for correlations between GDP and pirate attacks, we need to know what data types these are.
#GDP stands for Gross Domestic Product (US Dollars).
ggplot(aes(x=year, y=GDP), data=gdp_nigeria)+ geom_line()+labs(title= "Figure ...", subtitle = "Gross Domestic Product of Nigeria ofer the span of 1993-2019 in US Dollars", x= "Year")
class(gdp_nigeria$GDP)#numeric data type, with the information, it is about US Dollars, what would make GDP an ratio variable 




#frequency is an absolute (ratio) data type, thus we need to do the pearson method
ggplot(aes(years, fill = attack_type), data = new)+geom_bar()+
  labs(title = "Figure ...", subtitle = "Frequency of pirate attacks near Nigeria in the time periode from 1993-2020, with a distinction in attack type", y="Frequency", x= "Years")

gdp_nigeria$pirateattacks_freq <- c(3,0,2,3,8,1,10,9,19,14,39,27,17,11,40,39,28,18,10,23,28,18,14,35,35,48,32)


ggplot(aes(year,pirateattacks_freq), data = gdp_nigeria)+geom_line()+labs(title = "Figure ...", subtitle = "Frequency of priate attacks near Nigeria in the period of 1993-2019",x="Year", y = "Frequency pirate attacks")

#correllations
correlation_gdp <-cor.test(gdp_nigeria$GDP, gdp_nigeria$pirateattacks_freq, method = "pearson")
correlation_gdp

#proportion of explained variance
r <- 0.5261597
r_squared <- r^2
r_squared