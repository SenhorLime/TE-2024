class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
    
  def funcao(qualquer_coisa):
    print("Ola, meu nome e " + qualquer_coisa.nome) 
    
  def __str__(self):
    return f"{self.nome} ({self.idade})"
  
pl = Pessoa("Joao", 36)
pl.funcao()
print(pl)