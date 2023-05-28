class Policial:
    def __init__(self,nome,nomeDeGuerra,sessao,rg,habilitacao):
        self.nome = nome
        self.nomeDeGuerra = nomeDeGuerra
        self.posto_graduacao = self.fun_posto_graduacao()
        self.sessao = sessao
        self.rg =int(rg)
        self.habilitacao = habilitacao

    def fun_posto_graduacao(self):

        self.posto_graducao_funcao = None
        self.op_posto_graduacao = True

        while self.op_posto_graduacao == True:
            print(f'---- Escolha Posto ou Graduação do Policial: {self.nomeDeGuerra} ----')
            print("""
                [1] Oficial
                [2] Praça                          
            
            """)
            self.posto_graducao_funcao = input('---- Qual opção desejada ? ---- ')
            self.op_posto_graduacao  = False

            if self.posto_graducao_funcao == '1':
               self.graduacao_oficial = None 
               self.op_oficial = True

               while self.op_oficial == True:
                print(f'---- Escolha Posto  do Policial: {self.nomeDeGuerra} ----')
                print("""
                [1] Coronel
                [2] Tenente-Coronel
                [3] Major
                [4] Capitão
                [5] 1º Tenente
                [6] 2º Tenente
                [7] Aspirante a Oficial     """)

                self.posto_graducao_funcao =input('Qual Opção desejada ?')
                self.op_oficial = False 

                if self.posto_graducao_funcao == '1':
                    self.posto_graducao_funcao= 'Coronel'
                elif self.posto_graducao_funcao == '2':
                    self.posto_graducao_funcao= 'Tenente-Coronel'  
                elif self.posto_graducao_funcao == '3':
                    self.posto_graducao_funcao= 'Major'                 
                elif self.posto_graducao_funcao == '4':
                    self.posto_graducao_funcao= 'Capitão'      
                elif self.posto_graducao_funcao == '5':
                    self.posto_graducao_funcao= '1º Tenente'
                elif self.posto_graducao_funcao == '6':
                    self.posto_graducao_funcao = '2º Tenente' 
                else:
                    self.posto_graducao_funcao =  'Aspirante a Oficial '    

              ##Pracas

            if self.posto_graducao_funcao == '2':
               self.graduacao_praca = None 
               self.op_praca = True

               while self.op_praca == True:
                print(f'---- Escolha Posto  do Policial: {self.nomeDeGuerra} ----')
                print("""
                [1] Subtenente 
                [2] 1º Sargento 
                [3] 2º Sargento 
                [4] 3º Sargento 
                [5] Cabo 
                [6] Soldado 
                
                    """)

                self.posto_graducao_funcao =input('Qual Opção desejada ?')
                self.op_praca = False 

                if self.posto_graducao_funcao == '1':
                    self.posto_graducao_funcao= 'Subtenente '
                elif self.posto_graducao_funcao == '2':
                    self.posto_graducao_funcao= '1º Sargento'  
                elif self.posto_graducao_funcao == '3':
                    self.posto_graducao_funcao= '2º Sargento'                 
                elif self.posto_graducao_funcao == '4':
                    self.posto_graducao_funcao= '3º Sargento'      
                elif self.posto_graducao_funcao == '5':
                    self.posto_graducao_funcao= 'Cabo'                
                else:
                    self.posto_graducao_funcao =  'Soldado'    

               
            
        print(f'FIM --- Opaçao escolhida {self.posto_graducao_funcao}')

pm = Policial('ziwert', 'ziwert', 'furriel',111111, 'B')  
 

#pm.posto_graduacao()

     
