import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

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
    city = ''

    while city not in CITY_DATA:
        city = input("\What city would you like to know about?  Input either chicago, new york city or washington \n").lower()
        if city in CITY_DATA:
            print('I love that city! Hurray for :',city.upper())
            break
        else:
            print('wrong input,try again')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''

    while month not in MONTH_DATA:
        month = input("\nWhat month would you prefer to learn about?January February... Maybe all?\n").lower()
        if month in MONTH_DATA:
            print(month.upper(),'! Nice choice!')
            break
        else:
            print('wrong input,try again')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = ''
    while day not in DAY_DATA:
        day = input("\nWhich day would you be interested in: Monday, Tuesday... Maybe all?\n").lower()
        if day in DAY_DATA:
            print(day.upper(), " it is! great idea")
            break
        else:
            print("Day not found. Please input: all, monday, tuesday, wednseday,thursday,friday,saturday,sunday")
            break
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

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    month_comm = df['month'].mode()[0]
    print("The most usage occurs during the month of {}.\n".format(month_comm))
    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.weekday_name
    day_comm = df['day'].mode()[0]
    print("The most common day of travel is {}.\n".format(day_comm))
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    hour_comm = df['hour'].mode()[0]
    return print("The most common hour of travel is at {}.\n".format(hour_comm))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_comm = df['Start Station'].mode()[0]



    # TO DO: display most commonly used end station
    end_comm = df['End Station'].mode()[0]

    print("The most commonly used starting and ending stations are {} and {}.\n".format(start_comm, end_comm))


    # TO DO: display most frequent combination of start station and end station trip
    freq_combinat = df.groupby(['Start Station', 'End Station']).size().nlargest(1)

    print("The most frequent start station to end station combination is {}.\n".format(freq_combinat))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total = df['Trip Duration'].sum()


    # TO DO: display mean travel time
    avg = df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The user types are: ', user_types)

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print("The count of user gender from the given fitered data is: \n" + str(gender_count))
    except:
        print("Sorry. No data available!")
        print('Washington does not have gender information')


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth = df['Birth Year'].min()
        latest_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].count()
        print('Earliest birth from the given fitered data is: {}\n'.format(earliest_birth))
        print('Most recent birth from the given fitered data is: {}\n'.format(latest_birth))
        print('Most common birth from the given fitered data is: {}\n'.format(common_birth))
    except:
        print("Sorry. No data available!")



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data on user request.
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    print(df.head())
    next = 0
    while True:
        view_raw_data = input('\nWould you like to see the next rows of raw data? Say yes! Enter yes or no.\n')
        if view_raw_data.lower() != 'yes':
            return
        next = next + 3
        print(df.iloc[next:next+3])
# if more than 5 added information will be missed.
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
