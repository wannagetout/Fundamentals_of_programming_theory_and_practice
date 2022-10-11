"""
import math


x = float(input())

y = float(input())

first_summand = math.asin(math.cos(x + math.sqrt(3)/2*math.pi))
#a = 1.2
#b = math.pow(math.cos(y))
#c = math.sqrt(2 - b)
#second_summand = a * c
second_summand = 1.2 * (math.sqrt(2 - math.pow((math.cos(y)), 2)))
#second_summand = 1.2 * math.sqrt(2 - math.sqrt(math.cos(y)))
denominator = math.pow(x, 2) + math.pow(y, 2) + 1

# вычислить выражение, результат занести в переменную z 
z = (first_summand + second_summand) / denominator

print(round(z, 5))

#--------------------------------------------------------------------------------------------------------------------------------------------------
"""
#--------------------------------------------------------------------------------------------------------------------------------------------------
"""from math import sqrt, acos, degrees


def compute_len(x_0,y_0,x_1,y_1):
    
    len_line = sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
    
    return len_line


def compute_area(a_1, a_2, a_3):
    
    p = (a_1 + a_2 + a_3) / 2
    
    area = sqrt(p * (p - a_1) * (p - a_2) * (p - a_3))
    
    return area


def compute_angle(a_1, a_2, a_3):
    
    angle_rad = acos((a_1 ** 2 + a_2 ** 2 - a_3 ** 2)/
                     (2 * a_1 * a_2))
    
    return degrees(angle_rad)

x_a = float(input("x_a = "))
y_a = float(input("y_a = "))
x_b = float(input("x_b = "))
y_b = float(input("y_b = "))
x_c = float(input("x_c = "))
y_c = float(input("y_c = "))

c = compute_len(x_a, y_a, x_b, y_b)
a = compute_len(x_b, y_b, x_c, y_c)
b = compute_len(x_a, y_a, x_c, y_c)

if a + b <= c or b + c <= a or a +c <= b:
    print("Треугольник не существует")
else:     
    s = compute_area(a, b,c)
    p = a + b + c
    angle_A = compute_angle(c, b, a)
    angle_B = compute_angle(c, a, b)
    angle_C = compute_angle(a, b, c)
    
print("Стороны : ", round(a, 3), round(b, 3), round(c, 3))
print("Площадь : ", round(s,3))
print("Периметр : ", round(p,3))
print("Углы : ", round(angle_A, 3), round(angle_B, 3), round(angle_C, 3))"""

#--------------------------------------------------------------------------------------------------------------------------------------------------
"""import math

x_a = float(input())
y_a = float(input())
x_b = float(input())
y_b = float(input())
x_c = float(input())
y_c = float(input())


def compute_len(x_0,y_0,x_1,y_1):
    len_line = math.sqrt((x_1 - x_0) ** 2 + (y_1 - y_0) ** 2)
    return len_line


def compute_area(a_1, a_2, a_3): 
    p = (a_1 + a_2 + a_3) / 2
    area = math.sqrt(p * (p - a_1) * (p - a_2) * (p - a_3))
    return area

a = compute_len(x_b, y_b, x_c, y_c)
b = compute_len(x_a, y_a, x_c, y_c)
c = compute_len(x_a, y_a, x_b, y_b)

if a + b <= c or b + c <= a or a +c <= b:    
    print("error")
else:
    p = a + b + c
    s = compute_area(a, b, c)


    r = math.sqrt(((p/2 - a) * (p/2 - b) * (p/2 - c)) / (p / 2)) # Радиус вписанной в треугольник окружности
    R = (a * b * c) / (4 * s)

    
    m_a = 0.5 * math.sqrt(2 * ((c ** 2) + (b ** 2)) - (a ** 2))
    m_b = 0.5 * math.sqrt(2 * ((a ** 2) + (c ** 2)) - (b ** 2))
    m_c = 0.5 * math.sqrt(2 * ((a ** 2) + (b ** 2)) - (c ** 2))

    median_sum = m_a + m_b + m_c
    
    print(round(r, 4), round(R,4), round(median_sum,4))"""

#--------------------------------------------------------------------------------------------------------------------------------------------------

"""v = float(input())

if v <= 0:
    print("error")
elif v <= 7.8:
    print(0)
elif v > 7.8 and v <11.2:
    print(1)
elif v >= 11.2 and v <= 16.4:
    print(2)
else:
    print(3)"""

#--------------------------------------------------------------------------------------------------------------------------------------------------

