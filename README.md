# git-basic

**Arquivo criado para documentar o progresso realizado no curso.**

## Glossário:

* **U** > untracked (status do arquivo)

* **M** > modified (status do arquivo)

* **-f** > forçar

* **-a** > all

* **-m** > mensagem


## Comandos mais utilizados:

### 1. git init
Para iniciar um repositório, iniciar com o comando git init (no software escolhido ou GIT BASH)
O comando abaixo irá aparecer no site do GitHub, com as informações de usuário corretas.

``` echo "#nome_pasta" > README.md   
git init   
git add README.md   
git commit -m "first commit"   
git branch -m main   
git remote add origin git@github.com   
git push -u origin main 
```

### 2. git status
Comando utilizado muito frequentemente para verificar mudanças no projeto. Capaz de mapear todas as alterações, como arquivos não monitorados ou arquivados. Com ele é possível verificar quais arquivos já foram enviados para o servidor, ou salvos no projeto.   

### 3. git add
Comando para adicionar arquivos na fila, que serão enviados ao repositório no próximo ´git commit´.

### 4. git commit
Comando que captura o repositório no estado atual e atualiza o histórico do mesmo. Com esse comando é criado um identificador único.

### 5. git push
Comando para atualizar o código do servidor, com base no código local enviado.

### 6. git pull
Comando importante quando se está trabalhando em um repositório compartilhado, utilizar ele ao iniciar os trabalhos. Capaz de buscar atualizações, e se houver, unir ao código atual.

### 7. git clone
Baixa  um repositório de servidores remotos.

### 8. git rm 
Deleta arquivos da monitorização do git. Ele não terá mais atualizações consideradas pelo git, somente se forem adicionadas e commitadas novamente.  

### 9. git log
Acessar um log de modificações feitas no projeto. Recebe uma informação dos commits realizados até então.

### 10. git mv
Renomear um arquivo e/ou mover para outra pasta.

### 11. git checkout
Comando capaz de alternar entre versões de arquivos, commits ou branches.  

### 12. git ignore
Inserir um arquivo na raiz do projeto para ignorar arquivos que não devem entrar no versionamento.

### 13. git reset
Exclui alterações commitadas e/ou pendentes.

### 14. git shortlog
Log resumido do projeto.

## BRANCHES
É a forma que o git separa as versões do projeto, que geralmente se inicia na main. Normalmente novas features ficam em uma branch separada. Após as alterações serem finalizadas, os branches são unidos para o código fonte.  

```git branch (visualizar branches disponíveis)```   
```git branch nome_nova_branch (criar uma branch)```  

### 1. git checkout 
Mudar para outra branch.   

Para criar e logo em seguida mudar para essa nova branch:

```git checkout -b nome_nova_branch```    

### 2. git merge
```git merge nome```      

Unir o código de dois branches distintos. Normalmente é por meio dele que recebemos atualizações de outros desenvolvedores do projeto.

### 3. git stash
Podemos salvar as modificações atuais para prosseguir com uma outra abordagem de solução e não perder o código. Após o comando, o branch será resetado para sua versão de acordo com o repositório.  
Comandos possíveis:  
```git stash list (verificar stashs criadas)  
git stash <nome> (recuperar)  
git stash apply <número_da_stash>  
git stash show -p <nº> (mostrar modificações realizadas)
```
### 4. git tag 
```git tag -a "nome_tag" -m "mensagem"```   
Serve como checkpoint de um branch. Demarca estágios do desenvolvimento.

### 5. git push (tags)
Tags podem ser enviadas para o repositório de código e compartilhada entre devs.
```git push origin <nome_tag>
git push origin --tags (envia todas)
```

## ADMINISTRAÇÃO

### 1. git clean
Verifica e limpa arquivos untrackeds.

### 2. git gc
"Garbage collector" - identifica arquivos que não são necessários e os exclui.

### 3. git fsck
"File System Check" - verifica a integridade de arquivos.

### 4. git reflog
Mapeia todos os passos no repositório, até mudanças de branch.

### 5. git archive

## COMO CRIAR COMMITS ÚTEIS

Separar assunto do corpo da mensagem;  
Assunto com no máximo 50 caracteres;  
Letra inicial maiúscula;  
Corpo com no máximo 72 caracteres;  
Explicar o porquê e como foi realizado o commit.  

# Anotações importantes

* Utilizar comando "git pull" sempre ao iniciar o trabalho para receber atualizações da master antes de criar nova branch.

* Utilizar o comando "git push" só irá enviar arquivos add e commited.

* Utilizar "cd .." para voltar para pasta anterior

* Utilizar "git add ." para adicionar todos os arquivos.  




#### Contribuidores do projeto:

<a href="url"><img src="https://i.imgur.com/fKZak9c.jpeg" alt="Sara" width="200"/></a>  
<a href="url"><img src="https://i.imgur.com/W1pV6C6.jpeg" alt="Cecília" width="200" style="border-radius:50%"/></a>  
<a href="url"><img src="https://i.imgur.com/0eyEETU.jpeg" alt="Luna" width="200" style="border-radius:50%"></a>  
<a href="url"><img src="https://i.imgur.com/tVbxsLO.jpeg" alt="Simon" width="200" style="border-radius:50%"></a>  
<a href="url"><img src="https://i.imgur.com/19weZ0G.jpeg" alt="Lila" width="200" style="border-radius:50%"></a>  
