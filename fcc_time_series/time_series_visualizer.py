import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
from datetime import datetime

from matplotlib.patches import Patch

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(r'./fcc_time_series/fcc-forum-pageviews.csv',
                 parse_dates=['date'])

df.set_index(df['date'], inplace=True)
# Clean data

df = df[(df['value'] >= df['value'].quantile(0.025))
        & (df['value'] <= df['value'].quantile(0.975))]
# df.set_index(df['date'], inplace=True)


def gen_year_month(df=None, width = 0.02):
    try:
        month_list = [
            'January', 'February', 'March', 'April', 'May', 'June', 'July',
            'August', 'September', 'October', 'November', 'December'
        ]
        color_map = {'January': 'tab:blue', 'February': 'tab:orange', 'March': 'tab:green',
         'April': 'tab:red', 'May': 'tab:purple', 'June': 'tab:brown', 'July': 'tab:pink',
          'August': 'tab:grey', 'September' : 'tab:olive', 'October': 'tab:cyan',
           'November': 'tab:blue', 'December': 'tab:orange'}
        x_pos = []
        y_pos = []
        color_list = []

        year_list = list(set(df.index.get_level_values(0)))
        year_list.sort(key = lambda x: int(x))
        for year in year_list:
            months = list(df[str(year)].index)
            months.sort(key = lambda x: month_list.index(x))

            for month in months:
                if month_list.index(month) > 5:
                    x_val = int(year) + (month_list.index(month) % 6 + 1/2)*width
                else:
                    x_val = int(year) + (month_list.index(month) % 6 - 5 - 1/2)*width
                    
                y_val = df[year, month]
                x_pos.append(x_val)
                y_pos.append(y_val)
                color_list.append(color_map.get(month))

                # print(str(x_val) + '---' + str(y_val))

        return (x_pos, y_pos, color_list)
    
    except Exception as e:
        print("Error in gen_year_month fn", str(e))

def draw_line_plot():
    df_copy = df
    # Draw line plot
    figure = plt.figure(figsize=(15, 5))
    plt.plot(df_copy.index, df_copy['value'], color='red')
    plt.xticks(ticks=[
        '2016-07-01', '2017-01-01', '2017-07-01', '2018-01-01', '2018-07-01',
        '2019-01-01', '2019-07-01', '2020-01-01'
    ],
               labels=[
                   '2016-07', '2017-01', '2017-07', '2018-01', '2018-07',
                   '2019-01', '2019-07', '2020-01'
               ])
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    fig = figure.figure

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png', dpi=250)
    return fig


# def draw_bar_plot():
#     # Copy and modify data for monthly bar plot
#     df_bar = df
#     df_bar['year'] = df_bar['date'].apply(lambda x: x.strftime('%Y'))
#     df_bar['month'] = df_bar['date'].apply(lambda x: x.strftime('%B'))

#     df_grouped = df_bar.groupby(['year', 'month'])['value'].mean()

#     bar_width = 0.04
#     x_pos, y_pos, color_list = gen_year_month(df_grouped, bar_width)

#     legend_elements = [Patch(facecolor='tab:blue', label='January'),Patch(facecolor='tab:orange', label='February'),Patch(facecolor='tab:green', label='March'),
#         Patch(facecolor='tab:red', label='April'),Patch(facecolor='tab:purple', label='May'),Patch(facecolor='tab:brown', label='June'),
#         Patch(facecolor='tab:pink',label='July'),Patch(facecolor='tab:grey', label='August'),Patch(facecolor='tab:olive', label='September'),
#         Patch(facecolor='tab:cyan', label='October'),Patch(facecolor='tab:blue', label='November'),Patch(facecolor='tab:orange', label='December')]
    
    
#     fig, ax = plt.subplots(figsize=(10, 8))


#     ax.bar(x_pos, y_pos,
#             width=bar_width, color = color_list)
#     plt.figure(figsize=(10, 8))
#     ax.set_xlabel('Years')
#     ax.set_ylabel('Average Page Views')
#     ax.set_xticks(ticks = [2016, 2017, 2018, 2019])
#     ax.set_xticklabels(labels = [2016, 2017, 2018, 2019], fontdict= {'rotation':90})
#     ax.legend(handles=legend_elements, title='Months')
    
#     # print('yo')

#     # Draw bar plot

#     # Save image and return fig (don't change this part)
#     fig.savefig('bar_plot.png')
#     return fig

#copied from Internet
def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["Years"] = df_bar.index.year
    df_bar["Months"] = df_bar.index.month_name()
    df_bar = pd.DataFrame(df_bar.groupby(["Years", "Months"], sort=False)["value"].mean().round().astype(int))
    df_bar = df_bar.rename(columns={"value": "Average Page Views"})
    df_bar = df_bar.reset_index()
    missing_data = {
        "Years": [2016, 2016, 2016, 2016],
        "Months": ['January', 'February', 'March', 'April'],
        "Average Page Views": [0, 0, 0, 0]
    }

    df_bar = pd.concat([pd.DataFrame(missing_data), df_bar])

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(19.2, 10.8), dpi=100)
    ax.set_title("Daily freeCodeCamp Forum Average Page Views per Month")

    chart = sns.barplot(data=df_bar, x="Years", y="Average Page Views", hue="Months", palette="tab10")
    chart.set_xticklabels(chart.get_xticklabels(), rotation=90, horizontalalignment='center')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    # df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    months_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
                    'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    fig, axs = plt.subplots(ncols=2, figsize=(18,6), dpi=200)
    sns.boxplot(x=df_box['year'], y=df_box['value'],linewidth=0.5,fliersize=1, ax=axs[0])
    sns.boxplot(x=df_box['month'], y=df_box['value'],order=months_list,linewidth=0.5,fliersize=1 ,ax=axs[1])
    axs[0].set_xlabel('Year')
    axs[0].set_ylabel('Page Views')
    axs[0].set_title('Year-wise Box Plot (Trend)')
    axs[1].set_xlabel('Month')
    axs[1].set_ylabel('Page Views')
    axs[1].set_title('Month-wise Box Plot (Seasonality)')
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig


if __name__ == '__main__':
    # draw_line_plot()
    draw_bar_plot()
    # draw_box_plot()
