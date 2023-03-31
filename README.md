# Projet_CAP_579
Oeil dans le dos (pas vraiment un oeil):
  Le but de ce projet est le développement d'une solution permettant à l'utilisateur de savoir s'il est physiquement suivi
  basée sur les paquets wifi des smartphones et autres objets connectés. Lorsqu'on active la Wi-Fi à un appareil, l'appareil
  Envoit des paquets de demande de connexion des différents réseaux connus.
  Nous exploitons ces paquets pour savoir si l'utilisateur est suivi, nous utilisons un script permettant de récupérer les paquets (sniff probes.sh)
  qui les écrits dans un fichier texte (ex: 06-03-2023.txt ou OUT.txt); avec ces fichiers texte, on les traite et stocke dans un fichier .db (SSID.db lisable avec DBeaver)
  avec un script python (todb.py).
  Ce traitement se fait automatiquement avec Onlaunch.sh qui se lance lors du démarrage de la raspberry pi avec un dungle wifi en monitor

Remerciment à brannondorsey, https://github.com/brannondorsey/sniff-probes
