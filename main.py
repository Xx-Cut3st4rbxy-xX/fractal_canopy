import turtle as trl
def fractal_canopy(repeat, lenght, angle):
    trl.down()
    if repeat == 0:
        return "Error! Podaj prawidłowy stopień."
    trl.width(repeat)
    trl.forward(lenght)
    trl.left(angle)
    fractal_canopy(repeat - 1, lenght / 2, angle)
    trl.right(angle * 2)
    fractal_canopy(repeat - 1, lenght / 2, angle)
    trl.left(angle)
    trl.backward(lenght)
trl.up()
trl.left(90)
r3peat = input("Enter the number of repeats: ")
l3nght = input("Enter the lenght of the main line (mm): ")
angl3 = input("Enter the angle between branches (°): ")
r3peat = int(r3peat)
l3nght = int(l3nght)
angl3 = int(angl3)
fractal_canopy(r3peat, l3nght, angl3)
trl.mainloop()