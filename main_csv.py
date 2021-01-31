import os
import csv
import json
import javlib
import re

def find_all_movie(work_direct):
 
    total = []
    file_type = ['.mp4', '.avi', '.rmvb', '.wmv', '.mov', '.mkv', '.flv', '.ts', '.webm', '.MP4', '.AVI', '.RMVB', '.WMV','.MOV', '.MKV', '.FLV', '.TS', '.WEBM', ]
    dirs = os.listdir(work_direct)
    for entry in dirs:
        f = os.path.join(work_direct, entry)
        if os.path.isdir(f):
            total += find_all_movie(f)
        elif os.path.splitext(f)[1] in file_type:
            movie = entry.split(".",1)[0]
            movie= re.split('([A-Z]*-[0-9]*)',movie)[1]
            total.append(movie)
    return total

def find_new_moive (movies,file_path):
    # print(movies)
    movie_exists = []
    if os.path.exists(file_path):
        with open(file_path,"r",encoding='utf-8') as f : 
            movie_exisits_csv = csv.DictReader(f)
            # movie_exists_json = json.load(f)
            # print(movie_exists_json)
            for movie in movie_exisits_csv:
                movie_exists.append(movie['movie'])
    # print(movie_exists)
    new_movie = list(set(movies).difference(set(movie_exists)))
    return new_movie

def retrive_rating(new_movies):
    result = []
    i = 0
    t = len(new_movies)
    # Log Output
    if t!=0 :
        print("================数据抓取================")
    else :
        print("================无数据抓取==============")
    
    for movie in new_movies:
        i = i+1
        # Log Output
        print("当前进度： ", i,"/",t)
        try:
            json_data={}
            # print (movie.split(".",1)[0])   
            
            # Log Output
            print("当前影片: ",movie)
            json_data=json.loads(javlib.main(movie))
            number = json_data['number']
            actor = json_data['actor']
            score = json_data['score']
            release = json_data['release']
        except :
            number = movie.split(".",1)[0]
            actor =''
            score =''
            release =''
        
        finally:
            if movie != number:
                number = movie
            movie_infor = {
                'movie':number,
                'actor':actor,
                'score':score,
                'release':release
            }
        # Log Output
        print("相关讯息: ",movie_infor)
        print("----------------------------------------")
        result.append(movie_infor)

    if i!=0 :
        print("================数据抓取完毕============")
    else :
        print("========================================")
    return result

def write_file(movie_ratings,file_path,rewrite):
    headers = ['movie', 'actor', 'score', 'release']
    with open (file_path,'a',encoding='utf-8') as f:
        f_csv = csv.DictWriter(f, headers)
        if rewrite:
            f_csv.writeheader()
        f_csv.writerows(movie_ratings)


def jav_rates(work_direct,file_path):

#     # find all movies of the word directory
    movies = find_all_movie(work_direct)

    # Log Output
    print("============任务基本信息================")
    print("已有电影数量：",len(movies))

     # compare and find new movies in the directoyr
    new_movies = find_new_moive(movies,file_path)

     # Log Output
    print("data.csv中已有电影数量：",(len(movies)-len(new_movies)))
    print("本次新增电影数量: ",len(new_movies))
    print("========================================")

    if len(new_movies) == len(movies) :
         rewrite = 1
    else:
        rewrite = 0

     # print(rewrite)
#     # retrive rating of the new movies
    movie_rating = retrive_rating(new_movies)

     # Log Output
    
    print("================写入文档================")
     # update file
    write_file(movie_rating,file_path,rewrite)
    
    # Log Output
    print("================写入完毕================")

if __name__ == '__main__':
    version = '3.7'
    FILE_PATH = 'data2.csv'
   #WORK_DIRECT = 'Z:/Movies/JAV_output'
    WORK_DIRECT = 'Z:/Movies/in'
    # Main function: read all the movies from the work directory and get their ratings.
    jav_rates(WORK_DIRECT,FILE_PATH)

    # total = find_all_movie("Z:\Movies\JAV_output")
    
