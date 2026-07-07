import os
from src.generator import QRGenerator
from src.logger import HistoryLogger

def display_menu():
    """Prints out the user control configurations panel option indexes."""
    print("\n====== CUSTOM QR CODE CONFIGURATOR ======")
    print("1. Compile Fresh Custom QR Graphic")
    print("2. Display System Operational Logs")
    print("3. Shutdown Configuration Station")
    print("=========================================")

def main():
    log_path = "data/generation_history.log"
    
    # Initialize our backend manager tool instances
    generator = QRGenerator(output_dir="outputs")
    logger = HistoryLogger(log_path=log_path)
    
    print("=========================================")
    print(" WELCOME TO THE PIXEL QR CODE GENERATOR  ")
    print("=========================================")
    
    while True:
        display_menu()
        choice = input("Select an action panel (1-3): ").strip()
        
        if choice == "1":
            print("\n--- QR Code Input Extraction ---")
            data = input("Enter Text payload or URL link to encode: ").strip()
            if not data:
                print("Error: Encoding data payload cannot be left completely blank!")
                continue
                
            file_name = input("Enter output graphic file name (e.g., my_link): ").strip()
            if not file_name:
                file_name = "qr_export"
                
            # Guarantee standard file path tracking checks
            if not file_name.endswith(".png"):
                file_name = file_name + ".png"
                
            target_check = os.path.join("outputs", file_name)
            if os.path.exists(target_check):
                overwrite = input(f"Warning: '{file_name}' already exists! Overwrite? (y/n): ").strip().lower()
                if overwrite != "y":
                    print("Operation aborted by user.")
                    continue

            print("\n--- Custom Colorization (Optional) ---")
            print("You can type standard color names (e.g., black, white, blue, red, darkblue)")
            fill = input("Enter grid square color [Default: black]: ").strip() or "black"
            back = input("Enter canvas background color [Default: white]: ").strip() or "white"
            
            try:
                # Trigger pixel composition and compilation operations inside generator layer
                exported_path = generator.generate_qr(
                    data=data,
                    file_name=file_name,
                    fill_color=fill,
                    back_color=back
                )
                
                # Commit successful action summary to historical text audit log file
                logger.log_entry(data_payload=data, file_name=file_name)
                
            except ValueError:
                print("Error: One of the entered color names is invalid! Canvas generation failed.")
            except Exception as e:
                print(f"An unexpected imaging error occurred: {e}")
                
        elif choice == "2":
            print("\n--- Reading System Historical Logs ---")
            if os.path.exists(log_path):
                with open(log_path, "r", encoding="utf-8") as file:
                    log_data = file.read()
                    if log_data.strip() == "":
                        print("The audit tracking logs are currently completely empty.")
                    else:
                        print(log_data)
            else:
                print("No history logs found yet. Generate a QR code first!")
                
        elif choice == "3":
            print("\nClosing imaging matrix pipelines safely. Connection closed!")
            break
        else:
            print("Invalid administration command choice! Please input an index option from 1 to 3.")

if __name__ == "__main__":
    main()