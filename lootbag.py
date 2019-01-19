# You have an acquaintance whose job is to, once a year, delivery presents to the best kids around the world. They have a problem, though. There are so many good boys and girls in the world now, that their old paper accounting systems just don't cut it anymore. They want you to write a program that will let them do the following tasks.


import sqlite3
import sys

print(sys.argv)

lootbag_db = 'lootbag.db'

class Lootbag:
    """a class that holds methods that can return the information about the children who can receive gifts, what gifts they are receving, and when they can recieve them
 
    """
    
    def __init__(self, lootbag_db = 'lootbag.db'):
        self.lootbag_db = lootbag_db



    def getChildren(self):
        with sqlite3.connect(self.lootbag_db) as conn:
            cursor = conn.cursor()

            children = cursor.execute('SELECT * FROM children')
            children = cursor.fetchall()
            print(children)

    def getChild(self,child):
        with sqlite3.connect(self.lootbag_db) as conn:
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
        
    # addSuper() will be like addChild()  
    def addChild(self,child):
        """method that adds children

        Arguments:
            child {name} -- [name of the child]
            child {receiving} -- [is the kid able to receive gifts,true/false]
        """

        with sqlite3.connect(self.lootbag_db) as conn:
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


    def addGift(self,gift):
        """add gift to the gifts table
        
        Arguments:
            gift -- {
                "name": [name of toy],
                "child_name": [name of child]
            }
            
        """
        with sqlite3.connect(self.lootbag_db) as conn:
            cursor = conn.cursor()
            child_name = gift['child_name']
            try:
                cursor.execute(
                    f"""
                    INSERT INTO gifts
                    SELECT ?,?,?, childid
                    FROM children c
                    WHERE c.name = '{child_name}'
                    """, (None, gift['name'],0)
                )
            
            except sqlite3.OperationalError as err:
                print('oops', err)

    def removeGift(self,gift):
        """remove gift to the gifts table
        
        Arguments:
            
            "child_name": [name of child]  
        """
        with sqlite3.connect(self.lootbag_db) as conn:
            cursor = conn.cursor()
            # child_name = gift['child_name']
            gift_name = gift['gift_name']
            child_name = gift['child_name']
            try:
                cursor.execute(
                    f"""
                    DELETE FROM Gifts 
                    WHERE childid in (select c.childid from children c where c.name = '{child_name}')
                    and name = '{gift_name}'
                    """
                )
            
            except sqlite3.OperationalError as err:
                print('oops', err)

    def ls(self): 
        """print all the kids that are recieving presents
        
        """
        with sqlite3.connect(self.lootbag_db) as conn:
            cursor = conn.cursor()
            
            try:
                cursor.execute(
                    f"""
                    SELECT *
                    FROM children
                    WHERE receiving == 1
                    """
                )
                kid_list = cursor.fetchall()
                print("These are the kids receving gifts:", kid_list)
                return kid_list
            except sqlite3.OperationalError as err:
                print("oops", err)

    def ls_gift(self,child_name):
        """print gifts for a specific kid"""
        with sqlite3.connect(self.lootbag_db) as conn:
            cursor = conn.cursor()
        
            try:
                cursor.execute(
                    f"""
                    SELECT name
                    FROM gifts 
                    WHERE childid in (SELECT c.childid from Children c WHERE c.name = '{child_name}' and c.receiving = 1)
                    """
                )
                kid_list = cursor.fetchall()
                print("These are the gifts for the requested name:", kid_list)
                return kid_list
            except sqlite3.OperationalError as err:
                print("oops", err)
       

if __name__ == '__main__':
    # getChildren()
    # addChild({
    #     "name":"Lesley",
    #     "receiving":1
    # })
    # addGift({
    #     'name': 'car',
    #     'child_name': 'Lesley'
    # })

    
# ==================================================
# 1. Add a toy to the bag o' loot, and label it with the child's name who will receive it. The first argument must be the word add. The second argument is the gift to be delivered. The third argument is the name of the child.
# ==================================================

    if sys.argv[1] == 'add':
        Lootbag().addGift({
        'name': sys.argv[2],
        'child_name': sys.argv[3]  
        })


# ===================================================
# 2.Remove a toy from the bag o' loot in case a child's status changes before delivery starts.
# ==================================================
    elif sys.argv[1] == 'remove':
        Lootbag().removeGift({
        'child_name': sys.argv[2],
        'gift_name': sys.argv[3],
        })
    

# ===================================================
# 3. Produce a list of children currently receiving presents.
# ===================================================
    elif sys.argv[1] == 'ls':
        Lootbag().ls()

# ===================================================
# 4. List toys in the bag o' loot for a specific child.
# ===================================================
    elif sys.argv[1] == 'list':
        Lootbag().ls_gift(sys.argv[2])
    
    
# ===================================================
# The command below adds kids for testing 
# ===================================================
    elif sys.argv[1] == 'add_child':
        Lootbag().addChild({
            "name": sys.argv[2],
            "receiving": sys.argv[3]
        })
