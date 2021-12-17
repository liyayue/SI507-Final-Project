#########################################
##### Name: Xiaoyue Liu             #####
##### Uniqname:liyayue              #####
#########################################


import requests
import json
import re
import html
from time import sleep
import os
os.chdir("D:\\Umich 材料\\课程\\SI 507\\Final project\\Data\\Hotel")

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
page_num = 13

def soure_json_formate_change_fun(get_url_text):
    start_index = re.search('{&quot;entityType&quot;:&quot;hotel&quot', get_url_text).span()
    end_index = re.search('isNightlyRate&quot;:true}],&quot;anchorPins&quot', get_url_text).span()
    content_wanted = get_url_text[start_index[0]-1:(end_index[0]+len("isNightlyRate&quot;:true}]"))]
    html_formate = html.unescape(content_wanted)    
    filter_content = html_formate.replace('"offers":[','"offers":')
    filter_content = filter_content.replace('],"sponsoredListing"',',"sponsoredListing"')
    filter_content = filter_content.replace('null','"null"')
    filter_content = filter_content.replace('false',"")
    filter_content = filter_content.replace('true','"true"')
    filter_content = filter_content.replace('candidate_location_ids":[','candidate_location_ids":')
    filter_content = filter_content.replace('],"placement_slot_name',',"placement_slot_name')
    filter_content = filter_content.replace('dates={"H":{"ci":"2021-12-19","co":"2021-12-20","dt":"def"}}','')
    filter_content = filter_content.replace('"isInstantBook":,"isOptimusOffer":,','')
    filter_content = filter_content.replace('"is_managed_bid":,','')
    filter_content = filter_content.replace('dates={\"H\":{\"ci\":\"2021-12-19\",\"co\":\"2021-12-20\",\"dt\":\"def\"}}','')
    filter_content = filter_content.replace('dates={\\"H\\":{\\"ci\\":\\"2021-12-19\\",\\"co\\":\\"2021-12-20\\",\\"dt\\":\\"def\\"}}','')
    filter_content = filter_content.replace('"offers":,','"offers":"null",')
    filter_content = filter_content.replace("Marriott\'s Grand Chateau","Marriott's Grand Chateau")
    try:
        hotel_dic_json = json.loads(filter_content)
    except:
        filter_content = filter_content[0:len(filter_content)-1]
        filter_content = filter_content + "}]"
        hotel_dic_json = json.loads(filter_content)
    return hotel_dic_json


for i in range(page_num):
    if i == 0:
        url = "https://www.tripadvisor.com/Hotels-g45963-Las_Vegas_Nevada-Hotels.html"
    else:
        url = "https://www.tripadvisor.com/Hotels-g45963-oa" + str(30*i) + "-Las_Vegas_Nevada-Hotels.html"
    response = requests.get(url, headers = headers)
    response_text = response.text
    hotel_info_json = soure_json_formate_change_fun(response_text)
    print(i)
    if i == 0:
        hotel_info_json_dic = hotel_info_json
    else:
        hotel_info_json_dic = hotel_info_json_dic + hotel_info_json
    sleep(10)


filename = 'hotel_data.json'
with open(filename, 'w') as fp:
     json.dump(hotel_info_json_dic, fp, indent=15)