"""import math

edge_len = float(input())
height = float(input())

if edge_len <= 0 or height <= 0:
    print("error")
else:
    pyramid_v = (edge_len ** 2 * height) / (4 * math.sqrt(3))
    pyramid_s = ((edge_len ** 2 * math.sqrt(3)) / 4) + (((3 * edge_len) / 2)*math.sqrt((height ** 2) + (edge_len ** 2 / 12)))

    print(round(pyramid_v, 3), round(pyramid_s, 3))"""

#--------------------------------------------------------------------------------------------------------------------------------------------------

"""year = int(input())

if year < 1582:
    print("error")
elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(366)
else:
    print(365)"""

#--------------------------------------------------------------------------------------------------------------------------------------------------

"""money = int(input())

if money < 1 or money > 99:
    print("error")
elif money == 11 or money == 12 or money == 13 or money == 14:
        print(money, "рублей")
elif money % 10 == 1:   
    print(money, "рубль")
elif money % 10 == 2 or money % 10 == 3 or money % 10 == 4:
    print(money, "рубля")
else:
    print(money, "рублей")"""

#--------------------------------------------------------------------------------------------------------------------------------------------------

"""import math

a = float(input()) # метры
b = float(input()) # миллилитры
v = int(input()) # литры

if a <= 0 or b <= 0 or v <= 0:
    print("error")
else:
    s = a * a
    s_pull = s * 5
    charge_color = (s_pull * b) / 1000
    jars = charge_color / v
    print(math.ceil(jars))
"""
#--------------------------------------------------------------------------------------------------------------------------------------------------

"""h = int(input()) # часы
m = int(input()) # минуты
s = int(input()) # секунды

if (h < 0 or h > 11) or (m < 0 or m > 59) or (s < 0 or s > 59):
    print("error")
else: 
    h_degrees = 30 * h
    m_degrees = m * 0.5
    s_degrees = s * (0.5/60)

    degree = (h_degrees + m_degrees + s_degrees)

    print(round(degree, 2))"""

#--------------------------------------------------------------------------------------------------------------------------------------------------
# Расчёт прибыли от вложений
"""from math import pow

# deposit - сумма вклада, interest_rate -процентная ставка,
# amount_months - количество месяцев
def compute_income(deposit, interest_rate, amount_months):
    income = deposit * pow((1 + (interest_rate / (12 * 100))), amount_months)
    return round(income - deposit) 

x = float(input())
k = float(input())
n = int(input())
# вычислить прибыль с помощью функции
s = compute_income(x, k, n)
print(s)"""

#--------------------------------------------------------------------------------------------------------------------------------------------------

"""def compute_income(deposit, interest_rate, amount_months):
    income = deposit * pow((1 + (interest_rate / (12 * 100))), amount_months)
    return round(income - deposit) 
   

k = 7.0 # занести процент вклада
n = 6.0 # занести количество месяцев
s = 775.0 # занести прибыль

for x in range(1000, 30000):
    
    #вычислить прибыль для вклада x с помощью функции  compute_income(x, ..., ...)
    income = compute_income(x, k, n)
    #print(x)
    #print(income)
    if round(income) == s:
       # вывести значение вклада x
       print(x)
       break"""
       

#--------------------------------------------------------------------------------------------------------------------------------------------------

"""import math

def compute_population(t):
   #вычислить численность населения для года t по формуле
   c = 172 # 172 миллиарда человек
   t_1 = 2000 # 2000 год
   tau = 45 # 45 лет
   n_t = (c / tau) * ((math.pi / 2) - (math.atan((t_1 - t) / tau)))
   return n_t


#ввести строку с перечисленными через пробел годами

x_list=[int(x) for x in input().split()]
population = [compute_population(t) for t in x_list]


for i in range(len(x_list)):
    print(f'{"%5d - %6.3f миллиард(ов)"}' % (x_list[i], population[i]))



# сформировать список years_list на основе years_str_list, 
#преобразовав строковые значения в целые


# создать список population_list, каждый элемент которого вычисляется 
# функцией compute_population от соответсвующего года из списка years_list


# в цикле для каждого года вывести численность населения, для вывода использовать 
# формат "%5d - %6.3f миллиард(ов)"""

#--------------------------------------------------------------------------------------------------------------------------------------------------

"""import matplotlib.pyplot as plt

line = plt.plot([1, 5, -3, -0.5], [1, 25, 9, 0.25])
plt.setp(line, color="green", linewidth = 1, marker=".")

plt.gca().spines["left"].set_position("zero")
plt.gca().spines["bottom"].set_position("zero")

plt.gca().spines["right"].set_visible(False)
plt.gca().spines["top"].set_visible(False)

plt.show()"""

