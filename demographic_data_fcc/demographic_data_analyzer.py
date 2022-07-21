import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('./demographic_data_fcc/adult.data.csv')

    # print(df.head())

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.groupby(['race']).count().iloc[:, 1]
    race_count = race_count.reindex(['White', 'Black', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other'])
    # race_count.sort(reverse=True)
    
    # What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)
    # average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = df.groupby(['education']).count().loc['Bachelors'].iloc[0] / df.shape[0] * 100
    percentage_bachelors = percentage_bachelors.round(1)
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.groupby(['education']).count().iloc[:, 0].loc[['Bachelors', 'Doctorate', 'Masters']].sum()
    lower_education = df.shape[0] - higher_education

    # percentage with salary >50K
    higher_education_rich = df[df['salary'] == '>50K'].groupby(['education']).count().iloc[:, 0].loc[['Bachelors', 'Doctorate', 'Masters']].sum() / higher_education * 100
    higher_education_rich = higher_education_rich.round(1)

    non_higher_education_degrees = list(set(df[df['salary'] == '>50K'].groupby(['education']).count().index.to_list()) - set(['Bachelors', 'Doctorate', 'Masters'])  )
    lower_education_rich = df[df['salary'] == '>50K'].groupby(['education']).count().iloc[:, 0].loc[non_higher_education_degrees].sum() / lower_education * 100
    lower_education_rich = lower_education_rich.round(1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == df['hours-per-week'].min()]
    num_min_workers.round(1)

    rich_percentage = num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0] * 100 
    round(rich_percentage, 1)
    # What country has the highest percentage of people that earn >50K?
    df2 = pd.concat([df[df['salary'] == '>50K'].groupby(['native-country']).count().iloc[:, 1]], axis = 1)
    df2.columns = ['rich_population']
    df2['population_country_wise'] = df.groupby(['native-country']).count().iloc[:, 0]
    df2['percentage_rich'] = df2['rich_population'] / df2['population_country_wise'] * 100

    highest_earning_country = df2['percentage_rich'].idxmax()
    highest_earning_country_percentage = df2['percentage_rich'].max()
    highest_earning_country_percentage = highest_earning_country_percentage.round(1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')].groupby(['occupation']).count().iloc[:, 0].idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }


if __name__=="__main__":
    calculate_demographic_data(print_data=True)