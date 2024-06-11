def countStudents(students, sandwiches):
    
    # Count the number of students who prefer sandwiches of type 0 and 1
    zeros = students.count(0)  # Count students preferring sandwich type 0
    ones = students.count(1)  # Count students preferring sandwich type 1

    # Iterate through each sandwich in the queue
    for sandwich in sandwiches:
        # If the sandwich is of type 0
        if sandwich == 0:
            # If there are still students who prefer sandwich type 0, serve them
            if zeros > 0:
                zeros -= 1
            # If there are no students left who prefer sandwich type 0, stop serving
            else:
                break
        # If the sandwich is of type 1
        elif sandwich == 1:
            # If there are still students who prefer sandwich type 1, serve them
            if ones > 0:
                ones -= 1
            # If there are no students left who prefer sandwich type 1, stop serving
            else:
                break
    
    # Return the number of students who did not get a sandwich
    return zeros + ones

#Time: O(N+M)
#Space: O(1) 

if __name__ == "__main__":
    
    students = [1, 1, 1, 0, 0, 1]
    sandwiches = [1, 0, 0, 0, 1, 1] 
    
    print(countStudents(students, sandwiches))
