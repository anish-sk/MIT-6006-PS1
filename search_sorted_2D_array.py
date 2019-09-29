def search_sorted_2D_array(A, v):
    '''
    Return tuple (x, y) such that A[y][x] == v, or None.
    Input:  A | Array of equal length arrays of integers 
              |     representing the rows of a 2D array
              |     where A[y][x] >= A[y - 1][x] and
              |           A[y][x] >= A[y][x - 1] 
              |     for all (x, y) in range.
            v | An integer to search for in A.
    '''
    if(len(A)==0):
      return None
    else:
      n=len(A)
      m=len(A[0])
      i=n-1
      j=0
      for __ in range(m+n):
        if(A[i][j]==v):
          return (j,i)
        elif(A[i][j]<v):
          if(j==m-1):
            return None
          else:
            j+=1
        else:
          if(i==0):
            return None
          else:
            i-=1
    return None


    
