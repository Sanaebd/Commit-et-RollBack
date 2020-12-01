#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=.;'
                      'Database=WideWorldImporters;'
                      'Trusted_Connection=yes;')

avant_modif = "select CustomerID, CustomerName from WideWorldImporters.Sales.Customers where CustomerID= 27"
try:
    conn.autocommit = False
    cursor = conn.cursor()
    apres_modif = "update WideWorldImporters.Sales.Customers set CustomerName = 'Sanae BADAD'where CustomerID= 27"
    cursor.execute(apres_modif)
    conn.commit()
    print('commited')

except Exception:
    conn.rolback()
    print('rolback')
    
finally:
    cursor.execute(avant_modif)
    for r in cursor.fetchall():
            print(r)
    cursor.close()
    conn.close()
    print('Connexion is closed')
        
        
    
    
    


# In[ ]:





# In[ ]:




