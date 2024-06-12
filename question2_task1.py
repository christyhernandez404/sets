#You are given a list of customer IDs, some of which are duplicated. 
#Write a Python function to remove duplicates and display the unique customer IDs.

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
#Steps
#wite a function
#must remove duplicates & display unique customer IDs = converting a list to a set will do both

def convert(alist):
    aset = set(alist)
    print(aset)

convert(customer_ids)
