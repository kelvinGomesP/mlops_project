import numpy as np
import pandas as pd
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
 
df = pd.read_csv(r'notebook\data\StudentsPerformance.csv')
print(df)

# CATEGORIAS UNICAS


'''
print("categorias em 'gender'", end=" ")
print(df['gender'].unique())

print("categorias em 'race/ethnicity'", end=" ")
print(df['race/ethnicity'].unique())

print("categorias em 'parental level of education'", end=" ")
print(df['parental level of education'].unique())

print("categorias em 'lunch'", end=" ")
print(df['lunch'].unique())

print("categorias em 'test preparation course'", end=" ")
print(df['test preparation course'].unique())
'''


# COLUNAS 'NUMERICAS' E ' CATEGORICAS'
'''
features_numericas = [feature for feature in df.columns if df[feature].dtype != 'O']
features_categoria = [feature for feature in df.columns in df[feature].dtype != 'O']

print('Temos {} feature numerica: {}'.format(len(features_numericas),features_numericas))
print('\nTemos {} features categoria: {}'.format(len(features_categoria), features_categoria))

'''

#total e media e numero max e min dos estudantes
'''
df['total score'] = df['math_score'] + df['reading_score'] + df['writing_score']
d['average'] = df['total score']/3
df.head()

reading_full = df[df['reading score'] == 100]['average'].count()
writing_full = df[df['writing score'] == 100]['average'].count()
math_full = df[df['math score'] == 100]['average'].count()

print(f'Numero de esudantes com nota max matematica: {math_full})
print(f'Numero de esudantes com nota max leitura{reading_full})
print(f'Numero de esudantes com nota max escrita{writing_full})


reading_less_20 = df[df['reading_score'] <= 20]['average'].count()
writing_less_20 = df[df['writing_score'] <= 20]['average'].count()
math_less_20 = dfr[df['math_score']<=20]['avarage'].count()


print(f'Numero de esudantes com nota menor que 20 matematica: {math_full})
print(f'Numero de esudantes com nota menor que 20 leitura{reading_full})
print(f'Numero de esudantes com nota menor que 20  escrita{writing_full})



'''
# HISTOGRAMA E KDE
