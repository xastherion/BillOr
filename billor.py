#   BILLS_ORGANIZER
import os, shutil, time, datetime
from tkinter import Label, Entry, Button, Tk, Checkbutton, StringVar, IntVar, Spinbox, OptionMenu
from datetime import datetime

# -------------
master = Tk()
master.title('Bills-Organizer - Rechnung Eingabe')
master.geometry('500x520')    # breite-X-hohe x,y
# GEOMETRIE  ##########################################
alt = '30'    # alt estandar para cada boton, entrada o etiqueta
alt2 = '25'   # alto para las etiquetas
anch = ['100', '300', '150']       # anch para etiquetas y botones
dist_hor = ['30', '160', '290']    # distancias entre columnas
dist_ver = ['030', '060', '090', '120', '150',
            '180', '210', '240', '270', '300',
            '330', '360', '390', '420', '450',
            '480']  # dist lineas
msgs = {'msg_leer': '***',
        'msg_format': 'Falsches Format, bitte engeben YYYY-MM-DD',
        'msg_nodatum': 'Einkaufsdatum ist leer, ich übernehme Heute',
        'msg_fileimp': 'file.pdf importiert, Quell-Datei ist gelöscht!',
        'msg_keinimp': 'für diese Rechnung wurde keine PDF-Datei importiert!',
        'msg_pdfimp': 'PDF-Datei importiert, Quelle NICHT gelöscht!',
        'msg_clean': ' ########################################### '}
# Listen von valide datum
tagen = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '28', '29', '30', '31']
monaten = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
jahren = ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023',
          '2024', '2025', '2026', '2027', '2028', '2029', '2030', '2031']
# END GEOMETRIE  ##########################################


def ordner_mounten():
    os.system("sudo mount -t smbfs //user@server.pfad.edu/home ./ideep")
    os.system("open ~/Desktop")



def etiketten():
    # RECHNUNG
    Label(master, text='RECHNUNG').place(x=dist_hor[0], y=dist_ver[0], width=anch[0], height=alt2)
    Label(master, text='Rechnungsnr', bg = "grey").place(x=dist_hor[0], y=dist_ver[1], width=anch[0], height=alt2)
    Label(master, text='Einkaufdatum', bg = "grey").place(x=dist_hor[0], y=dist_ver[2], width=anch[0], height=alt2)
    Label(master, text='Lieferant', bg = "grey").place(x=dist_hor[0], y=dist_ver[3], width=anch[0], height=alt2)
    Label(master, text='Bemerkung', bg = "grey").place(x=dist_hor[0], y=dist_ver[4], width=anch[0], height=alt2)
    Label(master, text='Rechngspfad', bg = "grey").place(x=dist_hor[0], y=dist_ver[5], width=anch[0], height=alt2)
    # ARTIKEL
    Label(master, text='ARTIKEL').place(x=dist_hor[0], y=dist_ver[7], width=anch[0], height=alt2)
    Label(master, text='Name', bg = "grey").place(x=dist_hor[0], y=dist_ver[8], width=anch[0], height=alt2)
    Label(master, text='Preis', bg = "grey").place(x=dist_hor[0], y=dist_ver[9], width=anch[0], height=alt2)
    Label(master, text='Menge', bg = "grey").place(x=dist_hor[0], y=dist_ver[10], width=anch[0], height=alt2)
    eingaben_rech()
    # BUTTONS
    # Button(master, text='Validieren', command=validation).place(x=30, y=dist_ver[12], width=anch[0], height=alt)


def eingaben_rech():  # ENTRYS RECHNUNG ###################################### Entry rechnungsnummer
    global var_rnummer, var_ekdatum_d, var_ekdatum_m, var_ekdatum_j, var_ekdatum, var_liefnt, var_bemerkg, \
           var_rgnpfad, var_brutto, var_ekdatum2filename, \
           entry_rnummer, entry_ekdatum, entry_liefnt, entry_bemerkg, entry_rgnpfad, chkbutton_brutto
    var_rnummer = StringVar()
    var_ekdatum_d = StringVar(value='00')
    var_ekdatum_m = StringVar(value='00')
    var_ekdatum_j = StringVar(value='0000')
    var_ekdatum = StringVar()
    var_liefnt = StringVar()
    var_bemerkg = StringVar()
    var_rgnpfad = StringVar(value='n')
    var_brutto = StringVar()
    var_ekdatum2filename = StringVar()

    entry_rnummer = Entry(master, textvariable=var_rnummer).  place(x=dist_hor[1], y=dist_ver[1], width=anch[1], height=alt)
    Entry(master, textvariable=var_ekdatum_d).place(x=160, y=dist_ver[2], width=30, height=alt)
    Entry(master, textvariable=var_ekdatum_m).place(x=190, y=dist_ver[2], width=30, height=alt)
    Entry(master, textvariable=var_ekdatum_j).place(x=220, y=dist_ver[2], width=60, height=alt)

    entry_liefnt = Entry(master, textvariable=var_liefnt).place(x=dist_hor[1], y=dist_ver[3], width=anch[1], height=alt)
    entry_bemerkg = Entry(master, textvariable=var_bemerkg).place(x=dist_hor[1], y=dist_ver[4], width=anch[1], height=alt)
    entry_rgnpfad = Entry(master, textvariable=var_rgnpfad).place(x=dist_hor[1], y=dist_ver[5], width=anch[1], height=alt)
    chkbutton_brutto = Checkbutton(master, text='Brutto Preise (Standard Netto)', variable=var_brutto).place(x=dist_hor[1], y=dist_ver[6])

    Button(master, text='Exit ohne speicher', command=ende).                place(x=320, y=dist_ver[12], width=anch[2], height=alt)
    Button(master, text='Import Rechnung', command=pdfrechnungsfile_import).place(x=150, y=dist_ver[13], width=anch[2], height=alt)
    Button(master, text='Clipboard kopieren', command=ende).                place(x=320, y=dist_ver[14], width=anch[2], height=alt)
    Button(master, text='Ordner mounten', command=ordner_mounten).          place(x=150, y=dist_ver[15], width=anch[2], height=alt)
    eingaben_art()


