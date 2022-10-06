% Dataset questions

% Fisrt question
question_first('Czy produkt jest uszkodzony?').

% Question structure
% (Question, if yes, if not, if number)
question_t_f('Czy produkt jest uszkodzony?', 'Czy uszkodzenie jest natury mechanicznej?', 'Czy produkt jest niezgodny z opisem').

question_t_f('Czy uszkodzenie jest natury mechanicznej?', 'Przykro nam gwarancja tego nie obsługuje', 'Czy buty sie rozkleily?').
question_t_f('Czy buty sie rozkleily?', 'Reklamacja przyjeta', 'Twoj problem jest zbyt zlozony zadzwon do kosultanta 665 665 665').

question_t_f('Czy produkt jest niezgodny z opisem', 'Reklamacja przyjeta', 'Prosze wybrac jedna z przyczyn').
question_t_f('Czy produkt nie dotarl?', 'Zglos brak przesylki pod numerem 503 503 503', 'Czy produkt nie dotarl?').

% Multi answer question structure
% (Question, list answers)
question_choose_answer('Prosze wybrac jedna z przyczyn', ['Jakosc produktu mi nie odpowiada', 'Kolor sie nie zgadza', 'Model się nie zgadza', 'Rozmiar się nie zgadza']).
question_choose_answer('Rozmiar się nie zgadza', ['Wymien na inny romiar', 'Zwrot pieniedzy']).
question_choose_answer('Model się nie zgadza', ['Wymien na inny model', 'Zwrot pieniedzy']).
question_choose_answer('Kolor sie nie zgadza', ['Wymien na inny kolor', 'Zwrot pieniedzy']).

% answer(questione, company response, if we add something to end)
%answer('Przykro nam gwarancja tego nie obsluguje', 'Przykro nam gwarancja tego nie obsluguje?', 'N').
answer('Reklamacja przyjeta', 'Reklamacja przyjeta', 'N').
answer('Przykro nam gwarancja tego nie obsługuje', 'Przykro nam gwarancja tego nie obsługuje', 'N').
answer('Twoj problem jest zbyt zlozony zadzwon do kosultanta 665 665 665', 'Twoj problem jest zbyt zlozony zadzwon do kosultanta 665 665 665', 'N').
answer('Wymien na inny romiar', 'Wymiana przyjeta', 'N').
answer('Wymien na inny model', 'Wymiana przyjeta', 'N').
answer('Wymien na inny kolor', 'Wymiana przyjeta', 'N').
answer('Zwrot pieniedzy', 'Reklamacja przyjeta', 'N').
answer('Jakosc produktu mi nie odpowiada', 'Przykro nam gwarancja tego nie obsluguje', 'N').




%
% How to use?
% Consult files and run comand:
% start.
%


% Start function
start :-
   write('Shoe advertiser'), nl,
   write('Answer all questions with '/y/' for yes or '/n/' for no or number for multichose answer'), nl, %   clear_stored_answers,
   question_first(Question_First),
   ask_next_questions(D, Question_First).


ask_next_questions(D, Question):-
    (
        question_t_f(Question, TrueAns, FalseAns),
        ask_question(Question, t_f),
        get_answer(Ans),
        choose_question(Ans, Question, NextQuestion),
        ask_next_questions(D, NextQuestion)
    );
    (
        question_choose_answer(Question, Answers),
        ask_question(Answers, m_a),
        get_answer(Ans),
        conver_asci_to_int(Ans, Num),
        nth1(Num, Answers, Answer),
        ask_next_questions(D, Answer)
    );
    answer_question(D, Question).

choose_question(121, Question, NextQuestion):- % 121 == y
    question_t_f(Question, NextQuestion, _).

choose_question(116, Question, NextQuestion):- % 121 == t
    question_t_f(Question, NextQuestion, _).

choose_question(102, Question, NextQuestion):- % 102 == f
    question_t_f(Question, _, NextQuestion).

choose_question(110, Question, NextQuestion):- % 110 == n
    question_t_f(Question, _, NextQuestion).

answer_question(D, LastAnswer):-
    answer(LastAnswer, CmpanyAnswer, _),
    write(CmpanyAnswer).


% Ask questions

ask_question(Q, t_f) :-
    write(Q).

ask_question(Qs, m_a) :-
    show_list(Qs, 1).



% Get user answer

get_answer(Char) :-
    get(Char).    %    read(A),



conver_asci_to_int(Asci, Int):-
    Int is Asci - 48.

show_list([], N).
show_list([A|B], N) :-
  write(N), write('. '), write(A), nl,
  N1 is N + 1,
  show_list(B, N1).