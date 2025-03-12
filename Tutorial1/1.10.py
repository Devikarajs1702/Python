def sum_evens(cnt):
    total = 0  
    
    for i in range(cnt):
        num = int(input(f"Enter number {i+1}: "))  
        if num % 2 == 0: 
            total += num  
    
    return total 

cnt = int(input("Enter how many numbers: "))

print(f"Sum of even numbers: {sum_evens(cnt)}")
