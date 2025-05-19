def build_user_prompt(hand, position, stack, blinds, reads, game_type):
    return f"""
Hand: {hand}
Position: {position}
Stack: {stack}
Blinds: {blinds}
Reads: {reads}
Game Type: {game_type}

What should I do?
"""
