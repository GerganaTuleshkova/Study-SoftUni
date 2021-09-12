def longest_symbol_subsequent(text, symbol):
    longest_subsequent = 0
    for i in range(len(text)):
        current_ch = text[i]
        current_subsequent = 0
        if current_ch == symbol:
            current_subsequent += 1

            for j in range(i + 1, len(text)):
                next_ch = text[j]

                if next_ch == symbol:
                    current_subsequent += 1
                else:
                    if current_subsequent > longest_subsequent:
                        longest_subsequent = current_subsequent
                    break
                if current_subsequent > longest_subsequent:
                    longest_subsequent = current_subsequent

    return longest_subsequent



tickets = [x.strip() for x in input().split(", ")]

winning_combo_at = "@" * 6
winning_combo_hash = "#" * 6
winning_combo_dollar = "$" * 6
winning_combo_circumflex = "^" * 6

for ticket in tickets:
    if not len(ticket) == 20:
        print("invalid ticket")
        continue

    left_half = ticket[:10]
    right_half = ticket[10:]

    match_symbol = ""

    if winning_combo_at in left_half and winning_combo_at in right_half:
        match_symbol = "@"
    elif winning_combo_hash in left_half and winning_combo_hash in right_half:
        match_symbol = "#"
    elif winning_combo_dollar in left_half and winning_combo_dollar in right_half:
        match_symbol = "$"
    elif winning_combo_circumflex in left_half and winning_combo_circumflex in right_half:
        match_symbol = "^"
    else:
        print(f'ticket "{ticket}" - no match')
        continue

    left_matches = longest_symbol_subsequent(left_half, match_symbol)
    right_matches = longest_symbol_subsequent(right_half, match_symbol)

    min_matches_count = min(left_matches, right_matches)

    if min_matches_count == 10:
        print(f'ticket "{ticket}" - {min_matches_count}{match_symbol} Jackpot!')
    else:
        print(f'ticket "{ticket}" - {min_matches_count}{match_symbol}')