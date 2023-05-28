class Escala:
    def __init__(self, tipo_escala):
        self.tipo_escala = self.fun_escala() #não esta retornando valor
        self.horario_escolhido = self.escolher_horario()

    def fun_escala(self):
        self.funcao = None
        self.op_funcao = True

        while self.op_funcao == True:
            print('------Escolha uma das opções abaixo: --------')
            print("""
                [1] RPA
                [2] Atendente 
                [3] Ajunto
                [4] Sala de Rádio
                [5] Furriel
                [6] ROTAM
                [7] CPU
                [8] Rancho
                [9] Motorista Dia            
            
            """)
            self.funcao = input('---- Qual opção desejada ? ---- ')
            self.op_funcao = False

            if self.funcao == '1':
                self.funcao = 'RPA'
                #return self.funcao
            elif self.funcao == '2':   
                self.funcao = 'Atendente'
            elif self.funcao == '3': 
                self.funcao = 'Ajunto'
            elif self.funcao == '4': 
                self.funcao = 'Sala de Rádio'  
            elif self.funcao == '5': 
                self.funcao = 'Furriel'             
            elif self.funcao == '6': 
                self.funcao = 'ROTAM' 
            elif self.funcao == '7': 
                self.funcao = 'CPU' 
            elif self.funcao == '8': 
                self.funcao = 'Rancho' 
            
            else: 
                self.funcao = 'Motorista Dia'     
                
            
                

            print(f'FIM FUNCAO  aaaaa  {self.funcao}')

    def escolher_horario(self):
        self.horario_func = None
        self.opcao_horario = True

        while self.opcao_horario == True:
            print(f'-----ESCOLHA horarios para: {self.tipo_escala}------')
            print("""
                [1] 06H00 - 18h00
                [2] 07h00 - 19h00
                [3] 18h00 - 06h00
                [4] 19h00 - 07h00
                [5] 10h00 - 10h00
                [6] 08h00 - 11h30 /13h30 - 17h30
                [7] 08h00 - 11h30 / 13h30 - 16h00
                [8] 08h00 - 12h00 
            """)
            self.horario_func = input('---- Qual horario desejado ? ---- ')
            self.opcao_horario = False

            if self.horario_func == '1':
                self.horario_func = '06H00 - 18h00'
                #return '06H00 - 18h00'
            elif self.horario_func == '2':
                self.horario_func = '07h00 - 19h00'
                #return '07h00 - 19h00'
            elif self.horario_func == '3':
                self.horario_func = '18h00 - 06h00'
                #return '18h00 - 06h00'
            elif self.horario_func == '4':
                self.horario_func = '19h00 - 07h00'
                #return '19h00 - 07h00'
            elif self.horario_func == '5':
                self.horario_func = '10h00 - 10h00'
                #return '10h00 - 10h00'
            elif self.horario_func == '6':
                self.horario_func = '08h00 - 11h30 / 13h30 - 17h30'
                #return '08h00 - 11h30 / 13h30 - 17h30'
            elif self.horario_func == '7':
                self.horario_func = '08h00 - 11h30 / 13h30 - 16h00'
                #return '08h00 - 11h30 / 13h30 - 16h00'
            else:
                self.horario_func = '08h00 - 12h00'
                #return '08h00 - 12h00'
        print('FIM hoario')

# Criando uma instância da classe Escala
escala = Escala('rpa')

print(f' esta retornado {escala.funcao} e horario {escala.horario_func}')
print('------')
print(escala.tipo_escala)