# You have an acquaintance whose job is to, once a year, delivery presents to the best kids around the world. They have a problem, though. There are so many good boys and girls in the world now, that their old paper accounting systems just don't cut it anymore. They want you to write a program that will let them do the following tasks.

# 1.Add a toy to the bag o' loot, and label it with the child's name who will receive it. The first argument must be the word add. The second argument is the gift to be delivered. The third argument is the name of the child.

# python lootbag.py add kite suzy
# python lootbag.py add baseball michael

# addSuper() will be like addChild()
import sqlite3
import sys

lootbag_db = 'lootbag.db'

class Lootbag():
    
    
    def addChild():
        """method that adds children
        """

        with sqlite3.connect(lootbag_db) as conn:
            cursor = conn.cursor()