import sqlite3
from PIL import Image
import os
path = os.getcwd()
path = os.path.splitdrive(path)
p = ''
for i in path:
    p+= i.replace("\\","/")
print(p)


def l(m):
    l = ()
    k = ''
    for i in m:
        l = i
    for i in l:
        k = i
    return k
#список кортежей покемошек
def list_pokemon():
    con = sqlite3.connect('Db_Pokemon.db')
    cur = con.cursor()
    cur.execute('SELECT name From Pokemon')
    return cur.fetchall()



#Основная функция для работы с бд и таблицей
def ev(name):
    new = ''
    con = sqlite3.connect('Db_Pokemon.db')
    cur = con.cursor()
    t = (name,)
    cur.execute('SELECT evolution From Pokemon Where name=?',t)
    a = l(cur.fetchall())
#если все пусто в итогом выводеииз таблице значит такого покемона нет 
    if a == '':
        return ['We do not have this pokemon']
    if name == 'Eevee' or  a == 'Eevee':
        t = ('Eevee',)
        p = []
        m = [['Eevee'],['Eevee'],['Eevee']]
        cur.execute('SELECT name From Pokemon Where evolution=?',t)
        a = cur.fetchall()
        for i in a:
            for j in i:
                p.append(j)
        
        for i in range(len(m)):
            m[i].append(p[i])
        return m
                  
        #m = [name]
        
    if a == 'Egg':
    # так смотрим до тех пор пока еволюция не будет
    
        cur.execute('SELECT name From Pokemon Where evolution=?',t)
        a = l(cur.fetchall())
        m = [name]
        while True:
            cur.execute('SELECT name From Pokemon Where evolution=?',t)
            a = l(cur.fetchall())
            t = (a,)
            if a!= '':
                m.append(a)
            else:
                break
        return m
    if a == '-':
        return [name]
            
    else:
        while True:
            cur.execute('SELECT evolution From Pokemon Where name=?',t)
            a = l(cur.fetchall())
            t = (a,)
            cur.execute('SELECT evolution From Pokemon Where name=?',t)
            b = l(cur.fetchall())
            if b =='Egg':
                new = a
                break
        return ev(new)
def id_p(pokemon):
    id_n = []
    con = sqlite3.connect('Db_Pokemon.db')
    cur = con.cursor()
    a = l(cur.fetchall())
    if ['Eevee', 'Vaporeon'] in pokemon  :
        return [['133','134'],['133','135'],['133','136']]
    for i in pokemon:
        t = (i,)
        cur.execute('SELECT id From Pokemon Where name=?',t)
        a = l(cur.fetchall())
        id_n.append(a)
    return id_n
def spl(pic):
    for i in pic:
        spliting(i)
def spliting(pic):
    if ['133','134'] in pic:
        spl(pic)
        return
    try:  
        p = 0
        z = 0
        x = 0
        path = './Pokemon/'
        for i in pic:
            im1 = Image.open(path+i+'.bmp')
            x,y = im1.size
            p += y
        im = Image.new('RGB', (x, p))
        for i in pic:
            im1 = Image.open(path+i+'.bmp')
            x,y = im1.size
            im.paste(im1, (0,z))
            z+= y
        im.show()
    except:
        print('We do not have this pokemon')
        

        
def all():
    t = ev('Nidor')
    print(t)
    y = id_p(t)
    print(y)
    spliting(y)


    
all()
                         
            
                
        
            
            
            
            
            
        
        
            
            
        
