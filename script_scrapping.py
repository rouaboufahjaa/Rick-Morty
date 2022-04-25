from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from crud.episode import add_description_episode
import requests
import os

driver = webdriver.Chrome(ChromeDriverManager().install())
community_episodes = []
community_images=[]
save_path='thumbnails'

for sn in range(1,7):
    driver.get('https://www.imdb.com/title/tt2861424/episodes?season='+ str(sn))
    content = driver.page_source
    page_html = BeautifulSoup(content, 'html.parser')
    episode_containers = page_html.find_all('div', class_ = 'info')
    for episodes in episode_containers:
            season = sn
            episode_number = episodes.meta['content']
            title = episodes.a['title']
            description = episodes.find('div', class_='item_description').text
            add_description_episode(title,description)
            episode_data = [episode_number,title,season, description]
            community_episodes.append(episode_data)
    episode_images = page_html.find_all('div', class_ = 'image')
    for episodes in episode_images:
            thumbnail = episodes.find('img', class_='zero-z-index')
            community_images.append([thumbnail])
            if thumbnail:
                completeName = os. path. join(save_path, thumbnail['src'][36:])
                response = requests.get(thumbnail['src'], stream=True)
                file1 = open(completeName, 'wb').write(response.content)
import pandas as pd 
community_episodes = pd.DataFrame(community_episodes, columns = ['episode_number','title','season', 'description'])
community_images=pd.DataFrame(community_images, columns = ['thumbnail'])
community_episodes.to_csv('csv/description.csv')
community_images.to_csv('csv/thumbnail.csv')
