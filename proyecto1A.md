---
title: "Análisis y diseño de algoritmos: Proyecto final"
author: "Emilio E. G. Cantón Bermúdez y Roberto Gervacio Guendulay"
date: 09/05/2019
header-includes:
	- \usepackage{tikz}
	- \usetikzlibrary{automata,positioning}
	- \definecolor{activeNode}{RGB}{0, 127, 255}
	- \definecolor{change}{RGB}{255, 0, 0}
---

\newpage

# Resumen

El ordenamiento es uno de los bloques elementales para la creación de algoritmos más complejos. Para el desarrollo de estos algoritmos, el tiempo que te tome ordenar tu información puede llegar a ser vital. En este trabajo analizamos los algoritmos **Bubble Sort, Quick Sort, Radix Sort, Heapsort** y **Mergesort**.

# Heapsort

De acuerdo con [Srini Devadas](https://www.youtube.com/watch?v=B7hVxCmfPtM&t=2641s), un *heap* es una implementacióna de la estructura de datos abstracta, *priority queue*. En general el objetivo, tal como es definido en *priority queue*, es poder **insertar una llave**, **remover el valor máximo** (tomando en cuenta un tipo de comparación indefinida). Un *heap* lo que logra es implementar la manera más eficiente de cumplir estos requisitos al aplicar un árbol binario semi-completo.

Comenzamos considerando un arreglo de números (llaves)

$$[4, 1, 6, 8, 9, 5, 2]$$

Dado éste arreglo observamos que si tomamos el índice del primer número (comenzando por 1) y aplicamos la fórmula $2\cdot i+1$ para el hijo izquierdo y $2\cdot i+2$ para el hijo derecho podemos ver que nuestro arreglo ya es un árbol binario completo (en este caso).

\begin{center}
	\begin{tikzpicture}[shorten >=1pt,node distance=1.5cm,on grid,auto] 
		\node[circle, draw] (1) {$4$};
		\node[right of=1, node distance=0.5cm] () {$1$};

		\node[circle, draw, below left of=1] (2) {$1$};
		\node[right of=2, node distance=0.5cm] () {$2$};

		\node[circle, draw, below right of=1] (3) {$6$};
		\node[right of=3, node distance=0.5cm] () {$3$};

		\node[circle, draw, below of=2, left=5pt] (4) {$8$};
		\node[right of=4, node distance=0.5cm] () {$4$};

		\node[circle, draw, below of=2, right=5pt] (5) {$9$};
		\node[right of=5, node distance=0.5cm] () {$5$};

		\node[circle, draw, below of=3, left=5pt] (6) {$5$};
		\node[right of=6, node distance=0.5cm] () {$6$};

		\node[circle, draw, below of=3, right=5pt] (7) {$2$};
		\node[right of=7, node distance=0.5cm] () {$7$};


		\path[-]
		(1)
			edge node {} (2)
			edge node {} (3)
		(2)
			edge node {} (4)
			edge node {} (5)
		(3)
			edge node {} (6)
			edge node {} (7)
		;
	\end{tikzpicture}
	\newline
	\newline
	\textbf{Fig 1.1: Representación de \textit{heap}}
\end{center}

La operación elemental para esta estructura de datos es *heapify*, la cual ordena de acuerdo con la comparación establecida un padre con sus hijos (el sub-árbol más pequeño). En este caso construiremos lo que se conoce como un *max-heap* al comparar con el número mayor.

\begin{center}
	\begin{tikzpicture}[shorten >=1pt,node distance=1.5cm,on grid,auto] 
		\node[circle, draw, below left of=1] (2) {$1$};

		\node[circle, draw, below of=2, left=3pt] (4) {$8$};
		\node[circle, draw, below of=2, right=3pt] (5) {$9$};

		\path[-]
		(2)
			edge node {} (4)
			edge node {} (5)
		;
	\end{tikzpicture}
	$\Rightarrow$
	\begin{tikzpicture}[shorten >=1pt,node distance=1.5cm,on grid,auto] 
		\node[circle, draw, below left of=1] (2) {$9$};

		\node[circle, draw, below of=2, left=3pt] (4) {$8$};
		\node[circle, draw, below of=2, right=3pt] (5) {$1$};

		\path[-]
		(2)
			edge node {} (4)
			edge node {} (5)
		;
	\end{tikzpicture}
	\newline
	\newline
	\textbf{Fig. 1.2: Max-Heapify}
\end{center}

Tomamos ésta como nuestra operación elemental y asumimos que para cualquier árbol al que se le aplique *max-heapify* sus hijos **ya son max-heaps**. Teniendo en cuenta que si a un padre le aplicamos nuestra operación elemental, es decir, lo cambiamos por unos de los hijos, entonces tenemos que asegurar que le hijo sigue siendo *max-heap*, por lo tanto, aplicamos recursivamente al hijo la operación y así sucesivamente. 

\begin{center}
	\begin{tikzpicture}[shorten >=1pt,node distance=1cm,on grid,auto] 
		\node[circle, draw, fill=activeNode] (1) {$4$};
		\node[circle, draw, below left of=1] (2) {$1$};
		\node[circle, draw, below right of=1] (3) {$6$};
		\node[circle, draw, below of=2, left=2pt] (4) {$8$};
		\node[circle, draw, below of=2, right=2pt] (5) {$9$};
		\node[circle, draw, below of=3, left=2pt] (6) {$5$};
		\node[circle, draw, below of=3, right=2pt] (7) {$2$};
		\path[-]
		(1)
			edge node {} (2)
			edge node {} (3)
			edge node {} (3)
		(2)
			edge node {} (4)
			edge node {} (5)
		(3)
			edge node {} (6)
			edge node {} (7)
		;
		\path[->]
		(1)
			edge [out=30, in=30, draw=change] node {} (3)
		;
	\end{tikzpicture}
	$\Rightarrow$
	\begin{tikzpicture}[shorten >=1pt,node distance=1cm,on grid,auto] 
		\node[circle, draw] (1) {$6$};
		\node[circle, draw, below left of=1] (2) {$1$};
		\node[circle, draw, below right of=1, fill=activeNode] (3) {$4$};
		\node[circle, draw, below of=2, left=2pt] (4) {$8$};
		\node[circle, draw, below of=2, right=2pt] (5) {$9$};
		\node[circle, draw, below of=3, left=2pt] (6) {$5$};
		\node[circle, draw, below of=3, right=2pt] (7) {$2$};
		\path[-]
		(1)
			edge node {} (2)
			edge node {} (3)
		(2)
			edge node {} (4)
			edge node {} (5)
		(3)
			edge node {} (6)
			edge node {} (7)
		;
		\path[->]
		(3)
			edge [out=160, in=150, draw=change] node {} (6)
		;
	\end{tikzpicture}
	$\Rightarrow$
	\begin{tikzpicture}[shorten >=1pt,node distance=1cm,on grid,auto] 
		\node[circle, draw] (1) {$6$};
		\node[circle, draw, below left of=1] (2) {$1$};
		\node[circle, draw, below right of=1] (3) {$5$};
		\node[circle, draw, below of=2, left=2pt] (4) {$8$};
		\node[circle, draw, below of=2, right=2pt] (5) {$9$};
		\node[circle, draw, below of=3, left=2pt, fill=activeNode] (6) {$4$};
		\node[circle, draw, below of=3, right=2pt] (7) {$2$};
		\path[-]
		(1)
			edge node {} (2)
			edge node {} (3)
		(2)
			edge node {} (4)
			edge node {} (5)
		(3)
			edge node {} (6)
			edge node {} (7)
		;
	\end{tikzpicture}
	\newline
	\newline
	\textbf{Fig 1.3: Max-Heapify nodo raíz}
\end{center}

Como podemos ver para el peor de los casos para un nodo raíz en un *heap* (asumiendo que todos sus hijos son *max-heaps*) el número de operaciones elementales que realizará es $\lfloor\log_2{n}\rfloor$ donde $n$ es el número de nodos en el árbol. En este caso tenemos que $n=7$ y $\lfloor\log_2{n}\rfloor$=2 y como vemos en la Fig. 1.3 efectivamente se realiza dos veces la operación.

Aprovechando la suposición que todos los nodos hijos ya son *max-heaps* comenzamos nuestro algoritmo de ordenamiento en ${n\over 2}\in \Bbb{N}$[^1] basado en la observación en que **todos los nodos $[{n\over 2}+1,\cdots,n]$ son hojas**. Nos interesan estos nodos en particular ya que al recibir el arreglo nuestra representación no es un *max-heap* por ahota, por lo que, hay que aplicar las operaciones elementales correspondientes para dejarlo en éste estado. De esta manera si comenzamos por los nodos en los que sus hijos son hojas, tenemos asegurado que éstos ya son *max-heaps* por definición.

[^1]: *La división que se realiza es entera, es decir, que $n=2m+r$ y el resultado de aplicar la división entera $n\over 2$ nos da $m$*
[^2]: *Tomamos un árbol binario completo como ejemplo ya que es el peor caso*

\newpage
Ahora comenzamos a analizar el número de operaciones que realizaremos para obtener la complejidad del algoritmo. Dada la estructura de un árbol binario completo[^2] sabemos que el número de nodos a partir de la raíz de puede representar por la siguiente serie

$$1,\, 2,\, 4,\, 8, \cdots, {n+1\over 16}, {n+1\over 8}, {n+1\over 4}, {n+1\over 2}$$

De acuerdo con nuestras observaciones sobre el número máxmo de operaciones para un nodo raíz en un árbol, el número de nodos en cierto nivel y que cualquier nodo intermedio en un árbol binario es por sí solo un árbol binario, podemos ver que el número total de operaciones se da por la siguiente sumatoria

$n_0=n+1$
$${n_0\over 4} \cdot 1 + {n_0\over 8} \cdot 2 + {n_0\over 16} \cdot 3 + \cdots + {n_0\over n_0/2} \cdot ({n_0\over 2} - 1) + {n_0\over n_0}\cdot \log_2{n}$$

$$=(n_0)({1\over 4} \cdot 1 + {1\over 8} \cdot 2 + {1\over 16} \cdot 3 + \cdots + {1\over n_0/2} \cdot ({n_0\over 2} - 1) + {1\over n_0}\cdot \log_2{n})$$

$$=({n_0\over 4})(1 \cdot 1 + {1\over 2} \cdot 2 + {1\over 4} \cdot 3 + \cdots + {1\over n_0/8} \cdot ({n_0\over 2} - 1) + {1\over n_0/4}\cdot \log_2{n})$$

$$=({n_0\over 4})(1 \cdot 1 + {1\over 2} \cdot 2 + {1\over 4} \cdot 3 + \cdots + {1\over n_0/8} \cdot ({n_0\over 2} - 1) + {1\over n_0/4}\cdot \log_2{n})$$

$k=\log_2(n)$

$$={n_0\over 4}\cdot \sum\limits_{i=0}^{k}{{i+1\over 2^i}}$$

Con la prueba de proporción de [d'Alembert](https://en.wikipedia.org/wiki/Ratio_test) podemos ver que la sumatoria converge

$$L=\lim\limits_{n\rightarrow\infty}\Big\lvert{{n+2\over 2^{n+1}}\over{n+1\over 2^n}}\Big\rvert=\lim\limits_{n\rightarrow\infty}\Bigg\lvert{2^n\cdot (n+2)\over 2^{n+1}\cdot (n+1)}\Bigg\rvert=0$$

Dado que

$$(n)2^n+2^{n+1}<(n+1)2^{n+1}$$
$$(n)2^n<(n+1)2^{n+1}-2^{n+1}$$
$$(n)2^n<(n)2^{n+1}$$
$$2^n<2^{n+1}$$

Y finalmente podemos ver que nuestra complejidad se comporta de la siguiente manera

$$\frac{n_0}{4}\sum\limits_{i=0}^{\infty}{{i+1\over 2^i}}=\frac{n_0}{4}(1 + 2 + \frac{3}{4} + \frac{4}{8} + \frac{5}{16}...)= \frac{n_0}{4}\cdot 4=n_0=n+1$$

$$=O(n)$$

\newpage

# Merge Sort

Tomaremos la comparación entre dos número como la operación elemental. Dicho ésto, primero definiremos el procedimiento *merge*, el cual es básico para la demostración de la complejidad del algoritmo *merge sort*.

Supongamos que tenemos dos tuplas[^3], $a$ y $b$, las cuales formarán una tupla, $c$. Para cada paso en este procedimiento haremos una comparación entre $a_i$ y $b_j$ en la cual (definiendo el comparador como el menor o igual) obtenemos $min(a_i, b_j)$ y lo agregamos a $c$. Consecuentemente, si $a_i$ fue el menor de éstos dos, obtenemos $min(a_{i+1}, b_j)$ y así consecutivamente hasta obtener $c$ el cual tendrá todos los valores de $a$ y de $b$ ordenados. Cómo podemos ver esta operación nos toma $|a| + |b|$ operaciones elementales ya que realizamos una operación por cada valor de $a$ y $b$.

$$\therefore merge =O(n)$$

Habiendo definido el procedimiento *merge* podemos comenzar a calcular la complejidad. Dividimos en dos[^4] recursivamente una n-tupla $t$ de manera que nos quedamos con una tupla $a$ y una tupla $b$ tal que

$$a=(t_0,t_1,\cdots,t_{\frac{1}{2}-1})$$
$$b=(t_{\frac{1}{2}},t_{\frac{1}{2}+1},\cdots,t_{n-1})$$

De esta manera podemos continuar dividiendo (recursivamente) las tuplas resultantes y hasta llegar a nuestro caso base el cual es una tupla de cardinalidad $1$ la cual por definición esta ordenada. Al llegar a este punto comenzamos a aplicar el procedimiento *merge* con las tuplas que hemos obtenido como podemos ver en la Fig. 2.1. para la tupla $(4, 2, 5, 3, 1)$

\begin{center}
\begin{tikzpicture}[scale=0.6, every node/.style={scale=0.6},shorten >=1pt,node distance=1.7cm,on grid,auto] 
		\node[circle, draw] (1) {$4, 2, 5, 3, 1$};
		\node[circle, draw, below left of=1] (2) {$4, 2$};
		\node[circle, draw, below right of=1] (3) {$5, 3, 1$};
		\node[circle, draw, below of=2, left=2pt] (4) {$4$};
		\node[circle, draw, below of=2, right=2pt] (5) {$2$};
		\node[circle, draw, below of=3, left=2pt] (6) {$5$};
		\node[circle, draw, below of=3, right=2pt] (7) {$3, 1$};
		\node[circle, draw, below of=7, left=2pt] (8) {$3$};
		\node[circle, draw, below of=7, right=2pt] (9) {$1$};

		\path[-]
		(1)
			edge node {} (2)
			edge node {} (3)
		(2)
			edge node {} (4)
			edge node {} (5)
		(3)
			edge node {} (6)
			edge node {} (7)
		(7)
			edge node {} (8)
			edge node {} (9)
		;
	\end{tikzpicture}
	$\Rightarrow$
	\begin{tikzpicture}[scale=0.6, every node/.style={scale=0.6}, shorten >=1pt,node distance=1.7cm,on grid,auto] 
		\node[circle, draw] (1) {$4, 2, 5, 3, 1$};
		\node[circle, draw, below left of=1] (2) {$4, 2$};
		\node[circle, draw, below right of=1] (3) {$5, 3, 1$};
		\node[circle, draw, below of=2, left=2pt] (4) {$4$};
		\node[circle, draw, below of=2, right=2pt] (5) {$2$};
		\node[circle, draw, below of=3, left=2pt] (6) {$5$};
		\node[circle, draw, below of=3, right=2pt, fill=activeNode] (7) {$1, 3$};

		\path[-]
		(1)
			edge node {} (2)
			edge node {} (3)
		(2)
			edge node {} (4)
			edge node {} (5)
		(3)
			edge node {} (6)
			edge node {} (7)
		;
	\end{tikzpicture}
	$\Rightarrow$
	\begin{tikzpicture}[scale=0.6, every node/.style={scale=0.6},shorten >=1pt,node distance=1.7cm,on grid,auto] 
		\node[circle, draw] (1) {$4, 2, 5, 3, 1$};
		\node[circle, draw, below left of=1, fill=activeNode] (2) {$2, 4$};
		\node[circle, draw, below right of=1, fill=activeNode] (3) {$1, 3, 5$};

		\path[-]
		(1)
			edge node {} (2)
			edge node {} (3)
		;
	\end{tikzpicture}
	$\Rightarrow$
	\begin{tikzpicture}[scale=0.6, every node/.style={scale=0.6},shorten >=1pt,node distance=1.7cm,on grid,auto] 
		\node[circle, draw, fill=activeNode] (1) {$1, 2, 3, 4, 5$}
		;
	\end{tikzpicture}
	\newline
	\newline
	\textbf{Fig 2.1: Ejemplo de Merge Sort}
\end{center}

Teniendo en cuenta todo lo anteriormente definido podemos definir las llamadas recursivas de la siguiente manera

$$T(n)=T(\frac{n}{2})+T(\frac{n}{2})+c\cdot n=2T(\frac{n}{2})+c\cdot n$$

Donde $c$ es una constante que define el tiempo que toma nuestra operación elemental, la comparación. Representando nuestra función recursiva en un árbol (Fig 2.2) de llamadas podemos comenzar a ver la complejidad

\begin{center}
\begin{tikzpicture}[shorten >=1pt,node distance=1cm,on grid,auto] 
		\node (1) {$n$};

		\node [below of=1, left=2pt] (2) {$\frac{n}{2}$};
		\node [below of=1, right=2pt] (3) {$\frac{n}{2}$};

		\node [below of=2, left=5pt] (4) {$\frac{n}{4}$};
		\node [below of=2, right=5.5pt] (5) {$\frac{n}{4}$};
		\node [below of=3, left=5.5pt] (6) {$\frac{n}{4}$};
		\node [below of=3, right=5pt] (7) {$\frac{n}{4}$};

		\node [below of=4, left=10pt] (8) {$\frac{n}{8}$};
		\node [below of=4, left=2pt] (9) {$\frac{n}{8}$};
		\node [below of=5] (10) {$\frac{n}{8}$};
		\node [below of=5, right=2pt] (11) {$\frac{n}{8}$};
		\node [below of=6, left=2pt] (12) {$\frac{n}{8}$};
		\node [below of=6] (13) {$\frac{n}{8}$};
		\node [below of=7, right=2pt] (14) {$\frac{n}{8}$};
		\node [below of=7, right=10pt] (15) {$\frac{n}{8}$};

		\node [below of=10, left=1pt, node distance=0.5cm] (16) {$\vdots$};
		\node [below of=16] (17) {$1\quad 1 \quad 1\quad 1\quad \cdots\quad 1 \quad 1\quad 1\quad 1$};
		
		\path[->]
		(1)
			edge node {} (2)
			edge node {} (3)
		(2)
			edge node {} (4)
			edge node {} (5)
		(3)
			edge node {} (6)
			edge node {} (7)
		(4)
			edge node {} (8)
			edge node {} (9)
		(5)
			edge node {} (10)
			edge node {} (11)
		(6)
			edge node {} (12)
			edge node {} (13)
		(7)
			edge node {} (14)
			edge node {} (15)
		;
	\end{tikzpicture}
\end{center}

Como podemos observar se forma las siguiente sumatoria

$$n+\frac{n}{2}+\frac{n}{2}^2+\frac{n}{4}+\frac{n}{4}+\frac{n}{4}+\frac{n}{4}_4+\cdots+\overbrace{1+1+1+1+1+\cdots+1}^n$$
$$=n+2\cdot \frac{n}{2}+4\cdot \frac{n}{4}+\cdots+n\cdot 1$$
$$=n+\frac{2n}{2}+\frac{4n}{4}+\cdots+n\cdot 1$$
$$=\overbrace{n+n+n+\cdots+n}^{\log_2(n) + 1}$$
$$=n\cdot\log_2(n) + 1$$
$$=n\log_2(n) + n$$
$$=O(n\log_2(n))$$

[^3]: *Definida matemáticamente como una lista ordenada de elementos (en este caso números)*
[^4]: *Tomamos $n/2$ como una división entera tal que si $n=2m+q\Rightarrow \frac{n}{2}=m$*