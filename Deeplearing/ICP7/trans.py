# Just disables the warning, doesn't enable AVX/FMA
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
#importing Libraries
import tensorflow as tf

#Taking rows and columns from the user
row=int(input("Enter no of rows:"))
col=int(input("Enter no of columns"))

#taking values from the user
matA = input("Enter Matrix A - 4 Values (Separated by comma) : ")
matB = input("Enter Matrix B - 4 Values (Separated by comma) : ")
matC = input("Enter Matrix C - 4 Values (Separated by comma) : ")
val=row*col

#converting values into List
matListA = [int(A) for A in matA.split(',')]
matListB = [int(B) for B in matB.split(',')]
matListC = [int(C) for C in matC.split(',')]

#validating matrics
if not len(matListA)==val:
    print("matrix A is invalid")
    exit()
elif not len(matListB)==val:
    print("matrix B is invalid")
    exit()
elif not len(matListC)==val:
    print("matrix C is invalid")
    exit()
else:
    #Converting list into matrix with entered rows and columns
    matrixA = tf.constant(matListA,shape=[row, col])
    matrixB = tf.constant(matListB,shape=[row, col])
    matrixC = tf.constant(matListC,shape=[row, col])
    #Here temp1 = matrixA^2
    temp1=tf.pow(matrixA, 2)

    #Here temp2 = (matrixA^2)+matrixB
    temp2=tf.add(temp1, matrixB)

    #Here temp3 = ((matrixA^2)+matrixB)*matrixC
    temp3 = tf.matmul(temp2, matrixC)
    with tf.Session() as sess:
        print("Matrix A : ", sess.run(matrixA))
        print("Matrix B : ", sess.run(matrixB))
        print("Matrix C : ", sess.run(matrixC))
        print("Matrix a^2 : ", sess.run(temp1))
        print("Matrix (a^2)+b : ", sess.run(temp2))
        print("Matrix (a^2)+b *c : ", sess.run(temp3))