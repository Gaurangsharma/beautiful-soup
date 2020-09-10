# import json
# import pandas as pd 
# import numpy as np
# from matplotlib import pyplot as plt
# from scipy.stats import norm
# import seaborn as sns

# def bar_graph(cuisine_name,dishes_count):
#    # salary data derived from https://datavizpyr.com/density-plots-with-pandas-in-python/
#     # stackoverflow_salary_file = "https://raw.githubusercontent.com/datavizpyr/data/master/SO_data_2019/2019_Stack_Overflow_Survey_Education_Salary_US.tsv"
#     # # load the salary data 
#     # print(stackoverflow_salary_file)
#     df=pd.DataFrame(
#     {
#     'Cusine':cuisine_name,
#     'No of Recipies':dishes_count,
#     })
#     # print(df)
#     # salary=df.to_csv(sep="\t")
#     # print(salary)
#     salary_wide=df.pivot(columns='Cusine',values='No of Recipies')
#     salary_wide.head()
#     print(salary_wide.head())
#     salary_wide.plot.hist(figsize=(8,6),xlim=(0,80),linewidth=10,fontsize=6)
#     plt.xlabel("Recipe Size") 
#     plt.ylabel("No. of Recipe") 
#     plt.title("Cusine Details")
#     plt.show()
#     # plt.savefig("multiple_density_plots_with_Pandas_Python.jpg")

# f=open('train.json')
# data=json.load(f)
# cuisine_name, dishes_count=[],[]
# for i in range(len(data)):
#     cuisine_name.append(data[i]['cuisine'])
#     dishes_count.append(len(data[i]['ingredients']))
# bar_graph(cuisine_name,dishes_count)





    
