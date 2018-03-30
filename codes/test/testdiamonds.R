library(ggplot2)
library(gcookbook)
diamonds <- diamonds
set.seed(123)
diamonds <- diamonds[sample(nrow(diamonds),1000),]

summary(diamonds)
str(diamonds)

head(diamonds)

ggplot(diamonds) + geom_point(aes(x=carat,y=price,color=color,shape=cut))

ggplot(diamonds) + geom_histogram(aes(x=price,fill=cut),position = "fill")

ggplot(diamonds) + geom_bar(aes(x=clarity,fill=color))

ggplot(diamonds) + geom_density(aes(x=price,fill=cut,color=cut),alpha=0.2)

ggplot(diamonds) + geom_boxplot(aes(x=cut,y=price,fill=color))

ggplot(diamonds) + geom_point(aes(x=carat,y=price,color=color,shape=cut)) + scale_y_log10() +labs(x='克拉',y='价格',title='一张很厉害的图')+ theme(text=element_text(family="Microsoft YaHei"))

