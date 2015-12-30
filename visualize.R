

#load required libraries
require(ggplot2)
require(ggthemes)

#load data
a <-read.csv('paradox.csv')

#visualize
ggplot(a, aes(x=a$Index,y=a$Probability)) + 
  xlab("Number of People")+
  ylab("Birthday Probability")+
  theme_economist(base_size = 10,horizontal = TRUE)+
  geom_line(aes(x = a$Index,y = a$Probability,color='red',size=1)) + 
  theme(text=element_text(size=12))+
  ggtitle("\nThe Birthday Paradox")+
  theme(plot.title = element_text(hjust = 0.5))+
  labs(colour = 'Probability')
