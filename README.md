# Welcome to "The Real House Helps of Kawagware" Episode Link Retrieval Notebook!

### App now available on streamlit

https://karusamuel-thrk-scraper-app-zdi1ne.streamlit.app/

🎬 Lights, Camera, Links! 📺

Get ready to streamline your "Real House Helps of Kawagware" binge-watching experience like never before! In this notebook, we're on a mission to organize and gather all the episode links from the show's YouTube channel, ensuring you can navigate through the series effortlessly.

No more endless scrolling or frantic searching – we're here to curate a neatly ordered list of episode links, so you can dive straight into the drama without missing a beat. From the pilot to the latest release, every episode link will be at your fingertips, meticulously arranged for your convenience.

Join us as we harness the power of web scraping to extract these valuable links, ensuring they're presented in perfect sequential order. With our streamlined approach, you'll spend less time searching and more time indulging in the captivating world of "The Real House Helps of Kawagware."

So grab your 🍿, settle into your favorite spot, and let's embark on this quest to organize and conquer the episode links. Lights, camera, links – let's make binge-watching a breeze!

# imports

importing the necessary libraries for the project 


```python
# common imports 
import numpy as np
import pandas as pd
```


# Data Sources 

the data source for this project is going to be youtube data is scraped using scrape tube package from the TRHK main youtube channel 

### Scrape Tube

ScrapeTube is a Python library designed specifically for scraping  data from YouTube. It offers a convenient and efficient way to extract various types of information from YouTube channels, videos, and playlists. 📺 👾

