#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By : TheDataHunter - https://github.com/TheDataHunter
# Created Date : 10/08/2022
# version ='1.0'
# status : RFU (ready for use)
# license : GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007
# copyrights : 
# ---------------------------------------------------------------------------
""" A simple Python script that looks up your Country Phone Codes """
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
from tkinter import *
from tkinter import ttk
# ---------------------------------------------------------------------------
# Dictionaries
# ---------------------------------------------------------------------------
country_dct = {
    'AFG':'93', 
    'AFG':'93', 
    'ALA':'358', 
    'ALB':'355', 
    'DZA':'213', 
    'ASM':'1', 
    'AND':'376', 
    'ANG':'244', 
    'AIA':'1', 
    'ATG':'1', 
    'ARG':'54', 
    'ARM':'374', 
    'ABW':'297', 
    'AUS':'61', 
    'AUT':'43', 
    'AZE':'994', 
    'BHS':'1', 
    'BHR':'973', 
    'BGD':'880', 
    'BRB':'1', 
    'BLR':'375', 
    'BEL':'32', 
    'BLZ':'501', 
    'BEN':'229', 
    'BMU':'1', 
    'BTN':'975', 
    'BOL':'591', 
    'BES':'599', 
    'BIH':'387', 
    'BWA':'267', 
    'BRA':'55', 
    'IOT':'246', 
    'VIR':'1', 
    'BRN':'673', 
    'BGR':'359', 
    'BFA':'226', 
    'MMR':'95', 
    'BDI':'257', 
    'KHM':'855', 
    'CMR':'237', 
    'CAN':'1', 
    'CPV':'238', 
    'CYM':'1', 
    'CAF':'236', 
    'TCD':'235', 
    'CHL':'56', 
    'CHN':'86', 
    'CXR':'61', 
    'CCK':'61', 
    'COL':'57', 
    'COM':'269', 
    'COG':'242', 
    'COD':'243', 
    'COK':'682', 
    'CRI':'506', 
    'HRV':'385', 
    'CUB':'53', 
    'CUW':'599', 
    'CYP':'357', 
    'CZE':'420', 
    'DNK':'45', 
    'DJI':'253', 
    'DMA':'1', 
    'DOM':'1', 
    'TLS':'670', 
    'ECU':'593', 
    'EGY':'20', 
    'SLV':'503', 
    'GBR':'44', 
    'GNQ':'240', 
    'ERI':'291', 
    'EST':'372', 
    'EST':'251', 
    'SWZ':'268', 
    'FLK':'500', 
    'FRO':'298', 
    'FSM':'691', 
    'FJI':'679', 
    'FIN':'358', 
    'FRA':'33', 
    'PYF':'262', 
    'PYF':'508', 
    'PYF':'590', 
    'PYF':'594', 
    'PYF':'596', 
    'GUF':'594', 
    'PYF':'689', 
    'GAB':'241', 
    'GMB':'220', 
    'GEO':'995', 
    'DEU':'49', 
    'GHA':'233', 
    'GIB':'350', 
    'GRC':'30', 
    'GRL':'299', 
    'GRD':'1', 
    'GLP':'590', 
    'GUM':'1', 
    'GTM':'502', 
    'GGY':'44', 
    'GIN':'224', 
    'GNB':'245', 
    'GUY':'592', 
    'HTI':'509', 
    'HND':'504', 
    'HKG':'852', 
    'HUN':'36', 
    'ISL':'354', 
    'IND':'91', 
    'IDN':'62', 
    'IRN':'98', 
    'IRQ':'964', 
    'IRL':'353', 
    'IMN':'44', 
    'ISR':'972', 
    'ITA':'39', 
    'CIV':'225', 
    'JAM':'1', 
    'JPN':'81', 
    'JEY':'44', 
    'JOR':'962', 
    'KAZ':'7', 
    'KEN':'254', 
    'KIR':'686', 
    'KWT':'965', 
    'KGZ':'996', 
    'LAO':'856', 
    'LVA':'371', 
    'LBN':'961', 
    'LSO':'266', 
    'LBR':'231', 
    'LBY':'218', 
    'LIE':'423', 
    'LTU':'370', 
    'LUX':'352', 
    'MAC':'853', 
    'MDG':'261', 
    'MWI':'265', 
    'MYS':'60', 
    'MDV':'960', 
    'MLI':'223', 
    'MLT':'356', 
    'MHL':'692', 
    'MTQ':'596', 
    'MRT':'222', 
    'MUS':'230', 
    'MYT':'262', 
    'MEX':'52', 
    'MDA':'373', 
    'MCO':'377', 
    'MNG':'976', 
    'MNE':'382', 
    'MSR':'1', 
    'MAR':'212', 
    'MOZ':'258', 
    'NAM':'264', 
    'NRU':'674', 
    'NPL':'977', 
    'NLD':'31', 
    'NCL':'687', 
    'NZL':'64', 
    'NIC':'505', 
    'NER':'227', 
    'NGA':'234', 
    'NIU':'683', 
    'NFK':'672', 
    'PRK':'850', 
    'MKD':'389', 
    'NOR':'47', 
    'OMN':'968', 
    'PAK':'92', 
    'PLW':'680', 
    'PSE':'970', 
    'PSE':'972', 
    'PAN':'507', 
    'PNG':'675', 
    'PRY':'595', 
    'PER':'51', 
    'PHL':'63', 
    'PCN':'64', 
    'POL':'48', 
    'PRT':'351', 
    'PRT':'239', 
    'PRI':'1', 
    'QAT':'974', 
    'REU':'262', 
    'ROU':'40', 
    'RUS':'7', 
    'RWA':'250', 
    'BLM':'590', 
    'SHN':'290', 
    'KAN':'1', 
    'LCA':'1', 
    'MAF':'590', 
    'SPM':'508', 
    'VCT':'1', 
    'WSM':'685', 
    'SMR':'378', 
    'STP':'239', 
    'SAU':'966', 
    'SEN':'221', 
    'SRB':'381', 
    'SYC':'248', 
    'SLE':'232', 
    'SGP':'65', 
    'SXM':'1', 
    'SVK':'421', 
    'SVN':'386', 
    'SLB':'677', 
    'SOM':'252', 
    'ZAF':'27', 
    'SGS':'500', 
    'KOR':'82', 
    'SSD':'211', 
    'ESP':'34', 
    'LKA':'94', 
    'SDN':'249', 
    'SUR':'597', 
    'SJM':'47', 
    'SWE':'46', 
    'CHE':'41', 
    'SYR':'963', 
    'TWN':'886', 
    'TJK':'992', 
    'TZA':'255', 
    'THA':'66', 
    'TGO':'228', 
    'TKL':'690', 
    'TON':'676', 
    'TTO':'1', 
    'TUN':'216', 
    'TUR':'90', 
    'TKM':'993', 
    'TCA':'1', 
    'TUV':'688', 
    'UGA':'256', 
    'UKR':'380', 
    'ARE':'971', 
    'USA':'1', 
    'VGB':'1', 
    'URY':'598', 
    'UZB':'998', 
    'VUT':'678', 
    'VAT':'39', 
    'VEN':'58', 
    'VNM':'84', 
    'WLF':'681', 
    'ESH':'212', 
    'YEM':'967', 
    'ZMB':'260', 
    'ZWE':'263'
    }
