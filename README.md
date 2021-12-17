# SI507-Final-Project

## REQUIRED PACKAGES

* import requests
* import json
* import re
* import html
* from time import sleep
* import os
* from treelib import Tree
* from pandas.core.frame import DataFrame
* import plotly
* import plotly.graph_objects as go
* import plotly.offline as of
* import plotly.express as px
* from geopy.distance import geodesic

## RUNNING INSTRUCTIONS

Firstly, make sure your python has the above package installed. Secondly, download all the files on the github in a single document. Unzip the **yelp_lv_dataset.zip**, since the json file is to large to upload, and make sure the json file in the same path as the other files. Then, open the **final programming code.py** and change the work path to the one where you just downloaded the files and run it. Since I have stored all the data needed in json files and uploaded them, so you can only run this file. Now you can start to interact with the programming.

If you want to run from getting the hotel data, open the **hotel_data_webscraping.py** file. In addition to changing the working path as mentioned in the previous paragraph, you also need to change the headers to your own device or the site will refuse access. Way to do so it to, taking Google Chrome for example, right click on the web page and click on Inspect, under Network click on Doc, press F5 to refresh the data if there is no response, find the user-agent in the displayed file and that is your header. Then, you can run this file and get the hotel data.

## Authors

* **Xiaoyue Liu** - *Initial work* - 

## Acknowledgments

* Professor Bobby Madamanchi and the instruction team of SI 507 in Fall 2021, whose code examples helped form the basis of this project.
