from src.game import GameWindow

def main():
    game_engine = GameWindow(width=600, height=400, block_size=20)
    
    print("=========================================")
    print("INITIALIZING REAL-TIME SNAKE GAME ENGINE ")
    print("=========================================")
    print("-> Creating Tkinter Canvas Frame Interface")
    print("-> Binding Arrow Key Mechanical Input Vectors")
    print("-> Launching Asynchronous Frame Tick Loop Pipelines")
    
    game_engine.launch()

if __name__ == "__main__":
    main()