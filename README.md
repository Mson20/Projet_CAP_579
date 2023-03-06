# Projet_CAP_579
Oeil dans le dos (pas vraiment un oeil):
  Le but de ce projet est le développemenet d'une solution permettant à l'utilisateur de savoir s'il est physiquement suivi
  basée sur les packets wifi des smartphones et autres objets connectés. Lors ce qu'on active la wifi à un appareil, l'appareil
  envoit des packets de demande de connection des différents réseaux connues.
  Nous exploitons ces packets pour savoir si l'utilisateur est suivi, nous utilisons un script permettant de récupérer les paquets (sniff-probes.sh)
  qui les écrits dans un fichier texte (ex: 06-03-2023.txt); avec ces fichiers texte, on les traite et stocke dans un fichier .db (SSID.db lisable avec DBeaver)
  avec un script python (todb.py).
  Ce traitement ce fait automatiquement avec Onlaunch.sh qui se lance lors du démarrage de la raspberry pi avec un dungle wifi en monitor