#--------------------------------------------------------------------------------------------------------------------------------------------------

"""import matplotlib.pyplot as plt

x_list = [1, 5, -3]

y_list = [-5, 6, 1 ]

plt.plot(x_list, x_list)

plt.show()"""

#--------------------------------------------------------------------------------------------------------------------------------------------------

"""import math
import matplotlib.pyplot as plt

def compute_population(t):
   #вычислить численность населения для года t по формуле
   c = 172 # 172 миллиарда человек
   t_1 = 2000 # 2000 год
   tau = 45 # 45 лет
   n_t = (c / tau) * ((math.pi / 2) - (math.atan((t_1 - t) / tau)))
   return n_t

a = int(input())
b = int(input())
#ввести строку с перечисленными через пробел годами

x_list=[i for i in range(a, b+1, 25)]         #[int(x) for x in input().split()]
population = [compute_population(t) for t in x_list]

line = plt.plot(x_list, population)

plt.setp(line, color="green", linewidth = 0.5, marker="+")

plt.grid()
plt.show()
"""
#--------------------------------------------------------------------------------------------------------------------------------------------------

"""import matplotlib.pyplot as plt

line_blue = plt.plot([1, 5, -3, -0.5], [1, 25, 9, 0.25], label='Крутая синяя линия')
line_red = plt.plot([-6, -5, 0, -0.5], [1, 25, 9, 0.25], label='Крутая красная линия(красная, потому что злится)')

plt.setp(line_blue, color = 'blue', linewidth = 1, marker = 'v')
plt.setp(line_red, color = 'red', linewidth = 0.5, marker = '.')

plt.grid()
plt.legend()
plt.title('Синяя и красная линии (дома отдыхают)')

plt.show()"""

#--------------------------------------------------------------------------------------------------------------------------------------------------

"""from math import *
import matplotlib.pyplot as plt

def f_x(x):
    x = radians(x)
    fx = e**cos(x) + log(sin(0.8 * x)**2 + 1) * cos(x)
    return fx


def y_x(x):
    x = radians(x)
    yf = -log((cos(x) + sin(x))**2 + 1.7) + 2
    return yf


a = -240
b = 360
n = 70
h = (b - a)/(n - 1)

list_x = [a + h * i for i in range(n)]

list_fx = [degrees(f_x(x)) for x in list_x]
list_yx = [degrees(y_x(x)) for x in list_x]


line_fx = plt.plot(list_fx, label='f(x)')
line_yx = plt.plot(list_yx, label='y(x)')

plt.setp(line_fx, color='green', linewidth = 0.8, marker='+')
plt.setp(line_yx, color='purple', linewidth = 1, marker='.')


plt.gca().spines["left"].set_position("zero")
plt.gca().spines["bottom"].set_position("zero")
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

plt.grid()
plt.legend()
plt.show()"""

#--------------------------------------------------------------------------------------------------------------------------------------------------

"""plt.xlim(0, 12)
plt.ylim(0, 12)

ax = plt.gca()
circle = Circle((5, 5), 3)

ax.add_patch(circle)

plt.show()"""

#--------------------------------------------------------------------------------------------------------------------------------------------------

"""n = 8
m = 8
plt.xlim(0, n)
plt.ylim(0, m)
ax = plt.gca()

vertrces = [(0, 6), (2, 8), (2, 4), (4, 6), (4, 2), (6, 4), (6, 0), (8, 2)]
codes = [1, 2, 1, 2, 1, 2, 1, 2]

path = Path(vertrces, codes)
path_patch = PathPatch(path, lw=3)
ax.add_patch(path_patch)
ax.axes.set_axis_off()
plt.show()"""

#--------------------------------------------------------------------------------------------------------------------------------------------------

