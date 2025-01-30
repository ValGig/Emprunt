import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import tkinter as tk
from tkinter import messagebox
from tkinter import *
matplotlib.use('TkAgg')

def calcul_pret():
    # Calcul de la durée du prêt
    attente = np.linspace(0, 15, 16)

    try:
        prix_min = float(prix_min_entry.get())
    except ValueError:
        print("Entrée de prix min invalide.")

    try:
        prix_max = float(prix_max_entry.get())
    except ValueError:
        print("Entrée de prix max invalide.")

    prix_list = np.linspace(prix_min, prix_max, 100)

    try:
        epargne_mensuelle = float(epargne_mensuelle_entry.get())
    except ValueError:
        print("Entrée invalide dans le champ épargne mensuelle.")

    try:
        loyer = float(loyer_entry.get())
    except ValueError:
        print("Entrée invalide dans le champ loyer.")

    try:
        taux_interets = float(taux_interets_entry.get())  
    except ValueError:
        print("Entrée invalide dans le champ taux d'intérêt.")

    try:
        apport_actuel = float(apport_actuel_entry.get())  
    except ValueError:
        print("Entrée invalide dans le champ apport actuel.")
    
    try:
        revenus = float(revenus_entry.get())  
    except ValueError:
        print("Entrée invalide dans le champ apport actuel.")

    try:
        mensualite = float(mensualite_entry.get())  
    except ValueError:
        print("Entrée invalide dans le champ apport actuel.")

    costs = []
    duree_pret = []
    for prix in prix_list:
        prix = int(prix)
        cost_row = []
        duree_total_raw = []
        duree_total_raw2 = []
        for i in attente:
            i = int(i)
            apport = apport_actuel + i * 12 * epargne_mensuelle
            pret = prix - apport
            try:
                # Calcul de la durée du prêt avec gestion de l'erreur du log
                duree = (np.log(mensualite / (mensualite - pret * taux_interets / 12)) / np.log(1 + taux_interets / 12))/12
                if np.isnan(duree) :  # Vérification si la durée est négative ou "NaN"
                    raise ValueError("Durée invalide")
            except (ValueError, ZeroDivisionError, FloatingPointError):
                # Si une erreur est détectée dans le calcul du log, afficher la popup d'erreur
                messagebox.showerror("Erreur de calcul", "Certains montants sont supérieurs à la capacité d'emprunt")
                return None  # Retourne None pour éviter les calculs incorrects
            total = apport + duree * 12 * mensualite + loyer * 12 * i
            cost_row.append(total)
            duree_total_raw.append(duree)
        costs.append(cost_row)
        duree_pret.append(duree_total_raw)

    costs = np.array(costs)
    duree_pret = np.array(duree_pret)
    return costs, duree_pret, attente, prix_list, mensualite, loyer

def plot_graph(costs, duree_pret, attente, prix_list, mensualite, loyer):
    X, Y = np.meshgrid(attente, prix_list)  
    Z = costs
    Z1 = duree_pret

    fig, [ax, ax1] = plt.subplots(1, 2, figsize=(17, 7))

    contour = ax.contourf(X, Y, Z, 20, cmap='magma')  
    contour1 = ax1.contourf(X, Y, Z1, 20, cmap='magma')

    fig.colorbar(contour, ax=ax)
    fig.colorbar(contour1, ax=ax1)

    ax.set_title(f'Coût de revient du bien avec mensualités de {mensualite} Eur et loyer de {loyer} Eur')
    ax.set_xlabel('Temps d\'Attente (en années)')
    ax.set_ylabel('Prix du Bien (€)')
    ax.grid()

    ax1.set_title(f'Durée du prêt pour mensualités de {mensualite} Eur et loyer de {loyer} Eur')
    ax1.set_xlabel('Temps d\'Attente (en années)')
    ax1.set_ylabel('Prix du Bien (€)')
    ax1.grid()

    plt.tight_layout()
    plt.show()

# Fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calculateur d'emprunt")
fenetre.config(bg='#2f2f2f')

# Titre de l'application
title_label = tk.Label(fenetre, text="Calculateur d'emprunt", bg='#2f2f2f', fg='white', font=("Helvetica", 20))
title_label.grid(row=0, column=0, columnspan=3, pady=20)

# Labels et champs de saisie
field_font = ("Helvetica", 12)
label_color = '#e1e1e1'
entry_color = '#3b3b3b'
highlight_color = '#e76f51'

# Fonction pour créer des champs de saisie
def create_input(label_text, row, entry_variable):
    label = tk.Label(fenetre, text=label_text, bg='#2f2f2f', fg=label_color, font=field_font)
    label.grid(row=row, column=0, sticky='w', padx=10, pady=5)
    entry = tk.Entry(fenetre, textvariable=entry_variable, font=field_font, bg=entry_color, fg='white', relief='flat')
    entry.grid(row=row, column=1, padx=10, pady=5)
    return entry

def update_mensualite(*args):
    # Récupérer les revenus
    try:
        revenus = float(revenus_entry.get())
        mensualite_entry.set(str(0.35 * revenus))  # Mettre à jour epargne_pendant_remboursement_entry
    except ValueError:
        pass  # Si la valeur n'est pas valide, ne rien faire
        
# Création des champs d'entrée
prix_min_entry = tk.StringVar()
prix_min_field = create_input("Prix minimum du bien:", 1, prix_min_entry)

prix_max_entry = tk.StringVar()
prix_max_field = create_input("Prix max du bien:", 2, prix_max_entry)

revenus_entry = tk.StringVar() 
revenus_field = create_input("Revenus mensuels:", 3, revenus_entry)

epargne_mensuelle_entry = tk.StringVar()
epargne_mensuelle_field = create_input("Épargne mensuelle:", 4, epargne_mensuelle_entry)

mensualite_entry = tk.StringVar()
mensualite_field = create_input("Mensualité (max par defaut):", 5, mensualite_entry)

revenus_entry.trace("w", update_mensualite)

loyer_entry = tk.StringVar()
loyer_field = create_input("Loyer moyen:", 6, loyer_entry)

taux_interets_entry = tk.StringVar()
taux_interets_field = create_input("Taux d'intérêt annuel:", 7, taux_interets_entry)

apport_actuel_entry = tk.StringVar()
apport_actuel_field = create_input("Apport actuel:", 8, apport_actuel_entry)

# Boutons d'action
button_font = ("Helvetica", 14)
button_color = highlight_color

# Bouton calcul
bouton_calcul = tk.Button(fenetre, text="Lancer le calcul", command=lambda: calcul_pret(), font=button_font, bg=button_color, fg='white', relief='flat')
bouton_calcul.grid(row=9, column=0, columnspan=2, pady=20)

# Bouton plot
bouton_plot = tk.Button(fenetre, text="Tracer le graph", command=lambda: plot_graph(*calcul_pret()), font=button_font, bg=button_color, fg='white', relief='flat')
bouton_plot.grid(row=10, column=0, columnspan=2, pady=20)

fenetre.mainloop()
