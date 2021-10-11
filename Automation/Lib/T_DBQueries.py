#!/usr/bin/python
class DB_INIT_QUERIES():
    def init_tables():
        nasdaq_table = "CREATE TABLE IF NOT EXISTS stocks_NASDAQ( "\
                +"symbol VARCHAR(100) NOT NULL PRIMARY KEY, "\
                +"name VARCHAR(1000), "\
                +"lastsale VARCHAR(100) , "\
                +"netchange VARCHAR(100) , "\
                +"pctchange VARCHAR(100) , "\
                +"volume VARCHAR(100) , "\
                +"marketCap VARCHAR(100) , "\
                +"country VARCHAR(100),  "\
                +"ipoyear VARCHAR(100),  "\
                +"industry VARCHAR(500),  "\
                +"sector VARCHAR(500),  "\
                +"url VARCHAR(500) ) "
        nyse_table = "CREATE TABLE IF NOT EXISTS stocks_NYSE ( "\
                +"symbol VARCHAR(100) NOT NULL PRIMARY KEY, "\
                +"name VARCHAR(1000), "\
                +"lastsale VARCHAR(100) , "\
                +"netchange VARCHAR(100) , "\
                +"pctchange VARCHAR(100) , "\
                +"volume VARCHAR(100) , "\
                +"marketCap VARCHAR(100) , "\
                +"country VARCHAR(100),  "\
                +"ipoyear VARCHAR(100),  "\
                +"industry VARCHAR(500),  "\
                +"sector VARCHAR(500),  "\
                +"url VARCHAR(500) ) "
        amex_table = "CREATE TABLE IF NOT EXISTS stocks_AMEX ( "\
                +"symbol VARCHAR(100) NOT NULL PRIMARY KEY, "\
                +"name VARCHAR(1000), "\
                +"lastsale VARCHAR(100) , "\
                +"netchange VARCHAR(100) , "\
                +"pctchange VARCHAR(100) , "\
                +"volume VARCHAR(100) , "\
                +"marketCap VARCHAR(100) , "\
                +"country VARCHAR(100),  "\
                +"ipoyear VARCHAR(100),  "\
                +"industry VARCHAR(500),  "\
                +"sector VARCHAR(500),  "\
                +"url VARCHAR(500) ) "