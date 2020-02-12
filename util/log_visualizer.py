from matplotlib import pyplot as plt
from matplotlib import gridspec
import numpy as np
import sys
import re

# Regex
capture_train_regex = re.compile("\[\s*(\d+) Steps\] Train Loss: \s*(\d+.\d+), Train accuracy: (\d.\d+)\(\s*(\d+.\d+) sec/batch\)")
capture_test_regex = re.compile("\[\s*(\d+) Steps\] Average Test accuracy: (\d.\d+)")

def parse_log(log_text):
    log = {
        "train": {
            "loss": {
                "step": [],
                "value": []
            },
            "accuracy": {
                "step": [],
                "value": []
            },
            "time": {
                "step": [],
                "value": []
            }
        },
        "test": {
            "accuracy": {
                "step": [],
                "value": []
            }
        }
    }

    for log_line in log_text.splitlines():
        if log_line.find("Train accuracy") > 0:
            groups = capture_train_regex.match(log_line)
            step, loss, accuracy, time = int(groups.group(1)), float(groups.group(2)), float(groups.group(3)), float(groups.group(4))
            log["train"]["loss"]["step"].append(step)
            log["train"]["loss"]["value"].append(loss)
            log["train"]["accuracy"]["step"].append(step)
            log["train"]["accuracy"]["value"].append(accuracy)
            log["train"]["time"]["step"].append(step)
            log["train"]["time"]["value"].append(time)
        elif log_line.find("Average Test accuracy") > 0:
            groups = capture_test_regex.match(log_line)
            step, accuracy = int(groups.group(1)), float(groups.group(2))
            log["test"]["accuracy"]["step"].append(step)
            log["test"]["accuracy"]["value"].append(accuracy)

    return log


def build_and_save_graph(log, graph_file_name):
    fig = plt.figure()
    fig.suptitle("Train and Test Metrics")
    gs = gridspec.GridSpec(nrows=2, ncols=1)
    axs = [plt.subplot(gsidx) for gsidx in gs]

    axs[0] = plt.subplot(2, 1, 1)
    axs[0].set_ylabel("Accuracy")
    # axs[0].set_xlabel("Step")
    axs[0].plot(log["train"]["accuracy"]["step"], log["train"]["accuracy"]["value"])
    axs[0].plot(log["test"]["accuracy"]["step"], log["test"]["accuracy"]["value"])
    axs[0].legend(["Train", "Test"])

    axs[1] = plt.subplot(2, 1, 2)
    axs[1].set_ylabel("Loss")
    axs[1].set_xlabel("Step")
    axs[1].plot(log["train"]["loss"]["step"], log["train"]["loss"]["value"])
    axs[1].legend(["Train"])

    plt.savefig(graph_file_name)


if __name__ == "__main__":
    log_file_name = sys.argv[1]
    if len(sys.argv) >= 3:
        graph_file_name = sys.argv[2]
    else:
        graph_file_name = sys.argv[1].replace(".log", ".png").replace(".txt", ".png")

    with open(log_file_name, "r") as log_file:
        log_text = log_file.read()

    build_and_save_graph(parse_log(log_text), graph_file_name)
