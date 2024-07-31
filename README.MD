## NFC Reader

This project allows you to read NFC badges using the ACR122U reader and writes the badge IDs where your cursor is, followed by a newline.

### Prerequisites

1. **NFC Reader**: ACR122U
2. **Drivers**: Install the drivers for the ACR122U reader from the official ACS website:
   - [ACR122U Driver](https://www.acs.com.hk/en/driver/3/acr122u-usb-nfc-reader/)

### Installation

1. **Download the executable**:
   - Go to the [releases page](https://github.com/<your-username>/<your-repo>/releases) to download the latest version of `nfc_reader.exe`.

2. **Run the executable**:
   - Double-click `nfc_reader.exe` to start the program.
   - A console window will open, indicating that the NFC reader is starting.

### Usage

1. Open a text editor or document (such as Notepad, Word, or a form field).
2. Place the cursor where you want the badge IDs to be written.
3. Run `nfc_reader.exe`.
4. Place the NFC badges on the ACR122U reader. The badge ID will appear at the cursor position, followed by a newline after each scan.

### Notes

- Ensure that the cursor is placed in a text input area before scanning badges.
- Make sure the NFC reader is properly connected and recognized by your system before running `nfc_reader.exe`.

### Troubleshooting

1. **NFC Reader Not Detected:**
   - Ensure that the NFC reader is properly connected to your computer.
   - Verify that the drivers are installed and that the reader is recognized by the operating system.

2. **Badge ID Not Displayed:**
   - Ensure that the cursor is placed in a text input area before scanning badges.
   - Verify that the NFC badge is compatible with the ACR122U reader.

For any questions or issues, please contact technical support or refer to the ACR122U reader documentation.