"""from matplotlib.patches import Circle, Wedge, Polygon, Ellipse, Arc, Path, PathPatch
import matplotlib.pyplot as plt

def draw_cat(ax):
    # туловище
    poly = [(3, 1), (4, 14), (5, 11), (8, 11), (9, 14), (10, 1)]
    polygon = Polygon(poly, fc="green", ec="black", lw=4)
    ax.add_patch (polygon)

    # глаза
    circle = Circle((5.3, 8.5), 1.2, fc="white", ec="black", lw=4)
    ax.add_patch (circle)

    circle = Circle((7.7, 8.5), 1.2, fc="white", ec="black", lw=4)
    ax.add_patch (circle)

    # зрачки
    circle = Circle((6, 8.3), 0.1, fc="black", ec="black", lw=4)
    ax.add_patch (circle)

    circle = Circle((7, 8.3), 0.1, fc="black", ec="black", lw=4)
    ax.add_patch (circle)

    # нос
    circle = Circle((6.5, 7.5), 0.3, fc="black", ec="black", lw=4)
    ax.add_patch (circle)

    # задние лапы
    wedge = Wedge((3, 1), 2, 86, 180, fc="green", ec="black", lw=4)
    ax.add_patch (wedge)
    
    wedge = Wedge((10, 1), 2, 0, 94, fc="green", ec="black", lw=4)
    ax.add_patch (wedge)

    # передние лапы
    ellipse = Ellipse((5.5,1.2), 2, 1.5, fc="green", ec="black", lw=4)
    ax.add_patch (ellipse)

    ellipse = Ellipse((7.5,1.2), 2, 1.5, fc = "green", ec="black", lw=4)
    ax.add_patch (ellipse)

    # улыбка
    arc =  Arc((6.5, 6.5), 5, 3, 0, 200, 340, lw=4, fill=False)
    ax.add_patch(arc)

    # линия между носом и улыбкой, усы
    vertices = [(6.5, 5), (6.5, 7.5), (10, 6), (6.5, 7.5), (10, 6.5), (6.5, 7.5), (10, 7),
                (6.5, 7.5), (3, 6), (6.5, 7.5), (3, 6.5), (6.5, 7.5), (3, 7)]
    
    # число 1 соответствует команде matplotlib.path.Path.MOVETO
    # число 2 соответствует команде matplotlib.path.Path.LINETO
    codes = [1, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]

    path = Path(vertices, codes)
    path_patch = PathPatch(path, fill=False, lw=1)
    ax.add_patch(path_patch)

n = 13
m  = 15
plt.xlim(0, n)
plt.ylim(0, m)

ax = plt.gca()
draw_cat(ax)

ax.axes.set_axis_off()
plt.show()"""

#--------------------------------------------------------------------------------------------------------------------------------------------------

"""from matplotlib.patches import Path, PathPatch
import matplotlib.pyplot as plt

n = 8

m  = 7

plt.xlim(0, n)

plt.ylim(0, m)

ax = plt.gca()

# создать массив точек
vertices = [(1, 3), (7, 2), (6, 1), (3, 1), (1, 3), (4, 2.5), (4,6), (7, 3), (4,2.5)]

#создать список кодов для последовательности рисования:
codes = [1,2,2,2,2,1,2,2,2]


#создать объект path
path = Path(vertices, codes)

#создать фигуру
path_patch = PathPatch(path, lw=3)

# Добавить созданную фигуру в область ax:
ax = plt.gca()
ax.add_patch(path_patch)
ax.axes.set_axis_off()
#оператор 1

plt.show()
"""

#--------------------------------------------------------------------------------------------------------------------------------------------------

"""import matplotlib.pyplot as plt
from matplotlib.patches import Wedge, Arc

n = 8
m  = 7
plt.xlim(0, 6)
plt.ylim(0, 5)
ax = plt.gca()

# нарисовать сектор (среди возможных вариантов указать  НАИМЕНЬШИЕ ПОЛОЖИТЕЛЬНЫЕ углы)
figure_w = Wedge((3, 1), 2, 45, 135)# сформировать сектор, параметры для цвета линии и заливки, а также толщины линии не указывать
ax.add_patch(figure_w)

# нарисовать дугу (среди возможных вариантов указать НАИМЕНЬШИЕ ПОЛОЖИТЕЛЬНЫЕ углы
#с НУЛЕВЫМ углом поворота)
# дуга должна иметь определенную толщину (linewidth=3), цвет не указывать
figure_a = Arc((3, 1), 6, 6, 0, 45, 135, lw=3)# сформировать дугу
ax.add_patch(figure_a)

#ax.axes.set_axis_off()
plt.grid()
plt.show()"""

#--------------------------------------------------------------------------------------------------------------------------------------------------

"""
# Рассчитать теплопроводность кремния для заданного интервала температур. Количество расчетных значений - 20
import matplotlib.pyplot as plt

def compute_lambda(t):
    b = 33
    l_0 = 844
    t_0 = 100
    y = b * l_0 / (t - t_0)
    return y

t1, t2 = float(input()), float(input())

if t2 <= t1 or t1 <= 100:
    print("Неверные границы значений")
else:
    n = 20
    h = (t2 - t1) / (n - 1)
    
    t_list = [t1 + i * h for i in range(0, n)]
    lambda_list = [compute_lambda(t) for t in t_list]
    
    print("-" * 21)
    print("| %7s | %7s |" % ("t", "L(t)"))
    print("-" * 21)
    for i in range(len(t_list)):
         print("| %7.2f | %7.2f |" % (t_list[i], lambda_list[i]))
    print("-" * 21)"""

