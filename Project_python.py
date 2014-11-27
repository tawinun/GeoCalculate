def square_area(side): #calculate square area
      area = side*side
      print area
square_area(input())

def rectangle_area(width, length): #calculate rectangle area
      area = width*length
      print area
rectangle_area(input(), input())

def paralellogram_area(base, height): #calculate paralellogram area
      area = base*height
      print area
paralellogram_area(input(), input())

def rhombus_kite_area(diagonal1, diagonal2): #calculate rhombus area
      p_diagonal = diagonal1*diagonal2
      area = (1/2)*p_diagonal
      print area
rhombus_kite_area(input(), input())trapezium

def trapezium_area(diagonal, branch1, branch2): #calculate trapezium area
      sum_branch = branch1+branch2
      area = (1/2)*diagonal*sum_branch
      print area
trapezium_area(input(), input(), input())

def trapezoid(parallel_side1, parallel_side2, height):
      area = (1/2.0)*height*(parallel_side1+parallel_side2)
      print area
trapezium_area(input(), input(), input()) 

def triangle_area(base, height): #calculate triangle area
      area = (1.0/2)*base*height
      print area
triangle_area(input(), input())

def equilateral_triangle_area(side): #calculate equilateral triangle area
      area = (sqrt(3)/4.0)*side*side
      print area
equilateral_triangle_area(input())

def rightangled_triangle_area(cathetus1, cathetus2): #calculate rightangled triangle area
      area = (1/2.0)*cathetus1*cathetus2
      print area
equilateral_triangle_area(input())

def curved_base_triangular_area(degree, radian): #calculate curved base triangular area
      area = (degree/360.0)*pi*(radian**2)
      print area
equilateral_triangle_area(input())

def circle_area(radian):
      area = float(pi*(radian**2))
      print area
circle_area(input())

def circle_circumference(radian):
      area = 2.0*pi*radian
      print area
circle_circumference(input())

def sphere_surface_area(radian):
      area = 4.0*pi*(radian**2)
      print area
sphere_surface_area(input())

def circularcone_surface_area(radian, slant):
      area = pi*radian*slant
      print area
circularcone_surface_area(input(), input())

def cylinder_surfaceside_area(radian, height):
      area = 2.0*pi*radian*height
      print area
cylinder_surface_area(input(), input())

def sphere_volume(radian):
      volume = (4.0/3)*pi*(radian**3)
      print volume
sphere_volume(input())

def cylinder_volume(radian, height):
      volume = pi*(radian**2)*float(height)
      print volume
cylinder_volume(input(), input())

def cone_volume(radian, height)
      volume = (1.0/3)*pi*(radian**2)*float(height)
      print volume
cone_volume(input(), input())

def trapezoid_volume(parallel_side1, parallel_side2, height, height_prism):
      volume = (1/2.0)*height*(parallel_side1+parallel_side2)*height_prism
      print volume
trapezium_volume(input(), input(), input(), input()) 

def cube_volume(side):
      volume = side**3.0
      print volume
cube_volume(input())

def rectangle_prism_volume(width, length, height)
      volume = width*length*height
      print volume
rectangle_prism_volume(input(), input(), input()) 














