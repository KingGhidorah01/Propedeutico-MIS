mas_grande = None
print("Antes:", mas_grande)
for iterval in [3, 41, 12, 9, 74, 15]:
    if mas_grande is None or iterval > mas_grande:
        mas_grande = iterval
    print("Loop:", iterval, mas_grande)
print('El más grande:', mas_grande)
