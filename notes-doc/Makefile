SOURCE_MD := $(shell find ce6fa/99c4a/science/chemistry/organic/ -name "*.md")
SOURCE_CARDS := $(shell find ce6fa/112bb5f/science/biology/botany/panatomy/complex/ -name "*.md")

EXPORTED_MD=\
 $(SOURCE_MD:.md=.pdf) \

CARDS_CONFIG=\
 $(SOURCE_CARDS:.md=.cards) \

PANDOC=/usr/bin/pandoc

PANDOC_OPTIONS=--standalone --from markdown+tex_math_single_backslash+tex_math_double_backslash+tex_math_dollars --verbose 

MNEMOCARDS=/usr/bin/mnemocards

PANDOC_PDF_OPTIONS=--template hovel 

%.pdf : %.md
	mkdir -p 99d0afe/$(dir $@)  
	$(PANDOC) $(PANDOC_OPTIONS) $(PANDOC_PDF_OPTIONS) -o 99d0afe/$@ $<

%.cards : %.md
	mkdir -p 99d0afe/$(dir $@)
	cp  $< 99d0afe/$@
	cp  e1d99d/cconfig.json 99d0afe/$(dir $@)cards_config.json
	cd 99d0afe/$(dir $@); $(MNEMOCARDS) generate --output-dir ./ -f cards_config.json ./ ; mnemocards import -c /mnt/pool/doc/anki/gen/collection.anki2 README.apkg 

ccards: $(CARDS_CONFIG)

document: $(EXPORTED_MD)

.PHONY: all clean


