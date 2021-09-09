######################################
##  Cluster analysis on supervised and unsupervised datasets
#resources:
# a) https://www.youtube.com/watch?v=Tq-B95qbVXg
# b) https://www.r-bloggers.com/stringdist-0-9-2-dist-objects-string-similarities-and-some-deprecated-arguments/
# c) https://www.r-bloggers.com/fuzzy-string-matching-a-survival-skill-to-tackle-unstructured-information/
# d) http://www.yimizhao.com/single-post/2015/04/08/Compute-Levenshtein-distance-using-R
# e) http://stackoverflow.com/questions/21511801/text-clustering-with-levenshtein-distances
##########################################

#source('wordcount.R')
if (!require('stringr')) install.packages('stringr')
if (!require('dplyr')) install.packages('dplyr')
if (!require('tidyr')) install.packages('tidyr')
if (!require('utils')) install.packages('utils')
if (!require('stringdist')) install.packages('stringdist')


#read in unsupervised skill set:
unsup<-read.csv('wordcount.csv')

distancemodels <- stringdistmatrix(unsup$Keyword,unsup$Keyword,method = "jw")
rownames(distancemodels) <- unsup$Keyword
hc <- hclust(as.dist(distancemodels))

# run the stringdistmatrix function and request 200 groups
uniquemodels <- unique(as.character(unsup$Keyword))
distancemodels <- stringdistmatrix(uniquemodels,uniquemodels,method = "jw")
rownames(distancemodels) <- uniquemodels
hc <- hclust(as.dist(distancemodels))
dfClust <- data.frame(uniquemodels, cutree(hc, k=200))
names(dfClust) <- c('modelname','cluster')

# visualize the groupings
plot(table(dfClust$cluster))
print(paste('Average number of models per cluster:', mean(table(dfClust$cluster))))

# let's look at the top groups and see what the algorithm did:
ta <- table(dfClust$cluster)
ta <- cbind(ta,ta/length(dfClust$cluster))
ta <- ta[order(ta[,2], decreasing=TRUE),]
p <- data.frame(factorName=rownames(ta), binCount=ta[,1], percentFound=ta[,2])
dfClust <- merge(x=dfClust, y=p, by.x = 'cluster', by.y='factorName', all.x=T)
dfClust <- dfClust[rev(order(dfClust$binCount)),]
names(dfClust) <-  c('cluster','modelname')
head (dfClust[c('cluster','modelname')],50)

head(dfClust)
head(unsup)

# try combining fields together
#to allow for visual inspection, we concatenate all keywords
#that are clustered together by the algorith into one field
#later, we use dplyr to aggregate sum the frequencies by cluster group
final<-merge(dfClust,unsup,by.x='modelname',by.y='Keyword')
names(final)[3:4]<-c('out.1','out.2')

test<-final %>%
  select(modelname,cluster,Freq) %>%
  group_by(cluster) %>%
  select(modelname) %>%
  summarise(members=paste(modelname, collapse=" ,"))

final2<-final %>%
  group_by(cluster) %>%
  summarise(aggd.freq=sum(Freq))


final.m<-merge(test,final2,by='cluster')

final.m<-final.m %>%
  arrange(desc(aggd.freq))

#visual analysis of output:
write.csv(final.m,'cluster_out.csv', row.names = F)

#most interesting terms from the analysis, to be considered for entry in supervised data set:
#statistical analysis, modeling, zoomdata, optimization
