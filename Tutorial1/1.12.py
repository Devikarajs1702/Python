def sum_avg_pos_neg(numbers):
    pos_total = 0  
    neg_total = 0  
    pos_count = 0  
    neg_count = 0 

    for num in numbers:
        if num > 0:
            pos_total += num
            pos_count += 1
        elif num < 0:
            neg_total += num
            neg_count += 1

    pos_avg = pos_total / pos_count if pos_count > 0 else 0
    neg_avg = neg_total / neg_count if neg_count > 0 else 0

    return pos_total, pos_avg, neg_total, neg_avg


nums_list = []
for index in range(4):
    value = int(input(f"Enter number {index+1}: "))
    nums_list.append(value)

pos_total, pos_avg, neg_total, neg_avg = sum_avg_pos_neg(nums_list)

print(f"Sum of positive numbers: {pos_total}")
print(f"Average of positive numbers: {pos_avg:.2f}")
print(f"Sum of negative numbers: {neg_total}")
print(f"Average of negative numbers: {neg_avg:.2f}")
