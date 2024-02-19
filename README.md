Hejsan svejsan kära william,
här kommer det lite mysiga instruktioner för isolering av röst från ljudfil
vänligen ladda ned FFmpeg från denna mycket inte sketchiga länk
https://github.com/BtbN/FFmpeg-Builds/releases 
lägg sedan till pathen till bin filen från den extraherade filen (no virus trust me bro) i dina vackra och kurviga environmental variables
*hmpf* nånting ... pip install -r requirements.txt ... *hmpf* *hmpf* glömde inte alls skriva det *hmpf* 
därefter får du hjärtligt vänligen utöva detta kommando i valfri terminal:
python -m spleeter separate (uppatadata da file pahh) -o output_directory -p spleeter:2stems 
promise no rce included *wink* *wink*
pilla *wink* sedan lite on da code och uppdatera lite file pahh (du hittar hoppas jag)
nej men det var allt puss på dig min raraste sötaste pookie bear

pssssss... jag brukar icket kirra något mysigt litet rum för mina python projekt så du får med några extra modules på köpet 😉 

OCH JUSTE
kan vara så att spleeter modulen är lite konstig i bollen så att säga så för att installera den felfritt (det som funkade för mig) var med python 3.10.1 och pip 21.2.4, sedan en lätt ´pip install spleeter´, det var något konstigt med numpy versionen som spleeter var kompatibel med men dem fixar säkert det snart