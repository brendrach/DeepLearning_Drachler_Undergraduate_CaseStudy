import numpy as np
import sys

def matrix_sum(A):
        '''
        Summary:
        Sums a multidimensional array, A
        
        Parameters
        ----------
        A : A matrix of arbitrary dimensions. Must have length in both
            dimensions. i.e. cannot be a list. See list_sum.
        '''
        
        mat_sum = 0
        
        ## Count along the rows and columns and add each element.
        for rows in range(len(A[:,0])):
            for cols in range(len(A[0,:])):
                mat_sum += A[rows,cols]
                
        return mat_sum
    
    
def list_sum(A):
    '''
    Summary:
    Sums a list, A.
    
    Parameters
    ----------
    A : A list. 
    
    '''
    
    sum_list = 0
    
    ## Sum the elements of the list.
    for index in range(len(A)):
        sum_list += A[index]
        
    return sum_list
    


def transpose(A):
    '''
    Summary:
    Returns the tranpose of a matrix, A.
    
    Parameters
    ----------
    A : An arbitrary dimensional matrix.
    
    '''
    
    ## Initialize the size of the output array as 
    ## the opposite of the input. 
    ## So, output[dimension_rows = A[dimension_cols], dimension_cols = A[dimension_rows]] 
    output = np.zeros((len(A[0,:]), len(A[:,0])))
    
    ## Loop over the matrix and exchange the rows and columns.
    for rows in range(len(A[:,0])):
        for cols in range(len(A[0,:])):
            output[cols,rows] = A[rows,cols]
        
    return output


def dot(A,B):
    '''
    Summary:
    Computes the dot product of two 1D matrices. For computing
    higher dimensional matrices use multiply. You could in theory
    combine these two and add checks to see the dimension before doing
    any computations but for simplicity, I would leave them separate. 
    
    Parameters
    ----------
    A : a list.
    B : a list.
    '''
    
    output = 0
    
    ## Compute a dot product
    for i in range(len(A)):
        for j in range(len(B)):
            output += A[i] * B[i]
            
    return(output)
    

def multiply(A, B):
    '''
    Summary:
    Computes the product of two matrices. Returns a matrix.
    
    Parameters
    ----------
    A : a matrix.
    B : a matrix.
    '''
    
    ## Check if the two matrices can even be multiplied.
    if len(A[0,:]) != len(B):
        sys.exit("This matrix multiplication is not valid, the number of rows \
                 in Matrix A must equal the number of columns in Matrix B. ")
    
    ## Initialize the output size.
    new_matrix = np.zeros(len(A[:,0]))
    
    
    ## Compute the values in the output.
    for rows in range(len(A[:,0])):
        for cols in range(len(B)):
            
            index_value = 0
            for k in range(0, len(B)):
                index_value = index_value + A[rows,k] * B[k]                
            
            new_matrix[rows] = index_value

    return new_matrix