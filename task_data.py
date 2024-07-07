task_data = {
    # Defaults:
    # "task_cost": 1
    # "people_per_grid": 1
    # "floor_specific: None"
    # "task_limit": None

    # Cuisine, 1/2
    "cuisine": {
        "cells": ["B"+str(i) for i in range(2, 9)],
        "people_per_grid": 2,
        "task_cost": 3.5,
    },
    # Trois, Lundi et Vendredi
    "essuis": {
        "cells": ["C2", "C6"],
    },
    # Trois, Poubelles, Mercredi
    "poubelles_mercredi": {
        "cells": ["C4"],
        "task_cost": 0.5,
    },
    # Trois, Cuisine
    "cuisine_nettoyage": {
        "cells": ["C7"],
        "people_per_grid": 3,
    },
    # 4, Tous les jours sauf dimanche
    "salle_a_manger": {
        "cells": ["D"+str(i) for i in range(2, 8)],
    },
    # 5
    "etage_2": {
        "cells": ["E"+str(i) for i in range(2, 9)],
        "floor_specific": 2
    },
    # 6
    "etage_3": {
        "cells": ["F"+str(i) for i in range(2, 9)],
        "floor_specific": 3
    },
    # 7
    "etage_4": {
        "cells": ["G"+str(i) for i in range(2, 9)],
        "floor_specific": 4
    },
    # 8
    "etage_1": {
        "cells": ["H"+str(i) for i in range(2, 9)],
        "task_limit": 5,
    },
    # 9
    "rez_de_chaussee": {
        "cells": ["I"+str(i) for i in range(2, 9)],
        "task_limit": 4,
    },
    # 10
    "cave": {
        "cells": ["J"+str(i) for i in range(2, 9)],
        "task_limit": 3,
    },
    # 11
    "petit_dej": {
        # Tous les jours sauf dimanche
        "cells": ["K"+str(i) for i in range(2, 8)],
        "task_cost": 0.5,
    },
    # 12, Lundi
    "bac_poubelle": {
        "cells": ["L2"],
    },
    # 12, Jardin, Mardi, Jeudi
    "jardin": {
        "cells": ["L3", "L5"],
    },
    # 12, Fruits, Mercredi
    "fruits": {
        "cells": ["L4"],
    },
    # 12, Kali, Vendredi
    "kali" : {
        "cells": ["L6"],
    },
    # 12 , Poubelles, dimanche
    "poubelles_dimanche": {
        "cells": ["L8"],
        "task_cost": 0.5,
    }
}

for key in task_data.keys():
    if task_data[key].get("task_cost") is None:
        task_data[key]["task_cost"] = 1

    if task_data[key].get("people_per_grid") is None:
        task_data[key]["people_per_grid"] = 1

    if task_data[key].get("floor_specific") is None:
        task_data[key]["floor_specific"] = None

    if task_data[key].get("task_limit") is None:
        task_data[key]["task_limit"] = None

task_order = [
    'cuisine',
    'etage_2',
    'etage_3',
    'etage_4',
    'essuis',
    'cuisine_nettoyage',
    'salle_a_manger',
    'etage_1',
    'rez_de_chaussee',
    'cave',
    'bac_poubelle',
    'jardin',
    'fruits',
    'kali',
    'poubelles_mercredi',
    'poubelles_dimanche',
    'petit_dej',
]

days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']