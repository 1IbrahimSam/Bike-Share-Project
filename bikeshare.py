import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("please, select a city (chicago, new york city, washington) : ").lower()
    while city not in CITY_DATA.keys():
        print("Invalid input, please re-enter a valid city")
        city  = input("please, select a city (chicago, new york city, washington) : ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['jan','feb','mar','apr','may','jun','all']
    while True:
              month = input ("Please, select a month (jan, feb, mar, apr, may, jun, all) : ").lower()
              if month in months :
                 break
              else:
                 print("Invalid entry") 
                             
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sat','sun','mon','tus','wed','thu','fri','all']
    while True:
            day = input("Select a day to filter (sat, sun, mon, tus, wed , thu, fri, all) : ").lower()
            if day in days:
                 break
            else:
               print("Retype your selection from the list")
               


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    df['hour'] = df['Start Time'].dt.hour   
    
    if month != 'all':
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    frequent_month = df['month'].mode()[0]

    print('The Most Frequent Month:', frequent_month)


    # TO DO: display the most common day of week
    frequent_day_of_week = df['day_of_week'].mode()[0]

    print('The Most frequent Day Of the Week:', frequent_day_of_week)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]

    print('The Common Start Hour:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_used_start_station = df['Start Station'].mode()[0]

    print("The most commonly used start station is: ", commonly_used_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    print("The most commonly noticed end station is: ", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['frequent combination']= df['Start Station']+ " to " + df['End Station'] 
    trip_stations = df['frequent combination'].mode()[0]
    print('the Most frequent combination of start station and end station trip is : ', trip_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('The total travel time for all selected trips is :', total_time//60, ' mins.')

    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('The mean travel time for all selected trips is :', avg_time//60, ' mins.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('For the displayed data; user types are: ', user_type)

    # TO DO: Display counts of gender   
    try:
        gender_data = df['Gender'].value_counts()
        print('The users data by gender are : ', gender_data)
    except:
          
        print("There is no 'Gender' data for the selected city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print("The earliest year of birth is:", earliest)
        print("The most recent year of birth is: ", recent)
        print("The most common year of birth is: ", common_year)
    except:
        print("There are No Birth Year data for the selected city .")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Appreciate your time, see you soon') 
            break

if __name__ == "__main__":
    main()