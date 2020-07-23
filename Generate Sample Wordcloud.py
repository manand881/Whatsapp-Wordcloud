# Program to create a word cloud based on the lyrics of 'laid to rest' by lamb of god.


from wordcloud import WordCloud                     # Importing Wordcloud to process input string to word cloud
import matplotlib.pyplot as plt                     # importing matplotliib to process wordcloud data into an image
 

text=str()                                          # creating an empty string

f=open("Laid to Rest Lyrics.txt",encoding="utf8")   # opening the lyric file 


for line in f:
    text=text+f.readline()+" "                      # iterating through all the lines and appending it to the string


print("\n",text)                                    # printing the lyrics to screen
 


wordcloud = WordCloud(width=1920, height=1080, margin=10).generate(text)    # Create the wordcloud object

plt.imshow(wordcloud, interpolation='bilinear')                             # Display the generated image:
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()