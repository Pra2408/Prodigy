##Installing Required Packages
install.packages("tidyverse")
install.packages("tidytext")
install.packages("wordcloud")
install.packages("ggplot2")
install.packages("textdata")
#Accessing Library
library(tidyverse)
library(tidytext)
library(wordcloud)
#Loading Data Sets 
data=Twitter
data
#Analysis
data=data %>%
  select(Text,Sentiment)%>%
  mutate(Text=tolower(Text))%>%
  unnest_tokens(word,Text)
#Processing
data <- data %>%
  inner_join(get_sentiments("afinn"), by = "word") %>%
  group_by(Sentiment) %>%
  summarize(Sentiment_score = sum(value))
#Visualisation
ggplot(data, aes(x = Sentiment, y = Sentiment_score)) +
  geom_bar(stat = "identity", fill = "steelblue") +
  labs(title = "Sentiment Analysis", x = "Sentiment", y = "Sentiment Score")


