
## Files

- **.gitignore**: Specifies files to be ignored by git.
- **alpaca/config.ini**: Configuration file containing API keys and base URL.
- **alpaca/config.ini_example**: Example configuration file with placeholder values.
- **alpaca/test_config.py**: Script to read and validate the configuration file.
- **alpaca/test.py**: Script to interact with the Alpaca API using the configuration.
- **requirements.txt**: Lists the dependencies required for the project.

## Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Cjaimesg/apaca-api.git
    cd <repository-directory>
    ```

2. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Configure API keys**:
    - Copy [config.ini_example](http://_vscodecontentref_/5) to [config.ini](http://_vscodecontentref_/6).
    - Replace the placeholder values in [config.ini](http://_vscodecontentref_/7) with your actual Alpaca API keys and base URL.

## Usage

1. **Run the configuration test**:
    ```sh
    python alpaca/test_config.py
    ```

2. **Run the Alpaca API test**:
    ```sh
    python alpaca/test.py
    ```

## License

This project is licensed under the MIT License.