# n1=input("enter the first number")
# n2=input("enter the second number")
# if n1>n2:
#     print("the biggest number is ",n1)
# print("the biggest number is ",n2)
# else:
#     print("the biggest number ",n2)
# 
# 
# def num_to_words(num):
#     # Define dictionaries to map digits to words
#     ones = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
#     tens = {0: '', 1: 'ten', 2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
#     teens = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

#     # Convert the number to a string and split into individual digits
#     num_str = str(num)
#     digits = [int(d) for d in num_str]

#     # Convert the digits to words
#     words = []
#     if len(digits) == 4:
#         words.append(' '.join([ones[digits[0]], 'thousand']))
#         digits = digits[1:]
#     if len(digits) == 3:
#         if digits[0] > 0:
#             words.append(' '.join([ones[digits[0]], 'hundred']))
#         digits = digits[1:]
#     if len(digits) == 2:
#         if digits[0] == 1:
#             words.append(teens[int(str(digits[0])+str(digits[1]))])
#             digits = []
#         else:
#             words.append(tens[digits[0]])
#             digits = digits[1:]
#     if len(digits) == 1:
#         words.append(ones[digits[0]])

#     # Join the words into a single string and return
#     return ' '.join(words)

# # Example usage
# num =int(input("enter the number : "))
# words = num_to_words(num)
# print(words)  # Output: "one thousand two hundred thirty four"


# t=(10,20,[50,60],30)
# print(t[2])
# l=(10,20,30,40)
# l.append(50)
# print(l)

# n=range(10,20,2)
# for i in n:
#     print(i)