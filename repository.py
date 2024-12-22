import sqlite3
from create_db_from_schema import create_db
from type import *

def dict_factory(cursor, row):
   row_dict = {}
   for index, column in enumerate(cursor.description):
       row_dict[column[0]] = row[index]
   return row_dict

conn = sqlite3.connect('./db/recipe.db')
conn.row_factory = dict_factory


# dbの疎通確認に使った
# create_db(conn)

cur = conn.cursor()

def fetch_all_recipe():
    cur.execute('SELECT id, title, making_time, serves, ingredients, cost from recipes')
    return cur.fetchall()

def fetch_specific_recipe(recipe_id):
    cur.execute('SELECT id, title, making_time, serves, ingredients, cost from recipes where id = ?', [recipe_id])
    return cur.fetchone()

def register_recipe(recipe):
    cur.execute('INSERT into recipes (title, making_time, serves, ingredients, cost) values (?,?,?,?,?)', [recipe.title, recipe.making_time, recipe.serves, recipe.ingredients, recipe.cost])
    conn.commit()

    cur.execute('SELECT * from recipes ORDER BY created_at DESC LIMIT 1')
    return cur.fetchone()

def update_recipe(recipe_id, recipe):
    cur.execute('UPDATE recipes set title=?, making_time=?, serves=?, ingredients=?, cost=? WHERE id=?', [recipe.title, recipe.making_time, recipe.serves, recipe.ingredients, recipe.cost,recipe_id])
    conn.commit()

    cur.execute('SELECT * from recipes WHERE id=?', [recipe_id])
    return cur.fetchone()

def delete_recipe(recipe_id):
    cur.execute('SELECT * from recipes WHERE id=?', [recipe_id])
    if cur.fetchone == None:
        return False

    cur.execute('DELETE from recipes WHERE id=?', [recipe_id])
    conn.commit()
    return True
