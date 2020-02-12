CCPATH = src/UDLI.py
MSPATH = util/model_summarizer.py
LVPATH = util/log_visualizer.py
MODELDIR = models
OUTDIR = outs

FRAMEWORK = tf
MODEL ?= MODEL_NAME

all: compile summary

compile: $(MODELDIR)/$(MODEL).dlmdl
	python $(CCPATH) --framework=$(FRAMEWORK) --input=$(MODELDIR)/$(MODEL) --compile_out=$(OUTDIR)/$(MODEL)

run:
	python $(OUTDIR)/$(MODEL).py

summary:
	python3 $(MSPATH) $(MODELDIR)/$(MODEL).dlmdl

visualize:
	python3 $(LVPATH) $(LOG)

clean:
	rm -f $(OUTDIR)/*.py
