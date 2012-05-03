.PHONY: all clean reallyclean

all: paper.pdf poster.pdf

paper.pdf: paper.tex citations.bib counts_graph.png
	pdflatex $< && bibtex paper && pdflatex $< && pdflatex $< 

poster.pdf: poster.tex
	pdflatex $< && pdflatex $< 



%.pdf: %.ps
	ps2pdf $<

clean:
	-rm -f *.aux *.log *.bbl *.blg *.out

reallyclean: clean
	-rm -f paper.pdf
