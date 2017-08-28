#! /usr/bin/env python3
import psycopg2
from datetime import datetime

SETTINGS = {
    'db': 'udacity',
}


def get_data(sql):
    db = psycopg2.connect(database=SETTINGS['db'])
    c = db.cursor()
    c.execute(sql)
    result = c.fetchall()
    db.close()
    return result


def get_top_articles(amount=1):
    """Return top articles by amount

    :param amount:
    :return list:
    """
    sql = """SELECT articles.title, sum(top_articles.amount) AS amount 
                FROM top_articles, articles 
                WHERE top_articles.path 
                LIKE concat('%/article/%',articles.slug)
                GROUP BY articles.title 
                ORDER BY amount DESC
                LIMIT {};""".format(amount)
    return get_data(sql)


def get_authors_top():
    """Return top authors

    :return list:
    """
    sql = """SELECT authors.name, sum(top_articles.amount) AS amount
                FROM top_articles, articles, authors  
                WHERE top_articles.path 
                LIKE concat('%/article/%',articles.slug)
                AND authors.id = articles.author
                GROUP BY authors.name 
                ORDER BY amount DESC;"""
    return get_data(sql)


def get_errors():
    """Return list of errors more when one percent errors by day

    :return list:
    """
    sql = """SELECT request_list.day, 
        ROUND((error_list.errors/(request_list.requests/100))::DECIMAL, 2) 
        AS percent
        FROM request_list, error_list
        WHERE request_list.day = error_list.day
        AND (error_list.errors/(request_list.requests/100)) > 1
        ORDER BY percent DESC;"""
    return get_data(sql)


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
        day = datetime.strptime(str(date), '%Y-%m-%d')
        day = day.strftime('%B %d, %Y')
        print('\tDay: {} - {}% errors'.format(day, percent))


if __name__ == '__main__':
    top_articles(amount=3)
    top_authors()
    errors()
