import fresh_tomatoes
import media

toy_story = media.Movies("Toy Story", 
                         "A story of a boy & his toys that come to life",
                         "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=KYz2wyBy3kc")
                         
#print (toy_story.storyline)

avatar = media.Movies("Avatar",
                      "A Marine on an Alien planet",
                      "https://en.wikipedia.org/wiki/Avatar_(2009_film)#/media/File:Avatar-Teaser-Poster.jpg",
                      "https://www.youtube.com/watch?v=cRdxXPV9GNQ")
                      
#print (avatar.storyline)
#avatar.show_trailer()

transformers_5 = media.Movies("Transformers: The Last Knight",
                             "Optimus Prime finds his dead home planet, Cybertron, in which he comes to find he was responsible for its destruction. He finds a way to bring Cybertron back to life, but in order to do so, Optimus needs to find an artifact that is on Earth. ",
                             "https://en.wikipedia.org/wiki/Transformers:_The_Last_Knight#/media/File:Transformers_The_Last_Knight_poster.jpg",
                             "https://www.youtube.com/watch?v=sgnO5fO46pE")
                             
#print (transformers_5 .storyline)
#transformers_5 .show_trailer()

Doctor_strange = media.Movies("Doctor Strange", 
                         "While on a journey of physical and spiritual healing, a brilliant neurosurgeon is drawn into the world of the mystic arts",
                         "http://www.imdb.com/title/tt1211837/mediaviewer/rm3012758016",
                         "https://www.youtube.com/watch?v=HSzx-zryEgM")
                         
Sherlock_holmes = media.Movies("Sherlock Holmes",
                      "Detective Sherlock Holmes and his stalwart partner Watson engage in a battle of wits and brawn with a nemesis whose plot is a threat to all of England",
                      "http://www.imdb.com/title/tt0988045/mediaviewer/rm4059794944",
                      "https://www.youtube.com/watch?v=J7nJksXDBWc")
                      

A_wednesday = media.Movies("A Wednesday!", 
                         "A retiring police officer reminisces about the most astounding day of his career. About a case that was never filed but continues to haunt him in his memories - the case of a man and a Wednesday",
                         "http://www.imdb.com/title/tt1280558/mediaviewer/rm604086528",
                         "https://www.youtube.com/watch?v=OotnobIgFGE")
                        
Movies_list = [toy_story, avatar, transformers_5, Doctor_strange, Sherlock_holmes, A_wednesday]

fresh_tomatoes.open_movies_page(Movies_list)