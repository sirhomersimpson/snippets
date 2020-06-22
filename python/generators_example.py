import sys
import cProfile


'''
In this snippet, I will play with generators and see how it performs
'''

# Create a list comprehension
n = [num**2 for num in range(1000000)]
# Create a generator
n2 = (num**2 for num in range(100000))

#Memory imprint
print("Memory imprints:")
print("List comprehension: " + str(sys.getsizeof(n)))
print("Generator:" + str(sys.getsizeof(n2)))

print("===========")
print("Execution times:")
cProfile.run('sum(n)')
cProfile.run('sum(n2)')
