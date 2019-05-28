import os, sys
import sqlite3

db_filename = 'test.db'
db_exists = not os.path.exists(db_filename)

if __name__ == '__main__':
    if len(sys.argv) is 2 :
        querytype = sys.argv[1]
        print(querytype)
        func_database_opne(querytype)
    else :
        print("not args")

#connection = sqlite3.connect(db_filename)
#SELECT COUNT(*) FROM "main"."hospital"
#SELECT "_rowid_",* FROM "main"."hospital" LIMIT 0, 49999;
#DELETE FROM "main"."hospital" WHERE _rowid_ IN ('3');
def func_database_opne(querytype):
    with sqlite3.connect (db_filename) as conn:
        if db_exists:
            print('Creating schema.')
            return conn
        else :
            print('DB already exists.')
            if(querytype == 'update'):
            else if (querytype == 'insert'):
            else if (querytype == 'delete'):
            else if (querytype == 'select'):
            else:

    conn.close()