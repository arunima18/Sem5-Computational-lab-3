#Function for Partial Pivoting
def partial_pivot(Mat1,n):
    Mat2=[[0,0,0],[0,0,0],[0,0,0]]
    i=0
    j=0
    while i<=1:
        if Mat1[i][i]==0:
            j=i
            
            while j <= n:
                
                if Mat1[j+1][j]!=0:
                    Mat2[j]=Mat1[j+1]
                    Mat1[j+1]=Mat1[i]
                    Mat1[i]=Mat2[j]
                    j=6
                else:
                    j=j+1
        i=i+1
    return Mat1 
    
    
#Function for Gauss Jordan method for 3 cross 3 matrix
def Gauss(Mat1):
    i=0
    j=0
    k=0
    l=0
    num=0
    num2=0
    while i<=2:
        j=0
        k=0
        num=Mat1[i][i]
        while j<=3:
            
                
                Mat1[i][j]=Mat1[i][j]/num
                
                j=j+1 
            
        while k<=2:
            num2=Mat1[k][i]
            l=0
            if k!=i:
                while l<=3:
                    
                    Mat1[k][l]=Mat1[k][l]-num2*Mat1[i][l]
                    
                    l=l+1
                k=k+1
            else:
                k=k+1
        i=i+1 

    
    return Mat1
    
    
#Function for Gauss Jordan for calculating Inverse, Gauss Jordan for n=6
def inverse(Mat1):
    i=0
    j=0
    k=0
    l=0
    num=0
    num2=0
    while i<=2:
        j=0
        k=0
        num=Mat1[i][i]
        while j<=5:
            
                
                Mat1[i][j]=Mat1[i][j]/num
                
                j=j+1 
            
        while k<=2:
            num2=Mat1[k][i]
            l=0
            if k!=i:
                while l<=5:
                    
                    Mat1[k][l]=Mat1[k][l]-num2*Mat1[i][l]
                    
                    l=l+1
                k=k+1
            else:
                k=k+1
        i=i+1 
    return Mat1
        
        
#Function for multiplyig matrix
def multi(Mat1,Mat2):
    i=0
    k=0
    j=0
    sum=0
    arr=[[0,0,0],[0,0,0],[0,0,0]]
    while i<=2:
        j=0
        while j<=2:
            k=0
            sum=0
            while k<=2:
                sum=sum+ Mat1[i][k]*Mat2[k][j]
                k=k+1
                arr[i][j]=sum
            j=j+1
        i=i+1
    return arr
    
    
#Main Function
import Eqn1
Mat1=Eqn1.MatrixA
print('The first given augmented matrixA is ')
print(Mat1)
import Eqn2
Mat2=Eqn2.MatrixB
print('The second given augmented matrixB is ')
print(Mat2)

#Partial pivot and gauss jordan for matrix 1
Mat1a=partial_pivot(Mat1,2)
Mat1b=Gauss(Mat1a)
print('The augmented resultant matrixA is: ')
print(Mat1b)
i=0
print('The soltution for the first set of equations is: ')
while i<=2:
    print(Mat1b[i][3])
    i=i+1

#Partial pivot and gauss jordan for matrix 2 
Mat2a=partial_pivot(Mat2,2)
Mat2b=Gauss(Mat2a)
print('The augmented resultant matrixB is: ')
print(Mat2b)
i=0
print('The soltution for the second set of equations is: ')
while i<=2:
    print(Mat2b[i][3])
    i=i+1
    
#Inverse of Matrix
import Matrix
MatA=Matrix.Matrix
print('The given augmented matrix to calculte inverse is: ')
print(MatA)

MatAa=partial_pivot(MatA,5)
MatB=inverse(MatAa)
print('The inverse of the given matrix is: ')
i=0
j=0
Inverse=[[0,0,0],[0,0,0],[0,0,0]]
while i<=2:
    j=0
    while j<=2:
        Inverse[i][j]=(MatB[i][j+3])
        j=j+1 
    i=i+1 
print(Inverse)

#verify inverse
MatI=multi(MatAa,MatB)
print('We verify that the product of the two matrices are: ')
print(MatI)


'''
The first given augmented matrixA is 
[[1, 3, 2, 2], [2, 7, 7, -1], [2, 5, 2, 7]]
The second given augmented matrixB is 
[[0, 2, 5, 1], [3, -1, 2, -2], [1, -1, 3, 3]]
The augmented resultant matrixA is: 
[[1.0, 0.0, 0.0, 3.0], [0.0, 1.0, 0.0, 1.0], [0.0, 0.0, 1.0, -2.0]]
The soltution for the first set of equations is: 
3.0
1.0
-2.0
The augmented resultant matrixB is: 
[[1.0, 0.0, 0.0, -2.0], [0.0, 1.0, 0.0, -2.0], [0.0, 0.0, 1.0, 1.0]]
The soltution for the second set of equations is: 
-2.0
-2.0
1.0
the given augmented matrix to calculte inverse is: 
[[1, -3, 7, 1, 0, 0], [-1, 4, -7, 0, 1, 0], [-1, 3, -6, 0, 0, 1]]
The inverse of the given matrix is: 
[[-3.0, 3.0, -7.0], [1.0, 1.0, 0.0], [1.0, 0.0, 1.0]]
We verify that the product of the two matrices are: 
[[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]


'''





    
    
    
    
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    