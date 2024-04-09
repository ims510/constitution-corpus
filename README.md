# Constitution corpus
Projet pour cours "Outils de traitement de corpus" 

# La tache à réaliser

Je voudrais me concentrer sur une tâche de classification d'un texte en fonction de la langue du texte (par exemple prédire le pays, ou même la region d'un pays d'ou le texte provient).

# Un corpus qui répond à cette tâche

Le corpus qui m'a inspiré c'est le corpus MOROCO: https://huggingface.co/datasets/moroco 

Le corpus contient des échantillons de textes moldaves et roumains collectés dans le domaine de l'actualité. Les échantillons appartiennent à l'un des six thèmes suivants : (0) culture, (1) finance, (2) politique, (3) science, (4) sport, (5) technologie. Le corpus comprend un total de 33 564 échantillons classés dans l’une des six catégories mentionnées ci-dessus.

Les données textuelles collectées consistent en des reportages d'actualité librement disponibles sur Internet et d'intérêt public.

Les échantillons sont prétraités afin d'éliminer les entités nommées. Ceci est nécessaire pour empêcher les classificateurs de prendre des décisions basées sur des caractéristiques qui ne sont pas liées aux thèmes ou au pays d'origine du texte. Par exemple, les entités nommées qui font référence aux noms d’hommes politiques ou de joueurs de football peuvent fournir des indices sur le thème ou le pays.

# À quel type de prédiction peut servir ce corpus

La tâche principale de ce corpus est la classification de texte, avec la sous-tâche de classification par thème. Dans l'article écrit lors de la publication du corpus (https://arxiv.org/pdf/1901.06543v2.pdf), les auteurs ont utilisé ce corpus pour les tâches suivantes: 

-  discrimination binaire des échantillons de texte en textes moldaves ou roumains
-  catégorisation multi-classes, intra-dialect
- catégorisation multi-classes, à travers dialects


# À quel modèle il a servi

Depuis la publication de ce corpus dans l'article cité avant, 22 autres articles ont été publiés qui utilisent ce corpus dans leurs modèles (https://paperswithcode.com/dataset/moroco). Parmi eux, les plus pertinants pour le sorte de tâche qui m'intèresse sont:
- Discrimination entre les tweets roumains et moldaves standard à l'aide de ngrammes de caractères filtrés (https://aclanthology.org/2020.vardial-1.25.pdf)
- L'efficacité déraisonnable de l'apprentissage automatique dans l'identification des dialectes moldave et roumain (https://arxiv.org/pdf/2007.15700v3.pdf)
- Affiner le BERT avec le bruit au niveau des caractères pour un transfert zéro vers les dialectes et les langues étroitement liées (https://arxiv.org/pdf/2303.17683v1.pdf)