[ Check out ScrapeTube here!](https://github.com/TeamHG-Memex/scrape-tube) 


```python
# Scrapetube import
import scrapetube

# Getting data from the TRHK 
videos = scrapetube.get_channel("UCP456Szyc9zy-f0j3UoHzeg")


```

An empty data frame to store our data, let's call it  `df`



```python
df = pd.DataFrame()
```

loop through all the found videos assigning the to a list 
loop through all of the YouTube video objects found in the search results and  assign them to a list



```python

videos_list = []
for video in  videos:
    videos_list.append(video)
```

convert the list to a pandas data frame [df = pd.DataFrame (list)]



```python
df = pd.DataFrame(videos_list)
```


```python
# save a copy of our scraped data before cleaning 
df.to_csv("data/scraped_data.csv")
```

## Data Description


```python
# getting Dataframe info
df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 710 entries, 0 to 709
    Data columns (total 14 columns):
     #   Column              Non-Null Count  Dtype 
    ---  ------              --------------  ----- 
     0   videoId             710 non-null    object
     1   thumbnail           710 non-null    object
     2   title               710 non-null    object
     3   descriptionSnippet  709 non-null    object
     4   publishedTimeText   710 non-null    object
     5   lengthText          710 non-null    object
     6   viewCountText       710 non-null    object
     7   navigationEndpoint  710 non-null    object
     8   trackingParams      710 non-null    object
     9   showActionMenu      710 non-null    bool  
     10  shortViewCountText  710 non-null    object
     11  menu                710 non-null    object
     12  thumbnailOverlays   710 non-null    object
     13  richThumbnail       564 non-null    object
    dtypes: bool(1), object(13)
    memory usage: 72.9+ KB


- We have 710 videos from the channel with 14 columns  ����

- Most of our data is in nested objects / lists and needs to be cleaned 🧹

- We also have unnecessary columns for our use case  🗑️

- Our data is relatively clean with only a few missing rows 🧐 


## Data Cleaning

### Dropping unnecessary columns  

we have the following columns 

* **videoId** - the unique identifier for  the video

* **thumbnail** - a  thumbnail image of the video

* **title** - the title of the video

* **descriptionSnippet**  - a short description of the video

* **publishedTimeText** - the date and time the video was published

* **lengthText** - the length of the video

* **viewCountText** - the number of views the video has received 

### Columns to drop

The following columns are not necessary for our analysis and can  be dropped:

* `navigationEndpoint`: This column contains the URL to the video's page on YouTube.
* `trackingParams`: This column contains  tracking parameters that are used by YouTube to track the performance of the video.
* `showActionMenu`: This column indicates whether or not the action menu is visible on the video's page.
* `shortViewCountText`: This column contains the number of short views the video has received.
* ` menu`: This column contains the menu items that are available on the video's page.
* `thumbnailOverlays`: This column contains the overlays that are displayed on the video's thumbnail.
* `richThumbnail`: This column contains the rich thumbnail that is displayed on the video's page. 



```python
df = df.drop(columns=['trackingParams','showActionMenu','shortViewCountText','menu','thumbnailOverlays','richThumbnail',"navigationEndpoint"])
df.head(5)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>videoId</th>
      <th>thumbnail</th>
      <th>title</th>
      <th>descriptionSnippet</th>
      <th>publishedTimeText</th>
      <th>lengthText</th>
      <th>viewCountText</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>nsJIaPvbspg</td>
      <td>{'thumbnails': [{'url': 'https://i.ytimg.com/v...</td>
      <td>{'runs': [{'text': 'Heartbreak ni ile ile | TR...</td>
      <td>{'runs': [{'text': 'The Real Househelps of Kaw...</td>
      <td>{'simpleText': '10 months ago'}</td>
      <td>{'accessibility': {'accessibilityData': {'labe...</td>
      <td>{'simpleText': '251,135 views'}</td>
    </tr>
    <tr>
      <th>1</th>
      <td>kn11JasWx28</td>
      <td>{'thumbnails': [{'url': 'https://i.ytimg.com/v...</td>
      <td>{'runs': [{'text': 'Luma Mongaras wakwende uko...</td>
      <td>{'runs': [{'text': 'The Real Househelps of Kaw...</td>
      <td>{'simpleText': '10 months ago'}</td>
      <td>{'accessibility': {'accessibilityData': {'labe...</td>
      <td>{'simpleText': '197,956 views'}</td>
    </tr>
    <tr>
      <th>2</th>
      <td>EqvW6AwLB5s</td>
      <td>{'thumbnails': [{'url': 'https://i.ytimg.com/v...</td>
      <td>{'runs': [{'text': 'Mapenzi Inawaramba! | TRHK...</td>
      <td>{'runs': [{'text': 'The Real Househelps of Kaw...</td>
      <td>{'simpleText': '10 months ago'}</td>
      <td>{'accessibility': {'accessibilityData': {'labe...</td>
      <td>{'simpleText': '47,116 views'}</td>
    </tr>
    <tr>
      <th>3</th>
      <td>xX_6THG8YR4</td>
      <td>{'thumbnails': [{'url': 'https://i.ytimg.com/v...</td>
      <td>{'runs': [{'text': 'Ndanda ni wewe! | TRHK EP3...</td>
      <td>{'runs': [{'text': 'The Real Househelps of Kaw...</td>
      <td>{'simpleText': '10 months ago'}</td>
      <td>{'accessibility': {'accessibilityData': {'labe...</td>
      <td>{'simpleText': '153,011 views'}</td>
    </tr>
    <tr>
      <th>4</th>
      <td>qZ2jpOiPQsQ</td>
      <td>{'thumbnails': [{'url': 'https://i.ytimg.com/v...</td>
      <td>{'runs': [{'text': 'He he he!!! Sema kuwithdra...</td>
      <td>{'runs': [{'text': 'The Real Househelps of Kaw...</td>
      <td>{'simpleText': '10 months ago'}</td>
      <td>{'accessibility': {'accessibilityData': {'labe...</td>
      <td>{'simpleText': '179,489 views'}</td>
    </tr>
  </tbody>
</table>
</div>



## checking for null values 


```python
df.isnull().sum()
```




    videoId               0
    thumbnail             0
    title                 0
    descriptionSnippet    1
    publishedTimeText     0
    lengthText            0
    viewCountText         0
    dtype: int64



We have only 1 null value in descriptionSnippet


```python
# finding the row with the null value
df[df["descriptionSnippet"].isna()]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>videoId</th>
      <th>thumbnail</th>
      <th>title</th>
      <th>descriptionSnippet</th>
      <th>publishedTimeText</th>
      <th>lengthText</th>
      <th>viewCountText</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>709</th>
      <td>q7gLD7y8oik</td>
      <td>{'thumbnails': [{'url': 'https://i.ytimg.com/v...</td>
      <td>{'runs': [{'text': 'The Real Househelps of Kaw...</td>
      <td>NaN</td>
      <td>{'simpleText': '10 years ago'}</td>
      <td>{'accessibility': {'accessibilityData': {'labe...</td>
      <td>{'simpleText': '16,037 views'}</td>
    </tr>
  </tbody>
</table>
</div>



The above column is the column with null value

## Data conversion

### Cleaning thumbnail column


```python
# Getting thumbnail link from nested data 
df['thumbnail'] = df['thumbnail'].apply(lambda x:x['thumbnails'][0]['url'])
df.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>videoId</th>
      <th>thumbnail</th>
      <th>title</th>
      <th>descriptionSnippet</th>
      <th>publishedTimeText</th>
      <th>lengthText</th>
      <th>viewCountText</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>nsJIaPvbspg</td>
      <td>https://i.ytimg.com/vi/nsJIaPvbspg/hqdefault.j...</td>
      <td>{'runs': [{'text': 'Heartbreak ni ile ile | TR...</td>
      <td>{'runs': [{'text': 'The Real Househelps of Kaw...</td>
      <td>{'simpleText': '10 months ago'}</td>
      <td>{'accessibility': {'accessibilityData': {'labe...</td>
      <td>{'simpleText': '251,135 views'}</td>
    </tr>
    <tr>
      <th>1</th>
      <td>kn11JasWx28</td>
      <td>https://i.ytimg.com/vi/kn11JasWx28/hqdefault.j...</td>
      <td>{'runs': [{'text': 'Luma Mongaras wakwende uko...</td>
      <td>{'runs': [{'text': 'The Real Househelps of Kaw...</td>
      <td>{'simpleText': '10 months ago'}</td>
      <td>{'accessibility': {'accessibilityData': {'labe...</td>
      <td>{'simpleText': '197,956 views'}</td>
    </tr>
  </tbody>
</table>
</div>



### Cleaning title Column 


```python
# Getting title text from nested title data
df['title'] = df["title"].apply(lambda x:x['runs'][0]['text'])
df.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>videoId</th>
      <th>thumbnail</th>
      <th>title</th>
      <th>descriptionSnippet</th>
      <th>publishedTimeText</th>
      <th>lengthText</th>
      <th>viewCountText</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>nsJIaPvbspg</td>
      <td>https://i.ytimg.com/vi/nsJIaPvbspg/hqdefault.j...</td>
      <td>Heartbreak ni ile ile | TRHK EP312 Pt 2</td>
      <td>{'runs': [{'text': 'The Real Househelps of Kaw...</td>
      <td>{'simpleText': '10 months ago'}</td>
      <td>{'accessibility': {'accessibilityData': {'labe...</td>
      <td>{'simpleText': '251,135 views'}</td>
    </tr>
    <tr>
      <th>1</th>
      <td>kn11JasWx28</td>
      <td>https://i.ytimg.com/vi/kn11JasWx28/hqdefault.j...</td>
      <td>Luma Mongaras wakwende uko NKT! | TRHK EP312 Pt 1</td>
      <td>{'runs': [{'text': 'The Real Househelps of Kaw...</td>
      <td>{'simpleText': '10 months ago'}</td>
      <td>{'accessibility': {'accessibilityData': {'labe...</td>
      <td>{'simpleText': '197,956 views'}</td>
    </tr>
  </tbody>
</table>
</div>



### Cleaning descriptionSnippet Column


```python
# Getting description text from nested descriptionSnippet 
# For null values fill with unknown
df['descriptionSnippet'] = df['descriptionSnippet'].apply(lambda x: x['runs'][0]['text'] if isinstance(x,dict) else "unknown")
df.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>videoId</th>
      <th>thumbnail</th>
      <th>title</th>
      <th>descriptionSnippet</th>
      <th>publishedTimeText</th>
      <th>lengthText</th>
      <th>viewCountText</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>nsJIaPvbspg</td>
      <td>https://i.ytimg.com/vi/nsJIaPvbspg/hqdefault.j...</td>
      <td>Heartbreak ni ile ile | TRHK EP312 Pt 2</td>
      <td>The Real Househelps of Kawangware follows the ...</td>
      <td>{'simpleText': '10 months ago'}</td>
      <td>{'accessibility': {'accessibilityData': {'labe...</td>
      <td>{'simpleText': '251,135 views'}</td>
    </tr>
    <tr>
      <th>1</th>
      <td>kn11JasWx28</td>
      <td>https://i.ytimg.com/vi/kn11JasWx28/hqdefault.j...</td>
      <td>Luma Mongaras wakwende uko NKT! | TRHK EP312 Pt 1</td>
      <td>The Real Househelps of Kawangware follows the ...</td>
      <td>{'simpleText': '10 months ago'}</td>
      <td>{'accessibility': {'accessibilityData': {'labe...</td>
      <td>{'simpleText': '197,956 views'}</td>
    </tr>
  </tbody>
</table>
</div>



### Cleaning publishedTimeText Column


```python
# Getting publishedTimeText from nested object 
df['publishedTimeText'] = df['publishedTimeText'].apply(lambda x:x['simpleText'])
df.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>videoId</th>
      <th>thumbnail</th>
      <th>title</th>
      <th>descriptionSnippet</th>
      <th>publishedTimeText</th>
      <th>lengthText</th>
      <th>viewCountText</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>nsJIaPvbspg</td>
      <td>https://i.ytimg.com/vi/nsJIaPvbspg/hqdefault.j...</td>
      <td>Heartbreak ni ile ile | TRHK EP312 Pt 2</td>
      <td>The Real Househelps of Kawangware follows the ...</td>
      <td>10 months ago</td>
      <td>{'accessibility': {'accessibilityData': {'labe...</td>
      <td>{'simpleText': '251,135 views'}</td>
    </tr>
    <tr>
      <th>1</th>
      <td>kn11JasWx28</td>
      <td>https://i.ytimg.com/vi/kn11JasWx28/hqdefault.j...</td>
      <td>Luma Mongaras wakwende uko NKT! | TRHK EP312 Pt 1</td>
      <td>The Real Househelps of Kawangware follows the ...</td>
      <td>10 months ago</td>
      <td>{'accessibility': {'accessibilityData': {'labe...</td>
      <td>{'simpleText': '197,956 views'}</td>
    </tr>
  </tbody>
</table>
</div>



### Cleaning LengthText Column 


```python
# Getting lengthText from nested object  
df["lengthText"] = df["lengthText"].apply(lambda x:x['accessibility']['accessibilityData']['label'])
df.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>videoId</th>
      <th>thumbnail</th>
      <th>title</th>
      <th>descriptionSnippet</th>
      <th>publishedTimeText</th>
      <th>lengthText</th>
      <th>viewCountText</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>nsJIaPvbspg</td>
      <td>https://i.ytimg.com/vi/nsJIaPvbspg/hqdefault.j...</td>
      <td>Heartbreak ni ile ile | TRHK EP312 Pt 2</td>
      <td>The Real Househelps of Kawangware follows the ...</td>
      <td>10 months ago</td>
      <td>12 minutes, 36 seconds</td>
      <td>{'simpleText': '251,135 views'}</td>
    </tr>
    <tr>
      <th>1</th>
      <td>kn11JasWx28</td>
      <td>https://i.ytimg.com/vi/kn11JasWx28/hqdefault.j...</td>
      <td>Luma Mongaras wakwende uko NKT! | TRHK EP312 Pt 1</td>
      <td>The Real Househelps of Kawangware follows the ...</td>
      <td>10 months ago</td>
      <td>11 minutes, 18 seconds</td>
      <td>{'simpleText': '197,956 views'}</td>
    </tr>
  </tbody>
</table>
</div>



### Cleaning viewCountText Column


```python
# Getting viewCountText from nested object 
df['viewCountText'] = df['viewCountText'].apply(lambda x:x['simpleText'])
df.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>videoId</th>
      <th>thumbnail</th>
      <th>title</th>
      <th>descriptionSnippet</th>
      <th>publishedTimeText</th>
      <th>lengthText</th>
      <th>viewCountText</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>nsJIaPvbspg</td>
      <td>https://i.ytimg.com/vi/nsJIaPvbspg/hqdefault.j...</td>
      <td>Heartbreak ni ile ile | TRHK EP312 Pt 2</td>
      <td>The Real Househelps of Kawangware follows the ...</td>
      <td>10 months ago</td>
      <td>12 minutes, 36 seconds</td>
      <td>251,135 views</td>
    </tr>
    <tr>
      <th>1</th>
      <td>kn11JasWx28</td>
      <td>https://i.ytimg.com/vi/kn11JasWx28/hqdefault.j...</td>
      <td>Luma Mongaras wakwende uko NKT! | TRHK EP312 Pt 1</td>
      <td>The Real Househelps of Kawangware follows the ...</td>
      <td>10 months ago</td>
      <td>11 minutes, 18 seconds</td>
      <td>197,956 views</td>
    </tr>
  </tbody>
</table>
</div>



- Append the videoId to end of the YouTube link:  



```python
df = df.assign(Link='https://www.youtube.com/watch?v='+df['videoId'])

```


```python
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>videoId</th>
      <th>thumbnail</th>
      <th>title</th>
      <th>descriptionSnippet</th>
      <th>publishedTimeText</th>
      <th>lengthText</th>
      <th>viewCountText</th>
      <th>Link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>nsJIaPvbspg</td>
      <td>https://i.ytimg.com/vi/nsJIaPvbspg/hqdefault.j...</td>
      <td>Heartbreak ni ile ile | TRHK EP312 Pt 2</td>
      <td>The Real Househelps of Kawangware follows the ...</td>
      <td>10 months ago</td>
      <td>12 minutes, 36 seconds</td>
      <td>251,135 views</td>
      <td>https://www.youtube.com/watch?v=nsJIaPvbspg</td>
    </tr>
    <tr>
      <th>1</th>
      <td>kn11JasWx28</td>
      <td>https://i.ytimg.com/vi/kn11JasWx28/hqdefault.j...</td>
      <td>Luma Mongaras wakwende uko NKT! | TRHK EP312 Pt 1</td>
      <td>The Real Househelps of Kawangware follows the ...</td>
      <td>10 months ago</td>
      <td>11 minutes, 18 seconds</td>
      <td>197,956 views</td>
      <td>https://www.youtube.com/watch?v=kn11JasWx28</td>
    </tr>
    <tr>
      <th>2</th>
      <td>EqvW6AwLB5s</td>
      <td>https://i.ytimg.com/vi/EqvW6AwLB5s/hqdefault.j...</td>
      <td>Mapenzi Inawaramba! | TRHK EP312 Promo</td>
      <td>The Real Househelps of Kawangware follows the ...</td>
      <td>10 months ago</td>
      <td>44 seconds</td>
      <td>47,116 views</td>
      <td>https://www.youtube.com/watch?v=EqvW6AwLB5s</td>
    </tr>
    <tr>
      <th>3</th>
      <td>xX_6THG8YR4</td>
      <td>https://i.ytimg.com/vi/xX_6THG8YR4/hqdefault.j...</td>
      <td>Ndanda ni wewe! | TRHK EP311 Pt 2</td>
      <td>The Real Househelps of Kawangware follows the ...</td>
      <td>10 months ago</td>
      <td>11 minutes, 53 seconds</td>
      <td>153,011 views</td>
      <td>https://www.youtube.com/watch?v=xX_6THG8YR4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>qZ2jpOiPQsQ</td>
      <td>https://i.ytimg.com/vi/qZ2jpOiPQsQ/hqdefault.j...</td>
      <td>He he he!!! Sema kuwithdraw pesa kwa choo | TR...</td>
      <td>The Real Househelps of Kawangware follows the ...</td>
      <td>10 months ago</td>
      <td>12 minutes, 8 seconds</td>
      <td>179,489 views</td>
      <td>https://www.youtube.com/watch?v=qZ2jpOiPQsQ</td>
    </tr>
  </tbody>
</table>
</div>




```python
# reorder our dataframe from the first episode to the last
df.sort_index(ascending=False)
df.head()

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>videoId</th>
      <th>thumbnail</th>
      <th>title</th>
      <th>descriptionSnippet</th>
      <th>publishedTimeText</th>
      <th>lengthText</th>
      <th>viewCountText</th>
      <th>Link</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>nsJIaPvbspg</td>
      <td>https://i.ytimg.com/vi/nsJIaPvbspg/hqdefault.j...</td>
      <td>Heartbreak ni ile ile | TRHK EP312 Pt 2</td>
      <td>The Real Househelps of Kawangware follows the ...</td>
      <td>10 months ago</td>
      <td>12 minutes, 36 seconds</td>
      <td>251,135 views</td>
      <td>https://www.youtube.com/watch?v=nsJIaPvbspg</td>
    </tr>
    <tr>
      <th>1</th>
      <td>kn11JasWx28</td>
      <td>https://i.ytimg.com/vi/kn11JasWx28/hqdefault.j...</td>
      <td>Luma Mongaras wakwende uko NKT! | TRHK EP312 Pt 1</td>
      <td>The Real Househelps of Kawangware follows the ...</td>
      <td>10 months ago</td>
      <td>11 minutes, 18 seconds</td>
      <td>197,956 views</td>
      <td>https://www.youtube.com/watch?v=kn11JasWx28</td>
    </tr>
    <tr>
      <th>2</th>
      <td>EqvW6AwLB5s</td>
      <td>https://i.ytimg.com/vi/EqvW6AwLB5s/hqdefault.j...</td>
      <td>Mapenzi Inawaramba! | TRHK EP312 Promo</td>
      <td>The Real Househelps of Kawangware follows the ...</td>
      <td>10 months ago</td>
      <td>44 seconds</td>
      <td>47,116 views</td>
      <td>https://www.youtube.com/watch?v=EqvW6AwLB5s</td>
    </tr>
    <tr>
      <th>3</th>
      <td>xX_6THG8YR4</td>
      <td>https://i.ytimg.com/vi/xX_6THG8YR4/hqdefault.j...</td>
      <td>Ndanda ni wewe! | TRHK EP311 Pt 2</td>
      <td>The Real Househelps of Kawangware follows the ...</td>
      <td>10 months ago</td>
      <td>11 minutes, 53 seconds</td>
      <td>153,011 views</td>
      <td>https://www.youtube.com/watch?v=xX_6THG8YR4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>qZ2jpOiPQsQ</td>
      <td>https://i.ytimg.com/vi/qZ2jpOiPQsQ/hqdefault.j...</td>
      <td>He he he!!! Sema kuwithdraw pesa kwa choo | TR...</td>
      <td>The Real Househelps of Kawangware follows the ...</td>
      <td>10 months ago</td>
      <td>12 minutes, 8 seconds</td>
      <td>179,489 views</td>
      <td>https://www.youtube.com/watch?v=qZ2jpOiPQsQ</td>
    </tr>
  </tbody>
</table>
</div>



save the cleaned data 


```python
df.to_csv("data/cleaned_data.csv")
```

#### woohoo! We've Successfully Scraped "The Real House Helps of Kawagware" YouTube Channel!

🎉📺🎉

We've reached the end of our exhilarating journey through the digital realm of "The Real House Helps of Kawagware"! Armed with our Python skills and the powerful ScrapeTube library, we've successfully scraped a treasure trove of data from the show's YouTube channel.

But this is just the beginning! With our newfound dataset in hand, the possibilities are endless. Whether we're analyzing viewer engagement, uncovering trends, or simply indulging in some binge-watching, the insights we've gathered will surely add depth and excitement to our fandom.

As we close this notebook, let's take a moment to appreciate the thrill of discovery and the satisfaction of a job well done. We've mastered the art of data scraping, and "The Real House Helps of Kawagware" is just the beginning of our data-driven adventures.

So, what's next? Perhaps another YouTube channel to explore, or maybe a deep dive into data visualization and analysis? The choice is ours, and the world of data awaits!

Until next time, let's keep scraping, keep exploring, and keep embracing the thrill of discovery. And remember, the real drama isn't just on screen – it's in the data!

Lights out, camera off, but the adventure continues... 🚀✨
