import media
import fresh_tomatoes

avatar = media.Movie("Avatar",
                     "On the lush alien world of Pandora live the Na'vi, beings who appear primitive but are highly evolved. Because the planet's environment is poisonous, human/Na'vi hybrids, called Avatars, must link to human minds to allow for free movement on Pandora. Jake Sully (Sam Worthington), a paralyzed former Marine, becomes mobile again through one such Avatar and falls in love with a Na'vi woman (Zoe Saldana). As a bond with her grows, he is drawn into a battle for the survival of her world.",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

titanic = media.Movie("Titanic",
                      "James Cameron's Titanic is an epic, action-packed romance set against the ill-fated maiden voyage of the R.M.S. Titanic; the pride and joy of the White Star Line and, at the time, the largest moving object ever built. She was the most luxurious liner of her era, the ship of dreams, which ultimately carried over 1,500 people to their death in the ice cold waters of the North Atlantic in the early hours of April 15, 1912.",
                      "https://fanart.tv/fanart/movies/597/movieposter/titanic-521a6089df23f.jpg",
                      "https://www.youtube.com/watch?v=zCy5WQ9S4c0")

home_alone = media.Movie("Home Alone",
                         "When bratty 8-year-old Kevin McCallister (Macaulay Culkin) acts out the night before a family trip to Paris, his mother (Catherine O'Hara) makes him sleep in the attic. After the McCallisters mistakenly leave for the airport without Kevin, he awakens to an empty house and assumes his wish to have no family has come true. But his excitement sours when he realizes that two con men (Joe Pesci, Daniel Stern) plan to rob the McCallister residence, and that he alone must protect the family home.",
                         "https://images-na.ssl-images-amazon.com/images/I/A1srz798CtL._RI_.jpg",
                         "https://www.youtube.com/watch?v=CK2Btk6Ybm0")

alo = media.Movie("Alo",
                   "A talented Bengali city-girl of Kolkata wins the heart of everyone in a village. She decides to stay in a village to fulfil the last wish of his husband's mother. She refuses to accept the stereotype of low mentality and entwines everyone in love and happiness. But it was shortlived. She died giving birth to a baby girl",
                   "https://learningandcreativity.com/silhouette/wp-content/uploads/sites/3/2014/06/Alo.jpg",
                   "https://www.youtube.com/watch?v=fzcK0buXyKg")
movies = [avatar, titanic, home_alone, alo]

fresh_tomatoes.open_movies_page(movies)