#--------------------------------------------------------------------------------------------------------------------------------------------------
 
"""
#Рассчитать ежемесячную сумму платежа по кредиту при использовании дифференцированных выплат 
#(в этом случае ежемесячный платеж по погашению кредита постепенно уменьшается к концу периода кредитования)

def month_peyment(t = int, s = int, n = int, k = int):
    # s сумма кредита, руб
    # n срок кредита, месяцев
    # k процент
    return (s / n) + (s - (t - 1) * (s / n)) * (k / (12 * 100))

s, n, k = int(input()), int(input()), int(input())
sum_pay = 0
#payment = [month_peyment(t, s, n, k) for t in range(1, n + 1)]
for t in range(1, n + 1):
    
    pay = month_peyment(t, s, n, k)
    sum_pay += pay
    print(f"%2d месяц - %8.2f руб" %  (t, pay))
print(f"Доход банка - %6.2f руб" % (sum_pay - s))
"""
#--------------------------------------------------------------------------------------------------------------------------------------------------
"""
import matplotlib.pyplot as plt

def compute_lambda(t):
    b = 33
    l_0 = 884
    t_0 = 100
    y = b * l_0 /(t-t_0)
    return y



f =  open("lambda_exp.txt", "r")
t_list =[]
lambda_exp_list = []
for line in f:
	t_lambda_list = line.split()
	t_list.append(float(t_lambda_list [0]))
	lambda_exp_list.append(float(t_lambda_list [1]))
f.close()

lambda_list = [compute_lambda(t) for t in t_list]
error_list = [abs((lambda_exp_list[i] - lambda_list[i]) / lambda_exp_list[i])for i in range(len(t_list))]

print("-" * 40)
print("|%7s | %7s | %7s | %8s" % ("t", "l(t)", "exp(t)", "error"))
for i in range(len(t_list)):
    print("|%7d | %7.3f | %7.1f |%7.2f%% |" % (t_list[i], lambda_list[i], lambda_exp_list[i], error_list[i] * 100))
print("-" * 40)

max_error = max(error_list)
index_max_error = error_list.index(max_error)
print("Максимальная погрешность = %5.2f%%  при t = %5d" % (max_error * 100, t_list[index_max_error]))

min_error = min(error_list)
index_min_error = error_list.index(min_error)
print("Минимальная погрешность = %5.2f%% при t = %5d" % (min_error * 100, t_list[index_min_error]))

avg_error = sum(error_list) / len(error_list)
print("Средняя погрешность = %0.2f%%" % (avg_error * 100))

#Вычисление максимальной и средней погрешности для интервала температур от 300оК до 1400оК

dot_error_list = error_list[1:13]
dot_t_list = t_list[1:13]
a = [(i * 100) for i in dot_error_list]
dot_lambda_exp_list = lambda_exp_list[1:13]
dot_max_error = max(dot_error_list)
dot_index_max_error = dot_error_list.index(dot_max_error)
print("Максимальная погрешность диапазона 300К - 1400К = %5.2f%% при t = %5d" % (dot_max_error * 100, dot_t_list[dot_index_max_error]))

dot_avg_error = sum(dot_error_list) / len(dot_error_list)
print("Средняя погрешность диапазона 300К - 1400К = %0.2f%%" % (dot_avg_error * 100))


line_th = plt.plot(t_list, lambda_list, label='Теоретические')
line_exp = plt.plot(t_list, lambda_exp_list, label='Экспериментальные')


#Стили линий

plt.setp(line_th, color='blue', linestyle='--', linewidth = 2)
plt.setp(line_exp, color='red', linewidth = 2)
plt.legend()

plt.gca().spines["left"].set_position("zero")
plt.gca().spines["bottom"].set_position("zero")
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.title('Значения теплопроводности')

plt.show()
"""

