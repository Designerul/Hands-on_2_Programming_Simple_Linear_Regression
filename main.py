import numpy as np

class Dataset:
    def __init__(self):
        self.advertising = [23, 26, 30, 34, 43, 48, 52, 57, 58]
        self.sales = [651, 762, 856, 1063, 1190, 1298, 1421, 1440, 1518]

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

    print(f"Ecuación de regresión: Sales = {beta_1} * Advertising + {beta_0}")

    # Bucle para predicciones
    while True:
        rest = int(input("¿Deseas ingresar un valor a predecir? 1 = sí, 2 = no: "))
        if rest == 2:
            break
        elif rest == 1:
            vAd = float(input("Ingrese el valor de Advertising para predecir las ventas: "))
            solucion = predict(beta_1, beta_0, vAd)
            print(f"Predicción de Sales para Advertising de {vAd} millones: {solucion} millones")
        else :
            print("Entrada no válida.")

if __name__ == "__main__":
    main()
