def world_series_winners():
    try:
        infile = open('WorldSeriesWinners.txt', 'r')
        search_year = input("Input a year to find the winner of the World Series: ")
    except:
        print("Please enter a valid year.")
        world_series_winners()