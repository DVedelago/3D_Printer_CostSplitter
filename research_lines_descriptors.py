""" 


Defining the Research lines between which the costs must be split. 
using [Data_Structure] to assign Users to PIs


"""
# ################################################
# class ResearchLine:                            
                                               
#     def __init__(self, owners[], cm3) -> None: 
#         self.owners = owners[]                 
#         self.cm3_usage = cm3                   

# ################################################



# hhcm_owners = [
#     'Akash_Singh',
#     'aksingh',
#     'cburchielli',
#     'edb',
#     'ggarofalo',
#     'Giovanni_Garofalo',
#     'gsofia',
#     'Ioannis_Sarakoglou',
#     'Jorn_Malzahn',
#     'LBaccelliere',
#     'Navvab',
#     'Pietro_Gurnari',
#     'scarrozzo',
#     'Yifan',
#     'yizhang'
# ]



#HHCM_Tsagarakis = ResearchLine(hhcm_owners, 0)

###############################################################################################################################################

HHCM_Tsagarakis = {
    'owners': [
        'Akash_Singh',
        'aksingh',
        'cburchielli',
        'Carlo_Rizzardo',
        'edb',
        'ggarofalo',
        'Giovanni_Garofalo',
        'gsofia',
        'Ioannis_Sarakoglou',
        'Jiang',
        'Jorn_Malzahn',
        'LBaccelliere',
        'Navvab',
        'Pietro_Gurnari',
        'pgurnari',
        'scarrozzo',
        'sduddu',
        'Yifan',
        'yizhang',
        'chiara_castellani' # temporaneo, da vedere reale username, da controllare effettivo consumo, se troppo alto da spostare su altro budget
    ],
    'total_cm3': 0,
    'res_line_name': "HHCM Tsagarakis"
}


ADVR_Caldwell = {
    'owners': [
        'alperen_acemoglu',
        'asantangelo',
        'ardit_poka',
        'arditpoka',
        'cabello',
        'Carola_Abello',        
        'cdinatali',
        'DPARK',
        'Federico_Mariano',
        'federico_allione',
        'fmanara',        
        'Jesús_Ortiz',
        'JOrtiz',
        'Iacopo_Longinotti',
        'ksawant',
        'lorenzo_ceppari',
        'msposito',
        'psencandan',
        'rgagliardi',
        'Roberto_Pitzalis',
        'rpitzalis',
        'yonas tefera',
        'ytefera',
        'Yaesol_kim',
        'Donatien_Delehelle',
        'Donatien Delehelle',
        'DonDelehelle',
        'DDelehelle',
        'alibaba',           # This is still Donatien Delehelle, it's a temporary username
        'Chiara_Falagario' # beta - not in the queue yet - DV  # Demattos
        
    ],
    'total_cm3': 0,
    'res_line_name': "ADVR Caldwell"
}

ADVRF_Cordasco = {
    'owners': [
        'Yussef_Hassanien',
        'dvedelago',
        'mmigliorini',
        '--'                    # cadbottle, axis calib and maintenance prints
    ],
    'total_cm3': 0,
    'res_line_name': "ADVRF Cordasco"
}

DLS_Semini = {
    'owners': [
        'Giacomo_Mazzaglia',
        'Victor_Barasuol',
        'VBarasuol',
        'Sinan_Emre',
        'Matteo_Villa',
        'mavilla',
        'semre',
        'Seyed_Amir_Mohamad_Hosseini_Rad',
        'A_Rad',
        'arad',
        'isabe',
        'ksuryavanshi'
    ],
    'total_cm3': 0,
    'res_line_name': "DLS Semini"
}

HRII_Ajoudani = {
    'owners': [
        'Robin_Arbaud',
        'Fran_Ruiz',
        'pbalatti',
        'ggiardini',
        'Mattia_Leonori',
        'Pietro_Balatti',
        'fruiz',
        'rarbaud',
        'tspigno'
    ],
    'total_cm3': 0,
    'res_line_name': "HRII Ajoudani"

}

IRF_Cannella = {
    'owners':[
        
        'fnozadheravi',
        'Farshad_NH',
        'Lizhou_Xu',
        'khelifa_baizid',        
        'nicolò_rizzato',
        'mlahoud'
    ],
    'total_cm3': 0,
    'res_line_name': "IRF Cannella"
}



res_lines_list = [
    IRF_Cannella,
    HRII_Ajoudani,
    DLS_Semini,
    ADVRF_Cordasco,
    ADVR_Caldwell,
    HHCM_Tsagarakis
]
