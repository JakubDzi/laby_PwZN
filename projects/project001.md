# Projekt I
*Miłe złego początki*

---

##Opis
Celem pierwszego projektu jest napisanie skryptu, który wczytuje plik tekstowy i rysuje na konsoli
histogram wszystkich wyrazów w pliku. Należy znaleźć tekst jakiejś książki po angielsku i po polsku
(tłumaczenie) i zbadać rozkłady.

##Wymagania:
- nazwa pliku jako parametr skryptu
- wyświetlanie histogramu od najczęściej do najrzadziej występujących wyrazów
- opcjonalny parametr określający dla ilu wyrazów histogram wyświetlić (domyślnie 10)
- opcjonalny parametr określający minimalną długość histogramowanego słowa (domyślnie 0)
- *(opcjonalnie)* dodatkowy, opcjonalny parametr przyjmujący listę wyrazów ignorowanych
- *(opcjonalnie)* kolorowy histogram, który mnie oczaruje

##Przydatne biblioteki:
- [ascii_graph](https://github.com/kakwa/py-ascii-graph)
- [argparse](https://docs.python.org/3/library/argparse.html)