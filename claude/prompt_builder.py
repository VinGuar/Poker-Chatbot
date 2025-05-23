def build_user_prompt(hand, position, stack, blinds, reads, game_type, flop, turn, river, other_notes):
    return f"""
Hand: {hand}
Position: {position}
Stack: {stack}
Blinds: {blinds}
Reads: {reads}
Game Type: {game_type}
Notes: {game_type}
flop: {flop}
turn: {turn}
river: {river}
other_notes: {other_notes}
Analyze this for me?
"""

def build_user_prompt2(message):
    return f"""
Question: {message}

"""
