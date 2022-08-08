library(dplyr)
library(ggplot2)
library(RColorBrewer)

a = cancer_patient_data_sets
a$Level <- as.numeric(a$Level)

a$Level[a$Level == "High"] = as.numeric(3)
a$Level[a$Level == "Medium"] = as.numeric(2)
a$Level[a$Level == "Low"] = as.numeric(1)

c = filter(a, a$Level == 3)
high_level_data = c

medium_level_data = filter(a, a$Level == 2) 
low_level_data = filter(a, a$Level == 1)
heavy_smoker_data = filter(a, a$Smoking > 5)
non_heavy_smoker_data = filter(a, a$Smoking < 5)
passive_smoker_data = filter(a, a$`Passive Smoker` > 5)
male_data = filter(a, a$Gender == 1)
female_data = filter(a, a$Gender == 2)
environment_data = filter(a, a$`Air Pollution` > 3 & a$`Dust Allergy` > 3)
no_environment_data = filter(a, a$`Air Pollution` <= 3 & a$`Dust Allergy` <= 3)
unavoidable_data = filter(a, a$`Dust Allergy` >5 & a$`OccuPational Hazards`>5  & a$`Genetic Risk`>5  & a$`chronic Lung Disease`>5 
                          & a$`Balanced Diet` >5 )
avoidable_data = filter(a, a$`Dust Allergy`<= 5 & a$`OccuPational Hazards` <=5  & a$`Genetic Risk`<=5  & a$`chronic Lung Disease`<=5
                          & a$`Balanced Diet` <=5 )
heavy_alcohol_data = filter(a, a$`Alcohol use` > 5)



#######################################################################################################################
hist=ggplot(environment_data,aes(Level))
hist+geom_histogram( binwidth = 100, fill="pink", colour="black", stat="count")
#######################################################################################################################
bp<- ggplot(passive_smoker_data, aes(x="", y=Level, fill=Level))+
  geom_bar(width = 1, stat = "identity") 
pie <- bp + coord_polar("y", start=0)
pie
#######################################################################################################################
bp<- ggplot(female_data, aes(x="", y=Level, fill=Level))+
  geom_bar(width = 1, stat = "identity") 
pie <- bp + coord_polar("y", start=0)
pie
#######################################################################################################################
bp<- ggplot(heavy_smoker_data, aes(x="", y=Level, fill=Level))+
  geom_bar(width = 1, stat = "identity")
pie <- bp + coord_polar("y", start=0)
pie
########################################################################################################################
bp<- ggplot(non_heavy_smoker_data, aes(x="", y=Level, fill=Level))+
  geom_bar(width = 1, stat = "identity")
pie <- bp + coord_polar("y", start=0)
pie
########################################################################################################################
hist=ggplot(heavy_alcohol_data,aes(Wheezing))
hist+geom_histogram( binwidth = 1, fill="pink", colour="black")
########################################################################################################################
hist=ggplot(high_level_data,aes(`Alcohol use`))
hist+geom_histogram( binwidth = 100, fill="pink", colour="black", stat = "count")
########################################################################################################################
hist=ggplot(low_level_data,aes(`Alcohol use`))
hist+geom_histogram( binwidth = 100, fill="pink", colour="black", stat = "count")
########################################################################################################################
bp<- ggplot(high_level_data, aes(x="", y=Gender, fill =Age))+
  geom_bar(width = 1, stat = "identity") 
pie <- bp + coord_polar("y", start=0, clip= "off")
pie
########################################################################################################################
hist=ggplot(avoidable_data,aes(`Chest Pain`))
hist+geom_histogram( binwidth = 10, fill="pink", colour="black", stat = "count")
########################################################################################################################
summary(a)
########################################################################################################################
bp<- ggplot(avoidable_data, aes(x="", y=Level, fill =Level))+
  geom_bar(width = 1, stat = "identity") 
pie <- bp + coord_polar("y", start=0)
pie
########################################################################################################################
table(heavy_smoker_data$Level)
table(heavy_alcohol_data$Level)
285/435*100
276/356*100
########################################################################################################################
table(high_level_data$`Alcohol use` > 5)
table(high_level_data$Smoking > 5)
285/365*100
276/365*100
########################################################################################################################
435/1000*100 #heavy smokers compared to whole patients
356/1000*100 #heavy alcohol drinkers compared to hull whole patients
