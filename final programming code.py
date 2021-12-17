#################################
##### Name: Xiaoyue Liu     #####
##### Uniqname: liyayue     #####
##### SI507 Final Project   #####
##### Fall 2021             #####
#################################


import re
import json
from treelib import Tree
from pandas.core.frame import DataFrame
import plotly
import plotly.graph_objects as go
import plotly.offline as of
import plotly.express as px
from geopy.distance import geodesic
import os

work_path = "D:\\Umich 材料\\课程\\SI 507\\Final project\\check point\\data_jsonfile"
os.chdir(work_path)
filename_yelp = 'yelp_lv_dataset.json'
filename_hotel = 'hotel_data.json'

with open(filename_hotel, 'r') as f:
     hotel_json = json.load(f)
        
with open(filename_yelp, 'r') as f:
     yelp_lv_json = json.load(f)

hotel_rank_ten = ["Four Seasons Hotel Las Vegas", "ARIA Resort & Casino", "Wynn and Encore Las Vegas", "Wynn Las Vegas", "The Venetian Resort", "The Cosmopolitan of Las Vegas, Autograph Collection", "Bellagio Las Vegas", "Trump International Hotel Las Vegas", "Nobu Hotel at Caesars Palace", "Vdara Hotel & Spa at ARIA Las Vegas"]
hotel_all_list = []
for i in hotel_json:
    hotel_all_list.append(i["name"])





def tree_top10_hotel_fun(hotel_rank_ten):
    tree = Tree()    
    tree.create_node('Top 10 hotels in Las Vegas', 'top10_hotel')
    for i in range(len(hotel_rank_ten)):
        tree.create_node(hotel_rank_ten[i], str(i), parent='top10_hotel')
    return tree.show()


def get_hotel_location(hotel):
    lat_lon = []
    for i in hotel_json:
        if i["name"] == hotel:
            lat_lon.append(i["geoPoint"]["latitude"])
            lat_lon.append(i["geoPoint"]["longitude"])
            break
    return lat_lon # float


def calculate_distance_fun(lat_hotel, lon_hotel):    
    dis_dic = []
    dis_value_list = []
    for i in yelp_lv_json:
        dic_res = {}
        dic_res["name"] = i["name"]
        dic_res["address"] = i["address"]
        dic_res["stars"] = float(i["stars"])
        dic_res["review_count"] = int(i["review_count"])
        dic_res["accepts_credit_cards"] = i["accepts_credit_cards"]
        dic_res["restaurants_price_range"] = i["restaurants_price_range"]
        
        lat_res = float(i["latitude"])
        lon_res = float(i["longitude"])
        dic_res["distance"] = round((geodesic((lat_hotel, lon_hotel), (lat_res, lon_res)).miles), 2)
        dis_value_list.append(round((geodesic((lat_hotel, lon_hotel), (lat_res, lon_res)).miles), 2)) # float
        dis_dic.append(dic_res)
    return dis_dic, dis_value_list
        
    
def first_interact_fun(hotel_rank_ten = hotel_rank_ten, hotel_all_list = hotel_all_list):
    while True:
        try:
            hotel_name = str(input("Input the name of the hotel that you are considering to order in Las Vegas. Have no idea? Enter 0 to see the top 10 hotels in Las Vegas!"))
        except:
            pass
        if hotel_name == "0":
            tree_top10_hotel_fun(hotel_rank_ten)
        else:
            if hotel_name in hotel_all_list:
                print("Please wait for a few seconds!")
                lat_hotel_lon = get_hotel_location(hotel_name)
                dis_dic, dis_value_list = calculate_distance_fun(lat_hotel_lon[0], lat_hotel_lon[1])
                dis_input = float(input("How many miles away from the hotel would you like to find the restaurant information about? Ranging from {} to {}.".format(min(dis_value_list), max(dis_value_list))))
                return hotel_name, dis_input, dis_dic, dis_value_list
                break
            else:
                print("This hotel is unavaliable, please try another one.")   

                
def filter_dis_fun(dis_input, dis_dic, dis_value_list):
    dis_filter_dic = []
    dis_value_filter_list = []
    score_value_filter_list = []
    for i in range(len(dis_value_list)):
        if dis_value_list[i] <= dis_input:
            dis_filter_dic.append(dis_dic[i])
            dis_value_filter_list.append(dis_value_list[i])
            score_value_filter_list.append(float(dis_dic[i]["stars"]))
    total_no = len(dis_filter_dic)
    print("{} restaurants meet the requirement.".format(total_no))
    if total_no <= 15:
        for i in dis_filter_dic:
            print("{}, Rating: {}, No. review: {}, Address: {}".format(i["name"], i["stars"], i["review_count"], i["address"]))
    else:
        print("Only the top 15 rated restaurants are shown here.")
        rank_index = [index for index, value in sorted(list(enumerate(score_value_filter_list)), key = lambda x:x[1], reverse = True)]
        for i in range(15):
            print("{}, Rating: {}, No. review: {}, Price range: {}".format(dis_filter_dic[rank_index[i]]["name"], dis_filter_dic[rank_index[i]]["stars"], dis_filter_dic[rank_index[i]]["review_count"], dis_filter_dic[rank_index[i]]["restaurants_price_range"]))
    return dis_filter_dic, dis_value_filter_list, score_value_filter_list
        

