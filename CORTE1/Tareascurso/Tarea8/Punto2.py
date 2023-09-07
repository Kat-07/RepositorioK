#Realice un programa que solicite al usuario el nombre de un mes del año, 
#posteriormente debe entregar el numero de dias que tiene el mes
#junto con los festivos correspondientes

def dias_del_mes():
    mes=input('Por favor, ingrese un mes del año')

    while mes in ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']:
        if mes in ['enero','marzo','mayo','julio','agosto','octubre','diciembre']:
            if mes=='enero':
                print(mes,'tiene 31 días')
                print('Dias festivo 1 y 9 de', mes)
                break
            elif mes=='marzo':
                print(mes,'tiene 31 días')
                print('Dia festivo: 20 de',mes)
                break
            elif mes=='mayo':
                print(mes,'tiene 31 días')
                print('Dias festivo: 1 y 22 de',mes)
                break
            elif mes=='julio':
                print(mes,'tiene 31 días')
                print('Dias festivo: 3 y 20 de',mes)
                break
            elif mes=='agosto':
                print(mes,'tiene 31 días')
                print('Dias festivo: 7 y 21', mes)
                break
            elif mes=='octubre':
                print(mes,'tiene 31 días')
                print('Dias festivo: 6 de',mes)
                break
            elif mes=='diciembre':
                print(mes,'tiene 31 días')
                print('Dias festivo:8 y 25 de',mes)
                break

        elif mes=='febrero':
            print(mes,'Tiene 28 dias')
            print('No tiene dias festivo')
            break

    
        elif mes in ['abril','junio','septiembre','noviembre']:
            if mes=='abril':
                print(mes,'tiene 30 días')
                print('Dias festivo: 2,6,7,9', mes)  
                break
            elif mes=='junio':
                print(mes,'tiene 30 días')
                print('Dias festivo:12 y 19 de',mes)
                break
            elif mes=='septiembre':
                print(mes,'tiene 30 días')
                print('no tiene dias festivo')
                break
            elif mes=='noviembre':
                print(mes,'tiene 30 días')
                print('Dias festivo: 6 y 13 de',mes)
                break

        else:
            print('error')

if __name__=="__main__":
    dias_del_mes()