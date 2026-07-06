import os
from src.game import GameEngine

def display_dashboard(player):
    """Prints out the current status, level, and health profile of your hero."""
    print("\n=========================================")
    print(f"🧙 HERO: {player.name:<12} | CLASS: {player.role}")
    print(f"🌟 LEVEL: {player.level:<11} | XP: {player.xp}")
    print(f"❤️ HEALTH: {player.current_health}/{player.max_health:<9} | ATK: {player.attack_power}")
    print("=========================================")

def main():
    data_directory = "data"
    file_path = os.path.join(data_directory, "save_data.json")
    
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
        
    # Launch our primary RPG orchestrator engine instance
    rpg_core = GameEngine(file_path)
    
    print("=========================================")
    print("⚔️ WELCOME TO THE TEXT-BASED RPG WORLD ⚔️")
    print("=========================================")
    
    # Check if a save profile already exists on disk
    has_save = rpg_core.load_game()
    
    if has_save == True:
        print(f"Found saved data for {rpg_core.player.name}!")
        choice = input("1. Continue Quest\n2. Start Fresh\nChoose option (1-2): ").strip()
        if choice != "1":
            has_save = False
            
    if has_save == False:
        print("\n--- Create Your Character ---")
        name = input("Enter Character Name: ").strip()
        if not name:
            name = "Hero"
            
        print("\nChoose Your Class Archetype:")
        print("1. Warrior (High Health, Solid Damage)")
        print("2. Mage    (Lower Health, Devastating Spells)")
        role_choice = input("Select Class (1-2): ").strip()
        
        rpg_core.create_new_player(name, role_choice)
        print(f"\nWelcome to the realm, {rpg_core.player.name}!")

    # Exploration Event Loop
    while True:
        display_dashboard(rpg_core.player)
        print("1. 🗺️ Explore the Wilds (Look for Encounters)")
        print("2. 💤 Rest at Inn (Fully Restore Health)")
        print("3. 💾 Save Progress & Exit Game")
        
        action = input("What would you like to do? ").strip()
        
        if action == "1":
            # Generate a random enemy matching player scaling thresholds
            monster = rpg_core.generate_random_enemy()
            # Trigger the turn-based combat arena loop
            rpg_core.start_combat_arena(monster)
            
            # Post-combat safety check: Did the player perish?
            if not rpg_core.player.is_alive():
                print("\n☠️ Game Over! Deleting corrupted save profile details...")
                if os.path.exists(file_path):
                    os.remove(file_path)
                break
                
        elif action == "2":
            print("\nResting at the local tavern inn...")
            rpg_core.player.current_health = rpg_core.player.max_health
            print("💚 Health fully restored to maximum limits!")
            rpg_core.save_game()
            
        elif action == "3":
            rpg_core.save_game()
            print("Farewell, adventurer! Your progress has been sealed safely.")
            break
        else:
            print("Invalid command! Your choice fell into deep oblivion.")

if __name__ == "__main__":
    main()