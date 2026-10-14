# HP Switches API, cURL, Postman & Python Automation

## Overview
This project documents practical API exploration and Python-based network automation for HP and Aruba switches. It includes SSH connectivity, command execution, VLAN retrieval, device information and login/logout examples using Netmiko and Paramiko.

## Supported Lab Devices
- Aruba 2530
- HP 1950
- HPE 5510

## Requirements
- Ubuntu or another Linux environment
- Python 3.12 or compatible version
- SSH access to supported switches
- Netmiko and Paramiko
- cURL and Postman for API learning examples as they are added

## Installation

Clone the repository:

```bash
git clone <REPOSITORY_URL>
cd <REPOSITORY_FOLDER>
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Copy the example configuration:

```bash
cp credentials.example.py credentials.py
```

Edit `credentials.py` with your own switch IP addresses, usernames, passwords, SSH ports and, where required, HP 1950 extended CLI credentials.

**Security:** Never commit `credentials.py` or real credentials. Use only placeholders in example files.

## Running the Scripts

Run scripts from the activated virtual environment:

```bash
python aruba2530_getvlans.py
python aruba2530_netmiko_showversion.py
python hp1950_netmiko_dispversion.py
python hpe5510_netmiko.py
```

Use the appropriate script for your device and verify its configuration before execution.

## Project Structure

- `aruba2530_*.py` — Aruba 2530 connectivity and command examples
- `hp1950_*.py` — HP 1950 connectivity and command examples
- `hpe5510_*.py` — HPE 5510 connectivity example
- `credentials.example.py` — Safe configuration template
- `requirements.txt` — Python dependencies

## Security and Responsible Use

- Use only switches you own or are authorized to administer.
- Keep credentials and sensitive network information out of public commits.
- Replace example IP addresses with your own lab addresses.
- Review commands before running them on production equipment.

## Future Enhancements

- cURL and Postman API examples
- Improved error handling and logging
- Additional automation and documentation

## License

See the repository's `LICENSE` file once added.

## Script Reference

| Script | Purpose |
|---|---|
| `aruba2530_getvlans.py` | Retrieve VLAN information from an Aruba 2530 switch. |
| `aruba2530_login.py` | Demonstrate SSH login to an Aruba 2530 switch. |
| `aruba2530_logout.py` | Demonstrate SSH logout/session handling for an Aruba 2530 switch. |
| `aruba2530_netmiko.py` | Demonstrate switch connectivity using Netmiko. |
| `aruba2530_netmiko_showversion.py` | Retrieve switch version information using Netmiko. |
| `aruba2530_paramiko.py` | Demonstrate SSH connectivity using Paramiko. |
| `aruba2530_paramiko_rocommand.py` | Execute a read-only command using Paramiko. |
| `hp1950_netmiko.py` | Demonstrate Netmiko connectivity to an HP 1950 switch. |
| `hp1950_netmiko_dispversion.py` | Demonstrate HP 1950 extended CLI authentication and version retrieval. |
| `hpe5510_netmiko.py` | Demonstrate Netmiko connectivity and command execution on an HPE 5510 switch. |

**Note:** These scripts are lab examples. Review each script and verify the target device, credentials, SSH port, and command support before execution.

## Troubleshooting

- **ModuleNotFoundError:** Activate the virtual environment and run `pip install -r requirements.txt`.
- **SSH connection timeout:** Verify the switch IP address, network reachability, SSH service, and configured SSH port.
- **Authentication failure:** Verify the username and password in your local `credentials.py` file.
- **HP 1950 extended CLI failure:** Verify that extended CLI mode is supported and that the required confirmation and extended CLI password are handled correctly.
- **Command not recognized:** Check the switch model, firmware version, CLI mode, and command syntax.
- **Credentials module not found:** Ensure `credentials.py` exists in the project directory and matches the structure of `credentials.example.py`.
- **Permission or connection errors:** Check network access, account privileges, and device-side restrictions.

Run these examples only against switches you own or are authorized to administer.
