# Positive and Negative Numbers
- Positive numbers describe values greater than $0$
    - They have a $+$ (plus) sign at the front or no sign at all
        $$+4 = 4$$
- Negative numbers describe values lesser than $0$
    - They have a $-$ (minus) sign at the front
        $$-4$$

- They can be placed on a [Number Line](./Eyntam_Number-Line.md)

    ```tikz
    \usetikzlibrary{arrows}
    \begin{document}
        \begin{tikzpicture}[scale=1.5]
            \draw[latex-latex] (-4.5,0) -- (4.5,0);
            \foreach \x in  {-4, -3,-2,-1, 0, 1, 2, 3, 4}
                \draw[shift={(\x,0)},color=black] (0pt,3pt) -- (0pt,-3pt);
            \foreach \x in {-4, -3,-2,-1, 0, 1, 2, 3, 4}
                \draw[shift={(\x,0)},color=black] (0pt,0pt) -- (0pt,-3pt) node[below] 
                {$\x$};
        \end{tikzpicture}
    \end{document}
    ```

    - Any number is at the same distance from zero as its opposite
