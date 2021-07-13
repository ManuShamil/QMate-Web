import mysql.connector

class Db:
    def __init__(self):
        self.con = mysql.connector.connect(host="db", user="root", password="qmate", db="q_mate")
        self.cur=self.con.cursor(dictionary=True)


    def selectone(self,q):
        self.con = mysql.connector.connect(host="db", user="root", password="qmate", db="q_mate")
        self.cur = self.con.cursor(dictionary=True)
        self.cur.execute(q)
        res=self.cur.fetchone()
        return res

    def selectall(self,qry):
        self.con = mysql.connector.connect(host="db", user="root", password="qmate", db="q_mate")
        self.cur = self.con.cursor(dictionary=True)
        self.cur.execute(qry)
        res = self.cur.fetchall()
        return res

    def insert(self,qry):
        self.con = mysql.connector.connect(host="db", user="root", password="qmate", db="q_mate")
        self.cur = self.con.cursor(dictionary=True)
        self.cur.execute(qry)
        id=self.cur.lastrowid
        self.con.commit()
        return id

    def update(self,qry):
        self.con = mysql.connector.connect(host="db", user="root", password="qmate", db="q_mate")
        self.cur = self.con.cursor(dictionary=True)
        self.cur.execute(qry)
        id=self.cur.lastrowid
        self.con.commit()
        return id

    def delete(self,qry):
        self.con = mysql.connector.connect(host="db", user="root", password="qmate", db="q_mate")
        self.cur = self.con.cursor(dictionary=True)
        self.cur.execute(qry)
        id=self.cur.lastrowid
        self.con.commit()
        return id
