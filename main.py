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
            total.append(entry)
    return total

def find_new_moive (movies,file_path):
    with open(file_path,"r") as f :
        data = json.load(f)
    new_movie = list(set(movies).difference(set(data)))
    return new_movie

def retrive_rating(new_movies):
    for movie in new_movies:
        json_data={}
        json_data=json.loads(javlib.main(movie.split(".",1)[0]))
    return json_data

def jav_rates(work_direct,file_path):

#     # find all movies of the word directory
    movies = find_all_movie(work_direct)

#     # compare and find new movies in the directoyr
    new_movies = find_new_moive(movies,file_path)

    # retrive rating of the new movies
    movie_rating = retrive_rating(new_movies)

    return movie_rating

#     # update file
#     write_file(movie_rating,file)


if __name__ == '__main__':
    version = '3.6'
    FILE_PATH ="data.json"
    WORK_DIRECT = "Z:\Movies\JAV_output"

    # Main function: read all the movies from the work directory and get their ratings.
    result = jav_rates(WORK_DIRECT,FILE_PATH)

    print(result)
    # total = find_all_movie("Z:\Movies\JAV_output")
    
