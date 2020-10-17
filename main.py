import os
import json
import javlib

def find_all_movie(work_direct):
 
    total = []
    file_type = ['.mp4', '.avi', '.rmvb', '.wmv', '.mov', '.mkv', '.flv', '.ts', '.webm', '.MP4', '.AVI', '.RMVB', '.WMV','.MOV', '.MKV', '.FLV', '.TS', '.WEBM', ]
    dirs = os.listdir(work_direct)
    for entry in dirs:
        f = os.path.join(work_direct, entry)
        if os.path.isdir(f):
            total += find_all_movie(f)
        elif os.path.splitext(f)[1] in file_type:
            total.append(entry.split(".",1)[0])
    return total

def find_new_moive (movies,file_path):
    # print(movies)
    movie_exists = []
    if os.path.exists(file_path):
        with open(file_path,"r") as f :
            movie_exists_json = json.load(f)
            # print(movie_exists_json)
            for movie in movie_exists_json:
                movie_exists.append(movie['movie'])
    # print(movie_exists)
    new_movie = list(set(movies).difference(set(movie_exists)))
    return new_movie

def retrive_rating(new_movies):
    result = []
    for movie in new_movies:
        try:
            json_data={}
            # print (movie.split(".",1)[0])   
            print(movie)
            json_data=json.loads(javlib.main(movie))
            number = json_data['number']
            actor = json_data['actor']
            score = json_data['score']
        except :
            number = movie.split(".",1)[0]
            actor =''
            score =''
             
        finally:
            movie_infor = {
                'movie':number,
                'actor':actor,
                'score':score
            }

        print(movie_infor)
        result.append(movie_infor)
    return result

def write_file(movie_ratings,file_path):
    with open (file_path,'a',encoding='utf-8') as f:
        json.dump(movie_ratings,f)

def jav_rates(work_direct,file_path):

#     # find all movies of the word directory
    movies = find_all_movie(work_direct)

    print(len(movies))

#     # compare and find new movies in the directoyr
    new_movies = find_new_moive(movies,file_path)

    print (new_movies)

    # retrive rating of the new movies
    movie_rating = retrive_rating(new_movies)

#     # update file
    write_file(movie_rating,file_path)


if __name__ == '__main__':
    version = '3.6'
    FILE_PATH = 'data.json'
    WORK_DIRECT = 'Z:/Movies/JAV_output'

    # Main function: read all the movies from the work directory and get their ratings.
    jav_rates(WORK_DIRECT,FILE_PATH)

    # total = find_all_movie("Z:\Movies\JAV_output")
    
