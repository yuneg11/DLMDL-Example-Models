import pandas as pd
import json
import sys

pd.set_option('display.max_rows', 1000)


def show_model(model):
    def show_layers(layers):
        index = [
            ("name", "name"),
            ("num_output", "attributes.num_output"),
            ("kernel_size", "attributes.kernel_size"),
            ("stride", "attributes.stride"),
            ("padding", "attributes.padding"),
            ("dropout", "attributes.dropout_ratio")
        ]
        data = dict([[label, []] for label, _ in index])
        for layer in layers:
            for label, key in index:
                try:
                    value = layer
                    for subkey in key.split("."):
                        value = value[subkey]
                    data[label].append(value)
                except:
                    data[label].append("")
        df = pd.DataFrame(data)

        print("=" * 80)
        print(df)
        print("=" * 80)
    def show_learning_option(learning_option):
        pass

    show_layers(model["layers"])
    show_learning_option(model["learning_option"])


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: " + sys.argv[0] + " <model_file_name>")
        exit()

    model_file_name = sys.argv[1]
    with open(model_file_name, "r") as model_file:
        model = json.load(model_file)
        show_model(model)
