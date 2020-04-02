import numpy as np
import matrix_library_solutions as ml
import sys

def test_sum_matrix():
    A = np.random.rand(3,3)
    
    if np.sum(A) - ml.matrix_sum(A) > 1e-10:
        sys.exit('The matrix sum function is not working.')


def test_sum_list():
    A = np.random.rand(10)
    
    if np.sum(A) - ml.list_sum(A) > 1e-10:
        sys.exit('The list sum function is not working.')
        
        
def test_transpose():
    A = np.random.rand(6,4)
    
    if np.sum(np.transpose(A) - ml.transpose(A)) > 1e-10:
        sys.exit('The tranpose function is not working.')
        

def test_dot():
    A = np.random.rand(15)
    B = np.random.rand(15)
    
    if np.sum(A.dot(B) - ml.dot(A,B)) > 1e-10:
        sys.exit('The dot function is not working.')
        
def test_multiply():
    A = np.random.rand(10,3)
    B = np.random.rand(3)
    
    if np.sum(np.matmul(A,B) - ml.multiply(A,B)) > 1e-10:
        sys.exit('The multiply matrices function is not working.')
        
        