def second_interact_fun(dis_dic, dis_value_list):
    while True:
        dis_input_next = float(input("If you want to change the range please enter a number between {} and {}. Or enter 9 for a comparison between two hotels.".format(min(dis_value_list), max(dis_value_list))))
        if dis_input_next == 9:
            break
        else:
            filter_dis_fun(dis_input_next, dis_dic, dis_value_list)
        

def third_interact_fun(hotel_rank_ten = hotel_rank_ten, hotel_all_list = hotel_all_list):
    while True:
        try:
            hotel_name = str(input("Input the name of the hotel that you are considering to order in Las Vegas. Have no idea? Enter 0 to see the top 10 hotels in Las Vegas!"))
        except:
            pass
        if hotel_name == "0":
            tree_top10_hotel_fun(hotel_rank_ten)
        else:
            if hotel_name in hotel_all_list:
#                 print("Please wait for a few seconds!")
#                 lat_hotel_lon = get_hotel_location(hotel_name)
#                 dis_dic, dis_value_list = calculate_distance_fun(lat_hotel_lon[0], lat_hotel_lon[1])
#                 dis_input = float(input("How many miles away from the hotel would you like to find the restaurant information about? Ranging from {} to {}.".format(min(dis_value_list), max(dis_value_list))))
                return hotel_name     # , dis_input, dis_dic, dis_value_list
                break
            else:
                print("This hotel is unavaliable, please try another one.")   

                
def forth_interact_fun():
    option_no = int(input("Enter 1 if you want to know the distance distribution of restaurants near the hotel, enter 2 if you want to know the scattered distribution between ratings and distances of restaurants near the hotel, enter 3 to exit:"))
    return option_no
           
    
def zhixing_fun():
    hotel_name_one = third_interact_fun()
    hotel_name_two = third_interact_fun()
    print("Please wait for a few seconds!")
    dis_dic1, x_value_hotel1 = plot_pre_fun(hotel_name_one)
    dis_dic2, x_value_hotel2 = plot_pre_fun(hotel_name_two)
    
    while True:
        try:
            option_no = forth_interact_fun()
        except:
            pass
        else:
            if option_no == 1:
                histogram_chart_fun(x_value_hotel1, x_value_hotel2, hotel_name_one, hotel_name_two)
            elif option_no == 2:
                scatter_chart_fun(dis_dic1, x_value_hotel1, x_value_hotel2, hotel_name_one, hotel_name_two)
            else:
                print("Exit")
                break
                

def histogram_chart_fun(x_value_hotel1, x_value_hotel2, hotel_name_one, hotel_name_two):
    # Histogram
    hist1 = go.Histogram(x = x_value_hotel1, xbins = {'size': 1}, name = hotel_name_one) 
    hist2 = go.Histogram(x = x_value_hotel2, xbins = {'size': 1}, name = hotel_name_two)
    fig = go.Figure([hist1, hist2])
    fig.update_layout(
        title = 'Distance distribution of restaurants near the hotel',
        xaxis_title = 'Distance (miles)',
        yaxis_title = 'Count',
        bargap = 0.1, 
    )
    fig.show()

    
def plot_pre_fun(hotel_name):
    lat_hotel_lon = get_hotel_location(hotel_name)
    dis_dic, dis_value_list = calculate_distance_fun(lat_hotel_lon[0], lat_hotel_lon[1])
    return dis_dic, dis_value_list


def scatter_chart_fun(dis_dic1, x_value_hotel1, x_value_hotel2, hotel_name_one, hotel_name_two):
    rating_score_list = []
    name_hotel_list1 = [hotel_name_one for i in range(len(dis_dic1))]
    name_hotel_list2 = [hotel_name_two for i in range(len(dis_dic1))]
    for i in dis_dic1:
        rating_score_list.append(float(i["stars"]))
    data_dic1 = {"distance" : x_value_hotel1, "score" : rating_score_list, "hotel name": name_hotel_list1}
    data_dic2 = {"distance" : x_value_hotel2, "score" : rating_score_list, "hotel name": name_hotel_list2}
    dataframe_hotel1 = DataFrame(data_dic1)
    dataframe_hotel2 = DataFrame(data_dic2)
    dataframe_hotel_compare = dataframe_hotel1.append(dataframe_hotel2)

    fig = px.scatter(dataframe_hotel_compare, x = 'distance', y = 'score',
                     color='hotel name',
                     )  
    fig.show()




if __name__ == "__main__":
    hotel_name_input, dis_value_input, distance_dic, distance_value_list = first_interact_fun()
    distance_filter_dic, distance_value_filter_list, score_value_filter_list = filter_dis_fun(dis_value_input, distance_dic, distance_value_list)
    second_interact_fun(distance_dic, distance_value_list)
    zhixing_fun()


