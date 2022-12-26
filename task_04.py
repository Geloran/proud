def music():
    my_favorite_songs = {
    'Waste a Moment': 3.03,
    'New Salvation' : 4.02,
    'Staying\' Alive' : 3.40,
    'Out of Touch' : 3.03,
    'A Sorta Fairtale': 5.28,
    'Easy' :4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
    import random
    s = sum(random.sample(list(my_favorite_songs.values()), 3))
    print ("3 случайных песни звучат" , s , "минут")


music() 

