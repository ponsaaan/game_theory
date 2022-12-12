import regret_matching

MONICA = 0
GARY = 1
NUM_ITERATIONS = 1000


def main():
    game = [
        [[0, 0], [-1, 1], [1, -1]],
        [[1, -1], [0, 0], [-1, 1]],
        [[-1, 1], [1, -1], [0, 0]]
    ]

    regret_matching.Player.init_game(regret_matching.Player, game)

    # regret_matching
    monica_mixed_strategy = []
    monica = regret_matching.Player(MONICA)
    # gary_initial_strategy = np.zeros(21)
    # gary_initial_strategy[13] = 1
    gary = regret_matching.Player(GARY)
    for _ in range(NUM_ITERATIONS):
        _, played_pure_strategies = monica.simulate_game([gary])
        monica.update_cum_regret(played_pure_strategies)
        monica.update_strategy()
        monica_mixed_strategy.append(monica.cum_strategy / monica.num_played)

        _, played_pure_strategies = gary.simulate_game([monica])
        gary.update_cum_regret(played_pure_strategies)
        gary.update_strategy()

    print(f"Monica's converged strategy is {monica.cum_strategy / monica.num_played}")
    print(f"Gary's converged strategy is {gary.cum_strategy / gary.num_played}")
    # np.save("rsp_result", np.array(monica_mixed_strategy))


if __name__ == "__main__":
    main()
