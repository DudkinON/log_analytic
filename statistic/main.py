#! /usr/bin/env python3
from statistic.db import get_top_articles, get_authors_top, get_errors
from datetime import datetime


def top_articles(amount):
    """Output top [amount] articles

    :param amount:
    :return void:
    """
    top_three_articles = get_top_articles(amount)
    print("\nThe most three most popular articles of all time are:")
    for title, views in top_three_articles:
        print('\tArticle title: "{}" - {} views'.format(title, views))


def top_authors():
    """Output top authors

    :return void:
    """
    authors = get_authors_top()
    print("\nThe most popular article authors of all time:")
    for author, views in authors:
        print('\tAuthor name: {} - {} views'.format(author, views))


def errors():
    """Output list of days where percent of errors more 1%

    :return void:
    """
    errors_list = get_errors()
    print("\nThe days when requests return more when 1 % errors:")
    for date, percent in errors_list:
        day = datetime.strptime(str(date), '%Y-%M-%d').strftime('%B %d, %Y')
        print('\tDay: {} - {}% errors'.format(day, percent))

if __name__ == '__main__':
    top_articles(amount=3)
    top_authors()
    errors()

