s = [2,3,5,6]
def subset(s):
    subsets = [[]]
    for elem in s:
        new_subsets=[subset + [elem] for subset in subsets]
        subsets.extend(new_subsets)
    return subsets
all_subsets=subset(s)
print(all_subsets)
def subsetsum(s):
    subsets = subset(s)
    return [sum(subset) for subset in subsets]
all_subsets_sums=subsetsum(s)
print(all_subsets_sums) 
k=5
if k in all_subsets_sums:
    print("yes")
else:
    print("no")