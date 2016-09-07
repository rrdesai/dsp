# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists and Tuples are both ordered sequences of objects. From a technical standpoint, tuples are immutable which means they cannot be altered after they are created while lists can have elements removed and changed. From a usage standpoint tuples are generally used when the objects stored are of different types and must be treated as a unit to be useful (ie latitude, longitude) which is to say position has semantic value. In comparison lists are used when the objects stored are of the same type (ie names).  
Tuples will work as keys in a dictionary because they are immutable.  

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are both data structures but lists are ordered while sets are not. Additonally, items in a set must be unique while lists may contain duplicate entries. When finding an element sets will return a result much faster since sets are implemented using hash tables which performs a key/value lookup when trying to locate an element. 

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> lambda allows the user to define (simple) functions on the fly without having to formally declare them. an example would be mod_11 = lambda x: x%11. This could then be used in a sort: sorted([123,456,789,101,112,131,415], key = lambda x: x%11) which would return the list sorted not by the numbers themselves but rather by their remainders when divided by 11 since they would be run through the lambda operation. 

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> comprehensions allow for the construction of lists/sets/dicts based on a set of rules. map and filter can be combined with other methods to have identical results but for simple constructions 

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937 days  

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





