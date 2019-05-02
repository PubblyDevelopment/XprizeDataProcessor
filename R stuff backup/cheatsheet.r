str(DATA) # quick summary
breaks = c() # customize histogram bins
main = "title" # label graph
xlab = "xlabel" # x label
barplot(table()) # barplot of cateogorical values
data <- read.csv(file="My Documents/stats/data.csv") # read in data
m <- lm(Y ~ X) # regression line :3c #lm is linear model! ah ha!
cor(var1, var2, use="complete.obs") # ignore NA values
names(my.lm) # will tell you all the stuff thats available
summary(my.lm) # will give you an ugly, complex summary
abline(my.lm) # make a linear regression line
abline(h=0) # make a pretty horizontal line when plotting fitted values v residuals
cricket = data.frame(list(Temperature=c(54.5,59.5,63.5,67.5,72.0,78.5,83.0), 
                          Result=c(81,97,103,123,150,182,195)))  # BS temp data
library(Lock5Data) # load the lockdata
data(BaseballHits) # USE the magical lockdata
prop.test(x,n) # confidence interval for true proportion, x is successes, n is total trials
prop.test(43,315, p=0.25, alternative = "less") # motherfucking proportion test with more shit, p is dat proportion
                                                # of the null hyp, alt is our test, can be "greater" or "two.sided"
# use fisher.test(my.data) if cell counts are less than 5