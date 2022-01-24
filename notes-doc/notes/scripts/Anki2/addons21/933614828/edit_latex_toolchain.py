from anki import latex

# ["pdfcrop", "--margins", ".5 .5 .5 .5", "tmp.pdf", "tmp.pdf"],

latex.pngCommands = [
    ["pdflatex", "-interaction=nonstopmode", "tmp.tex"],
    ["convert", "-density","150","-quality","90","tmp.pdf", "tmp.png"]
]

latex.svgCommands = [
    ["xelatex", "-interaction=nonstopmode", "-no-pdf", "tmp.tex"],
    ["dvisvgm", "--no-fonts", "-Z", "2", "tmp.xdv", "-o", "tmp.svg"]
]
