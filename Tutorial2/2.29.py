def set_ops(s1, s2):
    union_res = s1 | s2
    inter_res = s1 & s2
    diff1_res = s1 - s2
    diff2_res = s2 - s1
    sym_diff_res = s1 ^ s2
    return union_res, inter_res, diff1_res, diff2_res, sym_diff_res

s1 = set(map(int, input("Enter elements of first set (space-separated): ").split()))
s2 = set(map(int, input("Enter elements of second set (space-separated): ").split()))

union_res, inter_res, diff1_res, diff2_res, sym_diff_res = set_ops(s1, s2)

print(f"\nUnion: {union_res}")
print(f"Intersection: {inter_res}")
print(f"Difference (Set1 - Set2): {diff1_res}")
print(f"Difference (Set2 - Set1): {diff2_res}")
print(f"Symmetric Difference: {sym_diff_res}")
