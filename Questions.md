Questions:
How to use from builtins import * or from future
       do I put that at the top then write in py2 or py3 or write in a mixture..?
    if you import futer into a py2 code can you run it in py2 and py3?

I do not understand how to prevent SQL INJECTION in dynamic queries.
  unsafe_query = '''SELECT * FROM users
                      WHERE name = {0}'''.format("'Erich'; DROP TABLE users;")
              ='''SELECT * FROM users
                      WHERE name = 'Erich'; DROP TABLE users;'''

  cur.execute('''SELECT * FROM users
                      WHERE name = %s''', ("'Erich'; DROP TABLE users;", ))


  wouldn't this equal
  cur.execute('''SELECT * FROM users
                      WHERE name = 'Erich'; DROP TABLE users;'''
  and result in the same problem? or does the execute command evaluate the string bening input as it gets inserted?

SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame
See the caveats in the documentation: http://pandas.pydata.org/pandas-docs/stable/indexing.html#indexing-view-versus-copy
