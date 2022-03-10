import pandas as pd
import time

def csv_to_excel(file_name=None):
    try:
        dataframe = pd.read_csv(file_name)
        dataframe.to_excel('test01.xlsx')
    except Exception as e:
        print("error in csv_to_excel fn", str(e))

if __name__=="__main__":
    start = time.time()

    csv_to_excel(file_name='abc.csv')

    print("this took about ", str(round(time.time()-start, 2)))