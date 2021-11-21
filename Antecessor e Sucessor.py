n = int(input('Digite um número: '))

print('\n#Com váriaveis#\n')
an = n - 1
su = n + 1
print('O valor era {}, seu antecessor é {} e seu sucessor é {}'.format(n,an,su))

print('\n#Sem váriaveis#\n') #Assim últiliza menos memoria
print('O valor era {}, seu antecessor é {} e seu sucessor é {}'.format(n,(n-1),(n+1)))
