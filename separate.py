import subprocess
from colorama import Fore
import os

def separate(filePath, output_directory):        
    command = f"python -m spleeter separate {filePath} -o {output_directory} -p spleeter:2stems"

    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        if result.stdout.decode().__contains__("succesfully"):
            print(Fore.GREEN, "Succesfully separated song", Fore.RESET)

            # JUST NU TAR DNE FILEPATH, DEN SKA BARA TA FILENAME I FRAMTIDEN
            song_name = os.path.splitext(os.path.basename(filePath))[0]
            song_output_path = os.path.join(output_directory, song_name)

            if os.path.isdir(song_output_path):  
                for stem in os.listdir(song_output_path):
                    stem_path = os.path.join(song_output_path, stem)
                    if os.path.isdir(stem_path):
                        files = os.listdir(stem_path)
                        for file in files:
                            if os.path.join(stem_path, file).__conatins__("vocals"):
                                print(os.path.join(stem_path, file).__conatins__("vocals"))
                                print("HEJSAN HOPPSAN")
                                return os.path.join(stem_path, file).__conatins__("vocals")
                    else:
                        # Om inga sub_directories existerar
                        print(stem_path)
                        print("HEJSAN HOPPSAN 123321")
                        if stem_path.__contains__("vocals"):
                            return stem_path
    except Exception as e:
        print("An error occurred:", e)
