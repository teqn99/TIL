import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


df = pd.read_json('test.json')
df_a = df.iloc[:19]
df_b = df.iloc[19:]

df_final = pd.DataFrame()
newdata = {}
newdata = {'id': [], 'title': [],'genres': [], 'vote_average': []}
    
for i in range(len(df_b)):
    newdata['id'].append(df_b.iloc[i]['pk'])
    newdata['title'].append(df_b.iloc[i]['fields']['title'])
    genre_list = []
    for j in df_b.iloc[i]['fields']['genres']:
        for k in range(len(df_a)):
            if df_a.iloc[k]['pk'] == j:
                genre_list.append(df_a.iloc[k]['fields']['name'])
    newdata['genres'].append(" ".join(genre_list))
    newdata['vote_average'].append(df_b.iloc[i]['fields']['vote_average'])
df_new = pd.DataFrame(newdata)

count_vect = CountVectorizer(min_df=0, ngram_range=(1,3))
genre_mat = count_vect.fit_transform(df_new['genres'])
genre_sim = cosine_similarity(genre_mat, genre_mat)
genre_sim_sorted_ind = genre_sim.argsort()[:, ::-1]


def func(df, movie_title, top=10):
    # 특정 영화정보 뽑아내기 
    tmi = df[df['title'] == movie_title].index.values
    # 타겟 영화와 비슷한 코사인 유사도값
    sim_index = genre_sim_sorted_ind[tmi, :top].reshape(-1)
    # 본인 제외
    sim_index = sim_index[sim_index != tmi]
    # data frame으로 만들고 vote_count 값으로 정렬한 뒤 return
    result = df.iloc[sim_index].sort_values('vote_average', ascending=False)[:10]
    return result


# a = func(df_new, movie_title="올드보이")
# print(a)