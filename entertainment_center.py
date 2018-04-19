import fresh_tomatoes
import media

walk_to_remember = media.Movie("A Walk to Remember",
                        "Girl who change the life of a boy.",
                        "http://www.gstatic.com/tv/thumb/movieposters/29274/p29274_p_v8_ae.jpg",
                        "https://www.youtube.com/watch?v=EgdoQ8Oxu2E",
                        "January 25, 2002")

tokyo_drift = media.Movie("Tokyo Drift",
                        "Drift racing in Japan.",
                        "http://www.gstatic.com/tv/thumb/movieposters/159790/p159790_p_v8_ak.jpg",
                        "https://www.youtube.com/watch?v=p8HQ2JLlc4E",
                        "June 16, 2006")

the_foreigner = media.Movie("The Foreigner",
                        "Father seeks vengence for the death of his daughter.",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcSLrVta3GZy0KL1uMKRobMcjsNt3neibUJh2e8_I7T_gqNrRGO2",
                        "https://www.youtube.com/watch?v=CQsRAYf8Cyk",
                        "September 30, 2017")


blood_wars = media.Movie("Underworld: Blood Wars",
                        "Selene vs the lycans.",
                        "https://ia.media-imdb.com/images/M/MV5BMjI5Njk0NTIyNV5BMl5BanBnXkFtZTgwNjU4MjY5MDI@._V1_UX182_CR0,0,182,268_AL_.jpg",
                        "https://www.youtube.com/watch?v=iT8w3gSa000",
                        "January 6, 2017")

john_wick = media.Movie("John Wick",
                        "Payback for killing his dog.",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcS0l5fuKfa2dQBtNqViR1Haj9JpYl4xRtaMasZyv1fLodr9WHsa",
                        "https://www.youtube.com/watch?v=cQ5qjJJlH4A",
                        "October 24, 2014")

civil_war = media.Movie("Captain America: Civil War",
                        "Team cap vs team iron man.",
                        "http://t3.gstatic.com/images?q=tbn:ANd9GcTz1xU3qYlGXViIS51HIQh71D339ceW2nlWnb8zzSaJAL0newVj",
                        "https://www.youtube.com/watch?v=mKScYV9jzG0",
                        "May 6, 2016")

    # Store the Movie objects in a list.
movies = [walk_to_remember, tokyo_drift, the_foreigner, blood_wars, john_wick, civil_war]

    # Open the movie website in the user's browser, featuring the movies above.
fresh_tomatoes.open_movies_page(movies)

