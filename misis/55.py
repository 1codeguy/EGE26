import turtle

def draw_line(length, angle, scale):
    """Рисует линию заданной длины под заданным углом, умножая длину на scale."""
    turtle.setheading(angle)  # Устанавливаем угол поворота
    turtle.forward(length * scale)  # Рисуем линию с учетом масштаба

def repeat_lines(length, k, c, scale):
    """Повторяет рисование линий в зависимости от параметров и масштаба."""
    if length > 0:
        for i in range(1, k + 1):
            angle = 180 - 180 * (i - 2) / i  # Вычисляем угол
            draw_line(length, angle, scale)  # Передаем масштаб в функцию рисования
            turtle.penup()
            turtle.home()  # Возвращаемся в исходную позицию
            turtle.pendown()

def main():
    turtle.speed(1)  # Устанавливаем скорость рисования
    scale = 20       # Масштаб рисунка (можно изменить для увеличения или уменьшения)
    c = 0.5          # Начальное значение c
    for k in range(1, 7):  # Цикл от 1 до 6
        draw_line(2, -60, scale)   # Рисуем линию длиной 2 под углом -60 градусов с учетом масштаба
        repeat_lines(2, k, c, scale)  # Повторяем рисование линий с учетом масштаба
        c += 0.2             # Увеличиваем значение c на 0.2

    turtle.done()  # Завершаем рисование

main()