# WhatsApp Chat WordCloud Generator for sentiment analysis

This project is aimed at trying to understand the word dynamics between two people in a whatsapp chat to try and understand their sentiment. This is just a fun project I came up with to out of curiosity.

![Laid To Rest](https://github.com/manand881/Whatsapp-Wordcloud-Generator/blob/master/Laid%20To%20Rest.png)

<p align="center">
  <img width="460" height="300" src="https://github.com/manand881/Whatsapp-Wordcloud-Generator/blob/master/Laid%20To%20Rest.png">
</p>

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install [wordcloud](https://pypi.org/project/wordcloud/) and [matplotlib](https://pypi.org/project/matplotlib/).

```bash
pip install wordcloud
pip install matplotlib
```

## Usage

The project has the following import statements so make sure that all the conditions are met.

```python
from wordcloud  import WordCloud, STOPWORDS                             # importing Wordcloud to create wordcloud object and define stop words
from os.path    import isfile, join                                     # importing isFile and join to detect if the items in the directory are files                         
from os         import listdir                                          # importing listdir to list items in the directory

import matplotlib.pyplot as plt                                         # importing matplotliib to process wordcloud data into an image
import os                                                               # importing os to get current working direcotry
```

## How to Use

* Import whatsApp chats to the same directory as a the program 'WhatsApp Chat WordCloud.py'. you can import and process multiple WhatsApp chats at once.

* Do not chage the name of the imported WhatsApp chat.

* Do not change or edit the contents of the WhatsApp chat.

## Warning

This is merely an exercise of curiosity and does not imply to be a tool for phycological analysis. It is recommended for you to not come to any conclusions unless you are a trained individual.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
I would be happy to answer any question by [mail](manand881@gmail.com)

## License
[The Unlicense](https://choosealicense.com/licenses/unlicense/)
