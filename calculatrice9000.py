import tkinter as tk


calcul=""
# ajouter les calcules
def ajout_calcule(symbol):
    global calcul
    calcul+=str(symbol)
    text_resultat.delete(1.0,"end")
    text_resultat.insert(1.0,calcul)

    calcul +=str(pow)
    text_resultat.delete(1.0,"end")
    text_resultat.insert(1.0, calcul)




def eval_calcul():
    global calcul
    try:
        calcul=str(eval(calcul))
        text_resultat.delete(1.0,"end")
        text_resultat.insert(1.0,calcul)
        
    except:
        efface_ecran()
        text_resultat.insert(1.0,"Erreur")

def efface_ecran():
    global calcul
    calcul=""
    text_resultat.delete(1.0,"end")



# création de la fenêtre
windows=tk.Tk()
windows.geometry("400x350")
windows.title("Calculatrice")
text_resultat=tk.Text(windows, height=2, width=16, font=('Arial',24 ))
text_resultat.grid(columnspan=5)

#Paramétrage des boutons de la calculette 
btn_1=tk.Button(windows,text="1", command= lambda: ajout_calcule(1),width=5,font=('Arial',14))
btn_1.grid(row=2,column=1)

btn_2=tk.Button(windows,text="2", command= lambda: ajout_calcule(2),width=5,font=('Arial',14))
btn_2.grid(row=2,column=2)

btn_3=tk.Button(windows,text="3", command= lambda: ajout_calcule(3),width=5,font=('Arial',14))
btn_3.grid(row=2,column=3)

btn_4=tk.Button(windows,text="4", command= lambda: ajout_calcule(4),width=5,font=('Arial',14))
btn_4.grid(row=3,column=1)

btn_5=tk.Button(windows,text="5", command= lambda: ajout_calcule(5),width=5,font=('Arial',14))
btn_5.grid(row=3,column=2)

btn_6=tk.Button(windows,text="6", command= lambda: ajout_calcule(6),width=5,font=('Arial',14))
btn_6.grid(row=3,column=3)

btn_7=tk.Button(windows,text="7", command= lambda: ajout_calcule(7),width=5,font=('Arial',14))
btn_7.grid(row=4,column=1)

btn_8=tk.Button(windows,text="8", command= lambda: ajout_calcule(8),width=5,font=('Arial',14))
btn_8.grid(row=4,column=2)

btn_9=tk.Button(windows,text="9", command= lambda: ajout_calcule(9),width=5,font=('Arial',14))
btn_9.grid(row=4,column=3)

btn_0=tk.Button(windows,text="0", command= lambda: ajout_calcule(0),width=5,font=('Arial',14))
btn_0.grid(row=5,column=2)

btn_open=tk.Button(windows,text="(", command= lambda: ajout_calcule("("),width=5,font=('Arial',14))
btn_open.grid(row=5,column=1)

btn_close=tk.Button(windows,text=")", command= lambda: ajout_calcule(")"),width=5,font=('Arial',14))
btn_close.grid(row=5,column=3)

btn_somm=tk.Button(windows,text="+", command= lambda: ajout_calcule("+"),width=5,font=('Arial',14))
btn_somm.grid(row=2,column=5)

btn_sous=tk.Button(windows,text="-", command= lambda: ajout_calcule("-"),width=5,font=('Arial',14))
btn_sous.grid(row=3,column=5)

btn_multi=tk.Button(windows,text="x", command= lambda: ajout_calcule("*"),width=5,font=('Arial',14))
btn_multi.grid(row=4,column=5)

btn_divi=tk.Button(windows,text="/", command= lambda: ajout_calcule("/"),width=5,font=('Arial',14))
btn_divi.grid(row=5,column=5)

btn_egal=tk.Button(windows,text="=", command= eval_calcul,width=5,font=('Arial',14))
btn_egal.grid(row=6,column=3)

btn_eff=tk.Button(windows,text="C", command= efface_ecran,width=5,font=('Arial',14))
btn_eff.grid(row=6,column=1)

btn_virg=tk.Button(windows,text=".", command= lambda: ajout_calcule("."),width=5,font=('Arial',14))
btn_virg.grid(row=6,column=2)

btn_pourc=tk.Button(windows,text="%", command= lambda: ajout_calcule("%"),width=5,font=('Arial',14))
btn_pourc.grid(row=6,column=5)

btn_racin=tk.Button(windows,text="v2", command= lambda: ajout_calcule("v2"),width=5,font=('Arial',14))
btn_racin.grid(row=3,column=6)


windows.mainloop()

