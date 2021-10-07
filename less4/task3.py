'''
Задача 3
Реализовать класс точки в N мерном пространстве.
Реализовать валидацию точки.
Реализовать метод получения расстояния этой точки от точки начала координат до этой точки.
Реализовать метод получение размерности.


Реализовать класс прямой в N мерном пространстве(применить наследование от точки в н мерном пространстве).
При инициализации объекта на вход будут приходить два кортежа, которые будут представлять точку A и точку B.

Предусмотреть валидацию данных.
Разработать метод подсчета расстояния между точками.
Разработать метод переноса к началу координат. (то есть точка а становится началом координат, а точка B параллельно переносится. расстояние между точками измениться не должно)

Примечания:
1.	точки прямой должны иметь один и тот же порядок\размерность
2.	для получения расстояния следует использовать расширенную теорему пифагора
3.	постараться сократить дупликацию кода

'''

class Points:
    def __init__(self, n):
        self.n=n
 
    def pointadd(self, *args):
        self.point_coord=args
        print('точка была добавленна',self.point_coord)
        
 
    def point_verification(self):
        for i in self.point_coord:
            try:
                float(i)
            except Exception as e:
                print(f'Error coordinate {i}!!! {e}')
            else:
                print(f'Verification coordinate {i} successfully completed!')

 
    def dist_from_beg(self):
        x=0
        for i in self.point_coord:
            x=x+(i)**2
        print(x**0.5)

class Straight(Points):
        def __init__(self, first_point, second_point):
            self.first_point=first_point
            self.second_point=second_point
            
            
        def straight_validation(self):
            self.point_coord=self.first_point
            print('Point A of straight ver')
            self.point_verification()
            self.point_coord=self.second_point
            print('Point B of straight ver')
            self.point_verification()
        
        def dist_between_points(self):
            x=0
            for i in range(0,len(self.first_point)):
                x=x+(self.first_point[i]-self.second_point[i])**2
            print('The dist between 2 points of straight is: ',x**0.5)

        def point_A_null(self):
            a=[]
            b=[]
            for i in range(0,len(self.first_point)):
                a.append(self.second_point[i]-self.first_point[i])
                b.append(0)
            self.second_point=tuple(a)
            self.first_point=tuple(b)
            print(f'new coord is A:{self.first_point} B:{self.second_point}')
            
            
        

# point1=Points(3)
# point1.pointadd(1.1,2,3)
# point1.dist_from_beg()
# point1.point_verification()

point_A=(4,5,6)
point_B=(7,8,-1)
straight1=Straight(point_A,point_B)
straight1.straight_validation()
straight1.dist_between_points()
straight1.point_A_null()
straight1.dist_between_points()