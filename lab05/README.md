<P>System ten opiera się o&nbsp;trudność problemu Diffie-Hellmana, wersja
bardziej złożona jest podstawą amerykańskiego standardu podpisu cyfrowego DSA. 
Przygotowanie
kluczy wymaga znalezienie liczby&nbsp;<I>p</I>, jeśli nie pseudopierwszej, to
przynajmniej takiej, że <I>p&minus;1</I> ma duży dzielnik pierwszy. W&nbsp;zadaniu
poniższym dla uproszczenia nie będziemy się tym zajmować. </P>

<P>Następnym problemem jest znalezienie generatora. <I>g</I>&nbsp;jest
generatorem Z<I>p*</I>&nbsp;=&nbsp;{1,2,...,<I>p&minus;1</I>} jeśli kolejne potęgi
<I>g</I>&nbsp;mod&nbsp;<I>p</I> wyczerpują cały zbiór reszt. Generatorów jest
dość dużo (dokładniej, ich liczba jest równa liczbie Eulera
<I>&phi;</I>(<I>p&minus;1</I>)). 
W&nbsp;zadaniu
poniższym dla uproszczenia również nie będziemy się tym zajmować.
<!--
Na ogół wystarczy przejrzeć kilka małych liczb by
znaleźć generator. Na pewno <I>g<sup>p&minus;1</sup></I>&nbsp;=&nbsp;1 (mod&nbsp;<I>p</I>).
Liczba&nbsp;<I>g</I> nie jest generatorem, jeśli już mniejsza potęga jest
równa&nbsp;1 (bo wówczas niektóre wartości nie wystąpią wcale). Jeśli mniejsza
potęga jest równa&nbsp;1, to musi ona być dzielnikiem <I>p</I>&minus;1, wystarczy więc
skupić się na obliczeniu niektórych tylko potęg. W&nbsp;programie znajdowania
generatora trzeba będzie znaleźć dzielniki&nbsp;<I>&gamma;</I> liczby <I>p&minus;1</I>
mniejsze niż ustalona liczba, np. 1000 (w&nbsp;realnym programie należałoby
rozważać znacznie większe dzielniki), a&nbsp;następnie testować czy
<I>g</I><sup>(<I>p&minus;1</I>)/<I>&gamma;</I></sup>&nbsp;=&nbsp;1 (mod&nbsp;<I>p</I>). Jeśli tak,
to&nbsp;<I>g</I> na pewno nie jest generatorem i&nbsp;trzeba testować kolejnego
kandydata. W&nbsp;przeciwnym przypadku, z&nbsp;dużym prawdopodobieństwem można
założyć, że&nbsp;<I>g</I> generatorem jest.</P>-->

<P><B>Kryptosystem ElGamala</B>: dane są liczba pierwsza&nbsp;<I>p</I> oraz
generator&nbsp;<I>g</I> grupy Z<I>p*&nbsp;</I>=&nbsp;{1,2,...,<I>p&minus;</I>1}.
Mogą być
one ustalone jeden raz dla większej liczby uczestników. Kluczem prywatnym Bolka
jest dowolna liczba&nbsp;<I>b</I>, a&nbsp;kluczem publicznym potęga
<I>&beta;=g<sup>b</sup>&nbsp</I>(mod&nbsp;<I>p</I>). Nie można obliczyć wykładnika
ze znajomości potęgi, ale oczywiście zależność odwrotna nie zachodzi. Tak więc
kluczy tych nie można zamienić miejscami. Algorytmy szyfrowania i&nbsp;podpisu
cyfrowego muszą być różne.</P>

<P><B>Szyfrowanie</B>: Alicja chce wysłać do Bolka wiadomość <I>m&lt;p</I>.
Losuje liczbę&nbsp;<I>k</I>. Szyfrogramem tej wiadomości jest para
<I>&lt;g<sup>k</sup>,&nbsp;m*&beta;<sup>k</sup>&gt;</I>&nbsp;(mod&nbsp;<I>p</I>).</P>

<P>Bolek najpierw oblicza czynnik zaciemniający
<I>&beta;<sup>k</sup>&nbsp;=&nbsp;</I>(<I>g<sup>b</sup></I>)<I><sup>k</sup>&nbsp;=&nbsp;</I>(<I>g<sup>k</sup></I>)<I><sup>b</sup></I>
(mod&nbsp;<I>p</I>). Potem wykonuje dzielenie by obliczyć&nbsp;<I>m</I>.

<P><B>Podpis</B>: Bolek chce podpisać wiadomość <I>m&lt;p</I>. Losuje liczbę
<I>k</I> względnie pierwszą z&nbsp;<I>p</I>&minus;1<I>.</I> Podpis pod tą
wiadomością składa się z&nbsp;dwu części: <I>r=g<sup>k</sup></I> (mod&nbsp;<I>p</I>)
oraz <I>x&nbsp;=&nbsp;</I>(<I>m&minus;b*r</I>)<I>*k</I><sup>&minus;1</sup>
(mod&nbsp;<I>p&minus;</I>1). Sama wiadomość&nbsp;<I>m</I> też musi być
przekazana.</P>

