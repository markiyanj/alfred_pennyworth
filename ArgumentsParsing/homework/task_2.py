import argparse

import pandas as pd
import time


def argument_parser():
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

    return args


def get_fav_beer_type(beer_review, show_max):
    fav_beer_type = beer_review.groupby(['beer_style'])['review_overall'].sum().sort_values()
    name = fav_beer_type.iloc[show_max].keys()[0]
    print(
        f'Based on the overall review favorite beer type is: {name} '
        f'with a total score from all reviewers {fav_beer_type[name]}', '\n')


def get_fav_beer_name(beer_review, show_max):
    fav_beer_name = beer_review.groupby(['beer_name'])['review_overall'].sum().sort_values()
    beer_name = fav_beer_name.iloc[show_max].keys()[0]
    print(
        f'Based on the overall review favorite beer name is: {beer_name} '
        f'with a total score from all reviewers {fav_beer_name[beer_name]}', '\n')


def get_most_review_day(beer_review, show_max):
    most_review_day = beer_review.groupby(['review_time'])['review_time'].count().sort_values()
    day = most_review_day.iloc[show_max].keys()[0]
    print(f'The day with the most reviews is: {time.ctime(day)} with {most_review_day[day]} reviews', '\n')


def get_reviewers_stats(beer_review):
    reviewers = beer_review.groupby(['review_profilename'])['review_profilename'].count().sort_values()
    i = 0
    print('Number of reviews for reviewer:')
    while True:
        try:
            name = reviewers.keys()[i]
            print(f'{name} - {reviewers[name]} reviews')
            i += 1
        except IndexError:
            break


if __name__ == '__main__':

    args = argument_parser()
    beer_review = pd.read_csv(args.path)
    show_max = [-1]
    try:
        if args.beer_type:
            get_fav_beer_type(beer_review, show_max)
        if args.beer_name:
            get_fav_beer_name(beer_review, show_max)
        if args.day_of_review:
            get_most_review_day(beer_review, show_max)
        if args.reviewer_stats:
            get_reviewers_stats(beer_review)
    except TypeError as e:
        print(e)
