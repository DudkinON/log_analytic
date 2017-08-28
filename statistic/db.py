import psycopg2

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
                WHERE top_articles.path LIKE concat('%/article/%',articles.slug)
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
                WHERE top_articles.path LIKE concat('%/article/%',articles.slug)
                AND authors.id = articles.author
                GROUP BY authors.name 
                ORDER BY amount DESC;"""
    return get_data(sql)


def get_errors():
    """Return list of errors more when one percent errors by day

    :return list:
    """
    sql = """SELECT request_list.day, ROUND((error_list.errors/(request_list.requests/100))::DECIMAL, 2) AS percent
                FROM request_list, error_list
                WHERE request_list.day = error_list.day
                AND (error_list.errors/(request_list.requests/100)) > 1
                ORDER BY percent DESC;"""
    return get_data(sql)