#--------------------------------------------------------------------------------------------------------------------------------------------------
"""
from math import pi, atan
import matplotlib.pyplot as plt

def calculate_population(t = int):
    # t - год, для которого вычисляется численность населения
    c = 172
    t1 = 2000
    tau = 45
    n = c/tau * (pi/2 - atan((t1 - t) /tau))
    return n

years = [1000, 1750, 1800, 1850, 1900, 1950, 1955, 
         1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 
         2000, 2005, 2010, 2011, 2012, 2013, 2014, 2015,
         2016, 2017, 2018, 2019]

population =[0.400, 0.791, 1.000, 1.262, 1.650, 2.519,
             2.756, 3.021, 3.335, 3.692, 4.068, 4.435, 4.831,
             5.264, 5.674, 6.071, 6.344, 6.933, 7.015, 7.100,
             7.162, 7.271, 7.358, 7.444, 7.530, 7.669, 7.763]

a, b = int(input()), int(input())
#print(a)
#print(b)

r_population = [calculate_population(t) for t in years]
#print(*r_population)

#lambda_list = [compute_lambda(t) for t in t_list]
#error_list = [abs((lambda_exp_list[i] - lambda_list[i]) / lambda_exp_list[i])for i in range(len(t_list))]

error_list = [abs((r_population[i] - population[i]) / population[i]) for i in range(len(years))]

print("-" * 40)
print("|%8s |%7s | %7s | %7s | %8s" % ("id", "p", "p(t)", "years", "error"))
for i in range(len(years)):
    print("| %7d |%7.3f | %7.3f | %7.1f |%7.2f%% |" % (i, population[i], r_population[i], years[i], error_list[i] * 100))
print("-" * 40)

min_error = min(error_list[a:b+1])
index_min_error = error_list.index(min_error)
min_error_year = years[index_min_error]

max_error = max(error_list[a:b+1])
index_max_error = error_list.index(max_error)
max_error_year = years[index_max_error]

avg_error = sum(error_list[a:b+1]) / len(error_list[a:b+1])
print("Погрешность - минимальная, год: %4d, максимальная, год: %4d, средняя, процент: %6.3f" % (min_error_year, max_error_year, round(avg_error * 100, 3)))

line_th = plt.plot(years, r_population, label='Теоретические')
line_exp = plt.plot(years, population, label='Экспериментальные')


plt.setp(line_th, color='blue', linestyle='--', linewidth = 2)
plt.setp(line_exp, color='red', linewidth = 2)
plt.legend()



plt.gca().spines["left"]
plt.gca().spines["bottom"].set_position("zero")
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)
plt.title('Численность населения планеты')

plt.show()
"""

"""def avg_temp(t_0, t_12):
    return (float(t_0) + float(t_12)) / 2

list_0 = input().split()
list_12 = input().split()
c = float(input())

avg_list_day = [avg_temp(i, j) for i, j  in zip(list_0, list_12)]
#avg_list_12 = [avg_temp(i) for i in list_12]

#all_d = sum(avg_list_day) / len(avg_list_day)
days = [avg_list_day.index(i) for i in avg_list_day if i > c]
for i in range(len(avg_list_day)):
    if avg_list_day[i] > c:
        print(i)"""


"""
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib.patches import Patch, Circle


def compute_range(x_0 = int, y_0 = int, x_1 = int, y_1 = int):
    len_line = sqrt((int(x_1) - int(x_0)) ** 2 + (int(y_1) - int(y_0)) ** 2)
    return len_line


o_x = input().split()
o_y = input().split()

k = int(input())
r = int(input())

radio_dot_x = o_x[k]
radio_dot_y = o_y[k]

distances = [compute_range(radio_dot_x, radio_dot_y, o_x[i], o_y[i]) for i in range(len(o_x))]

count = 0
for d in distances:
    if d < r:# сравните расстояние d с радиусом действия r
        count = count +1
print(count)
"""

"""
month_energy = input().split()
n = int(input())
a, b = float(input()), float(input())
month_energy_integers = [int(i) for i in month_energy]

def using_energy(using_month_energy):
    if using_month_energy > n:
        over_normal_using = using_month_energy - n
        return (n * a) + (over_normal_using * b)
    else:
        return using_month_energy * a
    
month_energy_cost = [using_energy(int(i)) for i in month_energy]

year_energy_using = sum(month_energy_integers)
year_energy_cost = sum(month_energy_cost)

print("Сумма: %6d кВт ч, стоимость %7.2f руб" % (year_energy_using, year_energy_cost))
"""
"""
from math import pow

s, n, k = int(input()), int(input()), int(input())

def differentiated_payment(s = int, n = int, k = int, t = int) -> float:
    return (s / n) + (s - (t - 1) * (s / n)) * (k / (12 * 100))

def annuity_payment(s = int, n = int, k = int) -> float:
    k_a = k / (12 * 100)
    return ((k_a * ((1 + k_a) ** n)) / (((1 + k_a)** n) - 1)) * s

list_differentiated_payment = [differentiated_payment(s, n, k, i) for i in range(1, n+1)]
list_annuity_payment = [annuity_payment(s, n, k) for _ in range(1, n+1)]


for month in range(n):
    print("%2d месяц - (диф.) %8.2f руб - (анн.) %8.2f руб" % (month + 1, list_differentiated_payment[month], list_annuity_payment[month]))

print("Доход банка - (диф.) %6.2f руб - (анн.) %6.2f руб" % ((sum(list_differentiated_payment) - s), (sum(list_annuity_payment) - s)))
"""

