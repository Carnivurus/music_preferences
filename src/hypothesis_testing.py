import pandas as pd 
from scipy.stats import levene, ttest_ind

def ttest(time1,time2, df1, df2,day):
    shelbyville_data = df1[df1['time'].between(time1,time2)&(df1['day']==day)]
    springfield_data = df2[df2['time'].between(time1,time2)&(df2['day']==day)]

    df1 = pd.pivot_table(data=shelbyville_data , index='genre', values='track', aggfunc='count')
    df2 = pd.pivot_table(data=springfield_data , index='genre', values='track', aggfunc='count')

    # Creating a common index
    all_genres = df1.index.union(df2.index)

    shelbyville_reindexed = df1.reindex(all_genres, fill_value=0)
    spring_reindexed = df2.reindex(all_genres, fill_value=0)
    
    t_stat, p_value = ttest_ind(shelbyville_reindexed, spring_reindexed, equal_var=False)

    alpha = 0.05

    if p_value < alpha:
        print('Null hypothesis reject')
    else:
        print('Cannot reject null hypothesis')

    return p_value

def test_hypothesis_one(data):
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

    print('------------------------------------')
    print('Hypothesis one')
    print('H0 = There are not differences in the way users in Springfield and Shelbyville consume music')
    # Perform test
    for day in (['Monday', 'Wednesday', 'Friday']):
        #levene to verify if deviation is normal
        stat, p_value = levene(springfield_data[day], shelbyville_data[day])
        alpha = 0.05
        # print('------------------')
        # print(f'{day} , levene test')
        if p_value <= alpha:
            # print('Variances are significantly different')
            status = False
        else:
            # print('Cannot reject variances are equal')
            status = True

        #t-test
        t_stat, p_value = ttest_ind(springfield_data[day], shelbyville_data[day], equal_var=status)
        t_test_results[day] = {
            't_stat': t_stat,
            'p_value': p_value
        }

        # Evaluating hypothesis
        alpha = 0.05
        print('------------------')
        print(f'{day} comparison hypothesis')
        if p_value < alpha:
            print('Null hypothesis rejected')
        else:
            print('Cannot reject null hypothesis')
    # return pivot_table, t_test_results

def test_hypothesis_two(data):
    '''
    Hypothesis 2: Music at the Beginning and End of the Week
    According to the second hypothesis, on Monday mornings (7 to 11 hrs) and Friday nights (17 to 23 hrs),
    Springfield residents listen to genres different from those enjoyed by Shelbyville users.'''

    dt1 = pd.to_datetime('07:00:00', format='%H:%M:%S')
    dt2 = pd.to_datetime('11:00:00', format='%H:%M:%S')
    dt3 = pd.to_datetime('17:00:00', format='%H:%M:%S')
    dt4 = pd.to_datetime('23:00:00', format='%H:%M:%S')

    shelbyville_df = data[data['city']=='Shelbyville']
    springfield_df = data[data['city']=='Springfield']
    

    print('------------------------------------')
    print('Hypothesis two')
    print('H0 = Monday mornings (7 to 11 hrs) Springfield residents listen to the same genres than Shelbyville users')

    morning = ttest(dt1,dt2,shelbyville_df,springfield_df,'Monday')

    print('------------------')
    print('H0 = Friday nights (17 to 23 hrs) Springfield residents listen to the same genres than Shelbyville users')
    afternoon = ttest(dt3,dt4,shelbyville_df,springfield_df,'Friday')

    return 

def test_hypothesis_three(data):
    '''Hypothesis 3: Gender Preferences in Springfield and Shelbyville
    Hypothesis: Shelbyville loves rap music. Springfield residents prefer pop music.'''

    shelbyville_df = data[data['city']=='Shelbyville']
    springfield_df = data[data['city']=='Springfield']

    shelbyville_genre = shelbyville_df['genre'].value_counts().head(1)
    springfield_genre = springfield_df['genre'].value_counts().head(1)
    
    print('------------------------------------')
    print('Hypothesis three')
    
    if shelbyville_genre.index == 'rap':
        print('The favorite genre for Shelbyville is rap')
    else:
        print('The favorite genre for Shelbyville is NOT rap')

    if springfield_genre.index == 'pop':
        print('The favorite genre for Springfield is pop')
    else:
        print('The favorite genre for Shelbyville is NOT pop')

    # if shelbyville_genre == ''
