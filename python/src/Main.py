import sys
from ConfigFile import ConfigFile
from Dataset import Dataset
from Detector import Detector
from Nsa import Nsa


def init_search_space(config_file: ConfigFile):
    config_file.setSearchSpace()
    for i in range(config_file.problemSize):
        config_file.setSearchSpaceIndex(0.0, (2 * i))
        config_file.setSearchSpaceIndex(1.0, (2 * i + 1))


def run(config_file: ConfigFile):
    general_results: list = list()
    init_search_space(config_file)
    traning_dataset = Dataset(
        config_file.traning_dataset_csv_file
    )
    testing_dataset = Dataset(
        config_file.testing_dataset_csv_file
    )
    self_dataset_for_training = traning_dataset.read()
    generate_self_dataset_for_testing = testing_dataset.read()
    training_detectors = Detector(config_file, self_dataset_for_training)
    testing_detectors = Detector(
        config_file, generate_self_dataset_for_testing)
    nsa = Nsa(training=training_detectors, detection=testing_detectors,
              results=general_results, configs=config_file)
    nsa.run()


def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        configFile = ConfigFile(filename)
        run(configFile)
    else:
        print(f'Usage {sys.argv[0]} <CONFIG-FILE>')
        return -1

    return 0


if __name__ == '__main__':
    main()
