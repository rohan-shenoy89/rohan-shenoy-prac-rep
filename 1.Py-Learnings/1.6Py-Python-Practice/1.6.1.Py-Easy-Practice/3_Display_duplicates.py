# Display all duplicate items from a list

def displayDuplicates(sample_list):
    non_dup_list = []
    dup_list = []

    for i in sample_list:
        if i not in non_dup_list:
            non_dup_list.append(i)
        else:
            dup_list.append(i)
    return dup_list


sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
print(displayDuplicates(sample_list))
