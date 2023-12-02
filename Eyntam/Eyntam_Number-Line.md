# The Number Line
- A line that compares numbers, placing smaller numbers at the left and larger numbers at the right


## Examples
```tikz
\usetikzlibrary{arrows}
\begin{document}
    \begin{tikzpicture}[scale=2]
        \draw[latex-latex] (-3.5,0) -- (3.5,0);
        \foreach \x in  {-3,-2,-1,0,1,2,3}
            \draw[shift={(\x,0)},color=black] (0pt,3pt) -- (0pt,-3pt);
        \foreach \x in {-3,-2,-1,0,1,2,3}
            \draw[shift={(\x,0)},color=black] (0pt,0pt) -- (0pt,-3pt) node[below] 
            {$\x$};
    \end{tikzpicture}
\end{document}
```

- Numbers can also be represented with fractions

```tikz
\usetikzlibrary{arrows}
\usetikzlibrary{math}
\begin{document}
    \begin{tikzpicture}[scale=2]
        \draw[latex-latex] (-3.5,0) -- (3.5,0);

        \foreach \x in  {-3,-2,-1,0,1,2,3}
            \draw[shift={(\x,0)},color=black] (0pt,3pt) -- (0pt,-3pt);

        \foreach \x in {-3,-2,-1,0,1,2,3}
            \draw[shift={(\x,0)},color=black] (0pt,0pt) -- (0pt,-3pt) node[below] 
            {$\x$};

        \foreach \x in {-2.38, -3/4, 0, 1, 1/2, 2, 3}
            \draw[shift={(\x,3pt)},color=black] (0pt,0pt) -- (0pt,-3pt) node[above] 
            {$\x$};
    \end{tikzpicture}
\end{document}
```
