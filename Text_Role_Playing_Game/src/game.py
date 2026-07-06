import json
import os
import random
from src.character import Character

class GameEngine:
    def __init__(self, save_path):
        self.save_path = save_path
        self.player = None
        
        # Array pool of potential monster types, structural base stats, and descriptions
        self.monster_templates = [
            {"name": "Slime", "role": "Beast", "health": 20, "attack": 4, "xp_reward": 15},
            {"name": "Goblin Scout", "role": "Goblin", "health": 35, "attack": 7, "xp_reward": 25},
            {"name": "Orc Warrior", "role": "Orc", "health": 55, "attack": 12, "xp_reward": 45},
            {"name": "Shadow Dragon", "role": "Boss", "health": 100, "attack": 18, "xp_reward": 100}
        ]

    def load_game(self):
        """Loads saved player progress profile details from JSON storage."""
        if os.path.exists(self.save_path):
            with open(self.save_path, "r") as file:
                data = json.load(file)
                self.player = Character(
                    name=data["name"],
                    role=data["role"],
                    health=data["max_health"],
                    attack_power=data["attack_power"],
                    xp=data["xp"],
                    level=data["level"]
                )
                # Restore mid-game current health parameters safely
                self.player.current_health = data["current_health"]
            return True
        return False

    def save_game(self):
        """Saves current player character progression stats to file."""
        if self.player != None:
            with open(self.save_path, "w") as file:
                json.dump(self.player.to_dict(), file, indent=4)
            print("💾 Game progress backed up safely inside the local archives.")

    def create_new_player(self, name, role_choice):
        """Generates a fresh starting hero class profile matching the chosen role archetype."""
        # Setup specific role distributions: Warriors have high health, Mages have high damage
        if role_choice == "1":
            self.player = Character(name, "Warrior", health=60, attack_power=10)
        else:
            self.player = Character(name, "Mage", health=40, attack_power=15)
        self.save_game()

    def generate_random_enemy(self):
        """Selects a random monster template from the pool based on the player's level."""
        # Scale the selection list context so beginners don't face dragons instantly
        if self.player.level < 3:
            template = random.choice(self.monster_templates[:2])  # Slime or Goblin
        else:
            template = random.choice(self.monster_templates)      # Any monster
            
        return Character(template["name"], template["role"], template["health"], template["attack"])

    def start_combat_arena(self, enemy):
        """Runs the turn-based combat loop until one entity falls."""
        print(f"\n⚠️ A wild {enemy.name} (HP: {enemy.max_health}, ATK: {enemy.attack_power}) emerges from the shadows!")
        
        while self.player.is_alive() and enemy.is_alive():
            print(f"\n=== {self.player.name} (HP: {self.player.current_health}/{self.player.max_health}) vs {enemy.name} (HP: {enemy.current_health}/{enemy.max_health}) ===")
            print("1. Strike with Weapon")
            print("2. Cast Healing Spell")
            action = input("Select combat action (1-2): ").strip()
            
            # --- Player Action Phase ---
            if action == "1":
                self.player.attack(enemy)
            elif action == "2":
                self.player.cast_heal()
            else:
                print("You fumbled your turn due to confusion! (Invalid selection)")
                
            # Check if the monster was defeated before letting it attack back
            if not enemy.is_alive():
                print(f"☠️ {enemy.name} has been vanquished!")
                
                # Extract rewards out of template maps matching the enemy's name string identity
                reward_xp = 20
                for item in self.monster_templates:
                    if item["name"] == enemy.name:
                        reward_xp = item["xp_reward"]
                        
                print(f"🎉 Victory! Gained +{reward_xp} Experience Points.")
                self.player.xp = self.player.xp + reward_xp
                self.player.check_level_up()
                break
                
            # --- Enemy Action Phase ---
            print("")
            enemy.attack(self.player)
            
            if not self.player.is_alive():
                print(f"💀 You were struck down by {enemy.name}... Your adventure ends here.")
                break