# ---------------------------------------------------------------------------
# CODE
# ---------------------------------------------------------------------------

# function to set iso3_code_entry
def run_query(*args):

    if iso3_code_entry.get() != '' :
        # store entries
        iso3 = iso3_code_entry.get()
        
        # insert new Entry from Dictionary
        phone_dct = country_dct.get(iso3)
        print(phone_dct)
        phone_code_entry.delete(0,END)
        phone_code_entry.insert(0,str(phone_dct))
        phone_code_entry.config(state= "disabled")
        iso3_code_entry.config(state= "disabled")
        
    elif iso3_code_entry.get() != '' :
        phone_code_entry.delete(0,END)
        iso3_code_entry.delete(0,END)    
        
    elif phone_code_entry.get() != '' :
        # store entries
        phone = phone_code_entry.get()

        # insert new Entry from Dictionary
        for key, value in country_dct.items():
            if value == phone:
                iso3_dct = key
        # iso3_dct = country_dct.get(phone)
        print(iso3_dct)
        iso3_code_entry.delete(0,END)
        iso3_code_entry.insert(0,iso3_dct)
        phone_code_entry.config(state= "disabled")
        iso3_code_entry.config(state= "disabled")
    
    elif iso3_code_entry.get() == '' and phone_code_entry.get() =='':
        reset_entries()

# RESET function to clean all entries
def reset_entries():
    phone_code_entry.config(state= "enabled")
    iso3_code_entry.config(state= "enabled")
    iso3_code_entry.delete(0,END)
    phone_code_entry.delete(0,END)
    return

# Create object
root = Tk()
root.bind('<Return>', run_query)
root.bind('<KP_Enter>', run_query)

# Set Title of App
root.title("PHONE")

# General Adjustments
root.geometry("250x150")
mainframe = ttk.Frame(root, padding="4 4 15 15")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S), columnspan=3)

# Interface Labels
ttk.Label(mainframe, text="").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Country Name (ISO-3)").grid(column=1, row=2, sticky=W)
ttk.Label(mainframe, text="").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, text="Country Number Prefix").grid(column=1, row=4, sticky=W)
ttk.Label(mainframe, text="").grid(column=1, row=5, sticky=W)

# Buttons
ttk.Button(mainframe, text="RESET", command=reset_entries).grid(column=1, row=6, sticky=W)
ttk.Button(mainframe, text="RUN", command=run_query).grid(column=2, row=6, sticky=W)

# Entry Country in ISO-3
iso3_code = StringVar()
iso3_code_entry = ttk.Entry(mainframe, width=5, textvariable=iso3_code)
iso3_code_entry.grid(column=2, row=2, sticky=(E))
ttk.Label(mainframe, text="        ").grid(column=2, row=2, sticky=W)

# Entry Country Phone Code
phone_code = StringVar()
phone_code_entry = ttk.Entry(mainframe, width=5, textvariable=phone_code)
phone_code_entry.grid(column=2, row=4, sticky=(E))
ttk.Label(mainframe, text="      +").grid(column=2, row=4, sticky=W)

# Execute tkinter
root.mainloop()
