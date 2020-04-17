CHOICE = input("Which Pokemon would you like to research? (Enter Name or Dex#, ex- Blastoise or 9): ").lower().strip()
URL = 'https://pokeapi.co/api/v2/pokemon/' + CHOICE + '/'


print(URL)
