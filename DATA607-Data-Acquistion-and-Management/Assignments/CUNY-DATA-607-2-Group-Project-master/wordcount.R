source('db_layer.r')

if (!require('rJava')) install.packages('rJava')
if (!require('RWeka')) install.packages('RWeka')
if (!require('tm')) install.packages('tm')
if (!require('SnowballC')) install.packages('SnowballC')
if (!require('wordcloud')) install.packages('wordcloud')
if (!require('reshape2')) install.packages('reshape2')
if (!require('dplyr')) install.packages('dplyr')

db_name <- "data_science_wordver"

### Note - copy scrape output to the directory listed below

samp = Corpus(DirSource("ScrapeOutput"), 
              readerControl = list(language = "en_EN", load = F))

# Make lowercase 
samp_clean = tm_map(samp, tolower)

# Remove special characters and punctuation (code may have to be adjusted
# depending on the input structure)

for(j in seq(samp_clean))   
{   
    samp_clean[[j]] = iconv(samp_clean[[j]], to="ASCII", sub = "") 
    samp_clean[[j]] <- gsub("/|@|\\|", " ", samp_clean[[j]])
    samp_clean[[j]] <- gsub("(?<!\\w)r(?!\\w|&D)", "rlanguage", samp_clean[[j]], perl = TRUE) #R: Rlanguage
    samp_clean[[j]] <- gsub("(?<!\\w)c(?!\\w|#|\\+)", "clanguage", samp_clean[[j]], perl = TRUE) #C: Clanguage
    samp_clean[[j]] <- gsub("c\\+\\+", "cpp", samp_clean[[j]], perl = TRUE) # C++: cpp
    samp_clean[[j]] <- gsub("c#", "csharp", samp_clean[[j]], perl =TRUE) # C# CSharp
}  
samp_clean = tm_map(samp_clean, PlainTextDocument)  
samp_clean = tm_map(samp_clean, removePunctuation)
samp_clean = tm_map(samp_clean, removeNumbers)  

# Remove stopwords
samp_clean = tm_map(samp_clean, removeWords, stopwords("english")) 

# Strip white space
#samp_clean = tm_map(samp_clean, stemDocument) # do not stem for now
samp_clean = tm_map(samp_clean, stripWhitespace) 

# Tokenize 1 to 4-grams
xgramTokenizer = function(x) NGramTokenizer(x, Weka_control(min = 1, max = 4))

# Calculate ngram freqs
tdmatrix = TermDocumentMatrix(samp_clean, control = list(tokenize = xgramTokenizer))

# ngram frequencies
wdcnt = as.matrix(tdmatrix)
wdcnt.df = data.frame(wdcnt)
wdcnt.df$keywords = rownames(wdcnt.df)
wdcnt.df.melted = melt(wdcnt.df)
wdcnt.df.melted = wdcnt.df.melted[, c(1,3)]
colnames(wdcnt.df.melted) = c("Keyword","Freq")
wdcnt.df.sub = arrange(wdcnt.df.melted, desc(Freq))
wdcnt.df.sub <- wdcnt.df.sub[c(1:1000),]

#Dump to csv file
write.csv(wdcnt.df.sub, "wordcount.csv",row.names = F)

wordcloud(samp_clean, max.words = 100, random.order = F, rot.per=0.0, colors=brewer.pal(3,"Dark2" ))



#save results to db
#first add skills
lapply(wdcnt.df.sub$Keyword, insSkillNoCatDB)

#then add counts for skills
logged <- mapply(upsertSkillCount, wdcnt.df.sub$Keyword, wdcnt.df.sub$Freq)
#check sample in db
head(getSkillCounts('',''))

