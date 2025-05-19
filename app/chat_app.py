from claude.claude_interface import ask_claude
from claude.prompt_builder import build_user_prompt

def main():
    print("♠️ Welcome to PokerBot (Claude Edition)")
    while True:
        hand = input("Hand (e.g., AKo): ")
        position = input("Position (e.g., UTG, MP, CO): ")
        stack = input("Stack size (e.g., 30bb): ")
        blinds = input("Blinds (e.g., 100/200): ")
        reads = input("Reads (e.g., BTN is loose, BB is tight): ")
        game_type = input("Game type (e.g., MTT, cash, SNG): ")

        user_prompt = build_user_prompt(hand, position, stack, blinds, reads, game_type)
        system_prompt = open("prompts/base_prompt.txt").read()
        response = ask_claude(system_prompt, user_prompt)

        print("\n🧠 Claude's Answer:\n")
        print(response)
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()
