# Funkcje skrótu

Dwie najpopularniejsze i najczęściej używane funkcje skrótu to md5 oraz sha-1. Na wielu systemach są one dostępne bez dodatkowych instalacji, na komputerze sigma polecenia brzmią md5sum oraz sha1sum. Pierwsza z tych funkcji zwraca skrót 128-bitowy, druga 160-bitowy. Standard SHA udostępnia wiele dalszych funkcji: sha224sum sha256sum sha384sum sha512sum, dających coraz dłuższe skróty. Inna funkcja skrótu to b2sum. Skróty zapisywane są w systemie szesnastkowym (bez dodatkowych wyjaśnień, że chodzi o ten system zapisu).

## Zadanie

1. Przygotuj plik personal.txt zawierający imię i nazwisko. Oblicz wszystkie funkcje skrótu na tym pliku, wyniki zapisz do pliku hash.txt w kolejności coraz dłuższych skrótów.

2. Przygotuj drugą wersje pliku personal_.txt, różniącą się jedynie dodatkowym pustym wierszem na końcu. Oblicz wartość wszystkich funkcji skrótu dla obu wersji pliku połączonego z tym samym plikiem plikiem wykładu hash-.pdf (tzn. wykonaj polecenia:

- cat hash-.pdf personal.txt | md5sum >> hash.txt
- cat hash-.pdf personal_.txt | md5sum >> hash.txt
	
itd. dla obu wersji pliku z danymi osobowymi). Następnie sprawdź liczbę bitów (nie bajtów) różnych w obu wynikach. 