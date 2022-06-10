"""
When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

Input Format

The first line contains , the number of testcases.
Each testcase contains  lines, representing time  and time .
Constraints
Input contains only valid timestamps
Output Format

Print the absolute difference  in seconds.

Sample Input 0

2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
Sample Output 0

25200
88200
Explanation 0

In the first query, when we compare the time in UTC for both the time stamps, we see a difference of 7 hours. which is  seconds or  seconds.

Similarly, in the second query, time difference is 5 hours and 30 minutes for time zone adjusting for that we have a difference of 1 day and 30 minutes. Or 
"""

 
from datetime import datetime
from tkinter.messagebox import NO


def calculate_difference_in_dates_per_year(date_1=None, date_2=None):
    DAYS_IN_MONTHS_DICT_NON_LEAPYEAR = {
        'Jan' : 31,'Feb' : 28,'Mar' : 31, 'Apr' : 30, 'May' : 31, 'Jun' : 30, 'Jul' : 31, 'Aug' : 31, 'Sep' : 30, 'Oct' : 31, 'Nov' : 30, 'Dec' : 31
    }
    DAYS_IN_MONTHS_DICT_LEAPYEAR = {
        'Jan' : 31,'Feb' : 29,'Mar' : 31, 'Apr' : 30, 'May' : 31, 'Jun' : 30, 'Jul' : 31, 'Aug' : 31, 'Sep' : 30, 'Oct' : 31, 'Nov' : 30, 'Dec' : 31
    }

    DAYS_IN_YEAR = 365
    DAYS_IN_LEAP_YEAR = 366

   
    if date_1 and date_2:
        no_of_days_1 , no_of_days_2= 0, 0

        YEAR = date_1[0]
        if check_leap_year(YEAR):
            DAYS_IN_MONTHS_DICT = DAYS_IN_MONTHS_DICT_LEAPYEAR
        else :
            DAYS_IN_MONTHS_DICT = DAYS_IN_MONTHS_DICT_NON_LEAPYEAR

        for month, no_of_days in DAYS_IN_MONTHS_DICT.items(): 
            #calculating the no of days in date 1
            if month != date_1[1]:
                no_of_days_1 += no_of_days
            else:
                no_of_days_1 += date_1[2]
                break

        YEAR = date_2[0]
        if check_leap_year(YEAR):
            DAYS_IN_MONTHS_DICT = DAYS_IN_MONTHS_DICT_LEAPYEAR
        else :
            DAYS_IN_MONTHS_DICT = DAYS_IN_MONTHS_DICT_NON_LEAPYEAR

        for month, no_of_days in DAYS_IN_MONTHS_DICT.items():
            if month != date_2[1]:
                no_of_days_2 += no_of_days
            else:
                no_of_days_2 += date_2[2]
                break

    return (no_of_days_2 - no_of_days_1)

def calculate_difference_in_days_between_years(year_1:int, year_2:int):
    """
    calculates the days between starting of year_1 and starting of year_2 ; year_2 > year_1.
    """
    if year_1 != year_2:
        difference =  ((year_2 - year_1) // 4 ) + 365 * (year_2 - year_1) 
        if (year_2 - year_1) % 4 == 1 and  (year_1 % 4 == 0): 
            difference = difference + 1
        if (year_2 - year_1) % 4 == 2 and ((year_1 % 4 == 0) or ((year_1+1) % 4 == 0)):
            difference = difference + 1
        if (year_2 - year_1) % 4 == 3 and ((year_1 % 4 == 0) or ((year_1+1) % 4 == 0) or ((year_1+2) % 4 == 0)):
            difference = difference + 1

        #checking for non-leap centuries and subtracting it.

        for i in  range((year_2-year_1)//100 + 2):
            century = (year_1 // 100 + (i))* 100

            if not check_leap_year(century) and century < year_2 and century >= year_1:
                difference = difference - 1 

        return difference

    return 0

def check_leap_year(year:int):
    # returns True for leap year.
    if year % 400 == 0 or (year % 100 !=0 and year % 4 ==0 ):
        return True   
    else :
        return False

def timestamp_to_seconds(timestamp=None, gmt_diff=None):
    try:
        Hour, Min, Sec = map(int, timestamp.split(':'))
        total_sec = Hour * SECS_IN__AN_HOUR + Min * SECS_IN_A_MIN + Sec
        sign, gmt_diff_hour, gmt_diff_min =  gmt_diff[0], int(gmt_diff[1:3]), int(gmt_diff[3:])
        total_diff = gmt_diff_hour * SECS_IN__AN_HOUR + gmt_diff_min * SECS_IN_A_MIN
        if sign == '+':
            total_diff = 0 - total_diff
        
        return total_sec + total_diff
        print(timestamp)
    except Exception as e:
        print('error in timestamp_to_seconds function', str(e))

if __name__=="__main__":
    SECS_IN_A_DAY = 86400
    SECS_IN__AN_HOUR = 3600
    SECS_IN_A_MIN = 60

    answer_list = []
    Test_cases = int(input())

    for _ in range(Test_cases):
        (_ ,date, month, year, timestamp, gmt_diff) =  input().split()
        date_1 = (int(year), month, int(date), timestamp, gmt_diff)
        (_ ,date, month, year, timestamp, gmt_diff) =  input().split()
        date_2 = (int(year), month, int(date), timestamp, gmt_diff)

        date_1_total_sec = timestamp_to_seconds(date_1[3], date_1[4])
        date_2_total_sec = timestamp_to_seconds(date_2[3], date_2[4])

        # date_1 = (2014, 'January', 1) 
        # date_2 = (2013, 'January', 1)
        # date_3 = (2020, 'January', 1) 

        date_max, date_min = (date_1, date_2) if date_1[0] == max(date_1[0], date_2[0]) else (date_2, date_1)

        days_differnce_in_years = calculate_difference_in_days_between_years(date_min[0], date_max[0])

        difference_per_year  = calculate_difference_in_dates_per_year(date_min, date_max)

        total_days_difference  = days_differnce_in_years + difference_per_year
        total_days_difference_secs = total_days_difference * SECS_IN_A_DAY

        if (date_max == date_1):
            total_difference = (date_1_total_sec - date_2_total_sec) + total_days_difference_secs
        else:
            total_difference = (date_2_total_sec - date_1_total_sec) + total_days_difference_secs

        answer_list.append(abs(total_difference))

    for result in answer_list:
        print(result)
    # Test_cases = int(input())

    # for test_case in range(0, Test_cases):
    #     time_a , time_b = input(), input()
    #     print("First Timestamp :  " + str(time_a))
    #     print("Second Timestamp :  " + str(time_b))