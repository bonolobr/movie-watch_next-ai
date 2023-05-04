#<------- Import Library and Load Language Model ------->
import spacy
nlp = spacy.load('en_core_web_md')

#<------- Define Lists ------->
movie_list = []

#<------- Define Functions ------->

def read_available_movies():
    '''
    Function reads the avilable movies from the movies.txt file.\n
    Returns a list of all the available movies.
    '''
    with open('movies.txt', 'r+') as file:
        for line in file:
            temp = line.strip()
            movie_list.append(temp)
    return movie_list

def available_movies_dict(movie_list):
    '''
    Function inputs the list of all available movies.\n
    Returns a dictionary of the available movies where the key is the movie title and value is the description
    '''         
    movie_list_tuples = []

    for movie in movie_list:
        movie_tuple = movie.split(' :')
        movie_list_tuples.append(movie_tuple)
        all_movies_dict = dict(movie_list_tuples)
    return all_movies_dict

def movie_suggestion(movie_watched):
    '''
    Function inputs the description of the movie watched.\n
    Returns the movie the user would watch next if they watched the movie inputted.
    '''
    similarity_score_list =[]

    movie_list = read_available_movies()
    available_movies = available_movies_dict(movie_list)

    # Parse the movie watched through the language model
    movie_watched_to_compare = nlp(movie_watched)

    # Run for loops to compare the description of the movie watched to all the available moves in the dictionary
    # Create a list of these similarity scores
    for movie_option_description in available_movies.values():
        similarity = nlp(movie_option_description).similarity(movie_watched_to_compare)
        similarity_score_list.append(similarity )

    # Identify the maximum similarity score
    # Obtain the index number of the maximum similarity score in the similarity score list
    # Apply the index to the dictionary of all available movies to identify the movie to be suggested next that is most similar
    maximum_similarity = max(similarity_score_list)
    for score in similarity_score_list:
        if score ==  maximum_similarity:
            index = similarity_score_list.index(score)
    title_of_similar_movie = list(available_movies)[index]

    return title_of_similar_movie 

#<------- Program ------->

# Define variable that is the description that is associated with the movie watched, named Planet Hulk
Planet_Hulk_desc = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'

suggested_similar_movie_title_watch_next = movie_suggestion(Planet_Hulk_desc)

print(f"Based on the movie you've watched, we'd recommend you watch {suggested_similar_movie_title_watch_next} next")
