line_1 = input().split()
line_2 = input().split()
line_3 = input().split()

line_1 = [int(x) for x in line_1]
line_2 = [int(x) for x in line_2]
line_3 = [int(x) for x in line_3]

player_1_won = False
player_2_won = False

column_1 = [line_1[0], line_2[0], line_3[0]]
column_2 = [line_1[1], line_2[1], line_3[1]]
column_3 = [line_1[2], line_2[2], line_3[2]]

diagonal_1 = [line_1[0], line_2[1], line_3[2]]
diagonal_2 = [line_1[2], line_2[1], line_3[0]]

if 6 in [sum(line_1), sum(line_2), sum(line_3),
         sum(column_1), sum(column_2), sum(column_3),
         sum(diagonal_1), sum(diagonal_2)]:
    player_2_won = True
if (1, 3) in [(len(set(line_1)), sum(line_1)),
                (len(set(line_2)), sum(line_2)),
                (len(set(line_3)), sum(line_3)),
                (len(set(column_1)), sum(column_1)),
                (len(set(column_2)), sum(column_2)),
                (len(set(column_3)), sum(column_3)),
                (len(set(diagonal_1)), sum(diagonal_1)),
                (len(set(diagonal_2)), sum(diagonal_2))]:
    player_1_won = True

if player_2_won:
    print("Second player won")
elif player_1_won:
    print("First player won")
elif not player_1_won and not player_2_won:
    print("Draw!")