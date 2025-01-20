from klassen import Magier, Schurke, Goblin, GoblinKoenig, Kampf

def main():
    magier = Magier("Gandalf", 100, 15, 5, 50)
    schurke = Schurke("Loki", 80, 10, 3, 25)
    goblin = Goblin("Goblin", 50, 7, 2)
    goblin_koenig = GoblinKoenig("Goblin-König", 200, 20, 8)

    print("Kampf 1: Gandalf gegen Goblin")
    print(Kampf.kampf_szenario(magier, goblin))

    print("\nKampf 2: Loki gegen Goblin-König")
    print(Kampf.kampf_szenario(schurke, goblin_koenig))

if __name__ == "__main__":
    main()
