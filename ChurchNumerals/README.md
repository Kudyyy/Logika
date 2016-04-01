#Liczebniki Churcha:

Liczebniki Churcha to sposób na reprezentację liczb naturalnych. Reprezentacja liczby n odbywa się za pomocą funkcji f. n razy wykonana funkcja f oznacza liczbę n,
k razy wykonana funkcja f oznacza liczbę k itd.

	zero 	:= f x = x			lambda f: lambda x: x
	jeden 	:= f x = f x			
	dwa 	:= f x = f ( f x )
	trzy 	:= f x = f ( f ( f x ) )
	.
	.
	.
	n		:= f x = f^n x


Liczba n może powstać poprzez wykonanie funkcji f o jeden raz więcej na liczbie n-1.
Więc definiujemy sobie funkcję *succ* która dla n wykonuję funkcję f n+1 razy.

	succ 	:= n f x =  f ( n f x ) 	lambda n: lambda f: lambda x: f(n(f)(x))

W ten sposób możemy otrzymać każdą kolejną liczb w taki sposób:

	succ(zero) = f ( zero f x ) = f ( ( f x = x ) f x ) = f ( x ) = f x = jeden
	succ(jeden) = f ( jeden f x ) = f ( ( f x = f x ) f x ) = f ( f x ) = dwa
	.
	.
	.

Dodawanie dwóch liczb m i n polega na wykonaniu funkcji f m+n razy  
![f^(m+n)=f^m(f^n)](https://latex.codecogs.com/gif.latex?f^(^m^&plus;^n^)=f^m(f^n))

	add		:= m n f x = m f ( n f x ) 	lambda m: lambda n: lambda f: lambda x: m(f)(n(f)(x))

Mnożenie dwóch liczb m i n polega na wykonaniu funkcji f m\*n razy  
![f^(m\*n)=(f^n)^m](https://latex.codecogs.com/gif.latex?f^(^m^*^n^)=(f^n)^m)

	mult	:= m n f x = m ( n f ) x	lambda m: lambda n: lambda f: lambda x: m(n(f))(x)

Podnoszenie liczby m do potęgi n polega na wykonaniu funkcji f m^n razy:

	exp 	:= m n f x = ( n m ) f x 	lambda m: lambda n: lambda f: lambda x: (n)(m)(f)(x)

Jeżeli naszą funkcją f będzie funkcja `lambda x:x+1` a argumentem x będzie 0
to korzystając z liczebników Churcha jesteśmy w stanie przedstawić każdą
 liczbę naturalną i wykonać na nich podstawowe działania arytmetyczne.

Jako funkcję pomocnicze w programie wykorzystałem getNum oraz getChurch.

**getNum** powoduję to, iż do funkcji dopisywane są dwa argumenty,
pierwszy to funkcja inkrementująca f1 a drugi to arg1 = 0, pozwala to
przedstawić liczby Churcha jako liczby naturalne.

**getChurch** tworzy nam rekurencyjnie dowolną większą bądź równą 0 liczbę Churcha.

