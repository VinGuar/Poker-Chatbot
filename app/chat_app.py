from claude.claude_interface import ask_claude
from claude.prompt_builder import build_user_prompt
from claude.prompt_builder import build_user_prompt2
from app.retriever import retrieve_context
from langchain.memory import ConversationSummaryMemory
from langchain_openai import ChatOpenAI
def main():
    llm_for_memory = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo") 
    memory = ConversationSummaryMemory(llm=llm_for_memory)
    chat_summary = memory.load_memory_variables({})["history"]

    print("♠️ Welcome to PokerBot (Claude Edition)")
    while True:
        # hand = input("Hand (e.g., AKo): ")
        # position = input("Position (e.g., UTG, MP, CO): ")
        # stack = input("Stack size (e.g., 30bb): ")
        # blinds = input("Blinds (e.g., 100/200): ")
        # reads = input("Reads (e.g., BTN is loose, BB is tight): ")
        # game_type = input("Game type (e.g., MTT, cash, SNG): ")
        # flop = input("flop: ")
        # turn = input("turn: ")
        # river = input("river: ")

        # other_notes = input("Other notes: ")

        message = input("Ask away! ")

        # user_prompt = build_user_prompt(hand, position, stack, blinds, reads, game_type, flop, turn, river, other_notes)
        user_prompt2 = build_user_prompt2(message)
        context = retrieve_context(user_prompt2)
        print(context)

        system_prompt = open("prompts/base_prompt.txt").read()
        system_prompt2 = open("prompts/conversational_prompt.txt").read()

        full_prompt = f"""
            Use the following context only if applicable to help answer the user's poker question. 
            Be GTO-aware, and include exploitative adjustments if relevant. Double check what you are saying is correct.

            Context:
            {context}

            Conversation Summary:
            {chat_summary}

            ---

            User Question:
            {user_prompt2}
            """
        response = ask_claude(system_prompt2, full_prompt)
        memory.save_context({"input": user_prompt2}, {"output": response})

        print("\n🧠 Claude's Answer:\n")
        print(response)
        print("\n" + "-"*50 + "\n")

if __name__ == "__main__":
    main()
