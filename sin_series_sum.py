import math
degrees=int(input("Enter degrees: "))
nterms=int(input("Enter terms: "))
radians=degrees*math.pi/180

def calculate_sin():
	result=0
	numerator=radians
	denominator=1
	for i in range(1,nterms+1):
		single_term=numerator/denominator
		result=result+single_term
		numerator=-numerator*radians*radians
		denominator=denominator*(2*i)*(2 * i + 1)
	return result
def main():
	result=calculate_sin()
	print("Sum of sin of the series is: ",result)
if __name__== "__main__":
	main()