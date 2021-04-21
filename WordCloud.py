
"""
Understanding AI Word Cloud
Make sure you have wordcloud install prior to running using the below command
pip install wordcloud

The following has been split into 3 sections, the definition of AI, the Value and combining the two
"""

from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import pandas as pd
  
df = pd.read_csv(r"SongLyrics.csv", encoding ="latin-1")
  
comment_words = ''
stopwords = set(STOPWORDS)

"""
Testing Lord Huron Lyrics for the fun of it
"""

# iterate through the lyrics column
for val in df.WhenTheNightIsOver:
    # typecaste each val to string
    val = str(val)
    tokens = val.split()
    # Converts each token into lowercase
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
    comment_words += " ".join(tokens)+" "
  
wordcloud = WordCloud(width = 800, height = 800,
                background_color ='black',
                stopwords = stopwords,
                min_font_size = 10).generate(comment_words)
  
                
plt.figure(figsize = (8, 8), facecolor = None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad = 0)
plt.show()
