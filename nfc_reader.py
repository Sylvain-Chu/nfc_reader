import logging
import time
import pyautogui
from smartcard.System import readers
from smartcard.util import toHexString
from smartcard.Exceptions import NoCardException, CardConnectionException

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

last_badge_id = None

def read_nfc():
    global last_badge_id
    try:
        available_readers = readers()
        if len(available_readers) == 0:
            logging.error("No NFC readers found.")
            return

        reader = available_readers[0]
        connection = reader.createConnection()

        try:
            connection.connect()
        except (NoCardException, CardConnectionException):
            return

        get_uid = [0xFF, 0xCA, 0x00, 0x00, 0x00]
        try:
            data, sw1, sw2 = connection.transmit(get_uid)
            if sw1 == 0x90 and sw2 == 0x00:
                badge_id = toHexString(data)
                if badge_id != last_badge_id:
                    logging.info(f"Badge ID: {badge_id}")
                    pyautogui.typewrite(badge_id)  
                    pyautogui.press('enter') 
                    logging.info("Badge ID written at cursor position.")
                    last_badge_id = badge_id
            else:
                logging.error(f"Failed to read badge. SW1: {sw1}, SW2: {sw2}")
        except CardConnectionException as e:
            logging.error(f"Card connection error: {e}")
    except Exception as e:
        logging.error(f"Error reading NFC: {e}")

def main():
    logging.info("Starting NFC reader...")
    try:
        while True:
            read_nfc()
            time.sleep(1.5)
    except KeyboardInterrupt:
        logging.info("NFC reader stopped by user.")

if __name__ == "__main__":
    main()
