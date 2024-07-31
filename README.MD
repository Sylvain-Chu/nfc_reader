### README for using `nfc_log.exe`

#### Introduction
This guide explains how to use the `nfc_log.exe` executable to read NFC badges with the ACR122U reader and write the badge IDs to where your cursor is, followed by a newline. The executable also prevents the same badge from being scanned twice in a row.

#### Prerequisites

1. **NFC Reader**: ACR122U
2. **Drivers**: Install the drivers for the ACR122U reader from the official ACS website:
   - [ACR122U Driver](https://www.acs.com.hk/en/driver/3/acr122u-usb-nfc-reader/)

#### Driver Installation

1. Download the driver for the ACR122U reader from the provided link.
2. Run the installer and follow the on-screen instructions to install the driver.
3. Once the installation is complete, connect your ACR122U reader to your computer.

#### Using `nfc_log.exe`

1. **Download and Extract**
   - Download the `nfc_log.exe` executable and place it in a directory of your choice.

2. **Running `nfc_log.exe`**
   - Double-click `nfc_log.exe` to run the program.
   - A console window will open, indicating that the NFC reader is starting.

3. **Scanning NFC Badges**
   - Place an NFC badge on the ACR122U reader.
   - The badge ID will be automatically written to where your mouse cursor is, followed by a newline.
   - If the same badge is scanned twice in a row, the program will not duplicate the badge ID.

4. **Stopping the Program**
   - To stop the program, simply close the console window or press `Ctrl+C` in the console.

#### Example Usage

1. Open a text editor or document (such as Notepad, Word, or a form field).
2. Place the cursor where you want the badge IDs to be written.
3. Run `nfc_log.exe`.
4. Place the NFC badges on the ACR122U reader. The badge ID will appear at the cursor position, followed by a newline after each scan.

#### Notes

- Ensure that the cursor is placed in a text input area before scanning badges.
- Make sure the NFC reader is properly connected and recognized by your system before running `nfc_log.exe`.

### Troubleshooting

1. **NFC Reader Not Detected:**
   - Ensure that the NFC reader is properly connected to your computer.
   - Verify that the drivers are installed and that the reader is recognized by the operating system.

2. **Badge ID Not Displayed:**
   - Ensure that the cursor is placed in a text input area before scanning badges.
   - Verify that the NFC badge is compatible with the ACR122U reader.

For any questions or issues, please contact technical support or refer to the ACR122U reader documentation.