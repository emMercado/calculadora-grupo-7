from PyQt5 import QtCore, uic, QtWidgets
import sys, math


#Cargar archivo ui
form_class = uic.loadUiType("calculadora.ui")[0]

#Operador
def operador(self,op):
  div = self.Calculo.toPlainText()
  if(validador(div)):
    nuevo = div + op
    pantalla(self,nuevo)

#Pantalla
def pantalla(self,a):
  self.Calculo.clear()
  self.Calculo.insertPlainText(a)
def history(self,a):
   self.historial.insertPlainText(a)

#validador
def validador(div):
  ultimo = div[len(div)-1]
  simbolos = "+-*/."
  encontro = True
  for i in range(len(simbolos)):
    if(simbolos[i] == ultimo):
      encontro = False
      break
  return encontro

#Calcular
def calcular(self,div):
  if (len(div)>2):
    resultado = eval(str(div))
    pantalla(self,str(resultado))
    history(self,str(resultado))
  else:
    pantalla(self,"ingrese una numero: ")

#clases
class MiVentana(QtWidgets.QMainWindow, form_class):
 def __init__(self, parent=None):
    QtWidgets.QMainWindow.__init__(self, parent)
    self.setupUi(self)
    #Listeners de Eventos de los botones de los números
    self.boton1.clicked.connect(self.click_1)
    self.boton2.clicked.connect(self.click_2)
    self.boton3.clicked.connect(self.click_3)
    self.boton4.clicked.connect(self.click_4)
    self.boton5.clicked.connect(self.click_5)
    self.boton6.clicked.connect(self.click_6)
    self.boton7.clicked.connect(self.click_7)
    self.boton8.clicked.connect(self.click_8)
    self.boton9.clicked.connect(self.click_9)
    self.boton0.clicked.connect(self.click_0)
    #Listeners de Eventos de los botones de las operaciones
    self.suma.clicked.connect(self.sumar)
    self.resta.clicked.connect(self.restar)
    self.potencia.clicked.connect(self.potenciar)
    self.division.clicked.connect(self.dividir)
    self.coma.clicked.connect(self.Coma)
    self.borrardigito.clicked.connect(self.Borrardig)
    self.limpiar.clicked.connect(self.borrar)
    self.raiz.clicked.connect(self.raizar)
    self.igual.clicked.connect(self.resultado)

#Eventos de asignación de valores al label
#Expresiones
 def borrar(self):
  self.Calculo.clear()
  self.historial.clear()

 def Borrardig(self):
  p = self.Calculo.toPlainText()
  pa = ""
  for i in range(len(p)):
    if (i == (len(p)-1)):
      pa += ""
    else:
         pa += p[i]
    pantalla(self,str(pa))

 def raizar(self):
  p = self.Calculo.toPlainText()
  r = math.sqrt(float(p))
  pantalla(self,str(r))

 def resultado(self):
  self.historial.insertPlainText('=');
  div = self.Calculo.toPlainText()
  calcular(self,div)

  #Numeros
 def click_1(self):
    self.Calculo.insertPlainText('1')
    self.historial.insertPlainText('1')
 def click_2(self):
    self.Calculo.insertPlainText('2')
    self.historial.insertPlainText('2')
 def click_3(self):
    self.Calculo.insertPlainText('3')
    self.historial.insertPlainText('3')
 def click_4(self):
    self.Calculo.insertPlainText('4')
    self.historial.insertPlainText('4')
 def click_5(self):
    self.Calculo.insertPlainText('5')
    self.historial.insertPlainText('5')
 def click_6(self):
    self.Calculo.insertPlainText('6')
    self.historial.insertPlainText('6')
 def click_7(self):
    self.Calculo.insertPlainText('7')
    self.historial.insertPlainText('7')
 def click_8(self):
    self.Calculo.insertPlainText('8')
    self.historial.insertPlainText('8')
 def click_9(self):
    self.Calculo.insertPlainText('9')
    self.historial.insertPlainText('9')
 def click_0(self):
    self.Calculo.insertPlainText('0')
    self.historial.insertPlainText('0')
#simbolos
 def sumar(self):
  self.Calculo.insertPlainText('+');
  self.historial.insertPlainText('+');
 def restar(self):
  self.Calculo.insertPlainText('-');
  self.historial.insertPlainText('-');
 def potenciar(self):
  self.Calculo.insertPlainText('*');
  self.historial.insertPlainText('*');
 def dividir(self):
  self.Calculo.insertPlainText('/');
  self.historial.insertPlainText('/');
 def Coma(self):
  self.Calculo.insertPlainText('.');
  self.historial.insertPlainText('.');

app = QtWidgets.QApplication(sys.argv)
MyWindow = MiVentana(None)
MyWindow.show()
app.exec_()