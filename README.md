
# MalwareBazaar Sample Fetcher 🛡️

This Python script interacts with the Abuse.ch API to fetch the latest malware samples from the past 60 minutes and saves them to a JSON file.

## Getting Started 🚀

### Prerequisites 📋

Before running this script, you need to have:

- Python 3.x installed on your machine.
- `requests` library installed. You can install it using pip:

  ```shell
  pip install requests
  ```

## Running the Script 🏃‍♂️

To execute the script, simply run the following command in your terminal:

```shell
python3 mb-recent.py
```

## Results 📄

The script will save the fetched malware samples to a file named `malware_samples.json` in the current directory.

## Automation with Crontab ⏲️

If you wish to automate the running of this script, you can schedule it using `crontab` on Unix-based systems:

1. Open your terminal and enter `crontab -e` to edit your crontab file.
2. Schedule the script to run at your desired interval. For example, to run the script every hour, add:

   ```shell
   0 * * * * /usr/bin/python3 /path/to/your/malware_sample_fetcher.py >> /path/to/your/cron.log 2>&1
   ```

   Replace `/path/to/your/` with the actual path to the script and `cron.log`.

   Or you can use [Crontab Generator](https://crontab-generator.org).

4. Save and exit the editor. The `crontab` service will handle the rest.

## Note 📝

- The script interacts with a third-party API and its availability is subject to that service's uptime.
- Ensure that you have the necessary permissions and are complying with the terms of use for the Abuse.ch API when using this script.

## License 📜

This project is open-sourced under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments 👏

- Kudos to the Abuse.ch API for providing the data used by this script.
