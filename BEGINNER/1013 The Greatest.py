# Make a program that reads 3 integer values and present the greatest one followed by the message "eh o maior".
# Use the following formula:
#
# "MaxAB formula"
#
# Input
# The input file contains 3 integer values.
#
# Output
# Print the greatest of these three values followed by a space and the message “eh o maior”.

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

distance = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

print(f'{distance:.4f}')
