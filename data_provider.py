# -*- coding: utf-8 -*-
import mysql.connector


class Service:

    def __init__(self):
        self.mydb = mysql.connector.connect(host="127.0.0.1",
                                            user="root",
                                            passwd="root",
                                            port="3306",
                                            database="phone_book",
                                            )

    def delete_contact(self, user_id, name, phone_number, birth_date):
        sql = "DELETE FROM contact WHERE user_id = %s and name = %s and phone_number = %s and birth_date = %s"
        val = (str(user_id), unicode(name), str(phone_number), str(birth_date))
        mycursor = self.mydb.cursor()
        mycursor.execute(sql, val)
        self.mydb.commit()

    def put_contact(self, user_id, name, phone_number, birth_date, old_name, old_phone_number, old_birth_date):
        sql = "SELECT * FROM contact WHERE user_id = %s and name = %s and phone_number = %s and birth_date = %s"
        val = (str(user_id), unicode(name), str(phone_number), str(birth_date))
        mycursor = self.mydb.cursor()
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        if not myresult:
            sql = "UPDATE contact SET name = %s, phone_number = %s, birth_date = %s WHERE user_id = %s and name = %s and phone_number = %s and birth_date = %s"
            val = (
            unicode(name), str(phone_number), str(birth_date), str(user_id), unicode(old_name), str(old_phone_number),
            str(old_birth_date))
            mycursor = self.mydb.cursor()
            mycursor.execute(sql, val)
            self.mydb.commit()
            return 0
        else:
            return 1

    def get_contacts(self, user_id):
        sql = "SELECT name, phone_number, birth_date FROM contact WHERE user_id = %s"
        mycursor = self.mydb.cursor()
        val = (unicode(user_id),)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        return myresult

    def post_contact(self, user_id, name, phone_number, birth_date):
        sql = "SELECT * FROM contact WHERE user_id = %s and name = %s and phone_number = %s and birth_date = %s"
        val = (str(user_id), unicode(name), str(phone_number), str(birth_date))
        mycursor = self.mydb.cursor()
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        if not myresult:
            sql = "INSERT INTO contact (user_id, name, phone_number, birth_date) VALUES (%s, %s, %s, %s)"
            val = (str(user_id), unicode(name), str(phone_number), str(birth_date))
            mycursor.execute(sql, val)
            self.mydb.commit()
            return 0
        else:
            return 1

    def post_user(self, login, password, email, birth_date):
        sql = "INSERT INTO user (login, password, email, birth_date) VALUES (%s, %s, %s, %s)"
        mycursor = self.mydb.cursor()
        val = (unicode(login), unicode(password), unicode(email), unicode(birth_date))
        mycursor.execute(sql, val)
        self.mydb.commit()
        return 0

    def get_email(self, email):
        sql = "SELECT * FROM user WHERE email = %s"
        mycursor = self.mydb.cursor()
        val = (unicode(email),)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        return myresult

    def get_login(self, login):
        sql = "SELECT * FROM user WHERE login = %s"
        mycursor = self.mydb.cursor()
        val = (unicode(login),)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        return myresult

    def get_user(self, login, password):
        sql = "SELECT * FROM user WHERE login = %s and password = %s"
        mycursor = self.mydb.cursor()
        val = (unicode(login), unicode(password))
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        return myresult

    def set_remember(self, login, password):
        sql = "INSERT INTO remember (login, password) VALUES (%s, %s)"
        mycursor = self.mydb.cursor()
        val = (unicode(login), unicode(password))
        mycursor.execute(sql, val)
        self.mydb.commit()
        return 0

    def delete_remember(self):
        sql = "TRUNCATE TABLE remember"
        mycursor = self.mydb.cursor()
        mycursor.execute(sql)

    def get_remember(self):
        sql = "SELECT login, password FROM remember"
        mycursor = self.mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult

    def get_all(self):
        sql = "SELECT author, quote FROM quotes"
        mycursor = self.mydb.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        return myresult
