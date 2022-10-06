
%Fakty taka ala bazka
matka(barbara,zaneta).
matka(barbara,kamil).
matka(aniela,roza).
matka(sabina,krzysztof).
matka(sabina,dorota).
matka(sabina,bogusia).
matka(roza,barbara).
matka(roza,wojtek).
matka(roza,piotrek).
matka(bogusia,daria).
matka(dorota, pawel).
matka(piotrek, simona).
matka(piotrek, claudia).
ojciec(stanislaw,barbara).
ojciec(stanislaw,wojtek).
ojciec(stanislaw,piotrek).
ojciec(krzysztof,zaneta).
ojciec(krzysztof,kamil).
ojciec(maciej,roza).
ojciec(juzef,krzysztof).
ojciec(juzef,dorota).
ojciec(juzef,bogusia).



%Reguly takie ala funkcje


kuzyn(Ja,Kuzyn):-
    ojciec(F,Kuzyn),
    ojciec(Z,F),
    ojciec(Z,X),
    ojciec(X,Ja).

babcia(Dziecko,Babcia):-
    matka(Babcia,Y),
    matka(Y,Dziecko).
babcia(Dziecko,Babcia):-
    matka(Babcia,Y),
    ojciec(Y,Dziecko).


dziadek(Dziecko,Y):-
    ojciec(Y,Z),
    ojciec(Z,Dziecko).
dziadek(Dziecko,Y):-
    ojciec(Y,Z),
    matka(Z,Dziecko).


dziadkowie(Dziecko,Ojca,Matki):-
    ojciec(Ojca, X),
    ojciec(X, Dziecko),
    ojciec(Matki, Y),
    matka(Y, Dziecko).

moz(M, Z):-
    matka(M, X),
    ojciec(Z, X).


rodzic(Rodzic, Dziecko):-
    ojciec(Rodzic, Dziecko);
    matka(Rodzic, Dziecko).


listadzieci(Rodzic,ListaDz):-
    findall(Dziecko,rodzic(Rodzic,Dziecko),ListaDz).




%zlicz([],0).

%zlicz([_|Lista1],Liczba):-
 %  zlicz(Lista1, Liczba1),
 % Liczba is Liczba1 +  1.


zliczDzieci(Rodzic, Liczba):-
    listadzieci(Rodzic, Lista),
    zlicz(Lista,Liczba).



listaDziadkow(Wnuczek, Lista):-
    findall(Dziadek, dziadkowie(Dziadek, Wnuczek), Lista).


dziadkowie(Dziadek, Wnuk):-
    ojciec(Dziadek, Ojciec),
    ojciec(Ojciec, Wnuk);

    matka(Dziadek, Ojciec2),
    ojciec(Ojciec2, Wnuk);

    ojciec(Dziadek, Matki2),
    matka(Matki2, Wnuk);

    matka(Dziadek, Matka),
    matka(Matka, Wnuk).






rodzenstwo(Ja, Rodz):-
    ojciec(Ojciec, Rodz),
    ojciec(Ojciec, Ja);
    matka(Matka, Rodz),
    matka(Matka, Ja).

rodzice(Ja, Rodzi):-
    ojciec(Rodzi, Ja);
    matka(Rodzi, Ja).


kuzyniset(Kuzyn, List):-
    setof(Kuzyni, kuzyni(Kuzyn, Kuzyni), List).

kuzyni(Kuzyn, Kuzyni):-
    ojciec(Rodz, Kuzyni),
    rodzenstwo(Rodzice, Rodz),
    rodzice(Kuzyn, Rodzice);

    matka(Rodz, Kuzyni),
    rodzenstwo(Rodzice, Rodz),
    rodzice(Kuzyn, Rodzice).

l_kuzynow(Kuzyn, Liczba):-
    kuzyniset(Kuzyn, List),
    policz(List, Liczba).


policz([], 0).
policz([_|Lista], Liczba):-
    policz(Lista, Liczba1),
    Liczba is Liczba1 + 1.


rodzice(Ja, Rodzice):-
    matka(Rodzice, Ja);
    ojciec(Rodzice, Ja).

krewni(Ja, Krewni):-
       rodzice(Ja, Krewni).
krewni(Ja, Krewni):-
    rodzice(Ja, Rodz),
    krewni(Rodz, Krewni).

krewni_set(Ja, Set):-
    setof(Krewni, krewni(Ja, Krewni), Set).


























potomek(Ja, Potomkowie):-
    rodzic(Ja, Potomkowie).


potomek(Ja, Potomkowie):-
    rodzic(Ja, Dziecko),
    potomek(Dziecko, Potomkowie).

potomek_lista(Ja, Lista):-
    findall(Potomkowie, potomek(Ja, Potomkowie), Lista).


wszyscy(X):-
    ojciec(X, Y);
    ojciec(Z, X);
    matka(X, C);
    matka(V, X).

wszyscy_set(Lista):-
    setof(X, wszyscy(X), Lista).










rodzice_t(Syn, Rodz):-
    ojciec(Rodz, Syn);
    matka(Rodz, Syn).

dzieci_t(Rodz, Dzieci):-
    ojciec(Rodz, Dzieci);
    matka(Rodz, Dzieci).

rodzenstwo_rodz(Syn, Set):-
    rodzice_t(Syn, Rodz),
    rodzice_t(Rodz, Dziadkowie),
    dzieci_t(Dziadkowie, Rodzenstwo_rodz).


rodzenstwo_rodz_set(Syn, Set):-
    setof(Rodzenstwo_rodz, rodzenstwo_rodz(Syn, Rodzenstwo_rodz), Set).





ojcowie_krewni(Syn, Ojcowie):-
    ojciec(Ojcowie, Syn).

ojcowie_krewni(Syn, Ojcowie):-
    ojciec(Ojciec, Syn),
    ojcowie_krewni(Ojciec, Ojcowie).















matki_krewne(Syn, Matka):-
    matka(Matka, Syn).

matki_krewne(Syn, Matki):-
    matka(Matka, Syn),
    matki_krewne(Matka, Matki).

matki_krewne_set(Syn, Set):-
    setof(Matki, matki_krewne(Syn, Matki), Set).


zliczanie_matek(Syn, L):-
    matki_krewne_set(Syn, Set),
    zlicz_m(Set, L).

zlicz_m([], 0).
zlicz_m([_|Set], L):-
    zlicz_m(Set, L1),
    L is L1 + 1.















