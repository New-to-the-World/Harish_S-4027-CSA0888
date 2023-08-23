def determine_season(month, day):
    seasons = {
        'Mar': (3, 20), 'Jun': (6, 21), 'Sep': (9, 22), 'Dec': (12, 21)
    }
    for season, (season_month, season_day) in seasons.items():
        if (month, day) >= (season_month, season_day):
            return season
    return 'Winter'

month = input("Enter the month (First three letters capitalized): ")
day = int(input("Enter the day: "))
season = determine_season(month, day)
print("The season associated with the date is:", season)
