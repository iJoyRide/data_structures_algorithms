def collision(asteroids):
    # Initialize an empty stack to keep track of asteroids moving right
    stack = []
    
    # Iterate through each asteroid
    for aes in asteroids:
        # Check if stack has element and the current asteroid is moving left and there are asteroids moving right
        while stack and aes < 0 and stack[-1] > 0:
            # Calculate the collision between the current asteroid and the top asteroid in the stack
            diff = aes + stack[-1]
            
            # If the current asteroid is destroyed due to collision
            if diff < 0:
                stack.pop()  # Remove the asteroid moving right from the stack
                
            # If the top asteroid in the stack is destroyed due to collision
            elif diff > 0:
                aes = 0  # Set the current asteroid as destroyed
                
            # If both asteroids are destroyed due to collision
            else:
                aes = 0  # Set both asteroids as destroyed
                stack.pop()  # Remove the asteroid moving right from the stack
        
        # If the current asteroid survives the collisions
        if aes:        
            stack.append(aes)  # Add the asteroid to the stack
    
    # Return the remaining asteroids after all collisions
    return stack

#Time: O(1) + O(1)
#Space: O(N)

if __name__ == "__main__":
    asteroids = [8, -8]
    print(collision(asteroids))
