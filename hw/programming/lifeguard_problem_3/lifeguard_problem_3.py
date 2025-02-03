
import math
import random

#Входные данные
def get_data():

    try:
        d_1 = int(input("Введите кратчайшее расстояние между спасателем и кромкой воды, d1 (ярды): "))          #yards
    except ValueError:
        print("Значение расстояния дожно быть целым числом (ярды)")
    try:
        d_2 = int(input("Введите кратчайшее расстояние от утопающего до берега, d2 (футы): "))
    except ValueError:
        print("Значение расстояния дожно быть целым числом (футы)")                                          #foots
    try:
        h = int(input("Введите боковое смещение между спасателем и утопающим, h (ярды): "))                     #yards
    except ValueError:
        print("Значение смещения дожно быть целым числом (ярды)")
    try:
        v_sand = int(input("Введите скорость движения спасателя по песку, v_sand (мили в час): "))              #mph
    except ValueError:
        print("Значение скорости дожно быть целым числом (мили в час)")
    try:
        n = int(input("Ведите коэффициент замедления спасателя при движении в воде, n: "))
    except ValueError:
        print("Значение коэффициента дожно быть целым числом")
    try:
        theta_1 = float(input("Введите направление движения спасателя по песку, theta1 (градусы): "))         #degrees
    except ValueError:
        print("Значение расстояния дожно быть вещественным числом (градусы)")

    return(d_1, d_2, h, v_sand, n, theta_1)

#Converters
def foots_to_miles(foots: int) -> float:
    return foots / 5280.0

def yards_to_miles(yards: int) -> float:
    return foots_to_miles(yards * 3.0)

def degrees_to_rads(dedgrees: int) -> float:
    return dedgrees * math.pi / 180.0

def mph_to_mps(mph: int) -> float:
    return mph / 3600.0



#normailization
def calculate_data(arr: list) -> list:
    d_1_normal = yards_to_miles(arr[0])            #miles
    d_2_normal = foots_to_miles(arr[1])            #miles
    h_normal = yards_to_miles(arr[2])
    v_sand_normal = mph_to_mps(arr[3])          #miles
    n = arr[4]
    theta_1_normal = degrees_to_rads(arr[5])   #rads

    #Calculations

    x = d_1_normal * math.tan(theta_1_normal)

    l_1 = (x ** 2 + d_1_normal ** 2) ** 0.5
    l_2 = ((h_normal - x) ** 2 + d_2_normal ** 2) ** 0.5

    t = v_sand_normal ** (-1) * (l_1 + n * l_2)
    return(arr[5], t)


def print_res(data: tuple):
    print(f"Если спасатель начнет движение под углом theta1, равным {data[0]:.{0}f} градусам, он достигнет утопающего через {data[1]:.{1}f} секунды")



#Program workflow
res = []
input_data = get_data()
new_data = list(input_data)
for _ in range(10000000):
    degree = random.choice(range(0, 900))
    new_data[5] = degree / 10.0
    calculation = calculate_data(new_data)
    res.append(calculation)
res.sort(key=lambda x: x[1])
print_res(res[0])


#Если спасатель начнет движение под углом theta1, равным 81 градусам, он достигнет утопающего через 23.1 секунды