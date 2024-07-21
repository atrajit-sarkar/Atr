# How to use the module Atr
## For Windows:
### Till now there are two submodule...
- Maths: Different maths topics are here....
- Telebot: Telebot Api and other useful functions are here.....

### To use the module into your project do the following steps....
- open cmd and type the following:
```cmd
C:\Users\atraj>where python
```
and hit enter.\
The out put will be something as follows:
```cmd
C:\Users\atraj>where python
D:\downloads\Python\python.exe
C:\Users\atraj\AppData\Local\Microsoft\WindowsApps\python.exe

C:\Users\atraj>
```
Then open powershell and do the following:
```shell
PS C:\Users\atraj> cd D:\downloads\Python
PS D:\downloads\Python> git clone https://github.com/atrajit-sarkar/Atr.git
```
After hitting enter you now can use Atr module in your projects........

## Important Note:
### The directory shown above after typing 
```cmd
C:\Users\atraj>where python
```
### Are two namely, D:\downloads\Python\python.exe
### C:\Users\atraj\AppData\Local\Microsoft\WindowsApps\python.exe in my case. 
### In your case you also have to set the path that is not same as the second path as in my case. This path will be always same for every pc.

## How to use Atr in your .py file....
### Creat a .py file in your favourite IDE. and type the following....
```python
from Atr.Maths import numbertheory as nt

print(f"The GCD(12,16) is {nt.gcd(12,16)}")
```
### Similaly you can use the following also
```python
from Atr.Maths import linear_alg as la
from Atr.Maths import switch 
from Atr.Telebot import TELEBOT_API
# All the modules docs are given in their readme files that you always can read from their corresponding folders.
```

## For Linux:
```bash
atrajit@Atrajit:~$ sudo su
[sudo] password for atrajit:
root@Atrajit:/home/atrajit# ls
Insta-Cypher  SocialMediaHackingToolkit  hydra.restore  main.py  myC  password.txt
root@Atrajit:/home/atrajit# mkdir myPython
root@Atrajit:/home/atrajit# ls
Insta-Cypher  SocialMediaHackingToolkit  hydra.restore  main.py  myC  myPython  password.txt
root@Atrajit:/home/atrajit# cd myPython/
root@Atrajit:/home/atrajit/myPython# git clone https://github.com/atrajit-sarkar/Atr.git
Cloning into 'Atr'...
remote: Enumerating objects: 12, done.
remote: Counting objects: 100% (12/12), done.
remote: Compressing objects: 100% (10/10), done.
remote: Total 12 (delta 0), reused 12 (delta 0), pack-reused 0
Receiving objects: 100% (12/12), done.
root@Atrajit:/home/atrajit/myPython# ls
Atr
root@Atrajit:/home/atrajit/myPython# nano main.py
root@Atrajit:/home/atrajit/myPython# python3 main.py
The GCD(12,16) is 4
root@Atrajit:/home/atrajit/myPython#
```

### Happy Coding and learning......