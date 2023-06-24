#                         OPERATION ON SET 

#      WITH other  sets 
# Intersection
set_intersection = {1, 2, 3, 4, 5}.intersection({3, 4, 5, 6}) # {3, 4, 5}
set_intersection_1 = {1, 2, 3, 4, 5} & {3, 4, 5, 6} # {3, 4, 5}
print("the intersection is: ", set_intersection)
# Union
set_union = {1, 2, 3, 4, 5}.union({3, 4, 5, 6}) # {1, 2, 3, 4, 5, 6}
set_union_1 = {1, 2, 3, 4, 5} | {3, 4, 5, 6} # {1, 2, 3, 4, 5, 6}
print("The Union is: ", set_union)

# Difference
set_difference = {1, 2, 3, 4}.difference({2, 3, 5}) # {1, 4}
set_difference_1 = {1, 2, 3, 4} - {2, 3, 5} # {1, 4}
print("The difference is: ", set_difference)

# Symmetric difference with
{1, 2, 3, 4}.symmetric_difference({2, 3, 5}) # {1, 4, 5}
{1, 2, 3, 4} ^ {2, 3, 5} # {1, 4, 5}

# Superset check
{1, 2}.issuperset({1, 2, 3}) # False
set_superset = {1, 2} >= {1, 2, 3} # False
print(set_superset)
# Subset check

set_subset = {1, 2}.issubset({1, 2, 3}) # True
{1, 2} <= {1, 2, 3} # True
print(set_subset)

# Disjoint check
set_disjoint = {1, 2}.isdisjoint({3, 4}) # True
{1, 2}.isdisjoint({1, 4}) # False
print(set_disjoint)


#       WITH single  sets 

print(" Operation on sets WITH single  sets") 
set_2 = {2,4,6,8,9}

# Existence check
print(2 in set_2)
print(3 not in set_2)

#  add and remove
s = {1,3,5,7}
print( s.add(9))
print( s.discard(1))
print( s.remove(3))
print( s.update({0,9,8}))

