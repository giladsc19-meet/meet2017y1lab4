speed=int(input('Speed: '))
is_birthday=False
if is_birthday:
    print('happy birthday')
else:
    print('no birthday :(')
    if speed<31:
        print('no ticket')
    elif speed>30 and speed<51:
        print('small ticket')
    else:
        print('big ticket')
    
