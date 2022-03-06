def quicksorting(p, r):
    # repeat and decrease sroting range till have an array (indexes of array!) with 2 element (then partition() sort it)
    if p < r:
        q = partition(p, r)
        quicksorting(p, q - 1)
        quicksorting(q + 1, r)


def partition(p, r):
    # sort array via one element
    x = input_array[r]
    i = p - 1
    for j in range(p, r):
        if input_array[j] <= x:
            i += 1
            exchange(i, j)
    exchange(i + 1, r)
    return i + 1


def exchange(in1, in2):
    # just a very simple method to exchange 2 element in array:
    temp = input_array[in1]
    input_array[in1] = input_array[in2]
    input_array[in2] = temp


size = int(input("Inter the size of your list: "))
input_array = []
for i in range(0, size):
    input_array.append(float(input(str(i + 1) + ". ")))
print(input_array, end="")
# call the first method to start the Process:
quicksorting(0, size - 1)
print(" ====> ", end="")
print(input_array)