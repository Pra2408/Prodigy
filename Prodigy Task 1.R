##Create a bar graph and histogram to visualize the distribution of a categorical or continuous variable.
##We have chosen "iris" dataset for the above task
# Load the required library
library(ggplot2)
# Create a bar chart for the categorical variable "Species"
ggplot(iris, aes(x = Species)) +
  geom_bar(fill = "skyblue") +
  labs(title = "Distribution of Iris Species") +
  xlab("Species") +
  ylab("Count")
# Create a histogram for the continuous variable "Sepal.Length"
ggplot(iris, aes(x = Sepal.Length)) +
  geom_histogram(fill = "skyblue") +
  labs(title = "Distribution of Sepal Length") +
  xlab("Sepal Length") +
  ylab("Frequency")

