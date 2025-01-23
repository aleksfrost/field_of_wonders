
import math

#Входные данные
d_1 = int(input("Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды): "))          #yards
d_2 = int(input("Введите кратчайшее расстояние от утопающего до берега, d2 (футы): "))                  #foots
h = int(input("Введите боковое смещение между спасателем и утопающим, h (ярды): "))                     #yards
v_sand = int(input("Введите скорость движения спасателя по песку, v_sand (мили в час): "))              #mph
n = int(input("Ведите коэффициент замедления спасателя при движении в воде, n: "))
theta_1 = float(input("Введите направление движения спасателя по песку, theta1 (градусы): "))         #degrees

def foots_to_miles(foots: int) -> float:
    return foots / 5280.0

def yards_to_miles(yards: int) -> float:
    return foots_to_miles(yards * 3)

def degrees_to_rads(dedgrees: int) -> float:
    return dedgrees * math.pi / 180.0

def mph_to_mps(mph: int) -> float:
    return mph / 3600.0



#normailization

d_1_normal = yards_to_miles(d_1)            #miles
d_2_normal = foots_to_miles(d_2)            #miles
h_normal = yards_to_miles(h)
v_sand_normal = mph_to_mps(v_sand)          #miles
theta_1_normal = degrees_to_rads(theta_1)   #rads


#Calculations

x = d_1_normal * math.tan(theta_1_normal)

l_1 = (x ** 2 + d_1_normal ** 2) ** 0.5
l_2 = ((h_normal - x) ** 2 + d_2_normal ** 2) ** 0.5

t = v_sand_normal ** (-1) * (l_1 + n * l_2)


print(f"Если спасатель начнет движение под углом theta1, равным {theta_1:.{0}f} градусам, он достигнет утопающего через {t:.{1}f} секунды")