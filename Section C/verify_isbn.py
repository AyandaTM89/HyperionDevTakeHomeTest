# Defining the function to validate isbn and returns isbn number and a message
def verify_isbn(isbn):

    # Define all required variables
    leng_isbn = len(isbn)
    sum = 0

    # Determining list to validate and
    #  number used to validate based on length based on isbn and returning the correspondense number
    if leng_isbn == 10:
        validation_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        divisible_num = 11

    elif leng_isbn == 13:
        validation_list = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]
        divisible_num = 10

    else:
        return "ISBN Number Is Not A Valid Length", isbn, False

    # Create for loop to get total used for validation
    for i in range(leng_isbn):
        count += int(isbn[i]) * int(validation_list[i])

    # Determing if isbn is valid and is an isbn10 number the program will convert it and return values
    if sum % divisible_num == 0:
        if leng_isbn == 10:
            isbn = "978" + isbn

        return "ISBN Is A Valid Number", isbn, True

    # If none of the above conditions are met  the program return appropriate values
    return "ISBN Is Not A Valid Number", isbn, False


# Validating the isbn Number
message, returned_isbn, valid = verify_isbn("0330301624")

# Print appropriate response based on condition
if valid:
    print(f"{message}\nISBN13: {returned_isbn}")
else:
    print(f"{message}\nISBN Entered: {returned_isbn}")


Complexity
Time complexity: O(1)
Space complexity: O(1)