import parallel as pa
import pipe as pi
import parallel5 as p5

def main():
    user_choise = input('Введите 1 если pipe\nВведите 2 если parallel5\nВведите 3 если parallel\nВвод:')
    if user_choise.lower() == '1':
        pi.main()
    elif user_choise.lower() == '2':
        p5.main()
    elif user_choise.lower() == '3':
        pa.main()
    else:
        print('не верно')
        main()


if __name__ == '__main__':
    main()