## Game of FizzBuzz
## Harry Ammon

def fizzBuzz(start, end):
    for i in range(start, end+1): #set up for loop
        #Self Note: the range function starts at 0 and itterates by 1 until it reaches end
        output = "" #create empty string
        if(i % 3 == 0):output += str("Fizz") # checks if number is divisable by 3    
        if(i% 5 == 0): output += str("Buzz") # checks if number is divisable by 5   
        if(output == ""): output = str(i) # if no text in string, add number to the string
            
        print (output) # print string

fizzBuzz(1,100)

        
