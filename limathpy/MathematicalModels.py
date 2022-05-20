#File to Numerical analysis 
from sympy import plot, symbols, Function, Eq, Derivative, dsolve, solve
from matplotlib import pyplot as plt
from celluloid import Camera
from IPython.display import HTML
import numpy as np

def sistem(matriz):
    """Given a list of lists, a system of differential equations returns."""
    t = symbols('t')
    x, y = symbols('x y', cls=Function)
    eq1 = Eq(Derivative(x(t), t), matriz[0][0]*x(t) + matriz[0][1]*y(t))
    eq2 = Eq(Derivative(y(t), t), matriz[1][0]*x(t) + matriz[1][1]*y(t))
    sols = dsolve((eq1, eq2))
    return sols[0].rhs, sols[1].rhs

def linear_system(matriz, cond_inic):
    """Given a system of differential equations, the linear system returns to t=0."""
    t = symbols('t')
    x, y = symbols('x y', cls=Function)
    sols = sistem(matriz)

    lineal1 = Eq(sols[0].subs({t:0}), cond_inic[0])
    lineal2 = Eq(sols[1].subs({t:0}), cond_inic[1])
    return lineal1, lineal2

def sistema_ed(matriz, cond_inic):
    """Given a matrix and initial conditions, the solution of the differential equation system returns."""
    t = symbols('t')
    x, y = symbols('x y', cls=Function)
    C1, C2 = symbols('C1 C2')
    sis_ed = sistem(matriz)
    sis_lin = linear_system(matriz, cond_inic)
    dict_sols = solve(sis_lin)
    expr1 = sis_ed[0].subs(dict_sols)
    expr2 = sis_ed[1].subs(dict_sols)
    return expr1, expr2
    
def diagram(par, x0, it):
    Args:
        par: is a simple structured text parser project
        x0: initial condition
        it:
    def f(x):
        return par*x*(1-x)
    fig, ax = plt.subplots()
    camera = Camera(fig)
    x = [x0]
    y = [x0]
    s = np.arange(0, 1, 0.01)

    for i in range(it):
        ax.plot(s, f(s), color='blue')
        ax.plot(s, s, color='black')
        x.append(x[2*i])
        x.append(f(x[2*i]))
        y.append(f(y[2*i]))
        y.append(f(y[2*i]))
        ax.plot(x, y, color='red')
        camera.snap()
    return camera.animate()    

def f(x):
    return 3.8*x*(1-x)
vals=[0.3]
iterations=50
for i in range(iterations):
    new = vals[-1]
    vals.append(f(new))
vals

fig, ax = plt.subplots(figsize=(10, 5))
x = range(len(vals))
ax.bar(x, vals)