# Chapter 1: String Manipulations

# Screen 1
# Find characters in movie variable
length_string = len(movie)

# Convert the above numeric variable to string
to_string = str(length_string)

# Predefined variable
statement = "Number of characters in this review:"

# Concatenate above two strings and print result
print(statement + " " + to_string)

# Screen 2
# Select the first 32 characters of movie1 string
first_part = movie1[:32]

# Select from 43rd character to the end of movie1
last_part = movie1[42:]

# Select from 33rd to the 42nd character
middle_part = movie2[32:42]

# Print concatenation of the variables first_part, middle_part and last_part in that order. Print movie2 variable
print(first_part+middle_part+last_part) 
print(movie2)

# Screen 3
# Extract the substring from the 12th to the 30th character from the variable movie which corresponds to the movie title. Store it in the variable movie_title
movie_title = movie[11:30]

# Obtain the palindrome - Use slicing. If you don't specify the first or second index and the third one is negative, it will return the characters jumping and backwards.
palindrome = movie_title[::-1]

# Print the word if it's a palindrome
if movie_title == palindrome:
	print(movie_title)


  

