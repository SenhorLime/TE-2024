import csv
import tkinter as tk
from tkinter import END, ttk
from typing import Dict, List


class CarsManager:
    def __init__(self):
        self.carsList: List[Dict] = list()

        self.loadCars()

    def loadCars(self):
        for index, car in enumerate(open("carros.csv", mode="r").readlines()[1:]):
            car = car.strip().split(",")
            self.carsList.append(
                {
                    "id": car[0],
                    "fabricante": car[1],
                    "modelo": car[2],
                    "ano": car[3],
                    "fileLine": index,
                }
            )

    def editCar(self, fileIndex: int, newData: Dict):
        self.carsList[fileIndex].update(newData)
        self.saveCars()

    def saveCars(self):
        with open("carros.csv", mode="w", newline="") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(["id", "fabricante", "modelo", "ano"])

            for car in self.carsList:
                writer.writerow(
                    [car["id"], car["fabricante"], car["modelo"], car["ano"]]
                )


class App:
    def __init__(self):
        # Define um dicionario de labels e entries
        self.labels: Dict[str, ttk.Label] = dict()
        self.entries: Dict[str, ttk.Entry] = dict()
        self.buttons: Dict[str, ttk.Button] = dict()

        # Configurando a janela
        self.root = tk.Tk()
        self.root.title("Lista de Carros")
        self.frame = ttk.Frame(self.root, padding="20").grid()

        # Classe para armazenar, acessar e alterar os dados dos carros
        self.carsManager = CarsManager()

        # Variavel de controle da paginacao
        self.pageIndex = 0

    def mainLoop(self):
        self.loadLabels()
        self.loadEntries()
        self.loadButtons()

        self.root.mainloop()

    def loadLabels(self):
        self.labels.update(
            {
                "id": ttk.Label(self.frame, text="ID:").grid(
                    row=0, column=0, padx=10, pady=5, sticky="e"
                ),
                "fabricante": ttk.Label(self.frame, text="Fabricante:").grid(
                    row=1, column=0, padx=10, pady=5, sticky="e"
                ),
                "modelo": ttk.Label(self.frame, text="Modelo:").grid(
                    row=2, column=0, padx=10, pady=5, sticky="e"
                ),
                "ano": ttk.Label(self.frame, text="Ano:").grid(
                    row=3, column=0, padx=10, pady=10, sticky="e"
                ),
            }
        )

    def loadEntries(self):
        self.entries.update(
            {
                "id": ttk.Entry(self.frame),
                "fabricante": ttk.Entry(self.frame),
                "modelo": ttk.Entry(self.frame),
                "ano": ttk.Entry(self.frame),
            }
        )

        self.entries["id"].grid_configure(row=0, column=1, padx=10, pady=5)
        self.entries["fabricante"].grid_configure(row=1, column=1, padx=10, pady=5)
        self.entries["modelo"].grid_configure(row=2, column=1, padx=10, pady=5)
        self.entries["ano"].grid_configure(row=3, column=1, padx=10, pady=5)

        self.showCar(self.carsManager.carsList[0])

    def loadButtons(self):
        self.buttons.update(
            {
                "previous": ttk.Button(
                    self.frame, text="<<", command=self.previousCar
                ).grid_configure(row=4, column=0, padx=10, pady=10),
                "next": ttk.Button(
                    self.frame, text=">>", command=self.nextCar
                ).grid_configure(row=4, column=3, padx=10, pady=10),
                "edit": ttk.Button(
                    self.frame, text="Editar", command=self.editCar
                ).grid_configure(row=4, column=1, padx=10, pady=10),
                "save": ttk.Button(
                    self.frame, text="Salvar", command=self.saveEditedCar
                ).grid_configure(row=4, column=2, padx=10, pady=10),
            }
        )

    def editCar(self) -> Dict:
        self.setEntriesState(True)

        newCarData = {
            "id": self.entries["id"].get(),
            "fabricante": self.entries["fabricante"].get(),
            "modelo": self.entries["modelo"].get(),
            "ano": self.entries["ano"].get(),
        }

        return newCarData

    def saveEditedCar(self):
        newCarData = self.editCar()
        currentCarData = self.carsManager.carsList[self.pageIndex]

        if (
            newCarData["id"] != currentCarData["id"]
            or newCarData["fabricante"] != currentCarData["fabricante"]
            or newCarData["modelo"] != currentCarData["modelo"]
            or newCarData["ano"] != currentCarData["ano"]
        ):
            self.carsManager.editCar(currentCarData["fileLine"], newCarData)

        self.setEntriesState(False)

    def clearEntries(self):
        self.entries["id"].delete(0, END)
        self.entries["fabricante"].delete(0, END)
        self.entries["modelo"].delete(0, END)
        self.entries["ano"].delete(0, END)

    def setEntriesState(self, enable: bool):
        if enable:
            self.entries["id"].configure(state="normal")
            self.entries["fabricante"].configure(state="normal")
            self.entries["modelo"].configure(state="normal")
            self.entries["ano"].configure(state="normal")

        else:
            self.entries["id"].configure(state="readonly")
            self.entries["fabricante"].configure(state="readonly")
            self.entries["modelo"].configure(state="readonly")
            self.entries["ano"].configure(state="readonly")

    def showCar(self, carData: Dict):
        self.setEntriesState(True)
        self.clearEntries()

        self.entries["id"].insert(0, carData["id"])
        self.entries["fabricante"].insert(0, carData["fabricante"])
        self.entries["modelo"].insert(0, carData["modelo"])
        self.entries["ano"].insert(0, carData["ano"])
        self.setEntriesState(False)

    def nextCar(self):
        self.pageIndex += 1

        if self.pageIndex >= len(self.carsManager.carsList):
            self.pageIndex -= 1

        self.showCar(self.carsManager.carsList[self.pageIndex])

    def previousCar(self):
        self.pageIndex -= 1

        if self.pageIndex < 0:
            self.pageIndex = 0

        self.showCar(self.carsManager.carsList[self.pageIndex])


App().mainLoop()
