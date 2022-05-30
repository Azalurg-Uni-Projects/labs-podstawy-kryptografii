System ten opiera się o trudność problemu Diffie-Hellmana, wersja bardziej złożona jest podstawą amerykańskiego standardu podpisu cyfrowego DSA. Przygotowanie kluczy wymaga znalezienie liczby p, jeśli nie pseudopierwszej, to przynajmniej takiej, że p−1 ma duży dzielnik pierwszy. W zadaniu poniższym dla uproszczenia nie będziemy się tym zajmować.

Następnym problemem jest znalezienie generatora. g jest generatorem Zp* = {1,2,...,p−1} jeśli kolejne potęgi g mod p wyczerpują cały zbiór reszt. Generatorów jest dość dużo (dokładniej, ich liczba jest równa liczbie Eulera φ(p−1)). W zadaniu poniższym dla uproszczenia również nie będziemy się tym zajmować.
Kryptosystem ElGamala: dane są liczba pierwsza p oraz generator g grupy Zp* = {1,2,...,p−1}. Mogą być one ustalone jeden raz dla większej liczby uczestników. Kluczem prywatnym Bolka jest dowolna liczba b, a kluczem publicznym potęga β=gb (mod p). Nie można obliczyć wykładnika ze znajomości potęgi, ale oczywiście zależność odwrotna nie zachodzi. Tak więc kluczy tych nie można zamienić miejscami. Algorytmy szyfrowania i podpisu cyfrowego muszą być różne.

Szyfrowanie: Alicja chce wysłać do Bolka wiadomość m<p. Losuje liczbę k. Szyfrogramem tej wiadomości jest para <gk, m*βk> (mod p).

Bolek najpierw oblicza czynnik zaciemniający βk = (gb)k = (gk)b (mod p). Potem wykonuje dzielenie by obliczyć m.

Podpis: Bolek chce podpisać wiadomość m<p. Losuje liczbę k względnie pierwszą z p−1. Podpis pod tą wiadomością składa się z dwu części: r=gk (mod p) oraz x = (m−b*r)*k−1 (mod p−1). Sama wiadomość m też musi być przekazana.

Alicja weryfikuje podpis sprawdzając równość (mod p) dwu wielkości: gm oraz rx*βr.

Pożytecznym może być zastosowanie algorytmu Euklidesa opisanego w Euklides.html.
Zadanie:
Program o nazwie elgamal korzysta z pliku elgamal.txt zawierającego liczbę pierwszą p oraz generator g. Testy programu będą wykonane z plikiem o zawartości:

1665997633093155705263923663680487185948531888850484859473375695734301776192932338784530163
 170057347237941209366519667629336535698946063913573988287540019819022183488419112350737049
Program wywołany z opcją
-k czyta z powyższego pliku i generuje parę kluczy zapisanych w plikach private.txt oraz public.txt. Każdy klucz składa się z dwu wierszy skopiowanych z powyższego pliku oraz trzeciego wiersza zawierającego odpowiednio wykładnik lub potęgę.
-e odczytuje klucz publiczny, następnie odczytuje wiadomość z pliku plain.txt i zapisuje zaszyfrowaną wiadomość w pliku crypto.txt. Jeśli warunek m<p nie jest spełniony, sygnalizuje błąd.
-d odczytuje klucz prywatny i kryptogram, a odszyfrowaną wiadomość zapisuje w pliku decrypt.txt.
-s odczytuje klucz prywatny, następnie odczytuje wiadomość z pliku message.txt i produkuje podpis, czyli dwa wiersze zapisane do pliku signature.txt.
-v odczytuje klucz publiczny, wiadomość z pliku message.txt oraz podpis z pliku signature.txt i weryfikuje ten podpis. Wynik weryfikacji (T/N) jest wyświetlany na ekranie oraz jest zapisywany w pliku verify.txt.
Pliki plain.txt oraz message.txt mogą być identyczne.
Sprawdzenie poprawności programu będzie m.in. zawierało sprawdzenie identyczności plików plain.txt oraz decrypt.txt oraz sprawdzenie poprawności weryfikowania podpisu poprawnego (tzn. signature.txt powstał w opisany wyżej sposób) i niepoprawnego w przeciwnym przypadku.

Program musi wykorzystywać działania arytmetyczne na liczbach kilkusetbitowych, w niektórych językach, np. python, są one dostępne bez dodatkowych bibliotek, w innych, np. Java, konieczne będzie użycie odpowiednich bibliotek.

Program nie ma prawa odczytywać innych plików niż wskazanych w poszczególnych opcjach.