"""
import numpy as np

path = np.array([15, 5, 12, 2, 21, 17, 21, 3, 10, 5])
speed = np.array([60, 30, 60,45, 50, 60, 50, 40, 60, 40])

len_path = path.sum()
print("Расстояние между пунктами A и B:", len_path)

len_path = np.sum(path)
print("Расстояние между пунктами A и B:", len_path)

time = path / speed
print("Время на каждом участке: ", np.round(time, 2))

sum_time = np.sum(time)
print("Общее время пути: ", round(sum_time, 2))

avg_speed = len_path / sum_time
print("Средняя скорость на всём пути: ", round(avg_speed, 2))
"""
"""import numpy as np

path_input = input()
speed_input = input()

path = np.array(path_input.split(), dtype=int)
speed = np.array(speed_input.split(), dtype=int)

path_sum = np.sum(path)
time = path / speed
time_sum = time.sum()
avg_speed = path_sum / time_sum
print("S = %3d км, T = %5.2f час, V = %5.2f км/ч" % (path_sum, time_sum, avg_speed))
"""


"""
import numpy as np

costs = np.array([1200, 1300, 900, 1450, 1300, 1000, 900, 1000, 1450, 1450, 1300, 1400])

# посчитать сумму за проезд в зимние месяцы
sum_winter = costs[0] + costs[1] + costs[-1]
# посчитать сумму за проезд в летние месяцы
sum_summer = costs[5] + costs[6] + costs[7]

if sum_winter > sum_summer:
    print("Зимой на проезд потрачено больше денег, сумма: %4d руб." % sum_winter)
elif sum_winter < sum_summer:
    print("Летом на проезд потрачено больше денег, сумма: %4d руб." % sum_summer)
else:
    print("Зимой и летом на проезд тратится одинаковая, сумма: %4d руб." % sum_winter)

# найти максимальную сумму оплаты за месяц    
max_costs = max(costs)

# найти номера месяцев, в которые тратилась наибольшая сумма
max_month = np.where(costs == max_costs)

print("Самая большая сумма:%4d руб., потрачена в следующих месяцах:" % max_costs, max_month[0] + 1)
"""

"""
import numpy as np

path_input = input()
speed_input = input()
n_start = int(input())
n_end = int(input()) + 1

path = np.array(path_input.split(), dtype=int)
speed = np.array(speed_input.split(), dtype=int)

path_sum = np.sum(path[n_start:n_end])
time = path[n_start:n_end] / speed[n_start:n_end]
time_sum = time.sum()
avg_speed = path_sum / time_sum

print("S = %3d км, T = %5.2f час, V = %5.2f км/ч" % (path_sum, time_sum, avg_speed))
"""

"""
import numpy as np

def get_trend(x, a):
    y = a[0] * x ** 2 + a[1] * x + a[2]
    return y

x_array = np.array([18.6, 99.9, 157.2, 219.9, 303.7, 399.6, 452.5, 528.4, 613.8, 669.7, 750.6, 816.2, 906.2])
h_array = np.array([85.7, 173.8, 196.7, 259.6, 332.5, 379.3, 414.2, 419.7, 461.3, 438.9, 447.8, 434.1, 441.4])

a = np.polyfit(x_array, h_array, 2)
h_zero = get_trend(0, a)
print("Высота, на которой стоит пушка: %6.2f м" % h_zero)

x_target = 1450
h_target = get_trend(x_target, a)
print("Высота в точке %4d м: %6.2f м" % (x_target, h_target))

delta_h = abs(51 - h_target)
if delta_h <= 0.5:
    print("Снаряд попадёт в мишень.")
else:
    print("Снаряд нее попадёт в мишень.")
"""

