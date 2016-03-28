#!/usr/bin/env python
import shelve
db=shelve.open("serverdb","r")
print(db.items())
