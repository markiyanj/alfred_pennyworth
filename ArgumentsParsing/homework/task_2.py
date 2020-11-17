import argparse

import pandas as pd

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--path",
                        required=True,
                        dest="path",
                        help="path to source file")
    parser.add_argument("-bt", "--beer_type",
                        required=False,
                        dest="beer_type",
                        help="find most favorite beer type",
                        action='store_true')
    parser.add_argument("-bn", "--beer_name",
                        required=False,
                        dest="beer_name",
                        help="find most favorite beer name",
                        action='store_true')
    parser.add_argument("-day", "--day_of_review",
                        required=False,
                        dest="day_of_review",
                        help="find day with they most number of review;(based on review_time)",
                        action='store_true')
    parser.add_argument("-rs", "--review_status",
                        required=False,
                        dest="reviewer_stats",
                        help="Show number of reviews for reviewer",
                        action='store_true')
    args = parser.parse_args()

    path = args.path

    beer_review = pd.read_csv(path)
    show_max = [-1]
    if args.beer_type:
        fav_beer_type = beer_review.groupby(['beer_style'])['review_overall'].agg(['sum']).sort_values(by='sum')
        print('Based on the overall review favorite beer type is:')
        print(fav_beer_type.iloc[show_max])
    if args.beer_name:
        fav_beer_name = beer_review.groupby(['beer_name'])['review_overall'].agg(['sum']).sort_values(by='sum')
        print('Based on the overall review favorite beer name is:')
        print(fav_beer_name.iloc[show_max])
    if args.day_of_review:
        most_review_day = beer_review.groupby(['review_time'])['review_time'].agg(['count']).sort_values(by='count')
        print('The day with the most reviews is:  ')
        print(most_review_day.iloc[show_max])
    if args.reviewer_stats:
        reviewers =  beer_review.groupby(['review_profilename'])['review_profilename'].agg(['count']).sort_values(by='count')
        print('Number of reviews for reviewer:')
        print(reviewers)