"""
import numpy as np

def get_trend(x, a):
    y = a[0] * x ** 2 + a[1] * x + a[2]
    return y

ox_input = input()
oy_input = input()
target_ox = float(input())
target_oy = float(input())
ox = np.array(ox_input.split(), dtype=float)
oy = np.array(oy_input.split(), dtype=float)

a = np.polyfit(ox, oy, 2)
h_zero = get_trend(0, a)
h_target = get_trend(target_ox, a)
delta_h = abs(target_oy - h_target)

if delta_h <= 0.5:
    bang = "yes"
else:
    bang = "no"

print("h0 = %6.2f, %2s" % (h_zero, bang))
"""


"""
import matplotlib.pyplot as plt
import numpy as np

def get_trend(x, a):
    y = a[0] * x ** 2 + a[1] * x + a[2]
    return y

x_array = np.array([18.6, 99.9, 157.2, 219.9, 303.7, 399.6, 452.5, 528.4, 613.8, 669.7, 750.6, 816.2, 906.2])
h_array = np.array([85.7, 173.8, 196.7, 259.6, 332.5, 379.3, 414.2, 419.7, 461.3, 438.9, 447.8, 434.1, 441.4])

a = np.polyfit(x_array, h_array, 2)
h_zero = get_trend(0, a)
print("Высота, на которой стоит пушка: %6.2f м" % h_zero)

x_target = 1450
h_target = get_trend(x_target, a)
print("Высота в точке %4d м: %6.2f м" % (x_target, h_target))

delta_h = abs(51 - h_target)
if delta_h <= 0.5:
    print("Снаряд попадёт в мишень.")
else:
    print("Снаряд нее попадёт в мишень.")
x_trend = [i for i in range(0, 1500, 10)]
y_trend = [get_trend(x, a) for x in x_trend]

plt.plot(x_array, h_array, 'go', label='положение снаряда')
plt.plot(x_trend, y_trend, '-r', label='линия тренда')

plt.plot([x_target], [h_target], 'b+', markersize=12)

plt.gca().spines["left"].set_position("zero")
plt.gca().spines["bottom"].set_position("zero")
plt.gca().spines["top"].set_visible(False)
plt.gca().spines["right"].set_visible(False)

plt.legend(loc="lower center")

plt.show()
"""

"""
import numpy as np

def line_trend(a, x):
    f = a[0] * x + a[1]
    return f

def poly_2_trend(b, x):
    f = b[0] * x ** 2 + b[1] * x + b[2]
    return f

x_array = input().split()
y_array = input().split()
x_array = np.array(x_array, dtype=float)
y_array = np.array(y_array, dtype=float)
a = np.polyfit(x_array, y_array, 1)
b = np.polyfit(x_array, y_array, 2)

line = [line_trend(a, x) for x in x_array]
poly_2 = [poly_2_trend(b, x) for x in x_array]

line_trend_error = np.abs((line - y_array) / y_array)
poly_2_error = np.abs((poly_2 - y_array) / y_array)

avg_line = np.mean(line_trend_error)
avg_poly_2 = np.mean(poly_2_error)

if avg_line == avg_poly_2:
    print("%5.3f %5.3f %5.3f" % (b[0], b[1], b[2]))
elif avg_line < avg_poly_2:
    print("%5.3f %5.3f" % (a[0], a[1]))
else:
    print("%5.3f %5.3f %5.3f" % (b[0], b[1], b[2]))
"""    

"""
import numpy as np
import numpy.linalg as alg

a = np.array([[3, 4, -2], [-2, -1, 4]])
b = np.array([[1, -3, -2, 1], [2, 4, -2, -1], [5, -2, 0, -2]])
c = np.array([[-1, 0, 2], [2, -2, 3], [0, 5, 1]])

#det_array = np.det(c)

#d = np.inv(c)

#d = np.dot(b, a)

#det_array = np.det(a)

#d =a + b

d = np.dot(c, b)
"""

import numpy as np
import numpy.linalg as alg

a = np.array([[3, 4, -2], 
              [-2, -1, 4], 
              [1, 2, 1]])
b = np.array([[1, -3, -2, 1],
              [2, 4, -2, -1],
              [5, -2, 0, -2]])
c = np.dot(a, b)
det_a = alg.det(a)
a_inv = alg.inv(a)
a_3 = np.dot(a, np.dot(a, a))
result = det_a * np.dot(a_inv, b) - 10 * np.dot(a_3, b)

print("A: \n", a)
print("B: \n", b)
print("A*B: \n", c)
print("Def(A): \n", det_a)
print("A^-1: \n", np.round(a_inv,1))
print("Result: \n", result)
