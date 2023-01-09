#from math import atan2, degrees
import math
import sys
sys.setrecursionlimit(10 ** 6)

#class Point:
#    def __init__(self, x, y):
#        self.x = x
#        self.y = y

#    def subtract(self, p):
#      return Point(self.x - p.x, self.y - p.y)

#    def __str__(self):
#        return '(' + str(self.x) + ', ' + str(self.y) + ')'

   
# calculates the cross product of vector p1 and p2
# if p1 is clockwise from p2 wrt origin then it returns +ve value
# if p2 is anti-clockwise from p2 wrt origin then it returns -ve value
# if p1 p2 and origin are collinear then it returs 0
#def cross_product(p1, p2):
#    return p1.x * p2.y - p2.x * p1.y

# returns the cross product of vector p1p3 and p1p2
# if p1p3 is clockwise from p1p2 it returns +ve value
# if p1p3 is anti-clockwise from p1p2 it returns -ve value
# if p1 p2 and p3 are collinear it returns 0
def direction(p1, p2, p3):
    #return  cross_product(p3.subtract(p1), p2.subtract(p1))
    p3_sub_p1=[p3[0]-p1[0],p3[1]-p1[1]]
    p2_sub_p1=[p2[0]-p1[0],p2[1]-p1[1]]
    return p3_sub_p1[0]*p2_sub_p1[1] - p2_sub_p1[0]*p3_sub_p1[1]
               
 

#def direction(a, b, c):
#    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
#    return ang
# checks if p1, p2 and p3 are collinear
def collinear(p1, p2, p3):
    return direction(p1, p2, p3) == 0

def distance_sq (p1, p2):
    return ((int(p1[0])-int(p2[0]))**2)+((int(p1[1])-int(p2[1]))**2)

#def collinear(p1, p2, p3):
     
    """ Calculation the area of 
        triangle. We have skipped
        multiplication with 0.5 to
        avoid floating point computations """
#    a = p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])
 
#    if (a == 0):
#        return True
#    else:
#        return False

visited = []
    