<P>Alicja weryfikuje podpis sprawdzając równość (mod&nbsp;<I>p</I>) dwu
wielkości: <I>g<sup>m</sup></I> oraz <I>r<sup>x</sup>*&beta;<sup>r</sup></I>.</P>
Pożytecznym może być zastosowanie algorytmu Euklidesa opisanego 
w&nbsp;<a href="http://inf.ug.edu.pl/~amb/krypto-lab/Euklides.html">Euklides.html</a>.

<H1>Zadanie:</H1>
<P>Program o&nbsp;nazwie
<FONT FACE="Courier 10 Pitch">elgamal</FONT> 
korzysta z&nbsp;pliku <FONT FACE="Courier 10 Pitch">elgamal.txt</FONT> zawierającego
liczbę pierwszą&nbsp;<I>p</I> oraz generator&nbsp;<I>g</I>.
Testy programu będą wykonane z&nbsp;plikiem o&nbsp;zawartości:
<pre>
1665997633093155705263923663680487185948531888850484859473375695734301776192932338784530163
 170057347237941209366519667629336535698946063913573988287540019819022183488419112350737049
</pre>

Program wywołany z&nbsp;opcją 
<ul>
<li><FONT FACE="Courier 10 Pitch">-k</FONT> czyta z&nbsp;powyższego pliku
    i&nbsp;generuje parę kluczy zapisanych w&nbsp;plikach 
    <FONT FACE="Courier 10 Pitch">private.txt</FONT> oraz 
    <FONT FACE="Courier 10 Pitch">public.txt</FONT>. Każdy klucz składa się z&nbsp;dwu
    wierszy skopiowanych z&nbsp;powyższego pliku oraz trzeciego wiersza
    zawierającego odpowiednio wykładnik lub potęgę.
<li><FONT FACE="Courier 10 Pitch">-e</FONT> odczytuje klucz publiczny,
    następnie odczytuje wiadomość z&nbsp;pliku 
    <FONT FACE="Courier 10 Pitch">plain.txt</FONT> i&nbsp;zapisuje zaszyfrowaną
    wiadomość w&nbsp;pliku <FONT FACE="Courier 10 Pitch">crypto.txt</FONT>.
    Jeśli warunek <I>m&lt;p</I> nie jest spełniony, sygnalizuje błąd. 
<li><FONT FACE="Courier 10 Pitch">-d</FONT> odczytuje klucz prywatny
    i&nbsp;kryptogram, a&nbsp;odszyfrowaną wiadomość zapisuje w&nbsp;pliku 
    <FONT FACE="Courier 10 Pitch">decrypt.txt</FONT>.
<li><FONT FACE="Courier 10 Pitch">-s</FONT> odczytuje klucz prywatny,
    następnie odczytuje wiadomość z&nbsp;pliku 
    <FONT FACE="Courier 10 Pitch">message.txt</FONT> 
    i&nbsp;produkuje podpis, czyli dwa wiersze zapisane do pliku 
    <FONT FACE="Courier 10 Pitch">signature.txt</FONT>. 
<li><FONT FACE="Courier 10 Pitch">-v</FONT> odczytuje klucz publiczny, wiadomość
    z&nbsp;pliku <FONT FACE="Courier 10 Pitch">message.txt</FONT> oraz podpis
    z&nbsp;pliku <FONT FACE="Courier 10 Pitch">signature.txt</FONT>
    i&nbsp;weryfikuje ten podpis.  Wynik weryfikacji (T/N) jest wyświetlany na ekranie
    oraz jest zapisywany w&nbsp;pliku
    <FONT FACE="Courier 10 Pitch">verify.txt</FONT>. 
</ul>
Pliki <FONT FACE="Courier 10 Pitch">plain.txt</FONT> oraz
<FONT FACE="Courier 10 Pitch">message.txt</FONT> mogą być identyczne.
</P><P>
Sprawdzenie poprawności programu będzie m.in. zawierało sprawdzenie
identyczności plików <FONT FACE="Courier 10 Pitch">plain.txt</FONT> oraz <FONT
FACE="Courier 10 Pitch">decrypt.txt</FONT> oraz sprawdzenie poprawności
weryfikowania podpisu poprawnego (tzn. <FONT FACE="Courier 10
Pitch">signature.txt</FONT> powstał w&nbsp;opisany wyżej sposób)
i&nbsp;niepoprawnego w&nbsp;przeciwnym przypadku.
</P><P>
Program musi wykorzystywać działania arytmetyczne na liczbach kilkusetbitowych, 
w&nbsp;niektórych językach, np. python, są one dostępne bez dodatkowych bibliotek, 
w&nbsp;innych, np. Java, konieczne będzie użycie odpowiednich bibliotek.
</P><P>
Program <strong>nie ma prawa</strong> odczytywać innych plików niż wskazanych
w&nbsp;poszczególnych opcjach.
</P>