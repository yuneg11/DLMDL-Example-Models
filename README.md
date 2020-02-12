# DLMDL v3.2 Example Models

## Preparation

Copy datasets to `datasets` folder to train models.
Otherwise, you have to change the paths in `learning_option` of each DLMDL model file.

Copy DLMDL v3.2 compiler to `src` folder to use commands defined in `makefile`.
Otherwise, you have to change `makefile` variables for your environment.

```
root
├ datasets (Place datasets here)
├ logs
├ models
├ src (Place DLMDL v3.2 compiler here)
└ util
```

## Usage

### Compile DLMDL model
```bash
# Using make command
#   model_name: name of model file in models directory without file extension
$ make compile MODEL=<model_name>

# Using direct DLMDL compiler command
#   framework: tf, caffe
#   dlmdl_model: DLMDL file path without file extensiont (ex: models/FLOWERS_AlexNet)
#   output: Output python file path without file extensiont (ex: outs/FLOWERS_AlexNet)
$ python src/UDLI.py --framework=<framework> --input=<dlmdl_model> --compile_out=<output>
```

### Run compiled DLMDL model
```bash
# Using make command
#   model_name: name of model file in models directory without file extension
$ make run MODEL=<model_name>

# Using direct command
#   output: Output python file path without file extensiont (ex: outs/FLOWERS_AlexNet)
$ python <output>.py
```

### Show DLMDL model summary
```bash
# Using make command
#   model_name: name of model file in models directory without file extension
$ make summary MODEL=<model_name>

# Using direct command
#   dlmdl_model: DLMDL file path without file extensiont (ex: models/FLOWERS_AlexNet)
$ python3 util/model_summarizer.py <dlmdl_model>.dlmdl
```

### Visualize DLMDL model training log
```bash
# Using make command
#   log_file: log file path to visualize (You have to make log file manually)
$ make summary LOG=<log_file>

# Using direct command
#   log_file: log file path to visualize (You have to make log file manually)
$ python3 util/log_visualizer.py <log_file>;
```

### Remove compiled DLMDL models
```bash
# Using make command
$ make clean

# Using direct command
#   output_dir: directory of output (ex: outs)
$ rm -f <output_dir>/*.py
```
