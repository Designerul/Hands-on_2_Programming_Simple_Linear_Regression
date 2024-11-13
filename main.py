import numpy as np

class Dataset:
    def __init__(self):
        self.advertising = [1,2,3,4,5,6,7,8,9]
        self.sales = [2,4,6,8,10,12,14,16,18]

    def get_data_adv(self):
        return self.advertising

    def get_data_sal(self):
        return self.sales

def predict(b1, b0, aAd):
    return b1 * aAd + b0

def main():
    datos = Dataset()
    adv_data = datos.get_data_adv()
    sal_data = datos.get_data_sal()

    # Número de elementos
    n = len(adv_data)

    # Sumatorias
    sum_x = sum(adv_data)
    sum_y = sum(sal_data)
    sum_x_squ = sum(x ** 2 for x in adv_data)
    sum_xy = sum(x * y for x, y in zip(adv_data, sal_data))

    # Cálculo de los coeficientes de la regresión
    beta_1 = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squ - sum_x ** 2)
    beta_0 = (sum_y - beta_1 * sum_x) / n

    # Bucle para predicciones
    while True:
        print("************************")
        print(f"Ecuación de regresión: Sales = {beta_1} * Advertising + {beta_0}")
        print("1 - Ingresar nuevo valor")
        print("2 - Salir")
        rest = int(input("Opcion: "))
        if rest == 2:
            break
        elif rest == 1:
            vAd = float(input("Ingrese el valor predecir las ventas: "))
            solucion = predict(beta_1, beta_0, vAd)
            print(f"Predicción de Sales para Advertising: {solucion} millones")
        else :
            print("Entrada no válida.")

if __name__ == "__main__":
    main()