class Challenge :
   def Hampers ( self , grid , arrhampers) :
       if not grid : return 0
       def dfs ( i , j , grid , hamperspoints) :
           if i < 0 or j < 0 or i >= row or j >= col or grid [ i ] [ j ] == 0 :
               return
           hamperspoints.append([j , i])
           grid [ i ] [ j ] = 0    # Mark cell as zero to avoid recounting
           dfs ( i + 1 , j , grid , hamperspoints)        
           dfs ( i - 1 , j , grid , hamperspoints)
           dfs ( i , j + 1 , grid , hamperspoints)
           dfs ( i , j - 1 , grid , hamperspoints)
           dfs ( i + 1 , j + 1 , grid , hamperspoints)        
           dfs ( i - 1 , j + 1 , grid , hamperspoints)
           dfs ( i + 1 , j - 1 , grid , hamperspoints)
           dfs ( i - 1 , j - 1 , grid , hamperspoints)
           return
       
       hampers = 0
       #arrhampers =[]
       #hamperpoints=[]
       row = len ( grid )
       col = len ( grid [ 0 ] )
       for i in range ( 0 , row ) :    # Traverse grid
           for j in range ( 0 , col ) :
               if grid [ i ] [ j ] == 1 :
                   hamperpoints=[]
                   if [i,j] not in visited:
                       dfs ( i , j , grid ,hamperpoints)
                       arrhampers.append(hamperpoints)
                       visited.append([i,j])
                       hampers += 1
        
       
    
   def jarvis_march(self , arrhamperpoints, polygons):
    # find the leftmost point
     arrhamperpoints.sort(key=lambda x: (x[0],x[1]))
     #a =  min(arrhamperpoints, key = lambda point: point.x)
     a=arrhamperpoints[0]
     index = arrhamperpoints.index(a)
    
    # selection sort
     l = index
     result = []
     result.append(a)
     #print (" First Boundary Point Added= ", a )
     #toomany=0
     while (True):
        #toomany=toomany+1
        #if toomany >1:
        #    exit()
        q = (l + 1) % len(arrhamperpoints)
        #print ("q=",q)
        
        #colinerpointstoappend = []
        #colinerpoints = []
        #colinerpoints.append(q)

        for i in range(len(arrhamperpoints)):
            #print ("i==l?-",i,l)
            if i == l:
                continue
            
            #if colinerpoints[0] != q:
            #    colinerpoints.clear()
            #   colinerpoints.append(q)
            
            # find the greatest left turn
            # in case of collinearity, consider the farthest point
            #print ("points= ",arrhamperpoints[i], arrhamperpoints[l], arrhamperpoints[q])
            d = direction(arrhamperpoints[l], arrhamperpoints[i], arrhamperpoints[q])
            #print ("angle=",d)
            dists_il= distance_sq(arrhamperpoints[i], arrhamperpoints[l])
            dists_ql= distance_sq(arrhamperpoints[q], arrhamperpoints[l])
            #print ("distsq=",dists)
            #if d == 0 and dists_il < dists_ql :
                #colinerpoints.append(i)
                #print ("Coliner point wrt ", q, " added index=", i)
            if d > 0 or (d == 0 and dists_il > dists_ql):
                q = i
                #if len(colinerpoints) > 1:
                #    for i in range(1, len(colinerpoints)) :
                #        colinerpointstoappend.append(colinerpoints[i])
                #print("more left index found=",q)
        l = q
        #print("new l found=",q)
        if l == index:
            break
        #print ("  checking coliner points to add for q=", result[-1], " are ", colinerpointstoappend)
        #if len(colinerpointstoappend) > 0 :
        #     for i in range (len(colinerpointstoappend)):
                #print ("     Coliner Boundary trying being added to ", result[-1], " is =", arrhamperpoints[colinerpointstoappend[i]])
        #        if arrhamperpoints[colinerpointstoappend[i]] not in result :
        #            result.append(arrhamperpoints[colinerpointstoappend[i]])
        #            #print ("Added")
        
        result.append(arrhamperpoints[q])
        #print (q, " th element as New Boundary Added = ", arrhamperpoints[q])
        #boundarytoprint.append(arrhamperpoints[q])

     #Now, added missing points on the boundary those are coliner with the boundary point found so far
     colinermissedpointstobeadded = []
     for i in range(len(result)):
        if len(result) == 1:
            continue
        p1= result[i]
        if i == (len(result)-1):
            p2= result[0]
        else:
            p2= result[i+1]

    
        for j in range(len(arrhamperpoints)):
            if arrhamperpoints[j] not in result and arrhamperpoints[j] not in colinermissedpointstobeadded:
                if collinear(p1,p2,arrhamperpoints[j]):
                    colinermissedpointstobeadded.append(arrhamperpoints[j])
                    #boundarytoprint.append(arrhamperpoints[j])

        
     for i in range(len(colinermissedpointstobeadded)):
        result.append(colinermissedpointstobeadded[i])
     
     polygons.append(result)
     
     #print(result)


                
if __name__ == '__main__':
    line1= input()
    R,C,k = (int(x) for x in line1.split())
    
    if R < 1 or R > 100 or C < 1 or C > 100 or k < 1 or k >= 15 :
      exit(0) 
    
# Initialize matrix
    matrix = []
# For user input
    for i in range(R):          # A for loop for row entries
        matrix.append(list(input())) 
        
    
    #print(matrix)
    result = [list( map(int,i) ) for i in matrix]
    #print(result)
    allhampers = []
    polygons = []
    boundarytoprint = []
    
    
    #print('Number of Hampers : ',Solution().Hampers(result, ))
   
    Challenge().Hampers(result , allhampers)
    #print(a)
    #print (allhampers[0])
    #allhampers[0].sort(key=lambda x: (x[0],x[1]))
    #print (allhampers[0])
    for i in range (len(allhampers)):
       Challenge().jarvis_march(allhampers[i] , polygons)
       #print ("Done with allhampers ", i)   
    
    boundaries = []
    
    countofgifts = []
    
    #for i in range (len(centers),0,-1) :
    if  len(polygons) < k  :
        k = len(polygons)
    for i in range(len(polygons)):
        countofgifts.append([len(polygons[i]), i])
    countofgifts.sort(reverse = True)
  
    for i in range (k) :
        ii=countofgifts[i][1]
        for j in range (len(polygons[ii])):
            boundaries.append([polygons[ii][j][0], R-1-polygons[ii][j][1]])
    boundaries.sort(key=lambda x: (x[0],x[1]))
  
    for i in range (len(boundaries)) :
       print(boundaries[i][0], boundaries[i][1])

    #print(polygons)
    

