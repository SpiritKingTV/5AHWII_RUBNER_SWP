# Linked List
In diesem Beispiel lernen wir, was eine Linked List ist und wie man sie anwendet


## Eingebaute Klassen
 * Klasse LinkedList erstellt (mit TopValue und length)
 * Klasse Node erstellt (mit nextValue und value)

## Eingebaute Methoden
* attach(self, newNode) --> Erstellt das erste Node oder hängt eines dran
* returnLList(self) --> Gibt alle werte der Reihe nach in LinkedList zurück
* returnlengthLlist(self) --> Gibt Länge der Linked List zurück
* find(self, value) --> Gibt zurück, ob die Node in der LL existiert
* insertBefore(self, curr, newnode) --> Erstellt eine Node in der LL vor einer ausgewählten Node
* insertAfter(self,prevnode,newnode) --> Erstellt eine Node in der LL nach einer ausgewählten Node
* deleteBefore(self,curr) -->  Löscht ein Node in der LL vor dem ausgewählten Node
* deleteAfter(self,nodenow) -->  Löscht ein Node in der LL nach dem ausgewählten Node
Note: Für die Before-Methoden bracht man Double Linked Lists

## Erweiterung der LL zu einer Double-Linked-List
Man fügt eine Variable (previous bzw. in meinem beispeil prev) hinzu.
Dort wird die vorherige Node der LL eingetragen

## Erweiterung auf ArrayLists(Lists)
Die selben Methoden wie bei double Linked List

## Tabelle der Aufwandsklassen
| Methode       | double-linked-list | ArrayList|
| ------------- | -------------   |--------------|
|attach| n+1  |n+1/1|
|returnAll| n  |n|
|returnLength| n  |n|
|find| n  |n|
|insertBefore| 1  |1|
|insertAfter| 1  |1|
|deleteBefore| 1  |1|
|deleteAfter| 1  |1|
|SortDesc| n^2  |n^2|
|SortAsc| n^2  |n^2|

## Zeitmessung
Zeitmessung der Sortierungen Aufsteigend bei 1000 Werten
![Zeit](https://github.com/SpiritKingTV/5AHWII_RUBNER_SWP/blob/main/LinkedList/Bild_2022-03-23_201819.png)

## Zusatz: Interface mit Kivy
Im Interface kann man Momentan eine ArrayList erstellen bzw. Werte hinzufügen. Diese können danach mit Refresh abgefragt. Zudem werden sie ausgegeben
Linked List: Bei linked List wurden sie noc nicht implementiert(Zeitmangel)
![Menü](https://github.com/SpiritKingTV/5AHWII_RUBNER_SWP/blob/main/LinkedList/Bild_2022-03-23_201308.png)

