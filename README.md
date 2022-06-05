# Random Color CLI

 **LE SCRIPT EST ENTRAIN D'ÊTRE RECODER EN DART POUR UNE PLUS LARGE COMPATIBILITÉ, UNE EXECUTION RAPIDE ET MOINS DE BUG.**
 
 --Date de sortie prévue : Ce weekend--

## 🔍 Aperçu 🔍


https://user-images.githubusercontent.com/79168733/165066342-ad345ae2-748e-4738-8faa-2f402236d5a3.mov

 * Le programme a été lancer sur iTerm2 sous macOS Catalina.

___
## 💻 Compatibilité 💻


 ### ** Mac** :
 - iTerm2 ✅
 - VSC ✅
 - Hyper ✅ 
 - IntelliJ ✅ 
 - Terminal System 🟧 Presque inutilisable trop de couleurs qui ne s'affichent pas. 

 ### **🐧 Linux** :
- VSC ✅
- Hyper ✅
- Terminal System ✅

 ### **🪟 Windows 10** :
- IntelliJ ✅ Changement de couleurs un petit peu plus lent que sur les autres systèmes.
- VSC 🟨 Utilisable mais problème de lenteur
- Hyper 🟨 Utilisable mais problème de lenteur
- cmd ❌
- Powershell ❌
- Windows Terminal ❌

\
 Si vous trouvez d'autres terminaux qui sont compatibles\incompatibles faites le nous savoir
___
## 📦 Comment installer et lancer Random Color CLI
\
**Avec Homebrew**\
`brew tap el2zay/randomcolor` \
`brew install randomcolor`\
 AVERTISSEMENT : **Prend beaucoup de temps à se lancer. Si vous êtes sur mac et que vous n'avez pas activer la serveillance de l'entrée descendez un peu pour savoir comment l'activer.**

\
**Avec python3**
Requis : pip et python3 
- Installez le requirements.txt à l'aide de la commande `pip install -r requirements.txt`. Attention vérifiez que vous êtes dans le dossier où se trouve le main.py et le requirements.txt
- Lancez le script à l'aide la commande `python3 main.py` sur macOS et Linux. Ou la commande `python main.py` si vous êtes sur Windows.

> Si vous êtes sur macOS testez le code. Si vous n'arrivez pas à changer de couleur à l'aide de la touche espace vous devez faire 3 choses en plus qui sont très simple.

Allez dans Menu Pomme > Préférences Système

Allez dans "Sécurité et Confidentialité"
![dz nuizdnxeiz,d](https://user-images.githubusercontent.com/79168733/165068097-f66dae94-4371-4f5a-9c17-583a7d898670.png)

Puis dans Confidentialité
\
![image](https://user-images.githubusercontent.com/79168733/165068536-a136266d-e20c-4c79-a13a-08a5f608e7a3.png)
              Puis dans Surveillance de l'entrée 
\
![Capture d’écran 2022-04-25 à 09 23 56](https://user-images.githubusercontent.com/79168733/165068644-eff80770-5bc1-4c27-acf4-40166feb30a7.png)
\
Cliquez sur le cadena en bas puis mettez votre mot de passe utilisateur/administrateur
\
Une fois le cadena déverouiller cochez le terminal que vous utilisez pour le CLI (iTerm dans mon cas)
![Capture d’écran 2022-04-25 à 09 24 09](https://user-images.githubusercontent.com/79168733/165069044-1224e8fc-5703-4dde-a7d5-b89a851da0cc.png)

\
Si votre Terminal ne s'affiche pas cliquez sur le + puis cherchez votre terminal.
\
Une fois effectuer vous pouvez relancer le script à l'aide de la commande `python3 main.py`

> Si vous n'avez pas réussi à lancer le script ouvrez une issue et expliquez votre problème.
___
## 🐞 Bugs Reportés 🐞
- Inquirer et Pynput non fonctionnel sur quasi tous les terminaux Windows

> Si vous avez trouvé un autre bug faites le moi savoir via les Issues.
> Des fois impossible de quitter le RGB to HEX.

___
## 🔜 Prochainement 🔜
- Compatibilité Windows et Terminal System pour macOS
- Plus besoin de changer les paramètres d'entrée de clavier macOS.
- Plus rapide et optimisé
- Full English support
- Installable depuis pip/brew/apt
___
## 👨‍💻 Auteurs et collaborateurs 👩‍💻 
[el2zay](https://github.com/el2zay) Créateur - Seul développeur actif
