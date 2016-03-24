import media
import fresh_tomatoes

'''   *********
ToDo:
    1) Decide on what extra info to provide
    2) Find a way to display that extra info
    3) Write a script to search out and grab the information for each movie (if
        possible)

    irt (2) Perhaps we could modify the bootstrap modal display to give the plot
        summary on one side of the trailer or perhaps even scroll down below the
        trailer?
    irt (1) I am thinking of providing the extra information on the staring
        actors and director, as well as actually providing the summary with maybe
        a link to the imdb page.

        on that note it would be cool to be able to have a python script that
        could grab all the information i usually want to find.

    irt (3) I found something about beautifulsoup module and urllib, see the
        following website for more links and ideas:
        http://stackoverflow.com/questions/2376798/how-to-write-a-python-script-to-search-a-website-html-for-matching-links

    4) Currently running the adding of new movies to the page through different
        script, will need to save and load into this final script
        
      *********   '''

dragon = media.Movie("How to Train Your Dragon",
                     "A boy finds a dragon and befriends it.",
                     "https://upload.wikimedia.org/wikipedia/en/9/99/How_to_Train_Your_Dragon_Poster.jpg",
                     "https://www.youtube.com/watch?v=GfBHLVtbG6U")
star_wars = media.Movie("Star Wars: A New Hope",
                     "A boy finds a lightsaber and takes a stand against an evil empire.",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/8/87/StarWarsMoviePoster1977.jpg/220px-StarWarsMoviePoster1977.jpg",
                     "https://www.youtube.com/watch?v=1g3_CFmnU7k")
dark_knight = media.Movie("The Dark Knight",
                          "Batman must save a city that does not want to be saved.",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/8/8a/Dark_Knight.jpg/220px-Dark_Knight.jpg",
                          "https://www.youtube.com/watch?v=EXeTwQWrcwY")
tome = media.Movie("Terrain of Magical Expertise",
                   "A group of friends must fight a virus that could destroy the virtual world.",
                   "http://orig15.deviantart.net/5584/f/2012/276/8/0/tome__it__s_serious_business_by_kirbopher15-d5gqjl7.jpg",
                   "https://www.youtube.com/watch?v=VH18zV_scgk")
princess_bride = media.Movie("The Princess Bride",
                             "A story about true love, kings, pirates, and starting wars.",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/d/db/Princess_bride.jpg/220px-Princess_bride.jpg",
                             "https://www.youtube.com/watch?v=VYgcrny2hRs")
two_towers = media.Movie("The Lord of the Rings: the Two Towers",
                         "Few fight against many to keep darkness from ruling the world and defending the last bastions of light.",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg/220px-Lord_of_the_Rings_-_The_Two_Towers.jpg",
                         "https://www.youtube.com/watch?v=cvCktPUwkW0")


movies = [dragon, star_wars, dark_knight, tome, princess_bride, two_towers]
fresh_tomatoes.open_movies_page(movies)
