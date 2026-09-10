import mysql.connector
from flask import current_app


def get_db():
    return mysql.connector.connect(
        **current_app.config['DB_CONFIG']
    )


def fetch_one(q, p=()):
    c = get_db()
    cur = c.cursor(dictionary=True)

    try:
        cur.execute(q, p)
        return cur.fetchone()
    finally:
        cur.close()
        c.close()


def fetch_all(q, p=()):
    c = get_db()
    cur = c.cursor(dictionary=True)

    try:
        cur.execute(q, p)
        return cur.fetchall()
    finally:
        cur.close()
        c.close()


def execute(q, p=()):
    c = get_db()
    cur = c.cursor()

    try:
        cur.execute(q, p)
        c.commit()
        return cur.lastrowid
    except Exception:
        c.rollback()
        raise
    finally:
        cur.close()
        c.close()