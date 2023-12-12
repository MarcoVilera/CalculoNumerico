import math
class Convertion():

    def __init__(self,number):

        self.number = number
    
    def decimalTobinary(self,bits=0):
        if bits <= 0:
            return '|No se puede alojar un número binario en bits negativos|'
        
        binaryArray = []
        number = self.number

        if number == 0:
            return '0'*bits if bits > 1 else '0'
            
        while number > 0:

            binaryNumber = str(number%2)
            binaryArray.append(binaryNumber)
            finalConvert = list(reversed(binaryArray))

            number = number // 2

            result = ""
            
            for i in finalConvert:

                result += i +""
        
        if len(result) < bits:
            result = '0'*(bits-len(result)) + result

        elif len(result) > bits:
            result = result[:bits]

        return result

    def decimaToOctal(self):
        octalArray = []
        number = self.number

        while number >= 1:
            octalArray.append(str(number%8))
            number //= 8

        octalArray = octalArray[::-1]
        result = ''

        for i in octalArray:
            result += i
        return result

    def decimaltoHex(self):
        hexaDecimals = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        hex = ''
        number = self.number
        while number > 0:
            dec = number % 16
            hex = hexaDecimals[dec] + hex
            number //= 16
        return hex


number = int(input('Ingresa un numero: '))
bits = int(input('Ingresa la cantidad de bits para la conversión a binario: '))
binary = Convertion(number).decimalTobinary(bits)
octal = Convertion(number).decimaToOctal()
hexadecimal = Convertion(number).decimaltoHex()

output = 'Decimal {} | Binario {} | Octal {} | Hexadecimal {}'.format(number,binary,octal,hexadecimal)
print(output)