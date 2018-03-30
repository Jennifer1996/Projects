library(ggplot2)
library(data.table)

movies <- fread("douban_movie_clean.txt", header=TRUE, sep="^", encoding="UTF-8")

ggplot(movies) + geom_histogram(aes(x=length))

