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
        'edb',
        'ggarofalo',
        'Giovanni_Garofalo',
        'gsofia',
        'Ioannis_Sarakoglou',
        'Jorn_Malzahn',
        'LBaccelliere',
        'Navvab',
        'Pietro_Gurnari',
        'scarrozzo',
        'Yifan',
        'yizhang'
    ],
    'total_cm3': 0
}


ADVR_Caldwell = {
    'owners': [
        'alperen_acemoglu',
        'asantangelo',
        'Carlo_Rizzardo',
        'cdinatali',
        'DPARK',
        'Federico_Mariano',
        'federico_allione',
        'fnozadheravi',
        'Jesús_Ortiz',
        'JOrtiz',
        'ksawant',
        'msposito',
        'psencandan',
        'rgagliardi',
        'Roberto_Pitzalis',
        'rpitzalis',
        'yonas tefera',
        'Yaesol_kim',
        'Donatien_Delehelle',
        'Donatien Delehelle',
        'DDelehelle',
        'alibaba'           # This is still Donatien Delehelle, it's a temporary username
    ],
    'total_cm3': 0
}

ADVRF_Cordasco = {
    'owners': [
        'Yussef_Hassanien',
        'dvedelago',
        'mmigliorini'
    ],
    'total_cm3': 0
}

DLS_Semini = {
    'owners': [
        'Giacomo_Mazzaglia',
        'Victor_Barasuol',
        'VBarasuol',
        'Sinan_Emre',
        'Matteo_Villa',
        'mavilla'
    ],
    'total_cm3': 0
}

HRII_Ajoudani = {
    'owners': [
        'Robin_Arbaud',
        'Fran_Ruiz',
        'pbalatti',
        'ggiardini',
        'Pietro_Balatti',
        'fruiz'
    ],
    'total_cm3': 0
}

IRF_Canali = {
    'owners':[
        'Iacopo_Longinotti',
        'carlo_canali',
        'Lizhou_Xu',
<<<<<<< HEAD
        'khelifa_baizid',
        'ardit_poka',
        'federico_manara'
=======
        'fmanara',
        'FMANARA',
        'arditpoka'
>>>>>>> c5c098bfb1604139e2467ea000c100d2b2c3f3e4
    ],
    'total_cm3': 0
}

res_lines_list = [
    IRF_Canali,
    HRII_Ajoudani,
    DLS_Semini,
    ADVRF_Cordasco,
    ADVR_Caldwell,
    HHCM_Tsagarakis
]