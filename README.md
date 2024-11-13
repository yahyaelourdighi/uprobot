# UpRobot - Website Monitoring Tool

UpRobot is a simple and powerful website monitoring tool that checks the "UP" and "DOWN" statuses of websites. It fetches the status, HTTP response codes, and logs results with time stamps, including the user’s public IP address and destination IP of the websites. The tool also allows you to monitor websites either manually or from a file.

![robot](https://github.com/user-attachments/assets/06c69ccd-dacf-43fc-9cae-98b75f1fe8f3)


## Features

- **Website Monitoring**: Check if websites are up or down.
- **Public IP Logging**: Displays the user's public IP address for each check.
- **Fast and Slow Scans**: Choose between fast and slow scan speeds.
- **Status Saving**: Optionally save "UP" status websites to a file.
- **Error Handling**: Graceful error handling with detailed output.
- **Support for Manual and File-Based Input**: Input websites manually or load them from a file.
- **Time Stamps**: Every check includes a time stamp for tracking.

## Requirements

- `requests`: To send HTTP requests and check the website status.
- `pyfiglet`: To display the tool's header in a stylized ASCII format.
- `colorama`: For colored terminal output.

## Installation

### Clone the repository:
```bash
git clone https://github.com/yahyaelourdighi/website-monitoring-tool.git
cd website-monitoring-tool
```

### Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Tool

Run the script using the following command:

```bash
python uprobot.py
```

### Input Methods

You can choose to input websites in two ways:

1. **Manually**: Input websites directly (comma-separated).
2. **From a file**: Provide a text file containing the list of websites.

### Scan Speed

Choose between:

- **Fast**: Faster scans with a shorter delay.
- **Slow**: Slower scans with a longer delay.

### Saving Results

You can save only the "UP" statuses to a file. If you choose to do so, the tool will ask you for the file name to save the results.

### Example Output:

```
===========================================
Website Monitoring Tool - Check the UP/DOWN status of websites.
===========================================
Tool created by Yahya El Ourdighi
https://www.linkedin.com/in/yahya-el-ourdighi-175028244/
https://github.com/yahyaelourdighi

Input websites manually or from a file? (manual/file): manual
Enter websites to monitor (comma-separated): google.com, example.com
Choose scan speed (fast/slow): fast
Save only 'UP' statuses to a file? (yes/no): no

Starting website monitoring...

2024-11-13 15:30:22 | google.com | UP | 200 | SrcIP: 192.168.1.1 | DstIP: 142.250.183.78
2024-11-13 15:30:22 | example.com | DOWN | 404 | SrcIP: 192.168.1.1 | DstIP: 93.184.216.34

Summary:
UP: 1
DOWN: 1
ERROR: 0
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Contributing

Feel free to fork this repository and make changes to improve the tool. If you have any ideas or features you'd like to see, open an issue or create a pull request!
