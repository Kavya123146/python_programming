#list comprehension
given_list=[x for x in range(5)]
print(given_list)
new_list=[var+3 for var in given_list]
print(new_list)
#Dict
given_list=[x for x in range(5)]
print(given_list)
new_list={var:var+3 for var in given_list}#
print(new_list)
#set
given_list={x for x in range(5)}
print(given_list)
new_list={var+3 for var in given_list}
print(new_list)
