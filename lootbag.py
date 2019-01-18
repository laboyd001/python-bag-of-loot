# You have an acquaintance whose job is to, once a year, delivery presents to the best kids around the world. They have a problem, though. There are so many good boys and girls in the world now, that their old paper accounting systems just don't cut it anymore. They want you to write a program that will let them do the following tasks.

# 1.Add a toy to the bag o' loot, and label it with the child's name who will receive it. The first argument must be the word add. The second argument is the gift to be delivered. The third argument is the name of the child.

# python lootbag.py add kite suzy
# python lootbag.py add baseball michael

# addSuper() will be like addChild()
import sqlite3
import sys

lootbag_db = 'lootbag.db'

def getChildren():
    with sqlite3.connect(lootbag_db) as conn:
        cursor = conn.cursor()

        children = cursor.execute('SELECT * FROM children')
        children = cursor.fetchall()
        print(children)

def getChild(child):
    with sqlite3.connect(lootbag_db) as conn:
        cursor = conn.cursor()

        cursor.execute(f'''SELECT c.*, gift.name
                           FROM children c
                           JOIN gifts g
                           ON c.childid = g.childid
                           WHERE c.name = '{child}'
                           '''
                       )

        child = cursor.fetchone()
        print(child)
        return child
    
    
def addChild(child):
    """method that adds children
    """

    with sqlite3.connect(lootbag_db) as conn:
        cursor = conn.cursor()

        try:
            cursor.execute(
                '''
                INSERT INTO children
                Values(?,?,?)
                ''', (None, child['name'], child['receiving'])
            )
        except sqlite3.OperationalError as err:
            print('oops', err)

if __name__ == '__main__':
    # getChildren()
    addChild({
        "name":"Lesley",
        "receiving":1
    })
