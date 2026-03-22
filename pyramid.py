import time
import turtle

jumlah = input("Jumlah: ")
ukuran = input("Ukuran: ")

try:
    jumlah = int(jumlah)
    ukuran = float(ukuran) or int(ukuran)
except ValueError:
    print("Error: Tolong masukkan angka dengan benar")
    time.sleep(1)
else:
    if jumlah <= 1 or ukuran <= 0:
        print("Error: Masukkan angka dengan benar")
        time.sleep(1)
        exit()

    t = turtle.Turtle()
    total = jumlah * ukuran

    t.right(90)
    t.up()
    t.forward(total / 2)
    t.left(90)
    t.down()
    t.forward(total - ukuran / 2)
    t.left(90)

    for i in range(jumlah):
        t.forward(ukuran)
        t.left(90)
        t.forward(ukuran)
        t.right(90)

    t.left(180)

    for i in range(jumlah - 1):
        t.forward(ukuran)
        t.right(90)
        t.forward(ukuran)
        t.left(90)

    t.forward(ukuran)
    t.left(90)
    t.forward(total - ukuran / 2 + ukuran)
    t.backward(total - ukuran / 2)

    for i in range(jumlah - 1):
        t.left(90)
        t.forward(ukuran * (i + 1))
        t.backward(ukuran * (i + 1))
        t.right(90)
        t.forward(ukuran)

    for i in range(jumlah - 1):
        t.left(90)
        t.forward(total - ukuran * (i + 1))
        t.backward(total - ukuran * (i + 1))
        t.right(90)
        t.forward(ukuran)
    
    t.left(90)
    t.pensize(2.5)

    for i in range(jumlah):
        t.forward(ukuran)
        t.left(90)
        t.forward(ukuran)
        t.forward(total * 2 - ukuran * 2 * (i + 1))
        t.backward(total * 2 - ukuran * 2 * (i + 1))
        t.right(90)

    t.left(180)

    for i in range(jumlah - 1):
        t.forward(ukuran)
        t.right(90)
        t.forward(ukuran)
        t.left(90)
    
    t.forward(ukuran)
    t.left(90)
    t.forward((total - ukuran / 2) * 2)

time.sleep(2)