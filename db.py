
import sqlite3 as lite 
import sys


con = lite.connect('D:\Python\Db_Pokemon.db')
f_n = open('D:\Python\Pokemon.txt')
n = [line.strip() for line in f_n]
f_p = open('D:\Python\Pokemon1.txt')
p = [line.strip() for line in f_p]
f_e = open('D:\Python\Pokemon2.txt')
e = [line.strip() for line in f_e]

pokemons = tuple(zip(n,p,e))

with con:
    cur = con.cursor()    
    cur.executemany("INSERT INTO Pokemon VALUES(?, ?, ?)", pokemons)
