import streamlit as st
import pandas as pd

st.set_page_config(page_title='Kenyan Comedy Series', page_icon='🍿')
'''
## 🍿 The Real Househelps of Kawangware Hub!

Get ready to binge on the latest episodes of your favorite Kenyan comedy series, right here on this exciting Streamlit app! 💃🕺

### 🔥 How to use this app?
 
>> **📺 Quick access to all available episodes** - *click on the expand icon on the top Right of the table to see all the episodes*

>> **🎥 Direct links to the official YouTube videos** - *click on the Youtube Link to watch the episode on Youtube*

>> **🔎 Search for Episodes** - *click on the search icon on the top Right to search for a specific episode `use this format e.g EP 20` for episode 20*

>> **📥 Download Data** - *click on the download icon on the top Right to download a minified version of the data set*

'''

# Load  the cleaned dataset from the /data folder
df = pd.read_csv("data/cleaned_data.csv")

# get only the important columns for us
df = df[['thumbnail', 'title', 'Link']]

df.sort_index(ascending=False,inplace=True)

# Fetch and display data for the current page
def display_data():
    st.dataframe(df,
                #  height=(df.shape[0] + 1) * 35 + 3,
                 use_container_width=True,
                 column_config={
                        "thumbnail": st.column_config.ImageColumn(
                        "P", help="StreamLit app preview screenshots",width="small",
                        )
                        ,
                        "Link": st.column_config.LinkColumn(
                        "Youtube Link",display_text="Link",width="small",
                        )      
                        }
                 ,hide_index=True  
                )

# Display data for the initial page
'''
### 📊 Data 
'''
display_data()

'''

Whether you're a die-hard TRHK fan or just looking for a good laugh, this app has got you covered! So, sit back, relax, and enjoy the show! 🎥📺
'''
