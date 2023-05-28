class Policial:
    def __init__(self,nome,nomeDeGuerra,sessao,rg,habilitacao):
        self.nome = nome
        self.nomeDeGuerra = nomeDeGuerra
        self.posto_graduacao = self.fun_posto_graduacao()
        self.sessao = sessao
        self.rg =int(rg)
        self.habilitacao = habilitacao

    def fun_posto_graduacao(self):

        self.posto_graduacao = None
        self.op_posto_graduacao = True

        while self.op_posto_graduacao == True:
            print(f'---- Escolha Posto ou Graduação do Policial: {self.nomeDeGuerra} ----')
            print("""
                [1] Oficial
                [2] Praça                          
            
            """)
            self.posto_graducao = input('---- Qual opção desejada ? ---- ')
            self.op_posto_graduacao  = False

            if self.posto_graduacao == '1':
               print(self.posto_graduacao)
            #Aqui esta retornando NONE
            print(f'FIM --- Opaçao escolhida {self.posto_graduacao}')

pm = Policial('ziwert', 'ziwert', 'furriel',111111, 'B')  
print(pm.posto_graducao) 

#pm.posto_graduacao()

     
