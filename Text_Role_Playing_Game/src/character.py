import random

class Character:
    def __init__(self, name, role, health, attack_power, xp=0, level=1):
        # Tracking core structural RPG attributes
        self.name = name
        self.role = role
        self.max_health = health
        self.current_health = health
        self.attack_power = attack_power
        self.xp = xp
        self.level = level

    def is_alive(self):
        """Returns True if character has health remaining, False otherwise."""
        return self.current_health > 0

    def take_damage(self, damage_amount):
        """Subtracts damage from current health pools, preventing negative values."""
        self.current_health = self.current_health - damage_amount
        if self.current_health < 0:
            self.current_health = 0
        print(f"💥 {self.name} took {damage_amount} damage! (Remaining HP: {self.current_health}/{self.max_health})")

    def attack(self, target_enemy):
        """Calculates variable damage variations and applies it to an enemy object."""
        # Add slight randomness to attacks (+/- 2 damage variations)
        damage_variance = random.randint(-2, 2)
        final_damage = self.attack_power + damage_variance
        
        if final_damage < 1:
            final_damage = 1  # Guarantee at least 1 minimum damage point
            
        print(f"⚔️ {self.name} swings at {target_enemy.name}!")
        target_enemy.take_damage(final_damage)
        return final_damage

    def cast_heal(self):
        """Restores a portion of health points up to max limits."""
        heal_amount = 15 + random.randint(0, 5)
        self.current_health = self.current_health + heal_amount
        if self.current_health > self.max_health:
            self.current_health = self.max_health
        print(f"💚 {self.name} cast a healing spell and recovered {heal_amount} HP! ({self.current_health}/{self.max_health})")

    def check_level_up(self):
        """Checks if accumulated XP crosses thresholds to scale stats up."""
        # Simple rule: level up every 50 XP points accumulated
        xp_needed = self.level * 50
        if self.xp >= xp_needed:
            self.xp = self.xp - xp_needed
            self.level = self.level + 1
            self.max_health = self.max_health + 15
            self.current_health = self.max_health  # Fully restore health on level up
            self.attack_power = self.attack_power + 3
            print(f"🌟🌟 LEVEL UP! {self.name} reached Level {self.level}! Max HP +15, Attack +3! 🌟🌟")
            return True
        return False

    def to_dict(self):
        """Converts stats into a clean dictionary structure for save file operations."""
        return {
            "name": self.name,
            "role": self.role,
            "max_health": self.max_health,
            "current_health": self.current_health,
            "attack_power": self.attack_power,
            "xp": self.xp,
            "level": self.level
        }