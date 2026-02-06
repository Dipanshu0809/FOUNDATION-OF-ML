# %%
import numpy as np
a = np.array([1,2,3,4,5])
print(a)



# %%
import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2], [3, 4]])

print(a)
print(b)
print(a.mean())
print(b.shape)


# %%
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)

print("Sum:", arr.sum())
print("Mean:", arr.mean())
print("Max:", arr.max())


# %%
import numpy as np

# 1D array
a = np.array([1, 2, 3, 4, 5])
print(a)

# 2D array
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

# Basic operations
print(a + 10)
print(a * 2)
print(a.mean())
print(a.sum())

# Shape and size
print(b.shape)
print(b.size)


# %%
import numpy as np
np.zeros(10)
np.zeros((3,3))

# %%
import numpy as np
np.ones((2,4))

# %%
import numpy as np
np.arange(0,10)

# %%
import numpy as np
np.arange(1,10,2)

# %%
import numpy as np
np.linspace(0,1,5)

# %%
import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
print(arr.ndim) #dimension
print(arr.size) 
print(arr.shape)
print(arr.dtype)

# %%
import numpy as np
arr=np.array([1.2 , 3.5 ,4.7])
arr_int=arr.astype(int)
print(arr_int)

# %%
import numpy as np
arr=np.array([1,2,3,4])
print(arr[0]) #indexing
print(arr[-1])

# %%
import numpy as np
arr=np.array([1,2,3,4])
print(arr[1:3]) #slicing
print(arr[::3])
print(arr[:3])

# %%



