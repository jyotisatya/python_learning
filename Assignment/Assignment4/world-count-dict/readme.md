### two way to loop a dictionary :

```python
# mirchi no 1
for book in iit_syllabus:
    print("key", book)
    print("value", iit_syllabus[book])
    print("\n--------------")


print(" \n\n#############################\n\n" )

# mirchi no 2
for book, object in iit_syllabus.items():
    print("key", book)
    print("value", object)
    print("\n--------------")

```    