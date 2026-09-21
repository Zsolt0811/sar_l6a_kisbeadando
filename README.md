Futószalag Minőségellenőrző Rendszer

Ez a repository egy ipari futószalag szimulációját és minőségellenőrzését valósítja meg ROS 2 alapon.

Működés Leírása:
1. conveyor_node: Másodpercenként generál egy alkatrészt egyedi azonosítóval. Véletlenszerűen (20% eséllyel) selejtes (NOK) státuszt ad neki.
2. inspector_node: Feliratkozik a 'conveyor_belt' topicra. Normál alkatrész esetén jóváhagyja azt, selejt esetén pedig figyelmeztet.

Futtatás:
```bash
1. cd ~/ros2_ws/src
   git clone [https://github.com/Zsolt0811/sar_l6a_kisbeadando.git](https://github.com/Zsolt0811/sar_l6a_kisbeadando.git)
2. cd ~/ros2_ws
   colcon build --packages-select sar_l6a_kisbeadando
3. source install/setup.bash
4. ros2 launch sar_l6a_kisbeadando beadando.launch.py



