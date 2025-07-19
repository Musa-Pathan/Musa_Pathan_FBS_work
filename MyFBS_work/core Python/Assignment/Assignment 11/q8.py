# 8. Print 1 to 100 in snakes and ladder pattern
def print_snakes_and_ladders():
    num = 1
    for row in range(10):
        current_row = []
        for col in range(10):
            current_row.append(num)
            num += 1
        
        # Reverse every alternate row to create the pattern
        if row % 2 != 0:
            current_row.reverse()
        
        # Print the row with formatting
        for val in current_row:
            print(f"{val:3}", end=" ")
        print()

# Call the function
print_snakes_and_ladders()
