<h1>ДКА и минимальный ПДКА</h1>
Корневой каталог - task1
<p>Импорты: copy, __future__, pytest</p>
<p>Установить нужно pytest, pytest-cov</p>
<div>pip3 install -r requrements.txt</div>
<p>Запуск тестов из корневого каталога (task1):

python3 -m pytest --cov automates tests
</p>
<h3> Файлы </h3>
Файлы в каталоге automates соответсвуют классам:
<ol>
<li>NFA - НКА</li>
<li>OneLetterNFA - однобуквенный НКА</li>
<li>CDFA - ПДКА</li>
<li>MinCDFA - минимальный ПДКА</li>
</ol>
В каталоге tests находятся тесты и подкатолог test_files с .doa автоматами
<ol>
<li>test_nfa - построение НКА</li>
<li>test_one_letter_nfa - построение однобуквенного НКА</li>
<li>test_cdfa - построение ПДКА</li>
<li>test_min_cdfa - построение минимального ПДКА</li>
<li>test_empty - корректность поведения для пустого автомата</li>
<li>test_transformations - построения однобуквенного по НКА, ПДКА по однобуквенному, Минимального по ПДКА </li>
<li>test_not_isomorphic - Проверка (не) равенства языков</li>
</ol>

<h3>На чем тестируется:</h3>

test.doa, ans_nfa.doa, ans_olnfa.doa, ans_cdfa.doa, ans_mcdfa.doa - ввод, ожидаемый вывод для НКА, однобуквенного НКА, ПДКА и минимального ПДКА соответственно

В основном проверяются cdfa и mcdfa, так как алгоритм проще, если бы была ошибка в olnfa и nfa, она должна была бы перейти в cdfa
<ul>
<li>test1 - номер 1 из дз3</li>
<li>test2 - номер 2 из дз3</li>
<li>test3 - номер 3 из дз3</li>
<li>test4 - номер 5 из дз3</li>
<li>test5 - пустой автомат</li>



</ul>
