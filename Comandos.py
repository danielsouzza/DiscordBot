class Commands:
    def rules(self):
        try:
            rules = open("").lower()
        except :
            exception = "Arquivo de regras ainda não existe"
            return exception
    def devDoc(self):
        return {
            "/python" : "https://docs.python.org/pt-br/3/",
            "/javadoc" : "https://docs.oracle.com/javase/7/docs/api/java/lang/Object.html",
            "erro" : "Sorry!! ainda não tenho essa documentação, me ajude a melhorar colaborando com links de mais documentação"
        }


    def commands(self):
        return{
            "/github" : "Veja o github do meu criador: https://github.com/danielsouzza",
            "/dev" : "Bem vindo(a) ao mundo da programação, daqui pra frente é só pra baixo",
            "/rules" :"As regras foram feitas para ser quebradas, mas se você quebrar uma, eu te expulso o serve é meu",
            "/devdoc" : "Tá na hora de estudar, liste as documentções as principais linguagens de programação",
            "erro" : "Opa!! esse comando não exite, digite '/help' para lista todos os comandos"
        }