def eingaben_art():     # accept entrys and delete olds entrys
    global entry_name, entry_preis, entry_menge, var_name, var_preis, var_menge
    var_name = StringVar(master, value='')
    var_preis = StringVar(master, value='')
    var_menge = StringVar(master, value='')
    entry_name = Entry(master, textvariable=var_name). place(x=dist_hor[1], y=dist_ver[8], width=anch[1], height=alt)
    entry_preis = Entry(master, textvariable=var_preis).place(x=dist_hor[1], y=dist_ver[9], width=anch[1], height=alt)
    entry_menge = Entry(master, textvariable=var_menge).place(x=dist_hor[1], y=dist_ver[10], width=anch[1], height=alt)
    Button(master, text='Speicher & Weiter', command=weitere_art).place(x=150, y=dist_ver[12], width=anch[2], height=alt)


def weitere_art():
    validation()
    schreiben()
    eingaben_art()

def validation():
    print(var_ekdatum_d.get(), var_ekdatum_m.get(), var_ekdatum_j.get())
    if (var_ekdatum_d.get() in tagen) and (var_ekdatum_m.get() in monaten) and (var_ekdatum_j.get() in jahren):
        print("korrekte tag, monat und jahr")

    if var_ekdatum.get() == "00.00.0000" :         # wenn keine EKDatum nehmt heute
        Label(master, text=msgs['msg_nodatum']).place(x=dist_hor[0], y=dist_ver[14], width=anch[1], height=alt)
        heute = time.strftime("%Y-%m-%d")
        var_ekdatum.set(heute)
    else:               # wenn EKDatum ist eingegeben, überprüft
        try:
            datum = (str(datetime.strptime(var_ekdatum.get(), "%Y-%m-%d"))).replace(" 00:00:00", '')
            var_ekdatum.set(datum)
            Label(master, text=msgs['msg_leer']).place(x=dist_hor[0], y=dist_ver[14], width=anch[1], height=alt)
        except ValueError:
            Label(master, text=msgs['msg_format']).place(x=dist_hor[0], y=dist_ver[14], width=anch[1], height=alt)

def schreiben():        # Schreibt alle vars in lista und lista in archivo
    global var_ekdatum2filename
    try:
        var_ekdatum2filename.set(var_ekdatum_j.get() + '-' + var_ekdatum_m.get() + '-' + var_ekdatum_d.get())
        var_ekdatum.set(var_ekdatum_d.get() + "." + var_ekdatum_m.get() + "." + var_ekdatum_j.get())
    except:
        Label(master, text=msgs['msg_format']).place(x=dist_hor[0], y=dist_ver[14], width=anch[1], height=alt)

    print(var_ekdatum.get(), var_ekdatum2filename.get())
    lista = [var_rnummer.get(), ';', var_ekdatum.get(), ';', var_liefnt.get(), ';', var_bemerkg.get(), ';',
             var_name.get(), ';', var_preis.get(), ';', var_menge.get(), '\n']
    archivo = open('rechnungen.csv', 'a')
    archivo.write("\t".join(lista))
    pdfrechnungsfile_import()


def pdfrechnungsfile_import():  # 3 Möglichkeiten: "n" importiert nichts, "s" importiert file.pdf und Pfadname importiert diese File
    global pdfname_ziel, var_rgnpfad
    pdfname_ziel = (var_ekdatum.get() + "-" + var_liefnt.get() + "-" + var_bemerkg.get() + ".pdf").replace('\t', '')
    if var_rgnpfad.get() == 's':
        var_rgnpfad.set('file.pdf')  # <-- beachtet auf Linux / Windows slash/backslash
        shutil.copyfile(var_rgnpfad.get(), pdfname_ziel)  # kopiert von Ziel
        os.remove(var_rgnpfad.get())  # lösch der Ziel
        Label(master, text=msgs['msg_fileimp']).place(x=dist_hor[0], y=dist_ver[14], width=anch[1], height=alt)
    elif var_rgnpfad.get() == 'n':
        Label(master, text=msgs['msg_keinimp']).place(x=dist_hor[0], y=dist_ver[14], width=anch[1], height=alt)
    else:
        shutil.copyfile(var_rgnpfad.get(), pdfname_ziel)
        Label(master, text=msgs['msg_pdfimp']).place(x=dist_hor[0], y=dist_ver[14], width=anch[1], height=alt)


def ende():  # esta funcion terminatodo con el boton "Exit"
    master.destroy()


etiketten()         # baut die fenster mit die notwendige etiketten

master.mainloop()   # 05.03.2019
