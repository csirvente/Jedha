#!/usr/bin/env python
# coding: utf-8

# In[1]:


def retour_capital(capital_i, interet, nb_annee):
    return capital_i*(1 + (interet/100))**nb_annee


# In[8]:


def question(arg):
    while True:
        try:
            value = float(input(arg))
            while value < 0:
                print("Veuillez rentrer un nombre positif")
                value = float(input(arg))
        except:
            print("Veuillez rentrer un nombre decimal")
            continue
        break
    return value


capital_i = question("Quel est votre capital investi")
interet = question("Quel est votre taux d'interet?")
nb_annee = question("En combien d'annee souhaitez vous investir")
invest_return = str(round(retour_capital(capital_i, interet, nb_annee), 2))
print("Votre retour sur investissement est de {} euros".format(invest_return))


# TODO LIST

# In[20]:


# verifier que la variable est defini
try:
    todo_list
except NameError:
    todo_list = None

# Test whether variable is defined to be None
if todo_list is None:
    todo_list = []
else:
    print(todo_list)

if input("voulez vous ajouter une element a votre todo? O/N") == "O":
    todo_list.append(input("Que voulez vous ajouter a votre to do?"))
print(todo_list)
if input("voulez vous supprimer un element de votre todo? O/N") == "O":
    value = int(input("Quel element voulez vous supprimer?"))-1
    todo_list.pop(value)
print(todo_list)


# In[ ]:


# In[ ]:
