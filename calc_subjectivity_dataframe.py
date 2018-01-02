#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys
from subjectivity import Sentiment

import pandas as pd
df = pd.read_json('datasets/essay_is300_combined.json')

# control_asnmt_1 = df[(df['Session'] == '2017 Spring') & (df['Phase'] == 'Assignment1') & (df['Group'] == 'Control')]
# control_asnmt_1 = list(control_asnmt_1['Q3'].values)
#
# expt_asnmt_1 = df[(df['Session'] == '2017 Spring') & (df['Phase'] == 'Assignment1') & (df['Group'] == 'Experiment')]
# expt_asnmt_1 = list(expt_asnmt_1['Q3'].values)
#
# control_asnmt_2 = df[(df['Session'] == '2017 Spring') & (df['Phase'] == 'Assignment2') & (df['Group'] == 'Control')]
# control_asnmt_2 = list(control_asnmt_2['Q3'].values)
#
# expt_asnmt_2 = df[(df['Session'] == '2017 Spring') & (df['Phase'] == 'Assignment2') & (df['Group'] == 'Experiment')]
# expt_asnmt_2 = list(expt_asnmt_2['Q3'].values)

# for sentence in [sent2, sent1]:
#     result = sentiment.analyze([sentence])
#     total = len(result['sentences'])
#     n_positive = result['results']['positive']['count']
#     n_negative = result['results']['negative']['count']
#     n_neutral = result['results']['neutral']['count']
#     subjectivity = float(n_positive + n_negative) / total
#     objectivity = float(n_neutral) / total
#     print subjectivity

i = 0

def calc_subjectivity(assignment, sentiment_instance):
    global i
    # print '################################################################################'
    print i
    result = sentiment_instance.analyze([assignment])
    # result = sentiment.analyze([assignment])
    total = len(result['sentences'])
    n_positive = result['results']['positive']['count']
    n_negative = result['results']['negative']['count']
    n_neutral = result['results']['neutral']['count']
    subjectivity = float(n_positive + n_negative) / total
    objectivity = float(n_neutral) / total
    i += 1
    # return (objectivity, subjectivity)
    return objectivity

from functools import partial
sentiment = Sentiment()
calc_subjectivity = partial(calc_subjectivity, sentiment_instance=sentiment)

# expt_asnmt_1_scores = [calc_subjectivity(assignment, sentiment) for assignment in expt_asnmt_1]
df['Objectivity'] = df['Q3'].apply(calc_subjectivity)

df.to_json('datasets/essay_is300_combined_objectivity.json', orient='records')
