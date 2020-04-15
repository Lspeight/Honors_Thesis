# Analysis of Data
Analysis was conducted in R 

## Rstudio Plotting 
### Figures 1.1, 1.2, & 1.3 
```
# Import Data
Pn_Ps <- read.csv("PnPs_results.txt", header=TRUE, sep = "")
# goal: boxplot to show individual histone genes (H2A, H2B, H3, & H4) pn/ps ratios with in the same ploidy
# sorting data
Pn_Ps.1 <- select(Pn_Ps,Ploidy,Histone,pn_ps)
View(Pn_Ps.1)
Pn_Ps.1.1 <- filter(Pn_Ps.1, Ploidy == 2)
View(Pn_Ps.1.1)
Pn_Ps.1.2 <- filter(Pn_Ps.1, Ploidy == 3)
View(Pn_Ps.1.2)
Pn_Ps.1.3 <- filter(Pn_Ps.1, Ploidy == 4)
View(Pn_Ps.1.3)
# creating boxplots 
ggplot(data = Pn_Ps.1.1, aes(x = Histone, y= pn_ps, color = Histone)) + geom_boxplot() + ggtitle("Pn/Ps of Histone gene in 2n Lineages")
ggplot(data = Pn_Ps.1.2, aes(x = Histone, y= pn_ps, color = Histone)) + geom_boxplot() + ggtitle("Pn/Ps of Histone gene in 3n Lineages")
ggplot(data = Pn_Ps.1.3, aes(x = Histone, y= pn_ps, color = Histone)) + geom_boxplot() + ggtitle("Pn/Ps of Histone gene in 4n Lineages")

```
