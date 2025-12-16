l = [45, 23, 67, 89, 23, 45, 12, 78, 34, 56, 89, 23, 90, 11, 67, 45, 42, 55, 78, 23, 34, 88, 45, 67, 12, 90, 56, 23, 78, 44, 11, 65, 45, 89, 22, 56, 34, 78, 45, 67, 23, 91, 34, 12, 78, 56, 23, 45, 89, 11]

def remove_duplicates(l):
    u_list = []
    for item in l:
        if item not in u_list:
            u_list.append(item)
    return u_list
unique_list = remove_duplicates(l)

print("Original List:", l)
print("List after removing duplicates:", unique_list)