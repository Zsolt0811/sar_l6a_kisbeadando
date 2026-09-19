Futószalag Minőségellenőrző Rendszer

Ez a repository egy ipari futószalag szimulációját és minőségellenőrzését valósítja meg ROS 2 alapon.

Működés Leírása
1. conveyor_node: Másodpercenként generál egy alkatrészt egyedi azonosítóval. Véletlenszerűen (20% eséllyel) selejtes (NOK) státuszt ad neki.
2. inspector_node: Feliratkozik a conveyorbelt topicra. Normál alkatrész esetén jóváhagyja azt, selejt esetén pedig figyelmeztet.
