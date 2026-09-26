-spec get_hint(Secret :: unicode:unicode_binary(),
               Guess :: unicode:unicode_binary()) -> unicode:unicode_binary().
get_hint(Secret, Guess) ->
    SecretList = binary_to_list(Secret),
    GuessList = binary_to_list(Guess),
    {Bulls, SecretCount, GuessCount} = count_bulls(
        SecretList, GuessList, 0, #{}, #{}),
    Cows = count_cows(maps:to_list(SecretCount), GuessCount, 0),
    list_to_binary(io_lib:format("~pA~pB", [Bulls, Cows])).

count_bulls([], [], Bulls, SecretCount, GuessCount) ->
    {Bulls, SecretCount, GuessCount};

count_bulls([S | ST], [G | GT], Bulls, SecretCount, GuessCount) ->
    case S =:= G of
        true ->
            count_bulls(ST, GT, Bulls + 1, SecretCount, GuessCount);
        false ->
            NewSecretCount = maps:update_with(
                S, fun(N) -> N + 1 end, 1, SecretCount),
            NewGuessCount = maps:update_with(
                G, fun(N) -> N + 1 end, 1, GuessCount),
            count_bulls(ST, GT, Bulls, NewSecretCount, NewGuessCount)
    end.

count_cows([], _GuessCount, Cows) ->
    Cows;

count_cows([{Digit, SecretN} | Rest], GuessCount, Cows) ->
    GuessN = maps:get(Digit, GuessCount, 0),
    count_cows(Rest, GuessCount, Cows + min(SecretN, GuessN)).
