import pandas as pd 
from scipy.stats import ttest_ind


def test_hypotheses_one(data):

    '''Hypothesis 1: Compare User Behavior in the Two Cities
    The first hypothesis states that there are differences in the way users in Springfield and Shelbyville consume music.
    -To verify this, use data from three days of the week: Monday, Wednesday, and Friday.Group the users by city. 
    -Compare the number of songs that each group played on Monday, Wednesday, and Friday.'''

    pivot_table = pd.pivot_table(data,values='track',index='city', columns='day', aggfunc='count')
    pivot_table = pivot_table[['Monday','Wednesday','Friday']]
    # print(pivot_table)

    filtered_data = data[data['day'].isin(['Monday', 'Wednesday', 'Friday'])]
    t_test_results= {}


    shelbyville_df = data[data['city']=='Shelbyville']
    shelbyville_data= pd.pivot_table(data=shelbyville_df, index='artist', columns='day', values='track', aggfunc='count', fill_value=0 )
    # shelbyville_data =  shelbyville_df.groupby(['artist','day']).size()

    springfield_df = data[data['city']=='Springfield']
    springfield_data =  pd.pivot_table(data=springfield_df, index='artist', columns='day', values='track', aggfunc='count', fill_value=0 )
         
    # Perform t-test
    for day in (['Monday', 'Wednesday', 'Friday']):
        t_stat, p_value = ttest_ind(springfield_data[day], shelbyville_data[day])

        t_test_results[day] = {
            't_stat': t_stat,
            'p_value': p_value
        }

        # Evaluating hypothesis
        alpha = 0.05

        if p_value <= alpha:
            print('Null hypothesis reject')
        else:
            print('Cannot reject null hypothesis')

    return pivot_table, t_test_results


    