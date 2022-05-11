bin_data = '10001111100101110010111010111110011'

# print binary data
print("The binary value is:", bin_data)

# initializing a empty string for
# storing the string data
str_data = ' '

# slicing the input and converting it
# in decimal and then converting it in string
for i in range(0, len(bin_data), 7):
    # slicing the bin_data from index range [0, 6]
    # and storing it as integer in temp_data
    temp_data = int(bin_data[i:i + 7])

    # passing temp_data in BinarytoDecimal() function
    # to get decimal value of corresponding temp_data
    decimal_data = BinaryToDecimal(temp_data)

    # Decoding the decimal value returned by
    # BinarytoDecimal() function, using chr()
    # function which return the string corresponding
    # character for given ASCII value, and store it
    # in str_data
    str_data = str_data + chr(decimal_data)

# printing the result
print("The Binary value after string conversion is:",
      str_data)