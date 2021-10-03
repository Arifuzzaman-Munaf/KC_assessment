def sum_large(number1, number2):
    len1 = len(number1)
    len2 = len(number2)

    """
    If the length of numbers are not same , then it will add leading zeros to equalize the numbers
    """
    number1 = {True:('0' * (len2-len1) + number1), False:number1}[len2 > len1]
    number2 = {True:('0' * (len1-len2) + number2), False:number2}[len2 < len1]

    sum = ""
    carry = 0

    for i in range(len2-1,-1, -1):
        temp = ((ord(number1[i]) - 48) + ((ord(number2[i]) - 48) + carry))
        sum += chr(temp % 10 + 48)
        carry = temp // 10

    # reverse the string to return actual result
    return sum[::-1]


if __name__ == '__main__':
    number1 = input() #"75459473085933857385395388927439940029438785"
    number2 = input() #"434340861520178920017602947608839099308038535839035"
    result = sum_large(number1, number2)
    print(result)



