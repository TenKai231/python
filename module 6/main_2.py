import numpy 
import sys

var_list= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_array= numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])

print("Ukuran keseluruhan elemen list dalam bytes = ",sys.getsizeof(var_list)*len(var_list))
print("Ukuran keseluruhan elemen NumPy dalam bytes = ", var_array.size*var_array.itemsize)

# matrix = [[0 for j in range (4)] for i in range (3)]
# print(matrix)


# tanpe library
var_mat = [[5,0],[1,5]]
def_mat = [[0 for j in range (2)] for i in range (2)]
for i in range (len(var_mat)):
    for j in range (len(var_mat[0])):
        def_mat[i][j] = var_mat[i][j] * 2 
print (def_mat)

# dengan library
var_mat = numpy.array([[5,0],[1,5]])
def_mat = var_mat * 2
print(def_mat)