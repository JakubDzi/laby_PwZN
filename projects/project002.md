# Projekt II
*Trochę fizyki*

---

## Opis

Celem tego projektu jest napisanie symulacji/wizualizacji modelu Isinga 2D metodą Monte Carlo.

## Skrypt przyjmuje jako parametry:
- rozmiar siatki
- wartość $J$
- parametr $\beta$
- wartość pola $H$
- liczbę kroków symulacji (1 krok oznacza $1\cdot$ liczba spinów)
- *(opcjonalny parametr)* początkową gęstość spinów $\uparrow$ (domyślnie 0.5)
- *(opcjonalny parametr)* nazwy pliku z obrazkami (domyślnie *step*)

## Skrypt zwraca:
- sekwencję obrazków zapisanych na dysku z kolejnymi krokami symulacji
- *(opcjonalnie)* plik z magnetyzacją w funkcji kroku (nazwa opcjonalnym parametrem skryptu)
- *(bardzo opcjonalnie)* filmik z animacją (nazwa opcjonalnym parametrem skryptu)

## Wymagania:
- symulacja ma być zaimplementowana jako obiekt
- ma wyświetlać się progress bar
- *(opcjonalnie)* Hamiltonian może być podawany obiektowi symulacji jako jeden z parametrów
- *(opcjonalnie)* do obiektu symulacji dorobić możliwość iterowania się po kolejnych krokach w pętli for
- *(opcjonalnie)* progress bar ma zawierać informacje na temat czasu, jaki upłynął
- *(opcjonalnie)* progress bar ma być super ładny i kolorowy

## Przydatne biblioteki:
- [Rich](https://github.com/willmcgugan/rich)
- [Pillow](https://pypi.org/project/Pillow/)