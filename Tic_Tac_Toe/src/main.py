from src.game import TicTacToeGUI

def main():
    print("=========================================")
    print("🎮 INITIALIZING TURN-BASED MATRIX ENGINE")
    print("=========================================")
    print("-> Instantiating Backend Matrix State Cache")
    print("-> Spanning 3x3 Graphical Button Coordinates")
    print("-> Binding Context-Safe Command Closures")
    
    game_engine = TicTacToeGUI()
    
    game_engine.launch()

if __name__ == "__main__":
    main()